# Source manifest — 2026-04-24

Generated at: 2026-04-24T06:00:47.679149+00:00
Profile: daily
Relevant source count: 257

## 1. ParaRNN: Large-Scale Nonlinear RNNs, Trainable in Parallel
- Domain: machinelearning.apple.com
- URL: https://machinelearning.apple.com/research/large-scale-rnns
- Relevance score: 21.0
- Published: Thu, 23 Apr 2026 00:00:00 GMT
- Summary: Recurrent Neural Networks (RNNs) are naturally suited to efficient inference, requiring far less memory and compute than attention-based architectures, but the sequential nature of their computation has historically made it impractical to scale up RNNs to billions of parameters. A new advancement from Apple researchers makes RNN training dramatically more efficient — enabling large-scale training for the first time and widening the set of architecture choices available to practitioners in designing LLMs, particularly for resource-constrained deployment. In ParaRNN: Unlocking Parallel Training…
- Extract: ParaRNN: Large-Scale Nonlinear RNNs, Trainable in Parallel Recurrent Neural Networks (RNNs) are naturally suited to efficient inference, requiring far less memory and compute than attention-based architectures, but the sequential nature of their computation has historically made it impractical to scale up RNNs to billions of parameters. A new advancement from Apple researchers makes RNN training dramatically more efficient — enabling large-scale training for the first time and widening the set of architecture choices available to practitioners in designing LLMs, particularly for resource-constrained deployment. In ParaRNN: Unlocking Parallel Training of Nonlinear RNNs for Large Language Models, a new paper accepted to ICLR 2026 as an Oral, Apple researchers share a new framework for parall

## 2. A pelican for GPT-5.5 via the semi-official Codex backdoor API
- Domain: simonwillison.net
- URL: https://simonwillison.net/2026/Apr/23/gpt-5-5/
- Relevance score: 20.2
- Published: 2026-04-23T19:59:47+00:00
- Summary: <p><a href="https://openai.com/index/introducing-gpt-5-5/">GPT-5.5 is out</a>. It's available in OpenAI Codex and is rolling out to paid ChatGPT subscribers. I've had some preview access and found it to be a fast, effective and highly capable model. As is usually the case these days, it's hard to put into words what's good about it - I ask it to build things and it builds exactly what I ask for!</p> <p>There's one notable omission from today's release - the API:</p> <blockquote> <p>API deployments require different safeguards and we are working closely with partners and customers on the safety and security requirements for serving it at scale. We'll bring GPT‑5.5 and GPT‑5.5 Pro to the API very soon.</p> </blockquote> <p>When I run my <a href="https://simonwillison.net/tags/pelican-riding-a-bicycle/">pelican benchmark</a> I always prefer to use an API, to avoid hidden system prompts in ChatGPT or other agent harnesses from impacting the results.</p> <h4 id="the-openclaw-backdoor">The OpenClaw backdoor</h4> <p>One of the ongoing tension points in the AI world over the past few months has concerned how agent harnesses like OpenClaw and Pi interact with the APIs provided by the big pr
- Extract: A pelican for GPT-5.5 via the semi-official Codex backdoor API 23rd April 2026 GPT-5.5 is out. It’s available in OpenAI Codex and is rolling out to paid ChatGPT subscribers. I’ve had some preview access and found it to be a fast, effective and highly capable model. As is usually the case these days, it’s hard to put into words what’s good about it—I ask it to build things and it builds exactly what I ask for! There’s one notable omission from today’s release—the API: API deployments require different safeguards and we are working closely with partners and customers on the safety and security requirements for serving it at scale. We’ll bring GPT‑5.5 and GPT‑5.5 Pro to the API very soon. When I run my pelican benchmark I always prefer to use an API, to avoid hidden system prompts in ChatGPT 

## 3. Google DeepMind Introduces Decoupled DiLoCo: An Asynchronous Training Architecture Achieving 88% Goodput Under High Hardware Failure Rates
- Domain: marktechpost.com
- URL: https://www.marktechpost.com/2026/04/23/google-deepmind-introduces-decoupled-diloco-an-asynchronous-training-architecture-achieving-88-goodput-under-high-hardware-failure-rates/
- Relevance score: 19.5
- Published: Fri, 24 Apr 2026 04:40:10 +0000
- Summary: <p>Training frontier AI models is, at its core, a coordination problem. Thousands of chips must communicate with each other continuously, synchronizing every gradient update across the network. When one chip fails or even slows down, the entire training run can stall. As models scale toward hundreds of billions of parameters, that fragility becomes increasingly untenable. [&#8230;]</p> <p>The post <a href="https://www.marktechpost.com/2026/04/23/google-deepmind-introduces-decoupled-diloco-an-asynchronous-training-architecture-achieving-88-goodput-under-high-hardware-failure-rates/">Google DeepMind Introduces Decoupled DiLoCo: An Asynchronous Training Architecture Achieving 88% Goodput Under High Hardware Failure Rates</a> appeared first on <a href="https://www.marktechpost.com">MarkTechPost</a>.</p>
- Extract: Training frontier AI models is, at its core, a coordination problem. Thousands of chips must communicate with each other continuously, synchronizing every gradient update across the network. When one chip fails or even slows down, the entire training run can stall. As models scale toward hundreds of billions of parameters, that fragility becomes increasingly untenable. Google DeepMind is now proposing a different model entirely. Google DeepMind researchers introduced Decoupled DiLoCo (Distributed Low-Communication), a distributed training architecture that decouples compute into asynchronous, fault-isolated ‘islands,’ enabling large language model pre-training across geographically distant data centers without requiring the tight synchronization that makes conventional approaches brittle a

## 4. OpenAI releases "Spud" GPT-5.5 model
- Domain: axios.com
- URL: https://www.axios.com/2026/04/23/openai-releases-spud-gpt-model
- Relevance score: 19.0
- Published: Thu, 23 Apr 2026 18:00:08 +0000
- Summary: <p>OpenAI on Thursday released its most capable model, GPT-5.5, codenamed "Spud," just one week after competitor Anthropic launched its latest <a href="https://www.axios.com/2026/04/16/anthropic-claude-opus-model-mythos" target="_blank">model</a>. </p><p><strong>Why it matters: </strong><a href="https://www.axios.com/technology/automation-and-ai" target="_blank">AI</a> releases are getting faster, more efficient and more powerful. </p><hr /><p><strong>What they're saying: </strong>"This is a new class of intelligence. It's a big step towards more agentic and intuitive computing," OpenAI co-founder Greg Brockman told reporters in a briefing.</p><ul><li>GPT-5.5 is a "faster, sharper thinker for fewer tokens" compared to 5.4, he added, and can handle multi-step workflows more autonomously with less user input.</li><li>Despite the jump in capability, OpenAI says GPT-5.5 matches GPT-5.4's response speed in real-world use.</li><li>It's available starting Thursday in ChatGPT and Codex for paid subscribers, with API access coming soon once OpenAI finishes incorporating additional cybersecurity guardrails.</li></ul><p><strong>Zoom in: </strong>OpenAI says the model improvements are stronges
- Extract: Title: OpenAI releases "Spud" GPT-5.5 model URL Source: https://www.axios.com/2026/04/23/openai-releases-spud-gpt-model Published Time: 2026-04-23T18:00:08.572691Z Markdown Content: # OpenAI releases "Spud" GPT-5.5 model Manage your tracker preferences We use cookies and similar tracking technologies to remember preferences, analyze traffic, and deliver ads. Using some kinds of trackers (like cross-site or behavioral advertising cookies) may be considered a “sale” or “sharing” of personal data under certain state laws. You can opt in or out of these trackers below. Targeted advertising cookies and similar trackers - [x] On Setting this to “off” disables targeted advertising and related trackers in your current browser. To fully opt out, you must disable tracking on each browser and device 

## 5. CI-Work: Benchmarking Contextual Integrity in Enterprise LLM Agents
- Domain: arxiv.org
- URL: https://arxiv.org/abs/2604.21308
- Relevance score: 15.0
- Published: Fri, 24 Apr 2026 00:00:00 -0400
- Summary: arXiv:2604.21308v1 Announce Type: cross Abstract: Enterprise LLM agents can dramatically improve workplace productivity, but their core capability, retrieving and using internal context to act on a user's behalf, also creates new risks for sensitive information leakage. We introduce CI-Work, a Contextual Integrity (CI)-grounded benchmark that simulates enterprise workflows across five information-flow directions and evaluates whether agents can convey essential content while withholding sensitive context in dense retrieval settings. Our evaluation of frontier models reveals that privacy failures are prevalent (violation rates range from 15.8%-50.9%, with leakage reaching up to 26.7%) and uncovers a counterintuitive trade-off critical for industrial deployment: higher task utility often correlates with increased privacy violations. Moreover, the massive scale of enterprise data and potential user behavior further amplify this vulnerability. Simply increasing model size or reasoning depth fails to address the problem. We conclude that safeguarding enterprise workflows requires a paradigm shift, moving beyond model-centric scaling toward context-centric architectures.

## 6. Agentic AI for Personalized Physiotherapy: A Multi-Agent Framework for Generative Video Training and Real-Time Pose Correction
- Domain: arxiv.org
- URL: https://arxiv.org/abs/2604.21154
- Relevance score: 14.5
- Published: Fri, 24 Apr 2026 00:00:00 -0400
- Summary: arXiv:2604.21154v1 Announce Type: new Abstract: At-home physiotherapy compliance remains critically low due to a lack of personalized supervision and dynamic feedback. Existing digital health solutions rely on static, pre-recorded video libraries or generic 3D avatars that fail to account for a patient's specific injury limitations or home environment. In this paper, we propose a novel Multi-Agent System (MAS) architecture that leverages Generative AI and computer vision to close the tele-rehabilitation loop. Our framework consists of four specialized micro-agents: a Clinical Extraction Agent that parses unstructured medical notes into kinematic constraints; a Video Synthesis Agent that utilizes foundational video generation models to create personalized, patient-specific exercise videos; a Vision Processing Agent for real-time pose estimation; and a Diagnostic Feedback Agent that issues corrective instructions. We present the system architecture, detail the prototype pipeline using Large Language Models and MediaPipe, and outline our clinical evaluation plan. This work demonstrates the feasibility of combining generative media with agentic autonomous decision-making to scale perso

## 7. MISTY: High-Throughput Motion Planning via Mixer-based Single-step Drifting
- Domain: arxiv.org
- URL: https://arxiv.org/abs/2604.21489
- Relevance score: 14.5
- Published: Fri, 24 Apr 2026 00:00:00 -0400
- Summary: arXiv:2604.21489v1 Announce Type: cross Abstract: Multi-modal trajectory generation is essential for safe autonomous driving, yet existing diffusion-based planners suffer from high inference latency due to iterative neural function evaluations. This paper presents MISTY (Mixer-based Inference for Single-step Trajectory-drifting Yield), a high-throughput generative motion planner that achieves state-of-the-art closed-loop performance with pure single-step inference. MISTY integrates a vectorized Sub-Graph encoder to capture environment context, a Variational Autoencoder to structure expert trajectories into a compact 32-dimensional latent manifold, and an ultra-lightweight MLP-Mixer decoder to eliminate quadratic attention complexity. Importantly, we introduce a latent-space drifting loss that shifts the complex distribution evolution entirely to the training phase. By formulating explicit attractive and repulsive forces, this mechanism empowers the model to synthesize novel, proactive maneuvers, such as active overtaking, that are virtually absent from the raw expert demonstrations. Extensive evaluations on the nuPlan benchmark demonstrate that MISTY achieves state-of-the-art resul

## 8. Efficient Logic Gate Networks for Video Copy Detection
- Domain: arxiv.org
- URL: https://arxiv.org/abs/2604.21694
- Relevance score: 14.5
- Published: Fri, 24 Apr 2026 00:00:00 -0400
- Summary: arXiv:2604.21694v1 Announce Type: cross Abstract: Video copy detection requires robust similarity estimation under diverse visual distortions while operating at very large scale. Although deep neural networks achieve strong performance, their computational cost and descriptor size limit practical deployment in high-throughput systems. In this work, we propose a video copy detection framework based on differentiable Logic Gate Networks (LGNs), which replace conventional floating-point feature extractors with compact, logic-based representations. Our approach combines aggressive frame miniaturization, binary preprocessing, and a trainable LGN embedding model that learns both logical operations and interconnections. After training, the model can be discretized into a purely Boolean circuit, enabling extremely fast and memory-efficient inference. We systematically evaluate different similarity strategies, binarization schemes, and LGN architectures across multiple dataset folds and difficulty levels. Experimental results demonstrate that LGN-based models achieve competitive or superior accuracy and ranking performance compared to prior models, while producing descriptors several orders

## 9. Stream2LLM: Overlap Context Streaming and Prefill for Reduced Time-to-First-Token (TTFT)
- Domain: arxiv.org
- URL: https://arxiv.org/abs/2604.16395
- Relevance score: 14.5
- Published: Fri, 24 Apr 2026 00:00:00 -0400
- Summary: arXiv:2604.16395v2 Announce Type: replace-cross Abstract: Context retrieval systems for LLM inference face a critical challenge: high retrieval latency creates a fundamental tension between waiting for complete context (poor time-to-first-token) and proceeding without it (reduced quality). Streaming context incrementally--overlapping retrieval with inference--can mitigate this latency, but doing so with concurrent requests introduces new challenges: requests contend for GPU compute and memory, and scheduling must adapt to dynamic context arrivals. We present Stream2LLM, a streaming-aware LLM serving system for concurrent prefill-decode disaggregated deployments. Stream2LLM introduces adaptive scheduling and preemption for two distinct retrieval patterns: append-mode (progressive context accumulation) and update-mode (iterative refinement with cache invalidation). It decouples scheduling decisions from resource acquisition, enabling flexible preemption strategies guided by hardware-specific cost models, and uses longest common prefix matching to minimize redundant computation when input changes dynamically. To evaluate Stream2LLM, we collect two large-scale, real-world streaming wor

## 10. Hyperloop Transformers
- Domain: arxiv.org
- URL: https://arxiv.org/abs/2604.21254
- Relevance score: 14.5
- Published: Fri, 24 Apr 2026 00:00:00 -0400
- Summary: arXiv:2604.21254v1 Announce Type: cross Abstract: LLM architecture research generally aims to maximize model quality subject to fixed compute/latency budgets. However, many applications of interest such as edge and on-device deployment are further constrained by the model's memory footprint, thus motivating parameter-efficient architectures for language modeling. This paper describes a simple architecture that improves the parameter-efficiency of LLMs. Our architecture makes use of looped Transformers as a core primitive, which reuse Transformer layers across depth and are thus more parameter-efficient than ordinary (depth-matched) Transformers. We organize the looped Transformer into three blocks--begin, middle, and end blocks--where each block itself consists of multiple Transformer layers, and only the middle block is applied recurrently across depth. We augment the looped middle block with hyper-connections (Xie et al., 2026), which expand the residual stream into matrix-valued residual streams. Hyper-connections are applied only after each loop, and therefore add minimal new parameters and compute cost. Across various model scales, we find that our Hyper-Connected Looped Trans

## 11. Musical Score Understanding Benchmark: Evaluating Large Language Models' Comprehension of Complete Musical Scores
- Domain: arxiv.org
- URL: https://arxiv.org/abs/2511.20697
- Relevance score: 14.0
- Published: Fri, 24 Apr 2026 00:00:00 -0400
- Summary: arXiv:2511.20697v4 Announce Type: replace-cross Abstract: Understanding complete musical scores entails integrated reasoning over pitch, rhythm, harmony, and large-scale structure, yet the ability of Large Language Models and Vision--Language Models to interpret full musical notation remains insufficiently examined. We introduce Musical Score Understanding Benchmark (MSU-Bench), a human-curated benchmark for score-level musical understanding across textual (ABC notation) and visual (PDF) modalities. MSU-Bench contains 1,800 generative question-answer pairs from works by Bach, Beethoven, Chopin, Debussy, and others, organised into four levels of increasing difficulty, ranging from onset information to texture and form. Evaluations of more than fifteen state-of-the-art models, in both zero-shot and fine-tuned settings, reveal pronounced modality gaps, unstable level-wise performance, and challenges in maintaining multilevel correctness. Fine-tuning substantially improves results across modalities while preserving general knowledge, positioning MSU-Bench as a robust foundation for future research in multimodal reasoning. The benchmark and code are available at https://github.com/Congr

## 12. Xiaomi Releases MiMo-V2.5-Pro and MiMo-V2.5: Matching Frontier Model Benchmarks at Significantly Lower Token Cost
- Domain: marktechpost.com
- URL: https://www.marktechpost.com/2026/04/22/xiaomi-releases-mimo-v2-5-pro-and-mimo-v2-5-matching-frontier-model-benchmarks-at-significantly-lower-token-cost/
- Relevance score: 10.5
- Published: Thu, 23 Apr 2026 03:46:24 +0000
- Summary: <p>Xiaomi's MiMo team just dropped two new models that push open-source agentic AI closer to frontier territory than ever before. </p> <p>The post <a href="https://www.marktechpost.com/2026/04/22/xiaomi-releases-mimo-v2-5-pro-and-mimo-v2-5-matching-frontier-model-benchmarks-at-significantly-lower-token-cost/">Xiaomi Releases MiMo-V2.5-Pro and MiMo-V2.5: Matching Frontier Model Benchmarks at Significantly Lower Token Cost</a> appeared first on <a href="https://www.marktechpost.com">MarkTechPost</a>.</p>

## 13. The billion-dollar startup with a different idea for AI
- Domain: artificialintelligence-news.com
- URL: https://www.artificialintelligence-news.com/news/the-billion-dollar-startup-with-a-different-idea-for-ai-ami-labs-yann-lecun/
- Relevance score: 10.2
- Published: Thu, 23 Apr 2026 12:30:00 +0000
- Summary: <p>A billion dollars in startup funding for a company that employs 12 people is an indication that investors still have faith in AI. But the founder of the startup in question – AMI Labs&#8217; Yann LeCun – believes that the breed of technology we currently term AI (large language models) is not the way through [&#8230;]</p> <p>The post <a href="https://www.artificialintelligence-news.com/news/the-billion-dollar-startup-with-a-different-idea-for-ai-ami-labs-yann-lecun/">The billion-dollar startup with a different idea for AI</a> appeared first on <a href="https://www.artificialintelligence-news.com">AI News</a>.</p>

## 14. ​OpenAI launches new artificial intelligence model GPT- 5.1 with improved token usage - The Times of India
- Domain: timesofindia.indiatimes.com
- URL: https://news.google.com/rss/articles/CBMizAFBVV95cUxQSjBVb2JQX24tcHhncVgzMWdVcGpKNmhmVlp2TXM3SU8tVW55ckgwa19UOG45dWNMS01FT1E2OWw5VGoxVlkybG1HclpKNkRZZnJMZ1NSQlA3WDJOTHZLc0JLSGhIWWpZcW1OMlhsdER2RnZCRVlWYmxYd1dqbjhyMUR0NGpiVTFpZmZFSGFjVXZ1OUtQU25TZjlmdHAzeDYwMzBaeElTNnpMdW9wSlcxMUkxWHFDNjZZRHZBZEZ6RjBOU1F1OUdLaVhtclfSAdIBQVVfeXFMTWZSSjdhQUFLSFFSbEMwbmZLOUdZUlV3RlYzR2NCRHZqZnV5STllVFFSREdHaU1IRk1jVXdKa0dPTUs5cDNINDkxd3NqTkNmY0txVnRjZENYWmFXaUZWd2F1ZklFWkJSaFlNS1h4Q0JkbUpPZElQd0dTWGg4YjRxX1lHUnJmYzkyTVZpcFpRdjRIVXJ2aWhTTHhsQXFxWWR0S1JYby12TVRHVE9Rb2IzSnZKZHduYzBmaHJLaTE3dXBtaUFzT1YxVXNabmFCaFhpNE13
- Relevance score: 10.0
- Published: Fri, 24 Apr 2026 03:24:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMizAFBVV95cUxQSjBVb2JQX24tcHhncVgzMWdVcGpKNmhmVlp2TXM3SU8tVW55ckgwa19UOG45dWNMS01FT1E2OWw5VGoxVlkybG1HclpKNkRZZnJMZ1NSQlA3WDJOTHZLc0JLSGhIWWpZcW1OMlhsdER2RnZCRVlWYmxYd1dqbjhyMUR0NGpiVTFpZmZFSGFjVXZ1OUtQU25TZjlmdHAzeDYwMzBaeElTNnpMdW9wSlcxMUkxWHFDNjZZRHZBZEZ6RjBOU1F1OUdLaVhtclfSAdIBQVVfeXFMTWZSSjdhQUFLSFFSbEMwbmZLOUdZUlV3RlYzR2NCRHZqZnV5STllVFFSREdHaU1IRk1jVXdKa0dPTUs5cDNINDkxd3NqTkNmY0txVnRjZENYWmFXaUZWd2F1ZklFWkJSaFlNS1h4Q0JkbUpPZElQd0dTWGg4YjRxX1lHUnJmYzkyTVZpcFpRdjRIVXJ2aWhTTHhsQXFxWWR0S1JYby12TVRHVE9Rb2IzSnZKZHduYzBmaHJLaTE3dXBtaUFzT1YxVXNabmFCaFhpNE13?oc=5" target="_blank">​OpenAI launches new artificial intelligence model GPT- 5.1 with improved token usage</a>&nbsp;&nbsp;<font color="#6f6f6f">The Times of India</font>

## 15. Microsoft launches ‘vibe working’ in Word, Excel, and PowerPoint
- Domain: theverge.com
- URL: https://www.theverge.com/news/917328/microsoft-agent-mode-vibe-working-office-word-excel-powerpoint
- Relevance score: 9.8
- Published: 2026-04-23T07:34:18-04:00
- Summary: Microsoft is rolling out a new Agent Mode inside Office apps like Word, Excel, and PowerPoint this week. Previously described by Microsoft as "vibe working," the Agent Mode is a more powerful version of the Copilot experience in Office that Microsoft has been trying to sell to businesses. "When we first shipped Copilot, foundation models [&#8230;]

## 16. Anthropic: No "kill switch" for AI in classified settings
- Domain: axios.com
- URL: https://www.axios.com/2026/04/22/anthropic-no-kill-switch-ai-classified-settings
- Relevance score: 9.5
- Published: Wed, 22 Apr 2026 23:57:37 +0000
- Summary: <p>Anthropic says it has no way to control or shut down its <a href="https://www.axios.com/technology/automation-and-ai" target="_blank">AI</a> models once they're deployed by the Pentagon, according to a new court filing.</p><p><strong>Why it matters: </strong>The Pentagon designated Anthropic a <a href="https://www.axios.com/2026/03/09/anthropic-sues-pentagon-supply-chain-risk-label" target="_blank">supply chain risk</a>, contending the AI firm is inappropriately getting involved in how its technology can be used in sensitive military operations. </p><hr /><p><strong>What's inside:</strong> Anthropic argues in the <a href="https://storage.courtlistener.com/recap/gov.uscourts.cadc.42923/gov.uscourts.cadc.42923.01208843394.0.pdf" target="_blank">filing</a> to a federal appeals court in D.C. that it has no visibility, technical ability or any kind of "kill switch" for its technology once it's deployed.</p><ul><li>The company also says the Pentagon has the opportunity to test models before deployment.</li></ul><p><strong>Catch up quick: </strong>The company's usage policies include no Claude for autonomous weapons or mass surveillance, red lines that the Pentagon dismissed as red her

## 17. Supply chain cracks constrain AI boom
- Domain: axios.com
- URL: https://www.axios.com/2026/04/23/ai-iran-supply-chain
- Relevance score: 9.5
- Published: Thu, 23 Apr 2026 16:01:18 +0000
- Summary: <p>The <a href="https://www.axios.com/2026/04/23/ai-inflation-productivity-companies" target="_blank">AI economy</a> is being constrained by the physical world: The Iran war threatens to squeeze the industrial inputs that chip manufacturers depend on, the latest confirmation that once-reliable global chokepoints are now more fragile than ever.</p><p><strong>Why it matters: </strong>It is part of a growing pattern defining the economic conditions of the 2020s: shocks exposing the fragility of supply chains that the world took for granted.</p><hr /><ul><li>The AI buildout is the latest to be throttled by this trend — in this case, the effects of an uncertain Middle East conflict and the Strait of Hormuz's effective closure. </li></ul><p><strong>What they're saying:</strong> "Hyperscalers are committing roughly $650 billion to U.S. AI infrastructure this year alone. And that investment assumes the supply chain holding it together remains intact," Moody's David Pan tells Axios.</p><ul><li>"The AI economy runs on tokens, tokens run on GPUs and GPUs depend on Qatari helium, Israeli bromine, and [liquefied natural gas] tankers with a single, 21-mile-wide exit from the Persian Gulf," Pan a

## 18. DeepSeek unveils next-gen AI model as Huawei vows ‘full support’ with new chips
- Domain: scmp.com
- URL: https://www.scmp.com/tech/big-tech/article/3351239/deepseek-releases-next-gen-ai-model-world-leading-efficiency
- Relevance score: 9.3
- Published: Fri, 24 Apr 2026 03:25:33 +0000
- Summary: DeepSeek has finally released its much-anticipated next-generation foundational artificial intelligence model, the open-source V4, which it said was competitive with leading US closed-source models from the likes of OpenAI and Google DeepMind. The Hangzhou-based AI start-up released two versions of the model on Friday, with the V4-pro model boasting 1.6 trillion parameters, making it the company’s biggest-ever model by that metric, while the smaller V4-flash model has 284 billion parameters. A...

## 19. DeepSeek V4终于发布，但它留下的5道主观题还没有答案
- Domain: 36kr.com
- URL: https://36kr.com/p/3780375304312072
- Relevance score: 8.7
- Published: 2026-04-24 13:20:31  +0800
- Summary: <p>文｜周鑫雨</p> <p>资料整理｜钟楚笛</p> <p>编辑｜苏建勋 杨轩</p> <p>靴子终于落地。</p> <p>被调侃“Next Week”近3个月的DeepSeek V4，终于显露真身。</p> <p>1.6T的最大参数量、1M的上下文窗口、针对Agent的性能优化，以及基于MoE（混合专家模型）和稀疏注意力机制DSA，降低计算和显存需求——这些曾被外界纷纷猜测的参数和性能，随着V4的官宣，一锤定音。</p> <p class="image-wrapper"><img src="https://img.36krcdn.com/hsossms/20260424/v2_6fe3b89ee333454eb5ea0a0e5af92a4b@5783683_oswg172569oswg1080oswg742_img_000?x-oss-process=image/format,jpg/interlace,1" /></p> <p class="img-desc">DeepSeek V4性能测评结果。</p> <p>姗姗来迟的原由，与V4将训练框架从英伟达迁移到华为昇腾上有关，也与DeepSeek内部的决策变动有关。我们得知，2025年年中，DeepSeek曾面临一次较为严重的训练失败。</p> <p>“当时，DeepSeek面临重新适配芯片的问题。”一名知情者提到，“内部有关训练方向的意见也不完全统一。梁文锋提出了一些自己的要求，但在执行层面很难折中。”</p> <p>不过，与外界关于“新模型支持多模态生成和理解”的猜测不同，V4依然是个语言模型。暂缓多模态生成的训练策略，主要源于算力和现金的掣肘。</p> <p>多名知情者告诉《智能涌现》，DeepSeek的对外融资窗口，是2026年4月中旬打开的。内部的导火索，是DeepSeek需要更多资金支持，训练参数规模更大的模型，同时，留住和招纳更多的顶级人才。</p> <p>“1.6T的参数量与OpenAI、Anthropic等顶级厂商的模型相比，并不具有绝对的竞争力。”一名从业者对我们提到，很快，国内也有模型厂商，将发布<strong>3T</strong>参数规模的模型。</p> <p>在人才侧，随着郭达雅（DeepSeek R1核心作者）、王炳宣（DeepSeek LLM核心作者）等人才被字节、腾讯等大厂挖走，DeepSeek需要一笔大额融资稳定军心、招兵买马。</p> <p>而转向开放融资的外部导火索，几名业内人士猜测，与腾讯的投资态度有关。在开发融资前，梁文锋和马化腾曾有关注独家注资有过几次商谈。但两名相关人士透露，给腾讯20%股份的条件，没有得到梁文锋的同意。</p> <p>R1发布以来，一个明显的转变是：<strong>DeepSeek从一个偏非营利的、理想主义的技术乌托邦，被迫快速转向一家重

## 20. Winning a Kaggle Competition with Generative AI–Assisted Coding - NVIDIA Developer
- Domain: developer.nvidia.com
- URL: https://news.google.com/rss/articles/CBMinwFBVV95cUxORFM4UDVoMkZxODYtYWI1aEQ3ZlE5eVZUc19rRDhUa0x3ZEd3YkJ5VEdobkgtd2E4LWxJZkRVdTNjNVhhU1ZlcmZFcDc5R2ZTdHBKMllDZE5zZklCMkZKdzFPQmN2M2d2SXhzYUFhUG9aVGJiWTlRVjROcHhBYXFwSkM4aXluVk10by1LeWVrdEtHTnB3MkhyMUZQTGR0ZWM
- Relevance score: 8.5
- Published: Thu, 23 Apr 2026 20:25:49 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMinwFBVV95cUxORFM4UDVoMkZxODYtYWI1aEQ3ZlE5eVZUc19rRDhUa0x3ZEd3YkJ5VEdobkgtd2E4LWxJZkRVdTNjNVhhU1ZlcmZFcDc5R2ZTdHBKMllDZE5zZklCMkZKdzFPQmN2M2d2SXhzYUFhUG9aVGJiWTlRVjROcHhBYXFwSkM4aXluVk10by1LeWVrdEtHTnB3MkhyMUZQTGR0ZWM?oc=5" target="_blank">Winning a Kaggle Competition with Generative AI–Assisted Coding</a>&nbsp;&nbsp;<font color="#6f6f6f">NVIDIA Developer</font>

## 21. Applying multimodal biological foundation models across therapeutics and patient care - Amazon Web Services
- Domain: aws.amazon.com
- URL: https://news.google.com/rss/articles/CBMizAFBVV95cUxOVnQ3UGU3YmZOVGUwR2VkeERSWkRFcEUwV2JzSDNKZlRtRm1LcURNbnY5OVhCYmRyeVlnc3M1UDNocW9JM2Q2Q3p4LVlmb1FYNFVfd0JHYmpOS3BGaDM5dHhrcWsxT1p4NDhqcV9ZVlNIVG5oRTNxdFdiYVlxZlBBb0NGV1RnblhsZzNGQ1B4eHVsdXQ1V2J0c1ZsNXljTWxZUHVESGNZYXlmQWNfbnF1dWt6NTFnOVBra3laeHlBcjZlalhFRGhqRFZXLUU
- Relevance score: 8.5
- Published: Thu, 23 Apr 2026 16:17:29 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMizAFBVV95cUxOVnQ3UGU3YmZOVGUwR2VkeERSWkRFcEUwV2JzSDNKZlRtRm1LcURNbnY5OVhCYmRyeVlnc3M1UDNocW9JM2Q2Q3p4LVlmb1FYNFVfd0JHYmpOS3BGaDM5dHhrcWsxT1p4NDhqcV9ZVlNIVG5oRTNxdFdiYVlxZlBBb0NGV1RnblhsZzNGQ1B4eHVsdXQ1V2J0c1ZsNXljTWxZUHVESGNZYXlmQWNfbnF1dWt6NTFnOVBra3laeHlBcjZlalhFRGhqRFZXLUU?oc=5" target="_blank">Applying multimodal biological foundation models across therapeutics and patient care</a>&nbsp;&nbsp;<font color="#6f6f6f">Amazon Web Services</font>

## 22. PLDT Inc. will become Southeast Asia’s first telco to use one of the most advanced agentic artificial intelligence (AI) to expedite information exchange with enterprises. https://tinyurl.com/28849fzk - facebook.com
- Domain: facebook.com
- URL: https://news.google.com/rss/articles/CBMi3AFBVV95cUxPQnFqaGR0SnB3VFVienY0bXJ0dmtHcHdQOTRuaXRpYjhfaDViV1lvYnpsemo4LURVT2pORE5vR2NMRHZvV1lOSHZpMnZ3a1ZnLWhUMEl2Q3dFeU9lNVVSR0Y5bFk2OWZYQnVfcV9uTG1CWUVwSlI1RjBzVl9JRmtXOFp5YjQtNUdleXp1bVZXT1hYTnVldzY1WHcyVnA1MFJwNWd2NlZXaDZ6akhKWjY1QlJ3UWNyOXpSNERHZTNBTjlSeUNWUHhSOU9Kb3lHZ0p4XzB0X2lJTk1mX2Vy
- Relevance score: 8.5
- Published: Fri, 24 Apr 2026 04:03:17 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi3AFBVV95cUxPQnFqaGR0SnB3VFVienY0bXJ0dmtHcHdQOTRuaXRpYjhfaDViV1lvYnpsemo4LURVT2pORE5vR2NMRHZvV1lOSHZpMnZ3a1ZnLWhUMEl2Q3dFeU9lNVVSR0Y5bFk2OWZYQnVfcV9uTG1CWUVwSlI1RjBzVl9JRmtXOFp5YjQtNUdleXp1bVZXT1hYTnVldzY1WHcyVnA1MFJwNWd2NlZXaDZ6akhKWjY1QlJ3UWNyOXpSNERHZTNBTjlSeUNWUHhSOU9Kb3lHZ0p4XzB0X2lJTk1mX2Vy?oc=5" target="_blank">PLDT Inc. will become Southeast Asia’s first telco to use one of the most advanced agentic artificial intelligence (AI) to expedite information exchange with enterprises. https://tinyurl.com/28849fzk</a>&nbsp;&nbsp;<font color="#6f6f6f">facebook.com</font>

## 23. NVIDIA and Google infrastructure cuts AI inference costs
- Domain: artificialintelligence-news.com
- URL: https://www.artificialintelligence-news.com/news/nvidia-and-google-infrastructure-cuts-ai-inference-costs/
- Relevance score: 8.2
- Published: Thu, 23 Apr 2026 12:19:36 +0000
- Summary: <p>At the Google Cloud Next conference, Google and NVIDIA outlined their hardware roadmap designed to address the cost of AI inference at scale. The companies detailed the new A5X bare-metal instances, which run on NVIDIA Vera Rubin NVL72 rack-scale systems. Through hardware and software codesign, this architecture aims to deliver up to ten times lower [&#8230;]</p> <p>The post <a href="https://www.artificialintelligence-news.com/news/nvidia-and-google-infrastructure-cuts-ai-inference-costs/">NVIDIA and Google infrastructure cuts AI inference costs</a> appeared first on <a href="https://www.artificialintelligence-news.com">AI News</a>.</p>

## 24. Sony AI robot beats players as humanoid robot wins Beijing race
- Domain: artificialintelligence-news.com
- URL: https://www.artificialintelligence-news.com/news/sony-ai-robot-table-tennis-humanoid-robot-beijing-race/
- Relevance score: 8.2
- Published: Thu, 23 Apr 2026 10:00:00 +0000
- Summary: <p>An autonomous table tennis robot developed by Sony AI has competed against and defeated high-level human players in regulated matches, according to Reuters. The system is part of a broader category often referred to as &#8220;physical AI,&#8221; where artificial intelligence is applied to machines operating in real-world environments. The robot, named Ace, was designed to [&#8230;]</p> <p>The post <a href="https://www.artificialintelligence-news.com/news/sony-ai-robot-table-tennis-humanoid-robot-beijing-race/">Sony AI robot beats players as humanoid robot wins Beijing race</a> appeared first on <a href="https://www.artificialintelligence-news.com">AI News</a>.</p>

## 25. Solid Earnings From IBM and ServiceNow Fail to Quell Artificial Intelligence Concerns, Sending Software Stocks Lower. Here's What Investors Need to Know - The Motley Fool
- Domain: fool.com
- URL: https://news.google.com/rss/articles/CBMimAFBVV95cUxOVHlyc0ZEWEFlZG1jTmphSTFhNEthOFQyenRYTWY5cXN4RF9tbHZtQVgxS2lRTTJPcTRMUk9kSEg0dUc4QUoyZWI0WFMteUFqZkdNcWNMcUIyTHZRcG9tNU1WeFlSOVFoZmE1ODZaNXZkSl9uZVhub1JLc0FEWk0zaXE5ZmVvb3kwVlcxaXNsZnlfNC1MN0Z5Zg
- Relevance score: 8.0
- Published: Thu, 23 Apr 2026 19:03:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMimAFBVV95cUxOVHlyc0ZEWEFlZG1jTmphSTFhNEthOFQyenRYTWY5cXN4RF9tbHZtQVgxS2lRTTJPcTRMUk9kSEg0dUc4QUoyZWI0WFMteUFqZkdNcWNMcUIyTHZRcG9tNU1WeFlSOVFoZmE1ODZaNXZkSl9uZVhub1JLc0FEWk0zaXE5ZmVvb3kwVlcxaXNsZnlfNC1MN0Z5Zg?oc=5" target="_blank">Solid Earnings From IBM and ServiceNow Fail to Quell Artificial Intelligence Concerns, Sending Software Stocks Lower. Here's What Investors Need to Know</a>&nbsp;&nbsp;<font color="#6f6f6f">The Motley Fool</font>

## 26. Google Brings All Enterprise AI Agent Tools Under One Roof
- Domain: pymnts.com
- URL: https://www.pymnts.com/artificial-intelligence-2/2026/google-brings-all-enterprise-ai-agent-tools-under-one-roof/
- Relevance score: 8.0
- Published: Thu, 23 Apr 2026 17:44:54 +0000
- Summary: <p>Most enterprises experimenting with artificial intelligence (AI) agents face the same problem. Building an agent is one task. Connecting it to live data is another. Securing it, governing it and knowing when it fails has historically required a separate tool, a separate vendor and a separate procurement decision for each. At Google Cloud Next [&#8230;]</p> <p>The post <a href="https://www.pymnts.com/artificial-intelligence-2/2026/google-brings-all-enterprise-ai-agent-tools-under-one-roof/">Google Brings All Enterprise AI Agent Tools Under One Roof</a> appeared first on <a href="https://www.pymnts.com">PYMNTS.com</a>.</p>

## 27. White House Accuses China of Far-Reaching Theft of AI Tech
- Domain: pymnts.com
- URL: https://www.pymnts.com/artificial-intelligence-2/2026/white-house-accuses-china-of-far-reaching-theft-of-ai-tech/
- Relevance score: 8.0
- Published: Thu, 23 Apr 2026 17:07:57 +0000
- Summary: <p>The White House is reportedly accusing China of “industrial-scale” theft of U.S. artificial intelligence (AI) technology. With that accusation comes the warning that the government will crack down on this practice, the Financial Times (FT) reported Thursday (April 23), citing a memo seen by the news outlet. “The US government has information indicating that [&#8230;]</p> <p>The post <a href="https://www.pymnts.com/artificial-intelligence-2/2026/white-house-accuses-china-of-far-reaching-theft-of-ai-tech/">White House Accuses China of Far-Reaching Theft of AI Tech</a> appeared first on <a href="https://www.pymnts.com">PYMNTS.com</a>.</p>

## 28. Alibaba opens Qwen app to outside partners with China Eastern Airlines tie-up
- Domain: scmp.com
- URL: https://www.scmp.com/tech/big-tech/article/3351076/alibaba-opens-qwen-app-outside-partners-china-eastern-airlines-tie
- Relevance score: 7.8
- Published: Thu, 23 Apr 2026 03:12:43 +0000
- Summary: Alibaba Group Holding has struck its first external partnership for its flagship consumer artificial intelligence app, linking it with China Eastern Airlines in a move that pushes its agentic capabilities beyond the company’s own ecosystem and into real-world services. The company said the fresh collaboration allowed users of the Qwen app to manage the full flight booking process – from search and ticket purchase to seat selection and check-in – within a single natural-language chat interface....

## 29. Serving the For You feed
- Domain: simonwillison.net
- URL: https://simonwillison.net/2026/Apr/24/serving-the-for-you-feed/
- Relevance score: 7.7
- Published: 2026-04-24T01:08:17+00:00
- Summary: <p><strong><a href="https://atproto.com/blog/serving-the-for-you-feed">Serving the For You feed</a></strong></p> One of Bluesky's most interesting features is that anyone can run their own <a href="bluesky custom feed">custom "feed" implementation</a> and make it available to other users - effectively enabling custom algorithms that can use any mechanism they like to recommend posts.</p> <p>spacecowboy runs the <a href="https://bsky.app/profile/did:plc:3guzzweuqraryl3rdkimjamk/feed/for-you">For You Feed</a>, used by around 72,000 people. This guest post on the AT Protocol blog explains how it works.</p> <p>The architecture is <em>fascinating</em>. The feed is served by a single Go process using SQLite on a "gaming" PC in spacecowboy's living room - 16 cores, 96GB of RAM and 4TB of attached NVMe storage.</p> <p>Recommendations are based on likes: what else are the people who like the same things as you liking on the platform?</p> <p>That Go server consumes the Bluesky firehose and stores the relevant details in SQLite, keeping the last 90 days of relevant data, which currently uses around 419GB of SQLite storage.</p> <p>Public internet traffic is handled by a $7/month VPS on OVH, wh

## 30. Applying multimodal biological foundation models across therapeutics and patient care
- Domain: aws.amazon.com
- URL: https://aws.amazon.com/blogs/machine-learning/applying-multimodal-biological-foundation-models-across-therapeutics-and-patient-care/
- Relevance score: 7.5
- Published: Thu, 23 Apr 2026 16:17:29 +0000
- Summary: In this post, we'll explore how multimodal BioFMs work, showcase real-world applications in drug discovery and clinical development, and contextualize how AWS enables organizations to build and deploy multimodal BioFMs.

## 31. Here’s how our TPUs power increasingly demanding AI workloads.
- Domain: blog.google
- URL: https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/what-is-a-tpu/
- Relevance score: 7.5
- Published: Thu, 23 Apr 2026 12:00:00 +0000
- Summary: <img src="https://storage.googleapis.com/gweb-uniblog-publish-prod/images/What_is_a_TPU_social.max-600x600.format-webp.webp" />Learn how Google’s TPUs power increasingly demanding AI workloads with this new video.

## 32. Primech Holdings Accelerates U.S. Expansion for Primech AI’s Hytron, Selected for SelectUSA Tech Amid Growing Institutional Deployment Pipeline - The Manila Times
- Domain: manilatimes.net
- URL: https://news.google.com/rss/articles/CBMiuAJBVV95cUxOclNUcTFQaGk3cnd4NlluaFJkM2V2THVxTkVxTzNSWWs0WC01N3p0d09GTlVWM2dreVJTamh0YVlwdERaRmJKdllmcEpfc3pxd2VOYk9VSjlkRXptTHNJTTY5ZTF0S3hGa2tmZk5LQ24wWjQ3ZmJ4aUE4LVJhOGQzS2FlTGNKai00NDVHUi1RcFVGWTB6VXN6cnVjeHl3emFTVTRYaDFWb2Fic2NhUDBUOE93Y3lUaU5pMkVPaldyWHQ1WGdhYUE3LVdiZDBqaVpKVkt4UE5Ucy1fWTlxTDFxZ1k5azhGd3RQazFZVndTTWQ2M0RBZGJmbGw2c2RMUUFFSDFVTzNadkdNcnJCZkdsSEFPNW1LM3RYTVhSY3V0UG1TM09kdUxzY2JXV0hHNzhIZm9GWEl1ZEPSAb4CQVVfeXFMTzJlLU9Md250UGZtajdpa1FSWXcxOE4wOVVFN0Vuc1g3NTh6eC13OUQ5TXNqWDJHSWZEM1M3OHJwb2Vjdmp0WUJSaUVEcnFHNU55TTMwazBkckd6UktUOHNyN3JsdkdMak1nMUEzYjFoQzY3NUlrVElCamMyOWlmQXBNbHpUWkh1YjhkRzVaMHJVVUpsaTlhSkZfX2dBVDVFWHIwZUZIUmd0bEdPeFc2dkJ2UzhLSXp4Ul9YS080WklKTm5tSG9KSUxPQTRQZ0wyaDVqOXIxVko2RGhDMW43YmpsVldjQldfTmlEZjZ3czNlOXNJU19wbGRVSnVhZFo5MGRyMEcxa3FvMm9MeXpSTkRraUc2WUI1TWpiZWhPRVpwSVI0TGphbmo1MUpkckVJLUpJd05WcWxDek9aSk9B
- Relevance score: 7.5
- Published: Thu, 23 Apr 2026 11:17:16 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiuAJBVV95cUxOclNUcTFQaGk3cnd4NlluaFJkM2V2THVxTkVxTzNSWWs0WC01N3p0d09GTlVWM2dreVJTamh0YVlwdERaRmJKdllmcEpfc3pxd2VOYk9VSjlkRXptTHNJTTY5ZTF0S3hGa2tmZk5LQ24wWjQ3ZmJ4aUE4LVJhOGQzS2FlTGNKai00NDVHUi1RcFVGWTB6VXN6cnVjeHl3emFTVTRYaDFWb2Fic2NhUDBUOE93Y3lUaU5pMkVPaldyWHQ1WGdhYUE3LVdiZDBqaVpKVkt4UE5Ucy1fWTlxTDFxZ1k5azhGd3RQazFZVndTTWQ2M0RBZGJmbGw2c2RMUUFFSDFVTzNadkdNcnJCZkdsSEFPNW1LM3RYTVhSY3V0UG1TM09kdUxzY2JXV0hHNzhIZm9GWEl1ZEPSAb4CQVVfeXFMTzJlLU9Md250UGZtajdpa1FSWXcxOE4wOVVFN0Vuc1g3NTh6eC13OUQ5TXNqWDJHSWZEM1M3OHJwb2Vjdmp0WUJSaUVEcnFHNU55TTMwazBkckd6UktUOHNyN3JsdkdMak1nMUEzYjFoQzY3NUlrVElCamMyOWlmQXBNbHpUWkh1YjhkRzVaMHJVVUpsaTlhSkZfX2dBVDVFWHIwZUZIUmd0bEdPeFc2dkJ2UzhLSXp4Ul9YS080WklKTm5tSG9KSUxPQTRQZ0wyaDVqOXIxVko2RGhDMW43YmpsVldjQldfTmlEZjZ3czNlOXNJU19wbGRVSnVhZFo5MGRyMEcxa3FvMm9MeXpSTkRraUc2WUI1TWpiZWhPRVpwSVI0TGphbmo1MUpkckVJLUpJd05WcWxDek9aSk9B?oc=5" target="_blank">Primech Holdings Accelerates U.S. Expansion for Primech AI’s Hytron, Selected for SelectUSA Tech Amid Growing Institutional Deployment Pipeline</a>&nbsp;&nbsp;<font color="#6f6f6f">The Manila Times</font>

## 33. MINIX tackles on-device LLM and AI processing with new T4000 and T5000 Generative AI Mini Workstation - My Everyday Tech
- Domain: myeverydaytech.com
- URL: https://news.google.com/rss/articles/CBMikAFBVV95cUxPZDVBUkdwM1RobENMdkNZWVBHMk5EcjNZX1psOTBMYkpHU2F4MjVMVnRBMDFFanFMdTJ5X2JUbnZmakFKQi1HTTdETnR4V1FRR3JzTlBFQXZ6LUY5cnBEYVE4NWFqZ2xwb0lITHhWN2tlUGdIdm1MWi1FcTUxaVhYeTlWV3FyNm1OVDlYaU0zSVo
- Relevance score: 7.5
- Published: Thu, 23 Apr 2026 11:10:59 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMikAFBVV95cUxPZDVBUkdwM1RobENMdkNZWVBHMk5EcjNZX1psOTBMYkpHU2F4MjVMVnRBMDFFanFMdTJ5X2JUbnZmakFKQi1HTTdETnR4V1FRR3JzTlBFQXZ6LUY5cnBEYVE4NWFqZ2xwb0lITHhWN2tlUGdIdm1MWi1FcTUxaVhYeTlWV3FyNm1OVDlYaU0zSVo?oc=5" target="_blank">MINIX tackles on-device LLM and AI processing with new T4000 and T5000 Generative AI Mini Workstation</a>&nbsp;&nbsp;<font color="#6f6f6f">My Everyday Tech</font>

## 34. Anthropic's growing pains mount ahead of OpenAI showdown
- Domain: axios.com
- URL: https://www.axios.com/2026/04/23/anthropic-openai-showdown
- Relevance score: 7.5
- Published: Thu, 23 Apr 2026 09:00:06 +0000
- Summary: <p><a href="https://www.axios.com/2026/04/17/anthropic-white-house-wiles-bessent-amodei" target="_blank">Anthropic</a> is hitting turbulence at a critical moment, with a cascade of challenges<strong> </strong>converging ahead of a potential IPO that could value the company near $800 billion.</p><p><strong>Why it matters: </strong>The AI darling, whose <a href="https://www.axios.com/2026/04/13/anthropic-revenue-growth-ai" target="_blank">revenue has tripled</a> to $30 billion this year on the back of its wildly popular coding tools, has never been more valuable or more vulnerable.</p><hr /><ul><li>Chief rival <a href="https://www.axios.com/2026/04/21/openai-anthropic-enterprise-rivalry-heats-up" target="_blank">OpenAI senses opportunity</a> in the Claude maker's recent stumbles, courting frustrated developers and pitching itself as the steadier alternative ahead of dueling IPOs.</li></ul><p><strong>Zoom in: </strong>Anthropic's problems over the past two months span nearly every part of its business — product quality, pricing, security and capacity — and are starting to compound.</p><p><strong>1. Model backlash:</strong> Perceived declines in Opus 4.6 performance triggered an initia

## 35. Merchants See a Bigger AI Prize if Consumers Trust the System
- Domain: pymnts.com
- URL: https://www.pymnts.com/artificial-intelligence-2/2026/merchants-see-a-bigger-ai-prize-if-consumers-trust-the-system/
- Relevance score: 7.5
- Published: Thu, 23 Apr 2026 08:00:28 +0000
- Summary: <p>Autonomous commerce is no longer a future state. It is already reshaping how consumers spend. Scaling it, new data shows, demands more than capable technology. It demands trust. Findings in the new PYMNTS Intelligence report, “Embedded Offers: The Billion-Dollar Opportunity Inside Recent Consumer Spending,” produced in collaboration with FIS, find that adoption of autonomous and agentic [&#8230;]</p> <p>The post <a href="https://www.pymnts.com/artificial-intelligence-2/2026/merchants-see-a-bigger-ai-prize-if-consumers-trust-the-system/">Merchants See a Bigger AI Prize if Consumers Trust the System</a> appeared first on <a href="https://www.pymnts.com">PYMNTS.com</a>.</p>

## 36. Google's open-source DESIGN.md gives AI agents a prompt-ready blueprint for brand-consistent design
- Domain: the-decoder.com
- URL: https://the-decoder.com/googles-open-source-design-md-gives-ai-agents-a-prompt-ready-blueprint-for-brand-consistent-design/
- Relevance score: 7.3
- Published: Thu, 23 Apr 2026 17:20:06 +0000
- Summary: <p><img alt="" class="attachment-full size-full wp-post-image" height="1221" src="https://the-decoder.com/wp-content/uploads/2026/04/stitch_beta.png" style="height: auto; margin-bottom: 10px;" width="2108" /></p> <p> Google is open-sourcing the agent prompt behind its AI design tool Stitch. The DESIGN.md format is built to teach AI agents how to follow brand rules.</p> <p>The article <a href="https://the-decoder.com/googles-open-source-design-md-gives-ai-agents-a-prompt-ready-blueprint-for-brand-consistent-design/">Google&#039;s open-source DESIGN.md gives AI agents a prompt-ready blueprint for brand-consistent design</a> appeared first on <a href="https://the-decoder.com">The Decoder</a>.</p>

## 37. Researchers warn US politics is repeating its ChatGPT mistake with world models
- Domain: the-decoder.com
- URL: https://the-decoder.com/researchers-warn-us-politics-is-repeating-its-chatgpt-mistake-with-world-models/
- Relevance score: 7.3
- Published: Thu, 23 Apr 2026 13:33:58 +0000
- Summary: <p><img alt="" class="attachment-full size-full wp-post-image" height="768" src="https://the-decoder.com/wp-content/uploads/2026/04/world-model-globa-nano-banana-pro.jpg" style="height: auto; margin-bottom: 10px;" width="1376" /></p> <p> The next phase of AI development is moving beyond text and into the physical world. Researchers warn that US policymakers don't yet grasp the scale of what's coming, while China is already pulling ahead in robotics.</p> <p>The article <a href="https://the-decoder.com/researchers-warn-us-politics-is-repeating-its-chatgpt-mistake-with-world-models/">Researchers warn US politics is repeating its ChatGPT mistake with world models</a> appeared first on <a href="https://the-decoder.com">The Decoder</a>.</p>

## 38. Beijing moves to clean up online ad ecosystem in first-of-its-kind campaign
- Domain: scmp.com
- URL: https://www.scmp.com/tech/article/3351202/beijing-moves-clean-online-ad-ecosystem-first-its-kind-campaign
- Relevance score: 7.3
- Published: Thu, 23 Apr 2026 13:03:24 +0000
- Summary: China’s top market regulator will launch a six-month crackdown on the country’s internet advertising sector, targeting malpractices including the misuse of artificial intelligence, in what it described as its first campaign to clean up the broader online advertising ecosystem. The State Administration for Market Regulation (SAMR) said on Thursday that the campaign comes as new risks – from AI misuse to traffic-driven marketing tactics – emerge alongside long-standing issues, even as data and...

## 39. Why Anthropic’s Mythos has energised China’s cybersecurity industry
- Domain: scmp.com
- URL: https://www.scmp.com/tech/tech-trends/article/3351152/why-anthropics-mythos-has-energised-chinas-cybersecurity-industry
- Relevance score: 7.3
- Published: Thu, 23 Apr 2026 12:00:08 +0000
- Summary: In the second of a three-part series on Anthropic’s powerful Mythos artificial intelligence model, we examine the effect it has had on China’s cybersecurity and finance industries. US start-up Anthropic’s new AI model, Claude Mythos Preview, has drawn global attention for its ability to autonomously identify and exploit cybersecurity vulnerabilities at a level that appears to surpass conventional tools used in enterprise and financial systems. The model has not been made publicly available, with...

## 40. OpenAI says its new ChatGPT for Clinicians outperforms doctors on clinical tasks even when they have unlimited time and web access
- Domain: the-decoder.com
- URL: https://the-decoder.com/openai-says-its-new-chatgpt-for-clinicians-outperforms-doctors-on-clinical-tasks-even-when-they-have-unlimited-time-and-web-access/
- Relevance score: 7.3
- Published: Thu, 23 Apr 2026 10:21:15 +0000
- Summary: <p><img alt="" class="attachment-full size-full wp-post-image" height="768" src="https://the-decoder.com/wp-content/uploads/2026/04/chatgpt_health.png" style="height: auto; margin-bottom: 10px;" width="1376" /></p> <p> OpenAI is rolling out ChatGPT for Clinicians, a free version of its chatbot for medical professionals. A new benchmark claims GPT-5.4 beats human doctors on clinical tasks, even when those doctors have unlimited time and internet access.</p> <p>The article <a href="https://the-decoder.com/openai-says-its-new-chatgpt-for-clinicians-outperforms-doctors-on-clinical-tasks-even-when-they-have-unlimited-time-and-web-access/">OpenAI says its new ChatGPT for Clinicians outperforms doctors on clinical tasks even when they have unlimited time and web access</a> appeared first on <a href="https://the-decoder.com">The Decoder</a>.</p>

## 41. Tencent unveils first flagship AI model with former OpenAI researcher at helm
- Domain: scmp.com
- URL: https://www.scmp.com/tech/big-tech/article/3351101/tencent-unveils-first-flagship-ai-model-former-openai-researcher-helm
- Relevance score: 7.3
- Published: Thu, 23 Apr 2026 06:05:17 +0000
- Summary: Tencent Holdings has released a new flagship artificial intelligence model, the first since former OpenAI researcher Yao Shunyu joined the Chinese tech giant to lead its foundational AI development efforts. The Shenzhen-based company said on Thursday that the new model, an open-source program called “Hy3 preview”, was its most powerful yet, on par with top Chinese models but still lagging flagship products from US leaders such as OpenAI and Google DeepMind. Notably, the model is relatively small...

## 42. Can D2C Be ElasticRun’s Most Profitable Bet Yet?
- Domain: inc42.com
- URL: https://inc42.com/features/can-d2c-be-elasticruns-most-profitable-bet-yet/
- Relevance score: 7.3
- Published: Fri, 24 Apr 2026 03:30:15 +0000
- Summary: <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="1020" src="https://inc42.com/cdn-cgi/image/quality=90/https://asset.inc42.com/2026/04/ElasticRun-In-depth.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="1360" />India’s B2B ecommerce segment has rapidly evolved from a fragmented, kirana-led system into a tech-driven, digitised supply chain. But with&#8230;

## 43. Google pitches Agentic Data Cloud to help enterprises turn data into context for AI agents - InfoWorld
- Domain: infoworld.com
- URL: https://news.google.com/rss/articles/CBMi0wFBVV95cUxPc3dwTUJUSkJkMlh4bGsxSzJHREhsbFpiT0JKOEt6dmZlU1ZIelZNMldjd0lQYkpDcnVKdDAwTUhjM09NWmtOWTQtT1hyQ0VwVC1KZlZkVHZCUWZoeEV4NWpiZ1JPVkxReVRrakk2emtnajNScDR6a0E5dnpMZWdoYlYyTkNHbHFEZmZkcnhPNTNsdlEzeHp6bm1rNnlFbTBNTXZhX0FqdWZTakZySVk2VGw1STdkcWp1SDNIQXFwelNPVHotbUhTMjhONnNiSEVpY0hN
- Relevance score: 7.2
- Published: Thu, 23 Apr 2026 16:50:32 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi0wFBVV95cUxPc3dwTUJUSkJkMlh4bGsxSzJHREhsbFpiT0JKOEt6dmZlU1ZIelZNMldjd0lQYkpDcnVKdDAwTUhjM09NWmtOWTQtT1hyQ0VwVC1KZlZkVHZCUWZoeEV4NWpiZ1JPVkxReVRrakk2emtnajNScDR6a0E5dnpMZWdoYlYyTkNHbHFEZmZkcnhPNTNsdlEzeHp6bm1rNnlFbTBNTXZhX0FqdWZTakZySVk2VGw1STdkcWp1SDNIQXFwelNPVHotbUhTMjhONnNiSEVpY0hN?oc=5" target="_blank">Google pitches Agentic Data Cloud to help enterprises turn data into context for AI agents</a>&nbsp;&nbsp;<font color="#6f6f6f">InfoWorld</font>

## 44. It's a big one
- Domain: simonwillison.net
- URL: https://simonwillison.net/2026/Apr/24/weekly/
- Relevance score: 7.2
- Published: 2026-04-24T04:09:54+00:00
- Summary: <p><a href="https://simonw.substack.com/p/gpt-55-chatgpt-images-20-qwen36-27b">This week's edition</a> of my email newsletter (aka <a href="https://simonwillison.net/2023/Apr/4/substack-observable/">content from this blog</a> delivered to your inbox) features 4 pelicans riding bicycles, 1 possum on an e-scooter, up to 5 raccoons with ham radios hiding in crowds, 5 blog posts, 8 links, 3 quotes and a new chapter of my Agentic Engineering Patterns guide.</p> <p>Tags: <a href="https://simonwillison.net/tags/newsletter">newsletter</a></p>

## 45. 融了2000万美金，这家2000万美金ARR的AI公司，推出“视频版Photoshop”「Buzzy」
- Domain: 36kr.com
- URL: https://36kr.com/p/3780352721851397
- Relevance score: 7.2
- Published: 2026-04-24 12:58:37  +0800
- Summary: <p>文｜周鑫雨</p> <p>编辑｜杨轩</p> <h2><strong>一句话介绍</strong></h2> <p>Buzzy（https://www.buzzy.now/）是AI内容创作公司“感知阶跃”旗下的视频编辑Agent平台，主要面向C端内容创作者和中小型商家。</p> <p>好比“视频版的PhotoShop”，用户只需下达自然语言指令，就能驱动Agent对视频进行背景去除、光线修正、产品替换、背景/视角更改等编辑操作。</p> <h2><strong>团队介绍</strong></h2> <p>“感知阶跃”创始人兼CEO Ella Zhang（张诗莹），曾在苹果、Oculus VR、Google负责核心产品。</p> <p>在苹果期间，她曾为AirPods产品线创始团队核心成员，负责产品的系统集成和全周期设计落地，包括音频产品的架构设计、元器件选型、原理图绘制、版图设计、验证以及大规模生产。</p> <p>此后，张诗莹又在Google担任AR产品的系统架构师，负责Glass、Reflector等产品的算法和架构研发。</p> <p>“感知阶跃”其余核心成员，来自Adobe、小米、商汤等公司。</p> <h2><strong>融资进展</strong></h2> <p>近期，“感知阶跃”完成了新一轮融资，<strong>金额超过2000万美元，领投方为Redpoint（红点创投）。</strong>深渡资本担任本轮独家财务顾问。</p> <h2><strong>产品及业务</strong></h2> <p>在张诗莹看来，随着视频生成模型性能的发展，生成类的工具赛道，已经逐渐“红海”。她将市面上的视频创作工具，大致分成了两类：</p> <p>一类是“画布型”产品，优点在于可以通过手动控制，保证生成结果的质量，但缺点是对大多数用户而言，使用门槛高；另一类则是向用户提供预制的workflow和模板，劣势在于不够灵活，同时，idea不够创新。</p> <p>“用户更倾向于一次性生成整段视频，并通过不断迭代修改的方法来修到完美方案。所以一个指哪打哪的视频编辑器就变成了刚需。”</p> <p>当下，由于视频的连贯性以及模型理解能力的局限性，用户很难通过Chat的方式，对视频进行换背景、换人物、消除某元素的“局部精修”。大多AI编辑器会改变整个画面，接近于重新生成。</p> <p>近期，<strong>“感知阶跃”上线的新产品Buzzy，</strong>就是一款AI视频编辑器，让用户可以<strong>像P图一样便捷地“P视频”。</strong></p> <p>只需要通过Chat，Buzzy就可以对视频完成去除背景路人、修正光线、替换产品、合拍、更改背景与视角等操作，真正实现局部精修。</p> <p class="image-wrapper"><img 

## 46. Microsoft Tests Mythos to Identify and Mitigate Vulnerabilities
- Domain: pymnts.com
- URL: https://www.pymnts.com/artificial-intelligence-2/2026/microsoft-tests-mythos-to-identify-and-mitigate-vulnerabilities/
- Relevance score: 7.0
- Published: Wed, 22 Apr 2026 20:34:43 +0000
- Summary: <p>Microsoft is working with Anthropic and other partners through Project Glasswing to test Claude Mythos Preview, the company said in a Wednesday (April 22) blog post. Through this initiative, Microsoft aims to identify vulnerabilities earlier, mitigate them and coordinate a defensive response, according to the post. “We evaluated Mythos using CTI-REALM, our open-source benchmark [&#8230;]</p> <p>The post <a href="https://www.pymnts.com/artificial-intelligence-2/2026/microsoft-tests-mythos-to-identify-and-mitigate-vulnerabilities/">Microsoft Tests Mythos to Identify and Mitigate Vulnerabilities</a> appeared first on <a href="https://www.pymnts.com">PYMNTS.com</a>.</p>

## 47. A museum dedicated to artificial intelligence-driven art opens in downtown LA this summer - Daily Breeze
- Domain: dailybreeze.com
- URL: https://news.google.com/rss/articles/CBMiyAFBVV95cUxOYkg3aGtmQW1selFFY0VEWHFoR0lSNjJOSVdNenpLNVdrUU80SVN4RUQ3MnNQSno3UVJRU2RhRVhSMVA1cy1OSXBlRDVwTWdGVEdoWndyT2hSc25RNWlLNXJObEFSVi1OMWJQV3A4dGx0RVRMR1E4TF9DTGxDTnllLUpFcF9mdm1aSjNKUlpYajBrbHJYS3F3ZkNsS052NkZrdHFRSDJLZl9VaDNjQmhHVGNybENmUUhUZ1VYVy1wQXlCdlZFOVotNg
- Relevance score: 7.0
- Published: Thu, 23 Apr 2026 21:04:51 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiyAFBVV95cUxOYkg3aGtmQW1selFFY0VEWHFoR0lSNjJOSVdNenpLNVdrUU80SVN4RUQ3MnNQSno3UVJRU2RhRVhSMVA1cy1OSXBlRDVwTWdGVEdoWndyT2hSc25RNWlLNXJObEFSVi1OMWJQV3A4dGx0RVRMR1E4TF9DTGxDTnllLUpFcF9mdm1aSjNKUlpYajBrbHJYS3F3ZkNsS052NkZrdHFRSDJLZl9VaDNjQmhHVGNybENmUUhUZ1VYVy1wQXlCdlZFOVotNg?oc=5" target="_blank">A museum dedicated to artificial intelligence-driven art opens in downtown LA this summer</a>&nbsp;&nbsp;<font color="#6f6f6f">Daily Breeze</font>

## 48. Inside China, artificial intelligence is a snake eating its own tail - Defense News
- Domain: defensenews.com
- URL: https://news.google.com/rss/articles/CBMitgFBVV95cUxQVjBrZ0YxVUJDVmhKWFdSaHI1em11UmsxUTlvcXhPZVc1ckw5a1J0UFltWHcwd1pVTGJuRVIyVEFGM25hcURTSFROWFpCd1FWOVkxTktJT25KZVFiMF9wYm5aaGh3bkg3akFZcVFjU0FTbWFjck5Da3YzYmhmSEgta3FsZ1pRLTlpS1NzUG1COUNkbXVwRjFuS1B5WDEySU9Bc1RTRU9WOS1fWVloNTIxLXJEbzJGUQ
- Relevance score: 7.0
- Published: Thu, 23 Apr 2026 13:47:42 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMitgFBVV95cUxQVjBrZ0YxVUJDVmhKWFdSaHI1em11UmsxUTlvcXhPZVc1ckw5a1J0UFltWHcwd1pVTGJuRVIyVEFGM25hcURTSFROWFpCd1FWOVkxTktJT25KZVFiMF9wYm5aaGh3bkg3akFZcVFjU0FTbWFjck5Da3YzYmhmSEgta3FsZ1pRLTlpS1NzUG1COUNkbXVwRjFuS1B5WDEySU9Bc1RTRU9WOS1fWVloNTIxLXJEbzJGUQ?oc=5" target="_blank">Inside China, artificial intelligence is a snake eating its own tail</a>&nbsp;&nbsp;<font color="#6f6f6f">Defense News</font>

## 49. What we lose when artificial intelligence does our shopping - The Conway Daily Sun
- Domain: conwaydailysun.com
- URL: https://news.google.com/rss/articles/CBMi6wFBVV95cUxQTVU2TjdycE1fNkVQWEZSWUZreHVLa3Fpd1NkX2V5SWs4SjhVaWFIbUNTYnJvVHNYeFJYLWdyVV82MWVhTnZsbFdKN2ZQT0wzclpNU3FTU0dTVnQwenQyYmxsc1psVkRLMENvczlkU19rYVExRXJycDkxc05GcHg3VmRhYUc4eU5fN3lfZXJBTTFWakx0R25VYVN3UkJxTWFkTEZQRlpmYlBvT2Ixclg2ZEs3ams1cDViMElnMFEwLTRsRkwxLW8xMTRvaEw3Z3dnSjlMc21vQnkybWtjOF9WSlZ0LWRycEFPRDk0
- Relevance score: 7.0
- Published: Thu, 23 Apr 2026 13:04:12 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi6wFBVV95cUxQTVU2TjdycE1fNkVQWEZSWUZreHVLa3Fpd1NkX2V5SWs4SjhVaWFIbUNTYnJvVHNYeFJYLWdyVV82MWVhTnZsbFdKN2ZQT0wzclpNU3FTU0dTVnQwenQyYmxsc1psVkRLMENvczlkU19rYVExRXJycDkxc05GcHg3VmRhYUc4eU5fN3lfZXJBTTFWakx0R25VYVN3UkJxTWFkTEZQRlpmYlBvT2Ixclg2ZEs3ams1cDViMElnMFEwLTRsRkwxLW8xMTRvaEw3Z3dnSjlMc21vQnkybWtjOF9WSlZ0LWRycEFPRDk0?oc=5" target="_blank">What we lose when artificial intelligence does our shopping</a>&nbsp;&nbsp;<font color="#6f6f6f">The Conway Daily Sun</font>

## 50. Column: AI—Artificial Intelligence or Accidental Idiocy? - CityView NC
- Domain: cityviewnc.com
- URL: https://news.google.com/rss/articles/CBMilAFBVV95cUxOUDhyLUFOVnJJSjhSX2VzdVY1M0JBMFhWVXdjazY0ajIxOVVOMTljSndIVlRralJOc2Z5VWctS1k5R2tqdWZtZk5Bb3hMalNUZ1lPYTZCQVFOamM0MzB4dDJjMzFjSGZDaGxSY0o2cmZWZ19GQUFHTU5ta1N6MDNaZ21TaXZfSUVqQUl4VkNVYnNCaDQy
- Relevance score: 7.0
- Published: Thu, 23 Apr 2026 10:30:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMilAFBVV95cUxOUDhyLUFOVnJJSjhSX2VzdVY1M0JBMFhWVXdjazY0ajIxOVVOMTljSndIVlRralJOc2Z5VWctS1k5R2tqdWZtZk5Bb3hMalNUZ1lPYTZCQVFOamM0MzB4dDJjMzFjSGZDaGxSY0o2cmZWZ19GQUFHTU5ta1N6MDNaZ21TaXZfSUVqQUl4VkNVYnNCaDQy?oc=5" target="_blank">Column: AI—Artificial Intelligence or Accidental Idiocy?</a>&nbsp;&nbsp;<font color="#6f6f6f">CityView NC</font>

## 51. Why agentic AI push hinges on data readiness, not model power - The Edge Singapore
- Domain: theedgesingapore.com
- URL: https://news.google.com/rss/articles/CBMixAFBVV95cUxOSGNXMjdiVnlMMG5HVVIzaGRWSnNlMW9qdFRzcXMtRUNwbmxrb0NTM1NXM090NHZIUmpYX0lXTkFXZzQwU1NVSmg4ZktUTzktcXhMdjdSTGNIYkt3WVVzOU1fdjJ0Z1JtVjVoSXg5VW5RN0hTbG9BVld0eWlfQktfXzhzYklZU1lfbzlYLXFKZ0dFSE9PdWl0bTVqdGJ4ZE5hN0x5SWo2VUt2MDZhTTk2Zi1hd2ZNUDZHMzBQdVBLd0F5NVNO0gHKAUFVX3lxTE1iUFZuRk4tU1daaE1kNDQxd2NRWmNpTDQ5TjhSbXRudlRYQ0o1Skl4aGhCczQ0WXFKQUdEaTNCMW5SR0lmbXljZ01HNlJSdERScUFKZFd5TXVuM1FabmRwVkp1UmV1bGQ1dGltOWhuMkVWd3JxVnJCT3VYeXJQQjFQZVo2VVdWWnY1NTk2Z21oVkRpaXBnZGdydlVOTDlhQ0x4ek9oYVJmVUhhZndKbEIwaGowVi1GcU85bERqRXFWZzlZLXh0cmQwdkE
- Relevance score: 7.0
- Published: Fri, 24 Apr 2026 02:10:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMixAFBVV95cUxOSGNXMjdiVnlMMG5HVVIzaGRWSnNlMW9qdFRzcXMtRUNwbmxrb0NTM1NXM090NHZIUmpYX0lXTkFXZzQwU1NVSmg4ZktUTzktcXhMdjdSTGNIYkt3WVVzOU1fdjJ0Z1JtVjVoSXg5VW5RN0hTbG9BVld0eWlfQktfXzhzYklZU1lfbzlYLXFKZ0dFSE9PdWl0bTVqdGJ4ZE5hN0x5SWo2VUt2MDZhTTk2Zi1hd2ZNUDZHMzBQdVBLd0F5NVNO0gHKAUFVX3lxTE1iUFZuRk4tU1daaE1kNDQxd2NRWmNpTDQ5TjhSbXRudlRYQ0o1Skl4aGhCczQ0WXFKQUdEaTNCMW5SR0lmbXljZ01HNlJSdERScUFKZFd5TXVuM1FabmRwVkp1UmV1bGQ1dGltOWhuMkVWd3JxVnJCT3VYeXJQQjFQZVo2VVdWWnY1NTk2Z21oVkRpaXBnZGdydlVOTDlhQ0x4ek9oYVJmVUhhZndKbEIwaGowVi1GcU85bERqRXFWZzlZLXh0cmQwdkE?oc=5" target="_blank">Why agentic AI push hinges on data readiness, not model power</a>&nbsp;&nbsp;<font color="#6f6f6f">The Edge Singapore</font>

## 52. Trump science advisor says Chinese actors are copying American AI at massive scale
- Domain: the-decoder.com
- URL: https://the-decoder.com/trump-science-advisor-says-chinese-actors-are-copying-american-ai-at-massive-scale/
- Relevance score: 6.8
- Published: Thu, 23 Apr 2026 18:04:39 +0000
- Summary: <p><img alt="" class="attachment-full size-full wp-post-image" height="768" src="https://the-decoder.com/wp-content/uploads/2026/03/us_flag_wireframe.png" style="height: auto; margin-bottom: 10px;" width="1376" /></p> <p> The US government says it has evidence of large-scale, industrial distillation campaigns targeting American frontier models, with China as the primary culprit. Now the Trump administration is moving to fight back.</p> <p>The article <a href="https://the-decoder.com/trump-science-advisor-says-chinese-actors-are-copying-american-ai-at-massive-scale/">Trump science advisor says Chinese actors are copying American AI at massive scale</a> appeared first on <a href="https://the-decoder.com">The Decoder</a>.</p>

## 53. Huawei doubles down on autonomous driving, earmarking US$11.7b for autopilot training
- Domain: scmp.com
- URL: https://www.scmp.com/business/china-business/article/3351242/huawei-doubles-down-autonomous-driving-earmarking-us117b-autopilot-training
- Relevance score: 6.8
- Published: Fri, 24 Apr 2026 03:39:33 +0000
- Summary: Adamant about retaining its runaway lead in supplying smart driving systems in China, Huawei Technologies plans to invest as much as 80 billion yuan (US$11.7 billion) over the next five years to boost computing power essential for training and testing semi-autonomous cars. The massive capital expenditure would enhance the reliability of cars fitted with the Huawei Qiankun ADS autopilot system, as the Shenzhen-based tech giant looked to expand its customer base, said Jin Yuzhi, CEO of Huawei’s...

## 54. The role of AI in modern forex bot development
- Domain: artificialintelligence-news.com
- URL: https://www.artificialintelligence-news.com/news/the-role-of-ai-in-modern-forex-bot-development/
- Relevance score: 6.7
- Published: Wed, 22 Apr 2026 07:34:01 +0000
- Summary: <p>Artificial intelligence has become a defining force in financial markets. And currency trading is no exception. The rise of the AI-powered forex bot reflects a change toward automated systems capable of processing vast amounts of market data and identifying patterns beyond the reach of manual analysis. As global foreign exchange markets operate around the clock [&#8230;]</p> <p>The post <a href="https://www.artificialintelligence-news.com/news/the-role-of-ai-in-modern-forex-bot-development/">The role of AI in modern forex bot development</a> appeared first on <a href="https://www.artificialintelligence-news.com">AI News</a>.</p>

## 55. The agentic AI frenzy increases as more vendors stake their claims - InfoWorld
- Domain: infoworld.com
- URL: https://news.google.com/rss/articles/CBMiswFBVV95cUxNTlhFYjNYTVpqS2pxczJITzkwZUlzLXFQS2lpd2MtU2laMWRJTDB2VmYwaVB3YmZNdmstU1dyUmJZQ3BtVlFhZ0tfT05YZGxiMldmTWh2S29ZYXRBUmUyR3BmajBOZzFaclhsT3hIYUdCbTEtMTlRSkpHOXpsY3pNUUw5cVpGa0o3YkZNWEtqMHRaSVJmMTRTNXdZWXVmRHFNdWxyZUN6ZHNwVXNSdElwY0JqRQ
- Relevance score: 6.7
- Published: Fri, 24 Apr 2026 01:18:42 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiswFBVV95cUxNTlhFYjNYTVpqS2pxczJITzkwZUlzLXFQS2lpd2MtU2laMWRJTDB2VmYwaVB3YmZNdmstU1dyUmJZQ3BtVlFhZ0tfT05YZGxiMldmTWh2S29ZYXRBUmUyR3BmajBOZzFaclhsT3hIYUdCbTEtMTlRSkpHOXpsY3pNUUw5cVpGa0o3YkZNWEtqMHRaSVJmMTRTNXdZWXVmRHFNdWxyZUN6ZHNwVXNSdElwY0JqRQ?oc=5" target="_blank">The agentic AI frenzy increases as more vendors stake their claims</a>&nbsp;&nbsp;<font color="#6f6f6f">InfoWorld</font>

## 56. Google puts AI agents at heart of its enterprise money-making push - Taipei Times
- Domain: taipeitimes.com
- URL: https://news.google.com/rss/articles/CBMidkFVX3lxTE1KckdUWDFWZVRrVndrRXpIc0ExNU5MZHdQc3daZDRDSFhYN0FoYllzYkp5cC1aX0VCc1lFS3FMQVd5eXVnV2M1QTFzSEcwZEtoeFJIZ2VxQ0xKVmYwR25rOXJ0VDl6NXY4MDVXODFET29pRVh5b3c
- Relevance score: 6.5
- Published: Wed, 22 Apr 2026 16:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE1KckdUWDFWZVRrVndrRXpIc0ExNU5MZHdQc3daZDRDSFhYN0FoYllzYkp5cC1aX0VCc1lFS3FMQVd5eXVnV2M1QTFzSEcwZEtoeFJIZ2VxQ0xKVmYwR25rOXJ0VDl6NXY4MDVXODFET29pRVh5b3c?oc=5" target="_blank">Google puts AI agents at heart of its enterprise money-making push</a>&nbsp;&nbsp;<font color="#6f6f6f">Taipei Times</font>

## 57. Bret Taylor’s Sierra buys YC-backed AI startup Fragment
- Domain: techcrunch.com
- URL: https://techcrunch.com/2026/04/23/bret-taylors-sierra-buys-yc-backed-ai-startup-fragment/
- Relevance score: 6.5
- Published: Thu, 23 Apr 2026 21:00:00 +0000
- Summary: Sierra, the AI customer service agent startup founded by technologist Bret Taylor, announced today that it has acquired the YC-backed French startup Fragment.

## 58. Meta to lay off 8,000 as part of AI efficiency push
- Domain: axios.com
- URL: https://www.axios.com/2026/04/23/meta-layoffs-ai-efficiency-push
- Relevance score: 6.5
- Published: Thu, 23 Apr 2026 19:54:02 +0000
- Summary: <p><a href="https://www.axios.com/2026/03/31/meta-layoffs-ai-spending-efficiency" target="_blank">Meta</a> told staff Thursday it plans to lay off roughly 8,000 people, or around 10% of the company, two sources confirmed to Axios. </p><p><strong>Why it matters:</strong> The cuts underscore how soaring AI costs are pressuring even the biggest tech companies to cut jobs to protect margins and reassure investors.</p><hr /><p><strong>Zoom out:</strong> Meta's <a href="https://www.axios.com/2026/01/28/meta-earnings-outlook-ai-spending" target="_blank">capital expenditures</a> have ballooned in recent years, sparking investor concerns that excessive AI spending will eat into profits.</p><ul><li>In January, the company <a href="https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx" target="_blank">said</a> it expects capital expenditures to soar by at least 60% this year compared with 2025, "driven by increased investment to support our Meta Superintelligence Labs efforts and core business."</li><li>Free cash flow, meanwhile, is expected to plunge 83% year over year.</li></ul><p><strong>Reality check:</stro

## 59. What to know about the missing scientists alarming Congress
- Domain: axios.com
- URL: https://www.axios.com/2026/04/23/missing-scientists-space-nuclear-congress-investigating
- Relevance score: 6.5
- Published: Thu, 23 Apr 2026 17:02:50 +0000
- Summary: <p>The disappearances and <a href="https://www.axios.com/2025/12/17/police-mit-professor-shooting-brookline-ma-nuno-loureiro" target="_blank">deaths</a> of at least 10 scientists, researchers and staffers who worked on nuclear and space programs are raising alarms on Capitol Hill. </p><p><strong>The big picture:</strong> The cases date back to at least 2023, but national security concerns prompted a <a href="https://www.axios.com/2026/04/08/pam-bondi-epstein-house-oversight-subpoena" target="_blank">House Oversight Committee</a> investigation. </p><hr /><ul><li>Chairman James Comer (R-Ky.) and Rep. Eric Burlison (R-Mo.) <a href="https://oversight.house.gov/release/comer-burlison-seek-information-on-missing-nuclear-and-rocket-scientists/" target="_blank">sent letters</a> to FBI Director Kash Patel, NASA administrator Jared Isaacman, Energy Secretary Chris Wright and Defense Secretary Pete Hegseth, seeking information on the deaths and disappearances, and "the processes and procedures in place to protect American scientific secrets and ensure personnel safety."</li></ul><h2>What prompted the probe?</h2><p><strong>The committee's letter</strong> did not cite a specific reason for the 

## 60. Another customer of troubled startup Delve suffered a big security incident
- Domain: techcrunch.com
- URL: https://techcrunch.com/2026/04/23/another-customer-of-troubled-startup-delve-suffered-a-big-security-incident/
- Relevance score: 6.5
- Published: Thu, 23 Apr 2026 14:00:00 +0000
- Summary: TechCrunch has confirmed that Delve was the compliance company that performed the security certifications for Context AI, the AI agent training startup that last week disclosed a security incident.

## 61. AI Designs Thermoelectric Generators 10,000 Times Faster Than We Can
- Domain: spectrum.ieee.org
- URL: https://spectrum.ieee.org/ai-designed-thermoelectric-generator
- Relevance score: 6.5
- Published: Thu, 23 Apr 2026 11:00:01 +0000
- Summary: <img src="https://spectrum.ieee.org/media-library/an-n-p-pair-consisting-of-two-silver-columns-of-material-sits-in-a-gold-vise-like-device-copper-colored-ribbons-come-from-bel.jpg?id=65560088&amp;width=1245&amp;height=700&amp;coordinates=0%2C62%2C0%2C63" /><br /><br /><p><em></em>Waste heat is everywhere: car engines, <a href="https://spectrum.ieee.org/a-thermoelectric-generator-that-runs-on-exhaust-fumes" target="_self">industrial machinery</a>, kitchen appliances—even <a href="https://spectrum.ieee.org/a-thermoelectric-generator-for-wearable-tech" target="_blank">your own body</a>. Some of that lost energy can be converted into electricity using thermoelectric generators: compact, solid-state devices that produce power directly from temperature differences without the need for spinning turbines or moving parts.</p><p>But designing materials that make these systems efficient has long been an engineering slog, requiring slow simulations and painstaking experiments to identify combinations that conduct electricity while blocking heat.</p><p>Now researchers in Japan have built an <a href="https://doi.org/10.1038/s41586-026-10223-1" rel="noopener noreferrer" target="_blank">artificial

## 62. China's DeepSeek unveils V4 AI model in fresh challenge to US rivals - Nikkei Asia
- Domain: asia.nikkei.com
- URL: https://news.google.com/rss/articles/CBMi0gFBVV95cUxOUEV5V3o4QmROdmdsUjhOYWtUbm9IRE1ValRjQUxxWUtMRTRvQUJBNzVEU3NGM1N1WHgxSll3Z2dETUtrbUVrNkkxa0F6YWctazZNMEpGNnpIdG5WbUlzc0g5M3p0Rk1DNlJOMUN4SGN6engxV2tnMkR4OVo0ZmFVX3ZvU3loYmZZaEtoSVd4c2FJVzhwUWkwQmcxdzFzX3VOODZTTm9WM0tXb1RObnlSSV9zT3JSdEFyZnhvZ1loazFwM2dfLXBHTUY2b3hBbDZ4SUE
- Relevance score: 6.2
- Published: Fri, 24 Apr 2026 04:52:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi0gFBVV95cUxOUEV5V3o4QmROdmdsUjhOYWtUbm9IRE1ValRjQUxxWUtMRTRvQUJBNzVEU3NGM1N1WHgxSll3Z2dETUtrbUVrNkkxa0F6YWctazZNMEpGNnpIdG5WbUlzc0g5M3p0Rk1DNlJOMUN4SGN6engxV2tnMkR4OVo0ZmFVX3ZvU3loYmZZaEtoSVd4c2FJVzhwUWkwQmcxdzFzX3VOODZTTm9WM0tXb1RObnlSSV9zT3JSdEFyZnhvZ1loazFwM2dfLXBHTUY2b3hBbDZ4SUE?oc=5" target="_blank">China's DeepSeek unveils V4 AI model in fresh challenge to US rivals</a>&nbsp;&nbsp;<font color="#6f6f6f">Nikkei Asia</font>

## 63. 海光C86全栈产品与解决方案亮相第87届教育装备展
- Domain: 36kr.com
- URL: https://36kr.com/newsflashes/3780303367214341
- Relevance score: 6.2
- Published: 2026-04-24 12:25:21  +0800
- Summary: 36氪获悉，4月24日，在第87届中国教育装备展示会上，海光信息携手联想开天、东孚教育等生态伙伴参展，全面展示基于C86算力底座的“AI+教育”解决方案。据海光信息教育行业总经理余哲介绍，海光信息与同济大学共建��全国高校首个GPGPU千卡算力集群也将于5月正式上线。

## 64. Google explains why its all-in-one AI stack embraces competitors
- Domain: go.theregister.com
- URL: https://go.theregister.com/feed/www.theregister.com/2026/04/23/google_cloud_next_interview_ai_stack/
- Relevance score: 6.2
- Published: 2026-04-23T17:13:36.00Z
- Summary: <h4>'Differentiated, but open'</h4> <p><strong>Google Cloud Next</strong> Google Cloud’s Andi Gutmans said that the company holds a structural advantage over its largest rivals in the race to win value from AI agents in the enterprise, arguing that no competitor currently combines cloud computing infrastructure, frontier AI models, and a data platform under one roof.…</p>

## 65. Musk bets Tesla's AI future on Intel node that isn't finished yet
- Domain: go.theregister.com
- URL: https://go.theregister.com/feed/www.theregister.com/2026/04/23/musk_bets_teslas_ai_future/
- Relevance score: 6.2
- Published: 2026-04-23T11:43:12.00Z
- Summary: <h4>EV maker leaning on still-in-development 14A process for Terafab, says it needs to build own silicon</h4> <p>Elon Musk used Tesla's latest earnings call to reveal plans to build AI chips on Intel's not-yet-finished 14A process – a bet on silicon that doesn't exist.…</p> <p><!--#include virtual='/data_centre/_whitepaper_textlinks_top.html' --></p>

## 66. Fact Check Team: Exploring the evolution of artificial intelligence regulations - KVII
- Domain: abc7amarillo.com
- URL: https://news.google.com/rss/articles/CBMijAJBVV95cUxOOXFleWNuUkJ1bHFHUDNLZEtrNFp1ZmpzUUN3Y01xMEVDaS0tUnVKSElDanJBN0FJeWhqNFQ4UGZMM3Q1ZFZQdndyRmxUQmdMSWIyelB0Q0UxanJRUUNZRmd5bXZSei1xdkdwLUhITFVSR3VVcW9wdUh4MGdmQmsyLU4ybWVvaUtHT2VKOUtlbjRLbDBjLVhjUWxQYnJLOU9icmk3MXktM3VHNGxKNkpiT1gzV2ROSTlYWjlXVGlqTVBjcG9feTY2c0xmaDh2U0txT2dsbEw4VzRRM2pxV1VVOU1wU1EwUmc2RmdhSF82SUFBdlE2dzBIeEx6VzlobEYwTVppR3NzYVFhRVdI
- Relevance score: 6.0
- Published: Thu, 23 Apr 2026 23:33:31 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMijAJBVV95cUxOOXFleWNuUkJ1bHFHUDNLZEtrNFp1ZmpzUUN3Y01xMEVDaS0tUnVKSElDanJBN0FJeWhqNFQ4UGZMM3Q1ZFZQdndyRmxUQmdMSWIyelB0Q0UxanJRUUNZRmd5bXZSei1xdkdwLUhITFVSR3VVcW9wdUh4MGdmQmsyLU4ybWVvaUtHT2VKOUtlbjRLbDBjLVhjUWxQYnJLOU9icmk3MXktM3VHNGxKNkpiT1gzV2ROSTlYWjlXVGlqTVBjcG9feTY2c0xmaDh2U0txT2dsbEw4VzRRM2pxV1VVOU1wU1EwUmc2RmdhSF82SUFBdlE2dzBIeEx6VzlobEYwTVppR3NzYVFhRVdI?oc=5" target="_blank">Fact Check Team: Exploring the evolution of artificial intelligence regulations</a>&nbsp;&nbsp;<font color="#6f6f6f">KVII</font>

## 67. Insurance Denials Meet Their Match in AI-Powered Appeals
- Domain: pymnts.com
- URL: https://www.pymnts.com/artificial-intelligence-2/2026/insurance-denials-meet-their-match-in-ai-powered-appeals/
- Relevance score: 6.0
- Published: Thu, 23 Apr 2026 20:38:48 +0000
- Summary: <p>A patient is denied coverage for a drug he has taken for 18 years. His insurer says he should try a cheaper alternative. He finds an AI tool, submits his case and sends the resulting letter to his insurer. The denial is reversed before the end of the day. That outcome is still rare. [&#8230;]</p> <p>The post <a href="https://www.pymnts.com/artificial-intelligence-2/2026/insurance-denials-meet-their-match-in-ai-powered-appeals/">Insurance Denials Meet Their Match in AI-Powered Appeals</a> appeared first on <a href="https://www.pymnts.com">PYMNTS.com</a>.</p>

## 68. Groq’s Inference Chips Are Beating NVIDIA’s Blackwell by 5x on Cost – And Doing It Twice as Fast - Wccftech
- Domain: wccftech.com
- URL: https://news.google.com/rss/articles/CBMitwFBVV95cUxNYWQ3WUxyczZJSVpSeGJrSmdIaFBQZEZXcHk1M0ZQTGNlVWt2MDVsanoxWEZnYUtCV2d4WThvdlVhWW83ZVJ6NWc1bHZ1NkV3TkZkSDBVS29PRGFYb1ZaQ0t3VFV3cnVtbUZmYjV2dlRvZlZ6Zm5pVWNrVXgzUkd6bFEtQ0M4WmQ2MkdpbUEzQ0FKY2dSYUE0a2JrYTZ2SW9YOVZDRW1TU2ZCM016TkxqcUFrYlVUMlnSAbwBQVVfeXFMTWZLaDB5Q2ZvLUNabDhfVWlCWHJBVjJoeS1ENnIxSnBZS0VPZjdFM2N4OFFyVzVEZ2MyVWFQMlYtOGJISVlfb29teGVmM1hlV1ZMRnNUMTlONjRnSTFscU1OeWs2Zi1XaXRSN1JqekphSThXZlYtMGpPUHN6OGpEa0gydnBkRm94dTdJYXdpQnl0VlYwQVZGUmRjWDlWV0pHdmFieGR2VzNIamlqVmRFM1ZEYVlaaG1SaW9SbWg
- Relevance score: 6.0
- Published: Thu, 23 Apr 2026 19:52:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMitwFBVV95cUxNYWQ3WUxyczZJSVpSeGJrSmdIaFBQZEZXcHk1M0ZQTGNlVWt2MDVsanoxWEZnYUtCV2d4WThvdlVhWW83ZVJ6NWc1bHZ1NkV3TkZkSDBVS29PRGFYb1ZaQ0t3VFV3cnVtbUZmYjV2dlRvZlZ6Zm5pVWNrVXgzUkd6bFEtQ0M4WmQ2MkdpbUEzQ0FKY2dSYUE0a2JrYTZ2SW9YOVZDRW1TU2ZCM016TkxqcUFrYlVUMlnSAbwBQVVfeXFMTWZLaDB5Q2ZvLUNabDhfVWlCWHJBVjJoeS1ENnIxSnBZS0VPZjdFM2N4OFFyVzVEZ2MyVWFQMlYtOGJISVlfb29teGVmM1hlV1ZMRnNUMTlONjRnSTFscU1OeWs2Zi1XaXRSN1JqekphSThXZlYtMGpPUHN6OGpEa0gydnBkRm94dTdJYXdpQnl0VlYwQVZGUmRjWDlWV0pHdmFieGR2VzNIamlqVmRFM1ZEYVlaaG1SaW9SbWg?oc=5" target="_blank">Groq’s Inference Chips Are Beating NVIDIA’s Blackwell by 5x on Cost – And Doing It Twice as Fast</a>&nbsp;&nbsp;<font color="#6f6f6f">Wccftech</font>

## 69. Pentagon workers vibe-code 100,000 AI ‘agents’ to use on unclassified networks - Breaking Defense
- Domain: breakingdefense.com
- URL: https://news.google.com/rss/articles/CBMisgFBVV95cUxOX3NqQVVpVXVIMDJ2M0NUTlJuNDVPY20wUmZBZlNJZzNCcmlWVVY1R0RQM0cyTks2a1dBSDhZWkFqS0hkRk9BSkNPcF9yR0I5YlBhU1EtYW9nb0dJalFvR2djYjdXa1lvSFVVaUtIeHlfZkJRSC1tNkFRSmFudmd6SG5aSGkyYWZ1Z3k2WWVDakE3Ym5VajFZaE43dFNKajVLRU9ZT2RxTkV1VVJ3LWhLRjd3
- Relevance score: 6.0
- Published: Thu, 23 Apr 2026 17:56:24 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMisgFBVV95cUxOX3NqQVVpVXVIMDJ2M0NUTlJuNDVPY20wUmZBZlNJZzNCcmlWVVY1R0RQM0cyTks2a1dBSDhZWkFqS0hkRk9BSkNPcF9yR0I5YlBhU1EtYW9nb0dJalFvR2djYjdXa1lvSFVVaUtIeHlfZkJRSC1tNkFRSmFudmd6SG5aSGkyYWZ1Z3k2WWVDakE3Ym5VajFZaE43dFNKajVLRU9ZT2RxTkV1VVJ3LWhLRjd3?oc=5" target="_blank">Pentagon workers vibe-code 100,000 AI ‘agents’ to use on unclassified networks</a>&nbsp;&nbsp;<font color="#6f6f6f">Breaking Defense</font>

## 70. LangChain.js for Beginners: A Free Course to Build Agentic AI Apps with JavaScript
- Domain: devblogs.microsoft.com
- URL: https://devblogs.microsoft.com/blog/langchainjs-for-beginners
- Relevance score: 6.0
- Published: Thu, 23 Apr 2026 17:00:14 +0000
- Summary: <p>Want to build AI agents with JavaScript that go beyond basic chat completions? Agents that reason, call tools, and pull from knowledge bases on their own? We put together a free, open source course to help you get there. LangChain.js for Beginners is 8 chapters and 70+ runnable TypeScript examples. Clone the repo, add your [&#8230;]</p> <p>The post <a href="https://devblogs.microsoft.com/blog/langchainjs-for-beginners">LangChain.js for Beginners: A Free Course to Build Agentic AI Apps with JavaScript</a> appeared first on <a href="https://devblogs.microsoft.com">Microsoft for Developers</a>.</p>

## 71. Cet agent IA a ouvert sa propre boutique, mais a oublié un détail absurde le jour J - Numerama
- Domain: numerama.com
- URL: https://news.google.com/rss/articles/CBMixwFBVV95cUxOaWJ2UjFPN1RETE9UVUJZdklmbTdFd0xtcVYxaFZzUTFrYnVkczk3WkNsVi11WkdHd0RpNUp2ellheTVuVDhfSmdISmw5Qi1RYURpOHpzenZ0M1JQay1PenhVeW9FNDNCTGtxUlZPem1BcmJaVG1QU2hHdFJKUTFlTld6eUlac0hJOE1BYVNMb2JXME5iOUJmU2FQcS1nNmZucVkyOTRKd2pCNlMyOGpacVB6TGN1V19ZclowZ0ZfUmlNbHpneGNz
- Relevance score: 6.0
- Published: Thu, 23 Apr 2026 16:34:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMixwFBVV95cUxOaWJ2UjFPN1RETE9UVUJZdklmbTdFd0xtcVYxaFZzUTFrYnVkczk3WkNsVi11WkdHd0RpNUp2ellheTVuVDhfSmdISmw5Qi1RYURpOHpzenZ0M1JQay1PenhVeW9FNDNCTGtxUlZPem1BcmJaVG1QU2hHdFJKUTFlTld6eUlac0hJOE1BYVNMb2JXME5iOUJmU2FQcS1nNmZucVkyOTRKd2pCNlMyOGpacVB6TGN1V19ZclowZ0ZfUmlNbHpneGNz?oc=5" target="_blank">Cet agent IA a ouvert sa propre boutique, mais a oublié un détail absurde le jour J</a>&nbsp;&nbsp;<font color="#6f6f6f">Numerama</font>

## 72. U.S. accuses China of "industrial-scale" campaigns to steal AI secrets
- Domain: axios.com
- URL: https://www.axios.com/2026/04/23/us-china-ai-theft-distillation
- Relevance score: 6.0
- Published: Thu, 23 Apr 2026 16:17:46 +0000
- Summary: <p>The <a href="https://www.axios.com/politics-policy/donald-trump" target="_blank">Trump</a> administration on Thursday accused China-backed actors of running "deliberate, industrial-scale campaigns" to distill and copy American frontier <a href="https://www.axios.com/2026/04/22/anthropic-no-kill-switch-ai-classified-settings" target="_blank">AI models</a>.</p><p><strong>Why it matters: </strong>The accusation pushes the <a href="https://www.axios.com/2025/09/18/white-house-ai-race-china" target="_blank">U.S.-China AI rivalry</a> into more confrontational territory — and could complicate President Trump's upcoming visit to Beijing.</p><hr /><p><strong>Driving the news:</strong> Michael Kratsios, director of the White House Office of Science and Technology Policy, sent a <a href="https://whitehouse.gov/wp-content/uploads/2026/04/NSTM-4.pdf" target="_blank">memo</a> Thursday to federal agency heads accusing mostly China-based actors of using proxy accounts to evade detection and jailbreak models to "expose proprietary information" and "extract capabilities from American AI models."</p><ul><li>Distillation attacks involve querying proprietary models, like Claude or Gemini, millions o

## 73. Meta licencie 10% de son personnel et va analyser le travail des employés restants pour entraîner des agents IA... qui pourraient un jour les remplacer - L'Usine Digitale
- Domain: usine-digitale.fr
- URL: https://news.google.com/rss/articles/CBMixgJBVV95cUxNeDRfdnZOc1NBSTQ1dmJYX2RabmNyakhIYmM2SlRSMDBQdGtLVFBQVjZxcTZpYmVuR0RCVGNibGYtTWpIUENrWkZBbTU2YkVjUHpOa1dLOHI4REFGaXlta1BpY1U0UDRibXg1STlxc0pVZmhDSFRWUVdLV3Y2NEp2dV8zaEs3UWo3TUZsSkJ2OFpkUWd2VDh0SlRtYWlEWDdKTG53eXNfdXZ3UG8xY3puaVNWSnZGTjRoVlhnenhxLW1ubzhwc3hZSUU3MFpGei1QaGhPdktHMURGSmNTZVpSUUh2Y2Q2UlBiRHVQUktSSzZiSnFOOTBYeC16S1V3TDFUWGNKd2cyNUZNa0x4RThZMXd4T1FMem43aUZlOU1zYTZ5a1BkYnVycEVvZUZHeFRFXzJOeklIaWZVNk03MWU4ajBTSzVzZw
- Relevance score: 6.0
- Published: Fri, 24 Apr 2026 04:00:01 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMixgJBVV95cUxNeDRfdnZOc1NBSTQ1dmJYX2RabmNyakhIYmM2SlRSMDBQdGtLVFBQVjZxcTZpYmVuR0RCVGNibGYtTWpIUENrWkZBbTU2YkVjUHpOa1dLOHI4REFGaXlta1BpY1U0UDRibXg1STlxc0pVZmhDSFRWUVdLV3Y2NEp2dV8zaEs3UWo3TUZsSkJ2OFpkUWd2VDh0SlRtYWlEWDdKTG53eXNfdXZ3UG8xY3puaVNWSnZGTjRoVlhnenhxLW1ubzhwc3hZSUU3MFpGei1QaGhPdktHMURGSmNTZVpSUUh2Y2Q2UlBiRHVQUktSSzZiSnFOOTBYeC16S1V3TDFUWGNKd2cyNUZNa0x4RThZMXd4T1FMem43aUZlOU1zYTZ5a1BkYnVycEVvZUZHeFRFXzJOeklIaWZVNk03MWU4ajBTSzVzZw?oc=5" target="_blank">Meta licencie 10% de son personnel et va analyser le travail des employés restants pour entraîner des agents IA... qui pourraient un jour les remplacer</a>&nbsp;&nbsp;<font color="#6f6f6f">L'Usine Digitale</font>

## 74. AI-Driven Multiagent System for Guiding First-Line Immunotherapy for NSCLC - The ASCO Post
- Domain: ascopost.com
- URL: https://news.google.com/rss/articles/CBMiuAFBVV95cUxOTGlyZmppWTJOTXU3eTRSd0pCRFFKcUVZUkRwa1dpd2RfbEZ6SUs0SGpiQjFzMHJscTlmZ2VpT00zdmlyanZfUTFUU2dKTkZqYVJ2cHlGeTB3cVdHd2kwZ1k2amVGTVNGN1kxZnUxTW9ycGl5cHFXMzRSTVhtcTZkMDhxckNvTU85UVBlM2UtZTNQQ050bkRlbnVQREJRaWJYX3Rkc3JaTjdhc0pXVDZaN0V6TDRjS1p5
- Relevance score: 6.0
- Published: Fri, 24 Apr 2026 01:36:35 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiuAFBVV95cUxOTGlyZmppWTJOTXU3eTRSd0pCRFFKcUVZUkRwa1dpd2RfbEZ6SUs0SGpiQjFzMHJscTlmZ2VpT00zdmlyanZfUTFUU2dKTkZqYVJ2cHlGeTB3cVdHd2kwZ1k2amVGTVNGN1kxZnUxTW9ycGl5cHFXMzRSTVhtcTZkMDhxckNvTU85UVBlM2UtZTNQQ050bkRlbnVQREJRaWJYX3Rkc3JaTjdhc0pXVDZaN0V6TDRjS1p5?oc=5" target="_blank">AI-Driven Multiagent System for Guiding First-Line Immunotherapy for NSCLC</a>&nbsp;&nbsp;<font color="#6f6f6f">The ASCO Post</font>

## 75. OpenAI's new Trusted Access program gives Microsoft its most capable models for cyber defense
- Domain: the-decoder.com
- URL: https://the-decoder.com/openais-new-trusted-access-program-gives-microsoft-its-most-capable-models-for-cyber-defense/
- Relevance score: 5.8
- Published: Thu, 23 Apr 2026 16:09:29 +0000
- Summary: <p><img alt="" class="attachment-full size-full wp-post-image" height="768" src="https://the-decoder.com/wp-content/uploads/2026/04/microsoft_chatgpt.png" style="height: auto; margin-bottom: 10px;" width="1376" /></p> <p> OpenAI and Microsoft are joining forces to shore up cybersecurity as AI models become a bigger threat. The debate started with Anthropic's Mythos model, which is designed to hunt down security flaws on its own.</p> <p>The article <a href="https://the-decoder.com/openais-new-trusted-access-program-gives-microsoft-its-most-capable-models-for-cyber-defense/">OpenAI&#039;s new Trusted Access program gives Microsoft its most capable models for cyber defense</a> appeared first on <a href="https://the-decoder.com">The Decoder</a>.</p>

## 76. Zerodha Pivots Creator-Led Zero1 To In-House Content Model
- Domain: inc42.com
- URL: https://inc42.com/buzz/zerodha-pivots-creator-led-zero1-to-in-house-content-model/
- Relevance score: 5.8
- Published: Thu, 23 Apr 2026 16:06:50 +0000
- Summary: <img alt="Zerodha Raises F&amp;O Charges To ₹40 Per Order For Certain Intraday Trades" class="webfeedsFeaturedVisual wp-post-image" height="1020" src="https://inc42.com/cdn-cgi/image/quality=90/https://asset.inc42.com/2026/03/zerodha-crisis-featured.png" style="display: block; margin: auto; margin-bottom: 5px;" width="1360" />Zero1 Network, a new-age media joint venture between Zerodha and LearnApp, is pivoting its business from its erstwhile model of&#8230;

## 77. OpenAI releases open-source model that strips personal data from text
- Domain: the-decoder.com
- URL: https://the-decoder.com/openai-releases-open-source-model-that-strips-personal-data-from-text/
- Relevance score: 5.8
- Published: Thu, 23 Apr 2026 13:53:13 +0000
- Summary: <p><img alt="" class="attachment-full size-full wp-post-image" height="768" src="https://the-decoder.com/wp-content/uploads/2026/04/Privacy-Filter.png" style="height: auto; margin-bottom: 10px;" width="1376" /></p> <p> OpenAI has released Privacy Filter, an open-source model designed to detect and redact personal data in text.</p> <p>The article <a href="https://the-decoder.com/openai-releases-open-source-model-that-strips-personal-data-from-text/">OpenAI releases open-source model that strips personal data from text</a> appeared first on <a href="https://the-decoder.com">The Decoder</a>.</p>

## 78. L&T Incorporates AI Data Centre Subsidiary Vyoma.AI
- Domain: inc42.com
- URL: https://inc42.com/buzz/lt-incorporates-ai-data-centre-subsidiary-vyoma-ai/
- Relevance score: 5.8
- Published: Thu, 23 Apr 2026 13:08:19 +0000
- Summary: <img alt="l&amp;t vyoma.ai data centre" class="webfeedsFeaturedVisual wp-post-image" height="1020" src="https://inc42.com/cdn-cgi/image/quality=90/https://asset.inc42.com/2026/04/LT-AI-ft.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="1360" />Indian infrastructure giant L&#38;T (Larsen &#38; Toubro) has incorporated a wholly owned subsidiary Vyoma.AI ltd in India formed to launch&#8230;

## 79. Inside The Legal Battle Between IPO-Bound RentoMojo & Cofounder Ajay Nain
- Domain: inc42.com
- URL: https://inc42.com/buzz/inside-the-legal-battle-between-ipo-bound-rentomojo-cofounder-ajay-nain/
- Relevance score: 5.8
- Published: Thu, 23 Apr 2026 12:23:51 +0000
- Summary: <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="1020" src="https://inc42.com/cdn-cgi/image/quality=90/https://asset.inc42.com/2026/04/ftr-21.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="1360" />Ajay Nain, cofounder and former COO of RentoMojo, has alleged in a petition before the NCLT’s Bengaluru bench that he&#8230;

## 80. UPI In March: PhonePe Tightens Grip At Top As Transactions Cross 1,000 Cr Mark
- Domain: inc42.com
- URL: https://inc42.com/buzz/upi-in-march-phonepe-tightens-grip-at-top-as-transactions-cross-1000-cr-mark/
- Relevance score: 5.8
- Published: Thu, 23 Apr 2026 08:34:43 +0000
- Summary: <img alt="UPI In March: PhonePe Tightens Grip At Top As Transactions Cross 1,000 Cr Mark" class="webfeedsFeaturedVisual wp-post-image" height="1020" src="https://inc42.com/cdn-cgi/image/quality=90/https://asset.inc42.com/2026/04/UPI-ftr.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="1360" />IPO-Bound PhonePe retained its top position in the UPI ecosystem in March, with its transactions jumping 88% to 1,050 Cr&#8230;

## 81. Developing | DeepSeek releases next-gen AI model with ‘world-leading’ cost efficiency - South China Morning Post
- Domain: scmp.com
- URL: https://news.google.com/rss/articles/CBMisAFBVV95cUxOa1dLMjNxOGlBUFI0aktxeXpMVFlxYS1ZVE50Z3NCUVlzdUhWdTk5UGdKTlRwTlhRa240SkZ3aWZtOUVfOUdMeDV1WjRhZkVjU0JpVWVGRmJxQTR1SU1xSzdsNzhJQ19qdDdEdl9McE5kS0pfVmNaX3dES2FLS05qU2lGcWJ5Y0dsVDNMb2dxSzY4OUo3U0JkMG1jVG9XQ3p1NHJqUFZSM3Vja0xOWThNSNIBsAFBVV95cUxOc2VXN01yVUlpSkdtWlVWTjllZXhyS3Rka0pPYlRXSTlhR3pRRDNPQ2JxY1I0dE94VF9lajRWR1d5UlFTZlhaelVFYzN0TmVyMEdmLWdfcHJIT2ktN2tuN0c0aHF1NTgwRU5hQkZBVWoySTZLcnVycWlpNWVpdlA3ZWduRUF5SHlUYlVhSGgwc1dLUGlTV2RlVkYxTm5adnpwdjdzQlB2OHBrSkRIaVBFaQ
- Relevance score: 5.8
- Published: Fri, 24 Apr 2026 03:25:33 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMisAFBVV95cUxOa1dLMjNxOGlBUFI0aktxeXpMVFlxYS1ZVE50Z3NCUVlzdUhWdTk5UGdKTlRwTlhRa240SkZ3aWZtOUVfOUdMeDV1WjRhZkVjU0JpVWVGRmJxQTR1SU1xSzdsNzhJQ19qdDdEdl9McE5kS0pfVmNaX3dES2FLS05qU2lGcWJ5Y0dsVDNMb2dxSzY4OUo3U0JkMG1jVG9XQ3p1NHJqUFZSM3Vja0xOWThNSNIBsAFBVV95cUxOc2VXN01yVUlpSkdtWlVWTjllZXhyS3Rka0pPYlRXSTlhR3pRRDNPQ2JxY1I0dE94VF9lajRWR1d5UlFTZlhaelVFYzN0TmVyMEdmLWdfcHJIT2ktN2tuN0c0aHF1NTgwRU5hQkZBVWoySTZLcnVycWlpNWVpdlA3ZWduRUF5SHlUYlVhSGgwc1dLUGlTV2RlVkYxTm5adnpwdjdzQlB2OHBrSkRIaVBFaQ?oc=5" target="_blank">Developing | DeepSeek releases next-gen AI model with ‘world-leading’ cost efficiency</a>&nbsp;&nbsp;<font color="#6f6f6f">South China Morning Post</font>

## 82. You’re about to feel the AI money squeeze
- Domain: theverge.com
- URL: https://www.theverge.com/ai-artificial-intelligence/917380/ai-monetization-anthropic-openai-token-economics-revenue
- Relevance score: 5.8
- Published: 2026-04-23T09:45:00-04:00
- Summary: Earlier this month, millions of OpenClaw users woke up to a sweeping mandate: The viral AI agent tool, which this year took the worldwide tech industry by storm, had been severely restricted by Anthropic. Anthropic, like other leading AI labs, was under immense pressure to lessen the strain on its systems and start turning a [&#8230;]

## 83. An update on recent Claude Code quality reports
- Domain: simonwillison.net
- URL: https://simonwillison.net/2026/Apr/24/recent-claude-code-quality-reports/
- Relevance score: 5.7
- Published: 2026-04-24T01:31:25+00:00
- Summary: <p><strong><a href="https://www.anthropic.com/engineering/april-23-postmortem">An update on recent Claude Code quality reports</a></strong></p> It turns out the high volume of complaints that Claude Code was providing worse quality results over the past two months was grounded in real problems.</p> <p>The models themselves were not to blame, but three separate issues in the Claude Code harness caused complex but material problems which directly affected users.</p> <p>Anthropic's postmortem describes these in detail. This one in particular stood out to me:</p> <blockquote> <p>On March 26, we shipped a change to clear Claude's older thinking from sessions that had been idle for over an hour, to reduce latency when users resumed those sessions. A bug caused this to keep happening every turn for the rest of the session instead of just once, which made Claude seem forgetful and repetitive.</p> </blockquote> <p>I <em>frequently</em> have Claude Code sessions which I leave for an hour (or often a day or longer) before returning to them. Right now I have 11 of those (according to <code>ps aux | grep 'claude '</code>) and that's after closing down dozens more the other day.</p> <p>I estimat

## 84. Cathie Wood’s ARK makes its first lead investment in startup Lucra — and it isn’t AI - TechCrunch
- Domain: techcrunch.com
- URL: https://news.google.com/rss/articles/CBMitgFBVV95cUxPd0s0VmNDVVM3MG1EanF3SC1PTkdZZmR3cjNUcElqWEVXT0Y1c1RETmlBYmlhb2xnaXU0elRkNDJ1N0dDbVkzbUlIY2ViZjdJRUp1aDB0VE96Sk5Nc1pGTk45d3I3cUZIenlCY0swS3E5OV84WnRYS05ya3NORE1PQmlUT1RUbnNseEdpU1ozQU1zUlhYU2ttRXZHNVVqeE5iRWRETkJURXljU3JVa2g1WlBCMFliZw
- Relevance score: 5.5
- Published: Wed, 22 Apr 2026 15:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMitgFBVV95cUxPd0s0VmNDVVM3MG1EanF3SC1PTkdZZmR3cjNUcElqWEVXT0Y1c1RETmlBYmlhb2xnaXU0elRkNDJ1N0dDbVkzbUlIY2ViZjdJRUp1aDB0VE96Sk5Nc1pGTk45d3I3cUZIenlCY0swS3E5OV84WnRYS05ya3NORE1PQmlUT1RUbnNseEdpU1ozQU1zUlhYU2ttRXZHNVVqeE5iRWRETkJURXljU3JVa2g1WlBCMFliZw?oc=5" target="_blank">Cathie Wood’s ARK makes its first lead investment in startup Lucra — and it isn’t AI</a>&nbsp;&nbsp;<font color="#6f6f6f">TechCrunch</font>

## 85. Anthropic investigates report of rogue access to hack-enabling Mythos AI
- Domain: theguardian.com
- URL: https://www.theguardian.com/technology/2026/apr/22/anthropic-investigates-report-of-rogue-access-to-hack-enabling-mythos-ai
- Relevance score: 5.5
- Published: Wed, 22 Apr 2026 08:58:06 GMT
- Summary: <p>‘Handful’ of people allegedly gain unauthorised access to model adept at detecting cybersecurity vulnerabilities</p><ul><li><p><a href="https://www.theguardian.com/business/live/2026/apr/22/uk-inflation-increase-fuel-prices-oil-falls-trump-ceasefire-extended-business-live-news-updates">Business live – latest updates</a></p></li></ul><p>The AI developer Anthropic has confirmed it is investigating a report that unauthorised users have gained access to its Mythos model, which it has warned <a href="https://www.theguardian.com/technology/2026/apr/08/anthropic-ai-cybersecurity-software">poses risks to cybersecurity</a>.</p><p>The US startup made the statement after Bloomberg reported on Wednesday that a small group of people had accessed the model, which has not been released to the public because of its <a href="https://www.theguardian.com/business/2026/apr/13/goldman-sachs-chief-hyper-aware-risks-anthropics-mythos-ai-david-solomon">ability to enable cyber-attacks</a>.</p> <a href="https://www.theguardian.com/technology/2026/apr/22/anthropic-investigates-report-of-rogue-access-to-hack-enabling-mythos-ai">Continue reading...</a>

## 86. ✰PREMIUM What we lose when artificial intelligence does our shopping - Brooklyn Eagle
- Domain: brooklyneagle.com
- URL: https://news.google.com/rss/articles/CBMie0FVX3lxTE1BSHRXY0hMLThuc3BNM29SdzE0UHQ0WEtSSEZLZGFYakhodWJfSm5MemRlOThHdzRYNTUwcFM5ZVJmQzMydHE0SUFtT3d5b09VdHZXRDQ5VXdjVzZpaU1FWHZNZkEtR0pSZm43WnM0b0JDUHJTN3NGSjBBZw
- Relevance score: 5.5
- Published: Thu, 23 Apr 2026 18:12:49 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMie0FVX3lxTE1BSHRXY0hMLThuc3BNM29SdzE0UHQ0WEtSSEZLZGFYakhodWJfSm5MemRlOThHdzRYNTUwcFM5ZVJmQzMydHE0SUFtT3d5b09VdHZXRDQ5VXdjVzZpaU1FWHZNZkEtR0pSZm43WnM0b0JDUHJTN3NGSjBBZw?oc=5" target="_blank">✰PREMIUM What we lose when artificial intelligence does our shopping</a>&nbsp;&nbsp;<font color="#6f6f6f">Brooklyn Eagle</font>

## 87. How artificial intelligence reshapes the mind that uses it. - Psychology Today
- Domain: psychologytoday.com
- URL: https://news.google.com/rss/articles/CBMilAFBVV95cUxNTGJrOGFWYlkyNE9rbks1TkxfZlF0S3prNlVCZXBoakpZcUlPaUZOMFp2NkR4alBPdzFQd0VjX3I3UmJ6ZHAzZzR5WTlBdlNmMGlZZTk0Vi1EMmdHM0xNSlVQUENqQzRoQzJuYzEwcmJnX19yU1B3alhEYlpPZkUzc2Y2TDFRekV0SFZ5LVpLTW95NUhU0gGaAUFVX3lxTE1LOXFuc3l1TDRGaW9GVHNybEdKdXhrUmJlcldDdHZLaDgyY1o4ZTNzOW1PU19GOFNPUGZ1cjZVX1d6WlE0akMwQVlBUmUzV0JVY2tkS2NuWk5Ia3hhNno2MlVFUVNrQ0Z3ZG14d1JHbnF0cHp0a3JScWoxUmhtTUdyZ0pwdVAtU2NZeFVkZ1hPR1FMbG9ZYXRlbGc
- Relevance score: 5.5
- Published: Thu, 23 Apr 2026 17:04:20 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMilAFBVV95cUxNTGJrOGFWYlkyNE9rbks1TkxfZlF0S3prNlVCZXBoakpZcUlPaUZOMFp2NkR4alBPdzFQd0VjX3I3UmJ6ZHAzZzR5WTlBdlNmMGlZZTk0Vi1EMmdHM0xNSlVQUENqQzRoQzJuYzEwcmJnX19yU1B3alhEYlpPZkUzc2Y2TDFRekV0SFZ5LVpLTW95NUhU0gGaAUFVX3lxTE1LOXFuc3l1TDRGaW9GVHNybEdKdXhrUmJlcldDdHZLaDgyY1o4ZTNzOW1PU19GOFNPUGZ1cjZVX1d6WlE0akMwQVlBUmUzV0JVY2tkS2NuWk5Ia3hhNno2MlVFUVNrQ0Z3ZG14d1JHbnF0cHp0a3JScWoxUmhtTUdyZ0pwdVAtU2NZeFVkZ1hPR1FMbG9ZYXRlbGc?oc=5" target="_blank">How artificial intelligence reshapes the mind that uses it.</a>&nbsp;&nbsp;<font color="#6f6f6f">Psychology Today</font>

## 88. Sans l’intelligence artificielle, ce conte de fées moderne n’aurait jamais existé : comment Pellegrino Matarazzo s’est imposé comme « l’homme du miracle » à la Real Sociedad - Goal.com
- Domain: goal.com
- URL: https://news.google.com/rss/articles/CBMivgJBVV95cUxPVElWSndGNzhCWS1HUlB5Ui1lX0UweGVNSE1DVjF5Qk95a19NelB1amhhZ1NXMVZNTkdWVUI3Z0J1QmowbTd1V25WMnA2SUtLNkR5SmxWSGlPWGZhRU1JVzdUSzVPVTBhdDQtdzVGVWt5aHRUeGRIQjNTemNvc3o5VmcxdnpJWElZUTRpMk5TUzRzUU9wZU1xR1N0bnp5X0UxV3JmQkJ1WndzZzV3U0UwTnJLdFdZdzVEeVJadjAzcEdRd2N5YnhEYk03S1gtU1lLMDVqTHp1aWRodnNUTlN4UEZTMUROUEJPd1BOcFVXZDhJTzZ0dFVreDV1dnljUVdGZnloUS1xUG9fN1pYMXhjSkFaQkJnc3A2cUZueWM4NTR4bW5kdkdxbXlpdHNZYTFPWEp4ZktUdlBLaFJvcGc
- Relevance score: 5.5
- Published: Thu, 23 Apr 2026 17:00:23 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMivgJBVV95cUxPVElWSndGNzhCWS1HUlB5Ui1lX0UweGVNSE1DVjF5Qk95a19NelB1amhhZ1NXMVZNTkdWVUI3Z0J1QmowbTd1V25WMnA2SUtLNkR5SmxWSGlPWGZhRU1JVzdUSzVPVTBhdDQtdzVGVWt5aHRUeGRIQjNTemNvc3o5VmcxdnpJWElZUTRpMk5TUzRzUU9wZU1xR1N0bnp5X0UxV3JmQkJ1WndzZzV3U0UwTnJLdFdZdzVEeVJadjAzcEdRd2N5YnhEYk03S1gtU1lLMDVqTHp1aWRodnNUTlN4UEZTMUROUEJPd1BOcFVXZDhJTzZ0dFVreDV1dnljUVdGZnloUS1xUG9fN1pYMXhjSkFaQkJnc3A2cUZueWM4NTR4bW5kdkdxbXlpdHNZYTFPWEp4ZktUdlBLaFJvcGc?oc=5" target="_blank">Sans l’intelligence artificielle, ce conte de fées moderne n’aurait jamais existé : comment Pellegrino Matarazzo s’est imposé comme « l’homme du miracle » à la Real Sociedad</a>&nbsp;&nbsp;<font color="#6f6f6f">Goal.com</font>

## 89. Artificial intelligence in tourism: the challenge of transforming corporate culture - en.travel2latam.com
- Domain: en.travel2latam.com
- URL: https://news.google.com/rss/articles/CBMivwFBVV95cUxNMDdZRXc4UFRZb1RhUy1zTmlWMWtMOVNQamNQUG9VQlJTalByRXNMYmdWS1hrb2VCMC05eFo2VnRQekUtZWVvSV9EbDhPMU02eWJmRFUzOTJ4bkNZcmlMQjFlRTBPQk1EVnZIc29mVjZtd2lLZ2QwUDFfZDBiZkRCX3dTd0tfYVlBZnRVN1pHZWFWUTM3LTUwYnlJU3RoMTFKR2hWMi1PNUduSE14dm5NYlRocng2Q2NCVWhUZ3JJNA
- Relevance score: 5.5
- Published: Thu, 23 Apr 2026 15:06:58 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMivwFBVV95cUxNMDdZRXc4UFRZb1RhUy1zTmlWMWtMOVNQamNQUG9VQlJTalByRXNMYmdWS1hrb2VCMC05eFo2VnRQekUtZWVvSV9EbDhPMU02eWJmRFUzOTJ4bkNZcmlMQjFlRTBPQk1EVnZIc29mVjZtd2lLZ2QwUDFfZDBiZkRCX3dTd0tfYVlBZnRVN1pHZWFWUTM3LTUwYnlJU3RoMTFKR2hWMi1PNUduSE14dm5NYlRocng2Q2NCVWhUZ3JJNA?oc=5" target="_blank">Artificial intelligence in tourism: the challenge of transforming corporate culture</a>&nbsp;&nbsp;<font color="#6f6f6f">en.travel2latam.com</font>

## 90. Jonah Goldberg: Keep artificial intelligence out of American classrooms - TribLIVE.com
- Domain: triblive.com
- URL: https://news.google.com/rss/articles/CBMiogFBVV95cUxPRHM3VW50QWtUUVN5akc5SDhRVzAyWW45dW1jb1MxWG5mQTBmbVBLWklKS0hfS3hSamVELUktRTRLTG9zWXItSVVjRmJJVzQzZ1BmMEwzOXFMRVo5MENYUTFiQVBhMERzdGN0dmZ6Y0RjaW9LSG1PdGY0X21QcUZRVm9wVFVkSHVGX3IwVnpDcXFSUk16TFUyWTBZRDZzMGU3MFE
- Relevance score: 5.5
- Published: Thu, 23 Apr 2026 15:03:43 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxPRHM3VW50QWtUUVN5akc5SDhRVzAyWW45dW1jb1MxWG5mQTBmbVBLWklKS0hfS3hSamVELUktRTRLTG9zWXItSVVjRmJJVzQzZ1BmMEwzOXFMRVo5MENYUTFiQVBhMERzdGN0dmZ6Y0RjaW9LSG1PdGY0X21QcUZRVm9wVFVkSHVGX3IwVnpDcXFSUk16TFUyWTBZRDZzMGU3MFE?oc=5" target="_blank">Jonah Goldberg: Keep artificial intelligence out of American classrooms</a>&nbsp;&nbsp;<font color="#6f6f6f">TribLIVE.com</font>

## 91. Groundcover expands AI Observability for LLM interactions - SC Media
- Domain: scworld.com
- URL: https://news.google.com/rss/articles/CBMikAFBVV95cUxQcUVxWjloMHVGbVFJRW9BVm1vNjBsYWI4V1l5STNjOFpaZHlDYV9XREZQVEdleFBLdHo5Sy1va08wRnByNzg5QjNyUGh4b1pqMXcwbHhzRXpSYV9QWFA2NGpRVmppc0t3OWJRaEtUaHZCRDJNSGZndkZ4amNoSHJWNGVpVDhHTHpXNVVYSXp5dS0
- Relevance score: 5.5
- Published: Thu, 23 Apr 2026 13:31:52 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMikAFBVV95cUxQcUVxWjloMHVGbVFJRW9BVm1vNjBsYWI4V1l5STNjOFpaZHlDYV9XREZQVEdleFBLdHo5Sy1va08wRnByNzg5QjNyUGh4b1pqMXcwbHhzRXpSYV9QWFA2NGpRVmppc0t3OWJRaEtUaHZCRDJNSGZndkZ4amNoSHJWNGVpVDhHTHpXNVVYSXp5dS0?oc=5" target="_blank">Groundcover expands AI Observability for LLM interactions</a>&nbsp;&nbsp;<font color="#6f6f6f">SC Media</font>

## 92. What we lose when artificial intelligence does our shopping - The Conversation
- Domain: theconversation.com
- URL: https://news.google.com/rss/articles/CBMimgFBVV95cUxQOFBOOWxJczFyTGkwTHB5OGNadHVHNXJkUFhRQk9rODJiSDkxNUZiUHNxRVpoNl9TcXZmallPSGlpLXBxZlRCYTJmeklZYlFvZ1IzWFRWX21teG1OX1laTzNWamhXbU4xQzN6M0FMQ0Z3OTV1Q25UQTlUT0doRWlNaDhxOGJ5YWZERmRJYlROU2tWTTRYYWR0eDdn
- Relevance score: 5.5
- Published: Thu, 23 Apr 2026 12:22:43 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMimgFBVV95cUxQOFBOOWxJczFyTGkwTHB5OGNadHVHNXJkUFhRQk9rODJiSDkxNUZiUHNxRVpoNl9TcXZmallPSGlpLXBxZlRCYTJmeklZYlFvZ1IzWFRWX21teG1OX1laTzNWamhXbU4xQzN6M0FMQ0Z3OTV1Q25UQTlUT0doRWlNaDhxOGJ5YWZERmRJYlROU2tWTTRYYWR0eDdn?oc=5" target="_blank">What we lose when artificial intelligence does our shopping</a>&nbsp;&nbsp;<font color="#6f6f6f">The Conversation</font>

## 93. AI Cybersecurity startup Deep Algorithm raises Rs 16 Crore funding from Unicorn India Ventures - Indian Startup News
- Domain: indianstartupnews.com
- URL: https://news.google.com/rss/articles/CBMi1AFBVV95cUxPSGszdUM5X2pBR2xTcGYwQ3BtT0QyWTRCV0dWT2plaWl3YkhKUF9uaUdMS3RoNHJUWXp2ZzBVYnpreFBOeUUwRFAwaUwzV01qbWxia3YxZm55OXpFNGdPUDlwcFRJbTlYTUxwWFFENi1zTEpfX1A4SEdDaHFiWVVmeW4tZkNER3hLM1JObUpGUHFULXRvYUJzeTdpb1hiZzRyMHVNYkZwTURTVDd1YkNjNVhOTDlCTGV0cGtVd3R3QlcxYkR1Wm1lZHB5aEo4ZkNFa0hENNIB1AFBVV95cUxPSGszdUM5X2pBR2xTcGYwQ3BtT0QyWTRCV0dWT2plaWl3YkhKUF9uaUdMS3RoNHJUWXp2ZzBVYnpreFBOeUUwRFAwaUwzV01qbWxia3YxZm55OXpFNGdPUDlwcFRJbTlYTUxwWFFENi1zTEpfX1A4SEdDaHFiWVVmeW4tZkNER3hLM1JObUpGUHFULXRvYUJzeTdpb1hiZzRyMHVNYkZwTURTVDd1YkNjNVhOTDlCTGV0cGtVd3R3QlcxYkR1Wm1lZHB5aEo4ZkNFa0hENA
- Relevance score: 5.5
- Published: Thu, 23 Apr 2026 08:50:43 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi1AFBVV95cUxPSGszdUM5X2pBR2xTcGYwQ3BtT0QyWTRCV0dWT2plaWl3YkhKUF9uaUdMS3RoNHJUWXp2ZzBVYnpreFBOeUUwRFAwaUwzV01qbWxia3YxZm55OXpFNGdPUDlwcFRJbTlYTUxwWFFENi1zTEpfX1A4SEdDaHFiWVVmeW4tZkNER3hLM1JObUpGUHFULXRvYUJzeTdpb1hiZzRyMHVNYkZwTURTVDd1YkNjNVhOTDlCTGV0cGtVd3R3QlcxYkR1Wm1lZHB5aEo4ZkNFa0hENNIB1AFBVV95cUxPSGszdUM5X2pBR2xTcGYwQ3BtT0QyWTRCV0dWT2plaWl3YkhKUF9uaUdMS3RoNHJUWXp2ZzBVYnpreFBOeUUwRFAwaUwzV01qbWxia3YxZm55OXpFNGdPUDlwcFRJbTlYTUxwWFFENi1zTEpfX1A4SEdDaHFiWVVmeW4tZkNER3hLM1JObUpGUHFULXRvYUJzeTdpb1hiZzRyMHVNYkZwTURTVDd1YkNjNVhOTDlCTGV0cGtVd3R3QlcxYkR1Wm1lZHB5aEo4ZkNFa0hENA?oc=5" target="_blank">AI Cybersecurity startup Deep Algorithm raises Rs 16 Crore funding from Unicorn India Ventures</a>&nbsp;&nbsp;<font color="#6f6f6f">Indian Startup News</font>

## 94. India weighs stricter regulatory framework for artificial intelligence - Communications Today
- Domain: communicationstoday.co.in
- URL: https://news.google.com/rss/articles/CBMirgFBVV95cUxPYXpyR3ZfbzlXWW94bEIzYXgxQ0RyOU5jYklzNHc3VkJVSnBrMzRrLXp0ZjNjczBSTDVsU19uY25oajFQME9TaGJqRTU2b3p2YTFyeWRNUXpSVllSWU42aW1MMkNzSWhDTDlwTUdJMm5BNW5TQU8wWUZ0VGpWUFVPTmxJRjJoVDlySGN3MHpFbmJQeHBDWEJFRjZGRDJKZFhtdVRla25pSmN1cERaNnc
- Relevance score: 5.5
- Published: Thu, 23 Apr 2026 07:05:52 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMirgFBVV95cUxPYXpyR3ZfbzlXWW94bEIzYXgxQ0RyOU5jYklzNHc3VkJVSnBrMzRrLXp0ZjNjczBSTDVsU19uY25oajFQME9TaGJqRTU2b3p2YTFyeWRNUXpSVllSWU42aW1MMkNzSWhDTDlwTUdJMm5BNW5TQU8wWUZ0VGpWUFVPTmxJRjJoVDlySGN3MHpFbmJQeHBDWEJFRjZGRDJKZFhtdVRla25pSmN1cERaNnc?oc=5" target="_blank">India weighs stricter regulatory framework for artificial intelligence</a>&nbsp;&nbsp;<font color="#6f6f6f">Communications Today</font>

## 95. Your credit score may not matter soon. Here’s what AI looks at instead - Mint
- Domain: livemint.com
- URL: https://news.google.com/rss/articles/CBMi2wFBVV95cUxNdy00VkhTMDAtMWhTWkZyNEp1cHR2ZkxGeUQtMWI4QXl1OFRmOTVSdTZXZGpuQmQ3eGZQRElvQm1Zd2xIM1pjMEt6OFcxSGlMdHFXOWE2MDBBM0tWWTVhbkZmVWV4ZkNHRk9fSl8tM0JiS2R6SHQ3NUhDZy1rTU83Y18zNnhLbDl3aEFaaDdVNkdPU3luUUpLbUtYa3JkQm5xVGxoREJTR3hUYWo4THNtQmE5bEdGbHZYbEd0cVV6T2dtUzNZak10VDdBclNtajhHeko5Nm1uRDEzb2_SAeABQVVfeXFMTVY3ZDlyeFRCVmhwS3RMSkxMbjZtSTNKQmM5RmgwWV8tZHZUX3Vic0ItZ0NMblQ1OVZQMlY4MGs4RzRxcEszZnVDMFRHMG1pR1ZXXy1rTVp3ZTJCbktZbThBN2JYVE5IeUdiQ1FzbXpLYS1XblRBbXA1c2NhQU1NTU5DUDVkUjVlcGdnNHFWbVhBSkhtclBIZXBSZTNmLU1Md1hTWGR5a3VXa0dPRnZ4SElUUFNhbUZqUUp3bnJ3VTVvZ3JnOU5fVlR6UXNrV2JCX2VWZXVQNEN2Vk43cm9OWE0
- Relevance score: 5.5
- Published: Fri, 24 Apr 2026 05:05:05 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi2wFBVV95cUxNdy00VkhTMDAtMWhTWkZyNEp1cHR2ZkxGeUQtMWI4QXl1OFRmOTVSdTZXZGpuQmQ3eGZQRElvQm1Zd2xIM1pjMEt6OFcxSGlMdHFXOWE2MDBBM0tWWTVhbkZmVWV4ZkNHRk9fSl8tM0JiS2R6SHQ3NUhDZy1rTU83Y18zNnhLbDl3aEFaaDdVNkdPU3luUUpLbUtYa3JkQm5xVGxoREJTR3hUYWo4THNtQmE5bEdGbHZYbEd0cVV6T2dtUzNZak10VDdBclNtajhHeko5Nm1uRDEzb2_SAeABQVVfeXFMTVY3ZDlyeFRCVmhwS3RMSkxMbjZtSTNKQmM5RmgwWV8tZHZUX3Vic0ItZ0NMblQ1OVZQMlY4MGs4RzRxcEszZnVDMFRHMG1pR1ZXXy1rTVp3ZTJCbktZbThBN2JYVE5IeUdiQ1FzbXpLYS1XblRBbXA1c2NhQU1NTU5DUDVkUjVlcGdnNHFWbVhBSkhtclBIZXBSZTNmLU1Md1hTWGR5a3VXa0dPRnZ4SElUUFNhbUZqUUp3bnJ3VTVvZ3JnOU5fVlR6UXNrV2JCX2VWZXVQNEN2Vk43cm9OWE0?oc=5" target="_blank">Your credit score may not matter soon. Here’s what AI looks at instead</a>&nbsp;&nbsp;<font color="#6f6f6f">Mint</font>

## 96. Surveillance State: The growing use of artificial intelligence with camera networks - KSL TV 5
- Domain: ksltv.com
- URL: https://news.google.com/rss/articles/CBMixgFBVV95cUxPeUV1NkttWktrUXVhNGNUWUNtQW5WMEljeFJEVUItRFlvanBhM205dm91ZmhzNVhWVlhucnV0S0JaaGpDX01GUVh2TW5xLWYydjJ5YV93MDBEbkE2bnRzR2UwQ2g0Yk00c3hyVFZ6MHBwd2ZXUjFMU25qcDNZU0J3VzhfNVdGN3hLakxZN19raHdxa0hfUTd3NnhUb3E1clItLVByNzE2a04zOC1FNEtlY3Rob2RCLXg4cEpVZGZzTEJUakh2OGc
- Relevance score: 5.5
- Published: Fri, 24 Apr 2026 05:00:36 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMixgFBVV95cUxPeUV1NkttWktrUXVhNGNUWUNtQW5WMEljeFJEVUItRFlvanBhM205dm91ZmhzNVhWVlhucnV0S0JaaGpDX01GUVh2TW5xLWYydjJ5YV93MDBEbkE2bnRzR2UwQ2g0Yk00c3hyVFZ6MHBwd2ZXUjFMU25qcDNZU0J3VzhfNVdGN3hLakxZN19raHdxa0hfUTd3NnhUb3E1clItLVByNzE2a04zOC1FNEtlY3Rob2RCLXg4cEpVZGZzTEJUakh2OGc?oc=5" target="_blank">Surveillance State: The growing use of artificial intelligence with camera networks</a>&nbsp;&nbsp;<font color="#6f6f6f">KSL TV 5</font>

## 97. AI media planner, AI Creative Strategist... les 9 nouveaux métiers publicitaires de l’IA qui s'arrachent - Influencia
- Domain: influencia.net
- URL: https://news.google.com/rss/articles/CBMixAFBVV95cUxNT0lLMjByR3VWUkZzVlVKMExoc20zdGhFMkdZQUluYUQyN21xWFI3ZTRGRnJKMTFjYXZ0Mk9UY2Y1YTkteFRaMTVqVExGdFVwZjhzTmRtbnRyU0ZqZDUzZzdTVlpiNnA1YlNIT0NzM0tOVUU0dE4wVGdKcURYb2luTXpaTDBMUy1ab29uNTBfRnNmeW0wX3ZZUDQtVTM4QkRKSGhIYk56M0JKb0EyRmJSUkhoc0xpUDJ0dmQzZHlzcjZvOW9G
- Relevance score: 5.5
- Published: Fri, 24 Apr 2026 04:08:47 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMixAFBVV95cUxNT0lLMjByR3VWUkZzVlVKMExoc20zdGhFMkdZQUluYUQyN21xWFI3ZTRGRnJKMTFjYXZ0Mk9UY2Y1YTkteFRaMTVqVExGdFVwZjhzTmRtbnRyU0ZqZDUzZzdTVlpiNnA1YlNIT0NzM0tOVUU0dE4wVGdKcURYb2luTXpaTDBMUy1ab29uNTBfRnNmeW0wX3ZZUDQtVTM4QkRKSGhIYk56M0JKb0EyRmJSUkhoc0xpUDJ0dmQzZHlzcjZvOW9G?oc=5" target="_blank">AI media planner, AI Creative Strategist... les 9 nouveaux métiers publicitaires de l’IA qui s'arrachent</a>&nbsp;&nbsp;<font color="#6f6f6f">Influencia</font>

## 98. Declining income, no consent: AI eats into Korea's creative, language workforce - The Korea Times
- Domain: koreatimes.co.kr
- URL: https://news.google.com/rss/articles/CBMizAFBVV95cUxPSWwxWGY5VkR2WlJCTUNlS0JkeS1xRG1oSVZsTW5FV3BGdC1tbjFWeTZNdk1OUk9HcjVuRUExLXdwYjdxSkg0ZlRQbWNnT1dHblYxakFmcFIzeHZLYUdMOGdGeXp6bzg3V1FyTDNuLVZzeWk2ckdkTnA3eTNPQkV5ODA3Zmlqakg4dk1nTTBrWnkwWnZBMmpHVTFEWjNBYW1ab1VHdE02ZWdhR0l2cEFzLW1nemZzcXJFdUtraGFrTENwTTNJakhQbFZ5dGPSAdIBQVVfeXFMTy1tay1XX0FORmR5TktuLTJmYTVleE1iRnlPRVhfSlZpOGM3cl83VWVWUks5Rzc0VmNmNlpRTENidGgwNXBGMGRhdVYzN29QMmpJOWNBczc2TURxMWxjbU5zenA5ZE5kcV9KMC1RTzRidGM2azN6M183YlZiOGw2Z0NoSHg1dERJUGJIUlpXNkUzUXpNRHJqeFhLY1J5VTdoVXRMQ25CelN6NEpJMkN6WEpsVWhqaEc1ZVZPQXd6WTNMdTN4eG5QU3ZjcHI2ejRyWFh3
- Relevance score: 5.5
- Published: Fri, 24 Apr 2026 03:00:05 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMizAFBVV95cUxPSWwxWGY5VkR2WlJCTUNlS0JkeS1xRG1oSVZsTW5FV3BGdC1tbjFWeTZNdk1OUk9HcjVuRUExLXdwYjdxSkg0ZlRQbWNnT1dHblYxakFmcFIzeHZLYUdMOGdGeXp6bzg3V1FyTDNuLVZzeWk2ckdkTnA3eTNPQkV5ODA3Zmlqakg4dk1nTTBrWnkwWnZBMmpHVTFEWjNBYW1ab1VHdE02ZWdhR0l2cEFzLW1nemZzcXJFdUtraGFrTENwTTNJakhQbFZ5dGPSAdIBQVVfeXFMTy1tay1XX0FORmR5TktuLTJmYTVleE1iRnlPRVhfSlZpOGM3cl83VWVWUks5Rzc0VmNmNlpRTENidGgwNXBGMGRhdVYzN29QMmpJOWNBczc2TURxMWxjbU5zenA5ZE5kcV9KMC1RTzRidGM2azN6M183YlZiOGw2Z0NoSHg1dERJUGJIUlpXNkUzUXpNRHJqeFhLY1J5VTdoVXRMQ25CelN6NEpJMkN6WEpsVWhqaEc1ZVZPQXd6WTNMdTN4eG5QU3ZjcHI2ejRyWFh3?oc=5" target="_blank">Declining income, no consent: AI eats into Korea's creative, language workforce</a>&nbsp;&nbsp;<font color="#6f6f6f">The Korea Times</font>

## 99. Grok tells researchers pretending to be delusional ‘drive an iron nail through the mirror while reciting Psalm 91 backwards’
- Domain: theguardian.com
- URL: https://www.theguardian.com/technology/2026/apr/24/musk-grok-x-ai-researchers-delusional-advice-inputs
- Relevance score: 5.5
- Published: Fri, 24 Apr 2026 02:35:43 GMT
- Summary: <p>Elon Musk’s AI chatbot ‘extremely validating’ of delusional inputs and often went further, ‘elaborating new material’, study finds</p><ul><li><p><a href="https://www.theguardian.com/australia-news/live/2026/apr/24/andrew-hastie-us-defence-ndis-reform-cuts-budget-gas-export-fuel-crisis-jim-chalmers-anthony-albanese-ntwnfb">Follow our Australia news live blog for latest updates</a></p></li><li><p>Get our <a href="https://www.theguardian.com/email-newsletters?CMP=cvau_sfl">breaking news email</a>, <a href="https://app.adjust.com/w4u7jx3">free app</a> or <a href="https://www.theguardian.com/australia-news/series/full-story?CMP=cvau_sfl">daily news podcast</a></p></li></ul><p>Elon Musk’s AI chatbot Grok 4.1 told researchers pretending to be delusional that there was indeed a doppelganger in their mirror and they should drive an iron nail through the glass while reciting Psalm 91 backwards.</p><p>Researchers at the City University of New York (Cuny) and King’s College London have published a paper on how various chatbots protect – or fail to safeguard – users’ mental health.</p> <a href="https://www.theguardian.com/technology/2026/apr/24/musk-grok-x-ai-researchers-delusional-advice-in

## 100. Meta to cut workforce by 10% as artificial intelligence spending surges - France 24
- Domain: france24.com
- URL: https://news.google.com/rss/articles/CBMixwFBVV95cUxNckhjYklhLUYyZW5xSzVhNXNTWXo3OXFKcFJ2bWs5eGZYQURvTU5CampaMEpYRDAyQ0ktQkpsVndFUEFDbjhjSkJjenJIVm91TzA0aGt4TmE5Q2diZUtxM0RlSjFGWFhuVlo3NGJfQlNpR2lkU1kyd0JaWTBnT0FJZWJTSHh0dGY2UUlYUVFvTXh0UHE4UWNvbFZoVXNKYnktNHJya3k5VzA0bEZQMFhyUGZRZVFobzRkQWpSMDVkOWhpdTFVRENn
- Relevance score: 5.5
- Published: Fri, 24 Apr 2026 00:12:12 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMixwFBVV95cUxNckhjYklhLUYyZW5xSzVhNXNTWXo3OXFKcFJ2bWs5eGZYQURvTU5CampaMEpYRDAyQ0ktQkpsVndFUEFDbjhjSkJjenJIVm91TzA0aGt4TmE5Q2diZUtxM0RlSjFGWFhuVlo3NGJfQlNpR2lkU1kyd0JaWTBnT0FJZWJTSHh0dGY2UUlYUVFvTXh0UHE4UWNvbFZoVXNKYnktNHJya3k5VzA0bEZQMFhyUGZRZVFobzRkQWpSMDVkOWhpdTFVRENn?oc=5" target="_blank">Meta to cut workforce by 10% as artificial intelligence spending surges</a>&nbsp;&nbsp;<font color="#6f6f6f">France 24</font>

## 101. Kabeer Biswas’ M Raises ₹102 Cr From Peak XV, Blume
- Domain: inc42.com
- URL: https://inc42.com/buzz/kabeer-biswas-m-raises-%e2%82%b9102-cr-from-peak-xv-blume/
- Relevance score: 5.3
- Published: Wed, 22 Apr 2026 13:34:20 +0000
- Summary: <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="1020" src="https://inc42.com/cdn-cgi/image/quality=90/https://asset.inc42.com/2026/04/Untitled-design-10.png" style="display: block; margin: auto; margin-bottom: 5px;" width="1360" />Former Dunzo cofounder Kabeer Biswas’ new startup, M, is looking to net ₹102 Cr (about $11 Mn) from Peak XV&#8230;

## 102. THE PEOPLE DO NOT YEARN FOR AUTOMATION
- Domain: theverge.com
- URL: https://www.theverge.com/podcast/917029/software-brain-ai-backlash-databases-automation
- Relevance score: 5.3
- Published: 2026-04-23T10:00:00-04:00
- Summary: Today on Decoder, I want to lay out an idea that&#8217;s been banging around my head for weeks now as we&#8217;ve been reporting on AI and having conversations here on this show. I&#8217;ve been calling it software brain, and it&#8217;s a particular way of seeing the world that fits everything into algorithms, databases and loops [&#8230;]

## 103. Reversing enterprise security costs with AI vulnerability discovery
- Domain: artificialintelligence-news.com
- URL: https://www.artificialintelligence-news.com/news/reversing-enterprise-security-costs-with-ai-vulnerability-discovery/
- Relevance score: 5.2
- Published: Wed, 22 Apr 2026 15:45:14 +0000
- Summary: <p>Automated AI vulnerability discovery is reversing the enterprise security costs that traditionally favour attackers. Bringing exploits to zero was once viewed as an unrealistic goal. The prevailing operational doctrine aimed to make attacks so expensive that only adversaries with functionally unlimited budgets could afford them, thereby disincentivising casual use. However, the recent evaluation by the [&#8230;]</p> <p>The post <a href="https://www.artificialintelligence-news.com/news/reversing-enterprise-security-costs-with-ai-vulnerability-discovery/">Reversing enterprise security costs with AI vulnerability discovery</a> appeared first on <a href="https://www.artificialintelligence-news.com">AI News</a>.</p>

## 104. AI in law firms entering its closing summaries
- Domain: artificialintelligence-news.com
- URL: https://www.artificialintelligence-news.com/news/ai-in-law-firms-entering-its-closing-summaries/
- Relevance score: 5.2
- Published: Wed, 22 Apr 2026 13:51:00 +0000
- Summary: <p>In an interview with Artificial Lawyer, Paris-based AI-native consulting firm owner, Olivier Chaduteau, set out a three-part account of the current state of AI in the legal sector. At first, lawyers dismissed AI as irrelevant to expert work. In the second, organisations bought licences to LLMs to signal activity to partners and/or clients, but little [&#8230;]</p> <p>The post <a href="https://www.artificialintelligence-news.com/news/ai-in-law-firms-entering-its-closing-summaries/">AI in law firms entering its closing summaries</a> appeared first on <a href="https://www.artificialintelligence-news.com">AI News</a>.</p>

## 105. russellromney/honker
- Domain: simonwillison.net
- URL: https://simonwillison.net/2026/Apr/24/honker/
- Relevance score: 5.2
- Published: 2026-04-24T01:50:07+00:00
- Summary: <p><strong><a href="https://github.com/russellromney/honker">russellromney/honker</a></strong></p> "Postgres NOTIFY/LISTEN semantics" for SQLite, implemented as a Rust SQLite extension and various language bindings to help make use of it.</p> <p>The design of this looks very solid. It lets you write Python code for queues that looks like this:</p> <pre><span class="pl-k">import</span> <span class="pl-s1">honker</span> <span class="pl-s1">db</span> <span class="pl-c1">=</span> <span class="pl-s1">honker</span>.<span class="pl-c1">open</span>(<span class="pl-s">"app.db"</span>) <span class="pl-s1">emails</span> <span class="pl-c1">=</span> <span class="pl-s1">db</span>.<span class="pl-c1">queue</span>(<span class="pl-s">"emails"</span>) <span class="pl-c1">emails</span>.<span class="pl-c1">enqueue</span>({<span class="pl-s">"to"</span>: <span class="pl-s">"alice@example.com"</span>}) <span class="pl-c"># Consume (in a worker process)</span> <span class="pl-k">async</span> <span class="pl-k">for</span> <span class="pl-s1">job</span> <span class="pl-c1">in</span> <span class="pl-s1">emails</span>.<span class="pl-c1">claim</span>(<span class="pl-s">"worker-1"</span>): <span class="pl-en

## 106. 小鹏第二代VLA智驾报告首发，全系Ultra车型订单环比提升118%
- Domain: 36kr.com
- URL: https://36kr.com/newsflashes/3780375623357702
- Relevance score: 5.2
- Published: 2026-04-24 13:16:56  +0800
- Summary: 36氪获悉，今日，2026（第十九届）北京国际车展正式启幕，小鹏集团携全明星产品矩阵重磅亮相，涵盖全新车型小鹏GX、2026款小鹏MONA M03、全新小鹏P7、2026款小鹏X9等多款热门新车，以及全新一代人形机器人IRON、“陆地航母”分体式飞行汽车，全面展示小鹏集团在物理AI矩阵的前沿成果与全场景布局。据透露，3月，小鹏全系Ultra车型订单环比提升了118%，首次下单即选择Ultra及Ultra SE车型的成交量环比增长129.3%。

## 107. 用“活人感”做科技社区，小红书能成吗？
- Domain: 36kr.com
- URL: https://36kr.com/p/3778772970444033
- Relevance score: 5.2
- Published: 2026-04-24 10:14:50  +0800
- Summary: <p>文 | 钟艺璇</p> <p>编辑 | 乔芊</p> <p>没人能脱离AI这个浪潮，社区APP也不例外。</p> <p>只是对比豆包、千问——它们背后往往站着有能力制造C端入口的大公司，社区似乎天然有短板，从过去的路径看，它似乎只能做到在内容上与科技无限靠近，成为一个极客范儿的存在，但终究面临垂类用户增长见顶的事实。</p> <p>如果是一个综合类社区呢？在过去的垂类运营中，大规模引入KOL、KOC是迅速解决行业覆盖率的通用办法，但大水漫灌，或许会带来新老住民的气质冲突，尤其科技还是一个门槛较高的垂类，如果没有获得感，新用户的生命周期将会迅速缩短。</p> <p>今天的小红书或许是一个不错的观察样本，它足够活跃，Tiktok难民事件某种程度上印证了这个社区面对跨种族、乃至跨文化的一定包容性。而从去年以来，小红书社区业务的核心命题一直是做兴趣社区，它有扩容的野心，科技也成为过去一年增长最快的内容垂类之一——小红书科技内容发布同比增长超过100%，创作者规模同比增长超200%。</p> <p>更重要的是，中文世界还尚未诞生一个真正的大众科技社区，不是太硬核、就是被稀释。但在海外，X（原Twitter）证明了一个UGC平台有机会成长为全球科技内容最活跃、最实时的核心阵地之一。X甚至一度形成了马斯克效应，点赞谁，谁就火，今年3月，马斯克评价Kimi是 “Impressive work”，科技圈瞬间沸腾。</p> <p>作为中国最活跃的社区平台，小红书有这个野心。小红书科技运营负责人散兵提到，小红书的一个广泛目标是想成为最好的科技社区。</p> <p>但它还希望自己足够特别。散兵告诉36氪等媒体，在科技垂类的运营策略上，小红书不做资讯和教程，更愿意做“人之间的连接器”。</p> <p>要看懂这个有些抽象的词汇，我们或许可以从小红书近期举办的一场黑客松巅峰赛去理解。在这场比赛里，我们在现场见到了许多年轻的科技创业者们——他们正是小红书做科技垂类过程中希望首先吸引的人，也和散兵聊了聊小红书过去一年科技垂类运营的策略与变化。</p> <p class="image-wrapper"><img src="https://img.36krcdn.com/hsossms/20260424/v2_f079994867e040e4a6225259730dfa62@5971123_oswg564086oswg1600oswg1067_img_jpg?x-oss-process=image/quality,q_90/format,jpg/interlace,1" /></p> <p class="img-desc">小红书黑客松巅峰赛现场</p> <h3>Build in public</h3> <p>“在做一个产品之前，我们会把idea先发到小红书上，验证一下需求是否存在。”</

## 108. 博裕、经纬、顺为等投资前新石器COO超亿元，押注AI超便携电子纸｜硬氪独家
- Domain: 36kr.com
- URL: https://36kr.com/p/3778175428777218
- Relevance score: 5.2
- Published: 2026-04-24 09:30:00  +0800
- Summary: <p>作者｜黄楠</p> <p>编辑｜袁斯来</p> <p>当智能手机陷入性能过剩、AI功能同质化内卷，用户注意力被无限拆解与争夺时，一个被长期忽视的角落正悄然打开新赛道——手机背面的闲置空间。</p> <p>硬氪独家获悉，AI超便携电子纸品牌阅星曈近日完成天使轮至A轮融资，累计五轮金额超亿元人民币，投资方包括博裕创投、清流资本、希扬资本、小红书、经纬创投、顺为资本，多数股东持续追加。资金将用于完善生产制造与质量审核体系、拓展海外市场，搭建社区内容、优化产品体验，与全球用户共同构建AI时代手机副屏生态。</p> <p>阅星曈开创了“超便携电子纸”品类，其产品以极简的硬件设计与流畅的软件体验，深度融合AI能力，专注为数字时代用户提供专注、沉浸的阅读入口。</p> <p class="image-wrapper"><img src="https://img.36krcdn.com/hsossms/20260423/v2_e2ebc44d4dcb411c9e827d71ab5573a8@6022551_oswg606449oswg1920oswg800_img_jpg?x-oss-process=image/quality,q_90/format,jpg/interlace,1" /></p> <p class="img-desc">阅星曈超便携电子纸（图源/企业）</p> <p>创始人兼CEO胡宇沸是一位资深连续创业者，他毕业于香港中文大学，曾任新石器无人车COO、OYO酒店首席发展官、小蓝单车联合创始人兼COO、饿了么众包事业部总经理及Uber中国三城总经理等职务。多位核心成员均来自港中文、复旦大学、中国科学院大学、马里兰大学等院校，曾供职于头部互联网、智能硬件与AI企业，具备从爆品打造到全球化增长的完整能力闭环。</p> <p>鲜少有人预料到，胡宇沸再次创业时，会扎进一个轻巧到极易“被忽略”的硬件行业，做一款磁吸在手机背面的电子纸阅读器。</p> <p>它首款产品的重量仅有70克、4.3寸屏幕、售价不到300元。但就是这个隐藏在手机屏幕后的小配件，在零推广费用的前提下，依靠小红书社区的“云股东”共创众筹，一年内迅速完成了从产品定义到规模化验证的闭环。</p> <p>“是用户和我们一起，把这块小屏打磨成了今天的样子。”阅星曈创始人兼CEO胡宇沸表示。在产品定义与迭代过程中，有大量早期用户曾通过社群参与了需求反馈与功能建议。后续公司也会延续这一共创模式，在未来产品的立项和原型设计阶段开放用户参与通道，将用户反馈直接纳入早期研发流程。</p> <p class="image-wrapper"><img src="https://img.36krcdn.com/hsossms/20260423/v2_af83965686944f178a6f5bc8342f12eb@

## 109. 8点1氪丨华谊兄弟被申请破产重整；普华永道因恒大审计赔偿10亿港元；伊朗将恢复往返中国的航班
- Domain: 36kr.com
- URL: https://36kr.com/p/3780065714148610
- Relevance score: 5.2
- Published: 2026-04-24 08:05:57  +0800
- Summary: <h2>今日热点导览</h2> <p>抖音整治AI不当内容，重点处置利用AI技术换脸、盗声</p> <p>受燃油价格冲击，德国汉莎拟削减2万架次航班</p> <p>刹车功能或丧失，大众在美召回18853辆汽车</p> <p>光线传媒：公司第一款3A游戏开发进展比较顺利</p> <h2>TOP3大新闻</h2> <p><strong>华谊兄弟被申请破产重整</strong></p> <p>近日，华谊兄弟（300027）新增一则破产审查案件信息，申请人为北京泰睿飞克科技有限公司，经办法院为浙江省金华市中级人民法院。</p> <p>此次申请重整的债务，源于华谊兄弟与泰睿飞克的广告合同纠纷，法院 2025年9月判决华谊兄弟支付欠款，但公司至今未履行。2026年4月15日，华谊兄弟发布公告，债权人北京泰睿飞克科技有限公司以公司 “不能清偿到期债务且明显缺乏清偿能力” 为由，向法院申请对公司进行重整及预重整，涉案债务本金1140.52万元。（封面新闻、新浪新闻）</p> <p><strong>香港证监会：因中国恒大虚假财务报表问题，普华永道向股东赔偿10亿港元</strong></p> <p>36氪获悉，香港证监会与普华永道香港达成协议，据此，普华永道香港同意预留10亿港元，以向中国恒大集团的合资格独立少数股东作出赔偿。</p> <p>2019财政年度及2020财政年度，普华永道香港是中国恒大的核数师，而普华永道中天会计师事务所（特殊普通合伙）则协助普华永道香港对中国恒大的财务报表进行审计。本着为股东争取赔偿的最终目标，香港证监会断定，与普华永道香港达成协议，最符合中国恒大独立少数股东的利益，而根据该协议，已预留10亿港元，以透过由独立管理人监督的程序，分发予该等独立少数股东作为赔偿。</p> <p>2024年，中国证监会依法对普华永道恒大地产年报及债券发行审计工作未勤勉尽责案作出行政处罚，依据《中华人民共和国证券法》规定，没收普华永道案涉期间全部业务收入2774万元，并处以顶格罚款2.97亿元，合计罚没3.25亿元。</p> <p><strong>伊朗将恢复往返中国的航班</strong></p> <p>伊朗马汉航空4月23日表示将恢复伊朗往返中国航线客运航班。公告显示，自2026年4月26日起，马汉航空将逐步恢复伊朗往返中国的客运航班运营。（CCTV国际时讯）</p> <h2>大公司/大事件</h2> <p><strong>乐乐茶联名侵犯鲁迅形象被判陪20万</strong></p> <p>近日，上海市普陀区人民法院审理了一起因茶饮品牌联名侵犯鲁迅形象画作的著作权纠纷案件。</p> <p>2024年4月，奶茶品牌“乐乐茶”的运营公司以“世界读书日”为契机，推出了一款联名饮品。该公司在其微信公众号宣传文章、联名产品杯身等联名周边产品中，大量使用鲁迅手持奶茶杯的半身画像

## 110. Extract PDF text in your browser with LiteParse for the web
- Domain: simonwillison.net
- URL: https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/
- Relevance score: 5.2
- Published: 2026-04-23T21:54:24+00:00
- Summary: <p>LlamaIndex have a most excellent open source project called <a href="https://github.com/run-llama/liteparse">LiteParse</a>, which provides a Node.js CLI tool for extracting text from PDFs. I got a version of LiteParse working entirely in the browser, using most of the same libraries that LiteParse uses to run in Node.js.</p> <h4 id="spatial-text-parsing">Spatial text parsing</h4> <p>Refreshingly, LiteParse doesn't use AI models to do what it does: it's good old-fashioned PDF parsing, falling back to Tesseract OCR (or other pluggable OCR engines) for PDFs that contain images of text rather than the text itself.</p> <p>The hard problem that LiteParse solves is extracting text in a sensible order despite the infuriating vagaries of PDF layouts. They describe this as "spatial text parsing" - they use some very clever heuristics to detect things like multi-column layouts and group and return the text in a sensible linear flow.</p> <p>The LiteParse documentation describes a pattern for implementing <a href="https://developers.llamaindex.ai/liteparse/guides/visual-citations/">Visual Citations with Bounding Boxes</a>. I really like this idea: being able to answer questions from a PDF an

## 111. Everpure 'takes the hit' as AI-fueled supply crunch drives prices up 70%
- Domain: go.theregister.com
- URL: https://go.theregister.com/feed/www.theregister.com/2026/04/23/everpure_letter_covid/
- Relevance score: 5.2
- Published: 2026-04-23T14:57:19.00Z
- Summary: <h4>Storage vendor predicts current crunch will outlast COVID disruptions</h4> <p>The supply crunch gripping the storage market has pushed Everpure – the artist formerly known as Pure Storage – to reassure customers it won't make things worse.…</p>

## 112. Nancy Grace Roman Space Telescope trumps Trump cuts, is launch-ready ahead of schedule
- Domain: go.theregister.com
- URL: https://go.theregister.com/feed/www.theregister.com/2026/04/23/nancy_grace_roman_space_telescope/
- Relevance score: 5.2
- Published: 2026-04-23T13:57:15.00Z
- Summary: <h4>Revolutionary telescope aiming for space after multiple near death experiences</h4> <p>NASA's Nancy Grace Roman Space Telescope is ready for launch ahead of schedule despite repeated attempts by both Donald Trump's first and second administrations to cut funding.…</p> <p><!--#include virtual='/data_centre/_whitepaper_textlinks_top.html' --></p>

## 113. Company-wise memory in Amazon Bedrock with Amazon Neptune and Mem0
- Domain: aws.amazon.com
- URL: https://aws.amazon.com/blogs/machine-learning/company-wise-memory-in-amazon-bedrock-with-amazon-neptune-and-mem0/
- Relevance score: 5.0
- Published: Wed, 22 Apr 2026 15:56:24 +0000
- Summary: Company-wise memory in Amazon Bedrock, powered by Amazon Neptune and Mem0, provides AI agents with persistent, company-specific context—enabling them to learn, adapt, and respond intelligently across multiple interactions. TrendMicro, one of the largest antivirus software companies in the world, developed the Trend’s Companion chatbot, so their customers can explore information through natural, conversational interactions

## 114. Why the world’s banks are so worried about Anthropic’s latest AI model - The Conversation
- Domain: theconversation.com
- URL: https://news.google.com/rss/articles/CBMipgFBVV95cUxQUUJzODFIc2VuTHNzQnRUb1NSdC13MFJuM0dzbGhKRmtmWkhLSTYwcFJuakNlbEpRUkNCTXNjTnFtVWFvWXhSZk00eFFZemh6a0Rra3loSGlQV3FjRFVSemx3c3E0bjlYSGdIeHI3Y3M4b3dOeXZtSlExeXQwaWQ0QzdoRFBZNUM3WjFhT0tzM0dZaGkzN1VUdVJEOTUyR1hMcW5Zc0d3
- Relevance score: 5.0
- Published: Thu, 23 Apr 2026 20:09:54 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMipgFBVV95cUxQUUJzODFIc2VuTHNzQnRUb1NSdC13MFJuM0dzbGhKRmtmWkhLSTYwcFJuakNlbEpRUkNCTXNjTnFtVWFvWXhSZk00eFFZemh6a0Rra3loSGlQV3FjRFVSemx3c3E0bjlYSGdIeHI3Y3M4b3dOeXZtSlExeXQwaWQ0QzdoRFBZNUM3WjFhT0tzM0dZaGkzN1VUdVJEOTUyR1hMcW5Zc0d3?oc=5" target="_blank">Why the world’s banks are so worried about Anthropic’s latest AI model</a>&nbsp;&nbsp;<font color="#6f6f6f">The Conversation</font>

## 115. Blackstone president Jon Gray sees major year for IPOs driven by AI - Yahoo Finance Singapore
- Domain: sg.finance.yahoo.com
- URL: https://news.google.com/rss/articles/CBMitwFBVV95cUxPUk5zNXlrekhBdTFMQ01ZNTdDbzRjaldKWTZKSW9vTEJjLXgySGc5R0dOcTJMSDZUYTlwQU9aVUI1TFJiSzhQX0tGY2ZOaG9lOTl6S1FHY2xDcFdocW1TNnA1UnoySTFsdGlQRTNib1NlS0dPWDhCQ0hLR3hsMFhGZnJqWE9oekowUHJTR3NVTzhPV0IzNmRUY25SeEZXQk9pTUpiNmZBd0N1VzVTanhIWlh1X3pjM0k
- Relevance score: 5.0
- Published: Thu, 23 Apr 2026 18:12:05 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMitwFBVV95cUxPUk5zNXlrekhBdTFMQ01ZNTdDbzRjaldKWTZKSW9vTEJjLXgySGc5R0dOcTJMSDZUYTlwQU9aVUI1TFJiSzhQX0tGY2ZOaG9lOTl6S1FHY2xDcFdocW1TNnA1UnoySTFsdGlQRTNib1NlS0dPWDhCQ0hLR3hsMFhGZnJqWE9oekowUHJTR3NVTzhPV0IzNmRUY25SeEZXQk9pTUpiNmZBd0N1VzVTanhIWlh1X3pjM0k?oc=5" target="_blank">Blackstone president Jon Gray sees major year for IPOs driven by AI</a>&nbsp;&nbsp;<font color="#6f6f6f">Yahoo Finance Singapore</font>

## 116. The Pulse: AI token spending out of control – what’s next?
- Domain: newsletter.pragmaticengineer.com
- URL: https://newsletter.pragmaticengineer.com/p/the-pulse-ai-token-spending-out-of
- Relevance score: 5.0
- Published: Thu, 23 Apr 2026 16:51:01 GMT
- Summary: Details from 15 tech companies on the rapid growth of token spend, and their responses to it. Also: AI vendors can&#8217;t keep up with demand, plummeting morale at Meta, and more.

## 117. First Citizens to shed SVB name
- Domain: bankingdive.com
- URL: https://www.bankingdive.com/news/first-citizens-drops-svb-name-silicon-valley-bank-cit/818321/
- Relevance score: 5.0
- Published: Thu, 23 Apr 2026 11:24:21 -0400
- Summary: <figure><div><img src="https://imgproxy.divecdn.com/RidLqIJHeLRtK5AUvibTH_37EV47U168Rv35pRZozSk/g:ce/rs:fill:1600:900:1/Z3M6Ly9kaXZlc2l0ZS1zdG9yYWdlL2RpdmVpbWFnZS9HZXR0eUltYWdlcy0xMjQ5NjM5NDgzLmpwZw==.webp" /></div></figure><p>The Raleigh, North Carolina-based lender is dropping the Silicon Valley Bank name in the fourth quarter. It&rsquo;s also letting go of the CIT name that&rsquo;s remained with a commercial unit since a 2022 acquisition.</p>

## 118. Introducing GPT-5.5
- Domain: openai.com
- URL: https://openai.com/index/introducing-gpt-5-5
- Relevance score: 5.0
- Published: Thu, 23 Apr 2026 11:00:00 GMT
- Summary: Introducing GPT-5.5, our smartest model yet—faster, more capable, and built for complex tasks like coding, research, and data analysis across tools.

## 119. Samsung, SK Hynix and TSMC Battle for AI Chip Supremacy in Asia as 2026 Race Intensifies - International Business Times Australia
- Domain: ibtimes.com.au
- URL: https://news.google.com/rss/articles/CBMirAFBVV95cUxNV0s4N3VmOEpOVkw1VXQxSlJkQlNTSFhQa0luNzhSaHRKcnMzNFNvemI1YlRNQ280NGV3WTJFS3dGVWg4R1ZRUWMxLWliNVR2TFVmdGRVRzNzeGdDRTkyWW84NHJ0bmh5NVlYWmlER0hSOXk1WWszSkZYWGQycFREektWMkl6NkZZQkxHc1F3S2p1T2Nta1hJa3Awb05Cc0x6SnRuNmk5aE5IQzhU
- Relevance score: 5.0
- Published: Thu, 23 Apr 2026 09:34:07 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMirAFBVV95cUxNV0s4N3VmOEpOVkw1VXQxSlJkQlNTSFhQa0luNzhSaHRKcnMzNFNvemI1YlRNQ280NGV3WTJFS3dGVWg4R1ZRUWMxLWliNVR2TFVmdGRVRzNzeGdDRTkyWW84NHJ0bmh5NVlYWmlER0hSOXk1WWszSkZYWGQycFREektWMkl6NkZZQkxHc1F3S2p1T2Nta1hJa3Awb05Cc0x6SnRuNmk5aE5IQzhU?oc=5" target="_blank">Samsung, SK Hynix and TSMC Battle for AI Chip Supremacy in Asia as 2026 Race Intensifies</a>&nbsp;&nbsp;<font color="#6f6f6f">International Business Times Australia</font>

## 120. Samsung, SK hynix extend Korea chip rally as AI demand tightens supply - CHOSUNBIZ - Chosunbiz
- Domain: biz.chosun.com
- URL: https://news.google.com/rss/articles/CBMilAFBVV95cUxPOU1SUGI1ZTZ6RzR3MnQ3VjUtdHFKUEVHWHpudUx4SXR0MlBEWkJDRjJhN2d6ZWhBc1p0SXYtNUZ2RTM4LXA1ck5DZ3cyS3RuSGxGTzdvaERGbVpyd0h6cU0tYVZEdmpFN3FWVDdRc0Y1ZFRjSWpqaW5IQkRIZTdoSy03enBPR05KbW5LZ3YwSFpQaFo40gGUAUFVX3lxTE85TVJQYjVlNnpHNHcydDdWNS10cUpQRUdYem51THhJdHQyUERaQkNGMmE3Z3plaEFzWnRJdi01RnZFMzgtcDVyTkNndzJLdG5IbEZPN29oREZtWnJ3SHpxTS1hVkR2akU3cVZUN1FzRjVkVGNJamppbkhCREhlN2hLLTd6cE9HTkptbktndjBIWlBoWjg
- Relevance score: 5.0
- Published: Thu, 23 Apr 2026 08:23:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMilAFBVV95cUxPOU1SUGI1ZTZ6RzR3MnQ3VjUtdHFKUEVHWHpudUx4SXR0MlBEWkJDRjJhN2d6ZWhBc1p0SXYtNUZ2RTM4LXA1ck5DZ3cyS3RuSGxGTzdvaERGbVpyd0h6cU0tYVZEdmpFN3FWVDdRc0Y1ZFRjSWpqaW5IQkRIZTdoSy03enBPR05KbW5LZ3YwSFpQaFo40gGUAUFVX3lxTE85TVJQYjVlNnpHNHcydDdWNS10cUpQRUdYem51THhJdHQyUERaQkNGMmE3Z3plaEFzWnRJdi01RnZFMzgtcDVyTkNndzJLdG5IbEZPN29oREZtWnJ3SHpxTS1hVkR2akU3cVZUN1FzRjVkVGNJamppbkhCREhlN2hLLTd6cE9HTkptbktndjBIWlBoWjg?oc=5" target="_blank">Samsung, SK hynix extend Korea chip rally as AI demand tightens supply - CHOSUNBIZ</a>&nbsp;&nbsp;<font color="#6f6f6f">Chosunbiz</font>

## 121. Les réseaux sociaux pourraient freiner les capacités de lecture des adolescents selon une étude
- Domain: siecledigital.fr
- URL: https://siecledigital.fr/2026/04/23/les-reseaux-sociaux-pourraient-freiner-les-capacites-de-lecture-des-adolescents-selon-une-etude/
- Relevance score: 5.0
- Published: Thu, 23 Apr 2026 08:15:44 +0000
- Summary: <a href="https://siecledigital.fr/2026/04/23/les-reseaux-sociaux-pourraient-freiner-les-capacites-de-lecture-des-adolescents-selon-une-etude/" rel="nofollow" title="Les réseaux sociaux pourraient freiner les capacités de lecture des adolescents selon une étude"><img alt="Les réseaux sociaux pourraient freiner les capacités de lecture des adolescents selon une étude" class="webfeedsFeaturedVisual wp-post-image" height="350" src="https://siecledigital.fr/wp-content/uploads/2026/04/Les-reseaux-sociaux-pourraient-freiner-les-capacites-de-lecture-des-adolescents-selon-une-etude-600x350.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="600" /></a>On savait déjà que TikTok et Instagram monopolisaient l&#8217;attention des jeunes. Une nouvelle étude publiée dans le Journal of Research on Adolescence va plus loin. En effet, elle établit un lien direct entre l&#8217;usage intensif des réseaux et des difficultés en lecture sur plusieurs années. Que dit cette étude inquiétante ? Plus de 10 000 enfants, [&#8230;]

## 122. The global edtech boom is fading as investors look elsewhere
- Domain: restofworld.org
- URL: https://restofworld.org/2026/edtech-funding-collapse-k12-startups-ai-workforce/
- Relevance score: 5.0
- Published: Thu, 23 Apr 2026 08:00:00 +0000
- Summary: Venture capital is moving away from K-12 edtech worldwide as investors prioritize AI tools and workforce training with clearer returns.

## 123. Prime Video lance Apple TV+ en France, sans le moindre avantage sur le prix
- Domain: siecledigital.fr
- URL: https://siecledigital.fr/2026/04/23/prime-video-lance-apple-tv-en-france-sans-le-moindre-avantage-sur-le-prix/
- Relevance score: 5.0
- Published: Thu, 23 Apr 2026 07:44:20 +0000
- Summary: <a href="https://siecledigital.fr/2026/04/23/prime-video-lance-apple-tv-en-france-sans-le-moindre-avantage-sur-le-prix/" rel="nofollow" title="Prime Video lance Apple TV+ en France, sans le moindre avantage sur le prix"><img alt="Prime Video lance Apple TV+ en France, sans le moindre avantage sur le prix" class="webfeedsFeaturedVisual wp-post-image" height="350" src="https://siecledigital.fr/wp-content/uploads/2026/04/Prime-Video-lance-Apple-TV-en-France-sans-le-moindre-avantage-sur-le-prix-600x350.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="600" /></a>Les abonnés Prime Video français peuvent accéder au catalogue Apple TV sans quitter l&#8217;application Amazon. Sur le papier, la nouvelle est relativement séduisante Quel sera le prix pour Apple TV ? 9,99 euros par mois, ou 99 euros à l&#8217;année si vous préférez payer en une fois. C&#8217;est exactement ce qu&#8217;Apple facture en direct. Amazon [&#8230;]

## 124. India's IT model worked, until AI. Disruption now haunts its sub-optimal equilibrium - The Economic Times
- Domain: m.economictimes.com
- URL: https://news.google.com/rss/articles/CBMi5AFBVV95cUxNQmR2VHRBbHp0N2dxV3F5QUw5XzlSbzZ4bHpzWVNQaXh5QTV4Z2dmblRZY01Oc2dvUW1VZV81emdkN0NyYkF1MDhHQ1o0cHFnQXhKSHlaLU5Vc3l2LW9uNHhBX0NmejZhZ0hpbXN5ZTNObXNscUdFODgwSFFLTUVtSkpRekVEX3d5MkpHR3JsSlVJelJrbFlYTG1vX0xkMXZ0ZFhJYzVzeld2cmtGdEtvWVlmUXJxOUp2NVJ1V2haTjJ5cWtpZTFJalphV3B2SW5jNTN4R1pleFBNZHNqSjBaaTFmTWLSAeoBQVVfeXFMUGtHeDlJbURUYXN2R3ROU3p1clpCSTVBNmd6dUhpUHl1Zm1MVXhReFMtRUtmcVFRYXZjQ2U5Tm54cjNoV2ZZQ1libFFCd24ySnE3clBPcm8tUk9kMHlvMXp3WGU5V2x4d2N5S0s1OElPNk9OTUhQUHNwNGYtSHdXcjl3NlcxanE1bHZkQlRudEVIU1FMdnZ3cnNLNGdMUDZPaW1OZ2l5aHVEQ3UzVU1EYlEwUWFqN0Y5WUktb1Jzd1YxYS1SNU9oWVBBMDFVZUp4YmVIdGVuUkFNNXBKVHF1X0NiZGJndHlPWF9R
- Relevance score: 5.0
- Published: Fri, 24 Apr 2026 05:40:22 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi5AFBVV95cUxNQmR2VHRBbHp0N2dxV3F5QUw5XzlSbzZ4bHpzWVNQaXh5QTV4Z2dmblRZY01Oc2dvUW1VZV81emdkN0NyYkF1MDhHQ1o0cHFnQXhKSHlaLU5Vc3l2LW9uNHhBX0NmejZhZ0hpbXN5ZTNObXNscUdFODgwSFFLTUVtSkpRekVEX3d5MkpHR3JsSlVJelJrbFlYTG1vX0xkMXZ0ZFhJYzVzeld2cmtGdEtvWVlmUXJxOUp2NVJ1V2haTjJ5cWtpZTFJalphV3B2SW5jNTN4R1pleFBNZHNqSjBaaTFmTWLSAeoBQVVfeXFMUGtHeDlJbURUYXN2R3ROU3p1clpCSTVBNmd6dUhpUHl1Zm1MVXhReFMtRUtmcVFRYXZjQ2U5Tm54cjNoV2ZZQ1libFFCd24ySnE3clBPcm8tUk9kMHlvMXp3WGU5V2x4d2N5S0s1OElPNk9OTUhQUHNwNGYtSHdXcjl3NlcxanE1bHZkQlRudEVIU1FMdnZ3cnNLNGdMUDZPaW1OZ2l5aHVEQ3UzVU1EYlEwUWFqN0Y5WUktb1Jzd1YxYS1SNU9oWVBBMDFVZUp4YmVIdGVuUkFNNXBKVHF1X0NiZGJndHlPWF9R?oc=5" target="_blank">India's IT model worked, until AI. Disruption now haunts its sub-optimal equilibrium</a>&nbsp;&nbsp;<font color="#6f6f6f">The Economic Times</font>

## 125. DeepSeek rolls out new flagship AI model a year after breakthrough - Business Standard
- Domain: business-standard.com
- URL: https://news.google.com/rss/articles/CBMi2AFBVV95cUxOMkJMLU1Vc0t5VkdLR0o3SlZ0RnQ1VFJOXzRfMUt3bXB5bTV0Tk9WRTZCTHBqTTAtSzAxMzZoQ21STk1FSTczd25maFhXU3pWekpSY3pIQ0FDSDBEWGNtZFE1WUdxaC1aWlVVbXNPYk1EbDR0SThDQ1RSdlp2M05tX2c4S2xhbWxUMlJNTGlsLTZfTm53S2E0U1JVQ3VqeFhONkxzSHVKdGxiRmVUUkhVeEJkdUc3ZlNWbUFtMmNRLV9fYnNBRi1pR3NtcHM1Z01KVkw3ckR4UmXSAd4BQVVfeXFMTzQ5LVNPZ21aN09tZTBLdWlsZ0M1N3hxbGRESnZKNGxTb19DeTJPSGJmejloaDlicTZfa2NtV1VEcGczTGJKZEdUTGVkRk1jTFdHdG9KUGY0Z2tFQlBNdE9SU0xOZWhjcUZ6Yi1lQ1hfSzl5WlkzMTNHTVBpVnZuMDV5M3NmbGltQnJrVzZ1T1BDWlljSlJvelp2RlljdDRYZFNySnREb0dLUEl1VlRtOVQ2eXlUamRjWGRBSHl3NGN1VkRrSEtPTmotcWV5TF9Sci1wMlA0UFJjSDZWUHV3
- Relevance score: 5.0
- Published: Fri, 24 Apr 2026 04:37:33 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi2AFBVV95cUxOMkJMLU1Vc0t5VkdLR0o3SlZ0RnQ1VFJOXzRfMUt3bXB5bTV0Tk9WRTZCTHBqTTAtSzAxMzZoQ21STk1FSTczd25maFhXU3pWekpSY3pIQ0FDSDBEWGNtZFE1WUdxaC1aWlVVbXNPYk1EbDR0SThDQ1RSdlp2M05tX2c4S2xhbWxUMlJNTGlsLTZfTm53S2E0U1JVQ3VqeFhONkxzSHVKdGxiRmVUUkhVeEJkdUc3ZlNWbUFtMmNRLV9fYnNBRi1pR3NtcHM1Z01KVkw3ckR4UmXSAd4BQVVfeXFMTzQ5LVNPZ21aN09tZTBLdWlsZ0M1N3hxbGRESnZKNGxTb19DeTJPSGJmejloaDlicTZfa2NtV1VEcGczTGJKZEdUTGVkRk1jTFdHdG9KUGY0Z2tFQlBNdE9SU0xOZWhjcUZ6Yi1lQ1hfSzl5WlkzMTNHTVBpVnZuMDV5M3NmbGltQnJrVzZ1T1BDWlljSlJvelp2RlljdDRYZFNySnREb0dLUEl1VlRtOVQ2eXlUamRjWGRBSHl3NGN1VkRrSEtPTmotcWV5TF9Sci1wMlA0UFJjSDZWUHV3?oc=5" target="_blank">DeepSeek rolls out new flagship AI model a year after breakthrough</a>&nbsp;&nbsp;<font color="#6f6f6f">Business Standard</font>

## 126. DeepSeek Strikes Again With New AI Model to Challenge Global Tech Giants - Sri Lanka Guardian
- Domain: slguardian.org
- URL: https://news.google.com/rss/articles/CBMinAFBVV95cUxNZG1PSk9ZR3h0c3FfRmtqUThTVGNDanNialZYYkZpaUhxODVpcExPd256WVZUNW42clltRGVVTmJkVjNRaEEyRkpySmh5VXl1TmtDMGdJTHZNdEdBOE9VRmF5MG1TOUJIR2Y2RlhnQm1HRTZ5MFhyTC1WOF81UkY0M3Q3NEhCNUJpa01CQlZTM1I4alFOVTFNYUdFcUo
- Relevance score: 5.0
- Published: Fri, 24 Apr 2026 04:36:54 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMinAFBVV95cUxNZG1PSk9ZR3h0c3FfRmtqUThTVGNDanNialZYYkZpaUhxODVpcExPd256WVZUNW42clltRGVVTmJkVjNRaEEyRkpySmh5VXl1TmtDMGdJTHZNdEdBOE9VRmF5MG1TOUJIR2Y2RlhnQm1HRTZ5MFhyTC1WOF81UkY0M3Q3NEhCNUJpa01CQlZTM1I4alFOVTFNYUdFcUo?oc=5" target="_blank">DeepSeek Strikes Again With New AI Model to Challenge Global Tech Giants</a>&nbsp;&nbsp;<font color="#6f6f6f">Sri Lanka Guardian</font>

## 127. Droits voisins : la presse française a obtenu 21 millions d’euros des Big Tech et prépare sa riposte contre l'IA - mntd.fr
- Domain: mntd.fr
- URL: https://news.google.com/rss/articles/CBMiygFBVV95cUxPTUFqcUVSWnFVdHFuc0NHbVhMMy1aWERTcWdiTU5nMEtiWHZJWVhnZzRLeGQwT0lkWndWbnZKZnFOWUp4TFJnRFhUSmNNNVNhZk5iclhkWUctS1A5T3Q4LUFOMm1PTXRBYVFzVkZyWjdoVjRraVlUZVd5UGlaWmc1SVF1NXJobFRJZnAta1NmN242RFRIak56Q015cVNiYTIxd1oxVTdCcjFPeGpOTlEydkJjbmxZV1N3RlROZ2JwWXJLR3p4MUpSWGNn
- Relevance score: 5.0
- Published: Fri, 24 Apr 2026 04:03:55 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiygFBVV95cUxPTUFqcUVSWnFVdHFuc0NHbVhMMy1aWERTcWdiTU5nMEtiWHZJWVhnZzRLeGQwT0lkWndWbnZKZnFOWUp4TFJnRFhUSmNNNVNhZk5iclhkWUctS1A5T3Q4LUFOMm1PTXRBYVFzVkZyWjdoVjRraVlUZVd5UGlaWmc1SVF1NXJobFRJZnAta1NmN242RFRIak56Q015cVNiYTIxd1oxVTdCcjFPeGpOTlEydkJjbmxZV1N3RlROZ2JwWXJLR3p4MUpSWGNn?oc=5" target="_blank">Droits voisins : la presse française a obtenu 21 millions d’euros des Big Tech et prépare sa riposte contre l'IA</a>&nbsp;&nbsp;<font color="#6f6f6f">mntd.fr</font>

## 128. RBI Floats New Draft Rules To Govern Prepaid Payment Instruments
- Domain: inc42.com
- URL: https://inc42.com/buzz/rbi-floats-new-draft-rules-to-govern-prepaid-payment-instruments/
- Relevance score: 4.8
- Published: Wed, 22 Apr 2026 19:25:05 +0000
- Summary: <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="1020" src="https://inc42.com/cdn-cgi/image/quality=90/https://asset.inc42.com/2026/04/0205_MPC-RBI_Feature.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="1360" />The Reserve Bank of India (RBI) yesterday issued the draft framework to regulate prepaid payment instruments (PPIs). Called the draft&#8230;

## 129. Claude survey: new capabilities beat speed as top AI benefit, but creatives feel left behind
- Domain: the-decoder.com
- URL: https://the-decoder.com/claude-survey-new-capabilities-beat-speed-as-top-ai-benefit-but-creatives-feel-left-behind/
- Relevance score: 4.8
- Published: Thu, 23 Apr 2026 14:10:54 +0000
- Summary: <p><img alt="" class="attachment-full size-full wp-post-image" height="961" src="https://the-decoder.com/wp-content/uploads/2026/04/Anthropic-AI-Work.png" style="height: auto; margin-bottom: 10px;" width="1708" /></p> <p> A survey of 81,000 Claude users shows that gaining new capabilities ranks slightly ahead of speed as the most common productivity benefit. Creatives, meanwhile, feel both limited and threatened by AI. The sample, however, has a significant bias.</p> <p>The article <a href="https://the-decoder.com/claude-survey-new-capabilities-beat-speed-as-top-ai-benefit-but-creatives-feel-left-behind/">Claude survey: new capabilities beat speed as top AI benefit, but creatives feel left behind</a> appeared first on <a href="https://the-decoder.com">The Decoder</a>.</p>

## 130. MeitY tightens AI label rules, mandates continuous disclosure
- Domain: medianama.com
- URL: https://www.medianama.com/2026/04/223-meity-ai-label-rules-mandates-continuous-disclosure/
- Relevance score: 4.8
- Published: Thu, 23 Apr 2026 08:05:22 +0000
- Summary: <p>You can access the original document from hereYou can access the notification from here The Ministry of Electronics and Information&#8230;</p> <p>The post <a href="https://www.medianama.com/2026/04/223-meity-ai-label-rules-mandates-continuous-disclosure/">MeitY tightens AI label rules, mandates continuous disclosure</a> appeared first on <a href="https://www.medianama.com">MEDIANAMA</a>.</p>

## 131. Anthropic&#8217;s Mythos breach was humiliating
- Domain: theverge.com
- URL: https://www.theverge.com/ai-artificial-intelligence/917644/anthropic-claude-mythos-breach-humiliation
- Relevance score: 4.8
- Published: 2026-04-23T14:24:56-04:00
- Summary: Anthropic's tightly controlled rollout of Claude Mythos has taken an awkward turn. After spending weeks insisting the AI model is so capable at cybersecurity that it is too dangerous to release publicly, it appears the model fell into the wrong hands anyway. According to Bloomberg, a "small group of unauthorized users" has had access to [&#8230;]

## 132. Semiconductor windfall exposes risks as unions press for bonuses - Korea JoongAng Daily
- Domain: koreajoongangdaily.joins.com
- URL: https://news.google.com/rss/articles/CBMi3AFBVV95cUxOX2NSZzJvMDV3aUViNW9VV2NyZ2xhLUJZQjBWYkVDMXZlODFPSUpKcDRJUlZEWTNEOV80cGpfbk1XR21rMHJSU2ttOExNdFlESElZMkUxcjVIeW42UFlnVFJYczNrTzZfZE1ucUpOUnNNMDJoQWp2WHFFckdtSEhVSjRDZWNsejVvWDExVm1XMS1tY0k3MG9iYTBGS3lhYUlCNmpuZjhEOFpmUFJXRnJxei11NWsxNGFvU1MtS25fVFN3b3lRbmJpdUZaS29tTUFrby1RZXVnOTlxZVRm
- Relevance score: 4.7
- Published: Thu, 23 Apr 2026 15:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi3AFBVV95cUxOX2NSZzJvMDV3aUViNW9VV2NyZ2xhLUJZQjBWYkVDMXZlODFPSUpKcDRJUlZEWTNEOV80cGpfbk1XR21rMHJSU2ttOExNdFlESElZMkUxcjVIeW42UFlnVFJYczNrTzZfZE1ucUpOUnNNMDJoQWp2WHFFckdtSEhVSjRDZWNsejVvWDExVm1XMS1tY0k3MG9iYTBGS3lhYUlCNmpuZjhEOFpmUFJXRnJxei11NWsxNGFvU1MtS25fVFN3b3lRbmJpdUZaS29tTUFrby1RZXVnOTlxZVRm?oc=5" target="_blank">Semiconductor windfall exposes risks as unions press for bonuses</a>&nbsp;&nbsp;<font color="#6f6f6f">Korea JoongAng Daily</font>

## 133. The AI workplace paradox: Higher productivity, higher anxiety - Computerworld
- Domain: computerworld.com
- URL: https://news.google.com/rss/articles/CBMirwFBVV95cUxQalE0NGs5d295YU5XUmQyVDFNMWtlcC1XOG1ZSWxoamVUb3RsRm9vM2hTWkl0SV8xS1RhOVdTMHdpN3V5bWpMZFVpcjllUlpFQnlEWDRBRUloWlk1ak40dUZtRS1mMm9heHM3ek8yTlRXZGpmMnIwUmJSR09udmhObi0zbHJ4c3E3ejF6NWJQQ2YxVm9vY29PWm56QjAxNTQ0N0lOVi1hRXhERktpQ3lj
- Relevance score: 4.7
- Published: Fri, 24 Apr 2026 02:34:46 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMirwFBVV95cUxQalE0NGs5d295YU5XUmQyVDFNMWtlcC1XOG1ZSWxoamVUb3RsRm9vM2hTWkl0SV8xS1RhOVdTMHdpN3V5bWpMZFVpcjllUlpFQnlEWDRBRUloWlk1ak40dUZtRS1mMm9heHM3ek8yTlRXZGpmMnIwUmJSR09udmhObi0zbHJ4c3E3ejF6NWJQQ2YxVm9vY29PWm56QjAxNTQ0N0lOVi1hRXhERktpQ3lj?oc=5" target="_blank">The AI workplace paradox: Higher productivity, higher anxiety</a>&nbsp;&nbsp;<font color="#6f6f6f">Computerworld</font>

## 134. Google unleashes even more AI security agents to fight the baddies
- Domain: go.theregister.com
- URL: https://go.theregister.com/feed/www.theregister.com/2026/04/22/google_unleashes_even_more_ai/
- Relevance score: 4.7
- Published: 2026-04-22T12:01:43.00Z
- Summary: <h4>Along with a bunch of new services to make sure those same agents don't cause chaos</h4> <p><strong>Google Cloud Next</strong> Google Cloud chief operating officer Francis deSouza has summed up his company's security strategy du jour as follows: "You need to use AI to fight AI."…</p>

## 135. Database world trying to build natural language query systems again – this time with LLMs
- Domain: go.theregister.com
- URL: https://go.theregister.com/feed/www.theregister.com/2026/04/22/llms_natural_langauge_systems_new/
- Relevance score: 4.7
- Published: 2026-04-22T10:00:08.00Z
- Summary: <h4>Text-to-SQL might be useful for analysts and DBAs, but be cautious with general user adoption</h4> <p>Over the past few years, database and analytics vendors have hopped on a bandwagon that may take us all to a destination where common data queries are free from the constraints of the specialist query language SQL.…</p>

## 136. Microsoft and Meta announce large staff reductions as they spend big on AI
- Domain: theguardian.com
- URL: https://www.theguardian.com/technology/2026/apr/23/meta-microsoft-tech-ai-layoffs
- Relevance score: 4.5
- Published: Thu, 23 Apr 2026 22:51:49 GMT
- Summary: <p>Meta said it would cut 10% of it employees while Microsoft will offer voluntary retirement to about 7% of workers</p><p>Meta and Microsoft are trimming their workforces by thousands as they make heavy investments in AI and executives claim that the technology is meeting their companies’ productivity needs.</p><p>Meta told staff on Thursday that on 20 May it would cut some 10% of its personnel – just under 8,000 employees– to boost efficiency, part of a layoff plan <a href="https://www.theguardian.com/technology/2026/mar/13/meta-layoffs-ai">made months ago</a>. The company is also closing about 6,000 open roles. The same day, Microsoft <a href="https://www.ft.com/content/f5776fd6-22f3-43d1-806b-9858b64cfd18?syn-25a6b1a6=1">announced</a> to employees, for the first time, that it would offer voluntary retirement to about 7% of its American workforce of roughly 125,000.</p> <a href="https://www.theguardian.com/technology/2026/apr/23/meta-microsoft-tech-ai-layoffs">Continue reading...</a>

## 137. Stanchart, A*STAR collab on AI-led innovation for financial services - Frontier Enterprise
- Domain: frontier-enterprise.com
- URL: https://news.google.com/rss/articles/CBMipgFBVV95cUxOd2xDQlBIcFBJenc5V05GNUo3WFh6UjZ4U245eTZFOWFWaGVJeURuN1NKY1cyZ215VldrTHh3X0I4VEUzaGd4NnQ0Y2NaQ3A2aE1uOHNLS2xGYmlMd3dGM2FEaExfdE1sUnVBcjFBX2hqTmFWT0VHUzJYTjdVLWk1enRRSGQtMkNTMV92WE5ZeGJtaHU2Q1lNWnlBZjV3TGN4azc5MDRn
- Relevance score: 4.5
- Published: Thu, 23 Apr 2026 19:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMipgFBVV95cUxOd2xDQlBIcFBJenc5V05GNUo3WFh6UjZ4U245eTZFOWFWaGVJeURuN1NKY1cyZ215VldrTHh3X0I4VEUzaGd4NnQ0Y2NaQ3A2aE1uOHNLS2xGYmlMd3dGM2FEaExfdE1sUnVBcjFBX2hqTmFWT0VHUzJYTjdVLWk1enRRSGQtMkNTMV92WE5ZeGJtaHU2Q1lNWnlBZjV3TGN4azc5MDRn?oc=5" target="_blank">Stanchart, A*STAR collab on AI-led innovation for financial services</a>&nbsp;&nbsp;<font color="#6f6f6f">Frontier Enterprise</font>

## 138. IA agentique : les nouvelles compétences que les entreprises recherchent - LeMagIT
- Domain: lemagit.fr
- URL: https://news.google.com/rss/articles/CBMitAFBVV95cUxPSGVEOXEwa0JYbjJxVXBOUDJwc3BSLXRGbjRxMmFxcjQ5Mmh1ZXdmSE5JMGI1ZGt5WU5Lb2lGNmJQdFg3MFFjSUw0RjE0aXdFalp4ZUZQRVJXNFBFUFkzZUlBUmRudUtDZTZ1ZGk0OHlzWjdpWlNuLVFJYmozLWlTcXg5UDBZNVM2ZGd6XzRVRkZOcXo0V2hrQnVzUFZZTjJrc01aY0xJSTVvOVhpUUswVUVvUjQ
- Relevance score: 4.5
- Published: Thu, 23 Apr 2026 14:19:36 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMitAFBVV95cUxPSGVEOXEwa0JYbjJxVXBOUDJwc3BSLXRGbjRxMmFxcjQ5Mmh1ZXdmSE5JMGI1ZGt5WU5Lb2lGNmJQdFg3MFFjSUw0RjE0aXdFalp4ZUZQRVJXNFBFUFkzZUlBUmRudUtDZTZ1ZGk0OHlzWjdpWlNuLVFJYmozLWlTcXg5UDBZNVM2ZGd6XzRVRkZOcXo0V2hrQnVzUFZZTjJrc01aY0xJSTVvOVhpUUswVUVvUjQ?oc=5" target="_blank">IA agentique : les nouvelles compétences que les entreprises recherchent</a>&nbsp;&nbsp;<font color="#6f6f6f">LeMagIT</font>

## 139. Making Sense of the Early Universe
- Domain: blogs.nvidia.com
- URL: https://blogs.nvidia.com/blog/ai-gpu-early-universe-astronomy/
- Relevance score: 4.5
- Published: Thu, 23 Apr 2026 13:00:22 +0000
- Summary: This Spring Astronomy Day, here’s a look at how AI and GPUs are helping astronomers work through unprecedented volumes of cosmic data.

## 140. Billing for intelligence: how the value exchange hub will define the internet of agents - TMForum - Inform
- Domain: inform.tmforum.org
- URL: https://news.google.com/rss/articles/CBMi0AFBVV95cUxPSWY4TWJ2eTlYaklvb0cwWXB0ejJ5bXctTEUxUnM0bXlxcjBlRm5FOVdNUlRZSEQ2VzBQSkRWOWxSdFNKWnV4R1M5MVZqeFZxQnRhWl91RWI1T0hVcXgycV8yeE1jcTMxVUN6eDN2V2FNUzhITFVoUjhNalN2cjItbUttMmJaU1QxeG9aSnNGSVlMUGttNXFOMVBnUjlqY3JfTzB0UjVPekRJUjlkbC0xLWxIV0hTT0ZNTm1FU1dLU1hOaERtSlFKV0RySXZ2NUYy
- Relevance score: 4.5
- Published: Thu, 23 Apr 2026 11:09:05 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi0AFBVV95cUxPSWY4TWJ2eTlYaklvb0cwWXB0ejJ5bXctTEUxUnM0bXlxcjBlRm5FOVdNUlRZSEQ2VzBQSkRWOWxSdFNKWnV4R1M5MVZqeFZxQnRhWl91RWI1T0hVcXgycV8yeE1jcTMxVUN6eDN2V2FNUzhITFVoUjhNalN2cjItbUttMmJaU1QxeG9aSnNGSVlMUGttNXFOMVBnUjlqY3JfTzB0UjVPekRJUjlkbC0xLWxIV0hTT0ZNTm1FU1dLU1hOaERtSlFKV0RySXZ2NUYy?oc=5" target="_blank">Billing for intelligence: how the value exchange hub will define the internet of agents</a>&nbsp;&nbsp;<font color="#6f6f6f">TMForum - Inform</font>

## 141. Souveraineté financière : startups, banques et marchés à l’épreuve de l’échelle européenne
- Domain: maddyness.com
- URL: https://www.maddyness.com/2026/04/23/souverainete-financiere-startups-banques-et-marches-a-lepreuve-de-lechelle-europeenne/
- Relevance score: 4.5
- Published: Thu, 23 Apr 2026 09:13:07 +0000
- Summary: <p>L’article <a href="https://www.maddyness.com/2026/04/23/souverainete-financiere-startups-banques-et-marches-a-lepreuve-de-lechelle-europeenne/">Souveraineté financière : startups, banques et marchés à l’épreuve de l’échelle européenne</a> est apparu en premier sur <a href="https://www.maddyness.com">Maddyness - Le média pour comprendre l&#039;économie de demain</a>.</p>

## 142. Health Data Hub : Scaleway remplace (enfin) Microsoft
- Domain: maddyness.com
- URL: https://www.maddyness.com/2026/04/23/health-data-hub-scaleway-remplace-enfin-microsoft/
- Relevance score: 4.5
- Published: Thu, 23 Apr 2026 08:45:58 +0000
- Summary: <p>L’article <a href="https://www.maddyness.com/2026/04/23/health-data-hub-scaleway-remplace-enfin-microsoft/">Health Data Hub : Scaleway remplace (enfin) Microsoft</a> est apparu en premier sur <a href="https://www.maddyness.com">Maddyness - Le média pour comprendre l&#039;économie de demain</a>.</p>

## 143. GPT-5.5 Bio Bug Bounty
- Domain: openai.com
- URL: https://openai.com/index/gpt-5-5-bio-bug-bounty
- Relevance score: 4.5
- Published: Thu, 23 Apr 2026 00:00:00 GMT
- Summary: Explore the GPT-5.5 Bio Bug Bounty: a red-teaming challenge to find universal jailbreaks for bio safety risks, with rewards up to $25,000.

## 144. LMA issues AI governance blueprint as Lloyd’s market steps up adoption - Insurance Business
- Domain: insurancebusinessmag.com
- URL: https://news.google.com/rss/articles/CBMizAFBVV95cUxNWndHMnN6eW12VDBPUHpOeUFEUFRMcC1xTlBBalVMb0VueWFrZWpCYXdOdmJpMkMydUhlWTVtc3NSVXdfZ0FyMWpYQnYweUZ5QW4zcXNWWGNPb1pzU1pNel90QnpQblZXT0dHbGlYYWRDRGNwSnpTV2pfNUt6Qm1rdFFtRjhpU0pjRGxSMkd4dzZuUHFqTG1peEdMNmxOWENzamtNeHltZ0phUHBoWXFROXd3eEZlTGlWNUtreURKRmluT0QyQzhEemdwSlY
- Relevance score: 4.5
- Published: Fri, 24 Apr 2026 04:49:10 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMizAFBVV95cUxNWndHMnN6eW12VDBPUHpOeUFEUFRMcC1xTlBBalVMb0VueWFrZWpCYXdOdmJpMkMydUhlWTVtc3NSVXdfZ0FyMWpYQnYweUZ5QW4zcXNWWGNPb1pzU1pNel90QnpQblZXT0dHbGlYYWRDRGNwSnpTV2pfNUt6Qm1rdFFtRjhpU0pjRGxSMkd4dzZuUHFqTG1peEdMNmxOWENzamtNeHltZ0phUHBoWXFROXd3eEZlTGlWNUtreURKRmluT0QyQzhEemdwSlY?oc=5" target="_blank">LMA issues AI governance blueprint as Lloyd’s market steps up adoption</a>&nbsp;&nbsp;<font color="#6f6f6f">Insurance Business</font>

## 145. Pour Google, il faut une « défense totalement guidée par l’IA » contre de potentielles cyberattaques agentiques - La Tribune
- Domain: latribune.fr
- URL: https://news.google.com/rss/articles/CBMikwJBVV95cUxQMkFtVnVTWk81VGx1ekFzLTVJZ1R2dElWNC04RTkxODdlWTJYdkpUTFdjQnhPQzVLcmQ4MEw1NVJWNW16eUxwZmVsTDVjN3pWbmFHSVprWldaNkFWa09tNmwwMFBwSEFtVUQ1eS1ibWhJQlJxWTVnSFZ4alFlNW5BYmxrNG53N1RkM2kzUWZIVkxONkhuQ0RCSUhDZmRBdWRfWFBZMmxNSmRUS0FMSmlVeXo5ZUtZTnloZkxqLVM1NGlCOE0wWjBGZXdmeGwzbXZoT0o1WmNmQzFUXzZ3bXRqcmJ3Um1yVFJQdDVraThSUk1yb2plM0NTMGtYZGdGUHdXckVnR19MWXdsb0ZLSVdDSkZJaw
- Relevance score: 4.5
- Published: Fri, 24 Apr 2026 04:30:01 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMikwJBVV95cUxQMkFtVnVTWk81VGx1ekFzLTVJZ1R2dElWNC04RTkxODdlWTJYdkpUTFdjQnhPQzVLcmQ4MEw1NVJWNW16eUxwZmVsTDVjN3pWbmFHSVprWldaNkFWa09tNmwwMFBwSEFtVUQ1eS1ibWhJQlJxWTVnSFZ4alFlNW5BYmxrNG53N1RkM2kzUWZIVkxONkhuQ0RCSUhDZmRBdWRfWFBZMmxNSmRUS0FMSmlVeXo5ZUtZTnloZkxqLVM1NGlCOE0wWjBGZXdmeGwzbXZoT0o1WmNmQzFUXzZ3bXRqcmJ3Um1yVFJQdDVraThSUk1yb2plM0NTMGtYZGdGUHdXckVnR19MWXdsb0ZLSVdDSkZJaw?oc=5" target="_blank">Pour Google, il faut une « défense totalement guidée par l’IA » contre de potentielles cyberattaques agentiques</a>&nbsp;&nbsp;<font color="#6f6f6f">La Tribune</font>

## 146. Meta to layoff 8,000 from its workforce, amid AI spending push: Report - The Indian Express
- Domain: indianexpress.com
- URL: https://news.google.com/rss/articles/CBMi3wFBVV95cUxOTGEyQlBaZGlnNC1nQ19uVk5XNW90TTd6YUdWWGZNRjhUTWMyMHJKOVFPclJjWTk1dDNGay0tbVJiVDhIa2hKdVM5SVIxSFVZbm0zakN4Ym4xNVVEVExHUTRfdW9qeUtMZlktd29pNUswbTNsQ2NzMm1GWkhUckwxQmhqR0s1bXhtMmVSRUhqX3RwamprcjNhLXBOYi1fby1BX3VSdHVjcExMZE5kZjNmVnFVMGpVdmhucEFpV0ZiZkpNQy03cjlfbmR2NmIyMFN3M1lwV2d6dU9EMWppdjc40gHmAUFVX3lxTE5NMXVmd0NMY294QldOZ0dpV2FkMUhUdF9vNGtUY1RJZURHdzNyWFJRdFBUa2hXYjVYV1RlY3VxTVBkV2VNZnJQREFYUzluNXV4ZmhSS19JUkwwYzVaRkFSVnVHZDNDRU51cldwUWczNFFPRkQyUVpaMmtqMEVybTNuTGZSRmR3Rl9DTVdlVFJxdnBTd3prdG1oTnhIczJUandidDNQRXB1SF9yMEtqMDBabnRnVXd0NENrNEV3cUpNMmRiVUJEVkhyUDMtMEYwaG9wc1BsaDVNcXNxSXNDejBJejJWQ0Zn
- Relevance score: 4.5
- Published: Fri, 24 Apr 2026 03:57:39 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi3wFBVV95cUxOTGEyQlBaZGlnNC1nQ19uVk5XNW90TTd6YUdWWGZNRjhUTWMyMHJKOVFPclJjWTk1dDNGay0tbVJiVDhIa2hKdVM5SVIxSFVZbm0zakN4Ym4xNVVEVExHUTRfdW9qeUtMZlktd29pNUswbTNsQ2NzMm1GWkhUckwxQmhqR0s1bXhtMmVSRUhqX3RwamprcjNhLXBOYi1fby1BX3VSdHVjcExMZE5kZjNmVnFVMGpVdmhucEFpV0ZiZkpNQy03cjlfbmR2NmIyMFN3M1lwV2d6dU9EMWppdjc40gHmAUFVX3lxTE5NMXVmd0NMY294QldOZ0dpV2FkMUhUdF9vNGtUY1RJZURHdzNyWFJRdFBUa2hXYjVYV1RlY3VxTVBkV2VNZnJQREFYUzluNXV4ZmhSS19JUkwwYzVaRkFSVnVHZDNDRU51cldwUWczNFFPRkQyUVpaMmtqMEVybTNuTGZSRmR3Rl9DTVdlVFJxdnBTd3prdG1oTnhIczJUandidDNQRXB1SF9yMEtqMDBabnRnVXd0NENrNEV3cUpNMmRiVUJEVkhyUDMtMEYwaG9wc1BsaDVNcXNxSXNDejBJejJWQ0Zn?oc=5" target="_blank">Meta to layoff 8,000 from its workforce, amid AI spending push: Report</a>&nbsp;&nbsp;<font color="#6f6f6f">The Indian Express</font>

## 147. Meta plans 10% layoffs as AI spending soars: Source - CNA
- Domain: channelnewsasia.com
- URL: https://news.google.com/rss/articles/CBMiiwFBVV95cUxOTm1Vem9KcmkxVms2SHlTV3ZzMXhCQUlaek1WQWRlbk41d0lyM1pqbzZfOUxNQzFtRVNMeDN1UVFHZU9RTEZmNnVOaXZ0Z0lYTEowNE90WWJWS3c2b2ItWElPVEtZQV8wQmJ2U1d0eFdhTU9RZnVib2Y4THFRNHY0aXM2dzF4S3FBT1gw
- Relevance score: 4.5
- Published: Fri, 24 Apr 2026 00:36:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiiwFBVV95cUxOTm1Vem9KcmkxVms2SHlTV3ZzMXhCQUlaek1WQWRlbk41d0lyM1pqbzZfOUxNQzFtRVNMeDN1UVFHZU9RTEZmNnVOaXZ0Z0lYTEowNE90WWJWS3c2b2ItWElPVEtZQV8wQmJ2U1d0eFdhTU9RZnVib2Y4THFRNHY0aXM2dzF4S3FBT1gw?oc=5" target="_blank">Meta plans 10% layoffs as AI spending soars: Source</a>&nbsp;&nbsp;<font color="#6f6f6f">CNA</font>

## 148. Publicis Groupe APAC opens Singapore AI Hub to scale marketing tech globally - Campaign Brief Asia
- Domain: campaignbriefasia.com
- URL: https://news.google.com/rss/articles/CBMiugFBVV95cUxQMEtLMWlwQmdESEphRC1oMjhBVlhFbV92bC1YME5sM1pCZ1FlNXVEQ3llWFlFc2N3U1JOWC12cG4xNG15dXRoUlh5bF9RNFZtUjdzZHRaYU5oWkdxa1doTjk5b2tsMEtlZWFhRVZvcnFZclJPOU1ZMVJfWjhsRWQxRnJ1YldYcERlVEdKLWZVaHNHTXhZTmJFUUpEVHRoMU1wRHZKdlNid1dELWtCZUFwbXNfWm9ScGg3eFE
- Relevance score: 4.5
- Published: Fri, 24 Apr 2026 00:29:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiugFBVV95cUxQMEtLMWlwQmdESEphRC1oMjhBVlhFbV92bC1YME5sM1pCZ1FlNXVEQ3llWFlFc2N3U1JOWC12cG4xNG15dXRoUlh5bF9RNFZtUjdzZHRaYU5oWkdxa1doTjk5b2tsMEtlZWFhRVZvcnFZclJPOU1ZMVJfWjhsRWQxRnJ1YldYcERlVEdKLWZVaHNHTXhZTmJFUUpEVHRoMU1wRHZKdlNid1dELWtCZUFwbXNfWm9ScGg3eFE?oc=5" target="_blank">Publicis Groupe APAC opens Singapore AI Hub to scale marketing tech globally</a>&nbsp;&nbsp;<font color="#6f6f6f">Campaign Brief Asia</font>

## 149. Sony WH-1000XM6 vs. Bowers & Wilkins Px8 S2: How I'd justify spending $300 more for headphones
- Domain: zdnet.com
- URL: https://www.zdnet.com/article/sony-wh-1000xm6-vs-bowers-wilkins-px8-s2/
- Relevance score: 4.2
- Published: Thu, 23 Apr 2026 14:58:18 GMT
- Summary: Sony may be at the top of its game, but how well do the XM6 stack up against its more premium competitors? It comes down to how you use them.

## 150. YouTuber has DIMM idea, builds working DRAM in backyard
- Domain: go.theregister.com
- URL: https://go.theregister.com/feed/www.theregister.com/2026/04/23/youtuber_builds_working_dram/
- Relevance score: 4.2
- Published: 2026-04-23T17:43:14.00Z
- Summary: <h4>What are <i>you</i> doing to solve the memory crisis?</h4> <p>If you follow PC hardware prices, you’ll know AI demand has pushed memory prices higher as manufacturers prioritize memory for datacenters. To deal with that, you can pay through the nose, buy less memory, or ... try to build your own DRAM.…</p>

## 151. OpenAI recrute l’ancien patron Europe d’Airbnb pour monter en puissance sur le Vieux Continent
- Domain: maddyness.com
- URL: https://www.maddyness.com/2026/04/22/openai-recrute-lancien-patron-europe-dairbnb-pour-monter-en-puissance-sur-le-vieux-continent/
- Relevance score: 4.0
- Published: Wed, 22 Apr 2026 14:10:20 +0000
- Summary: <p>L’article <a href="https://www.maddyness.com/2026/04/22/openai-recrute-lancien-patron-europe-dairbnb-pour-monter-en-puissance-sur-le-vieux-continent/">OpenAI recrute l’ancien patron Europe d’Airbnb pour monter en puissance sur le Vieux Continent</a> est apparu en premier sur <a href="https://www.maddyness.com">Maddyness - Le média pour comprendre l&#039;économie de demain</a>.</p>

## 152. Insilico Medicine Showcases AI Drug Discovery Strategy at CNBC Converge and AACR - TipRanks
- Domain: tipranks.com
- URL: https://news.google.com/rss/articles/CBMixwFBVV95cUxNaFd2Ujl3MVM1eGxzb0w2OXJGQXd1cWlMd25Vbi0xUnNLSVl3S0gxZWF3X0VRS3pTN0FJSVVCdEtzRFVOSDNfTmk3NDBfeS10RG5VUzBCVi1yQklKbHdlcUlhNG9rUG5EOWxqaFZYWi16bWZtbVh2anc3bW5iYzBhMmVlcFJkLXFsS25NdGFjeTEzdGkyNUxhTlJHMGN3VFQ1Y01UYzYxZHVVbXQyNDlNZWJxNHYzSHRnb2ZMNTh4SEp2Qm95OVpv
- Relevance score: 4.0
- Published: Wed, 22 Apr 2026 06:22:03 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMixwFBVV95cUxNaFd2Ujl3MVM1eGxzb0w2OXJGQXd1cWlMd25Vbi0xUnNLSVl3S0gxZWF3X0VRS3pTN0FJSVVCdEtzRFVOSDNfTmk3NDBfeS10RG5VUzBCVi1yQklKbHdlcUlhNG9rUG5EOWxqaFZYWi16bWZtbVh2anc3bW5iYzBhMmVlcFJkLXFsS25NdGFjeTEzdGkyNUxhTlJHMGN3VFQ1Y01UYzYxZHVVbXQyNDlNZWJxNHYzSHRnb2ZMNTh4SEp2Qm95OVpv?oc=5" target="_blank">Insilico Medicine Showcases AI Drug Discovery Strategy at CNBC Converge and AACR</a>&nbsp;&nbsp;<font color="#6f6f6f">TipRanks</font>

## 153. L’IA peut-elle ressentir nos émotions ? - 42 - La réponse à presque tout - Regarder le documentaire complet - Arte.tv
- Domain: arte.tv
- URL: https://news.google.com/rss/articles/CBMiiAFBVV95cUxQanZYRjRCZ3VUN3N2aGlWNmhRLXFnRl9qVEZ5NlhJQ2pJc0Q3dXRyNWxSU2F0RldaNGNMTVdSeG01Vm9wQnBYcFI5ejQ2N3dpM1JydXJBMFhzY0JnTFdySEVmSU5MUy1wU3h2YmdFXzU0N05oNHZfWjdiVHd4bnBHMHdQejFueXFH
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 23:52:16 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiiAFBVV95cUxQanZYRjRCZ3VUN3N2aGlWNmhRLXFnRl9qVEZ5NlhJQ2pJc0Q3dXRyNWxSU2F0RldaNGNMTVdSeG01Vm9wQnBYcFI5ejQ2N3dpM1JydXJBMFhzY0JnTFdySEVmSU5MUy1wU3h2YmdFXzU0N05oNHZfWjdiVHd4bnBHMHdQejFueXFH?oc=5" target="_blank">L’IA peut-elle ressentir nos émotions ? - 42 - La réponse à presque tout - Regarder le documentaire complet</a>&nbsp;&nbsp;<font color="#6f6f6f">Arte.tv</font>

## 154. ATS Breathe Easy - The ATS AI Taskforce Tackling Technological Questions | Newswise - Newswise
- Domain: newswise.com
- URL: https://news.google.com/rss/articles/CBMipwFBVV95cUxQY3dScjZPcUdQVkM0NWpvbkdFY2N2aXJ5X1dUZHZVN2lEU0J1TDAyOEd2eVl1Q0pSWDJidV9uOXd3Y3hyaC0wQkpWVVQtV0xuYTJEVEhGeVdPR2dUT0NSbFNMVk5iMGJjdV82bWphMms0WkU5NG1UcGJuVFJTekluMUF0SEd6LU9WaDVNc1hBOEFJVVdvRzd6OGg5QzVKYmJuMTBBMFRONNIBpwFBVV95cUxQY3dScjZPcUdQVkM0NWpvbkdFY2N2aXJ5X1dUZHZVN2lEU0J1TDAyOEd2eVl1Q0pSWDJidV9uOXd3Y3hyaC0wQkpWVVQtV0xuYTJEVEhGeVdPR2dUT0NSbFNMVk5iMGJjdV82bWphMms0WkU5NG1UcGJuVFJTekluMUF0SEd6LU9WaDVNc1hBOEFJVVdvRzd6OGg5QzVKYmJuMTBBMFRONA
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 23:40:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMipwFBVV95cUxQY3dScjZPcUdQVkM0NWpvbkdFY2N2aXJ5X1dUZHZVN2lEU0J1TDAyOEd2eVl1Q0pSWDJidV9uOXd3Y3hyaC0wQkpWVVQtV0xuYTJEVEhGeVdPR2dUT0NSbFNMVk5iMGJjdV82bWphMms0WkU5NG1UcGJuVFJTekluMUF0SEd6LU9WaDVNc1hBOEFJVVdvRzd6OGg5QzVKYmJuMTBBMFRONNIBpwFBVV95cUxQY3dScjZPcUdQVkM0NWpvbkdFY2N2aXJ5X1dUZHZVN2lEU0J1TDAyOEd2eVl1Q0pSWDJidV9uOXd3Y3hyaC0wQkpWVVQtV0xuYTJEVEhGeVdPR2dUT0NSbFNMVk5iMGJjdV82bWphMms0WkU5NG1UcGJuVFJTekluMUF0SEd6LU9WaDVNc1hBOEFJVVdvRzd6OGg5QzVKYmJuMTBBMFRONA?oc=5" target="_blank">ATS Breathe Easy - The ATS AI Taskforce Tackling Technological Questions | Newswise</a>&nbsp;&nbsp;<font color="#6f6f6f">Newswise</font>

## 155. FairPrice to roll out AI-powered smart carts to more stores - Computer Weekly
- Domain: computerweekly.com
- URL: https://news.google.com/rss/articles/CBMiqAFBVV95cUxPZERWMXF6T25XYzRwbWtFZF9qTkZjWlhLd2J5SDJUd3h6TzFsUlA0bkRQUm8wOEN6Z1lBVVlsYU5SbURrUHZHazRLUDk4elVIaDhKYUlqT1d2ZlBJUlRGNXVLRnZXUElvTVU0NjVLWVQ5LWFaNnZFNG1iU1FzcnZkVlVaeTdzNlk5SXliNnZVNkt3UDQ4b2l1OG1icmpBQUhzRDJJQV92UWM
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 23:37:53 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiqAFBVV95cUxPZERWMXF6T25XYzRwbWtFZF9qTkZjWlhLd2J5SDJUd3h6TzFsUlA0bkRQUm8wOEN6Z1lBVVlsYU5SbURrUHZHazRLUDk4elVIaDhKYUlqT1d2ZlBJUlRGNXVLRnZXUElvTVU0NjVLWVQ5LWFaNnZFNG1iU1FzcnZkVlVaeTdzNlk5SXliNnZVNkt3UDQ4b2l1OG1icmpBQUhzRDJJQV92UWM?oc=5" target="_blank">FairPrice to roll out AI-powered smart carts to more stores</a>&nbsp;&nbsp;<font color="#6f6f6f">Computer Weekly</font>

## 156. Japan ruling party seeks AI penalties over deepfakes, piracy - upi.com
- Domain: upi.com
- URL: https://news.google.com/rss/articles/CBMiuAFBVV95cUxNYnM2bGgybFJfSjNZMXhnOW4wckFDLVFVOGxSVi0tTWhvVm9KTHNrbEY1eERRQ0h4V1N1NDVENUx1SW1vc28xS0Jubi1tdUVGU1BucEI5cXdZTmdNcFhZTDJnSGZQSXhYNXgtNV9JT0JSaFZSZ0RYeUdQaERrOFFXQTVoMzRLeVpLYTF6TFlvdUZrM0UyQ2xjM29TNDM3SEhfczI2cC1Fa2RRWUNBWEtDVjBBb2ZxWDFr0gG-AUFVX3lxTE1XcnhPb2JWOFN5RDhNT0hRRGJoMGRWUUM5N2hyYXBTaW5jRWJMNHQtY2ktallCSk1fTV8yMGhpZzUwT0hUZERYTUxNUjY4VjNjVnZrZWY4WVEyUWJscHJuQXhSakVROVkxdTVzSVRqUUxhQ29iV1c0endwekdJT3duczFFVWZXMV9EUy1fVVZ1REY2UnhnRFNvRm0xUVBMaWVpUmg0cHozQkhCdDIzODlBenNMN0t1YjVjY2FQcmc
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 23:36:01 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiuAFBVV95cUxNYnM2bGgybFJfSjNZMXhnOW4wckFDLVFVOGxSVi0tTWhvVm9KTHNrbEY1eERRQ0h4V1N1NDVENUx1SW1vc28xS0Jubi1tdUVGU1BucEI5cXdZTmdNcFhZTDJnSGZQSXhYNXgtNV9JT0JSaFZSZ0RYeUdQaERrOFFXQTVoMzRLeVpLYTF6TFlvdUZrM0UyQ2xjM29TNDM3SEhfczI2cC1Fa2RRWUNBWEtDVjBBb2ZxWDFr0gG-AUFVX3lxTE1XcnhPb2JWOFN5RDhNT0hRRGJoMGRWUUM5N2hyYXBTaW5jRWJMNHQtY2ktallCSk1fTV8yMGhpZzUwT0hUZERYTUxNUjY4VjNjVnZrZWY4WVEyUWJscHJuQXhSakVROVkxdTVzSVRqUUxhQ29iV1c0endwekdJT3duczFFVWZXMV9EUy1fVVZ1REY2UnhnRFNvRm0xUVBMaWVpUmg0cHozQkhCdDIzODlBenNMN0t1YjVjY2FQcmc?oc=5" target="_blank">Japan ruling party seeks AI penalties over deepfakes, piracy</a>&nbsp;&nbsp;<font color="#6f6f6f">upi.com</font>

## 157. New Conversational AI Tool Uses Trusted Medical Protocols to Help People Decide When to Seek Care | Newswise - Newswise
- Domain: newswise.com
- URL: https://news.google.com/rss/articles/CBMiywFBVV95cUxQVU1GaU9icWNZRE01QWNPUVRaWjVvNlhTV2taTjJ5V1RYa1BwdENWOGdZTjREajZPMTZLN0gwcXowSWJtdVpmUkhVNE5NLW1QVjBMZ3N5emh4bnM1RW84TktkcERMMlNHX3UzVDFWM1AyZ3ZSMkYtRmxUYWNhVnoySHhXeHcybjByQnN1X0lKS0lScG81N1JNZjhjNXp4ejEtMC1DMjdYWlNBR3ZwR1ROejBkOTZCV0JFcVZMUW96bGRhakNFcW5GMUFKNNIBywFBVV95cUxQVU1GaU9icWNZRE01QWNPUVRaWjVvNlhTV2taTjJ5V1RYa1BwdENWOGdZTjREajZPMTZLN0gwcXowSWJtdVpmUkhVNE5NLW1QVjBMZ3N5emh4bnM1RW84TktkcERMMlNHX3UzVDFWM1AyZ3ZSMkYtRmxUYWNhVnoySHhXeHcybjByQnN1X0lKS0lScG81N1JNZjhjNXp4ejEtMC1DMjdYWlNBR3ZwR1ROejBkOTZCV0JFcVZMUW96bGRhakNFcW5GMUFKNA
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 23:20:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiywFBVV95cUxQVU1GaU9icWNZRE01QWNPUVRaWjVvNlhTV2taTjJ5V1RYa1BwdENWOGdZTjREajZPMTZLN0gwcXowSWJtdVpmUkhVNE5NLW1QVjBMZ3N5emh4bnM1RW84TktkcERMMlNHX3UzVDFWM1AyZ3ZSMkYtRmxUYWNhVnoySHhXeHcybjByQnN1X0lKS0lScG81N1JNZjhjNXp4ejEtMC1DMjdYWlNBR3ZwR1ROejBkOTZCV0JFcVZMUW96bGRhakNFcW5GMUFKNNIBywFBVV95cUxQVU1GaU9icWNZRE01QWNPUVRaWjVvNlhTV2taTjJ5V1RYa1BwdENWOGdZTjREajZPMTZLN0gwcXowSWJtdVpmUkhVNE5NLW1QVjBMZ3N5emh4bnM1RW84TktkcERMMlNHX3UzVDFWM1AyZ3ZSMkYtRmxUYWNhVnoySHhXeHcybjByQnN1X0lKS0lScG81N1JNZjhjNXp4ejEtMC1DMjdYWlNBR3ZwR1ROejBkOTZCV0JFcVZMUW96bGRhakNFcW5GMUFKNA?oc=5" target="_blank">New Conversational AI Tool Uses Trusted Medical Protocols to Help People Decide When to Seek Care | Newswise</a>&nbsp;&nbsp;<font color="#6f6f6f">Newswise</font>

## 158. Meta says it will cut 8,000 jobs as AI spending soars - BBC
- Domain: bbc.com
- URL: https://news.google.com/rss/articles/CBMiWkFVX3lxTFBkSlFjci1vSDY4V1RtRlk4OWNmN09IdDg2bU95RmluaE05V0gwY3lqcE05QmkyUVYxMTYyS1RwQkRLSW9fVlRJMUFwTlctV293M2lTemVrZmFodw
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 22:56:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTFBkSlFjci1vSDY4V1RtRlk4OWNmN09IdDg2bU95RmluaE05V0gwY3lqcE05QmkyUVYxMTYyS1RwQkRLSW9fVlRJMUFwTlctV293M2lTemVrZmFodw?oc=5" target="_blank">Meta says it will cut 8,000 jobs as AI spending soars</a>&nbsp;&nbsp;<font color="#6f6f6f">BBC</font>

## 159. Pépite chinoise de l'IA, DeepSeek lance un nouveau modèle - TradingView
- Domain: fr.tradingview.com
- URL: https://news.google.com/rss/articles/CBMiYkFVX3lxTE00TDZnWllRY3lxWDZraGo0RlFiUVY4WVRlQ1FNeGNoaGpwamZxNzJ3cnhKNEVjU3FjUlVhYUtaTmR4eS1PR0JleHpES0NTMGg5cFp2bk5VZjA0bDliZENqSG9R
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 22:25:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE00TDZnWllRY3lxWDZraGo0RlFiUVY4WVRlQ1FNeGNoaGpwamZxNzJ3cnhKNEVjU3FjUlVhYUtaTmR4eS1PR0JleHpES0NTMGg5cFp2bk5VZjA0bDliZENqSG9R?oc=5" target="_blank">Pépite chinoise de l'IA, DeepSeek lance un nouveau modèle</a>&nbsp;&nbsp;<font color="#6f6f6f">TradingView</font>

## 160. AI: Our greatest ally or our most formidable challenge? - Independent Catholic News
- Domain: indcatholicnews.com
- URL: https://news.google.com/rss/articles/CBMiVEFVX3lxTE02dl9JNm1VM1hEZXI4YVpYVVZXSm00SXh2WEhIRXd3WERXME1SU3ZBUmxiVGRTNjNMRHJobE5mUWItXzg1TVZFTFUtSUNMR0Y4c0tDZg
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 21:56:51 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTE02dl9JNm1VM1hEZXI4YVpYVVZXSm00SXh2WEhIRXd3WERXME1SU3ZBUmxiVGRTNjNMRHJobE5mUWItXzg1TVZFTFUtSUNMR0Y4c0tDZg?oc=5" target="_blank">AI: Our greatest ally or our most formidable challenge?</a>&nbsp;&nbsp;<font color="#6f6f6f">Independent Catholic News</font>

## 161. Lawyers should disclose when AI causes errors, appeals court says - Reuters
- Domain: reuters.com
- URL: https://news.google.com/rss/articles/CBMiuAFBVV95cUxPY2xrOGNFVDd5S0wxWTkxSVdHa3QzUEVxZE9sa2ViVmlKSGx4cnJrSVRqZGVSOWt2WFJLeHoxY2w1dG5tTG16TndJa3duZVk0YXdhX2hjTnBzMzR0clhIaDhIRjB2QTA1VG1pODNRbzltMjdWOWFicUhROG5LanFXZFlrMTBwNnN0bVlQcFpwRVF5V3NveXdRVGMtUEVJV3NmUnJWbXBYZDVHZG5wXzVwT0tpX1doLUhJ
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 20:49:25 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiuAFBVV95cUxPY2xrOGNFVDd5S0wxWTkxSVdHa3QzUEVxZE9sa2ViVmlKSGx4cnJrSVRqZGVSOWt2WFJLeHoxY2w1dG5tTG16TndJa3duZVk0YXdhX2hjTnBzMzR0clhIaDhIRjB2QTA1VG1pODNRbzltMjdWOWFicUhROG5LanFXZFlrMTBwNnN0bVlQcFpwRVF5V3NveXdRVGMtUEVJV3NmUnJWbXBYZDVHZG5wXzVwT0tpX1doLUhJ?oc=5" target="_blank">Lawyers should disclose when AI causes errors, appeals court says</a>&nbsp;&nbsp;<font color="#6f6f6f">Reuters</font>

## 162. La Maison Blanche accuse la Chine de copier les intelligences artificielles américaines clandestinement et à grande échelle - franceinfo
- Domain: franceinfo.fr
- URL: https://news.google.com/rss/articles/CBMiowJBVV95cUxQN05fSWFCWElnekhCZ1RQMFFvQmxJV2hoRHIwMk44b2htbldJSl91NkxKdFhVR29qaUZDZjMxQ25tMHp3RUxrMmVXbDB2TGJiWUhiWktRaEhEVU9odENhRUZyd05VaWFadzJVLWZmOVhIVFJIcF9ySHFGelBRN3MwZU1KT3FLZUxvdV9YQjJUcmdjWDJodEd3SUI3S05HMnpnd3QteFRJNVlsQ3p2dzNZSnNtMm9FLWJPSEw4Z1VXdWxZTkRTbVRHZEJfYndVdHFacTNYaUhkYzZZZDVWWWJ3dG1MSExheTVGRTRsMnl3b3FxNnhSOThSTVBIcVd3ejlJOGdXTGhIS0VPNWxsT3VnajV5a3NRc2RJcUExTFR2dmx3bk0
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 20:46:54 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiowJBVV95cUxQN05fSWFCWElnekhCZ1RQMFFvQmxJV2hoRHIwMk44b2htbldJSl91NkxKdFhVR29qaUZDZjMxQ25tMHp3RUxrMmVXbDB2TGJiWUhiWktRaEhEVU9odENhRUZyd05VaWFadzJVLWZmOVhIVFJIcF9ySHFGelBRN3MwZU1KT3FLZUxvdV9YQjJUcmdjWDJodEd3SUI3S05HMnpnd3QteFRJNVlsQ3p2dzNZSnNtMm9FLWJPSEw4Z1VXdWxZTkRTbVRHZEJfYndVdHFacTNYaUhkYzZZZDVWWWJ3dG1MSExheTVGRTRsMnl3b3FxNnhSOThSTVBIcVd3ejlJOGdXTGhIS0VPNWxsT3VnajV5a3NRc2RJcUExTFR2dmx3bk0?oc=5" target="_blank">La Maison Blanche accuse la Chine de copier les intelligences artificielles américaines clandestinement et à grande échelle</a>&nbsp;&nbsp;<font color="#6f6f6f">franceinfo</font>

## 163. Washington accuse la Chine de vols massifs de technologies d’IA américaines - Ouest-France
- Domain: ouest-france.fr
- URL: https://news.google.com/rss/articles/CBMihgJBVV95cUxOclB1Y3RsNUUxa2ROenlUc3A0c3ZNRG9POEFnZHNQTXkzNGEyM1V0SWNkZHNtcDhVVThMdW9vVXFSTXlpdThZRUg4dHVvMDdEV3JuM1A3c0VOdDE0VzljSnY1Rndrdk1EMTVzaW16LWNpc19RVHBHVHRuRGFSRGJZclRQTWQtbmtrVTlrLXBqYlNtMnhkQzJyQXRCUlJZTXh5ZEhpd0dwTmE1dXcwbmg4Y3RaYkZKSGZ4ZDBSS1RCQ3haOTdIOURwMGdxSjNJLXNWelRzNi1WbzVhN2dUc3d5ZW1tN0ZaOHUwaVUyRHN1RHZNcU8tOF9CYUlvTnBPMks5ZzZuODRn
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 20:30:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMihgJBVV95cUxOclB1Y3RsNUUxa2ROenlUc3A0c3ZNRG9POEFnZHNQTXkzNGEyM1V0SWNkZHNtcDhVVThMdW9vVXFSTXlpdThZRUg4dHVvMDdEV3JuM1A3c0VOdDE0VzljSnY1Rndrdk1EMTVzaW16LWNpc19RVHBHVHRuRGFSRGJZclRQTWQtbmtrVTlrLXBqYlNtMnhkQzJyQXRCUlJZTXh5ZEhpd0dwTmE1dXcwbmg4Y3RaYkZKSGZ4ZDBSS1RCQ3haOTdIOURwMGdxSjNJLXNWelRzNi1WbzVhN2dUc3d5ZW1tN0ZaOHUwaVUyRHN1RHZNcU8tOF9CYUlvTnBPMks5ZzZuODRn?oc=5" target="_blank">Washington accuse la Chine de vols massifs de technologies d’IA américaines</a>&nbsp;&nbsp;<font color="#6f6f6f">Ouest-France</font>

## 164. Blame the Pentagon, Not AI, for Preventable Targeting Mistakes - Lawfare
- Domain: lawfaremedia.org
- URL: https://news.google.com/rss/articles/CBMioAFBVV95cUxPcmc0MHdVbElsUU9nZ3M5X2FQa3M3bGtlRWlZbzRza09uTnR2QVljbGNfbnNnM3FEeUJhNFhpVUp0Tk42OFhndkM2NGdZREJFbWpJNHQ2NVBYcFdzc2JBOFFaZkIwcXNHUTVhbnVxSlM2TkxTZFNJTVpWc05iX2VxbE1mSkRUZjdnQW1IR0pXQ0pfZkxWamNZU2xHd2F0OFVz
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 20:27:22 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMioAFBVV95cUxPcmc0MHdVbElsUU9nZ3M5X2FQa3M3bGtlRWlZbzRza09uTnR2QVljbGNfbnNnM3FEeUJhNFhpVUp0Tk42OFhndkM2NGdZREJFbWpJNHQ2NVBYcFdzc2JBOFFaZkIwcXNHUTVhbnVxSlM2TkxTZFNJTVpWc05iX2VxbE1mSkRUZjdnQW1IR0pXQ0pfZkxWamNZU2xHd2F0OFVz?oc=5" target="_blank">Blame the Pentagon, Not AI, for Preventable Targeting Mistakes</a>&nbsp;&nbsp;<font color="#6f6f6f">Lawfare</font>

## 165. Is AI a Fantastic Tool? The End of the World? Both? (VIDEO) - Plugged In
- Domain: pluggedin.com
- URL: https://news.google.com/rss/articles/CBMijwFBVV95cUxPb3NKQXZidDFkRGN1YXFOU2pOeWNDMEl2anBXbFVxVmpXajBUUnlGY0ZmX21RTERiTUZnVXcxcEtVVmRjY05FdGxUQVVudkZRY2t0ZHVHMFZZTGt2dzFfVmNNbEcyTXBuUDlPbVpGNjhMdVktWUxjaFBPR2ItQUxMSkRQbWs2M3VIQUJWc2RaUQ
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 20:14:20 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMijwFBVV95cUxPb3NKQXZidDFkRGN1YXFOU2pOeWNDMEl2anBXbFVxVmpXajBUUnlGY0ZmX21RTERiTUZnVXcxcEtVVmRjY05FdGxUQVVudkZRY2t0ZHVHMFZZTGt2dzFfVmNNbEcyTXBuUDlPbVpGNjhMdVktWUxjaFBPR2ItQUxMSkRQbWs2M3VIQUJWc2RaUQ?oc=5" target="_blank">Is AI a Fantastic Tool? The End of the World? Both? (VIDEO)</a>&nbsp;&nbsp;<font color="#6f6f6f">Plugged In</font>

## 166. Little Rock adopts citywide AI policy with new oversight committee, Mayor Scott says - KATV
- Domain: katv.com
- URL: https://news.google.com/rss/articles/CBMisAFBVV95cUxNZTdoS213ZUstY3hpS1Rka25sdXl4SEtmSVQ0WFluVG56aDd5c2JlWXQzWmtOZXJveGFlcncwc1hoWEJiR3FGN3dwZEFMbC1iRUFCZURaa0FrMW1tX0VDbDB4Q1BQS0pGYjNmN1hQUGxNVE9lREpyN3hIWXNfXzJOb1c2TDRRLXFnRW9BRVRZcHl0WWpYMVJkdVFMQVBKb3JMbE80c3JDWlZzTDNSbHNmMg
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 20:03:09 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMisAFBVV95cUxNZTdoS213ZUstY3hpS1Rka25sdXl4SEtmSVQ0WFluVG56aDd5c2JlWXQzWmtOZXJveGFlcncwc1hoWEJiR3FGN3dwZEFMbC1iRUFCZURaa0FrMW1tX0VDbDB4Q1BQS0pGYjNmN1hQUGxNVE9lREpyN3hIWXNfXzJOb1c2TDRRLXFnRW9BRVRZcHl0WWpYMVJkdVFMQVBKb3JMbE80c3JDWlZzTDNSbHNmMg?oc=5" target="_blank">Little Rock adopts citywide AI policy with new oversight committee, Mayor Scott says</a>&nbsp;&nbsp;<font color="#6f6f6f">KATV</font>

## 167. DC Edit | Govt Rules To Regulate AI Welcome - Deccan Chronicle
- Domain: deccanchronicle.com
- URL: https://news.google.com/rss/articles/CBMiogFBVV95cUxPVkVfMmpOSktZRjRzT25SZXBuZGx5V1JGTGdhQThzNDh2cjVMZVA0UXlZNi1meU1vSzFiaFdxdV9yTzZNemxwc1BxNHQzSHRCLUR3X3RTanV2aWZscGpfM0ZqVWd3V09TRnJYeDFlZWNhNnpYYmM5NzRVZXZqTzh3LVBvS2ZDYjRxU1BaemxQZXNmLVhZNmNlcWJXaWExdDVRTVHSAacBQVVfeXFMTkxQYlNFZEpsLW9zTnY3cmhjLVlXNzhYSWxFTHNFcFdIeHl3QWRNMnVQX2NZRXVnWnZacENLNERJYTlQeDVjRHEwWVhiZ29BdHZIR1N1MXNPUkw4dmRxMkFIcXRicXhPTWdvYkVSenFWSzM1bU1JTjd4Z3hvTDF3aUZzVThsUmNnQzh6dzh0LWs1QVR3WmhVcW4tTEFLSjBDVVpnTDR5YWs
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 19:46:31 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxPVkVfMmpOSktZRjRzT25SZXBuZGx5V1JGTGdhQThzNDh2cjVMZVA0UXlZNi1meU1vSzFiaFdxdV9yTzZNemxwc1BxNHQzSHRCLUR3X3RTanV2aWZscGpfM0ZqVWd3V09TRnJYeDFlZWNhNnpYYmM5NzRVZXZqTzh3LVBvS2ZDYjRxU1BaemxQZXNmLVhZNmNlcWJXaWExdDVRTVHSAacBQVVfeXFMTkxQYlNFZEpsLW9zTnY3cmhjLVlXNzhYSWxFTHNFcFdIeHl3QWRNMnVQX2NZRXVnWnZacENLNERJYTlQeDVjRHEwWVhiZ29BdHZIR1N1MXNPUkw4dmRxMkFIcXRicXhPTWdvYkVSenFWSzM1bU1JTjd4Z3hvTDF3aUZzVThsUmNnQzh6dzh0LWs1QVR3WmhVcW4tTEFLSjBDVVpnTDR5YWs?oc=5" target="_blank">DC Edit | Govt Rules To Regulate AI Welcome</a>&nbsp;&nbsp;<font color="#6f6f6f">Deccan Chronicle</font>

## 168. Feature: German bookstores find strength in culture, community to navigate AI era - Xinhua
- Domain: english.news.cn
- URL: https://news.google.com/rss/articles/CBMihgFBVV95cUxQVnY4M1hSR3BxbFFSYVVWMUstdGJzWk9OUVU2Z2ZlVGVhUzJibFQybk42TFE0VFF6NU5WX2hWcy1fMUtrUFlHS0FLMC1Dam41M0ZwNXJ0MmVOeUIxWDhMYk5fblhCc25DVm42UnFSdURCQVFMM0lsTGtjTXN1T19hS183bFdvUQ
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 19:41:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMihgFBVV95cUxQVnY4M1hSR3BxbFFSYVVWMUstdGJzWk9OUVU2Z2ZlVGVhUzJibFQybk42TFE0VFF6NU5WX2hWcy1fMUtrUFlHS0FLMC1Dam41M0ZwNXJ0MmVOeUIxWDhMYk5fblhCc25DVm42UnFSdURCQVFMM0lsTGtjTXN1T19hS183bFdvUQ?oc=5" target="_blank">Feature: German bookstores find strength in culture, community to navigate AI era</a>&nbsp;&nbsp;<font color="#6f6f6f">Xinhua</font>

## 169. Le Tech Flash : Tesla porte ses paris sur l'IA à 25 milliards de dollars, par Léa Benaim - 23/04 - BFM
- Domain: bfmtv.com
- URL: https://news.google.com/rss/articles/CBMiigJBVV95cUxNNXZGX0hKZGp2a201Q29xM3k2YVBHS3FqbEUyYk9mUlFjdF9jSF9HNjhMb1A3Q2t3a05rX00taTItTmZFcThUX3hvSnZIZ3VHVWEwNUt5SFNxM3JvXzJfU0lCT19ka1J3OVNlLUVYVFJKcEJvaU5GWDQzSWFNMVFpODdwOHM0ZHplb0EzUXJoemNtWWx2NHZ1N29xWmR5T0pzQ2twQWtCVEloNkdzdHp6OWlSZExCN0RTeGhMOWVXVmpSQWFPWWd3dGc5cE9ZQWZheXUzSzAyZU9Fa0ZhS1lKMFlSZ29wVHc1QTZSTVhEN2hhYm0zWUJwUDlqVDZ4WGh1blRiMkFVRk9iZw
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 19:13:21 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiigJBVV95cUxNNXZGX0hKZGp2a201Q29xM3k2YVBHS3FqbEUyYk9mUlFjdF9jSF9HNjhMb1A3Q2t3a05rX00taTItTmZFcThUX3hvSnZIZ3VHVWEwNUt5SFNxM3JvXzJfU0lCT19ka1J3OVNlLUVYVFJKcEJvaU5GWDQzSWFNMVFpODdwOHM0ZHplb0EzUXJoemNtWWx2NHZ1N29xWmR5T0pzQ2twQWtCVEloNkdzdHp6OWlSZExCN0RTeGhMOWVXVmpSQWFPWWd3dGc5cE9ZQWZheXUzSzAyZU9Fa0ZhS1lKMFlSZ29wVHc1QTZSTVhEN2hhYm0zWUJwUDlqVDZ4WGh1blRiMkFVRk9iZw?oc=5" target="_blank">Le Tech Flash : Tesla porte ses paris sur l'IA à 25 milliards de dollars, par Léa Benaim - 23/04</a>&nbsp;&nbsp;<font color="#6f6f6f">BFM</font>

## 170. Claude Mythos : le modèle d’IA le plus dangereux jamais créé ? - Futura, le média qui explore le monde
- Domain: futura-sciences.com
- URL: https://news.google.com/rss/articles/CBMizAFBVV95cUxOZDZTM3ZDTlRUUm8taEVlX2NIN3BZeWJrWXAyOHlyc1Vla3BBNVNtNjVZMi1fRHpuYmI0TEhHVS1QcUxSX1hyb2xWd24tV1c0SlRSenl2WGc2MkNzRnNodGJva3NERUg1M2dQaE9yV0VvaVVwenBrUFc1eWZzbk1Jc3RnWHE2OHRBaDNzNG0yOU53eVhGVWtkUmhPckJzUVhZLVU0RUZvdFBiRmFDVXFCODNzVlBMMjVSNERsb0hLT3VyeG12Q3ZnWWE5eG4
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 19:07:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMizAFBVV95cUxOZDZTM3ZDTlRUUm8taEVlX2NIN3BZeWJrWXAyOHlyc1Vla3BBNVNtNjVZMi1fRHpuYmI0TEhHVS1QcUxSX1hyb2xWd24tV1c0SlRSenl2WGc2MkNzRnNodGJva3NERUg1M2dQaE9yV0VvaVVwenBrUFc1eWZzbk1Jc3RnWHE2OHRBaDNzNG0yOU53eVhGVWtkUmhPckJzUVhZLVU0RUZvdFBiRmFDVXFCODNzVlBMMjVSNERsb0hLT3VyeG12Q3ZnWWE5eG4?oc=5" target="_blank">Claude Mythos : le modèle d’IA le plus dangereux jamais créé ?</a>&nbsp;&nbsp;<font color="#6f6f6f">Futura, le média qui explore le monde</font>

## 171. When AI Learns How the World Works - Goldman Sachs
- Domain: goldmansachs.com
- URL: https://news.google.com/rss/articles/CBMiiAFBVV95cUxOWmxvSFNLNTZrQjd3SWZJN0NxRUhSN1RBcmFMdWtaOXJ2V2pDUDZVNW9uWDg3SEdSbHJsYmVrX2tUb0hTdW5rT3QyMHlROENvX3pfUGk4VjFxUjE3eWhaMldZTjh1RFE1TUJVMV96amd5b2RrbkR5elBxUzBfUWlGbWhmc3RodWFw
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 19:01:04 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiiAFBVV95cUxOWmxvSFNLNTZrQjd3SWZJN0NxRUhSN1RBcmFMdWtaOXJ2V2pDUDZVNW9uWDg3SEdSbHJsYmVrX2tUb0hTdW5rT3QyMHlROENvX3pfUGk4VjFxUjE3eWhaMldZTjh1RFE1TUJVMV96amd5b2RrbkR5elBxUzBfUWlGbWhmc3RodWFw?oc=5" target="_blank">When AI Learns How the World Works</a>&nbsp;&nbsp;<font color="#6f6f6f">Goldman Sachs</font>

## 172. Thailand intensifies AI efforts in bid to close the skills gap - Bangkok Post
- Domain: bangkokpost.com
- URL: https://news.google.com/rss/articles/CBMitgFBVV95cUxPQVZWd0EzUVVEVHN1MEtiU0g5VlEyb19zaDJqdDFXb1B6ak9CeEExd3B4VTVob2hSeWpSdjRENTRSRjBGb1NINjRmd0FfdmktSXk0dDZJZkNvWUlZNlBHSXBXc3I4UUN5QmdxaDRVREpIOHB5ajFHTjdSZUk4QkZvc1pNTm1zT0NMRWJaeTg4M2NxaXZlZzBGNTgzdVN4RHhGalNqQ3Q5RzhYcld2Rk1jTlZfLVFUZw
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 18:01:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMitgFBVV95cUxPQVZWd0EzUVVEVHN1MEtiU0g5VlEyb19zaDJqdDFXb1B6ak9CeEExd3B4VTVob2hSeWpSdjRENTRSRjBGb1NINjRmd0FfdmktSXk0dDZJZkNvWUlZNlBHSXBXc3I4UUN5QmdxaDRVREpIOHB5ajFHTjdSZUk4QkZvc1pNTm1zT0NMRWJaeTg4M2NxaXZlZzBGNTgzdVN4RHhGalNqQ3Q5RzhYcld2Rk1jTlZfLVFUZw?oc=5" target="_blank">Thailand intensifies AI efforts in bid to close the skills gap</a>&nbsp;&nbsp;<font color="#6f6f6f">Bangkok Post</font>

## 173. Meta will cut 10% of workforce as company pushes deeper into AI - CNBC
- Domain: cnbc.com
- URL: https://news.google.com/rss/articles/CBMioAFBVV95cUxNWHNGbEZGWnZFVWhPZjFRbXFCeFpnV2FkY1VsUmgxbGZOQldqRnhCUFQwNEtab24yRTlPYkxFNmtYYnJpaWx4NkZfWkpJY3hRc1dsZTRwX0VjSFN0MnVlY3hSRGpKc3B6dzhxaW84ZFlvT2d1b1U0eDJNaFc3V3N5RXlxQUxjZEtsS3dUSHpfUjcwdFVGOTFzb2pUejg1U3dy0gGmAUFVX3lxTFBMai1HczNjYzFVbUEyY3Jrb3c2MkNjazd1dEFCbzk3OHE0Ykg4ZDVhNThGcG55TzRoaU9YOF9SVEtObzBVampsdmdaZnJzM05lMHZlTWVSczZGWENRZDdZR0FudzNmTmd5cGE3ekRELVN5eTZRbHY1NEYteEpFZmR1RHUzM0VOdUV1am1teW43OEdGM0lRY0Vub3plcVBoWUJfNVZqVGc
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 18:00:18 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMioAFBVV95cUxNWHNGbEZGWnZFVWhPZjFRbXFCeFpnV2FkY1VsUmgxbGZOQldqRnhCUFQwNEtab24yRTlPYkxFNmtYYnJpaWx4NkZfWkpJY3hRc1dsZTRwX0VjSFN0MnVlY3hSRGpKc3B6dzhxaW84ZFlvT2d1b1U0eDJNaFc3V3N5RXlxQUxjZEtsS3dUSHpfUjcwdFVGOTFzb2pUejg1U3dy0gGmAUFVX3lxTFBMai1HczNjYzFVbUEyY3Jrb3c2MkNjazd1dEFCbzk3OHE0Ykg4ZDVhNThGcG55TzRoaU9YOF9SVEtObzBVampsdmdaZnJzM05lMHZlTWVSczZGWENRZDdZR0FudzNmTmd5cGE3ekRELVN5eTZRbHY1NEYteEpFZmR1RHUzM0VOdUV1am1teW43OEdGM0lRY0Vub3plcVBoWUJfNVZqVGc?oc=5" target="_blank">Meta will cut 10% of workforce as company pushes deeper into AI</a>&nbsp;&nbsp;<font color="#6f6f6f">CNBC</font>

## 174. PARIS : Qualité de Vie au Travail - Une intelligence artificielle pour guider les décisions des DRH - Presse Agence
- Domain: presseagence.fr
- URL: https://news.google.com/rss/articles/CBMivAFBVV95cUxONGZyaGczR1FZTkdkVmRpTU8yNDRtaWxwcTliQlpuMzY2cmJsS09OQnFxZ1BKTkhvY3VtUTc2MUxNdjIzWGZYazhZWEVvNG5ISWYyQ2M5eDBlUXlNNno0TDlFUUR0YXNsb3VZS2Y2TW5VaG5OMlFndnNYdE9jUjRiUDJ2eGdNV0J3NjJJMnJrZHJTd3AtdTVNT0hvTWpUSmxaUUJxNjJ5Z19WMGJxdWdEMkw4bWdLS1ZlN0FKUQ
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 18:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMivAFBVV95cUxONGZyaGczR1FZTkdkVmRpTU8yNDRtaWxwcTliQlpuMzY2cmJsS09OQnFxZ1BKTkhvY3VtUTc2MUxNdjIzWGZYazhZWEVvNG5ISWYyQ2M5eDBlUXlNNno0TDlFUUR0YXNsb3VZS2Y2TW5VaG5OMlFndnNYdE9jUjRiUDJ2eGdNV0J3NjJJMnJrZHJTd3AtdTVNT0hvTWpUSmxaUUJxNjJ5Z19WMGJxdWdEMkw4bWdLS1ZlN0FKUQ?oc=5" target="_blank">PARIS : Qualité de Vie au Travail - Une intelligence artificielle pour guider les décisions des DRH</a>&nbsp;&nbsp;<font color="#6f6f6f">Presse Agence</font>

## 175. HrFlow.ai Raises $7M Pre-Series A for HR AI Platform - ACCESS Newswire
- Domain: accessnewswire.com
- URL: https://news.google.com/rss/articles/CBMi6wFBVV95cUxNTXlETzRsMWRPdDFoY293UzZGcGlxY01FQUs1ZTFIMVF0cmNPcTd0MS1EQjZPSnQ4OHh2czJlR2NvQklqempoeUp1QmV2bTV6ZXBlVFpsc3JVWEZJa3Y0OXVVTzhnYm5BdUZ5TklIS0liaDM1R2ZzV0RRVWR1YkVMZXlRTDN5TTZvU2NmbWZ3TEp0a013RXZuNm5vMjVJYkdwb1l4akNxLWxHeWt3YnRxbkpCb0w0T25rUXc0b2ZtVVQ0cjdSS2FWNmJFUVpvVFVlVGIyeEVYQlpwbVM1QmNlWENsZHlrNDE2c2o0
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 17:40:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi6wFBVV95cUxNTXlETzRsMWRPdDFoY293UzZGcGlxY01FQUs1ZTFIMVF0cmNPcTd0MS1EQjZPSnQ4OHh2czJlR2NvQklqempoeUp1QmV2bTV6ZXBlVFpsc3JVWEZJa3Y0OXVVTzhnYm5BdUZ5TklIS0liaDM1R2ZzV0RRVWR1YkVMZXlRTDN5TTZvU2NmbWZ3TEp0a013RXZuNm5vMjVJYkdwb1l4akNxLWxHeWt3YnRxbkpCb0w0T25rUXc0b2ZtVVQ0cjdSS2FWNmJFUVpvVFVlVGIyeEVYQlpwbVM1QmNlWENsZHlrNDE2c2o0?oc=5" target="_blank">HrFlow.ai Raises $7M Pre-Series A for HR AI Platform</a>&nbsp;&nbsp;<font color="#6f6f6f">ACCESS Newswire</font>

## 176. Mill joins Google's AI Futures Fund to advance food waste technology - Waste Today -
- Domain: wastetodaymagazine.com
- URL: https://news.google.com/rss/articles/CBMiqAFBVV95cUxPMWR3clhNQzZkSHcwZU51NFZXNU9nN2NPYUtzZE91TUFkRkhTbDBIV1RWNnVFd2FVWlMyM3BoMTB4Qm1PbERGZ0hhVjNJN3psNUpiT3pXRG44ZGRvcTNTLU5PQWcyVXJQcjd0MjBGZTVMMEMwdW4yZDRkWjFua09hS1FWcGF6cXRuZnMtM2xRZ0VaUnFobHM1a0ZuRG1tdWUta1I2Q25EaGg
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 17:25:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiqAFBVV95cUxPMWR3clhNQzZkSHcwZU51NFZXNU9nN2NPYUtzZE91TUFkRkhTbDBIV1RWNnVFd2FVWlMyM3BoMTB4Qm1PbERGZ0hhVjNJN3psNUpiT3pXRG44ZGRvcTNTLU5PQWcyVXJQcjd0MjBGZTVMMEMwdW4yZDRkWjFua09hS1FWcGF6cXRuZnMtM2xRZ0VaUnFobHM1a0ZuRG1tdWUta1I2Q25EaGg?oc=5" target="_blank">Mill joins Google's AI Futures Fund to advance food waste technology</a>&nbsp;&nbsp;<font color="#6f6f6f">Waste Today -</font>

## 177. L’étude choc du syndicat CFE-CGC de l’assurance révèle une pratique généralisée de l’IA, mais un manque de formation des salariés - L'Argus de l'assurance
- Domain: argusdelassurance.com
- URL: https://news.google.com/rss/articles/CBMixAJBVV95cUxOS2dwYWNTX21YcFpVUHpsVHdmQzU2aG9HcHF2QkVMazk5ZHJNTUhTWjBhRGNRMWRLc3VkSHBES3VVZ2NwWjlodDF6Z1FkSUUxWEp2U2Fma1Bkb0t2NW5DOXhmUTc2dWx2Mk1sRHh3TmVCU0liRnV1U1dQcXQ3SW9ZbzEtMVEtaXduVUdoeUlCS1E1ekxPZzlxeExWbld3ODhzenRFd21Ici0wM21tUFFTN1J3aHRzTkZCaHRKdF9zUDFmS0taUTE0djFCempVZnFNVmZ4bml3NXgtQW1fRFRrZ2JycDJLYWk5UDMwTU9YQUpldjYybUpYYjBzellNNzQ0anlIQXB5VHBhLXhYZEtpbEFyaEltTkRXVS1QV2RRUXJsbEE2d3lHSVByd0JYd2lDS0MyMkJHcEhKWXRvVHh6TWkxNTM
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 16:59:29 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMixAJBVV95cUxOS2dwYWNTX21YcFpVUHpsVHdmQzU2aG9HcHF2QkVMazk5ZHJNTUhTWjBhRGNRMWRLc3VkSHBES3VVZ2NwWjlodDF6Z1FkSUUxWEp2U2Fma1Bkb0t2NW5DOXhmUTc2dWx2Mk1sRHh3TmVCU0liRnV1U1dQcXQ3SW9ZbzEtMVEtaXduVUdoeUlCS1E1ekxPZzlxeExWbld3ODhzenRFd21Ici0wM21tUFFTN1J3aHRzTkZCaHRKdF9zUDFmS0taUTE0djFCempVZnFNVmZ4bml3NXgtQW1fRFRrZ2JycDJLYWk5UDMwTU9YQUpldjYybUpYYjBzellNNzQ0anlIQXB5VHBhLXhYZEtpbEFyaEltTkRXVS1QV2RRUXJsbEE2d3lHSVByd0JYd2lDS0MyMkJHcEhKWXRvVHh6TWkxNTM?oc=5" target="_blank">L’étude choc du syndicat CFE-CGC de l’assurance révèle une pratique généralisée de l’IA, mais un manque de formation des salariés</a>&nbsp;&nbsp;<font color="#6f6f6f">L'Argus de l'assurance</font>

## 178. AI automates quantum dot voltage tuning: toward scaling up quantum computing - EurekAlert!
- Domain: eurekalert.org
- URL: https://news.google.com/rss/articles/CBMiXEFVX3lxTE1hTEYzQlMwVUFtWEM3UkY3blBQXzJGbEcxbVEwdEdnWXgyeXJzTnR3UzRaeDZBNlNjZ0tXSHcwWG1hV1J0cFZEYmhMY3M4M0dLckhhb215b2pYM3Rw
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 16:17:01 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTE1hTEYzQlMwVUFtWEM3UkY3blBQXzJGbEcxbVEwdEdnWXgyeXJzTnR3UzRaeDZBNlNjZ0tXSHcwWG1hV1J0cFZEYmhMY3M4M0dLckhhb215b2pYM3Rw?oc=5" target="_blank">AI automates quantum dot voltage tuning: toward scaling up quantum computing</a>&nbsp;&nbsp;<font color="#6f6f6f">EurekAlert!</font>

## 179. "J’ai été choquée, car j’ai cru que c’était moi" : une influenceuse française découvre son image détournée par l’IA pour promouvoir un produit qu’elle ne connaît pas - ladepeche.fr
- Domain: ladepeche.fr
- URL: https://news.google.com/rss/articles/CBMinAJBVV95cUxQcEtBV1A1UVBQa0RCeHlRaDdBcDcxakpBZEwxc04zUy1BVDlYYWV4SnJMdHVQZTNXR0w3alNmWUVNRHpfRzNnYXNHTWNxTVdseThIWVRNczhOSS1NaFlMd2lPWHhlWDd3MEJoV0g2OHFteXNQRWxsNGs5UW1uYmNDRVVkWTVXakNPSms2S0xBeVZRbE8zSWFNT0FMcDR3VEx5aXdpcFdOZWVIVk0xbHY0NWtKQ3pUUE45UEt5RWxWMVFoVzNNNmZleUFUY0pzaWlhQ3dkTHllalFaSjY4MTROMG1SM25tcXZjb25JWHg2dElzQS12RDB5ZkxTbWc0Tzd4YjJtUTZWSTRzYV9CSDNfMUpYck9vV2xrbm1aTw
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 16:12:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMinAJBVV95cUxQcEtBV1A1UVBQa0RCeHlRaDdBcDcxakpBZEwxc04zUy1BVDlYYWV4SnJMdHVQZTNXR0w3alNmWUVNRHpfRzNnYXNHTWNxTVdseThIWVRNczhOSS1NaFlMd2lPWHhlWDd3MEJoV0g2OHFteXNQRWxsNGs5UW1uYmNDRVVkWTVXakNPSms2S0xBeVZRbE8zSWFNT0FMcDR3VEx5aXdpcFdOZWVIVk0xbHY0NWtKQ3pUUE45UEt5RWxWMVFoVzNNNmZleUFUY0pzaWlhQ3dkTHllalFaSjY4MTROMG1SM25tcXZjb25JWHg2dElzQS12RDB5ZkxTbWc0Tzd4YjJtUTZWSTRzYV9CSDNfMUpYck9vV2xrbm1aTw?oc=5" target="_blank">"J’ai été choquée, car j’ai cru que c’était moi" : une influenceuse française découvre son image détournée par l’IA pour promouvoir un produit qu’elle ne connaît pas</a>&nbsp;&nbsp;<font color="#6f6f6f">ladepeche.fr</font>

## 180. "iQiyi est devenu fou": en Chine, le concurrent de Netflix provoque l'émoi en générant des profils et vidéos de stars de ses programmes avec l'IA - BFM
- Domain: bfmtv.com
- URL: https://news.google.com/rss/articles/CBMivAJBVV95cUxPdk1vOVZIUHh6U0FON0NtYldpS1dEbVNEdWJGV3o0THZhN0FuTEgyemdhRHVlNGlORGNUUlZacmFuMjNncWZPR1B5MUZHNnZyOTgwSU9SQXRJZ0FpdkI0ZXdXYkg3dURtc3NJRFhneERlTDFOR21XWkQyNnhBbVF5U2dMNDJlWXJ5RHI3dHdvY2JiNjM0b2xnaV9HRlBrMTBkV1ROamVWdkxLRW5odFdjQ1Z4TUZnVTc4dGozMkZNX0lGLVZJVGg4NndNYTBMOUVQVlF5dHQ1N29HQ2E0MWtWbjdXakxKcEVJa2V4UFR4ZDF0WjZpUjhmeG91RkxCQU4wTGxLZFJMZFZtZUZiTU0wZHVBZ2oyc1ZodkM1WFJKLWdZb2w0YllmMEpfT2JEWEN6bXEzYmI3VUZjQXkt
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 14:34:34 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMivAJBVV95cUxPdk1vOVZIUHh6U0FON0NtYldpS1dEbVNEdWJGV3o0THZhN0FuTEgyemdhRHVlNGlORGNUUlZacmFuMjNncWZPR1B5MUZHNnZyOTgwSU9SQXRJZ0FpdkI0ZXdXYkg3dURtc3NJRFhneERlTDFOR21XWkQyNnhBbVF5U2dMNDJlWXJ5RHI3dHdvY2JiNjM0b2xnaV9HRlBrMTBkV1ROamVWdkxLRW5odFdjQ1Z4TUZnVTc4dGozMkZNX0lGLVZJVGg4NndNYTBMOUVQVlF5dHQ1N29HQ2E0MWtWbjdXakxKcEVJa2V4UFR4ZDF0WjZpUjhmeG91RkxCQU4wTGxLZFJMZFZtZUZiTU0wZHVBZ2oyc1ZodkM1WFJKLWdZb2w0YllmMEpfT2JEWEN6bXEzYmI3VUZjQXkt?oc=5" target="_blank">"iQiyi est devenu fou": en Chine, le concurrent de Netflix provoque l'émoi en générant des profils et vidéos de stars de ses programmes avec l'IA</a>&nbsp;&nbsp;<font color="#6f6f6f">BFM</font>

## 181. Platforms roll out anti-AI infringement measures as Douyin removes over 538,000 short videos - Global Times
- Domain: globaltimes.cn
- URL: https://news.google.com/rss/articles/CBMiYkFVX3lxTE5zd3RQOEpTemxQM09yaDA3OVVHdktYTkJXZ3duSk84Qnc1TFV0S2cxUW1FWTNrM3JsRTNJUG1JdGFucV9oTS1UdlZySGd6bU5zSzlkMXhwR0ZCZk9IQ2U0blhn
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 14:33:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE5zd3RQOEpTemxQM09yaDA3OVVHdktYTkJXZ3duSk84Qnc1TFV0S2cxUW1FWTNrM3JsRTNJUG1JdGFucV9oTS1UdlZySGd6bU5zSzlkMXhwR0ZCZk9IQ2U0blhn?oc=5" target="_blank">Platforms roll out anti-AI infringement measures as Douyin removes over 538,000 short videos</a>&nbsp;&nbsp;<font color="#6f6f6f">Global Times</font>

## 182. Et si l'Église parlait d'intelligence artificielle ? Un festival surprenant à Lamballe - Actu.fr
- Domain: actu.fr
- URL: https://news.google.com/rss/articles/CBMi2gFBVV95cUxOXzFocG52MFM3ZlBDd3ZQdlQydzY4RmFtZTZqM1JoWndJVlMzZFhwYUtlanQybEhHN0M0d2pEZWZPSkV5SWgyNDNsakFCcV9MWVAxNGUxLXlvaldialZ1QklxU2N5eGJ0UW4yYzg2MnhRMHF3c3g1ZVA2V0owM0dKUnA1cDhuZDJHNzIyQUxneVNZM1VqTE9EQ29hcGZ3b1dOX2xVTGdZbVUtR19qck9aUnVyZXUtS2FFNTFhdkJVQjlTZTY5U0M2TEVDSjBGYlhzTkZCNm83THhJUQ
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 14:20:02 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi2gFBVV95cUxOXzFocG52MFM3ZlBDd3ZQdlQydzY4RmFtZTZqM1JoWndJVlMzZFhwYUtlanQybEhHN0M0d2pEZWZPSkV5SWgyNDNsakFCcV9MWVAxNGUxLXlvaldialZ1QklxU2N5eGJ0UW4yYzg2MnhRMHF3c3g1ZVA2V0owM0dKUnA1cDhuZDJHNzIyQUxneVNZM1VqTE9EQ29hcGZ3b1dOX2xVTGdZbVUtR19qck9aUnVyZXUtS2FFNTFhdkJVQjlTZTY5U0M2TEVDSjBGYlhzTkZCNm83THhJUQ?oc=5" target="_blank">Et si l'Église parlait d'intelligence artificielle ? Un festival surprenant à Lamballe</a>&nbsp;&nbsp;<font color="#6f6f6f">Actu.fr</font>

## 183. Comment faire avec l’intelligence artificielle ? - Travailleur alpin
- Domain: travailleur-alpin.fr
- URL: https://news.google.com/rss/articles/CBMijwFBVV95cUxPQUVFckI5VFBVQ2wxVWxRQXZzYTduUXZZcHRIeDZjQTMyY3BFc3NURWhxNktWYi1hTzVLbTJrZTRnYVJ6U1kwNGNuWGVCMkpVb3JTZ2xvbGc4XzNOTUxGUEhOd2owYTJoWmpVcGQ0SFh6Z1FPT1hBWDBuR3lrU0RxVENBeUdzMWh2ZDFtV2QtOA
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 14:08:56 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMijwFBVV95cUxPQUVFckI5VFBVQ2wxVWxRQXZzYTduUXZZcHRIeDZjQTMyY3BFc3NURWhxNktWYi1hTzVLbTJrZTRnYVJ6U1kwNGNuWGVCMkpVb3JTZ2xvbGc4XzNOTUxGUEhOd2owYTJoWmpVcGQ0SFh6Z1FPT1hBWDBuR3lrU0RxVENBeUdzMWh2ZDFtV2QtOA?oc=5" target="_blank">Comment faire avec l’intelligence artificielle ?</a>&nbsp;&nbsp;<font color="#6f6f6f">Travailleur alpin</font>

## 184. L’IA au travail est un facteur d’inégalités de genre - Courrier international
- Domain: courrierinternational.com
- URL: https://news.google.com/rss/articles/CBMiywFBVV95cUxNdFhvMnZsV19famdJTUZCbUY5SWlZMWY5eE1lX3Jsam1zZzQ0ZDl2emFvcUdrTGdKb1U1MVp0QXJDck1LUHV0ZnNISTJRUGFpSzBYZ1pWM25SRUtfRGQzN2JtZG11NnUyckZRUUt1MkUwd2NORHRjZlEycEtlV1piRWpiZVc2eWxrelRaYlpiYVR4TzNldE9ubmxBS0pqT0FYaEhGeWRNNzMxa1Ytd2k4RlZpRnJhZVhpWmhkdTBuS3lzeUpIMGNvaUFfRQ
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 14:02:14 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiywFBVV95cUxNdFhvMnZsV19famdJTUZCbUY5SWlZMWY5eE1lX3Jsam1zZzQ0ZDl2emFvcUdrTGdKb1U1MVp0QXJDck1LUHV0ZnNISTJRUGFpSzBYZ1pWM25SRUtfRGQzN2JtZG11NnUyckZRUUt1MkUwd2NORHRjZlEycEtlV1piRWpiZVc2eWxrelRaYlpiYVR4TzNldE9ubmxBS0pqT0FYaEhGeWRNNzMxa1Ytd2k4RlZpRnJhZVhpWmhkdTBuS3lzeUpIMGNvaUFfRQ?oc=5" target="_blank">L’IA au travail est un facteur d’inégalités de genre</a>&nbsp;&nbsp;<font color="#6f6f6f">Courrier international</font>

## 185. Proposed AI evidence rule highlights new challenges for federal practitioners - Reuters
- Domain: reuters.com
- URL: https://news.google.com/rss/articles/CBMi0wFBVV95cUxNcUV4ZGZNWWtrMURjRnMzNWtKY0xHZ0VsSWd2emo3WjB1QzE0bkRXNVJKSEhUb3hRemZleFhqbEdlUzBRWkI4S1VIOXp2VXI0OG8xQ2RubThuV0ZEenl0bEpGRFdic0FPbV8xbFg5ZkpodXJncmFxRlRIVXZMV1pRcXJOT284bkZ3QzFqN2YtaUFkZzB2SnZ6N28ySk5ObElDS1BSNGl2MFBfVTJjZ2NyUVZrTFJsaGRySjh0NExEMlpCVFctc0NCcy1DeG9GWC1sbGFV
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 13:45:35 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi0wFBVV95cUxNcUV4ZGZNWWtrMURjRnMzNWtKY0xHZ0VsSWd2emo3WjB1QzE0bkRXNVJKSEhUb3hRemZleFhqbEdlUzBRWkI4S1VIOXp2VXI0OG8xQ2RubThuV0ZEenl0bEpGRFdic0FPbV8xbFg5ZkpodXJncmFxRlRIVXZMV1pRcXJOT284bkZ3QzFqN2YtaUFkZzB2SnZ6N28ySk5ObElDS1BSNGl2MFBfVTJjZ2NyUVZrTFJsaGRySjh0NExEMlpCVFctc0NCcy1DeG9GWC1sbGFV?oc=5" target="_blank">Proposed AI evidence rule highlights new challenges for federal practitioners</a>&nbsp;&nbsp;<font color="#6f6f6f">Reuters</font>

## 186. UAE unveils first fully AI-discovered cancer drug candidate - Gulf News
- Domain: gulfnews.com
- URL: https://news.google.com/rss/articles/CBMizAFBVV95cUxPMmlzREpJYUJKS1dpLWhHZl9ORzRlaGdBZk5ocnFwZTQ4S0NuVkNqdlJSVUtxZ0daY0ltaDZoS3NVOW9XYzQ3MWVoM0ExeGpVMklzTUUyUnc4QzF5OWY1RmlnWmVnLWxjM0dHckMxRG8zTDc3NVU1MTR3a250d1p1N0JwUVJaVlM3akZmOUpIUi1odi0zdng3UmM0RWZDLVdlSUsxVl91eWZudkg4ekpyM3NkN0dISU85eVhHd3hhdTlaT1kyREdzQ2oxY3XSAd8BQVVfeXFMT0l3STdfb1R2V3ZXMmw3cS1BT2d0bHRBZ0g4NkVLMXZXRkh2RFNyN2l2RGFHSmFJSk9xVFB1MHgyMzE4OUNIMGs2VEVhbVZmVzJiLWJEZFBIbktvTFpheUdDelVOa1FWLXdVUzRreHZlUGFMbTB4cnB1WDBqUGNrTzJ2NVZoRG9uSExLLXBWUXUwWFNVN2xOSkFYWDJlRUFra1c3UXI3Qmp5VkhTeFhOTFljYkNSMTk3bGhqS193MERuUVd0Q016a2FwVXBEd1QtMURhQ21JQmlYRWs5V1h4SQ
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 13:17:46 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMizAFBVV95cUxPMmlzREpJYUJKS1dpLWhHZl9ORzRlaGdBZk5ocnFwZTQ4S0NuVkNqdlJSVUtxZ0daY0ltaDZoS3NVOW9XYzQ3MWVoM0ExeGpVMklzTUUyUnc4QzF5OWY1RmlnWmVnLWxjM0dHckMxRG8zTDc3NVU1MTR3a250d1p1N0JwUVJaVlM3akZmOUpIUi1odi0zdng3UmM0RWZDLVdlSUsxVl91eWZudkg4ekpyM3NkN0dISU85eVhHd3hhdTlaT1kyREdzQ2oxY3XSAd8BQVVfeXFMT0l3STdfb1R2V3ZXMmw3cS1BT2d0bHRBZ0g4NkVLMXZXRkh2RFNyN2l2RGFHSmFJSk9xVFB1MHgyMzE4OUNIMGs2VEVhbVZmVzJiLWJEZFBIbktvTFpheUdDelVOa1FWLXdVUzRreHZlUGFMbTB4cnB1WDBqUGNrTzJ2NVZoRG9uSExLLXBWUXUwWFNVN2xOSkFYWDJlRUFra1c3UXI3Qmp5VkhTeFhOTFljYkNSMTk3bGhqS193MERuUVd0Q016a2FwVXBEd1QtMURhQ21JQmlYRWs5V1h4SQ?oc=5" target="_blank">UAE unveils first fully AI-discovered cancer drug candidate</a>&nbsp;&nbsp;<font color="#6f6f6f">Gulf News</font>

## 187. “J'emmerde le copyright” : Mathieu Kassovitz défend les acteurs IA, et le fait savoir - Les Numériques
- Domain: lesnumeriques.com
- URL: https://news.google.com/rss/articles/CBMizgFBVV95cUxQU0UtZjZBVDk5ZnEtaHp0TkU2UGZOSDF6OFhRTFBsTkF2MWxySU15NUFjZ0RoR0oxOUlrclpEN0ZTeF9rQ3pHd2laWDE5cjA1eGpSMW1ETGdsTXRYZjMtd3JXdnp4Vk9XZ21kLTVRb2U4UnlkdFBSdlFIdHA3ZnN1MHhLN0FUeHEwUTYxTWtTUEZpNEdPMzY3b1YtVWxYYjNicE1uNXZOWlA4d2VPWmxKaWxDak9YZzhERUVXM0RFbHJmcnVVZWdnUi1ISGVwZw
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 13:10:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMizgFBVV95cUxQU0UtZjZBVDk5ZnEtaHp0TkU2UGZOSDF6OFhRTFBsTkF2MWxySU15NUFjZ0RoR0oxOUlrclpEN0ZTeF9rQ3pHd2laWDE5cjA1eGpSMW1ETGdsTXRYZjMtd3JXdnp4Vk9XZ21kLTVRb2U4UnlkdFBSdlFIdHA3ZnN1MHhLN0FUeHEwUTYxTWtTUEZpNEdPMzY3b1YtVWxYYjNicE1uNXZOWlA4d2VPWmxKaWxDak9YZzhERUVXM0RFbHJmcnVVZWdnUi1ISGVwZw?oc=5" target="_blank">“J'emmerde le copyright” : Mathieu Kassovitz défend les acteurs IA, et le fait savoir</a>&nbsp;&nbsp;<font color="#6f6f6f">Les Numériques</font>

## 188. Jeux vidéo : Ubisoft acte la réduction du télétravail pour ses salariés
- Domain: maddyness.com
- URL: https://www.maddyness.com/2026/04/23/jeux-video-ubisoft-acte-la-reduction-du-teletravail-pour-ses-salaries/
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 12:52:15 +0000
- Summary: <p>L’article <a href="https://www.maddyness.com/2026/04/23/jeux-video-ubisoft-acte-la-reduction-du-teletravail-pour-ses-salaries/">Jeux vidéo : Ubisoft acte la réduction du télétravail pour ses salariés</a> est apparu en premier sur <a href="https://www.maddyness.com">Maddyness - Le média pour comprendre l&#039;économie de demain</a>.</p>

## 189. Des centaines d'euros par heure: et si vous étiez payé pour apprendre à l'IA à faire votre travail? - RMC
- Domain: rmc.bfmtv.com
- URL: https://news.google.com/rss/articles/CBMi7AFBVV95cUxNLWtYZzgxaFNTd091bDZGUnJUVkh6emx0UTNwVkZRYkhsR0E1cnJoc3BYaE40OTJtNW96cmw0Y3NIdkZXUk85RGJyOGFQYzZfZzNySHFKcVl1SGxRRlZwVFN5eUVNMlI4MGIzZC0waUNzd0RkRG91ZENROTZ2ejlQbmlDaVROcHNlbzNvV2FFTW1xMVk5RVlMbVc2N2l6SVNIenNBYzV4R2dCdzhtdHNkTzJQU0loR191bHFQM1EtcGlsbVdZS09GbzczcDl4TkFqRzVralJ3VFQ2bFYzR1JrUXhWek5tRzR6UWJEYg
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 12:02:53 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi7AFBVV95cUxNLWtYZzgxaFNTd091bDZGUnJUVkh6emx0UTNwVkZRYkhsR0E1cnJoc3BYaE40OTJtNW96cmw0Y3NIdkZXUk85RGJyOGFQYzZfZzNySHFKcVl1SGxRRlZwVFN5eUVNMlI4MGIzZC0waUNzd0RkRG91ZENROTZ2ejlQbmlDaVROcHNlbzNvV2FFTW1xMVk5RVlMbVc2N2l6SVNIenNBYzV4R2dCdzhtdHNkTzJQU0loR191bHFQM1EtcGlsbVdZS09GbzczcDl4TkFqRzVralJ3VFQ2bFYzR1JrUXhWek5tRzR6UWJEYg?oc=5" target="_blank">Des centaines d'euros par heure: et si vous étiez payé pour apprendre à l'IA à faire votre travail?</a>&nbsp;&nbsp;<font color="#6f6f6f">RMC</font>

## 190. AI is both threat and opportunity for Fintech, says Banking Secretary - ANI News
- Domain: aninews.in
- URL: https://news.google.com/rss/articles/CBMiuwFBVV95cUxOUWNtbGhJUEk5RGV6ME0xdHBwcGdGWlRmOEhmenowNVZZVElXUUZNZ0NDTHp1WU56V0FUWENENEN1VDBlWnFIWEVDa0s5TnVKWFhTQkZHcHp6T2VaMUJ3ZlNDMC1YQkRBRGtZM0lCMllsUzRRelI5c0lncGVXa0RLMV9EYWVwTlFTUF84MEJEaTZ1X1hHNkNOejcxZDNFRVFtbFhhNWZvOHY2SHpWVktESEdrQ28zZnRESXdZ
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 11:57:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiuwFBVV95cUxOUWNtbGhJUEk5RGV6ME0xdHBwcGdGWlRmOEhmenowNVZZVElXUUZNZ0NDTHp1WU56V0FUWENENEN1VDBlWnFIWEVDa0s5TnVKWFhTQkZHcHp6T2VaMUJ3ZlNDMC1YQkRBRGtZM0lCMllsUzRRelI5c0lncGVXa0RLMV9EYWVwTlFTUF84MEJEaTZ1X1hHNkNOejcxZDNFRVFtbFhhNWZvOHY2SHpWVktESEdrQ28zZnRESXdZ?oc=5" target="_blank">AI is both threat and opportunity for Fintech, says Banking Secretary</a>&nbsp;&nbsp;<font color="#6f6f6f">ANI News</font>

## 191. Inside Google Workspace Intelligence: AI, Admin Controls, And What It Means - ciol.com
- Domain: ciol.com
- URL: https://news.google.com/rss/articles/CBMipAFBVV95cUxPSHhleEFVczh6QkVscTBHS2VXWDBKdlJFd0JRY28ta3pIbjJERUFObTVZUThVSHpmRkllSEg2Y0pFM3c1Nmd3S0p2MnRPaW93ZjJsZkJ0ZWdWdlhkWDFPdF9IenQ5S19mT0ZEa21WUkluMzVYVkJ6QkxWTVdOUDJRRE9maE9XUWJTaGNHVElDQW1faXloNG5VM3BsN1RjUkdCMmtDb9IBpAFBVV95cUxPSHhleEFVczh6QkVscTBHS2VXWDBKdlJFd0JRY28ta3pIbjJERUFObTVZUThVSHpmRkllSEg2Y0pFM3c1Nmd3S0p2MnRPaW93ZjJsZkJ0ZWdWdlhkWDFPdF9IenQ5S19mT0ZEa21WUkluMzVYVkJ6QkxWTVdOUDJRRE9maE9XUWJTaGNHVElDQW1faXloNG5VM3BsN1RjUkdCMmtDbw
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 11:32:52 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMipAFBVV95cUxPSHhleEFVczh6QkVscTBHS2VXWDBKdlJFd0JRY28ta3pIbjJERUFObTVZUThVSHpmRkllSEg2Y0pFM3c1Nmd3S0p2MnRPaW93ZjJsZkJ0ZWdWdlhkWDFPdF9IenQ5S19mT0ZEa21WUkluMzVYVkJ6QkxWTVdOUDJRRE9maE9XUWJTaGNHVElDQW1faXloNG5VM3BsN1RjUkdCMmtDb9IBpAFBVV95cUxPSHhleEFVczh6QkVscTBHS2VXWDBKdlJFd0JRY28ta3pIbjJERUFObTVZUThVSHpmRkllSEg2Y0pFM3c1Nmd3S0p2MnRPaW93ZjJsZkJ0ZWdWdlhkWDFPdF9IenQ5S19mT0ZEa21WUkluMzVYVkJ6QkxWTVdOUDJRRE9maE9XUWJTaGNHVElDQW1faXloNG5VM3BsN1RjUkdCMmtDbw?oc=5" target="_blank">Inside Google Workspace Intelligence: AI, Admin Controls, And What It Means</a>&nbsp;&nbsp;<font color="#6f6f6f">ciol.com</font>

## 192. War at machine speed: How AI became a decisive force in US-Israel conflict with Iran - ThePrint
- Domain: theprint.in
- URL: https://news.google.com/rss/articles/CBMivAFBVV95cUxOSVBPc2xDcW9RS3k3ZUhVM0t3S1ZOYUJzLV8yNW9wSXd5T05vN0xkVTljVlF2WDV4LUhrajllZXRkZnNRUFFERG05SnV6ZDd2VnpCd3FHdUw0TThfOS1YTGk1bUw4bF9PZVpWc0l4aU5XS2wyeUc4eU5jeWJxTzA2UFZIZVc3MWFTbzNrOVdPb2JyblV1YmxxTF9uTGJ3RXVOd2pLZEZsOE5hUkdneU9wdC1kVmZSaExHYzEtMtIBwgFBVV95cUxPZW5XZkY4UDhJby1MT2U4Z3ROdUxnOFQwX0Q3Ul9mTkpCcXZMa1NJYWhpN1BSeEVxeUxWem4ycjhZRWpFbDJfTFhzbndSZ0ItOWdMaUtCZjkyd2hrbHhmTml2YnlUNHRSemMzYmFRWkZ3WW5ZYW9PNkx0eDRlVVdjeTl1TTJfNWNFZ09CZS1wb2h4TTlZcDZzSXhaVHNTT2VpRHA5WUo0RF9ZZHJNM3ZTTGp1clNuTHM0THpDNndLOFJPZw
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 11:03:20 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMivAFBVV95cUxOSVBPc2xDcW9RS3k3ZUhVM0t3S1ZOYUJzLV8yNW9wSXd5T05vN0xkVTljVlF2WDV4LUhrajllZXRkZnNRUFFERG05SnV6ZDd2VnpCd3FHdUw0TThfOS1YTGk1bUw4bF9PZVpWc0l4aU5XS2wyeUc4eU5jeWJxTzA2UFZIZVc3MWFTbzNrOVdPb2JyblV1YmxxTF9uTGJ3RXVOd2pLZEZsOE5hUkdneU9wdC1kVmZSaExHYzEtMtIBwgFBVV95cUxPZW5XZkY4UDhJby1MT2U4Z3ROdUxnOFQwX0Q3Ul9mTkpCcXZMa1NJYWhpN1BSeEVxeUxWem4ycjhZRWpFbDJfTFhzbndSZ0ItOWdMaUtCZjkyd2hrbHhmTml2YnlUNHRSemMzYmFRWkZ3WW5ZYW9PNkx0eDRlVVdjeTl1TTJfNWNFZ09CZS1wb2h4TTlZcDZzSXhaVHNTT2VpRHA5WUo0RF9ZZHJNM3ZTTGp1clNuTHM0THpDNndLOFJPZw?oc=5" target="_blank">War at machine speed: How AI became a decisive force in US-Israel conflict with Iran</a>&nbsp;&nbsp;<font color="#6f6f6f">ThePrint</font>

## 193. OG&E to Host Bidgely EmPOWER AI 2026 Annual Conference in New York City - Business Wire
- Domain: businesswire.com
- URL: https://news.google.com/rss/articles/CBMixgFBVV95cUxNemVmaHEtT2lxUEgzcWFUSlVRWFh5R0RfNU5EeTBKWEJmX2puWUJDSkk4QXh5TExjNE9mOHZHeHBnU0I5U01HUXBEQnZ6cjk5bEM0cnhLWWNSSE1RcHBBQnhFUjhLX0J4WExSOHkwX2IwVUYzTHVULVF3blRVMGNDYTEwMENFMGdud2dqSS1XaVg4RjI5YndueXA1a29BSFVDZlM2RzVKaFRvc1FQV1QxQlQtUmRQbDhkQmozNFptOGx3TEJTVmc
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 11:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMixgFBVV95cUxNemVmaHEtT2lxUEgzcWFUSlVRWFh5R0RfNU5EeTBKWEJmX2puWUJDSkk4QXh5TExjNE9mOHZHeHBnU0I5U01HUXBEQnZ6cjk5bEM0cnhLWWNSSE1RcHBBQnhFUjhLX0J4WExSOHkwX2IwVUYzTHVULVF3blRVMGNDYTEwMENFMGdud2dqSS1XaVg4RjI5YndueXA1a29BSFVDZlM2RzVKaFRvc1FQV1QxQlQtUmRQbDhkQmozNFptOGx3TEJTVmc?oc=5" target="_blank">OG&amp;E to Host Bidgely EmPOWER AI 2026 Annual Conference in New York City</a>&nbsp;&nbsp;<font color="#6f6f6f">Business Wire</font>

## 194. AI is fueling a surge in crypto fraud schemes, IRS investigators say. For one victim, "There's nothing left." - CBS News
- Domain: cbsnews.com
- URL: https://news.google.com/rss/articles/CBMicEFVX3lxTE1adDVVNm1NeWswbFJUNWxOMXpQVl9kNkkyYVpiNzNUdTMxamQyU0VPczNiRVhBc3dOTmpTXzJQTTVLUGs5c1VBTU05ZEhrcUxpTlh6NXVZQUJCMEFnZUxmOHpYRXlOR1diYjhVVk4yXzPSAXZBVV95cUxNR29SMEFTTlJhSnhRbEFVcEwyb2RGQW9wY1pUZi1pX3d6TGZWNWtkcVhvMTJmdHhVbHc2c0dvdUk1M2xUNVI2UEtXdjlGUkhaYTF2emw2OG45V2Q5TEZXUEdEZUxreHUxWUltWUFzNk5UbXZzc0Fn
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 10:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMicEFVX3lxTE1adDVVNm1NeWswbFJUNWxOMXpQVl9kNkkyYVpiNzNUdTMxamQyU0VPczNiRVhBc3dOTmpTXzJQTTVLUGs5c1VBTU05ZEhrcUxpTlh6NXVZQUJCMEFnZUxmOHpYRXlOR1diYjhVVk4yXzPSAXZBVV95cUxNR29SMEFTTlJhSnhRbEFVcEwyb2RGQW9wY1pUZi1pX3d6TGZWNWtkcVhvMTJmdHhVbHc2c0dvdUk1M2xUNVI2UEtXdjlGUkhaYTF2emw2OG45V2Q5TEZXUEdEZUxreHUxWUltWUFzNk5UbXZzc0Fn?oc=5" target="_blank">AI is fueling a surge in crypto fraud schemes, IRS investigators say. For one victim, "There's nothing left."</a>&nbsp;&nbsp;<font color="#6f6f6f">CBS News</font>

## 195. L’intelligence artificielle, moteur ou mirage d’une nouvelle prospérité ? - Crédit Agricole
- Domain: etudes-economiques.credit-agricole.com
- URL: https://news.google.com/rss/articles/CBMiugFBVV95cUxOdkQ2YWFqdXEyV2ZsYWNSNGRwWUsweU1uMTJCbG5ucFRkUFBuWnJ5ZTQ1ZGZFdC1QOEZiZWM2dzZ0UjRCbk1jRE1lamNWaVp6RkZ1V3l5MXRraFZhWWl3VmFQc0lSWTQ3cVM4M25wd2VUcVlvX09hbHd0YzB1c2JDUW9tTVU1anh6SUEyNWtKRTVFb1NUVDB6RlduVUlnbzgtbk5QZDdUWnFXcDdnNTY5NGc0alh0aG9Ld3c
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 10:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiugFBVV95cUxOdkQ2YWFqdXEyV2ZsYWNSNGRwWUsweU1uMTJCbG5ucFRkUFBuWnJ5ZTQ1ZGZFdC1QOEZiZWM2dzZ0UjRCbk1jRE1lamNWaVp6RkZ1V3l5MXRraFZhWWl3VmFQc0lSWTQ3cVM4M25wd2VUcVlvX09hbHd0YzB1c2JDUW9tTVU1anh6SUEyNWtKRTVFb1NUVDB6RlduVUlnbzgtbk5QZDdUWnFXcDdnNTY5NGc0alh0aG9Ld3c?oc=5" target="_blank">L’intelligence artificielle, moteur ou mirage d’une nouvelle prospérité ?</a>&nbsp;&nbsp;<font color="#6f6f6f">Crédit Agricole</font>

## 196. Dans le parcours d’achat, les avis clients résistent à la montée de l’intelligence artificielle
- Domain: siecledigital.fr
- URL: https://siecledigital.fr/2026/04/23/dans-le-parcours-dachat-les-avis-clients-resistent-a-la-montee-de-lintelligence-artificielle/
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 09:35:17 +0000
- Summary: <a href="https://siecledigital.fr/2026/04/23/dans-le-parcours-dachat-les-avis-clients-resistent-a-la-montee-de-lintelligence-artificielle/" rel="nofollow" title="Dans le parcours d&rsquo;achat, les avis clients résistent à la montée de l&rsquo;intelligence artificielle"><img alt="Dans le parcours d&#039;achat, les avis clients résistent à la montée de l&#039;intelligence artificielle" class="webfeedsFeaturedVisual wp-post-image" height="350" src="https://siecledigital.fr/wp-content/uploads/2026/04/Dans-le-parcours-dachat-les-avis-clients-resistent-a-la-montee-de-lintelligence-artificielle-600x350.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="600" /></a>On nous répète que l&#8217;IA va tout changer. Qu&#8217;elle va raccourcir nos recherches, nous mâcher le travail de comparaison, nous souffler le bon resto ou le bon plombier sans qu&#8217;on ait besoin de scroller pendant vingt minutes. Et c&#8217;est vrai, en partie. Sauf que quand on regarde les chiffres de près, la réalité est plus [&#8230;]

## 197. Un outil d’intelligence artificielle au service de l’imagerie cardiovasculaire - Univadis
- Domain: univadis.fr
- URL: https://news.google.com/rss/articles/CBMirwFBVV95cUxQRDUwR3dlY0NKcUtWUG95T3M5UHBqbWVNTHNGU0pmZEh5YUxCWjdpOXZKdWFCd0VyN1dYWG1lbFZDTERTc0RLeUNibEUycFhxem5NTWtrYUtObVhSeHZsRUtYTVpfb0JIVWtHU0EwaGs1VXNUZHZLMzJWemhLenBjQ3ZWN2tFcGVCQ3NYbXFrTDA4X19fUlVBbXJlak5pbWNDYU5UeGhNWUdZQWl2M1J3
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 09:20:41 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMirwFBVV95cUxQRDUwR3dlY0NKcUtWUG95T3M5UHBqbWVNTHNGU0pmZEh5YUxCWjdpOXZKdWFCd0VyN1dYWG1lbFZDTERTc0RLeUNibEUycFhxem5NTWtrYUtObVhSeHZsRUtYTVpfb0JIVWtHU0EwaGs1VXNUZHZLMzJWemhLenBjQ3ZWN2tFcGVCQ3NYbXFrTDA4X19fUlVBbXJlak5pbWNDYU5UeGhNWUdZQWl2M1J3?oc=5" target="_blank">Un outil d’intelligence artificielle au service de l’imagerie cardiovasculaire</a>&nbsp;&nbsp;<font color="#6f6f6f">Univadis</font>

## 198. Aujourd'hui l'économie - Mythos: l'intelligence artificielle qui fait trembler la finance mondiale - RFI
- Domain: rfi.fr
- URL: https://news.google.com/rss/articles/CBMi1wFBVV95cUxOdVJzTzZ1SmY1REVNWjNNMDIySXBIMHVsXzgtaDJRQUVqQ1N6cTJtWFFTcmZ6MDlBT0Fvc1FHTzBLRl9HQktQdU16YTNSRnI0TVBBZXhHWHB2cTctU3otWjRHZ1YycHBuWHRPeEVFOUlvZnlNU3lCVS1mMUNWTFpyZm9FY0NhTXllV1o4MkFvNDNwR0Znc1JzaHl5Smp2eFJzNlJBLTM3WVY1UlVWNkkwOEc5aUtLM0lsWEhwUnd5WXlxUGtHOHRLS0dGV01jc3hfU2lkSXdQZw
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 09:08:20 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi1wFBVV95cUxOdVJzTzZ1SmY1REVNWjNNMDIySXBIMHVsXzgtaDJRQUVqQ1N6cTJtWFFTcmZ6MDlBT0Fvc1FHTzBLRl9HQktQdU16YTNSRnI0TVBBZXhHWHB2cTctU3otWjRHZ1YycHBuWHRPeEVFOUlvZnlNU3lCVS1mMUNWTFpyZm9FY0NhTXllV1o4MkFvNDNwR0Znc1JzaHl5Smp2eFJzNlJBLTM3WVY1UlVWNkkwOEc5aUtLM0lsWEhwUnd5WXlxUGtHOHRLS0dGV01jc3hfU2lkSXdQZw?oc=5" target="_blank">Aujourd'hui l'économie - Mythos: l'intelligence artificielle qui fait trembler la finance mondiale</a>&nbsp;&nbsp;<font color="#6f6f6f">RFI</font>

## 199. Meet AGI CPU — a specialist processor that engineers believe will power the next wave of AI - Live Science
- Domain: livescience.com
- URL: https://news.google.com/rss/articles/CBMiyAFBVV95cUxNU0RMYVVaTXRycXJONDk0aEk5SDdDRmFXeVBWejN0ZTN2U2pIRTlxSUNjR01weUsxSEdfYUNwOTV1VGktZE5GUlFJcGhzX2huaEFDUTFlbUpKcTdiaFB0cUdJVHVOYUc0QVZFcU0yWTBYeF9QOUZ1b3FoTUpqMVlNUEdHN1lDdDF3bm5Da1R6bTZ0NkZkVk9WM2luT0Q1VmxoTXl3UlhwOFFMbUdZYTljeDVuT0RBdlhYWmxNY0tmcnlLRk50cXg4bQ
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 09:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiyAFBVV95cUxNU0RMYVVaTXRycXJONDk0aEk5SDdDRmFXeVBWejN0ZTN2U2pIRTlxSUNjR01weUsxSEdfYUNwOTV1VGktZE5GUlFJcGhzX2huaEFDUTFlbUpKcTdiaFB0cUdJVHVOYUc0QVZFcU0yWTBYeF9QOUZ1b3FoTUpqMVlNUEdHN1lDdDF3bm5Da1R6bTZ0NkZkVk9WM2luT0Q1VmxoTXl3UlhwOFFMbUdZYTljeDVuT0RBdlhYWmxNY0tmcnlLRk50cXg4bQ?oc=5" target="_blank">Meet AGI CPU — a specialist processor that engineers believe will power the next wave of AI</a>&nbsp;&nbsp;<font color="#6f6f6f">Live Science</font>

## 200. Threads change enfin sa version web et ajoute une fonction très attendue
- Domain: siecledigital.fr
- URL: https://siecledigital.fr/2026/04/23/threads-change-enfin-sa-version-web-et-ajoute-une-fonction-tres-attendue/
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 08:54:59 +0000
- Summary: <a href="https://siecledigital.fr/2026/04/23/threads-change-enfin-sa-version-web-et-ajoute-une-fonction-tres-attendue/" rel="nofollow" title="Threads change enfin sa version web et ajoute une fonction très attendue"><img alt="Threads change enfin sa version web et ajoute une fonction très attendue" class="webfeedsFeaturedVisual wp-post-image" height="350" src="https://siecledigital.fr/wp-content/uploads/2026/04/Threads-change-enfin-sa-version-web-et-ajoute-une-fonction-tres-attendue-600x350.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="600" /></a>Un an pendant lequel les utilisateurs de Threads sur navigateur devaient se résigner. Pour envoyer un message privé, pas d&#8217;autre option que de dégainer le téléphone. Pas de bouton, pas d&#8217;icône, rien. Le bureau était la vitrine. Le mobile, l&#8217;arrière-boutique où les choses se passaient vraiment. Ce temps-là touche à sa fin. Connor Hayes, le [&#8230;]

## 201. Vercel Finds More Compromised Accounts in Context.ai-Linked Breach - The Hacker News
- Domain: thehackernews.com
- URL: https://news.google.com/rss/articles/CBMigwFBVV95cUxQU2MwYkFKZ3BOckFXeDRraHdKeXBQYzZaSUdRMzNBc002V2JzTVc3ZmZwSlBzajdILU1lZE1tNF9TcENGakRwMnhibV9ESDMzT1FqamxycXkwS0h1WjJsYWc0eE9QaFNXZHBvdGZEc3FhTXV6RzFIaFlWSDJrQjFMU2NsZw
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 08:40:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMigwFBVV95cUxQU2MwYkFKZ3BOckFXeDRraHdKeXBQYzZaSUdRMzNBc002V2JzTVc3ZmZwSlBzajdILU1lZE1tNF9TcENGakRwMnhibV9ESDMzT1FqamxycXkwS0h1WjJsYWc0eE9QaFNXZHBvdGZEc3FhTXV6RzFIaFlWSDJrQjFMU2NsZw?oc=5" target="_blank">Vercel Finds More Compromised Accounts in Context.ai-Linked Breach</a>&nbsp;&nbsp;<font color="#6f6f6f">The Hacker News</font>

## 202. Rohff prend position sur l'intelligence artificielle : "quand t'es un vrai MC..." - Generations - Hip Hop Soul Radio
- Domain: generations.fr
- URL: https://news.google.com/rss/articles/CBMiuAFBVV95cUxNRWhTWkE2SzNaTXhHT3Y0amNxVzBzWm9BNUVWQmJ2YmZmdXRlemJwSlAySzlsbHhhQkhDc3hCekxWVUdROFd4YkxnYkl0NWM0TjN3QmVmWWVLU1lwOFY4ZW05M1RVa0NfNXVDWlVsbHRsR092VEtoQmpDQTA5UEpsbk52RnhnU21od1VvXzJKOHRrT3BOYVZSWlY4UDNrd1N4a2I2VTdYS0RxaF9yTTcxSjI2Qmwxd3lR
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 08:39:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiuAFBVV95cUxNRWhTWkE2SzNaTXhHT3Y0amNxVzBzWm9BNUVWQmJ2YmZmdXRlemJwSlAySzlsbHhhQkhDc3hCekxWVUdROFd4YkxnYkl0NWM0TjN3QmVmWWVLU1lwOFY4ZW05M1RVa0NfNXVDWlVsbHRsR092VEtoQmpDQTA5UEpsbk52RnhnU21od1VvXzJKOHRrT3BOYVZSWlY4UDNrd1N4a2I2VTdYS0RxaF9yTTcxSjI2Qmwxd3lR?oc=5" target="_blank">Rohff prend position sur l'intelligence artificielle : "quand t'es un vrai MC..."</a>&nbsp;&nbsp;<font color="#6f6f6f">Generations - Hip Hop Soul Radio</font>

## 203. Univity lève 27 millions d’euros pour mettre sa constellation de satellites au service des opérateurs télécoms
- Domain: maddyness.com
- URL: https://www.maddyness.com/2026/04/23/univity-leve-27-millions-deuros-pour-mettre-sa-constellation-de-satellites-au-service-des-operateurs-telecoms/
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 08:00:00 +0000
- Summary: <p>L’article <a href="https://www.maddyness.com/2026/04/23/univity-leve-27-millions-deuros-pour-mettre-sa-constellation-de-satellites-au-service-des-operateurs-telecoms/">Univity lève 27 millions d’euros pour mettre sa constellation de satellites au service des opérateurs télécoms</a> est apparu en premier sur <a href="https://www.maddyness.com">Maddyness - Le média pour comprendre l&#039;économie de demain</a>.</p>

## 204. App Store : 26 applications crypto piégées ont réussi à passer les contrôles d’Apple
- Domain: siecledigital.fr
- URL: https://siecledigital.fr/2026/04/23/app-store-26-applications-crypto-piegees-ont-reussi-a-passer-les-controles-dapple/
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 07:59:20 +0000
- Summary: <a href="https://siecledigital.fr/2026/04/23/app-store-26-applications-crypto-piegees-ont-reussi-a-passer-les-controles-dapple/" rel="nofollow" title="App Store : 26 applications crypto piégées ont réussi à passer les contrôles d&rsquo;Apple"><img alt="App Store 26 applications crypto piégées ont réussi à passer les contrôles d&#039;Apple" class="webfeedsFeaturedVisual wp-post-image" height="350" src="https://siecledigital.fr/wp-content/uploads/2026/04/App-Store-26-applications-crypto-piegees-ont-reussi-a-passer-les-controles-dApple-600x350.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="600" /></a>L&#8217;App Store a longtemps servi d&#8217;argument commercial à Apple. Nous avions un jardin fermé, contrôlé, plus sûr que le Far West du Play Store. La campagne FakeWallet vient de fissurer sérieusement ce discours. Vingt-six applications frauduleuses, repérées par les chercheurs de Kaspersky, ont réussi à s&#8217;infiltrer dans la boutique officielle d&#8217;iOS. Leur cible était les [&#8230;]

## 205. CuspAI, ou la promesse d’une science accélérée par l’intelligence artificielle - frenchweb.fr
- Domain: frenchweb.fr
- URL: https://news.google.com/rss/articles/CBMiqwFBVV95cUxPUElmbzFudlJKSmhhOERmaWdNaDNVRjNWV3lvVm1ZWktTa0M1dFdXazN0V2RiV2Y3c3h0amdoVzhLRXkwX0UyTElBWm53cHpRckZmR2FpbkpkTWllYkJKOVpqUWV1M2RaUnozVzMzZEY5Sk1GMFNLYTB0YlEyd0lCT3J4N3VOVldxdWliREg1OEF0THE1dzBqVmNUSV9xSWExekxqTHRCMWlsMVE
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 07:37:30 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiqwFBVV95cUxPUElmbzFudlJKSmhhOERmaWdNaDNVRjNWV3lvVm1ZWktTa0M1dFdXazN0V2RiV2Y3c3h0amdoVzhLRXkwX0UyTElBWm53cHpRckZmR2FpbkpkTWllYkJKOVpqUWV1M2RaUnozVzMzZEY5Sk1GMFNLYTB0YlEyd0lCT3J4N3VOVldxdWliREg1OEF0THE1dzBqVmNUSV9xSWExekxqTHRCMWlsMVE?oc=5" target="_blank">CuspAI, ou la promesse d’une science accélérée par l’intelligence artificielle</a>&nbsp;&nbsp;<font color="#6f6f6f">frenchweb.fr</font>

## 206. SpaceX prépare un pari colossal à 60 milliards pour s’offrir la pépite de l’IA Cursor
- Domain: siecledigital.fr
- URL: https://siecledigital.fr/2026/04/23/spacex-prepare-un-pari-colossal-a-60-milliards-pour-soffrir-la-pepite-de-lia-cursor/
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 07:30:14 +0000
- Summary: <a href="https://siecledigital.fr/2026/04/23/spacex-prepare-un-pari-colossal-a-60-milliards-pour-soffrir-la-pepite-de-lia-cursor/" rel="nofollow" title="SpaceX prépare un pari colossal à 60 milliards pour s&rsquo;offrir la pépite de l&rsquo;IA Cursor"><img alt="SpaceX prépare un pari colossal à 60 milliards pour s&#039;offrir la pépite de l&#039;IA Cursor" class="webfeedsFeaturedVisual wp-post-image" height="350" src="https://siecledigital.fr/wp-content/uploads/2026/04/SpaceX-prepare-un-pari-colossal-a-60-milliards-pour-soffrir-la-pepite-de-lIA-Cursor-600x350.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="600" /></a>Nous avons une nouvelle annonce dans le monde de la tech et surtout de l&#8217;IA. Elle risque de faire couler beaucoup d&#8217;encre. Cursor a mis moins de deux ans pour s&#8217;installer sur l&#8217;écran de presque tous les ingénieurs logiciel qui se respectent. L&#8217;accord contient une clause qui a fait sursauter toute la Silicon Valley. En [&#8230;]

## 207. Powering the AI Era: Why Energy Efficiency Is Becoming a Telecom Priority in Asia - Telecom Review Asia
- Domain: telecomreviewasia.com
- URL: https://news.google.com/rss/articles/CBMi3AFBVV95cUxNWWt2NlRCejNDc0tHTF80MDFnbmFrUXRCbWVBQlNPemtyZWJUZDlVdGhlQS16ZzhuVUlBeUdfWVZoMVlnbUl5alpjUlFrZ1hLTXd4Z19ScmN2c0thVEk3NjVXbFJObGhvX0l1ZWNFQWtJUXJJbWJIT0djNmdNLTIxNnk0aFVZNllSMzNEdW9kczBES1FFYkJ0WmUwYlFzMWJBRkdXUXJOcDM0Nkp6TWRGQ1dURFczUGhWdW41RFZEUmZacHpSa2U1dnloOXBZVnNwTDRXRVd5V2JNTEdr
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 06:45:59 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi3AFBVV95cUxNWWt2NlRCejNDc0tHTF80MDFnbmFrUXRCbWVBQlNPemtyZWJUZDlVdGhlQS16ZzhuVUlBeUdfWVZoMVlnbUl5alpjUlFrZ1hLTXd4Z19ScmN2c0thVEk3NjVXbFJObGhvX0l1ZWNFQWtJUXJJbWJIT0djNmdNLTIxNnk0aFVZNllSMzNEdW9kczBES1FFYkJ0WmUwYlFzMWJBRkdXUXJOcDM0Nkp6TWRGQ1dURFczUGhWdW41RFZEUmZacHpSa2U1dnloOXBZVnNwTDRXRVd5V2JNTEdr?oc=5" target="_blank">Powering the AI Era: Why Energy Efficiency Is Becoming a Telecom Priority in Asia</a>&nbsp;&nbsp;<font color="#6f6f6f">Telecom Review Asia</font>

## 208. AI is already leading to fewer jobs for young people, says Sunak - BBC
- Domain: bbc.com
- URL: https://news.google.com/rss/articles/CBMiWkFVX3lxTE5yLTU0X21uY2hjR1paT0ZNYU0xV2xtV2NVRF9zY3doLUtOaWJ1N3FvcXdvaTNQek84SjhvWDBEcFphVmpuYzh6YkhtTXd6SWhBV2wtd1BMMEVkQQ
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 06:45:39 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE5yLTU0X21uY2hjR1paT0ZNYU0xV2xtV2NVRF9zY3doLUtOaWJ1N3FvcXdvaTNQek84SjhvWDBEcFphVmpuYzh6YkhtTXd6SWhBV2wtd1BMMEVkQQ?oc=5" target="_blank">AI is already leading to fewer jobs for young people, says Sunak</a>&nbsp;&nbsp;<font color="#6f6f6f">BBC</font>

## 209. « IA : la vraie bataille est organisationnelle, pas technologique » - La Tribune
- Domain: latribune.fr
- URL: https://news.google.com/rss/articles/CBMivwFBVV95cUxPdUtMWUsxMGZSUXo5SFNmc05ic3BFb3d6LUFXWkxHOWpMN3Z6QkNJN0lFYWNGamIzdTRZV1VOb2l4RW9LZGp5dTQ4aFVnQWZtZE10MkZYTUpFS1lsTzl0ekRaaDg3enp1U254UWN6eFhLNkhZNUJpT3h5QlFRYVBWZWNKM09LSjZKNHkxUGwzZDNWRXJiamRGR3FQcl8yamxwd3lqSWdsMm5wYlRRNWR2WUs2M0lENGRJOHN1RTlFcw
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 06:35:01 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMivwFBVV95cUxPdUtMWUsxMGZSUXo5SFNmc05ic3BFb3d6LUFXWkxHOWpMN3Z6QkNJN0lFYWNGamIzdTRZV1VOb2l4RW9LZGp5dTQ4aFVnQWZtZE10MkZYTUpFS1lsTzl0ekRaaDg3enp1U254UWN6eFhLNkhZNUJpT3h5QlFRYVBWZWNKM09LSjZKNHkxUGwzZDNWRXJiamRGR3FQcl8yamxwd3lqSWdsMm5wYlRRNWR2WUs2M0lENGRJOHN1RTlFcw?oc=5" target="_blank">« IA : la vraie bataille est organisationnelle, pas technologique »</a>&nbsp;&nbsp;<font color="#6f6f6f">La Tribune</font>

## 210. Tencent, Alibaba circle DeepSeek in US$20 billion AI deal talks - digitimes
- Domain: digitimes.com
- URL: https://news.google.com/rss/articles/CBMimwFBVV95cUxNcjZxUWlfR0x0aXRELUNQalBGNTRNbElzalBWV1JIVEl6MTd5bm16bTlPcy01MmtZUjhRLVktYWk0RWt1TVRidmtDM3RWTnU0MWYyZjNyYy1HQ29kTnpFMWtCcFlXek5YRGV0OHI4RE9PVXJTeE5QWUhFeUhwT2U4cXl1c3haNFpFOXRRMFRQOVkzZzM0YmVhalYtQQ
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 06:22:24 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMimwFBVV95cUxNcjZxUWlfR0x0aXRELUNQalBGNTRNbElzalBWV1JIVEl6MTd5bm16bTlPcy01MmtZUjhRLVktYWk0RWt1TVRidmtDM3RWTnU0MWYyZjNyYy1HQ29kTnpFMWtCcFlXek5YRGV0OHI4RE9PVXJTeE5QWUhFeUhwT2U4cXl1c3haNFpFOXRRMFRQOVkzZzM0YmVhalYtQQ?oc=5" target="_blank">Tencent, Alibaba circle DeepSeek in US$20 billion AI deal talks</a>&nbsp;&nbsp;<font color="#6f6f6f">digitimes</font>

## 211. Zacks Investment Ideas feature highlights Nvidia, Taiwan and Intel - The Globe and Mail
- Domain: theglobeandmail.com
- URL: https://news.google.com/rss/articles/CBMi5AFBVV95cUxPSV96XzRRY0tWVnhGTk5zTy0yRDZoVFNBUjAtUnZFU1p6LWdMd3g1WTZkbE5LbDZhQ2NZYU1Nd004azMyZ2tHV3BRYU1aY01uNF9EVGdkOWh2dkRId1F5QWd4UGJEMUJsTzlUS0l0NDBPX1A0bTFLOGx5ZGU4VUhQQ2tkR1djWElpOXpUNmlmWDlNTE9WdW94NzRGbXN5RGt3dmFiaEprT2Q0eU03V0twVUxLNU5SRkF0Skc2UE9rck9BejVlUTB6TVpyLU9TSHVKaURISXk4ZE5ETUtyUEJZVnJTWTQ
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 04:32:03 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi5AFBVV95cUxPSV96XzRRY0tWVnhGTk5zTy0yRDZoVFNBUjAtUnZFU1p6LWdMd3g1WTZkbE5LbDZhQ2NZYU1Nd004azMyZ2tHV3BRYU1aY01uNF9EVGdkOWh2dkRId1F5QWd4UGJEMUJsTzlUS0l0NDBPX1A0bTFLOGx5ZGU4VUhQQ2tkR1djWElpOXpUNmlmWDlNTE9WdW94NzRGbXN5RGt3dmFiaEprT2Q0eU03V0twVUxLNU5SRkF0Skc2UE9rck9BejVlUTB6TVpyLU9TSHVKaURISXk4ZE5ETUtyUEJZVnJTWTQ?oc=5" target="_blank">Zacks Investment Ideas feature highlights Nvidia, Taiwan and Intel</a>&nbsp;&nbsp;<font color="#6f6f6f">The Globe and Mail</font>

## 212. New study offers insight into the type of AI radiologists prefer - Radiology Business
- Domain: radiologybusiness.com
- URL: https://news.google.com/rss/articles/CBMiswFBVV95cUxOZnAzSTZEYUdlNkxSWFpGUXFoWkwtanJ3OGh0eVpaTk1Ua2FzUTNxX18wbW5Yck5vVGc2MERFRktiTTlwRG8zV1YxZEVDaHZGaXNKOUtQVzREU0p4bXYzQUI4aV9rRkJVMUdjc1B6amFjYnJud0xQdjNlNjB0cGJpeWdKbEQ0eDVodmE0dk5XVmZiWVlKcUVFRFBJV296NG1WMXczR1lzNVE5WmItVVVvNHZEZw
- Relevance score: 4.0
- Published: Thu, 23 Apr 2026 01:39:55 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiswFBVV95cUxOZnAzSTZEYUdlNkxSWFpGUXFoWkwtanJ3OGh0eVpaTk1Ua2FzUTNxX18wbW5Yck5vVGc2MERFRktiTTlwRG8zV1YxZEVDaHZGaXNKOUtQVzREU0p4bXYzQUI4aV9rRkJVMUdjc1B6amFjYnJud0xQdjNlNjB0cGJpeWdKbEQ0eDVodmE0dk5XVmZiWVlKcUVFRFBJV296NG1WMXczR1lzNVE5WmItVVVvNHZEZw?oc=5" target="_blank">New study offers insight into the type of AI radiologists prefer</a>&nbsp;&nbsp;<font color="#6f6f6f">Radiology Business</font>

## 213. Exploiter la « Kill chain » de Palantir pour bombarder massivement l’Iran - Chronique de Palestine
- Domain: chroniquepalestine.com
- URL: https://news.google.com/rss/articles/CBMingFBVV95cUxPU1N6NjZXYjRDNEtOSF8yakVPQ2lUY3I1QmZsMEtXQ1RlTmJKdnRXRXVlZ1p0Q2xGZkJnSWdlemRiZzRoODl5ZGlFUXZUWTVCQTJ0QkNack9XN043Z3FBTFU1cFdpYko3aHRkY2VvZ1hSN1JQLUdRQzg5RzJ1dG5zY0dEc2FQb3I3SEFvaERrNmJsVDNzRWhfRTlqelllUQ
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 05:44:23 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMingFBVV95cUxPU1N6NjZXYjRDNEtOSF8yakVPQ2lUY3I1QmZsMEtXQ1RlTmJKdnRXRXVlZ1p0Q2xGZkJnSWdlemRiZzRoODl5ZGlFUXZUWTVCQTJ0QkNack9XN043Z3FBTFU1cFdpYko3aHRkY2VvZ1hSN1JQLUdRQzg5RzJ1dG5zY0dEc2FQb3I3SEFvaERrNmJsVDNzRWhfRTlqelllUQ?oc=5" target="_blank">Exploiter la « Kill chain » de Palantir pour bombarder massivement l’Iran</a>&nbsp;&nbsp;<font color="#6f6f6f">Chronique de Palestine</font>

## 214. Using AI to Monitor Protests and Civil Unrest Worldwide - MitKat Advisory Services Pvt Ltd
- Domain: mitkatadvisory.com
- URL: https://news.google.com/rss/articles/CBMiiwFBVV95cUxPbEMzUW5kYjFUYUdlR1lnVGpEQjh4ZXc2TVAtRzFNZ01YSWd4NW4wOXRyUXVnOTczUVpVaFpUQTUyNWtJd0xXSDdKZEQ1WUxNWWc0NDNJaW0zcXFhellWWTR1b21zOUhkODhNSDh2Q2FXR3Vtb0oxX0ZaZS1nbXdtZHBPY2xoeGZITVpR
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 05:31:32 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiiwFBVV95cUxPbEMzUW5kYjFUYUdlR1lnVGpEQjh4ZXc2TVAtRzFNZ01YSWd4NW4wOXRyUXVnOTczUVpVaFpUQTUyNWtJd0xXSDdKZEQ1WUxNWWc0NDNJaW0zcXFhellWWTR1b21zOUhkODhNSDh2Q2FXR3Vtb0oxX0ZaZS1nbXdtZHBPY2xoeGZITVpR?oc=5" target="_blank">Using AI to Monitor Protests and Civil Unrest Worldwide</a>&nbsp;&nbsp;<font color="#6f6f6f">MitKat Advisory Services Pvt Ltd</font>

## 215. Enhancing electoral communication in Ukraine with AI tools - International IDEA
- Domain: idea.int
- URL: https://news.google.com/rss/articles/CBMiggFBVV95cUxNM3hSVHNkQmxoV0E1UmduOUZpenVhUFZ1bkFmYW4yYWNFazc2MEZkN2FZVV9yTGlmX0NNWTdIS2FTTGMyblNOXzZhYUlNZ1BPQjVoRWtTalNQZnE5WU9vOW5WNm4yRDlLcXJvb2tPSVhlOGxtZE43bFVUOTd2amVEbVZB
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 05:28:58 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxNM3hSVHNkQmxoV0E1UmduOUZpenVhUFZ1bkFmYW4yYWNFazc2MEZkN2FZVV9yTGlmX0NNWTdIS2FTTGMyblNOXzZhYUlNZ1BPQjVoRWtTalNQZnE5WU9vOW5WNm4yRDlLcXJvb2tPSVhlOGxtZE43bFVUOTd2amVEbVZB?oc=5" target="_blank">Enhancing electoral communication in Ukraine with AI tools</a>&nbsp;&nbsp;<font color="#6f6f6f">International IDEA</font>

## 216. Modern Networks Are the Foundation of AI‑Ready Manufacturing - ARC Advisory
- Domain: arcweb.com
- URL: https://news.google.com/rss/articles/CBMigwFBVV95cUxPdlpRbzRPRDVONmNmeF9aaWtCZGxnZ0ItSzFOVFNUNmxIczJQUktnRk5Xc3lKNW1VOG9yVnQxbkdCYkdKdnE5VW5QYm1ZYmpsSDVacnVMUkZpd2dmaGhfTTl5a3MwUHJ0OGdfenVkZVlIcEVvX2EzQWZXREdxOHU4VEdTRQ
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 05:24:56 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMigwFBVV95cUxPdlpRbzRPRDVONmNmeF9aaWtCZGxnZ0ItSzFOVFNUNmxIczJQUktnRk5Xc3lKNW1VOG9yVnQxbkdCYkdKdnE5VW5QYm1ZYmpsSDVacnVMUkZpd2dmaGhfTTl5a3MwUHJ0OGdfenVkZVlIcEVvX2EzQWZXREdxOHU4VEdTRQ?oc=5" target="_blank">Modern Networks Are the Foundation of AI‑Ready Manufacturing</a>&nbsp;&nbsp;<font color="#6f6f6f">ARC Advisory</font>

## 217. Bright Side of AI: Unmasking ₹30,000 Cr Hidden Income - The420.in
- Domain: the420.in
- URL: https://news.google.com/rss/articles/CBMihgFBVV95cUxOVWVJOTQwZDJnMnVsak1PaFVXZl9MalZ2dmQtZzEtc3VsUHJSNzQ4OExTUDE4am5yZEEyT1RqZTA0YUNROE00YTNpTFpkdWtLbUVwRW9na1RpZXF0aXZ5aTctVEJ1WkdIQldHN1dYdjVORUZDRW91YTQ3WUVTZUdWNW9IU1gwUQ
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 05:10:09 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMihgFBVV95cUxOVWVJOTQwZDJnMnVsak1PaFVXZl9MalZ2dmQtZzEtc3VsUHJSNzQ4OExTUDE4am5yZEEyT1RqZTA0YUNROE00YTNpTFpkdWtLbUVwRW9na1RpZXF0aXZ5aTctVEJ1WkdIQldHN1dYdjVORUZDRW91YTQ3WUVTZUdWNW9IU1gwUQ?oc=5" target="_blank">Bright Side of AI: Unmasking ₹30,000 Cr Hidden Income</a>&nbsp;&nbsp;<font color="#6f6f6f">The420.in</font>

## 218. AI in short-term rentals: Costs, flops and hits - PhocusWire
- Domain: phocuswire.com
- URL: https://news.google.com/rss/articles/CBMilgFBVV95cUxOSzU3VkxuZVl6TE50WndFVmJBZVRCdlhCTnI2bS1QbzJuUlE2bnlRV3VlRWdtMkpMQjZSUVMwb1NwV0UwZUxvRENnVzdzTTNucEVFNzg2TTQyWnk0c0hQbFVWcE5ESElucHdWMjF0a29vbC1VSzF0d2E2OGtBZ0Jvc21yRlVZcm5EVHA1RWdYQ19hYUZkbUE
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 05:06:20 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMilgFBVV95cUxOSzU3VkxuZVl6TE50WndFVmJBZVRCdlhCTnI2bS1QbzJuUlE2bnlRV3VlRWdtMkpMQjZSUVMwb1NwV0UwZUxvRENnVzdzTTNucEVFNzg2TTQyWnk0c0hQbFVWcE5ESElucHdWMjF0a29vbC1VSzF0d2E2OGtBZ0Jvc21yRlVZcm5EVHA1RWdYQ19hYUZkbUE?oc=5" target="_blank">AI in short-term rentals: Costs, flops and hits</a>&nbsp;&nbsp;<font color="#6f6f6f">PhocusWire</font>

## 219. Les actions de Zhipu AI et MiniMax chutent après le lancement du nouveau modèle open-source de DeepSeek - Investing.com France
- Domain: fr.investing.com
- URL: https://news.google.com/rss/articles/CBMi7wFBVV95cUxOZFJfOERBZVo4VjNoRkgzWUVGMm1GWklfMjJwcUQ1ODZNcE9LM052cnM0a3lvVXRfQzBRenk2V3JCRjJqTGlOdG1Xd2piUzNYN0VMZm1yWGRfTlpUWU1IMTZIU3JrTmZaQWdkQkFHdEd3MzJMOC1ibEdlZW1kZk9DdHlRRkNSN2JrVjZlNklORF9LQ3JiQ3FxZ09HMl9MeTRCQ2RMT0ZLc1kwTFZZRUxnRVJ4U3FkUy1lVUF5T1U1NHZuSkUycHVFeUVmcFpvWHdjOTBfTWlLT2lra01jVGpmVGhzb0F4VE83ZElTTnEyWQ
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 05:06:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi7wFBVV95cUxOZFJfOERBZVo4VjNoRkgzWUVGMm1GWklfMjJwcUQ1ODZNcE9LM052cnM0a3lvVXRfQzBRenk2V3JCRjJqTGlOdG1Xd2piUzNYN0VMZm1yWGRfTlpUWU1IMTZIU3JrTmZaQWdkQkFHdEd3MzJMOC1ibEdlZW1kZk9DdHlRRkNSN2JrVjZlNklORF9LQ3JiQ3FxZ09HMl9MeTRCQ2RMT0ZLc1kwTFZZRUxnRVJ4U3FkUy1lVUF5T1U1NHZuSkUycHVFeUVmcFpvWHdjOTBfTWlLT2lra01jVGpmVGhzb0F4VE83ZElTTnEyWQ?oc=5" target="_blank">Les actions de Zhipu AI et MiniMax chutent après le lancement du nouveau modèle open-source de DeepSeek</a>&nbsp;&nbsp;<font color="#6f6f6f">Investing.com France</font>

## 220. Meta To Cut 8,000 Jobs As It Shifts Focus To AI, Internet Reacts: ‘Jobs Aren’t Forever’ - News18
- Domain: news18.com
- URL: https://news.google.com/rss/articles/CBMiwgFBVV95cUxNR24wUXBjekotMVFKdFdEMFdrM1FPSWNvVTM3aHRfRmlxc2M5TTZFclZ0YnNjYnk5N09OeTc2S3JiN28zOHl4WE1PbFduYlVWV2t1bGV6TkR6UUdhUTlST3hmRlNkTkFWSUFRNmVWZnllbWk2U1pJemY2TDN1b1R5MzVWeDJhUi05TXVDSVhjY05VbERwOWhUdWhBV1BKM1hiTGtlT19rN284VmVLMTRXT1Jwdk1LakhXbVNWT0JpX3VTUQ
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 05:00:12 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiwgFBVV95cUxNR24wUXBjekotMVFKdFdEMFdrM1FPSWNvVTM3aHRfRmlxc2M5TTZFclZ0YnNjYnk5N09OeTc2S3JiN28zOHl4WE1PbFduYlVWV2t1bGV6TkR6UUdhUTlST3hmRlNkTkFWSUFRNmVWZnllbWk2U1pJemY2TDN1b1R5MzVWeDJhUi05TXVDSVhjY05VbERwOWhUdWhBV1BKM1hiTGtlT19rN284VmVLMTRXT1Jwdk1LakhXbVNWT0JpX3VTUQ?oc=5" target="_blank">Meta To Cut 8,000 Jobs As It Shifts Focus To AI, Internet Reacts: ‘Jobs Aren’t Forever’</a>&nbsp;&nbsp;<font color="#6f6f6f">News18</font>

## 221. Tesla acquires mysterious AI hardware start-up for $2B - NewsBytes
- Domain: newsbytesapp.com
- URL: https://news.google.com/rss/articles/CBMiogFBVV95cUxPV0VoZkpjQ1p1c2hXUUc5WFhub2RMd1Nra2N5ZUdvQktGMF9fUUtfMXpUeXhWWllEUWtmZjBoNGtfMGpEUU5veXpEN2ZVdWhKdk9UY3pocHBSMWhHS1Vabm56TzlIa3pTMURCSl9CWXZWclc1VkVPRkp3Z01tQXYtMzRLa1JMTmsybzBsam9IVEFxYjk2TGlzT0l4SVgxUFl1MFE
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 04:42:35 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxPV0VoZkpjQ1p1c2hXUUc5WFhub2RMd1Nra2N5ZUdvQktGMF9fUUtfMXpUeXhWWllEUWtmZjBoNGtfMGpEUU5veXpEN2ZVdWhKdk9UY3pocHBSMWhHS1Vabm56TzlIa3pTMURCSl9CWXZWclc1VkVPRkp3Z01tQXYtMzRLa1JMTmsybzBsam9IVEFxYjk2TGlzT0l4SVgxUFl1MFE?oc=5" target="_blank">Tesla acquires mysterious AI hardware start-up for $2B</a>&nbsp;&nbsp;<font color="#6f6f6f">NewsBytes</font>

## 222. ‘Clearly me’: AI Chinese drama accused of stealing faces - The Straits Times
- Domain: straitstimes.com
- URL: https://news.google.com/rss/articles/CBMikwFBVV95cUxQeWx3OVZfNlBRX0d2VlhueGN6akFWN3NzWG9BTThSVDRYMTRVWWFWM0hXTWFJc085aXczVFNqWWlYU2NMcjJqY2dJTms4VTRsUXBWMTQ5dlVRTGVLaDFDczNRV2FnTHJ5SFMxWEE1VFkxRUZGemMxXzVlTWFTT0w1RmFrRUdCdHo4OXYxc1VKUVFnWGM
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 04:36:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMikwFBVV95cUxQeWx3OVZfNlBRX0d2VlhueGN6akFWN3NzWG9BTThSVDRYMTRVWWFWM0hXTWFJc085aXczVFNqWWlYU2NMcjJqY2dJTms4VTRsUXBWMTQ5dlVRTGVLaDFDczNRV2FnTHJ5SFMxWEE1VFkxRUZGemMxXzVlTWFTT0w1RmFrRUdCdHo4OXYxc1VKUVFnWGM?oc=5" target="_blank">‘Clearly me’: AI Chinese drama accused of stealing faces</a>&nbsp;&nbsp;<font color="#6f6f6f">The Straits Times</font>

## 223. Sokin integrates AI identity verification from Jumio - IBS Intelligence
- Domain: ibsintelligence.com
- URL: https://news.google.com/rss/articles/CBMilgFBVV95cUxQUnJnaUwxT1UwUVloQjdZSElueFhqaFRoSklrRGlONjZUcWdiS20xNmMtRVpFd3I2bWNqWFFIUEhEc3BORThna2ZGX2tTXzBSYWtLUTRJUUItTjVURFJaRmU3S1BwdUlaTUFyUndNX0xYX3FZZHFlLU5TSWV3aXpuODlJQVJ5bUh3V1BTcFQtRTRuRUNvdnc
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 04:19:48 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMilgFBVV95cUxQUnJnaUwxT1UwUVloQjdZSElueFhqaFRoSklrRGlONjZUcWdiS20xNmMtRVpFd3I2bWNqWFFIUEhEc3BORThna2ZGX2tTXzBSYWtLUTRJUUItTjVURFJaRmU3S1BwdUlaTUFyUndNX0xYX3FZZHFlLU5TSWV3aXpuODlJQVJ5bUh3V1BTcFQtRTRuRUNvdnc?oc=5" target="_blank">Sokin integrates AI identity verification from Jumio</a>&nbsp;&nbsp;<font color="#6f6f6f">IBS Intelligence</font>

## 224. Meta lays off 8,000 employees to focus on AI - NewsBytes
- Domain: newsbytesapp.com
- URL: https://news.google.com/rss/articles/CBMimAFBVV95cUxON3ZmZ0tTXzliVjVVcnJreXdnOFdBSFBqTV9hTV9DRjJzczJRRGllOC14X2dEeC1QYzhoeXBKeTgtbENsV2ppSk9XdHk3QXJwUl84MVRGc3cxVENpcnFhcDNuaE1tcjZQeUV5ZlVVemkyQTh2RS1vcjNJc2FkdldsZTlOMV9jWUxaU2tYRWdCNUtZMF9QbmxOZQ
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 04:10:31 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMimAFBVV95cUxON3ZmZ0tTXzliVjVVcnJreXdnOFdBSFBqTV9hTV9DRjJzczJRRGllOC14X2dEeC1QYzhoeXBKeTgtbENsV2ppSk9XdHk3QXJwUl84MVRGc3cxVENpcnFhcDNuaE1tcjZQeUV5ZlVVemkyQTh2RS1vcjNJc2FkdldsZTlOMV9jWUxaU2tYRWdCNUtZMF9QbmxOZQ?oc=5" target="_blank">Meta lays off 8,000 employees to focus on AI</a>&nbsp;&nbsp;<font color="#6f6f6f">NewsBytes</font>

## 225. India-Japan Data Pact for AI Smart Cities - GK Today
- Domain: gktoday.in
- URL: https://news.google.com/rss/articles/CBMic0FVX3lxTE5LRjNWTnl1OUlyRHJiUzFzRmx4UFYzWXpNRVkwZU45ejliYUNxdWI5SHZXaUczOGlpYzI1RS15bHNhSjZfZjNqMTY4OHpzV2F2YzdhckZPR1dRUUxRYWxudDZVTlV4WnZOQWlVRHF3MHI1ZlU
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 04:04:49 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMic0FVX3lxTE5LRjNWTnl1OUlyRHJiUzFzRmx4UFYzWXpNRVkwZU45ejliYUNxdWI5SHZXaUczOGlpYzI1RS15bHNhSjZfZjNqMTY4OHpzV2F2YzdhckZPR1dRUUxRYWxudDZVTlV4WnZOQWlVRHF3MHI1ZlU?oc=5" target="_blank">India-Japan Data Pact for AI Smart Cities</a>&nbsp;&nbsp;<font color="#6f6f6f">GK Today</font>

## 226. Mythos AI triggers global alarm as EU cyber experts urge calm - Euractiv
- Domain: euractiv.com
- URL: https://news.google.com/rss/articles/CBMilwFBVV95cUxOYkFHRVBJWUJKWGhDaFdBS1BuN3pGR1lIMTVtYkV4NkhKWm5iOXZBWDVucjFIanFMTFFVVEtoTXNKVXZjWlk4LUg1cHRnQ2dEUzZzWk01N0hKMUxZam5LbjNMaWZYazNBYXl2UlVyUEVoaV80RWFBZWM2M1dndXVNaGU2WFFVbUJyRDZqanhPR3dPbHdMd2dF
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 04:01:52 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMilwFBVV95cUxOYkFHRVBJWUJKWGhDaFdBS1BuN3pGR1lIMTVtYkV4NkhKWm5iOXZBWDVucjFIanFMTFFVVEtoTXNKVXZjWlk4LUg1cHRnQ2dEUzZzWk01N0hKMUxZam5LbjNMaWZYazNBYXl2UlVyUEVoaV80RWFBZWM2M1dndXVNaGU2WFFVbUJyRDZqanhPR3dPbHdMd2dF?oc=5" target="_blank">Mythos AI triggers global alarm as EU cyber experts urge calm</a>&nbsp;&nbsp;<font color="#6f6f6f">Euractiv</font>

## 227. "C'est le sens de l'histoire". Cette société développe l'IA pour mieux gérer les demandes des citoyens dans les mairies - France 3 Régions
- Domain: france3-regions.franceinfo.fr
- URL: https://news.google.com/rss/articles/CBMipgJBVV95cUxNbjhnMTJUTVZNbjNWNS1RVzBCYi1va2o0b3lKTXFQeXJhRUtQWlN1NDN3dkVMVmQxcEg1SWpEdlB6UXRhZnp5bENDT1VEQndyb3JGYVpSQ3U2ZzFEMHhENnZmb2JYTWRrZmloNVltRVZzRVdvYzhzdnVtZWtZS2dBQ0FGX0Q5aTVoZDBWYlRKRG5sWktLZWNGODVjeUVSMmZISWJJUHFnTmJfeUZYLXVYeDRKSkc3bXJmdTlZYkRaUVFzdmFuMWNsX1Rnd0pPVDhiQVFBZUxIckdESWFialBnM1JUODktaGctaldVZUpqTGxiQkh2MTNUYkpYT3Vod2JXWXFUSEVzeTdWU2hrVGNYNHVvb3ZJbDRUdDlkYkcxNjJQWDFGcEE
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 04:00:20 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMipgJBVV95cUxNbjhnMTJUTVZNbjNWNS1RVzBCYi1va2o0b3lKTXFQeXJhRUtQWlN1NDN3dkVMVmQxcEg1SWpEdlB6UXRhZnp5bENDT1VEQndyb3JGYVpSQ3U2ZzFEMHhENnZmb2JYTWRrZmloNVltRVZzRVdvYzhzdnVtZWtZS2dBQ0FGX0Q5aTVoZDBWYlRKRG5sWktLZWNGODVjeUVSMmZISWJJUHFnTmJfeUZYLXVYeDRKSkc3bXJmdTlZYkRaUVFzdmFuMWNsX1Rnd0pPVDhiQVFBZUxIckdESWFialBnM1JUODktaGctaldVZUpqTGxiQkh2MTNUYkpYT3Vod2JXWXFUSEVzeTdWU2hrVGNYNHVvb3ZJbDRUdDlkYkcxNjJQWDFGcEE?oc=5" target="_blank">"C'est le sens de l'histoire". Cette société développe l'IA pour mieux gérer les demandes des citoyens dans les mairies</a>&nbsp;&nbsp;<font color="#6f6f6f">France 3 Régions</font>

## 228. AI in Primary Aluminium Industry: Refinery to Recycling Gains - alcircle
- Domain: alcircle.com
- URL: https://news.google.com/rss/articles/CBMi1AFBVV95cUxQUHZscXNIcG5DYnZZUmpPTktGYUFsLUYya0luOVAxVkxKcDVMSnFTM2pTUTJ0Tml6VWF2cGFaazR1NS1uOFNaRGFULXd2MktyTmtuV1BJRzBVTE5TeC1kXzBwMXBRcW1xN1pTYXhUUG12bTU4ZEs5bi1POGNTVVJDODNBSlpJNHEzQnF0WlAydnpTeXJPWkt2a3JQRHFFeUN2aldQUS12cU5jWl84c0phbVBINU1WUGs0SERlY24wcHE4dHB5LWNpdC1JQ1BDb3ZaTUplRA
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 03:51:12 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi1AFBVV95cUxQUHZscXNIcG5DYnZZUmpPTktGYUFsLUYya0luOVAxVkxKcDVMSnFTM2pTUTJ0Tml6VWF2cGFaazR1NS1uOFNaRGFULXd2MktyTmtuV1BJRzBVTE5TeC1kXzBwMXBRcW1xN1pTYXhUUG12bTU4ZEs5bi1POGNTVVJDODNBSlpJNHEzQnF0WlAydnpTeXJPWkt2a3JQRHFFeUN2aldQUS12cU5jWl84c0phbVBINU1WUGs0SERlY24wcHE4dHB5LWNpdC1JQ1BDb3ZaTUplRA?oc=5" target="_blank">AI in Primary Aluminium Industry: Refinery to Recycling Gains</a>&nbsp;&nbsp;<font color="#6f6f6f">alcircle</font>

## 229. «IA : le vrai problème des agences n’est pas technologique, il est structurel», Guillaume Ruckebusch (Syneido) - Stratégies
- Domain: strategies.fr
- URL: https://news.google.com/rss/articles/CBMi9gFBVV95cUxOOUhwdFNyVDhLd3BwUU16WTlHd1o5YWtxUVYtMmJ4VTRmRWlDRWt4MUVtMVVnTlZhR3hYV2JON1c4ejRlcFM0Rk1BemZQNVZyYmFTVVM4N2ViVERLS1YydEltLTlDS0lVbDdwSFg5M2labnFNd0xpTEdFdTlJVjJqNU1SdzhqWnU2ZjlaNi1DQ1JxVUZqZDc5VUgxMXRIZGg3RHRUcG1Oc1pheFR3YWdseVFuR3RfMjIxdlp5UnoxZUR3SG1QcWRCYU1OQm90WW12Q1Q2RS1NUXVoOXBIRmhIVnpiZHJpRGhSeFNGc3pVcGVQS0VqZEE
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 03:30:01 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi9gFBVV95cUxOOUhwdFNyVDhLd3BwUU16WTlHd1o5YWtxUVYtMmJ4VTRmRWlDRWt4MUVtMVVnTlZhR3hYV2JON1c4ejRlcFM0Rk1BemZQNVZyYmFTVVM4N2ViVERLS1YydEltLTlDS0lVbDdwSFg5M2labnFNd0xpTEdFdTlJVjJqNU1SdzhqWnU2ZjlaNi1DQ1JxVUZqZDc5VUgxMXRIZGg3RHRUcG1Oc1pheFR3YWdseVFuR3RfMjIxdlp5UnoxZUR3SG1QcWRCYU1OQm90WW12Q1Q2RS1NUXVoOXBIRmhIVnpiZHJpRGhSeFNGc3pVcGVQS0VqZEE?oc=5" target="_blank">«IA : le vrai problème des agences n’est pas technologique, il est structurel», Guillaume Ruckebusch (Syneido)</a>&nbsp;&nbsp;<font color="#6f6f6f">Stratégies</font>

## 230. Roads to Prosperity: To work for us, AI must not think for us - The Edge Malaysia
- Domain: theedgemalaysia.com
- URL: https://news.google.com/rss/articles/CBMiUEFVX3lxTE9hWV9WSmJJN2c0dkIzdTdzQzI3cnR5SDJfTGxHZS1CcjNnQWUtWTJXaTZyb1BldU9TZGgxMnY4QmJ2NG9lNzYyOUlPV2hCU3p5
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 03:30:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiUEFVX3lxTE9hWV9WSmJJN2c0dkIzdTdzQzI3cnR5SDJfTGxHZS1CcjNnQWUtWTJXaTZyb1BldU9TZGgxMnY4QmJ2NG9lNzYyOUlPV2hCU3p5?oc=5" target="_blank">Roads to Prosperity: To work for us, AI must not think for us</a>&nbsp;&nbsp;<font color="#6f6f6f">The Edge Malaysia</font>

## 231. India needs digital identity for every device and stronger AI-led cyber defence to curb threats: Experts - ETCISO.in
- Domain: ciso.economictimes.indiatimes.com
- URL: https://news.google.com/rss/articles/CBMi6AFBVV95cUxQMTZTUVNuLVJHWVBma3l1U1BlblA3VkFTVzNmbVdKOFd2ckdHWmNXZXBSVnpSVWRMeU15NUV5RDFqNmJ6d0xOcUpzZVRWU0F3UjFrOGMzWHlxRzd6cmtCSVFaUzdoN2Y4dTVYZWU0eXJZQ2VRNlNibUpVRGk1Q29VOThDOXRvbUN0YkMtN0FLaDZWZVFodXBjY0dzdFFWZHRveVBpZmlxSmROZXRXNzNURl9JSFhrOWtIY2RYYjZiQTBjUjJhNi1vc1RyWm1zMVlPUkJBUGFNS1RnbHhtUDNxZWZkVzZ6SFpG
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 02:57:22 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi6AFBVV95cUxQMTZTUVNuLVJHWVBma3l1U1BlblA3VkFTVzNmbVdKOFd2ckdHWmNXZXBSVnpSVWRMeU15NUV5RDFqNmJ6d0xOcUpzZVRWU0F3UjFrOGMzWHlxRzd6cmtCSVFaUzdoN2Y4dTVYZWU0eXJZQ2VRNlNibUpVRGk1Q29VOThDOXRvbUN0YkMtN0FLaDZWZVFodXBjY0dzdFFWZHRveVBpZmlxSmROZXRXNzNURl9JSFhrOWtIY2RYYjZiQTBjUjJhNi1vc1RyWm1zMVlPUkJBUGFNS1RnbHhtUDNxZWZkVzZ6SFpG?oc=5" target="_blank">India needs digital identity for every device and stronger AI-led cyber defence to curb threats: Experts</a>&nbsp;&nbsp;<font color="#6f6f6f">ETCISO.in</font>

## 232. The real-time data solution to the AI energy problem - IT Brief Australia
- Domain: itbrief.com.au
- URL: https://news.google.com/rss/articles/CBMiiAFBVV95cUxPMnRQQ3U0SUVFU2lqWElqSkdzRkR3cUN1SjFKdmhJVTRTQlB3VmgxbkFyUkFVSy1SaUFZUXZGRVB6TTdHQURUV3pCZEMycmJyV2RCSWp6OXk3SndlSHFvdktMY3pfY096ZWFXRFppaUtBaUdCYU1WakdJNktfNG1hY0NTSmg2c2Jt
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 02:44:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiiAFBVV95cUxPMnRQQ3U0SUVFU2lqWElqSkdzRkR3cUN1SjFKdmhJVTRTQlB3VmgxbkFyUkFVSy1SaUFZUXZGRVB6TTdHQURUV3pCZEMycmJyV2RCSWp6OXk3SndlSHFvdktMY3pfY096ZWFXRFppaUtBaUdCYU1WakdJNktfNG1hY0NTSmg2c2Jt?oc=5" target="_blank">The real-time data solution to the AI energy problem</a>&nbsp;&nbsp;<font color="#6f6f6f">IT Brief Australia</font>

## 233. AI Legislative Update: April 24, 2026 - Transparency Coalition
- Domain: transparencycoalition.ai
- URL: https://news.google.com/rss/articles/CBMiggFBVV95cUxOWGtqZHVYTUE3Qkl1WjQ3WFkwR1g1UXdQUFRCMnlxWkttbk9KZ0JtUjRuSElNMXdBYVBOLUc4WE1GZ2FpSElMWUdUWmZQOERlN1Y2aVA2Y1cyeFo1M0FGY2tPOGp4b29Ba3BFZWt4X1VZVDYxcm5DLUk1OVVxMjcxR293
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 02:29:59 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxOWGtqZHVYTUE3Qkl1WjQ3WFkwR1g1UXdQUFRCMnlxWkttbk9KZ0JtUjRuSElNMXdBYVBOLUc4WE1GZ2FpSElMWUdUWmZQOERlN1Y2aVA2Y1cyeFo1M0FGY2tPOGp4b29Ba3BFZWt4X1VZVDYxcm5DLUk1OVVxMjcxR293?oc=5" target="_blank">AI Legislative Update: April 24, 2026</a>&nbsp;&nbsp;<font color="#6f6f6f">Transparency Coalition</font>

## 234. AI Images Just Got Way Too Real - fox10tv.com
- Domain: fox10tv.com
- URL: https://news.google.com/rss/articles/CBMidkFVX3lxTFBRaFlIaGhURkQzTjV3SUJTNFBfYm4zSlhPLW1VZXIxcHJneTVzWHlkOWxFTXQtOEdyUmw1Y2dFNEpGd0g3aFZYMWtwRnQ5ajdCajNCSE1jc0dfaEpaTmZaUGIzc3pRWVdHcTNKNWg1Wk40TngxSFHSAYoBQVVfeXFMUHFQQTc4MjczYU8tdlF5VzNHSUFSeXVsNXFTSy1aM2NRenM0X3FMQmtELUlhdVhuaEdibXVXbGdHZUtybE9ycW9jNWs0M2NIeEdMNmRENFUyT3A5QlF5OG9ueFlaa3B5WmlETjlrRFJoYU9YX3hMRkZqM0E1TG1LRmNMaXA4Y01MbThR
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 02:28:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFBRaFlIaGhURkQzTjV3SUJTNFBfYm4zSlhPLW1VZXIxcHJneTVzWHlkOWxFTXQtOEdyUmw1Y2dFNEpGd0g3aFZYMWtwRnQ5ajdCajNCSE1jc0dfaEpaTmZaUGIzc3pRWVdHcTNKNWg1Wk40TngxSFHSAYoBQVVfeXFMUHFQQTc4MjczYU8tdlF5VzNHSUFSeXVsNXFTSy1aM2NRenM0X3FMQmtELUlhdVhuaEdibXVXbGdHZUtybE9ycW9jNWs0M2NIeEdMNmRENFUyT3A5QlF5OG9ueFlaa3B5WmlETjlrRFJoYU9YX3hMRkZqM0E1TG1LRmNMaXA4Y01MbThR?oc=5" target="_blank">AI Images Just Got Way Too Real</a>&nbsp;&nbsp;<font color="#6f6f6f">fox10tv.com</font>

## 235. Interview: Firms eyeing industrial AI leadership must be in China, says Siemens executive - Xinhua
- Domain: english.news.cn
- URL: https://news.google.com/rss/articles/CBMifEFVX3lxTE9DUkpNRlpwb1YzeWVObFVqV2VEaTZGOV9Qblh0eUpoZnAtcUJ6QWE0WGN6bWxjUWNJRWVuQ3NoaWZHdWliRWxLaG5oU3R2RFBiMXdJdHo2UkpaelA5X2xoZnFvSHpNY1JqMXp5N3ota0Rja0kyVDlYb011WnA
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 02:11:15 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMifEFVX3lxTE9DUkpNRlpwb1YzeWVObFVqV2VEaTZGOV9Qblh0eUpoZnAtcUJ6QWE0WGN6bWxjUWNJRWVuQ3NoaWZHdWliRWxLaG5oU3R2RFBiMXdJdHo2UkpaelA5X2xoZnFvSHpNY1JqMXp5N3ota0Rja0kyVDlYb011WnA?oc=5" target="_blank">Interview: Firms eyeing industrial AI leadership must be in China, says Siemens executive</a>&nbsp;&nbsp;<font color="#6f6f6f">Xinhua</font>

## 236. Will the backlash against AI turn violent? – podcast
- Domain: theguardian.com
- URL: https://www.theguardian.com/news/audio/2026/apr/24/will-the-backlash-against-ai-turn-violent-podcast
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 02:00:27 GMT
- Summary: <p>An attack on the home of OpenAI’s CEO Sam Altman – and on the company’s headquarters – has led to concerns the backlash against AI could become violent. Guardian journalist Nick Robins-Early and researcher Sean Fleming discuss</p><p>In a couple of weeks, at an arraignment hearing in California, Daniel Moreno-Gama will face formal charges, including attempted double homicide.</p><p>It comes after his attack on the home of OpenAI CEO Sam Altman – throwing a molotov cocktail at the property – before attempting to break into the entrance of the company’s headquarters hours later.</p> <a href="https://www.theguardian.com/news/audio/2026/apr/24/will-the-backlash-against-ai-turn-violent-podcast">Continue reading...</a>

## 237. IBM shareholder proposal demands IBM defend AI bias protocols - cio.com
- Domain: cio.com
- URL: https://news.google.com/rss/articles/CBMipAFBVV95cUxQUnA3elRsZTlSZ25fLWV1S1JJV21WMnpxSnVQRTdpbHVEdjlkZ3BBRlZXRDlFZ1BiZVZGN2tlZ0dIS2stUmQwWHlmMGRGNDAzTGdjdklzcl8tSm9DNzhscU5ESDJ2THRiYlhydUxkY2d0RTdYTTdzaFpyMXBCdElXbFVXbVk3Wk1Sb0g0UXRfNTJJc2pqdlZRQmNkOVJicmdGZTEzdQ
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 01:54:30 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMipAFBVV95cUxQUnA3elRsZTlSZ25fLWV1S1JJV21WMnpxSnVQRTdpbHVEdjlkZ3BBRlZXRDlFZ1BiZVZGN2tlZ0dIS2stUmQwWHlmMGRGNDAzTGdjdklzcl8tSm9DNzhscU5ESDJ2THRiYlhydUxkY2d0RTdYTTdzaFpyMXBCdElXbFVXbVk3Wk1Sb0g0UXRfNTJJc2pqdlZRQmNkOVJicmdGZTEzdQ?oc=5" target="_blank">IBM shareholder proposal demands IBM defend AI bias protocols</a>&nbsp;&nbsp;<font color="#6f6f6f">cio.com</font>

## 238. Nasscom chair Srikanth Velamakanni says AI will transform India's tech - NewsBytes
- Domain: newsbytesapp.com
- URL: https://news.google.com/rss/articles/CBMiuAFBVV95cUxNekxvb21qUlVmYmx6dWplWTN1LTg5NC03aHg3a1NwRTVFMnFuQ1Z0STZVeHJwZ09rUUxQNE5nOW5wLU53VTBRbERjQ1BVSC1fTE5TOFhxNzdXSzNUTklZTmsyM3NoXzhFWnYzbWNSWFpVWno0bjVON3hxUHI4ZWxZWmxmbTZ4ZE9BWDdWbGhaUFhCSFBpZ2huQlA5RFpVRjYxMjdza1hxaEViTnBhS1kwaGZFLTh6am81
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 01:24:31 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiuAFBVV95cUxNekxvb21qUlVmYmx6dWplWTN1LTg5NC03aHg3a1NwRTVFMnFuQ1Z0STZVeHJwZ09rUUxQNE5nOW5wLU53VTBRbERjQ1BVSC1fTE5TOFhxNzdXSzNUTklZTmsyM3NoXzhFWnYzbWNSWFpVWno0bjVON3hxUHI4ZWxZWmxmbTZ4ZE9BWDdWbGhaUFhCSFBpZ2huQlA5RFpVRjYxMjdza1hxaEViTnBhS1kwaGZFLTh6am81?oc=5" target="_blank">Nasscom chair Srikanth Velamakanni says AI will transform India's tech</a>&nbsp;&nbsp;<font color="#6f6f6f">NewsBytes</font>

## 239. Mapping The Military AI Industry – Analysis - Eurasia Review
- Domain: eurasiareview.com
- URL: https://news.google.com/rss/articles/CBMiiAFBVV95cUxPWFh6LXV0ZWx3SG9FRURoTUVkYUp1VnM0RHFTVGRnOXVzWmhBSXdHajVoZUpGOXVpU0pHQmpsWXJ4MTZrOWlPRXNScVByR0hjakhiV3d5ZXJLbm1PLUZFMEZxTXBqekhFUnl4OVVuZmxwakVjdFRoV2s2Q19taEJ5LVUyUjE4TXRG
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 01:21:29 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiiAFBVV95cUxPWFh6LXV0ZWx3SG9FRURoTUVkYUp1VnM0RHFTVGRnOXVzWmhBSXdHajVoZUpGOXVpU0pHQmpsWXJ4MTZrOWlPRXNScVByR0hjakhiV3d5ZXJLbm1PLUZFMEZxTXBqekhFUnl4OVVuZmxwakVjdFRoV2s2Q19taEJ5LVUyUjE4TXRG?oc=5" target="_blank">Mapping The Military AI Industry – Analysis</a>&nbsp;&nbsp;<font color="#6f6f6f">Eurasia Review</font>

## 240. When it comes to AI, there is no such thing as too many chefs - Singapore Business Review
- Domain: sbr.com.sg
- URL: https://news.google.com/rss/articles/CBMipwFBVV95cUxPM21VSWZNbU1nQ3dLSWU1d3FnS0ZGc2NZeVA3OW44bXBVUU9aTnpkaEZSMkZ2RVIzM3VWVU9PdUppUnFwbWpaZE9BSlQxbjFuNTZra0c4MnBUZWtXMXdRV1hCLXJTYjJWMWx4ZlpmWVdEZ2pDdUR0RlVRUE9QbTJLa2xNZlRsUkF0QVR2bGRZeVluUmI0RjRQS0t0bDRIaWozVHRzdE9aUQ
- Relevance score: 4.0
- Published: Fri, 24 Apr 2026 00:39:22 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMipwFBVV95cUxPM21VSWZNbU1nQ3dLSWU1d3FnS0ZGc2NZeVA3OW44bXBVUU9aTnpkaEZSMkZ2RVIzM3VWVU9PdUppUnFwbWpaZE9BSlQxbjFuNTZra0c4MnBUZWtXMXdRV1hCLXJTYjJWMWx4ZlpmWVdEZ2pDdUR0RlVRUE9QbTJLa2xNZlRsUkF0QVR2bGRZeVluUmI0RjRQS0t0bDRIaWozVHRzdE9aUQ?oc=5" target="_blank">When it comes to AI, there is no such thing as too many chefs</a>&nbsp;&nbsp;<font color="#6f6f6f">Singapore Business Review</font>

## 241. Claude is connecting directly to your personal apps like Spotify, Uber Eats, and TurboTax
- Domain: theverge.com
- URL: https://www.theverge.com/ai-artificial-intelligence/917871/anthropic-claude-personal-app-connectors
- Relevance score: 3.8
- Published: 2026-04-23T18:27:11-04:00
- Summary: Claude users can access more apps with Anthropic's AI now thanks to new connectors for everything from hiking to grocery shopping. Anthropic already supported connecting numerous work-related apps to Claude, like Microsoft apps, but this expansion focuses on personal apps like Audible, Spotify, Uber, AllTrails, TripAdvisor, Instacart, TurboTax, and others. Some of these apps, such [&#8230;]

## 242. Google makes an interesting choice with its new agent-building tool for enterprises
- Domain: techcrunch.com
- URL: https://techcrunch.com/2026/04/22/google-makes-an-interesting-choice-with-its-new-agent-building-tool-for-enterprises/
- Relevance score: 3.5
- Published: Wed, 22 Apr 2026 16:58:27 +0000
- Summary: Gemini Enterprise Agent Platform takes an interesting approach: It is geared for IT and technical users.

## 243. Emma the joke-telling robot cracks up the care home: Paula Hornickel’s best photograph
- Domain: theguardian.com
- URL: https://www.theguardian.com/artanddesign/2026/apr/22/emma-robot-care-home-paula-hornickel-best-photograph
- Relevance score: 3.5
- Published: Wed, 22 Apr 2026 13:49:48 GMT
- Summary: <p>‘The first resident that Emma – a social robot – was introduced to was called Peter. After that, Emma assumed they were all called Peter, which everyone found hilarious. Then she broke down’</p><p>One morning in July 2025, I arrived in the small, quiet town of Albershausen in south-west Germany. It has only around 4,000 inhabitants. I went to visit a care home where they were piloting a social robot named Emma. A group of residents sat in a circle while Emma stood in the middle. She’s the height of a toddler, with big googly eyes, and was wearing a red hat knitted for her by one of the careworkers. The first resident she was introduced to was called Peter and, after he introduced himself, Emma assumed they were all called Peter, which everyone found hilarious. Then Emma broke down suddenly and the illusion was shattered.</p><p>Later on, Emma was working again, and I found her in the dining room with Waltraud, the resident in this photo. It was a calmer, more focused moment. I decided to sit them across from one another at eye level, Waltraud facing Emma. There was a soft light in the room and they both seemed very present with one another. There are also paradoxes in the picture

## 244. Codex settings
- Domain: openai.com
- URL: https://openai.com/academy/codex-settings
- Relevance score: 3.5
- Published: Thu, 23 Apr 2026 10:00:00 GMT
- Summary: Learn how to configure Codex settings, including personalization, detail level, and permissions, to run tasks smoothly and customize your workflow.

## 245. Quoting Maggie Appleton
- Domain: simonwillison.net
- URL: https://simonwillison.net/2026/Apr/23/maggie-appleton/
- Relevance score: 3.2
- Published: 2026-04-23T13:35:37+00:00
- Summary: <blockquote cite="https://maggieappleton.com/gathering-structures"><p>[...] if you ever needed another reason to <a href="https://www.swyx.io/learn-in-public">learn in public</a> by <a href="https://maggieappleton.com/garden-history">digital gardening</a> or podcasting or streaming or whathaveyou, add on that people will assume you’re more competent than you are. This will get you invites to very cool exclusive events filled with high-achieving, interesting people, even though you have no right to be there. A+ side benefit.</p></blockquote> <p class="cite">&mdash; <a href="https://maggieappleton.com/gathering-structures">Maggie Appleton</a>, Gathering Structures (<a href="https://notes.andymatuschak.org/Work_with_the_garage_door_up">via</a>)</p> <p>Tags: <a href="https://simonwillison.net/tags/blogging">blogging</a>, <a href="https://simonwillison.net/tags/maggie-appleton">maggie-appleton</a></p>

## 246. AI-powered robot beats elite table tennis players
- Domain: theguardian.com
- URL: https://www.theguardian.com/science/2026/apr/22/ai-powered-robot-beats-elite-table-tennis-players-milestone-robotics
- Relevance score: 3.0
- Published: Wed, 22 Apr 2026 15:00:30 GMT
- Summary: <p>In feat hailed as milestone in robotics, Sony AI’s Ace wins three out of five matches played under official rules</p><p>An AI-powered robot has beaten elite players at table tennis in a significant achievement for a machine faced with human athletes in a real-world competitive sport.</p><p>Named Ace, the robotic system developed by Sony AI, won three out of five matches against elite players, but lost the two it played against professionals, clawing back only one game in the seven contests.</p> <a href="https://www.theguardian.com/science/2026/apr/22/ai-powered-robot-beats-elite-table-tennis-players-milestone-robotics">Continue reading...</a>

## 247. Met police in talks to buy Palantir AI tech for use in criminal investigations
- Domain: theguardian.com
- URL: https://www.theguardian.com/uk-news/2026/apr/22/met-police-talks-palantir-ai-tech-criminal-investigations-automate-intelligence
- Relevance score: 3.0
- Published: Wed, 22 Apr 2026 14:00:26 GMT
- Summary: <p>Exclusive: Internal concerns over allowing US firm linked to ICE and Israeli military to process highly sensitive data </p><p>The Metropolitan police has held talks with <a href="https://www.theguardian.com/technology/palantir">Palantir</a> that could lead to the London force buying the US spy-tech company’s AI technology to automate intelligence analysis for criminal investigations, the Guardian has learned.</p><p>Palantir, whose software is used by Donald Trump’s ICE immigration enforcement programme and the Israeli military, demonstrated its systems to senior officers in the intelligence division at the UK’s largest police force last month. Intelligence staff have been tasked with finding intelligence systems that AI could automate to increase productivity.</p> <a href="https://www.theguardian.com/uk-news/2026/apr/22/met-police-talks-palantir-ai-tech-criminal-investigations-automate-intelligence">Continue reading...</a>

## 248. Beyond tools: India’s AI upskilling surge demands a mindset shift
- Domain: economictimes.indiatimes.com
- URL: https://economictimes.indiatimes.com/jobs/mid-career/beyond-tools-indias-ai-upskilling-surge-demands-a-mindset-shift/articleshow/130438594.cms
- Relevance score: 3.0
- Published: 2026-04-22T10:32:39Z
- Summary: India's professionals, including those with over 15 years of experience, are rapidly enrolling in AI and ML courses, signaling a shift from traditional expertise to staying relevant. This surge, extending beyond the tech sector, highlights a critical need to …

## 249. How indirect prompt injection attacks on AI work - and 6 ways to shut them down
- Domain: zdnet.com
- URL: https://www.zdnet.com/article/how-indirect-prompt-injection-attacks-on-ai-work-and-6-ways-to-shut-them-down/
- Relevance score: 2.7
- Published: Fri, 24 Apr 2026 00:00:45 GMT
- Summary: Cybercriminals are tricking AI into leaking your data, executing code, and sending you to malicious sites. Here's how.

## 250. Hands on with X’s new AI-powered custom feeds
- Domain: techcrunch.com
- URL: https://techcrunch.com/2026/04/22/hands-on-with-xs-new-ai-powered-custom-feeds/
- Relevance score: 2.5
- Published: Wed, 22 Apr 2026 22:25:53 +0000
- Summary: X's AI-powered custom timelines are replacing Communities, with Grok-curated feeds...and new ad slots.

## 251. Era raises $11M to build a software platform for AI gadgets
- Domain: techcrunch.com
- URL: https://techcrunch.com/2026/04/23/era-computer-raises-11m-to-build-a-software-platform-for-ai-gadgets/
- Relevance score: 2.5
- Published: Thu, 23 Apr 2026 16:00:00 +0000
- Summary: Era thinks that we will see many form factors of AI hardware, including glasses, rings, and pendants.

## 252. UK Biobank health data listed for sale in China, government confirms
- Domain: bbc.com
- URL: https://www.bbc.com/news/articles/cpvxgl3n138o
- Relevance score: 2.5
- Published: Thu, 23 Apr 2026 11:45:41 GMT
- Summary: The government said medical data of 500,000 people was affected but no personally identifiable information had been made available.

## 253. India’s app market is booming — but global platforms are capturing most of the gains
- Domain: techcrunch.com
- URL: https://techcrunch.com/2026/04/22/indias-app-market-is-booming-but-global-platforms-are-capturing-most-of-the-gains/
- Relevance score: 2.5
- Published: Thu, 23 Apr 2026 04:38:45 +0000
- Summary: Non-gaming apps, led by streaming and AI, are driving growth, even as India's spending per user lags global peers.

## 254. Due Diligence as a Catalyst for Growth (Blog)
- Domain: ssir.org
- URL: https://ssir.org/articles/entry/due-diligence-deeper-partnerships
- Relevance score: 2.5
- Published: 2026-04-22T12:00:00Z
- Summary: Why philanthropy should think of due diligence not as a vetting exercise, but as an opportunity to build deeper partnerships that lead to more sustainable impact.

## 255. The Pope’s Warnings About AI Were AI-Generated, a Detection Tool Claims
- Domain: wired.com
- URL: https://www.wired.com/story/pope-tweets-ai-generated-pangram-chrome-extension/
- Relevance score: 2.3
- Published: Wed, 22 Apr 2026 09:30:00 +0000
- Summary: Pangram Labs’ updated Chrome extension puts warning labels on AI slop as you scroll your social feeds.

## 256. This high-tech eye massager makes a great Mother's Day gift - and it's on sale
- Domain: zdnet.com
- URL: https://www.zdnet.com/article/renpho-eye-massager-deal/
- Relevance score: 2.2
- Published: Thu, 23 Apr 2026 20:19:30 GMT
- Summary: The Renpho Eye Massager can help alleviate piercing headaches and migraines - and it's 23% off at Amazon right now.

## 257. It's time to reclaim the word "Palantir" for JRR Tolkien
- Domain: zig.art
- URL: https://www.zig.art/p/its-time-to-reclaim-the-word-palantir
- Relevance score: 2.0
- Published: 2026-04-23T03:34:06Z
- Summary: Let's take back a term that once warned us about delusions of grandeur, careless leaders, and their ill-fated wars — and use it instead to better understand the risky nature of cloud platforms
