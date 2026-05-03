# TTS — Prononciation & Prosodie : Référence complète

> Dernière mise à jour : 2026-05-03  
> Moteur : Cartesia **sonic-3-2026-01-12**  
> Locale EN : voix `CARTESIA_VOICE_ID`, FR : `CARTESIA_VOICE_ID_FR`

---

## 1. Architecture du pipeline TTS

```
Script brut
  → normalize_pronunciations()        # table statique _SPELL_OUT_COMMON + _SPELL_OUT_FR_OVERRIDES
  → _auto_spell_unknown_acronyms()    # filet dynamique : [A-Z]{3-5} restants
  → _replace_dashes()                 # tirets cadratins/demi-cadratins → espace
  → _strip_trailing_pause_tokens()    # ellipses finales → '.'
  → split_script()                    # découpage en chunks (max chars)
  → _render_chunks_crossfade()        # rendu Cartesia par chunk + crossfade
```

---

## 2. Règles de prosodie et régulation du flux

### 2.1 Mode de rendu — `tts_mode: "chunks"`

| Paramètre | EN | FR |
|---|---|---|
| `tts_mode` | `chunks` | `chunks` |
| `tts_speed` | 0.94 | 0.85 |
| `tts_emotion` | `Enthusiastic` | `Enthusiastic` |
| `tts_chunk_max_chars` | 1 400 | 1 400 |
| `tts_chunk_crossfade_ms` | **200** | **200** |
| `CARTESIA_MODEL_ID` | `sonic-3-2026-01-12` | `sonic-3-2026-01-12` |

**Mode `chunks`** : chaque paragraphe-bloc est rendu dans une session WebSocket indépendante, puis les segments sont concaténés avec un crossfade. Cela évite la dégradation de qualité (bruit, instabilité de volume) qu'on observe après ~2 minutes dans une session unique continue.

**Mode `websocket`** *(non utilisé en prod)* : session unique `context_id` avec `continue=true`. Abandonné car la qualité se dégrade au-delà de ~120 s.

### 2.2 Trim des silences en bord de chunk

```python
SILENCE_THRESH_DB = -40.0   # seuil de détection du silence
KEEP_EDGE_MS      = 200     # ms de silence conservés de chaque côté
```

Cartesia ajoute un silence de "fin de phrase" (~400–800 ms) à la fin de chaque session. Sans trim, les silences s'accumulent et donnent l'impression que le podcast s'arrête entre chaque bloc. Le trim réduit ce silence à 200 ms, ce qui laisse suffisamment de matière pour le crossfade sans couper de parole réelle.

### 2.3 Crossfade inter-chunk

```
crossfade_ms = 200 ms
```

Les 200 dernières ms du chunk N et les 200 premières ms du chunk N+1 sont fondues ensemble (amplitude linéaire). Cela masque tout artefact de jointure (claquement, micro-silence). La valeur de `KEEP_EDGE_MS` est alignée sur `crossfade_ms` pour que la zone de fondu porte sur du silence résiduel, jamais sur de la parole réelle.

### 2.4 Découpage en chunks — `split_script()`

- Les paragraphes sont joints avec un **espace** (pas de `\n`) à l'intérieur d'un chunk.
- Raison : un `\n` dans le texte envoyé à Cartesia déclenche une pause de 500 ms–2 s (pause de paragraphe interne au modèle). En joignant avec un espace, on élimine ces pauses non souhaitées à l'intérieur d'un segment.
- La limite `tts_chunk_max_chars = 1 400` réduit les artefacts d'accélération au démarrage de session (Cartesia "chauffe" les 150–200 premières ms).

### 2.5 Remplacement des tirets — `_replace_dashes()`

| Motif | Remplacement | Raison |
|---|---|---|
| `—` (cadratin) | espace | pause Cartesia 500–800 ms |
| `–` (demi-cadratin) | espace | idem |
| ` - ` (tiret entouré d'espaces) | espace | idem |
| `GPT-5` → `GPT 5` | espace | tiret de numéro de version |
| `claude-3` → `claude 3` | espace | minuscule→chiffre |

Les tirets dans les composés français (multi-étapes, vision-langage) sont **conservés** car ils connectent minuscule→minuscule, exclus par la regex.

### 2.6 Suppression des tokens de pause finale — `_strip_trailing_pause_tokens()`

Cartesia interprète une ellipse finale (`...`) comme un signal d'attente et étire le silence de clôture de 1–3 s. Tout token `...` ou séquence `.` flottante en fin de texte est remplacé par un simple `.`.

### 2.7 Emotion Cartesia sonic-3

**Format** : chaîne unique (`str`), pas de tableau. Les valeurs valides du modèle sonic-3 sont des énumérations prédéfinies :

> `Enthusiastic` · `Excited` · `Curious` · `Confident` · `Content` · `Calm` · `Neutral` · `Sad` · `Anxious`

**Configuration actuelle** : `"Enthusiastic"` (EN et FR).

L'ancien format sonic-2 (`["positivity:high", "curiosity:low"]`) produisait des erreurs HTTP 400 — il n'est pas supporté par sonic-3.

### 2.8 Format compact des acronymes en FR — `_compact_fr_dots()`

En français, Cartesia interprète chaque espace entre les lettres d'un sigle comme une pause audible. `L. L. M.` → pause × 2 trop longues.

La fonction `_compact_fr_dots()` transforme automatiquement :
```
L. L. M.  →  L.L.M.
A. P. I.  →  A.P.I.
```
Exception : les mots de plus d'une lettre (`R. et D.`) sont préservés.

### 2.9 Filet automatique — `_auto_spell_unknown_acronyms()`

Après la table statique, tout token `\b[A-Z]{3-5}\b` restant est épelé lettre par lettre avec des points : `ABCD` → `A. B. C. D.` (EN) ou `A.B.C.D.` (FR).

Les tokens catchés sont enregistrés dans `data/state/acronyms_seen_{locale}.json` pour revue opérateur. Les entrées fréquentes doivent être promus dans la table statique.

---

## 3. Table des acronymes — EN (`_SPELL_OUT_COMMON`)

> La table EN est également la base FR (avec application automatique du format compact). Les surcharges FR spécifiques sont en §4.

### 3.1 Entreprises / fondeurs de puces

| Token | Rendu EN | Note |
|---|---|---|
| `TSMC` | T. S. M. C. | |
| `AMD` | A. M. D. | |
| `IBM` | I. B. M. | |
| `AWS` | A. W. S. | |
| `GCP` | G. C. P. | aussi Google Cloud Platform |
| `HPE` | H. P. E. | |
| `SAP` | S. A. P. | |
| `SMIC` | S. M. I. C. | Semiconductor Manufacturing Intl |
| `ASML` | A. S. M. L. | |
| `STMicro` | S. T. Micro | |
| `BMW` | B. M. W. | ★ prod |
| `ZTE` | Z. T. E. | ★ prod — télécoms chinois |
| `NTT` | N. T. T. | ★ prod — télécoms japonais |
| `PLDT` | P. L. D. T. | ★ prod — télécoms Philippines |
| `CNBC` | C. N. B. C. | ★ prod |
| `BBC` | B. B. C. | ★ prod |

### 3.2 Modèles / IA / entraînement

| Token | Rendu EN | Note |
|---|---|---|
| `GPT` | G. P. T. | |
| `BERT` | Burt | prononcé comme un mot |
| `LLM` | L. L. M. | |
| `LLMs` | L. L. M. s | |
| `SLM` | S. L. M. | |
| `SLMs` | S. L. M. s | |
| `LLaMA` | lama | |
| `LoRA` | lora | |
| `QLoRA` | Q. lora | |
| `MoE` | M. O. E. | |
| `RAG` | rag | mot |
| `RLHF` | R. L. H. F. | |
| `DPO` | D. P. O. | |
| `SFT` | S. F. T. | |
| `PEFT` | P. E. F. T. | |
| `CoT` | C. o. T. | Chain of Thought |
| `ToT` | T. o. T. | Tree of Thought |
| `FLOPs` | flops | mot |
| `FLOPS` | flops | mot |
| `SOTA` | sota | mot |
| `OOD` | O. O. D. | |
| `GPTQ` | G. P. T. Q. | ★ prod — quantisation |
| `GLM` | G. L. M. | ★ prod — famille de modèles |

### 3.3 Benchmarks

| Token | Rendu EN | Note |
|---|---|---|
| `MMLU` | M. M. L. U. | |
| `GSM8K` | G. S. M. 8. K. | |
| `HellaSwag` | hella-swag | |
| `HumanEval` | Human-Eval | |
| `BBH` | B. B. H. | |
| `GPQA` | G. P. Q. A. | |
| `MATH` | math | benchmark / mot |
| `SWE-bench` | swee-bench | |
| `ARC` | arc | mot |
| `AIME` | aim | mot |

### 3.4 Calcul / infra

| Token | Rendu EN | Note |
|---|---|---|
| `GPU` / `GPUs` | G. P. U. / G. P. U. s | |
| `CPU` / `CPUs` | C. P. U. / C. P. U. s | |
| `TPU` / `TPUs` | T. P. U. / T. P. U. s | |
| `NPU` / `NPUs` | N. P. U. / N. P. U. s | |
| `HPC` | H. P. C. | |
| `API` / `APIs` | A. P. I. / A. P. I. s | |
| `MCP` | M. C. P. | Model Context Protocol |
| `SDK` / `SDKs` | S. D. K. / S. D. K. s | |
| `CLI` | C. L. I. | |
| `IDE` | I. D. E. | |
| `VPN` | V. P. N. | |
| `ASIC` / `ASICs` | ay-sick / ay-sicks | mot |
| `FPGA` / `FPGAs` | F. P. G. A. / F. P. G. A. s | |
| `SSD` / `SSDs` | S. S. D. / S. S. D. s | |
| `HBM` | H. B. M. | |
| `VRAM` | V. R. A. M. | |
| `DRAM` | D. R. A. M. | |
| `CUDA` | koo-da | mot |
| `ROCm` | rock-em | |
| `LPDDR` | L. P. D. D. R. | ★ prod — mémoire |
| `EUV` | E. U. V. | ★ prod — lithographie |
| `RTX` | R. T. X. | ★ prod — GPU Nvidia |
| `RDMA` | R. D. M. A. | ★ prod — accès mémoire direct |
| `DSL` | D. S. L. | ★ prod |
| `MTIA` | M. T. I. A. | ★ prod — Meta Training & Inference Accelerator |
| `RISC` | risk | ★ prod — prononcé comme un mot |

### 3.5 Titres / business

| Token | Rendu EN | Note |
|---|---|---|
| `CEO` | C. E. O. | |
| `CTO` | C. T. O. | |
| `CFO` | C. F. O. | |
| `COO` | C. O. O. | |
| `CIO` | C. I. O. | |
| `CISO` | C. I. S. O. | |
| `IPO` / `IPOs` | I. P. O. / I. P. O. s | |
| `M&A` | M. and A. | |
| `VC` / `VCs` | V. C. / V. C. s | |
| `ROI` | R. O. I. | |
| `KPI` / `KPIs` | K. P. I. / K. P. I. s | |
| `OKR` / `OKRs` | O. K. R. / O. K. R. s | |
| `EBITDA` | ee-bit-da | mot |
| `OPEX` | op-ex | |
| `CAPEX` | cap-ex | |
| `GAAP` | gap | mot |
| `CAGR` | cay-ger | |
| `ARR` | A. R. R. | Annual Recurring Revenue |
| `WPP` | W. P. P. | ★ prod — holding pub |
| `PLC` | P. L. C. | ★ prod — statut juridique UK |
| `SMB` | S. M. B. | ★ prod — PME ou protocole réseau |

### 3.6 Finance / marchés

| Token | Rendu EN | Note |
|---|---|---|
| `GDP` | G. D. P. | |
| `CPI` | C. P. I. | |
| `PPI` | P. P. I. | |
| `PMI` | P. M. I. | |
| `LIBOR` | lie-bore | |
| `SOFR` | so-fer | |
| `NASDAQ` | naz-dak | |
| `FTSE` | foot-see | |
| `ETF` / `ETFs` | E. T. F. / E. T. F. s | |
| `REIT` / `REITs` | reet / reets | mot |
| `SPAC` / `SPACs` | spack / spacks | mot |
| `WTI` | W. T. I. | ★ prod — pétrole brut |
| `IRS` | I. R. S. | ★ prod (4×EN) |
| `IDC` | I. D. C. | ★ prod (3×EN) |

### 3.7 Régulateurs / institutions

| Token | Rendu EN | Note |
|---|---|---|
| `SEC` | S. E. C. | |
| `FTC` | F. T. C. | |
| `FDA` | F. D. A. | |
| `FOMC` | F. O. M. C. | |
| `ECB` | E. C. B. | |
| `IMF` | I. M. F. | |
| `WTO` | W. T. O. | |
| `OECD` | O. E. C. D. | |
| `NIST` | nist | |
| `GDPR` | G. D. P. R. | |
| `HIPAA` | hip-ah | |
| `FINRA` | fin-ra | |
| `HMRC` | H. M. R. C. | ★ prod — fisc UK |
| `NDRC` | N. D. R. C. | ★ prod — régulateur chinois |
| `APRA` | A. P. R. A. | ★ prod — régulateur australien |
| `NSA` | N. S. A. | ★ prod |
| `AISI` | A. I. S. I. | ★ prod — AI Safety Institute |
| `IEEE` | I. E. E. E. | ★ prod — organisme de standards |
| `INRIA` | in-ria | ★ prod — institut de recherche FR |
| `CAICT` | C. A. I. C. T. | ★ prod — recherche télécoms CN |
| `EDA` | E. D. A. | ★ prod — Electronic Design Automation |
| `DSO` | D. S. O. | ★ prod |
| `ADS` | A. D. S. | ★ prod |
| `JTC` | J. T. C. | ★ prod |
| `OPC` | O. P. C. | ★ prod |
| `AMI` | A. M. I. | ★ prod (6×FR, 2×EN) |
| `COVID` | covid | ★ prod — prononcé comme un mot |
| `CTI` | C. T. I. | ★ prod — Cyber Threat Intelligence |
| `ICU` | I. C. U. | ★ prod — unité de soins intensifs |
| `SWE` | S. W. E. | ★ prod |
| `SOP` | S. O. P. | ★ prod — Standard Operating Procedure |

### 3.8 Géographies

| Token | Rendu EN | Note |
|---|---|---|
| `USA` | U. S. A. | |
| `US` | U. S. | |
| `EU` | E. U. | |
| `UK` | U. K. | |
| `UAE` | U. A. E. | EN ; FR : voir §4 |
| `NATO` | NATO | mot |
| `APAC` | A. PAC. | |
| `EMEA` | E. M. E. A. | |
| `LATAM` | LA-tam | |
| `ASEAN` | AS-ee-an | |
| `BRICS` | bricks | mot |
| `MENA` | mee-na | mot |
| `GCC` | G. C. C. | Gulf Cooperation Council |

### 3.9 Cybersécurité

| Token | Rendu EN | Note |
|---|---|---|
| `SSO` | S. S. O. | |
| `MFA` | M. F. A. | |
| `2FA` | two-F. A. | |
| `TLS` | T. L. S. | |
| `CVE` / `CVEs` | C. V. E. / C. V. E. s | |
| `OWASP` | oh-wasp | |
| `EDR` | E. D. R. | |
| `SIEM` | seem | mot |
| `SOC` | sock | mot |
| `DDoS` | D. dos | |
| `SAML` | sam-el | |
| `JWT` | J. W. T. | |

### 3.10 Cloud / réseau

| Token | Rendu EN | Note |
|---|---|---|
| `S3` | S. three | |
| `EC2` | E. C. two | |
| `CDN` | C. D. N. | |
| `DNS` | D. N. S. | |
| `VPC` | V. P. C. | |
| `K8s` | kay-eight-ess | |
| `CI/CD` | see-eye-slash-see-dee | |

### 3.11 IA architectures / entraînement étendu

| Token | Rendu EN | Note |
|---|---|---|
| `GAN` / `GANs` | gan / gans | mots |
| `CNN` / `CNNs` | C. N. N. / C. N. N. s | |
| `LSTM` | L. S. T. M. | |
| `PPO` | P. P. O. | |
| `GRPO` | G. R. P. O. | |
| `ViT` | V. I. T. | |
| `CLIP` | clip | mot |
| `NeRF` | nerf | mot |
| `INT8` | int-eight | |
| `INT4` | int-four | |
| `FP16` | F. P. sixteen | |
| `BF16` | B. F. sixteen | |
| `TFLOP` | tee-flop | |
| `NVLink` | N. V. L. I. N. K. | |
| `CXL` | C. X. L. | |

### 3.12 Formats / licences / web

| Token | Rendu EN | Note |
|---|---|---|
| `JSON` | jay-son | |
| `YAML` | yamel | |
| `SQL` | sequel | |
| `NoSQL` | no-sequel | |
| `PDF` / `PDFs` | P. D. F. / P. D. F. s | |
| `GIF` | jiff | |
| `JPEG` | jay-peg | |
| `WASM` | wazm | |
| `MIT` | M. I. T. | licence |
| `AGPL` | A. G. P. L. | |
| `BSD` | B. S. D. | |

### 3.13 Recherche / conférences

| Token | Rendu EN | Note |
|---|---|---|
| `arXiv` | ar-kive | |
| `LaTeX` | Lay-Tech | |
| `NeurIPS` | noor-ips | |
| `ICML` | I. C. M. L. | |
| `ICLR` | I. C. L. R. | |
| `AAAI` | triple-A. I. | |
| `FAISS` | fais | mot |

### 3.14 Produits / marques AI

| Token | Rendu EN | Note |
|---|---|---|
| `OpenAI` | Open A. I. | |
| `NVIDIA` | en-vidia | |
| `DeepSeek` | Deep-Seek | |
| `ChatGPT` | Chat G. P. T. | |
| `Copilot` | Co-pilot | |
| `PyTorch` | Pie-Torch | |
| `TensorFlow` | Tensor-Flow | |
| `JAX` | jacks | |
| `vLLM` | V. L. L. M. | |
| `YOLO` | yo-loh | mot |
| `CLIP` | clip | mot |

### 3.15 Formats numériques et acronymes quantisation

| Token | Rendu EN | Note |
|---|---|---|
| `FP8` | F. P. eight | |
| `FP16` | F. P. sixteen | |
| `BF16` | B. F. sixteen | |
| `FP32` | F. P. thirty-two | |
| `INT8` | int-eight | mot |
| `INT4` | int-four | mot |
| `GPTQ` | G. P. T. Q. | ★ prod |

---

## 4. Surcharges FR (`_SPELL_OUT_FR_OVERRIDES`)

> Ces entrées **remplacent** la version EN (ou ajoutent des tokens inexistants en EN). Le format compact (sans espaces) est appliqué automatiquement à toute la table FR.

### 4.1 IA / ML core

| Token | Rendu FR | Note |
|---|---|---|
| `AI` | AI | laissé nu — Cartesia FR prononce "aï" naturellement |
| `OpenAI` | OpenAI | idem |
| `LLM` | L.L.M. | |
| `LLMs` | L.L.M.s | |
| `GPT` | G. P. T. | espace conservé (3 lettres, pause naturelle) |
| `AGI` | A.G.I. | |
| `NLP` | N.L.P. | |
| `RLHF` | R.L.H.F. | |
| `BERT` | Beurt | phonétique FR |

### 4.2 Infra / APIs

| Token | Rendu FR | Note |
|---|---|---|
| `API` | A.P.I. | |
| `APIs` | A.P.I.s | |
| `MCP` | M.C.P. | |
| `SDK` / `SDKs` | S.D.K. / S.D.K.s | |
| `CLI` | C.L.I. | |
| `IDE` | I.D.E. | |
| `VPN` | V.P.N. | |

### 4.3 Hardware

| Token | Rendu FR | |
|---|---|---|
| `GPU` / `GPUs` | G.P.U. / G.P.U.s | |
| `CPU` / `CPUs` | C.P.U. / C.P.U.s | |
| `TPU` / `TPUs` | T.P.U. / T.P.U.s | |
| `NPU` / `NPUs` | N.P.U. / N.P.U.s | |
| `HPC` | H.P.C. | |
| `HBM` | H.B.M. | |
| `VRAM` | V.R.A.M. | |
| `DRAM` | D.R.A.M. | |
| `FPGA` / `FPGAs` | F.P.G.A. / F.P.G.A.s | |

### 4.4 Titres / organisation

| Token | Rendu FR | Note |
|---|---|---|
| `CEO` | C. E. O. | espace conservé — PDG en FR mais CEO courant |
| `CTO` | C.T.O. | |
| `CFO` | C.F.O. | |
| `IPO` / `IPOs` | I.P.O. / I.P.O.s | |
| `ROI` | R.O.I. | |
| `KPI` / `KPIs` | K.P.I. / K.P.I.s | |
| `OKR` / `OKRs` | O.K.R. / O.K.R.s | |
| `PDG` | P. D. G. | Président-directeur général |
| `DG` | D. G. | |
| `DSI` | D. S. I. | Directeur des SI |
| `PME` | P. M. E. | |
| `TPE` | T. P. E. | |

### 4.5 Finance FR

| Token | Rendu FR | Note |
|---|---|---|
| `GDP` | G.D.P. | |
| `CPI` | C.P.I. | |
| `PIB` | P.I.B. | = GDP en français |
| `RGPD` | R.G.P.D. | = GDPR |
| `ONU` | O.N.U. | |
| `OTAN` | OTAN | prononcé comme un mot |
| `GAFAM` | GAFAM | idem |
| `R&D` | R. et D. | Recherche et Développement |

### 4.6 Spécificités FR — acronymes géographiques

| Token | Rendu FR | Note |
|---|---|---|
| `EAU` | eau | ★ **Critique** — Émirats arabes unis en FR. Sans cette override, auto-spell produit "E.A.U." au lieu du mot naturel "oh". |

### 4.7 Benchmarks / datasets FR

| Token | Rendu FR | Note |
|---|---|---|
| `MMLU` | M.M.L.U. | |
| `GPQA` | G.P.Q.A. | |
| `BBH` | B.B.H. | |
| `A2A` | a-deux-a | |
| `YOLO` | yo-lo | |
| `SQuAD` | skouade | |
| `GLUE` | glou | |
| `COCO` | ko-ko | |

### 4.8 Agents / Orchestration FR

| Token | Rendu FR | Note |
|---|---|---|
| `RPA` | èr-pé-a | |
| `LangChain` | langue-chain | |
| `LlamaIndex` | lama index | |
| `AutoGen` | auto-jène | |
| `CrewAI` | crew é-aï | |

### 4.9 Gouvernance / sécurité FR

| Token | Rendu FR | Note |
|---|---|---|
| `EU AI Act` | i-ou é-aï acte | |
| `AI TRiSM` | é-aï trisme | |
| `MITRE ATT&CK` | maï-teur attaque | |
| `ISO/IEC 42001` | i-zo barre i-e-c quarante-deux zéro un | |

### 4.10 Hardware / compute FR

| Token | Rendu FR | Note |
|---|---|---|
| `HBM2` | ache-bé-èm-deux | |
| `HBM3` | ache-bé-èm-trois | |
| `Triton` | traï-ton | |
| `cuDNN` | kou-dé-èn-èn | |
| `OpenVINO` | open-vi-no | |

### 4.11 Formats / MLOps FR

| Token | Rendu FR | Note |
|---|---|---|
| `K8s` | ka-huit-ès | |
| `CI/CD` | cé-i-barre oblique-cé-dé | |
| `BM25` | bé-èm-deux-cinq | |
| `HNSW` | ache-èn-ès-double-vé | |
| `TF-IDF` | té-èf-tiret-i-dé-èf | |
| `MP3` | èm-pé-trois | |
| `STT` | ès-té-té | |
| `Parquet` | parquet | |
| `Apache-2.0` | apache deux point zéro | |

---

## 5. Tokens non épelés — `_AUTO_SPELL_SKIP`

Ces tokens ressemblent à des acronymes (tout caps, 3–5 lettres) mais **doivent être lus comme des mots** par le TTS. Ils sont exclus du filet automatique.

| Token | Raison |
|---|---|
| `NATO` | mot (prononcé "nay-toh") |
| `NASA` | mot |
| `FAISS` | mot (Facebook AI Similarity Search) |
| `SWIFT` | mot |
| `OPEC` | mot |
| `OTAN` | mot (FR pour NATO) |
| `DARPA` | mot |
| `BAFIN` | mot |
| `GAFAM` | mot |
| `MATH` / `MATHS` | mot |
| `BRICS` | mot |
| `ASEAN` | mot |
| `NAFTA` | mot |
| `MENA` | mot |
| `BREEAM` | mot |
| `JOLTS` | mot |
| `ESOP` | mot (ee-sop) |
| `SWOT` | mot |
| `TOWS` | mot |
| `MERCOSUR` | mot |
| `OPENAI` | nom propre / mot |
| `ARM` | nom propre |
| `META` | nom propre |
| `APPLE` | nom propre |
| `AMAZON` | nom propre |
| `GOOGLE` | nom propre |
| `ORACLE` | nom propre |
| `DOGE` | ★ prod — mot |
| `EDGE` | ★ prod — mot |
| `EVAL` | ★ prod — mot |
| `GRASP` | ★ prod — mot |
| `MIMIC` | ★ prod — mot |
| `ONTO` | ★ prod — mot |
| `PARA` | ★ prod — mot |
| `POLIS` | ★ prod — mot |
| `PRO` | ★ prod — mot |
| `REALM` | ★ prod — mot |
| `YOYO` | ★ prod — mot |

---

## 6. Suivi de production — `acronyms_seen_{locale}.json`

Chaque acronyme capturé par le filet automatique est consigné avec :
- `count` — nombre d'occurrences cumulées
- `first_seen` / `last_seen` — horodatages ISO 8601

**Règle opérationnelle** : tout acronyme atteignant **2+ occurrences** doit être évalué pour promotion dans `_SPELL_OUT_COMMON`. Les entrées marquées `★ prod` dans ce document en sont le résultat.

Fichiers :
- `data/state/acronyms_seen_en.json`
- `data/state/acronyms_seen_fr.json`

---

## 7. Checklist pour ajouter un nouvel acronyme

1. **Il existe dans la table statique ?** → pas d'action
2. **Il est dans `_AUTO_SPELL_SKIP` ?** → le TTS le lit comme un mot, OK
3. **Il est dans `acronyms_seen_*.json` avec count ≥ 2 ?** → promouvoir dans `_SPELL_OUT_COMMON`
4. **La prononciation EN et FR sont identiques ?** → table EN suffit (compact dots appliqués auto)
5. **La prononciation FR diffère ?** → ajouter dans `_SPELL_OUT_FR_OVERRIDES`
6. **C'est un mot prononçable tout-caps ?** → ajouter dans `_AUTO_SPELL_SKIP`

---

*Généré à partir de `src/ai_press_review/tts/cartesia.py` et `config/podcast.yaml` — commit `05d3136`*
