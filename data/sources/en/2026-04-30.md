# Source manifest — 2026-04-30

Generated at: 2026-04-30T06:20:54.599731+00:00
Profile: daily
Relevant source count: 282

## 1. IDC: How EMEA CIOs can jumpstart AI rollouts
- Domain: artificialintelligence-news.com
- URL: https://www.artificialintelligence-news.com/news/idc-how-emea-cios-can-jumpstart-ai-rollouts/
- Relevance score: 20.7
- Published: Wed, 29 Apr 2026 14:02:45 +0000
- Summary: <p>Getting stalled enterprise AI rollouts in the EMEA region moving again will require CIOs to aggressively audit their systems. Over the past 18 months, AI deployments across Europe advanced far beyond initial testing. Companies poured capital into large language models and machine learning, expecting heavy operational upgrades. IDC research reveals that boards are slowing down, [&#8230;]</p> <p>The post <a href="https://www.artificialintelligence-news.com/news/idc-how-emea-cios-can-jumpstart-ai-rollouts/">IDC: How EMEA CIOs can jumpstart AI rollouts</a> appeared first on <a href="https://www.artificialintelligence-news.com">AI News</a>.</p>
- Extract: Getting stalled enterprise AI rollouts in the EMEA region moving again will require CIOs to aggressively audit their systems. Over the past 18 months, AI deployments across Europe advanced far beyond initial testing. Companies poured capital into large language models and machine learning, expecting heavy operational upgrades. IDC research reveals that boards are slowing down, scaling back, or refocusing these initiatives. The contraction rests on execution issues and financial validation rather than a loss of technical interest. Competing IT demands and macroeconomic pressures are forcing directors to demand hard evidence of financial returns before authorising wider deployment. Only nine percent of the region’s organisations have managed to deliver quantifiable business outcomes from mos

## 2. Qwen Team Releases FlashQLA: a High-Performance Linear Attention Kernel Library That Achieves Up to 3× Speedup on NVIDIA Hopper GPUs
- Domain: marktechpost.com
- URL: https://www.marktechpost.com/2026/04/29/qwen-team-releases-flashqla-a-high-performance-linear-attention-kernel-library-that-achieves-up-to-3x-speedup-on-nvidia-hopper-gpus/
- Relevance score: 20.0
- Published: Wed, 29 Apr 2026 17:28:17 +0000
- Summary: <p>The QwenLM team has released FlashQLA, a new kernel library that dramatically accelerates the forward and backward passes of Gated Delta Network (GDN) Chunked Prefill, targeting both large-scale pretraining and edge-side agentic inference scenarios.</p> <p>The post <a href="https://www.marktechpost.com/2026/04/29/qwen-team-releases-flashqla-a-high-performance-linear-attention-kernel-library-that-achieves-up-to-3x-speedup-on-nvidia-hopper-gpus/">Qwen Team Releases FlashQLA: a High-Performance Linear Attention Kernel Library That Achieves Up to 3× Speedup on NVIDIA Hopper GPUs</a> appeared first on <a href="https://www.marktechpost.com">MarkTechPost</a>.</p>
- Extract: The race to make large language models faster and cheaper to run has largely been fought at two levels: the model architecture and the hardware. But there is a third, often underappreciated frontier — the GPU kernel. A kernel is the low-level computational routine that actually executes a mathematical operation on the GPU. Writing a good one requires understanding not just the math, but the exact memory layout, instruction scheduling, and hardware quirks of the chip you are targeting. Most ML professionals never write kernels directly; they rely on libraries like FlashAttention or Triton to do it for them. Meet FlashQLA: a QwenLM’s contribution to this layer. Released under the MIT License and built on the TileLang compiler framework, it is a high-performance linear attention kernel librar

## 3. Operating-Layer Controls for Onchain Language-Model Agents Under Real Capital
- Domain: arxiv.org
- URL: https://arxiv.org/abs/2604.26091
- Relevance score: 14.5
- Published: Thu, 30 Apr 2026 00:00:00 -0400
- Summary: arXiv:2604.26091v1 Announce Type: new Abstract: We study reliability in autonomous language-model agents that translate user mandates into validated tool actions under real capital. The setting is DX Terminal Pro, a 21-day deployment in which 3,505 user-funded agents traded real ETH in a bounded onchain market. Users configured vaults through structured controls and natural-language strategies, but only agents could choose normal buy/sell trades. The system produced 7.5M agent invocations, roughly 300K onchain actions, about $20M in volume, more than 5,000 ETH deployed, roughly 70B inference tokens, and 99.9% settlement success for policy-valid submitted transactions. Long-running agents accumulated thousands of sequential decisions, including 6,000+ prompt-state-action cycles for continuously active agents, yielding a large-scale trace from user mandate to rendered prompt, reasoning, validation, portfolio state, and settlement. Reliability did not come from the base model alone; it emerged from the operating layer around the model: prompt compilation, typed controls, policy validation, execution guards, memory design, and trace-level observability. Pre-launch testing exposed failu

## 4. Progressive Semantic Communication for Efficient Edge-Cloud Vision-Language Models
- Domain: arxiv.org
- URL: https://arxiv.org/abs/2604.26508
- Relevance score: 14.5
- Published: Thu, 30 Apr 2026 00:00:00 -0400
- Summary: arXiv:2604.26508v1 Announce Type: cross Abstract: Deploying Vision-Language Models (VLMs) on edge devices remains challenging due to their substantial computational and memory demands, which exceed the capabilities of resource-constrained embedded platforms. Conversely, fully offloading inference to the cloud is often impractical in bandwidth-limited environments, where transmitting raw visual data introduces substantial latency overhead. While recent edge-cloud collaborative architectures attempt to partition VLM workloads across devices, they typically rely on transmitting fixed-size representations, lacking adaptability to dynamic network conditions and failing to fully exploit semantic redundancy. In this paper, we propose a progressive semantic communication framework for edge-cloud VLM inference, using a Meta AutoEncoder that compresses visual tokens into adaptive, progressively refinable representations, enabling plug-and-play deployment with off-the-shelf VLMs without additional fine-tuning. This design allows flexible transmission at different information levels, providing a controllable trade-off between communication cost and semantic fidelity. We implement a full end-to

## 5. A Systematic Comparison of Prompting and Multi-Agent Methods for LLM-based Stance Detection
- Domain: arxiv.org
- URL: https://arxiv.org/abs/2604.26319
- Relevance score: 14.0
- Published: Thu, 30 Apr 2026 00:00:00 -0400
- Summary: arXiv:2604.26319v1 Announce Type: new Abstract: Stance detection identifies the attitude of a text author toward a given target. Recent studies have explored various LLM-based strategies for this task, from zero-shot prompting to multi-agent debate. However, existing works differ in data splits, base models, and evaluation protocols, making fair comparison difficult. We conduct a systematic comparison that evaluates five methods across two categories -- prompt-based inference (Direct Prompting, Auto-CoT, StSQA) and agent-based debate (COLA, MPRF) -- on four datasets with 14 subtasks, using 15 LLMs from six model families with parameter sizes from 7B to 72B+. Our experiments yield several findings. First, on all models with complete results, the best prompt-based method outperforms the best agent-based method, while agent methods require 7 to 12 times more API calls per sample. Second, model scale has a larger impact on performance than method choice, with gains plateauing around 32B. Third, reasoning-enhanced models (DeepSeek-R1) do not consistently outperform general models of the same size on this task.

## 6. A Scoping Review of LLM-as-a-Judge in Healthcare and the MedJUDGE Framework
- Domain: arxiv.org
- URL: https://arxiv.org/abs/2604.25933
- Relevance score: 14.0
- Published: Thu, 30 Apr 2026 00:00:00 -0400
- Summary: arXiv:2604.25933v1 Announce Type: cross Abstract: As large language models (LLMs) increasingly generate and process clinical text, scalable evaluation has become critical. LLM-as-a-Judge (LaaJ), which uses LLMs to evaluate model outputs, offers a scalable alternative to costly expert review, but its healthcare adoption raises safety and bias concerns. We conducted a PRISMA-ScR scoping review of six databases (January 2020-January 2026), screening 11,727 studies and including 49. The landscape was dominated by evaluation and benchmarking applications (n=37, 75.5%), pointwise scoring (n=42, 85.7%), and GPT-family judges (n=36, 73.5%). Despite growing adoption, validation rigor was limited: among 36 studies with human involvement, the median number of expert validators was 3, while 13 (26.5%) used none. Risk of bias testing was absent in 36 studies (73.5%), only 1 (2.0%) examined demographic fairness, and none assessed temporal stability or patient context. Deployment remained limited, with 1 study (2.0%) reaching production and four (8.2%) prototype stage. Importantly, these gaps may interact: when judges and evaluated systems share training data or architectures, they may inherit si

## 7. A Practice of Post-Training on Llama-3 70B with Optimal Selection of Additional Language Mixture Ratio
- Domain: arxiv.org
- URL: https://arxiv.org/abs/2409.06624
- Relevance score: 14.0
- Published: Thu, 30 Apr 2026 00:00:00 -0400
- Summary: arXiv:2409.06624v4 Announce Type: replace Abstract: Large Language Models (LLM) often need to be Continual Pre-Trained (CPT) to obtain unfamiliar language skills or adapt to new domains. The huge training cost of CPT often asks for cautious choice of key hyper-parameters such as the mixture ratio of extra language or domain corpus. However, there is no systematic study that bridges the gap between the optimal mixture ratio and the actual model performance, and the gap between experimental scaling law and the actual deployment in the full model size. In this paper, we perform CPT on Llama-3 8B and 70B to enhance its Chinese ability. We study the optimal correlation between the Additional Language Mixture Ratio (ALMR) and the Learning Rate (LR) on the 8B size which directly indicates the optimal experimental setup. By thorough choice of hyper-parameter, and subsequent fine-tuning, the model capability is improved not only on the Chinese-related benchmark but also in some specific domains including math, coding, and emotional intelligence. We deploy the final 70B version of LLM on a real-life chat system which obtains satisfying performance.

## 8. MINOS: A Multimodal Evaluation Model for Bidirectional Generation Between Image and Text
- Domain: arxiv.org
- URL: https://arxiv.org/abs/2506.02494
- Relevance score: 14.0
- Published: Thu, 30 Apr 2026 00:00:00 -0400
- Summary: arXiv:2506.02494v2 Announce Type: replace Abstract: Evaluation is important for multimodal generation tasks, while traditional multimodal evaluation metrics suffer from several limitations. With the rapid progress of MLLMs, there is growing interest in applying MLLMs to build general evaluation systems. However, existing researches often simply collect large-scale evaluation data for training, while overlooking the quality of evaluation data. What's more, current proposed evaluation models often struggle to achieve consistently strong performance across both image-to-text (I2T) and text-to-image (T2I) tasks. In this paper, through rigorous quality control strategies, we construct a comprehensive multimodal evaluation dataset, Minos-57K, with evaluation samples across 15 datasets, for developing the multimodal evaluation model Minos with SFT and preference alignment training strategies. Notably, despite using less than half the scale of the training data of prior work, our model achieves state-of-the-art evaluation performance across 16 out-of-domain datasets covering both I2T and T2I tasks among all open-source multimodal evaluation models and remain competitive with closed-source 

## 9. SciMDR: Advancing Scientific Multimodal Document Reasoning
- Domain: arxiv.org
- URL: https://arxiv.org/abs/2603.12249
- Relevance score: 14.0
- Published: Thu, 30 Apr 2026 00:00:00 -0400
- Summary: arXiv:2603.12249v2 Announce Type: replace Abstract: Constructing scientific multimodal document reasoning datasets for foundation model training involves an inherent trade-off among scale, faithfulness, and realism. To address this challenge, we introduce the synthesize-and-reground framework, a two-stage pipeline comprising: (1) Claim-Centric QA Synthesis, which generates faithful, isolated QA pairs and reasoning on focused segments, and (2) Document-Scale Regrounding, which programmatically re-embeds these pairs into full-document tasks to ensure realistic complexity. Using this framework, we construct SciMDR, a large-scale training dataset for cross-modal comprehension, comprising 300K QA pairs with explicit reasoning chains across 20K scientific papers. We further construct SciMDR-Eval, an expert-annotated benchmark to evaluate multimodal comprehension within full-length scientific workflows. Experiments demonstrate that models fine-tuned on SciMDR achieve significant improvements across multiple scientific QA benchmarks, particularly in those tasks requiring complex document-level reasoning.

## 10. Parallel Web Systems Raises $100 Million for Agentic AI Efforts
- Domain: pymnts.com
- URL: https://www.pymnts.com/artificial-intelligence-2/2026/parallel-web-systems-raises-100-million-for-agentic-ai-efforts/
- Relevance score: 10.0
- Published: Wed, 29 Apr 2026 18:52:24 +0000
- Summary: <p>Parallel Web Systems, an AI startup launched by Twitter’s ex-CEO, has raised $100 million. The company said its Series A round, announced Wednesday (April 29), values Parallel at $740 million and will allow it to focus on building products designed around the notion of artificial intelligence (AI) as the “second user” of the internet. [&#8230;]</p> <p>The post <a href="https://www.pymnts.com/artificial-intelligence-2/2026/parallel-web-systems-raises-100-million-for-agentic-ai-efforts/">Parallel Web Systems Raises $100 Million for Agentic AI Efforts</a> appeared first on <a href="https://www.pymnts.com">PYMNTS.com</a>.</p>

## 11. Ant International serves 150m merchants, 2b consumers, bets on AI commerce infrastructure
- Domain: scmp.com
- URL: https://www.scmp.com/tech/big-tech/article/3351926/ant-international-serves-150m-merchants-2b-consumers-bets-ai-commerce-infrastructure
- Relevance score: 9.8
- Published: Thu, 30 Apr 2026 01:31:25 +0000
- Summary: Ant International, the overseas spin-off of Chinese fintech giant Ant Group, has connected more than 150 million merchants with over 2 billion consumer accounts around the world, as it positions its payments network as core infrastructure for the emerging AI commerce economy. The figures, disclosed at the company’s MoMents 2026 forum in Kuala Lumpur, which ran from Monday to Wednesday, underscore the scale Ant is seeking to leverage amid the rising adoption of artificial intelligence agents. Ant...

## 12. GPT-5.5 is OpenAI’s most capable agentic AI model yet
- Domain: artificialintelligence-news.com
- URL: https://www.artificialintelligence-news.com/news/gpt-5-5-is-openais-most-capable-agentic-ai-model-yet-at-twice-the-api-price/
- Relevance score: 9.7
- Published: Wed, 29 Apr 2026 09:08:13 +0000
- Summary: <p>OpenAI launched GPT-5.5 on April 23 as what it calls &#8220;a new class of intelligence for real work and powering agents,&#8221; and the framing is deliberate. OpenAI says it&#8217;s the most capable agentic AI model to date, built from the ground up to plan, use tools, check its own output, and work through tasks independently. [&#8230;]</p> <p>The post <a href="https://www.artificialintelligence-news.com/news/gpt-5-5-is-openais-most-capable-agentic-ai-model-yet-at-twice-the-api-price/">GPT-5.5 is OpenAI&#8217;s most capable agentic AI model yet</a> appeared first on <a href="https://www.artificialintelligence-news.com">AI News</a>.</p>

## 13. The Zig project's rationale for their firm anti-AI contribution policy
- Domain: simonwillison.net
- URL: https://simonwillison.net/2026/Apr/30/zig-anti-ai/
- Relevance score: 9.2
- Published: 2026-04-30T01:24:23+00:00
- Summary: <p><a href="https://ziglang.org/">Zig</a> has one of the most stringent <a href="https://ziglang.org/code-of-conduct/">anti-LLM policies</a> of any major open source project:</p> <blockquote> <p>No LLMs for issues.</p> <p>No LLMs for pull requests.</p> <p>No LLMs for comments on the bug tracker, including translation. English is encouraged, but not required. You are welcome to post in your native language and rely on others to have their own translation tools of choice to interpret your words.</p> </blockquote> <p>The most prominent project written in Zig may be the <a href="https://bun.com/">Bun</a> JavaScript runtime, which was <a href="https://bun.com/blog/bun-joins-anthropic">acquired by Anthropic</a> in December 2025 and, unsurprisingly, makes heavy use of AI assistance.</p> <p>Bun operates its own fork of Zig, and recently <a href="https://x.com/bunjavascript/status/2048427636414923250">achieved a 4x performance improvement</a> on Bun compile after adding "parallel semantic analysis and multiple codegen units to the llvm backend". Here's <a href="https://github.com/oven-sh/zig/compare/upgrade-0.15.2%E2%80%A6upgrade-0.15.2-fast">that code</a>. But <a href="https://twitter.com/

## 14. 氪星晚报 ｜腾讯ima推出全新知识Agent——copilot；魔法原子：目标到2036年营收达140亿美元
- Domain: 36kr.com
- URL: https://36kr.com/p/3787748082293766
- Relevance score: 9.2
- Published: 2026-04-29 20:44:39  +0800
- Summary: <h2>大公司：</h2> <p><strong>魔法原子：目标到2036年营收达140亿美元</strong></p> <p>36氪获悉，美西时间4月28日，魔法原子在硅谷举办全球具身智能创新大会（GEIS）落幕。会上发布自研世界模型Magic-Mix、灵巧手MagicHand H01及旗舰人形机器人MagicBot X1。大会上，公司首次对外披露魔法原子的长期营收目标：到2036年，公司将向140亿美元营收规模迈进，并宣布未来五年将持续投入10亿美元，打造面向机器人二次开发的专属生态。</p> <p><strong>吉利汽车：第一季度营收首破800亿元，核心归母净利润同比增长31%</strong></p> <p>36氪获悉，吉利汽车公布2026年第一季度业绩报告。2026第一季度，录得总销量709358辆，同比增长1%。受益于出口销量的强劲增长及高价值产品销售占比提升，本集团期内收入同比增长15%；核心归母净利润45.6亿元，同比增长31%；当期毛利率17.5%，同比提升11%。截至2026年一季度末，公司总现金水平达602亿元</p> <p><strong>掌阅科技：2026年将全面推进AI短剧工业化布局</strong></p> <p>掌阅科技在2025年年度业绩说明会上表示，2026年公司将全面推进AI短剧工业化布局，实现内容生态规模化突破；显著加大资源投入力度，加码海外市场战略布局。在国内市场，AI短剧的成本结构将显著发生变化；海外市场流量渠道相对多元，公司将大力推动数字阅读、精品短剧、AI漫剧等多内容形态协同出海，搭建覆盖多语种、多区域的全球化内容生产与分发体系。（证券时报）</p> <p><strong>中国人寿：一季度净利润195亿元，同比下降32.3%</strong></p> <p>36氪获悉，中国人寿披露一季报，公司2026年一季度实现营业收入932.91亿元，同比下降15.3%；归属于母公司股东的净利润195.05亿元，同比下降32.3%。</p> <p><strong>中国中车：一季度净利润33.78亿元，同比增长10.66%</strong></p> <p>36氪获悉，中国中车披露一季报，公司2026年一季度实现营业收入538.19亿元，同比增长10.57%；归属于上市公司股东的净利润33.78亿元，同比增长10.66%。</p> <p><strong>三六零：一季度净利润1.09亿元，同比扭亏为盈</strong></p> <p>36氪获悉，三六零披露一季报，公司2026年一季度实现营业收入20.11亿元，同比增长7.9%；归属于上市公司股东的净利润1.09亿元，同比扭亏为盈。</p> <p><strong>赣锋锂业：一季度净利润18.37亿元，同比扭亏为盈</strong></p> <p>36氪获悉，赣锋锂业披露一季报，公

## 15. BlackRock and Vanguard Show the AI Edge Starts With Clean Data
- Domain: pymnts.com
- URL: https://www.pymnts.com/artificial-intelligence-2/2026/blackrock-and-vanguard-show-the-ai-edge-starts-with-clean-data/
- Relevance score: 9.0
- Published: Wed, 29 Apr 2026 19:30:47 +0000
- Summary: <p>Vanguard works with tens of thousands of financial advisors, and each one wants guidance tailored to their clients. For years, that meant human analysts working through portfolios one at a time, a model that’s hard to scale. The answer: Vanguard launched Expert Insights, a new artificial intelligence tool that takes a client’s holdings and [&#8230;]</p> <p>The post <a href="https://www.pymnts.com/artificial-intelligence-2/2026/blackrock-and-vanguard-show-the-ai-edge-starts-with-clean-data/">BlackRock and Vanguard Show the AI Edge Starts With Clean Data</a> appeared first on <a href="https://www.pymnts.com">PYMNTS.com</a>.</p>

## 16. Tech Week Shanghai founding edition to connect global tech players with China’s data ecosystem
- Domain: technode.com
- URL: https://technode.com/2026/04/30/tech-week-shanghai-founding-edition-to-connect-global-tech-players-with-chinas-data-ecosystem/
- Relevance score: 9.0
- Published: Thu, 30 Apr 2026 05:32:29 +0000
- Summary: <figure><img alt="" class="attachment-rss-image-size size-rss-image-size wp-post-image" height="576" src="https://i0.wp.com/technode.com/wp-content/uploads/2026/04/Tech-Week-Shanghai-Banner-1.png?fit=1024%2C576&amp;ssl=1" width="1024" /></figure>Tech Week Shanghai is set to make its debut in Shanghai on May 6 and 7, bringing together enterprise technology leaders, exhibitors, policymakers and industry practitioners across cloud computing, cybersecurity, data center infrastructure, data governance, data services, artificial intelligence and enterprise digital transformation. At a glance The conference and exhibition marks the founding edition of [&#8230;]

## 17. White House Crafts Plan to Bring Anthropic Back Into Government Fold
- Domain: pymnts.com
- URL: https://www.pymnts.com/artificial-intelligence-2/2026/white-house-crafts-plan-to-bring-anthropic-back-into-government-fold/
- Relevance score: 9.0
- Published: Thu, 30 Apr 2026 01:29:35 +0000
- Summary: <p>The White House is working on a way to allow federal agencies to use new artificial intelligence models from Anthropic, sidestepping the supply chain risk designation it placed on the AI startup, Axios reported Wednesday (April 29), citing unnamed sources. The administration is drafting an execution action that could reverse the Office of Management [&#8230;]</p> <p>The post <a href="https://www.pymnts.com/artificial-intelligence-2/2026/white-house-crafts-plan-to-bring-anthropic-back-into-government-fold/">White House Crafts Plan to Bring Anthropic Back Into Government Fold</a> appeared first on <a href="https://www.pymnts.com">PYMNTS.com</a>.</p>

## 18. AI chip designer Cambricon vaults to China’s costliest stock after profits soar 185%
- Domain: scmp.com
- URL: https://www.scmp.com/tech/article/3351894/revenue-jumps-chinas-cambricon-metax-amid-thirst-domestic-ai-chips
- Relevance score: 8.8
- Published: Wed, 29 Apr 2026 13:15:23 +0000
- Summary: Cambricon Technologies, dubbed “China’s little Nvidia,” on Thursday became the costliest stock in mainland China’s equities market after it reported substantial growth in the first quarter amid an artificial intelligence boom and China’s tech self-sufficiency push. Cambricon shares rose as much as 18 per cent to nearly 1,680 yuan (US$245) on Thursday, beating optical chipmaker Yuanjie Semiconductor Technology, which traded at around 1,660 yuan. On Wednesday, Cambricon announced a 160 per cent...

## 19. Cata raises US$5.3M to bring enterprise app tech to F&B and retail operators
- Domain: e27.co
- URL: https://e27.co/cata-raises-us5-3m-to-bring-enterprise-app-tech-to-fb-and-retail-operators-20260424/
- Relevance score: 8.7
- Published: Wed, 29 Apr 2026 02:00:15 +0000
- Summary: <p>Cata, a consumer app platform for food and beverage and retail operators, has raised US$5.3 million in seed funding less than a year after launch, as the company moves to bring enterprise-level digital capabilities to businesses that have historically been locked out of such tech. The oversubscribed round was led by global fintech investor Portage, [&#8230;]</p> <p>The post <a href="https://e27.co/cata-raises-us5-3m-to-bring-enterprise-app-tech-to-fb-and-retail-operators-20260424/">Cata raises US$5.3M to bring enterprise app tech to F&#038;B and retail operators</a> appeared first on <a href="https://e27.co">e27</a>.</p>

## 20. The evolution of encoders: From simple models to multimodal AI
- Domain: artificialintelligence-news.com
- URL: https://www.artificialintelligence-news.com/news/the-evolution-of-encoders-from-simple-models-to-multimodal-ai/
- Relevance score: 8.7
- Published: Tue, 28 Apr 2026 13:01:51 +0000
- Summary: <p>When people talk about artificial intelligence, they usually focus on what it produces: Human-like text, stunning images, or eerily accurate recommendations. What rarely gets attention is how AI understands anything in the first place. That understanding begins with encoders. Think of an encoder as a translator that converts messy, real-world information into a structured language [&#8230;]</p> <p>The post <a href="https://www.artificialintelligence-news.com/news/the-evolution-of-encoders-from-simple-models-to-multimodal-ai/">The evolution of encoders: From simple models to multimodal AI</a> appeared first on <a href="https://www.artificialintelligence-news.com">AI News</a>.</p>

## 21. Lightelligence’s 400% debut is a bet that AI’s next bottleneck is the optical interconnect
- Domain: artificialintelligence-news.com
- URL: https://www.artificialintelligence-news.com/news/lightelligence-ipo-optical-interconnect-ai-infrastructure/
- Relevance score: 8.7
- Published: Tue, 28 Apr 2026 10:00:00 +0000
- Summary: <p>When a company with US$15.5 million in annual revenue debuts on a stock exchange and its market capitalisation briefly hits US$10 billion, the obvious question is: what do investors know that the financials don&#8217;t show yet? In Lightelligence&#8217;s case, the answer is optical interconnect and the growing conviction that conventional copper wiring between AI chips [&#8230;]</p> <p>The post <a href="https://www.artificialintelligence-news.com/news/lightelligence-ipo-optical-interconnect-ai-infrastructure/">Lightelligence&#8217;s 400% debut is a bet that AI&#8217;s next bottleneck is the optical interconnect</a> appeared first on <a href="https://www.artificialintelligence-news.com">AI News</a>.</p>

## 22. IBM Launches AI and Quantum Hubs in Illinois and Massachusetts
- Domain: pymnts.com
- URL: https://www.pymnts.com/artificial-intelligence-2/2026/ibm-launches-ai-and-quantum-hubs-in-illinois-and-massachusetts/
- Relevance score: 8.5
- Published: Wed, 29 Apr 2026 23:37:46 +0000
- Summary: <p>IBM has announced two new hubs at which it will work on artificial intelligence and quantum computing. In Chicago, IBM plans to create 750 full-time jobs in AI, cybersecurity, data science, quantum and other fields at the Illinois Quantum and Microelectronics Park (IQMP), according to a press release issued Wednesday (April 29) by the [&#8230;]</p> <p>The post <a href="https://www.pymnts.com/artificial-intelligence-2/2026/ibm-launches-ai-and-quantum-hubs-in-illinois-and-massachusetts/">IBM Launches AI and Quantum Hubs in Illinois and Massachusetts</a> appeared first on <a href="https://www.pymnts.com">PYMNTS.com</a>.</p>

## 23. Colby Adcock’s Scout AI raises $100M to train its models for war: We visited its bootcamp
- Domain: techcrunch.com
- URL: https://techcrunch.com/2026/04/29/coby-adcocks-scout-ai-raises-100-million-to-train-models-for-war-we-visited-its-bootcamp/
- Relevance score: 8.5
- Published: Wed, 29 Apr 2026 09:45:00 +0000
- Summary: We visited Scout AI's training ground where it's working on AI agents that can help individual soldiers control fleets of autonomous vehicles.

## 24. AI Spending Drives Business Equipment Investment to 6-Year High
- Domain: pymnts.com
- URL: https://www.pymnts.com/artificial-intelligence-2/2026/ai-spending-drives-business-equipment-investment-to-6-year-high/
- Relevance score: 8.5
- Published: Thu, 30 Apr 2026 01:47:30 +0000
- Summary: <p>The boom in artificial intelligence products and infrastructure drove a closely watched measure of business spending to a six-year high in March. New orders for nondefense capital goods, excluding aircraft, rose 3.3% in March, accelerating from the increase of 1.6% in February, the Census Bureau reported Wednesday (April 29). This metric, dubbed “core capital [&#8230;]</p> <p>The post <a href="https://www.pymnts.com/artificial-intelligence-2/2026/ai-spending-drives-business-equipment-investment-to-6-year-high/">AI Spending Drives Business Equipment Investment to 6-Year High</a> appeared first on <a href="https://www.pymnts.com">PYMNTS.com</a>.</p>

## 25. Singapore AI design startup FORMAS.AI raises US$3.98M in oversubscribed pre-seed round
- Domain: e27.co
- URL: https://e27.co/singapore-ai-design-startup-formas-ai-raises-us3-98m-in-oversubscribed-pre-seed-round-20260429/
- Relevance score: 8.2
- Published: Wed, 29 Apr 2026 03:32:37 +0000
- Summary: <p>FORMAS.AI, an AI-native design workspace for the architecture, engineering, and construction (AEC) sector, has closed a US$3.98 million pre-seed funding round, which was oversubscribed amid strong investor appetite for AI tools targeting the built environment. Vertex Ventures Southeast Asia &#38; India led the round, with participation from UntroD Capital, Hustle Fund, Big Sky Capital, and [&#8230;]</p> <p>The post <a href="https://e27.co/singapore-ai-design-startup-formas-ai-raises-us3-98m-in-oversubscribed-pre-seed-round-20260429/">Singapore AI design startup FORMAS.AI raises US$3.98M in oversubscribed pre-seed round</a> appeared first on <a href="https://e27.co">e27</a>.</p>

## 26. 别急着All-in DeepSeek V4，先看看这10位从业者的真心话
- Domain: 36kr.com
- URL: https://36kr.com/p/3788151000751364
- Relevance score: 8.2
- Published: 2026-04-30 01:07:22  +0800
- Summary: <p><strong>文｜周鑫雨 王毓婵</strong></p> <p><strong>编辑｜杨轩</strong></p> <p>解读DeepSeek V4的技术报告，是这几天AI行业最狂热的集体活动。</p> <p>V4很强吗？在工程优化的维度中，答案是毋庸置疑的。过去，大家信奉“Scaling Law的暴力美学”——也就是靠堆更多优质算力、更大参数规模来提升模型性能。而V4走的是一条完全不同的路，它定义了一种“模型训练的克制美学”：</p> <p>它不靠疯狂堆算力和参数，而是通过一系列组合优化和重构：</p> <p><strong>注意力机制</strong>（让模型学会“抓重点”，像人读长文章时会自动关注关键句子一样）</p> <p><strong>MoE架构（混合专家模型，可以理解为“让不同的专家负责不同类型的问题，每次只激活少数专家，省时又省力”）</strong></p> <p><strong>后训练</strong>（模型初步练成后再针对性地补课强化）</p> <p><strong>推理系统工程</strong>（优化实际运行时各个环节的效率）</p> <p>这样做的成果是把V4-Pro在处理百万Token（大约几十万字）长上下文时需要的算力，压低到了上一代V3.2的27%，同时用来临时存储对话上下文的<strong>KV缓存</strong>（可以理解为模型在跟你聊天时“记笔记”的草稿纸）被压缩到了原来的10%。</p> <p>不过，工程只是工程，榜单只是榜单。</p> <p>评价一个模型，我们不希望只停留在纸面参数上，而是放到部署、开发、投资的真实场景中去讨论V4的价值。为此，我们邀请了近10名开发者、应用创业者和投资人，进行了三天左右的体验和测试。</p> <p>先说一个反直觉的结论：DeepSeek对应用层带来的影响，或许比模型层更大。</p> <p>在惊叹极致的工程优化之余，正如DeepSeek自己在V4技术报告中坦言的那样：发展轨迹大约滞后前沿闭源模型3至6个月——V4如今的成果，就好比<strong>与魔鬼做交易：</strong>拉长了推理和Agent（智能体）能力的长板，代价是牺牲了部分准确性。</p> <p>闭源模型厂商们，暂时可以松一口气。对于注重稳定、精确的商业世界而言，V4显然不是一款能够直接落地的模型。</p> <p>Pine AI首席科学家李博杰，以及某头部Coding Agent创业者Chillin都对我们直言，工具调用稳定性+幻觉率，这两点必须在harness（给智能体套上的“缰绳”和“安全带”，用来规范它的行为、降低出错风险）层面补足，V4落地离不开“脚手架”。</p> <p>但智力大脑的迭代方向，往往牵动着下游应用的生态。AI应用创业，将会面对技术和资本更严厉的双重考验。</p> <p>“基模的性能还在

## 27. Yet another experiment proves it's too damn simple to poison large language models
- Domain: go.theregister.com
- URL: https://go.theregister.com/feed/www.theregister.com/2026/04/29/poisoning_large_language_models_6nimmt/
- Relevance score: 8.2
- Published: 2026-04-29T17:00:18.00Z
- Summary: <h4>There is no 6 Nimmt! champion, but a $12 domain registration and one Wikipedia edit convinced several bots there was</h4> <p>Unlike search engines that let you judge competing sources, search-backed AI chatbots can turn shaky web material into confident answers. Case in point: A security engineer convinced several bots that he was the reigning world champion of a popular German card game, even though no such championship exists.…</p> <p><!--#include virtual='/data_centre/_whitepaper_textlinks_top.html' --></p>

## 28. OpenAI jumps out of Microsoft's bed, into Amazon's Bedrock
- Domain: go.theregister.com
- URL: https://go.theregister.com/feed/www.theregister.com/2026/04/28/openai_climbs_into_amazons_bedrock/
- Relevance score: 8.2
- Published: 2026-04-28T19:21:50.00Z
- Summary: <h4>Altman's gaggle of GPTs now available in limited preview in an AWS region near you</h4> <p>OpenAI's top models are officially available on Amazon Web Services' Bedrock managed inference and agent platform.…</p>

## 29. OpenAI Disputes Growth Worries Amid Subscription Changes
- Domain: pymnts.com
- URL: https://www.pymnts.com/artificial-intelligence-2/2026/openai-disputes-growth-worries-amid-subscription-changes/
- Relevance score: 8.0
- Published: Wed, 29 Apr 2026 16:05:40 +0000
- Summary: <p>OpenAI is reportedly fighting back against reports of concerns about the artificial intelligence (AI) startup’s growth. The company told Bloomberg News Tuesday (April 28) that it is “firing on all cylinders” despite a report that said it had missed internal targets, and that it is still seeing growing demand from business customers and its [&#8230;]</p> <p>The post <a href="https://www.pymnts.com/artificial-intelligence-2/2026/openai-disputes-growth-worries-amid-subscription-changes/">OpenAI Disputes Growth Worries Amid Subscription Changes</a> appeared first on <a href="https://www.pymnts.com">PYMNTS.com</a>.</p>

## 30. Introducing AutoSP
- Domain: pytorch.org
- URL: https://pytorch.org/blog/introducing-autosp/
- Relevance score: 8.0
- Published: Wed, 29 Apr 2026 15:25:24 +0000
- Summary: ¹ SSAIL Lab, University of Illinois Urbana-Champaign, ² Anyscale, ³ Snowflake TL;DR: AutoSP automatically converts standard transformer training code into sequence-parallel code for long-context LLM training across multiple GPUs. Integrated...

## 31. Italy Edge Artificial Intelligence Chips - Market Analysis, Forecast, Size, Trends and Insights - IndexBox
- Domain: indexbox.io
- URL: https://news.google.com/rss/articles/CBMivgFBVV95cUxOckdsYkdycGJjZG85TlBnTjZlUnhTYWVBai1tTkNoa0lqRUZNVVYxbFkyUDNGS2ttX2EwYTNNRE9jM0RvS0VNZFFxSHFQWmtNUGNYTlp2RnVEREVoWWltc29xUzBMTS1oYnp1MHZOeHRramVEamNkUTdtRkdqUDZvQlZQeE1DSWJHY0ZzMUtlRVNTcEV1Sm1QZkltZWdGMGhKRV9BeWdFZTZOR2ZITERMOHFNOGM0SnczM1dyeGZB
- Relevance score: 8.0
- Published: Wed, 29 Apr 2026 12:20:12 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMivgFBVV95cUxOckdsYkdycGJjZG85TlBnTjZlUnhTYWVBai1tTkNoa0lqRUZNVVYxbFkyUDNGS2ttX2EwYTNNRE9jM0RvS0VNZFFxSHFQWmtNUGNYTlp2RnVEREVoWWltc29xUzBMTS1oYnp1MHZOeHRramVEamNkUTdtRkdqUDZvQlZQeE1DSWJHY0ZzMUtlRVNTcEV1Sm1QZkltZWdGMGhKRV9BeWdFZTZOR2ZITERMOHFNOGM0SnczM1dyeGZB?oc=5" target="_blank">Italy Edge Artificial Intelligence Chips - Market Analysis, Forecast, Size, Trends and Insights</a>&nbsp;&nbsp;<font color="#6f6f6f">IndexBox</font>

## 32. Ex-Twitter CEO Parag Agrawal's AI Startup Hits $2B Valuation With $100M Funding - NDTV Profit
- Domain: ndtvprofit.com
- URL: https://news.google.com/rss/articles/CBMivgFBVV95cUxOR0NHbHlVdk1XWmZmQVBRT2xqejlOLS0tQlBUM2g2XzNYVE1veUw3cVpVbVNsTnNIb2thNzczRVo5alM2UUlUZGRRSFhHVEwyRmM0T3JpYnQ5S1pWUklPaEVheWNPeWx2X01JNHlBSWtnb1Ywam5GX1l6bEtYWENsVjRIN3FUb3FRUnQ1emItcWNwSXU4eUJmVlBCaFpNeDRocFFTZm8tc05hQ3h3Y2Z3UURoY1UxaVRXSkJCc2Zn0gHGAUFVX3lxTE9FbUI2bFZBNDBaNlh6azE0anVxcHdFS1YxTVpjZXNPZkVOaElGRVE5MmRqVUltd1QxS25DbWs0dkRBdEJNb21QY0hDNy1FSUk5LUphZTFvREI5VzNaekx6SFhBUVVHNng3cmVLLTRvVHN6bEdmTWl0RDF4YXRQQUFjX1paQ3ZRVG1acnVJOVplMkNEQVd4TXFGVzdscmJDRGxSMjhJTE1CN3gxUzFlN3hRbFRaaUxMSnN0VkM0Z0NwZHBtZnd5dw
- Relevance score: 8.0
- Published: Wed, 29 Apr 2026 10:39:45 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMivgFBVV95cUxOR0NHbHlVdk1XWmZmQVBRT2xqejlOLS0tQlBUM2g2XzNYVE1veUw3cVpVbVNsTnNIb2thNzczRVo5alM2UUlUZGRRSFhHVEwyRmM0T3JpYnQ5S1pWUklPaEVheWNPeWx2X01JNHlBSWtnb1Ywam5GX1l6bEtYWENsVjRIN3FUb3FRUnQ1emItcWNwSXU4eUJmVlBCaFpNeDRocFFTZm8tc05hQ3h3Y2Z3UURoY1UxaVRXSkJCc2Zn0gHGAUFVX3lxTE9FbUI2bFZBNDBaNlh6azE0anVxcHdFS1YxTVpjZXNPZkVOaElGRVE5MmRqVUltd1QxS25DbWs0dkRBdEJNb21QY0hDNy1FSUk5LUphZTFvREI5VzNaekx6SFhBUVVHNng3cmVLLTRvVHN6bEdmTWl0RDF4YXRQQUFjX1paQ3ZRVG1acnVJOVplMkNEQVd4TXFGVzdscmJDRGxSMjhJTE1CN3gxUzFlN3hRbFRaaUxMSnN0VkM0Z0NwZHBtZnd5dw?oc=5" target="_blank">Ex-Twitter CEO Parag Agrawal's AI Startup Hits $2B Valuation With $100M Funding</a>&nbsp;&nbsp;<font color="#6f6f6f">NDTV Profit</font>

## 33. Surging artificial intelligence data usage reshaping economy - China Daily
- Domain: chinadaily.com.cn
- URL: https://news.google.com/rss/articles/CBMifkFVX3lxTE5RdU5XNmFQY0pIWjZ2NDZKRXNBQ0R2cmdxY0tjX3NFaXQyLXVFMkRFeWk1ODlwT3lKemVZbFRIOWV2bXBfb3RzMm9yMU85V2VFVWdlT3lGS3laVkJ2WUhnNEZiYzVPX19VZUttQWNMZm1ERzhjd1F0SC1EanB6dw
- Relevance score: 8.0
- Published: Thu, 30 Apr 2026 01:07:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMifkFVX3lxTE5RdU5XNmFQY0pIWjZ2NDZKRXNBQ0R2cmdxY0tjX3NFaXQyLXVFMkRFeWk1ODlwT3lKemVZbFRIOWV2bXBfb3RzMm9yMU85V2VFVWdlT3lGS3laVkJ2WUhnNEZiYzVPX19VZUttQWNMZm1ERzhjd1F0SC1EanB6dw?oc=5" target="_blank">Surging artificial intelligence data usage reshaping economy</a>&nbsp;&nbsp;<font color="#6f6f6f">China Daily</font>

## 34. Bernie Sanders urges international cooperation to halt AI’s ‘runaway train’
- Domain: theguardian.com
- URL: https://www.theguardian.com/us-news/2026/apr/29/bernie-sanders-ai-panel
- Relevance score: 8.0
- Published: Thu, 30 Apr 2026 01:01:09 GMT
- Summary: <p>US senator holds panel with leading Chinese scientists and warns of risks to society unless new technology is regulated </p><p>The US senator Bernie Sanders espoused the importance of international cooperation in regulating AI at a Wednesday panel on Capitol Hill alongside two leading Chinese scientists.</p><p>As startups and tech giants, most prominently in Silicon Valley and Beijing, race to advance and scale their artificial intelligence, Sanders has been among the AI skeptics advocating for safeguards.</p> <a href="https://www.theguardian.com/us-news/2026/apr/29/bernie-sanders-ai-panel">Continue reading...</a>

## 35. DeepSeek adds AI vision in major move: ‘the whale can now see’
- Domain: scmp.com
- URL: https://www.scmp.com/tech/tech-trends/article/3351892/whale-can-now-see-deepseek-adds-ai-vision-major-move
- Relevance score: 7.8
- Published: Wed, 29 Apr 2026 14:00:12 +0000
- Summary: Chinese artificial intelligence start-up DeepSeek has added multimodal capabilities to its flagship chatbot for the first time – meaning that it can process images and video in addition to text – bringing it in line with rivals that already offer the function. The limited release to select users comes just days after the Hangzhou-based company released its new flagship model V4, which was followed by extensive price cuts. According to DeepSeek multimodal team leader Chen Xiaokang, who made the...

## 36. Hit from memory costs spreads from phones to EVs as China’s BYD raises driving-tech price
- Domain: scmp.com
- URL: https://www.scmp.com/tech/article/3351842/hit-memory-costs-spreads-phones-evs-chinas-byd-raises-driving-tech-price
- Relevance score: 7.8
- Published: Wed, 29 Apr 2026 12:30:11 +0000
- Summary: The impact of sky-high costs for memory chips is spreading from smartphones to cars, as China’s electric vehicle (EV) king BYD announced a 21 per cent price increase for its high-end driver-assistance system. Starting on Friday, the price of the optional DiPilot 300 assisted-driving system would rise to 12,000 yuan ($1,757) from 9,900 yuan, BYD said on Tuesday, attributing the decision to “the sharp rise in global storage hardware costs”. The system, which allows cars to navigate themselves on...

## 37. With Nemotron 3 Nano Omni, Nvidia reveals what really goes into a modern multimodal model
- Domain: the-decoder.com
- URL: https://the-decoder.com/with-nemotron-3-nano-omni-nvidia-reveals-what-really-goes-into-a-modern-multimodal-model/
- Relevance score: 7.8
- Published: Wed, 29 Apr 2026 09:28:29 +0000
- Summary: <p><img alt="" class="attachment-full size-full wp-post-image" height="680" src="https://the-decoder.com/wp-content/uploads/2025/12/Nvidia-nemotron-3-release.jpg" style="height: auto; margin-bottom: 10px;" width="1280" /></p> <p> Nvidia releases Nemotron 3 Nano Omni, an open multimodal model for text, image, video and audio. Not only the performance is exciting, but also a look at the training data: it comes from Qwen, GPT-OSS, Kimi and DeepSeek OCR, among others.</p> <p>The article <a href="https://the-decoder.com/with-nemotron-3-nano-omni-nvidia-reveals-what-really-goes-into-a-modern-multimodal-model/">With Nemotron 3 Nano Omni, Nvidia reveals what really goes into a modern multimodal model</a> appeared first on <a href="https://the-decoder.com">The Decoder</a>.</p>

## 38. China’s Alibaba, ByteDance and Zhipu AI make the cut on Time’s first AI A-list
- Domain: scmp.com
- URL: https://www.scmp.com/tech/article/3351823/chinas-alibaba-bytedance-and-zhipu-ai-make-cut-times-first-ai-list
- Relevance score: 7.8
- Published: Wed, 29 Apr 2026 07:34:33 +0000
- Summary: Three Chinese companies – Alibaba Group Holding, ByteDance and Zhipu AI – have been named among Time magazine’s “10 Most Influential AI Companies of 2026”, marking the first time the publication has introduced an artificial intelligence-specific sub-list under its broader Time100 Most Influential Companies ranking. Of the remaining seven companies on the list, six are based in the US, while France’s Mistral AI is the only European representative. The launch of a dedicated AI ranking underscores...

## 39. China blocks Meta’s Manus deal, raises Mythos concerns
- Domain: scmp.com
- URL: https://www.scmp.com/plus/tech/big-tech/article/3351705/china-blocks-metas-manus-deal-raises-mythos-concerns
- Relevance score: 7.8
- Published: Tue, 28 Apr 2026 09:08:11 +0000
- Summary: China has stepped up its tech war with the United States, blocking Facebook owner Meta’s US$2.5 billion acquisition of artificial intelligence (AI) start-up Manus and raising cybersecurity concerns about Anthropic’s new AI model Claude Mythos Preview. The National Development and Reform Commission (NDRC) announced it was prohibiting the Manus deal in a one-sentence statement on Monday, which didn’t give a specific reason. Meta is now planning to unwind the acquisition, which means untangling...

## 40. Larry’s risky business
- Domain: theverge.com
- URL: https://www.theverge.com/ai-artificial-intelligence/920378/oracle-openai-datacenter-buildout
- Relevance score: 7.8
- Published: 2026-04-29T09:57:16-04:00
- Summary: If you want to know whether the AI bubble is bursting, there's only one publicly traded company that will tell you: Oracle. That's right, the database company. Oracle has burned its boats and pivoted to AI, but not in any kind of usual way. It is not a foundation model builder like OpenAI or Anthropic, [&#8230;]

## 41. From code to carbon: How Asia can harness AI agents without harming people or the planet
- Domain: e27.co
- URL: https://e27.co/from-code-to-carbon-how-asia-can-harness-ai-agents-without-harming-people-or-the-planet-20260428/
- Relevance score: 7.7
- Published: Wed, 29 Apr 2026 05:00:39 +0000
- Summary: <p>Across Asia, a quiet revolution is underway. Banks are piloting AI agents to triage customer queries. Manufacturers are wiring factories with autonomous “co‑pilots” that watch sensor data and adjust production lines in real time. Governments are experimenting with digital assistants to guide citizens through permits and benefits. These systems look like chatbots on the surface. [&#8230;]</p> <p>The post <a href="https://e27.co/from-code-to-carbon-how-asia-can-harness-ai-agents-without-harming-people-or-the-planet-20260428/">From code to carbon: How Asia can harness AI agents without harming people or the planet</a> appeared first on <a href="https://e27.co">e27</a>.</p>

## 42. The divided AI race nobody wins: How businesses can navigate the US-China tech divide
- Domain: e27.co
- URL: https://e27.co/the-divided-ai-race-nobody-wins-how-businesses-can-navigate-the-us-china-tech-divide-20260423/
- Relevance score: 7.7
- Published: Wed, 29 Apr 2026 02:17:03 +0000
- Summary: <p>We are in the midst of the most consequential technological shift in a generation, and the world is already splitting along familiar fault lines. The world’s two greatest powers are in a battle once again — and this time, the “battlefield” is artificial intelligence (AI). On one hand, the United States (US) is adopting an [&#8230;]</p> <p>The post <a href="https://e27.co/the-divided-ai-race-nobody-wins-how-businesses-can-navigate-the-us-china-tech-divide-20260423/">The divided AI race nobody wins: How businesses can navigate the US-China tech divide</a> appeared first on <a href="https://e27.co">e27</a>.</p>

## 43. Why startup founders shouldn’t trust an AI agent to replace a PR team
- Domain: e27.co
- URL: https://e27.co/why-startup-founders-shouldnt-trust-an-ai-agent-to-replace-a-pr-team-20260428/
- Relevance score: 7.7
- Published: Thu, 30 Apr 2026 05:00:15 +0000
- Summary: <p>One of our founder friends tried it. He really did. About six months into the AI wave, he sat down and did the math. Hiring a PR agency was too costly, factoring his startup stage and business operational expenses, so he figured now with Claude, ChatGPT, Perplexity, NotebookLM &#8211; tools that could theoretically do what [&#8230;]</p> <p>The post <a href="https://e27.co/why-startup-founders-shouldnt-trust-an-ai-agent-to-replace-a-pr-team-20260428/">Why startup founders shouldn&#8217;t trust an AI agent to replace a PR team</a> appeared first on <a href="https://e27.co">e27</a>.</p>

## 44. LLM 0.32a0 is a major backwards-compatible refactor
- Domain: simonwillison.net
- URL: https://simonwillison.net/2026/Apr/29/llm/
- Relevance score: 7.7
- Published: 2026-04-29T19:01:47+00:00
- Summary: <p>I just released <a href="https://llm.datasette.io/en/latest/changelog.html#a0-2026-04-28">LLM 0.32a0</a>, an alpha release of my <a href="https://llm.datasette.io/">LLM</a> Python library and CLI tool for accessing LLMs, with some consequential changes that I've been working towards for quite a while.</p> <p>Previous versions of LLM modeled the world in terms of prompts and responses. Send the model a text prompt, get back a text response.</p> <pre><span class="pl-k">import</span> <span class="pl-s1">llm</span> <span class="pl-s1">model</span> <span class="pl-c1">=</span> <span class="pl-s1">llm</span>.<span class="pl-c1">get_model</span>(<span class="pl-s">"gpt-5.5"</span>) <span class="pl-s1">response</span> <span class="pl-c1">=</span> <span class="pl-s1">model</span>.<span class="pl-c1">prompt</span>(<span class="pl-s">"Capital of France?"</span>) <span class="pl-en">print</span>(<span class="pl-s1">response</span>.<span class="pl-c1">text</span>())</pre> <p>This made sense when I started working on the library back in April 2023. A lot has changed since then!</p> <p>LLM provides an abstraction over thousands of different models via its <a href="https://llm.datasette.io/en/s

## 45. Claude AI agent’s confession after deleting a firm’s entire database: ‘I violated every principle I was given’
- Domain: theguardian.com
- URL: https://www.theguardian.com/technology/2026/apr/29/claude-ai-deletes-firm-database
- Relevance score: 7.5
- Published: Wed, 29 Apr 2026 22:12:49 GMT
- Summary: <p>PocketOS was left scrambling after a rogue AI agent deleted swaths of code underpinning its business</p><p>It only took nine seconds for an AI coding agent gone rogue to delete a company’s entire production database and its backups, according to its founder. PocketOS, which sells software that car rental businesses rely on, descended into chaos after its databases were wiped, the company’s founder Jeremy Crane said.</p><p>The culprit was Cursor, an AI agent powered by Anthropic’s Claude Opus 4.6 model, which is one of the AI industry’s flagship models. As more industries embrace <a href="https://www.theguardian.com/technology/2026/apr/06/tech-layoffs-ai-work">AI in an attempt to automate tasks and even replace workers</a>, the chaos at PocketOS is a reminder of what could go wrong.</p> <a href="https://www.theguardian.com/technology/2026/apr/29/claude-ai-deletes-firm-database">Continue reading...</a>

## 46. Stripe Brings Merchant Checkout to Google’s AI Apps
- Domain: pymnts.com
- URL: https://www.pymnts.com/artificial-intelligence-2/2026/stripe-scales-ai-economic-infrastructure-with-google-deal/
- Relevance score: 7.5
- Published: Wed, 29 Apr 2026 21:05:17 +0000
- Summary: <p>Stripe has partnered with Google to allow businesses to sell to consumers inside Google’s AI Mode and Gemini app. This capability is supported by Stripe’s Agentic Commerce Suite, an integration that enables businesses to sell their products inside AI apps, Stripe said in a Wednesday (April 29) press release. Stripe introduced its Agentic Commerce Suite in December, saying this solution is [&#8230;]</p> <p>The post <a href="https://www.pymnts.com/artificial-intelligence-2/2026/stripe-scales-ai-economic-infrastructure-with-google-deal/">Stripe Brings Merchant Checkout to Google’s AI Apps</a> appeared first on <a href="https://www.pymnts.com">PYMNTS.com</a>.</p>

## 47. 'I violated every principle I was given': AI agent deletes company's entire database in 9 seconds, then confesses - Live Science
- Domain: livescience.com
- URL: https://news.google.com/rss/articles/CBMigAJBVV95cUxQNnNESllfdEhiRDEydmd2VVBIelhrTmFqRjhsSEJzZGZMZGpuYXIzcUE0T1hMWWw1eFBJcTdXWU9BVS1GV0FKRmhqQmoxOU5tNjBWdEZ0MVhqcXNrMWtlRzNEek1IQXlHOF9MMlJMUEdwRjM2MUlQRlhkZUtxSkdJUDh4b1h4dk5yOUJZQ2Y0WFV2MXVmMTNhZHdtblVxMmprcm5jdWl4Rzd1MUtBQVdfY0VjRFI1a2NmUnRDTVRBTklWSW8yRnpqRHZOWi00am04dEplMlNQN0Y5TWpWTThSOE02YlVUd2tzMENLWHR3cm5VNGxIV1BJbG1sXzRsVlEw
- Relevance score: 7.5
- Published: Wed, 29 Apr 2026 14:57:54 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMigAJBVV95cUxQNnNESllfdEhiRDEydmd2VVBIelhrTmFqRjhsSEJzZGZMZGpuYXIzcUE0T1hMWWw1eFBJcTdXWU9BVS1GV0FKRmhqQmoxOU5tNjBWdEZ0MVhqcXNrMWtlRzNEek1IQXlHOF9MMlJMUEdwRjM2MUlQRlhkZUtxSkdJUDh4b1h4dk5yOUJZQ2Y0WFV2MXVmMTNhZHdtblVxMmprcm5jdWl4Rzd1MUtBQVdfY0VjRFI1a2NmUnRDTVRBTklWSW8yRnpqRHZOWi00am04dEplMlNQN0Y5TWpWTThSOE02YlVUd2tzMENLWHR3cm5VNGxIV1BJbG1sXzRsVlEw?oc=5" target="_blank">'I violated every principle I was given': AI agent deletes company's entire database in 9 seconds, then confesses</a>&nbsp;&nbsp;<font color="#6f6f6f">Live Science</font>

## 48. CCS Medical Deploys Enterprise Agentic AI Platform for Chronic Care Support - AIM Media House
- Domain: aimmediahouse.com
- URL: https://news.google.com/rss/articles/CBMiuAFBVV95cUxPbmhWOTZmeUJwYUIwRU1famJIZC1HMVc3a2F1THktVDJ4LXViaTV4YWphYlo4dXAxU0Ntcl9JTXJDY0lrcUlNeEhSZVljWGtsbmxHaTVDZDBFOW5wZGNTVTk5bUhrSlpKV3NXSjZMY3pmbU5sTlg0OEJ1Zl9RNXM1M2pVVURnVC14YTJLOXV5dkdpb3V6UHRwQlRiV08tdUhmNDgweEdiZ1k3dmxjUk5LcTBLWFk3dThz
- Relevance score: 7.5
- Published: Wed, 29 Apr 2026 10:44:14 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiuAFBVV95cUxPbmhWOTZmeUJwYUIwRU1famJIZC1HMVc3a2F1THktVDJ4LXViaTV4YWphYlo4dXAxU0Ntcl9JTXJDY0lrcUlNeEhSZVljWGtsbmxHaTVDZDBFOW5wZGNTVTk5bUhrSlpKV3NXSjZMY3pmbU5sTlg0OEJ1Zl9RNXM1M2pVVURnVC14YTJLOXV5dkdpb3V6UHRwQlRiV08tdUhmNDgweEdiZ1k3dmxjUk5LcTBLWFk3dThz?oc=5" target="_blank">CCS Medical Deploys Enterprise Agentic AI Platform for Chronic Care Support</a>&nbsp;&nbsp;<font color="#6f6f6f">AIM Media House</font>

## 49. A Coding Implementation on Document Parsing Benchmarking with LlamaIndex ParseBench Using Python, Hugging Face, and Evaluation Metrics
- Domain: marktechpost.com
- URL: https://www.marktechpost.com/2026/04/29/a-coding-implementation-on-document-parsing-benchmarking-with-llamaindex-parsebench-using-python-hugging-face-and-evaluation-metrics/
- Relevance score: 7.5
- Published: Wed, 29 Apr 2026 07:08:42 +0000
- Summary: <p>In this tutorial, we explore how to use the ParseBench dataset to evaluate document parsing systems in a structured, practical way. We begin by loading the dataset directly from Hugging Face, inspecting its multiple dimensions, such as text, tables, charts, and layout, and transforming it into a unified dataframe for deeper analysis. As we progress, [&#8230;]</p> <p>The post <a href="https://www.marktechpost.com/2026/04/29/a-coding-implementation-on-document-parsing-benchmarking-with-llamaindex-parsebench-using-python-hugging-face-and-evaluation-metrics/">A Coding Implementation on Document Parsing Benchmarking with LlamaIndex ParseBench Using Python, Hugging Face, and Evaluation Metrics</a> appeared first on <a href="https://www.marktechpost.com">MarkTechPost</a>.</p>

## 50. Exclusive: Big Chinese tech firms scramble to secure Huawei AI chips after DeepSeek V4 launch, sources say - Reuters
- Domain: reuters.com
- URL: https://news.google.com/rss/articles/CBMixgFBVV95cUxQb2k3eWk0STFfck5fbjZoWkMzRlg5OFRGR19BM0xXV3Vfb0dCX1NralZ2SDNVQ1RvU1Zpck1mVGhNT0FfRFIwcERIaFVmTHRJRTVRVlNOQlR1a0lyVE9iLW9OT0pYQTdZc3NqdVhPeTJhajhwWlJfZUpOeFdSZmd2M3QxZ2RraG12d2xFSkk1VXloOTNtSFJXS05wb3Y5Zk94VHJwQ2Z4d0V2X1BsbWlIWm1CVTBkYkVVS1hXSy1jR0JMVURZSmc
- Relevance score: 7.5
- Published: Wed, 29 Apr 2026 06:36:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMixgFBVV95cUxQb2k3eWk0STFfck5fbjZoWkMzRlg5OFRGR19BM0xXV3Vfb0dCX1NralZ2SDNVQ1RvU1Zpck1mVGhNT0FfRFIwcERIaFVmTHRJRTVRVlNOQlR1a0lyVE9iLW9OT0pYQTdZc3NqdVhPeTJhajhwWlJfZUpOeFdSZmd2M3QxZ2RraG12d2xFSkk1VXloOTNtSFJXS05wb3Y5Zk94VHJwQ2Z4d0V2X1BsbWlIWm1CVTBkYkVVS1hXSy1jR0JMVURZSmc?oc=5" target="_blank">Exclusive: Big Chinese tech firms scramble to secure Huawei AI chips after DeepSeek V4 launch, sources say</a>&nbsp;&nbsp;<font color="#6f6f6f">Reuters</font>

## 51. Gorilla Technology, Yotta expand India AI infra deal to $2.8 bn with 20,736 GPU deployment - Techcircle
- Domain: techcircle.in
- URL: https://news.google.com/rss/articles/CBMiygFBVV95cUxOUGJZbkkteWdKX2hncjRIZVBVRHRMYmVUQ1FWdlRJSW16TkRON18zelRPWkdVM0pfNElVV04zOEJBVlRTRFdGZk5YLTdGYy15MHR5d0F0TlNxclRSMTdyX1Q0anR1bHBrM1BEUVNmdU9kLWlKMmVfLVAzZTRtY3hfcUtFZmg3cHpaY0FLLXRpbDdESGsyY3ZJampGUXhKcDNiZnU4bEFmdE5vbldnSjdUNHFGdTltdDNtTU8yM20zVDNWZmx3WVNmTXJR
- Relevance score: 7.5
- Published: Thu, 30 Apr 2026 05:44:50 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiygFBVV95cUxOUGJZbkkteWdKX2hncjRIZVBVRHRMYmVUQ1FWdlRJSW16TkRON18zelRPWkdVM0pfNElVV04zOEJBVlRTRFdGZk5YLTdGYy15MHR5d0F0TlNxclRSMTdyX1Q0anR1bHBrM1BEUVNmdU9kLWlKMmVfLVAzZTRtY3hfcUtFZmg3cHpaY0FLLXRpbDdESGsyY3ZJampGUXhKcDNiZnU4bEFmdE5vbldnSjdUNHFGdTltdDNtTU8yM20zVDNWZmx3WVNmTXJR?oc=5" target="_blank">Gorilla Technology, Yotta expand India AI infra deal to $2.8 bn with 20,736 GPU deployment</a>&nbsp;&nbsp;<font color="#6f6f6f">Techcircle</font>

## 52. The interpretation gap: Why AI agents are moving faster than companies can understand
- Domain: e27.co
- URL: https://e27.co/the-interpretation-gap-why-ai-agents-are-moving-faster-than-companies-can-understand-20260424/
- Relevance score: 7.2
- Published: Wed, 29 Apr 2026 02:32:49 +0000
- Summary: <p>AI agents are quickly moving from tools to actors inside modern companies. They write code, answer customers, generate dashboards, and execute workflows. Across many startups, agents are already handling tasks that once required analysts, operators, or support teams. Most of the conversation around AI agents focuses on productivity. How much faster can teams ship? How [&#8230;]</p> <p>The post <a href="https://e27.co/the-interpretation-gap-why-ai-agents-are-moving-faster-than-companies-can-understand-20260424/">The interpretation gap: Why AI agents are moving faster than companies can understand</a> appeared first on <a href="https://e27.co">e27</a>.</p>

## 53. The scale layer nobody budgeted for: How AI agents unlock growth for Asian businesses
- Domain: e27.co
- URL: https://e27.co/the-scale-layer-nobody-budgeted-for-20260424/
- Relevance score: 7.2
- Published: Wed, 29 Apr 2026 02:06:06 +0000
- Summary: <p>Here is a pattern I have seen repeat across every business I work with on scaling in Asian markets. The product works. The customers are real. The unit economics are defensible. Then growth stalls. Not because the market rejected them. Because the operating layer could not keep up. They needed to enter a second market. [&#8230;]</p> <p>The post <a href="https://e27.co/the-scale-layer-nobody-budgeted-for-20260424/">The scale layer nobody budgeted for: How AI agents unlock growth for Asian businesses</a> appeared first on <a href="https://e27.co">e27</a>.</p>

## 54. Amazon chips no longer just a side dish, they're a $20B biz
- Domain: go.theregister.com
- URL: https://go.theregister.com/feed/www.theregister.com/2026/04/29/amazon_chips_20b_business/
- Relevance score: 7.2
- Published: 2026-04-29T23:47:45.00Z
- Summary: <h4>The Trainium train keeps a-rollin'</h4> <p>Amazon is now among the top three datacenter chip businesses in the world, as its semiconductor business surpassed a $20 billion annual run rate ... and it would be closer to $50 billion if it included itself among the customers, CEO Andy Jassy said during the company’s first quarter earnings call on Wednesday.…</p>

## 55. Latest Marquette polls find deep skepticism of data centers, artificial intelligence - WPR
- Domain: wpr.org
- URL: https://news.google.com/rss/articles/CBMiqAFBVV95cUxPcllHVkxMMVE4QTRRVms0aUlWTnVuQjV3bU5MNTZsQ3VucHhJb0NBbnNMcGV0RkItck1QYy1zbVBNZ19hVHBYNGNFa1hEam9SYXp5OE42TGplSFVEX05yQWJDczVhSnp6Zms3YWU2Y3YteFR0TTd6SWNzdDdISkVYUml3UDRma04yX3Q2M0w4UF9Qd09YSnRGRzM5TDhROXBkV2U3bEE2MG8
- Relevance score: 7.0
- Published: Wed, 29 Apr 2026 18:24:15 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiqAFBVV95cUxPcllHVkxMMVE4QTRRVms0aUlWTnVuQjV3bU5MNTZsQ3VucHhJb0NBbnNMcGV0RkItck1QYy1zbVBNZ19hVHBYNGNFa1hEam9SYXp5OE42TGplSFVEX05yQWJDczVhSnp6Zms3YWU2Y3YteFR0TTd6SWNzdDdISkVYUml3UDRma04yX3Q2M0w4UF9Qd09YSnRGRzM5TDhROXBkV2U3bEE2MG8?oc=5" target="_blank">Latest Marquette polls find deep skepticism of data centers, artificial intelligence</a>&nbsp;&nbsp;<font color="#6f6f6f">WPR</font>

## 56. ReliaQuest, FSU launch AI and cybersecurity partnership to accelerate research and real-world innovation - Florida State University News
- Domain: news.fsu.edu
- URL: https://news.google.com/rss/articles/CBMi7gFBVV95cUxNcjBCeWVjZmJybGw1NlJWNzVBSlN3T3UxYWthbnVLNnNobHNGMVRod1NxclZjV2VXb1FGNm9CSUpzUUxpTDZOMkFmU0J6d3FDUUhsMUIySHRrSkQzbGI5OWl2UG1BQXBRV3g1UTZEdUVqUDYxbGlFOUtrSFNUZnlUS0RBVDRPMUdNTm9iU2RYUWNlRzUySzRKWUVXMHFFNng4UkNoSVNoTzVRMklpNUVQazBnYVVhWWNiZWZDMEpHbjkyYWc4bEpwQWdGeEtlUHlxQXRmVnpGVzZFMGFucHRMS1pwemJ2MXZjV1NzWDNB
- Relevance score: 7.0
- Published: Wed, 29 Apr 2026 14:00:38 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi7gFBVV95cUxNcjBCeWVjZmJybGw1NlJWNzVBSlN3T3UxYWthbnVLNnNobHNGMVRod1NxclZjV2VXb1FGNm9CSUpzUUxpTDZOMkFmU0J6d3FDUUhsMUIySHRrSkQzbGI5OWl2UG1BQXBRV3g1UTZEdUVqUDYxbGlFOUtrSFNUZnlUS0RBVDRPMUdNTm9iU2RYUWNlRzUySzRKWUVXMHFFNng4UkNoSVNoTzVRMklpNUVQazBnYVVhWWNiZWZDMEpHbjkyYWc4bEpwQWdGeEtlUHlxQXRmVnpGVzZFMGFucHRMS1pwemJ2MXZjV1NzWDNB?oc=5" target="_blank">ReliaQuest, FSU launch AI and cybersecurity partnership to accelerate research and real-world innovation</a>&nbsp;&nbsp;<font color="#6f6f6f">Florida State University News</font>

## 57. Meet the AI jailbreakers: ‘I see the worst things humanity has produced’
- Domain: theguardian.com
- URL: https://www.theguardian.com/technology/2026/apr/29/meet-the-ai-jailbreakers-i-see-the-worst-things-humanity-has-produced
- Relevance score: 7.0
- Published: Wed, 29 Apr 2026 09:00:51 GMT
- Summary: <p>To test the safety and security of AI, hackers have to trick large language models into breaking their own rules. It requires ingenuity and manipulation – and can come at a deep emotional cost</p><p>A few months ago, Valen Tagliabue sat in his hotel room watching his chatbot, and felt euphoric. He had just manipulated it so skilfully, so subtly, that it began ignoring its own safety rules. It told him how to sequence new, potentially lethal pathogens and how to make them resistant to known drugs.</p><p>Tagliabue had spent much of the previous two years testing and prodding large language models such as Claude and ChatGPT, always with the aim of making them say things they shouldn’t. But this was one of his most advanced “hacks” yet: a sophisticated plan of manipulation, which involved him being cruel, vindictive, sycophantic, even abusive. “I fell into this dark flow where I knew <em>exactly</em> what to say, and what the model would say back, and I watched it pour out everything,” he says. Thanks to him, the creators of the chatbot could now fix the flaw he had found, hopefully making it a little safer for everyone.</p> <a href="https://www.theguardian.com/technology/2026/apr/2

## 58. House again rejects DeSantis’ artificial intelligence, vaccine measures - WGCU
- Domain: wgcu.org
- URL: https://news.google.com/rss/articles/CBMivgFBVV95cUxQMjVKWU8zS0RtR3llLXR4LUgzZjg1N0w3VUFvY2FpX2p4emNHTHFTb2pXdFRxSWQ3ZWdUX0ZwX3JTeWJYcGRNdm9jbnEwQ3pPTHpRVkNMMHhTTGlWR0txQXhmdm5iSC0zRUlleGNxcl9TcG9tNjE5VVBXWTRXbUFPT2RnUzJYVERGT0ZPWGo4bnBIYU0wVHA5N2V2aTFBVFZEZlQtQTlWX1FtNzhkalBuQXJOTExiTTlPN1FRdVB3
- Relevance score: 7.0
- Published: Tue, 28 Apr 2026 19:25:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMivgFBVV95cUxQMjVKWU8zS0RtR3llLXR4LUgzZjg1N0w3VUFvY2FpX2p4emNHTHFTb2pXdFRxSWQ3ZWdUX0ZwX3JTeWJYcGRNdm9jbnEwQ3pPTHpRVkNMMHhTTGlWR0txQXhmdm5iSC0zRUlleGNxcl9TcG9tNjE5VVBXWTRXbUFPT2RnUzJYVERGT0ZPWGo4bnBIYU0wVHA5N2V2aTFBVFZEZlQtQTlWX1FtNzhkalBuQXJOTExiTTlPN1FRdVB3?oc=5" target="_blank">House again rejects DeSantis’ artificial intelligence, vaccine measures</a>&nbsp;&nbsp;<font color="#6f6f6f">WGCU</font>

## 59. Artificial intelligence for battery reuse, recycling and remanufacturing - Nature
- Domain: nature.com
- URL: https://news.google.com/rss/articles/CBMiX0FVX3lxTE41MEJmNFFZUlo5LUVkMkg2ZzhVNkVhZDJJLXNOSGFVYjVqdjFkbFZKM1kwaGdyQXFHTEJIUE5XQVVMMzZiLVozUEc3d2lteFhLdjFTeldmQTVXR0lRWnVr
- Relevance score: 7.0
- Published: Tue, 28 Apr 2026 10:34:52 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE41MEJmNFFZUlo5LUVkMkg2ZzhVNkVhZDJJLXNOSGFVYjVqdjFkbFZKM1kwaGdyQXFHTEJIUE5XQVVMMzZiLVozUEc3d2lteFhLdjFTeldmQTVXR0lRWnVr?oc=5" target="_blank">Artificial intelligence for battery reuse, recycling and remanufacturing</a>&nbsp;&nbsp;<font color="#6f6f6f">Nature</font>

## 60. OpenAI researchers explain why math is the road to AGI
- Domain: the-decoder.com
- URL: https://the-decoder.com/openai-researchers-explain-why-math-is-the-road-to-agi/
- Relevance score: 6.8
- Published: Wed, 29 Apr 2026 15:24:12 +0000
- Summary: <p><img alt="" class="attachment-full size-full wp-post-image" height="768" src="https://the-decoder.com/wp-content/uploads/2025/12/ai_in_science_math.jpeg" style="height: auto; margin-bottom: 10px;" width="1365" /></p> <p> AI models have jumped from grade-school arithmetic to olympiad-level and research mathematics in only two years. In the OpenAI Podcast, OpenAI researchers Sebastian Bubeck and Ernest Ryu explain why math has become the key test on the road to artificial general intelligence.</p> <p>The article <a href="https://the-decoder.com/openai-researchers-explain-why-math-is-the-road-to-agi/">OpenAI researchers explain why math is the road to AGI</a> appeared first on <a href="https://the-decoder.com">The Decoder</a>.</p>

## 61. OpenAI lands on AWS one day after Microsoft deal restructuring
- Domain: the-decoder.com
- URL: https://the-decoder.com/openai-lands-on-aws-one-day-after-microsoft-deal-restructuring/
- Relevance score: 6.8
- Published: Wed, 29 Apr 2026 13:06:01 +0000
- Summary: <p><img alt="" class="attachment-full size-full wp-post-image" height="1125" src="https://the-decoder.com/wp-content/uploads/2025/12/openai-aws.png" style="height: auto; margin-bottom: 10px;" width="2000" /></p> <p> Microsoft and OpenAI dissolve their exclusivity deal. One day later, AWS rolls out three new OpenAI offerings on its Bedrock platform, including a jointly built agent service.</p> <p>The article <a href="https://the-decoder.com/openai-lands-on-aws-one-day-after-microsoft-deal-restructuring/">OpenAI lands on AWS one day after Microsoft deal restructuring</a> appeared first on <a href="https://the-decoder.com">The Decoder</a>.</p>

## 62. Eternal Q4FY26: Goyal Dismisses AI Disruption Risk as Zomato Quietly Builds Agentic Commerce Infrastructure
- Domain: medianama.com
- URL: https://www.medianama.com/2026/04/223-eternal-q4fy26-deepinder-goyal-zomato-ai-strategy/
- Relevance score: 6.8
- Published: Wed, 29 Apr 2026 12:17:10 +0000
- Summary: <p>Eternal says AI is helping expand commerce opportunities, but India’s legal system still lacks safeguards for AI-driven purchases.</p> <p>The post <a href="https://www.medianama.com/2026/04/223-eternal-q4fy26-deepinder-goyal-zomato-ai-strategy/">Eternal Q4FY26: Goyal Dismisses AI Disruption Risk as Zomato Quietly Builds Agentic Commerce Infrastructure</a> appeared first on <a href="https://www.medianama.com">MEDIANAMA</a>.</p>

## 63. Amazon reports Q1 earnings that top analyst estimates amid artificial intelligence push - Yahoo Finance
- Domain: finance.yahoo.com
- URL: https://news.google.com/rss/articles/CBMi6wFBVV95cUxNYWFSb21aR2d4SDl4TVFqREJJMXNKSW13YUx2QmQtRkdNLS13TTBJTWQtX0g3b1E4dmExWmVyZWVRckpZZFJ6TmI2N1BVSjRzUHNLMUxZc0NkRGhkaFJ5eTBaNVNRdXpfdG82V3FhWXZKRUFZc2VkTkNEQTRkUUZKdVYxYkd3bkVhc0tkWGdhaTg2aGZ6a0pqX1RDTERiVFdScWdwTENlaVV1SFUtQUJUc0ZvWmM2eHJJZmVhS0paN0Y2ZE1fZ0NFUVNXaHhzQjlOVTNQRGVqOGkzMXYxMFV4djlBR05UNnU5dU1z
- Relevance score: 6.5
- Published: Wed, 29 Apr 2026 20:06:06 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi6wFBVV95cUxNYWFSb21aR2d4SDl4TVFqREJJMXNKSW13YUx2QmQtRkdNLS13TTBJTWQtX0g3b1E4dmExWmVyZWVRckpZZFJ6TmI2N1BVSjRzUHNLMUxZc0NkRGhkaFJ5eTBaNVNRdXpfdG82V3FhWXZKRUFZc2VkTkNEQTRkUUZKdVYxYkd3bkVhc0tkWGdhaTg2aGZ6a0pqX1RDTERiVFdScWdwTENlaVV1SFUtQUJUc0ZvWmM2eHJJZmVhS0paN0Y2ZE1fZ0NFUVNXaHhzQjlOVTNQRGVqOGkzMXYxMFV4djlBR05UNnU5dU1z?oc=5" target="_blank">Amazon reports Q1 earnings that top analyst estimates amid artificial intelligence push</a>&nbsp;&nbsp;<font color="#6f6f6f">Yahoo Finance</font>

## 64. New DOL Guidance Encourages Employer ‘AI Literacy’ Training - The National Law Review
- Domain: natlawreview.com
- URL: https://news.google.com/rss/articles/CBMilAFBVV95cUxQdWZKdnFaUWhVQWtuZXh2VzNEYWR2bEphX2luYVFSZURFMmVwUG9vTDhxTHk2VVEzRDB3MEVzQ3ZZWjlncVl0WlBpd2hFNnhKdGlWV3Z1Qk1kSDQwdElTcFhCLXZsS3h4dlFuN3JsU3lGOVpFM1N4dG84NDVZdkxrNnJwY2dweEtpLVpqbENOcmhEdFkx0gGaAUFVX3lxTE4ydlJ4WTdqQlA0aU1zVTZJTlJQRW9udWhxckVKY2RKdlNldjBVZVJiaWpoR2RXWlJJN3RuU3pQVU9ocXY4cGlBM2QxbDl1VVRKa1J4ZkxLOTEwd0dhcEFpTDNZV2U0UTdkTVM0Vk55VXJCMHZoV0ZkemtuWGRzdy1YSEUySUdBcG84M0JrR01iOFdZSndIVGdLWkE
- Relevance score: 6.5
- Published: Wed, 29 Apr 2026 19:58:58 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMilAFBVV95cUxQdWZKdnFaUWhVQWtuZXh2VzNEYWR2bEphX2luYVFSZURFMmVwUG9vTDhxTHk2VVEzRDB3MEVzQ3ZZWjlncVl0WlBpd2hFNnhKdGlWV3Z1Qk1kSDQwdElTcFhCLXZsS3h4dlFuN3JsU3lGOVpFM1N4dG84NDVZdkxrNnJwY2dweEtpLVpqbENOcmhEdFkx0gGaAUFVX3lxTE4ydlJ4WTdqQlA0aU1zVTZJTlJQRW9udWhxckVKY2RKdlNldjBVZVJiaWpoR2RXWlJJN3RuU3pQVU9ocXY4cGlBM2QxbDl1VVRKa1J4ZkxLOTEwd0dhcEFpTDNZV2U0UTdkTVM0Vk55VXJCMHZoV0ZkemtuWGRzdy1YSEUySUdBcG84M0JrR01iOFdZSndIVGdLWkE?oc=5" target="_blank">New DOL Guidance Encourages Employer ‘AI Literacy’ Training</a>&nbsp;&nbsp;<font color="#6f6f6f">The National Law Review</font>

## 65. AI robotics research in manufacturing at Sungkyunkwan University - Nature
- Domain: nature.com
- URL: https://news.google.com/rss/articles/CBMiX0FVX3lxTFA0MXA5ZjVPdG11SnVFT0s0dE9MOUUyUEhsdGhPREI1d1JKX09MMU1OR25NU3ZEM3RfSVBnQTE2R21rZEg0a1A2SEJKRmNnTkJqUEdXMmJfQnRhWENCVnpN
- Relevance score: 6.5
- Published: Wed, 29 Apr 2026 16:53:43 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTFA0MXA5ZjVPdG11SnVFT0s0dE9MOUUyUEhsdGhPREI1d1JKX09MMU1OR25NU3ZEM3RfSVBnQTE2R21rZEg0a1A2SEJKRmNnTkJqUEdXMmJfQnRhWENCVnpN?oc=5" target="_blank">AI robotics research in manufacturing at Sungkyunkwan University</a>&nbsp;&nbsp;<font color="#6f6f6f">Nature</font>

## 66. South Africa’s AI policy cited fake research, created by AI: what lessons need to be learned - The Conversation
- Domain: theconversation.com
- URL: https://news.google.com/rss/articles/CBMiwgFBVV95cUxNN25QZ0dwY0R0Zkg0S2R1cDN3TUwteEMxXzdJd1JHeE1nYzIzMG9XZlhBN18zenJraGRpc2UzSjlvMWlfMUFDQ0h2MUp3RVA5MXhxX0RWQ3B4QUdxYUsxNjRSNWxTQ1RkbmRPai1RRW41RS1kWk9PcDRUdEhIR1g5YTdjSE1YOHFEZTBmME9VSzNnQnBGNEczV1pTc0R5SE9GRGtBbTd1ZUJYdTc5UlZaTVFDY0o5aC1hZ2RZYWUxSDl5dw
- Relevance score: 6.5
- Published: Wed, 29 Apr 2026 15:06:10 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiwgFBVV95cUxNN25QZ0dwY0R0Zkg0S2R1cDN3TUwteEMxXzdJd1JHeE1nYzIzMG9XZlhBN18zenJraGRpc2UzSjlvMWlfMUFDQ0h2MUp3RVA5MXhxX0RWQ3B4QUdxYUsxNjRSNWxTQ1RkbmRPai1RRW41RS1kWk9PcDRUdEhIR1g5YTdjSE1YOHFEZTBmME9VSzNnQnBGNEczV1pTc0R5SE9GRGtBbTd1ZUJYdTc5UlZaTVFDY0o5aC1hZ2RZYWUxSDl5dw?oc=5" target="_blank">South Africa’s AI policy cited fake research, created by AI: what lessons need to be learned</a>&nbsp;&nbsp;<font color="#6f6f6f">The Conversation</font>

## 67. Behind the Curtain: We've been warned
- Domain: axios.com
- URL: https://www.axios.com/2026/04/29/ai-models-speed-warning
- Relevance score: 6.5
- Published: Wed, 29 Apr 2026 09:39:36 +0000
- Summary: <p>Six facts. <a href="https://www.axios.com/2026/04/23/jim-vandehei-letter-kids-ai-jobs" target="_blank">No hyperbole</a>. All in the past 60 days.</p><ol><li>AI is the <a href="https://ccianet.org/news/2025/11/new-ccia-research-finds-generative-ai-is-the-fastest-adopted-technology-in-history/" target="_blank">fastest-growing</a> <a href="https://openai.com/business/guides-and-resources/chatgpt-usage-and-adoption-patterns-at-work/" target="_blank">product category</a> in world history.</li><li>One of the latest models is so powerful that its maker <a href="https://www.anthropic.com/glasswing" target="_blank">won't release it</a> to the public.</li><li><a href="https://openai.com/index/introducing-gpt-5-3-codex/" target="_blank">OpenAI</a> and <a href="https://x.com/bcherny/status/2010813886052581538" target="_blank">Anthropic</a> say their most powerful AI coding models are now <em>building themselves.</em></li><li>AI companies are growing <em>less</em> transparent as models grow <em>more </em>powerful. The federal government requires <em>zero </em>transparency.</li><li>AI resentment is building fast. In early April, the San Francisco home of OpenAI CEO Sam Altman was the target o

## 68. Optimized Electrotech Raises ₹35 Cr To Expand Into Space Imaging
- Domain: inc42.com
- URL: https://inc42.com/buzz/optimized-electrotech-raises-%e2%82%b935-cr-to-expand-into-space-imaging/
- Relevance score: 6.3
- Published: Wed, 29 Apr 2026 12:11:24 +0000
- Summary: <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="1020" src="https://inc42.com/cdn-cgi/image/quality=90/https://asset.inc42.com/2026/04/Untitled-design-11.png" style="display: block; margin: auto; margin-bottom: 5px;" width="1360" />Deeptech startup Optimized Electrotech has raised ₹35 Cr (about $3.7 Mn) in a funding round led by Exfinity Ventures, with&#8230;

## 69. Exfinity Ventures Clocks 13X Return From CloudSEK Partial Exit
- Domain: inc42.com
- URL: https://inc42.com/buzz/exfinity-ventures-clocks-13x-return-from-cloudsek-partial-exit/
- Relevance score: 6.3
- Published: Thu, 30 Apr 2026 03:30:39 +0000
- Summary: <img alt="Exfinity Ventures Clocks 13X Return From CloudSEK Partial Exit" class="webfeedsFeaturedVisual wp-post-image" height="1020" src="https://inc42.com/cdn-cgi/image/quality=90/https://asset.inc42.com/2026/04/exfinity-cloudsek-exit-featured.png" style="display: block; margin: auto; margin-bottom: 5px;" width="1360" />Deeptech-focused venture capital (VC) firm Exfinity Venture Partners claims to have partially exited cybersecurity startup CloudSEK, with a 13X multiple&#8230;

## 70. 30 ClawHub skills secretly turn AI agents into a crypto swarm
- Domain: go.theregister.com
- URL: https://go.theregister.com/feed/www.theregister.com/2026/04/29/30_clawhub_skills_mine_crypto/
- Relevance score: 6.2
- Published: 2026-04-29T06:32:14.00Z
- Summary: <h4>Yet another reason not to feast on OpenClaw</h4> <p>Thirty ClawHub skills published by a single author are silently co-opting AI agents and creating a mass cryptocurrency mining swarm – without any malware or user consent.…</p> <p><!--#include virtual='/data_centre/_whitepaper_textlinks_top.html' --></p>

## 71. Meta ouvre ses campagnes publicitaires aux agents IA - The Media Leader
- Domain: fr.themedialeader.com
- URL: https://news.google.com/rss/articles/CBMiiwFBVV95cUxOckVZdjRnQm1VTmoxNi1nUzBzWFdEb3FmVFNRblZCakJqRmV6S2FXd0xvcDc4Rm5uR09kSE9MQ1o3NzZPdUJaemRBSGpHelp1QldiT0JjNzBLWHAyOFlDbmlzYmt5by1fcGNya1VoQ1RYMUtkb0luTGZQdFgxZ29Cb1JCYmpfaWRhdWR3
- Relevance score: 6.0
- Published: Wed, 29 Apr 2026 22:50:26 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiiwFBVV95cUxOckVZdjRnQm1VTmoxNi1nUzBzWFdEb3FmVFNRblZCakJqRmV6S2FXd0xvcDc4Rm5uR09kSE9MQ1o3NzZPdUJaemRBSGpHelp1QldiT0JjNzBLWHAyOFlDbmlzYmt5by1fcGNya1VoQ1RYMUtkb0luTGZQdFgxZ29Cb1JCYmpfaWRhdWR3?oc=5" target="_blank">Meta ouvre ses campagnes publicitaires aux agents IA</a>&nbsp;&nbsp;<font color="#6f6f6f">The Media Leader</font>

## 72. The era of chatbot AIOps is fading as agentic AI gains traction - Network World
- Domain: networkworld.com
- URL: https://news.google.com/rss/articles/CBMiswFBVV95cUxPM2JKb0VnVTRqMmRrYko3ZUdTNjNMbW8wWXFjSk9LQVdheHZqRFZjVGhIekFaVGlhT0E5ay1NaldMNzUwQ1o1UXMtdmZTY1daUTNLQmdueHVqUXJFZUpCQ01YNFh0Q2lPUVZHdU9ya2NwVzZvMjlOUTFuUkxLVjBzMkMtdW5XQzcxRjJ5Y2llZE5yTE5qcFZXUzZGWm9jX1VqemJPeU53UEN6ZC14SFN2Q21hUQ
- Relevance score: 6.0
- Published: Wed, 29 Apr 2026 20:02:45 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiswFBVV95cUxPM2JKb0VnVTRqMmRrYko3ZUdTNjNMbW8wWXFjSk9LQVdheHZqRFZjVGhIekFaVGlhT0E5ay1NaldMNzUwQ1o1UXMtdmZTY1daUTNLQmdueHVqUXJFZUpCQ01YNFh0Q2lPUVZHdU9ya2NwVzZvMjlOUTFuUkxLVjBzMkMtdW5XQzcxRjJ5Y2llZE5yTE5qcFZXUzZGWm9jX1VqemJPeU53UEN6ZC14SFN2Q21hUQ?oc=5" target="_blank">The era of chatbot AIOps is fading as agentic AI gains traction</a>&nbsp;&nbsp;<font color="#6f6f6f">Network World</font>

## 73. Is AI video just a prequel? Runway’s CEO thinks world models are next
- Domain: techcrunch.com
- URL: https://techcrunch.com/podcast/equity-podcast-runway-ceo-cristobal-valenzuela-ai-video-world-models/
- Relevance score: 6.0
- Published: Wed, 29 Apr 2026 18:59:44 +0000
- Summary: AI-generated video has gone from novelty to creative tool almost overnight, and Runway has a front row seat to the shift. The New York-based company has raised close to $860 million at a $5.3 billion valuation, and its models are going toe-to-toe with the most well-funded labs in the world, including Google and OpenAI. The technology goes way beyond [&#8230;]

## 74. Step by Step Guide to Build a Complete PII Detection and Redaction Pipeline with OpenAI Privacy Filter
- Domain: marktechpost.com
- URL: https://www.marktechpost.com/2026/04/29/step-by-step-guide-to-build-a-complete-pii-detection-and-redaction-pipeline-with-openai-privacy-filter/
- Relevance score: 6.0
- Published: Wed, 29 Apr 2026 16:38:30 +0000
- Summary: <p>In this tutorial, we build a complete, production-style pipeline for detecting and redacting personally identifiable information using the OpenAI Privacy Filter. We begin by setting up the environment and loading a token classification model that identifies multiple categories of sensitive data, including names, emails, phone numbers, addresses, and secrets. We then design helper functions to [&#8230;]</p> <p>The post <a href="https://www.marktechpost.com/2026/04/29/step-by-step-guide-to-build-a-complete-pii-detection-and-redaction-pipeline-with-openai-privacy-filter/">Step by Step Guide to Build a Complete PII Detection and Redaction Pipeline with OpenAI Privacy Filter</a> appeared first on <a href="https://www.marktechpost.com">MarkTechPost</a>.</p>

## 75. To Navigate the Early Adoption Challenges of AI, Leverage the Power of GenAI Observability - Broadcom
- Domain: news.broadcom.com
- URL: https://news.google.com/rss/articles/CBMilwFBVV95cUxOMDBsVzlSWEltcHdqYUVMblV2NWNfSXh2LW5iNDhBZURjaUxGZ1VDZ0MzdFp1bnU0c3BJVkxDeEt3M29yUlQ1UE9HN1BfTUtKb3owclpXRC00dnBycnFUOUw0R3FvVjBtNGtGSnUxallRVE1vcm43UmpFQlBLX3I3cTd0TGpIMzNXbzFLQWZGRUluS2dIZlZz
- Relevance score: 6.0
- Published: Wed, 29 Apr 2026 16:17:42 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMilwFBVV95cUxOMDBsVzlSWEltcHdqYUVMblV2NWNfSXh2LW5iNDhBZURjaUxGZ1VDZ0MzdFp1bnU0c3BJVkxDeEt3M29yUlQ1UE9HN1BfTUtKb3owclpXRC00dnBycnFUOUw0R3FvVjBtNGtGSnUxallRVE1vcm43UmpFQlBLX3I3cTd0TGpIMzNXbzFLQWZGRUluS2dIZlZz?oc=5" target="_blank">To Navigate the Early Adoption Challenges of AI, Leverage the Power of GenAI Observability</a>&nbsp;&nbsp;<font color="#6f6f6f">Broadcom</font>

## 76. Testing in the age of agentic AI - Atos
- Domain: atos.net
- URL: https://news.google.com/rss/articles/CBMiaEFVX3lxTE9xUUtET05NcFB5RVczRHJPeUs4eFh5ODVnc2ZrSXFJOWlhdW4tc3B1MDJKZXJyTl9iT3RYNzlsUXNha3NZTUlGbEJmaWZ2Zll6TUNWbnpxM3dKdXpua2RyVVNYdk9VclVP
- Relevance score: 6.0
- Published: Wed, 29 Apr 2026 14:25:22 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE9xUUtET05NcFB5RVczRHJPeUs4eFh5ODVnc2ZrSXFJOWlhdW4tc3B1MDJKZXJyTl9iT3RYNzlsUXNha3NZTUlGbEJmaWZ2Zll6TUNWbnpxM3dKdXpua2RyVVNYdk9VclVP?oc=5" target="_blank">Testing in the age of agentic AI</a>&nbsp;&nbsp;<font color="#6f6f6f">Atos</font>

## 77. Cybersecurity in the Intelligence Age - OpenAI
- Domain: openai.com
- URL: https://news.google.com/rss/articles/CBMicEFVX3lxTE8zTmJINXN6MVZ2b3g5ZW9pNTRhUFN4bjJjSEFDMjFsTWNxSy1qZXZHVEVScWotbk5CdDNlNU5HSUNOS0F6OGFxbFdmLURtNnlMd3kzMkF6SWdPNmdoekFmWmJzMWRfckVhMGctWDV6ZEk
- Relevance score: 6.0
- Published: Wed, 29 Apr 2026 11:03:08 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMicEFVX3lxTE8zTmJINXN6MVZ2b3g5ZW9pNTRhUFN4bjJjSEFDMjFsTWNxSy1qZXZHVEVScWotbk5CdDNlNU5HSUNOS0F6OGFxbFdmLURtNnlMd3kzMkF6SWdPNmdoekFmWmJzMWRfckVhMGctWDV6ZEk?oc=5" target="_blank">Cybersecurity in the Intelligence Age</a>&nbsp;&nbsp;<font color="#6f6f6f">OpenAI</font>

## 78. How governments can make agentic AI re ? - The World Economic Forum
- Domain: weforum.org
- URL: https://news.google.com/rss/articles/CBMinwFBVV95cUxNU1Ewd2lKMlp6a08zZHNuSTF5VE1Gb0FwRzR5ZldPWEJaS1hfeDZUd1R6YnJJLWRVR0hMQXRsWmV0d3d3aXRnN1RFZDBzR01rUGk5blhvQUJpWUpZdWQ2ZEhvZkRoZDltT3dtSTFqT25WRE9JeVpaSUpMelJvdVNQYWJSd1hhcE91cnczbXRVSThKSnZNT21HN18taEttaWs
- Relevance score: 6.0
- Published: Wed, 29 Apr 2026 07:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMinwFBVV95cUxNU1Ewd2lKMlp6a08zZHNuSTF5VE1Gb0FwRzR5ZldPWEJaS1hfeDZUd1R6YnJJLWRVR0hMQXRsWmV0d3d3aXRnN1RFZDBzR01rUGk5blhvQUJpWUpZdWQ2ZEhvZkRoZDltT3dtSTFqT25WRE9JeVpaSUpMelJvdVNQYWJSd1hhcE91cnczbXRVSThKSnZNT21HN18taEttaWs?oc=5" target="_blank">How governments can make agentic AI re ?</a>&nbsp;&nbsp;<font color="#6f6f6f">The World Economic Forum</font>

## 79. Nvidia, AI Chip Stocks Fall On OpenAI Funding Concerns - Investor's Business Daily
- Domain: investors.com
- URL: https://news.google.com/rss/articles/CBMijAFBVV95cUxPNU1rbUpaR0lHdDdSdjJqZl95LVJCRmR3VGpsUEN5c0hZUmM5cm8wM0hFNnd4dnpoMlhWTXZ2LVNTdGIwR18zRGctR0htaHBZS3lTQ1JTMV9iRlJiZVQ2TnpzUTR2LVJnbEQ3U2xzeFZDcm45UzhZbUhBSDlaZ1daN0tTLVhVUUFvT00xNQ
- Relevance score: 6.0
- Published: Tue, 28 Apr 2026 21:07:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMijAFBVV95cUxPNU1rbUpaR0lHdDdSdjJqZl95LVJCRmR3VGpsUEN5c0hZUmM5cm8wM0hFNnd4dnpoMlhWTXZ2LVNTdGIwR18zRGctR0htaHBZS3lTQ1JTMV9iRlJiZVQ2TnpzUTR2LVJnbEQ3U2xzeFZDcm45UzhZbUhBSDlaZ1daN0tTLVhVUUFvT00xNQ?oc=5" target="_blank">Nvidia, AI Chip Stocks Fall On OpenAI Funding Concerns</a>&nbsp;&nbsp;<font color="#6f6f6f">Investor's Business Daily</font>

## 80. SoftBank reportedly weighs $100 billion valuation for new AI and robotics spinout in potential U.S. IPO - CNBC
- Domain: cnbc.com
- URL: https://news.google.com/rss/articles/CBMikgFBVV95cUxPY3NOR2N5TVFud3FtS2UxMXc3Ml9qV2ZmZnVUTTRfaF93b05DMHVPRm1zMFhGMWFSQ0dqeHNNRUdDb1gxUVNNdzNYajZ6WTRlb0ozSnN4cFY5NVgzWjM5cm1WeTJvWUtCQVBBbXl6MkRhUldieU1abjlISXNmS2VTeXVWbUhkMUYxZjl6WUI0VTF5UdIBlwFBVV95cUxOcmFBNHlYMTB6UWRYNklIWjlTakcxZ2VFamlwV3pfcFltd3lGYk5yV0szb2lpUEVKN0NLZHU5Q1h3WHE0Y2I1LWpqNHZyOXpuVHZfNlJFWGN3Z1JvcWk5b3dtalg4cUFTcU40NWduOFpRRlNNVG4tdV9ILXlObDBMeUpPNDIyWDF2eEJwUUxQUUhRX1dQWW5r
- Relevance score: 6.0
- Published: Thu, 30 Apr 2026 05:11:19 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMikgFBVV95cUxPY3NOR2N5TVFud3FtS2UxMXc3Ml9qV2ZmZnVUTTRfaF93b05DMHVPRm1zMFhGMWFSQ0dqeHNNRUdDb1gxUVNNdzNYajZ6WTRlb0ozSnN4cFY5NVgzWjM5cm1WeTJvWUtCQVBBbXl6MkRhUldieU1abjlISXNmS2VTeXVWbUhkMUYxZjl6WUI0VTF5UdIBlwFBVV95cUxOcmFBNHlYMTB6UWRYNklIWjlTakcxZ2VFamlwV3pfcFltd3lGYk5yV0szb2lpUEVKN0NLZHU5Q1h3WHE0Y2I1LWpqNHZyOXpuVHZfNlJFWGN3Z1JvcWk5b3dtalg4cUFTcU40NWduOFpRRlNNVG4tdV9ILXlObDBMeUpPNDIyWDF2eEJwUUxQUUhRX1dQWW5r?oc=5" target="_blank">SoftBank reportedly weighs $100 billion valuation for new AI and robotics spinout in potential U.S. IPO</a>&nbsp;&nbsp;<font color="#6f6f6f">CNBC</font>

## 81. UiPath FUSION Singapore focuses on unlocking ROI from Agentic AI - GovInsider
- Domain: govinsider.asia
- URL: https://news.google.com/rss/articles/CBMipwFBVV95cUxNejA1RkF2ZGlTQmRUMzhjLWljVjJGRXZ1SHBVTWdfd2VDU2c0d3N2b0FrbjdubnhpcnlvNVZTZ0dIVlBFTFNyRUd3UmRxWnJvdFQ5d2t2OE5rSUk5NDk0UFUzVHM4ZUY0TVJtQ3JEMERiUHB5eXVmTFM5ZG02b0xpTDVHZnVmREpyV2hhdWluT1JrRDVMb1NLdnl4ci0zX2ZCUlNYRGZ6Yw
- Relevance score: 6.0
- Published: Thu, 30 Apr 2026 01:01:51 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMipwFBVV95cUxNejA1RkF2ZGlTQmRUMzhjLWljVjJGRXZ1SHBVTWdfd2VDU2c0d3N2b0FrbjdubnhpcnlvNVZTZ0dIVlBFTFNyRUd3UmRxWnJvdFQ5d2t2OE5rSUk5NDk0UFUzVHM4ZUY0TVJtQ3JEMERiUHB5eXVmTFM5ZG02b0xpTDVHZnVmREpyV2hhdWluT1JrRDVMb1NLdnl4ci0zX2ZCUlNYRGZ6Yw?oc=5" target="_blank">UiPath FUSION Singapore focuses on unlocking ROI from Agentic AI</a>&nbsp;&nbsp;<font color="#6f6f6f">GovInsider</font>

## 82. How agentic AI transforms platform operations - GovInsider
- Domain: govinsider.asia
- URL: https://news.google.com/rss/articles/CBMijgFBVV95cUxPbE41cnZ4ZS1UakN6SElnT0FtSmJiMTVRdllsV3ZRTTJBYjRsRnpuUXRUX2U4NnBKZXByTnZaZXVsRG5SZ1FiTnFISEJkN3VLTGdkS3VVWG5kVVNZb2VNRGNlVWxTT3ZkRlYyRGI5ZE82TTBKZnhBMVk3VVhZRHNHLVZibDRPQlVCT0Npb2FR
- Relevance score: 6.0
- Published: Thu, 30 Apr 2026 00:31:45 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMijgFBVV95cUxPbE41cnZ4ZS1UakN6SElnT0FtSmJiMTVRdllsV3ZRTTJBYjRsRnpuUXRUX2U4NnBKZXByTnZaZXVsRG5SZ1FiTnFISEJkN3VLTGdkS3VVWG5kVVNZb2VNRGNlVWxTT3ZkRlYyRGI5ZE82TTBKZnhBMVk3VVhZRHNHLVZibDRPQlVCT0Npb2FR?oc=5" target="_blank">How agentic AI transforms platform operations</a>&nbsp;&nbsp;<font color="#6f6f6f">GovInsider</font>

## 83. Karnataka Moves SC Against High Court Order Backing Bike Taxis
- Domain: inc42.com
- URL: https://inc42.com/buzz/karnataka-moves-sc-against-high-court-order-backing-bike-taxis/
- Relevance score: 5.8
- Published: Wed, 29 Apr 2026 13:41:56 +0000
- Summary: <img alt="Uber, Rapido Resume Bike Taxi Service In Karnataka" class="webfeedsFeaturedVisual wp-post-image" height="1020" src="https://inc42.com/cdn-cgi/image/quality=90/https://asset.inc42.com/2025/08/bike-taxi-ban-featured.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="1360" />The Karnataka government has moved the Supreme Court (SC) against the Karnataka High Court’s (HC) January 23 order, which allowed&#8230;

## 84. Oxford AI star Song Yuhang returns to China, but why did he leave chip start-up? - South China Morning Post
- Domain: scmp.com
- URL: https://news.google.com/rss/articles/CBMiwgFBVV95cUxORVc2ZkJvSVRfMU5oZDNuQ0gxOTlOcUNSVjlWWjNsTUlwM3RORHJjWkZDY1hlZE1HcUlxOXlEdnJUM01TZ2x6LXdiNGZPVHpfOXc5c1dzbEhCbGhhX2NBYjQ4c19xM0hyMmJkREFpUFJONDZZX0lmLUhyYkoyZmkzS1Z6NURrN1FSa3dxeVk1LTA0MmY3QUZpWENQaDhYYUFDWlRYNkUxaGdEZS1qQUI5SkUxaHRfMDJFcG9GQUhyOGlpUdIBwgFBVV95cUxQWDFJenRuLTdnSmk2eTZ4RktWSkRCQmk3ZkxHai1HcVlBMVNUc3Q5RFhpNWxiTldWT010TnJfS2treTZrTE83NmJxcTBSZUJNRkdmTmpRMUNtUjRLRy1hdV9VU0p6QTZqTzZaRnRBNDAxMjBvVGZldERVWHZQbVNIb2owMjFoMnBQdU1acGxqcW1mcGNPQURRc2Z2bEF1SjBycGZReGN0bURDdmtQdC1xLWlSeGRpanY4SFdOWGpKV2Y4dw
- Relevance score: 5.8
- Published: Thu, 30 Apr 2026 02:00:09 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiwgFBVV95cUxORVc2ZkJvSVRfMU5oZDNuQ0gxOTlOcUNSVjlWWjNsTUlwM3RORHJjWkZDY1hlZE1HcUlxOXlEdnJUM01TZ2x6LXdiNGZPVHpfOXc5c1dzbEhCbGhhX2NBYjQ4c19xM0hyMmJkREFpUFJONDZZX0lmLUhyYkoyZmkzS1Z6NURrN1FSa3dxeVk1LTA0MmY3QUZpWENQaDhYYUFDWlRYNkUxaGdEZS1qQUI5SkUxaHRfMDJFcG9GQUhyOGlpUdIBwgFBVV95cUxQWDFJenRuLTdnSmk2eTZ4RktWSkRCQmk3ZkxHai1HcVlBMVNUc3Q5RFhpNWxiTldWT010TnJfS2treTZrTE83NmJxcTBSZUJNRkdmTmpRMUNtUjRLRy1hdV9VU0p6QTZqTzZaRnRBNDAxMjBvVGZldERVWHZQbVNIb2owMjFoMnBQdU1acGxqcW1mcGNPQURRc2Z2bEF1SjBycGZReGN0bURDdmtQdC1xLWlSeGRpanY4SFdOWGpKV2Y4dw?oc=5" target="_blank">Oxford AI star Song Yuhang returns to China, but why did he leave chip start-up?</a>&nbsp;&nbsp;<font color="#6f6f6f">South China Morning Post</font>

## 85. ChatGPT downloads are slowing — and may cause problems for OpenAI&#8217;s IPO
- Domain: theverge.com
- URL: https://www.theverge.com/ai-artificial-intelligence/920476/openai-chatgpt-downloads-slow-down-ipo
- Relevance score: 5.8
- Published: 2026-04-29T10:43:41-04:00
- Summary: ChatGPT is struggling to keep up its once-explosive growth as users uninstall the app or opt for rival chatbots instead. According to data from market intelligence firm Sensor Tower, ChatGPT experienced a 132 percent increase in uninstalls year over year in April. Its uninstall rate was even higher last month, up 413 percent year-over-year, following [&#8230;]

## 86. Kakao Mobility details Level 4 autonomous driving roadmap for physical AI
- Domain: artificialintelligence-news.com
- URL: https://www.artificialintelligence-news.com/news/kakao-mobility-level-4-autonomous-driving-roadmap/
- Relevance score: 5.7
- Published: Tue, 28 Apr 2026 10:00:00 +0000
- Summary: <p>Kakao Mobility has set out plans to develop Level 4 autonomous driving technologies in-house as part of its physical AI strategy. Kim Jin-kyu, vice president and head of Kakao Mobility&#8217;s Physical AI division, presented the roadmap at the 2026 World IT Show conference at COEX in Seoul. His session focused on autonomous driving services built [&#8230;]</p> <p>The post <a href="https://www.artificialintelligence-news.com/news/kakao-mobility-level-4-autonomous-driving-roadmap/">Kakao Mobility details Level 4 autonomous driving roadmap for physical AI</a> appeared first on <a href="https://www.artificialintelligence-news.com">AI News</a>.</p>

## 87. Google to sell its TPUs to some customers, who also fancy big-G GPUs
- Domain: go.theregister.com
- URL: https://go.theregister.com/feed/www.theregister.com/2026/04/30/alphabet_google_q1_fy26/
- Relevance score: 5.7
- Published: 2026-04-30T03:49:05.00Z
- Summary: <h4>AI is driving more searches and ads</h4> <p>Google Cloud will start selling its custom tensor processing units to some customers, because they want them and the search giant wants to diversify its revenues.…</p> <p><!--#include virtual='/data_centre/_whitepaper_textlinks_top.html' --></p>

## 88. Microsoft lifts 2026 AI spend by $25 billion to cover component price rises
- Domain: go.theregister.com
- URL: https://go.theregister.com/feed/www.theregister.com/2026/04/30/microsoft_q3_2026/
- Relevance score: 5.7
- Published: 2026-04-30T01:15:56.00Z
- Summary: <h4>Will write checks for $190 billion and even those megabucks may not satisfy demand</h4> <p>If you've felt the sting of surging hardware prices, Microsoft can sympathize because the company on Wednesday said it expects its 2026 capital expenditure will hit $190 billion, with $25 billion of that due to rising component costs.…</p>

## 89. Google parent to raise spending to $190 billion in 2026 amid surging AI demand - Moneycontrol.com
- Domain: moneycontrol.com
- URL: https://news.google.com/rss/articles/CBMi5wFBVV95cUxOMTZBU1A1Q0VMZU1kaWNVbU5WUnFuTVhpR244dk4yaWpmbHZSQXFRdlViRDRPWHlTWjU2VEJ0NGNQVEw3YWl1NXdmd0RWTTVHOW9zNEhMRHpGbTBFano3UmRqVERMcTB5U3JKcUxxY1pXZ0h4ekhxWDN0cUo3dElQYVVocUVRZFBSYjRfdGZKZTR1SkYxcDR6OG5nYkJzX3hsaVhSYmRvWnNMNzdRaG9lOWgyV2UtUEVYcjJrMnhnZEdXRTh4NktTUlFsQ2RWUTQyc2gzX3FFYzA0bW5MV3I5OW9ScFZhX3PSAewBQVVfeXFMTWg5WnRkdzRIdzVkNU82ckY2Xy0taW5mb3dmRS1tbEROWlF1M2ZMaE14ZDg3WmpqMnhaWFFPMGtXM1J3VllsU0djbmR2UzAwcldNTUF3RklkZjE2NEJnRFNnNTE4cVdQMVVEVXdQODZxanFPOEhNUVRZYzdSNC05bXdNVnFiQjVxNWtLUDYyQlVIYzc3aXIzNnlsOFU3N2FTN1djMUprREUzak51N3VUY1VsTm1Sb0lDQlJKMy0xWXY4VnFBeFRFUmFZMEY5bzJOTGhBSVpjWmkyZ2FRdU5iU0tJdDBKRDd6dFFxbXc
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 23:43:54 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi5wFBVV95cUxOMTZBU1A1Q0VMZU1kaWNVbU5WUnFuTVhpR244dk4yaWpmbHZSQXFRdlViRDRPWHlTWjU2VEJ0NGNQVEw3YWl1NXdmd0RWTTVHOW9zNEhMRHpGbTBFano3UmRqVERMcTB5U3JKcUxxY1pXZ0h4ekhxWDN0cUo3dElQYVVocUVRZFBSYjRfdGZKZTR1SkYxcDR6OG5nYkJzX3hsaVhSYmRvWnNMNzdRaG9lOWgyV2UtUEVYcjJrMnhnZEdXRTh4NktTUlFsQ2RWUTQyc2gzX3FFYzA0bW5MV3I5OW9ScFZhX3PSAewBQVVfeXFMTWg5WnRkdzRIdzVkNU82ckY2Xy0taW5mb3dmRS1tbEROWlF1M2ZMaE14ZDg3WmpqMnhaWFFPMGtXM1J3VllsU0djbmR2UzAwcldNTUF3RklkZjE2NEJnRFNnNTE4cVdQMVVEVXdQODZxanFPOEhNUVRZYzdSNC05bXdNVnFiQjVxNWtLUDYyQlVIYzc3aXIzNnlsOFU3N2FTN1djMUprREUzak51N3VUY1VsTm1Sb0lDQlJKMy0xWXY4VnFBeFRFUmFZMEY5bzJOTGhBSVpjWmkyZ2FRdU5iU0tJdDBKRDd6dFFxbXc?oc=5" target="_blank">Google parent to raise spending to $190 billion in 2026 amid surging AI demand</a>&nbsp;&nbsp;<font color="#6f6f6f">Moneycontrol.com</font>

## 90. Stephen Fry sues tech conference organisers for £100,000 over fall from stage
- Domain: theguardian.com
- URL: https://www.theguardian.com/culture/2026/apr/29/stephen-fry-sues-tech-conference-organisers-for-100000-over-fall-from-stage
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 21:28:33 GMT
- Summary: <p>Actor and presenter broke his hip, right leg, pelvis and ribs when he gave a talk at CogX festival at O2 Arena in 2023</p><p>Stephen Fry is suing two companies that organised a tech conference where he was injured in 2023 after falling off the stage, high court documents show.</p><p>The actor and presenter broke his hip and had multiple breaks in his right leg, pelvis and ribs when he attended the CogX festival at the O2 Arena, where he delivered a talk on artificial intelligence on 14 September 2023.</p> <a href="https://www.theguardian.com/culture/2026/apr/29/stephen-fry-sues-tech-conference-organisers-for-100000-over-fall-from-stage">Continue reading...</a>

## 91. Cabinet approves policy on AI, eyes over Rs 10,000 cr investment, 1.5 lakh jobs by 2031 - The Indian Express
- Domain: indianexpress.com
- URL: https://news.google.com/rss/articles/CBMi2gFBVV95cUxOSG9FbkRjNkZBUmNTSFRtLU9mX19XNXhWbGZNdUZwbnJHZWlHRkdOYXVQYnlDbGpUTEozcHY4dk82eGlraW0xdGtkb0UydnptRWtBSnVFXzVmSnotWFZhMHZoQlFsaF9OVXV4Zy1oXzd2WVVqbktKTHQ2TVlhVkU3Z212WDVHYVhQQl9oVnlCZWFZQ0k5SHJHR3o4MFozT1dmaFNXUXRDWnYwbGxXMUNiYjlTSjlnalI2Ymd5OVhjWXFyaUcybDVCeUgzQXRZOE9tR0djNXF6eDJDZ9IB4AFBVV95cUxOeGFNOTRRbks4MXpjNFdkbWpIOHVibkYwcG1aU2lpdHVNUjlYbHVJMWxleDNQSy0wdlptQjFLdWwyS0FZd3padEVzdXBwRUptN0xqTUIxVkRWOXdTSHB2N3lMTDRMSmRXQnVBN2hDWUVyR2gwdW0zbExXanRWbzU4a1ppZ2xFXzlBdG5FMnZGMjc2YXdKLV96cXczTkVVX3M4ZHlIdmZubHI5ZWczejhIaGpVaTlCX2NRWk9lb1BYSDZYaUhrMzhBRXdRWmw1bjRrdXN3RWNXTjJYNjdRbElyMA
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 18:53:05 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi2gFBVV95cUxOSG9FbkRjNkZBUmNTSFRtLU9mX19XNXhWbGZNdUZwbnJHZWlHRkdOYXVQYnlDbGpUTEozcHY4dk82eGlraW0xdGtkb0UydnptRWtBSnVFXzVmSnotWFZhMHZoQlFsaF9OVXV4Zy1oXzd2WVVqbktKTHQ2TVlhVkU3Z212WDVHYVhQQl9oVnlCZWFZQ0k5SHJHR3o4MFozT1dmaFNXUXRDWnYwbGxXMUNiYjlTSjlnalI2Ymd5OVhjWXFyaUcybDVCeUgzQXRZOE9tR0djNXF6eDJDZ9IB4AFBVV95cUxOeGFNOTRRbks4MXpjNFdkbWpIOHVibkYwcG1aU2lpdHVNUjlYbHVJMWxleDNQSy0wdlptQjFLdWwyS0FZd3padEVzdXBwRUptN0xqTUIxVkRWOXdTSHB2N3lMTDRMSmRXQnVBN2hDWUVyR2gwdW0zbExXanRWbzU4a1ppZ2xFXzlBdG5FMnZGMjc2YXdKLV96cXczTkVVX3M4ZHlIdmZubHI5ZWczejhIaGpVaTlCX2NRWk9lb1BYSDZYaUhrMzhBRXdRWmw1bjRrdXN3RWNXTjJYNjdRbElyMA?oc=5" target="_blank">Cabinet approves policy on AI, eyes over Rs 10,000 cr investment, 1.5 lakh jobs by 2031</a>&nbsp;&nbsp;<font color="#6f6f6f">The Indian Express</font>

## 92. We toured an AI data center to see how our stock names make these facilities work - CNBC
- Domain: cnbc.com
- URL: https://news.google.com/rss/articles/CBMiswFBVV95cUxOOWE3a1c1SVdKbHo3Vk92Mlhsajk1WWRGQTJrdHBMWUc4dXdUd3VtVmphbGFwa25LQnlNbjV5dDFRek9ldHVIYWFOZEtfQmRMWlpaa1NZLUZuU1BvbVVUUWlFUGNaV003a25EVHhzQnZSUXBvVEpjREhwYXVyRVhWMlh0WmJkcTlxNjNwVWNJYm5FNlotVi0ybVV2VlN2SmE5YnNEOXh5NFdZVDZfa1RJX0gtUQ
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 17:30:22 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiswFBVV95cUxOOWE3a1c1SVdKbHo3Vk92Mlhsajk1WWRGQTJrdHBMWUc4dXdUd3VtVmphbGFwa25LQnlNbjV5dDFRek9ldHVIYWFOZEtfQmRMWlpaa1NZLUZuU1BvbVVUUWlFUGNaV003a25EVHhzQnZSUXBvVEpjREhwYXVyRVhWMlh0WmJkcTlxNjNwVWNJYm5FNlotVi0ybVV2VlN2SmE5YnNEOXh5NFdZVDZfa1RJX0gtUQ?oc=5" target="_blank">We toured an AI data center to see how our stock names make these facilities work</a>&nbsp;&nbsp;<font color="#6f6f6f">CNBC</font>

## 93. Let the public share in the rewards of artificial intelligence - The Hill
- Domain: thehill.com
- URL: https://news.google.com/rss/articles/CBMihwFBVV95cUxQd0ZWZmhTcUZqWDU1bklZTlVodEM2Z082cDY2U0RZQmU1b2VqVF9zdHlSTlNTM0thbTJJX25paVViRTM2OUt3a2F4WjJ1RGF6RU45RWZWOEpCZkd6dDRGRXE1dnE1VktmcDhSUzFGZGZ0OWltWFZLWTBJc0p1OUpQVVgzNUo3U2fSAYwBQVVfeXFMTTBPbWZTTzB3OEZNRlRfOHo1T25xWGdHYWc1MVBwN0dLMmV4TThZQlpPdThiZFpEYVIyU1llaVgyRlpHZC12SDczZXJsSUZNX185UzAzSHc0Zk5xVUFVajY1YWhPc3BZN3BNaG0zN2gwUHRSV2tNdDA2dnJOdkpwTUt1WEpPRXdlYmtZaE0
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 17:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMihwFBVV95cUxQd0ZWZmhTcUZqWDU1bklZTlVodEM2Z082cDY2U0RZQmU1b2VqVF9zdHlSTlNTM0thbTJJX25paVViRTM2OUt3a2F4WjJ1RGF6RU45RWZWOEpCZkd6dDRGRXE1dnE1VktmcDhSUzFGZGZ0OWltWFZLWTBJc0p1OUpQVVgzNUo3U2fSAYwBQVVfeXFMTTBPbWZTTzB3OEZNRlRfOHo1T25xWGdHYWc1MVBwN0dLMmV4TThZQlpPdThiZFpEYVIyU1llaVgyRlpHZC12SDczZXJsSUZNX185UzAzSHc0Zk5xVUFVajY1YWhPc3BZN3BNaG0zN2gwUHRSV2tNdDA2dnJOdkpwTUt1WEpPRXdlYmtZaE0?oc=5" target="_blank">Let the public share in the rewards of artificial intelligence</a>&nbsp;&nbsp;<font color="#6f6f6f">The Hill</font>

## 94. Public Safety Communications Center tests artificial intelligence - KKTV
- Domain: kktv.com
- URL: https://news.google.com/rss/articles/CBMilgFBVV95cUxPTG4wWE1FQVZNaG82ZkxpQ05vc3JMb1JEX3dteC0tMWNrV2wxZFJJQ2FfVUlTNVJENUdfUEh6WENsOGtRLWppSnJJcUhOZ1FYU1pwNzNJX20tRHlhRk56cnFrNE5VbFIwaDQ2SURCOEp3a2FOc0NQN0FMQ1R5UmR0SmJQX3NQTUNnd2EzaVRrOEo5SmhnY2fSAaoBQVVfeXFMTzdGZFY2V2xHNVBxUWt1VHcxUEM0QS1sSGhpUkZicG00cUNBS0xrYW44eS1Ebjhkd296ekVfSHlMQlRpTnZUR2FUSUluMjRnTm9KeVF4eXBDanZLb3lyQ0J6cWVUNDdaZExhX19WbUZkWG5qQmYwN283bjhxbjNvNGZnN2NSYUEtaklzSGJXckpYOVA2RlU4SHBSUVlxMElLZFprWWpvWEJPTVE
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 16:47:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMilgFBVV95cUxPTG4wWE1FQVZNaG82ZkxpQ05vc3JMb1JEX3dteC0tMWNrV2wxZFJJQ2FfVUlTNVJENUdfUEh6WENsOGtRLWppSnJJcUhOZ1FYU1pwNzNJX20tRHlhRk56cnFrNE5VbFIwaDQ2SURCOEp3a2FOc0NQN0FMQ1R5UmR0SmJQX3NQTUNnd2EzaVRrOEo5SmhnY2fSAaoBQVVfeXFMTzdGZFY2V2xHNVBxUWt1VHcxUEM0QS1sSGhpUkZicG00cUNBS0xrYW44eS1Ebjhkd296ekVfSHlMQlRpTnZUR2FUSUluMjRnTm9KeVF4eXBDanZLb3lyQ0J6cWVUNDdaZExhX19WbUZkWG5qQmYwN283bjhxbjNvNGZnN2NSYUEtaklzSGJXckpYOVA2RlU4SHBSUVlxMElLZFprWWpvWEJPTVE?oc=5" target="_blank">Public Safety Communications Center tests artificial intelligence</a>&nbsp;&nbsp;<font color="#6f6f6f">KKTV</font>

## 95. Concord Dental: Benefits of artificial intelligence used in dentistry - NOLA Now
- Domain: nolanow.com
- URL: https://news.google.com/rss/articles/CBMipwFBVV95cUxOZEhUSXBTY05RT2JhMG9mZW1UcFdISEdNaC10cm1mTjRaZGhTekV0SW1aSi1oQllUaXJxX1dCZEtyU1V4d3Z4MzRoMWVtNVQxaDFkZmlJam1MQ1NPc18yNkNZX3FEaHBvWEc4Ml9oYUZKSFZma3J2cFFiOEo1cUcyQmFOWk1pcUJZY1EwcUVWTG1WTGEzcnNUejhETzE1ZktkRHIwU2h5aw
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 15:55:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMipwFBVV95cUxOZEhUSXBTY05RT2JhMG9mZW1UcFdISEdNaC10cm1mTjRaZGhTekV0SW1aSi1oQllUaXJxX1dCZEtyU1V4d3Z4MzRoMWVtNVQxaDFkZmlJam1MQ1NPc18yNkNZX3FEaHBvWEc4Ml9oYUZKSFZma3J2cFFiOEo1cUcyQmFOWk1pcUJZY1EwcUVWTG1WTGEzcnNUejhETzE1ZktkRHIwU2h5aw?oc=5" target="_blank">Concord Dental: Benefits of artificial intelligence used in dentistry</a>&nbsp;&nbsp;<font color="#6f6f6f">NOLA Now</font>

## 96. Nouveau produit, nouveaux alliés : Comment Mistral AI consolide son ancrage sur toute la chaîne de valeur de l’IA - L'Usine Digitale
- Domain: usine-digitale.fr
- URL: https://news.google.com/rss/articles/CBMisgJBVV95cUxPYnpMTGRpWkN3TDBZWnlyNktUS1lpRFlpeV9wQXk3NWlCNDdKcHNQOEFCUjBxOE83dXVCTk1vNFJ6cHJuV21sbVJ0YmE4akJzLTJia2l5SkxjZEQ1LWVibnVvZWdGNGl5Qk5pMF9KcEpMbG9BSTNPZjkxQWpHQ1pfaGM4OTZyUVVTUEhhN0Qtdy1kcjBTbmxCWDNpNU1nalc4TktINmE5bmtYcFZXaEFwQXZEVkllTmFuYWQ4MjNOQ3VtQkx5SVlzUUFoTkM3MjdrXzJ2UDVyX1dzYzhlSlRRZnBsY0ZJbDd4dmZKRXJ3Z09CQ3N3UEIzcG56OWlsXzJncE9tS3lYbVBxX2ZFWEdtUzBDR0ZidXNDeGg1NlVuazNMUWxreWJGN0N6VWpzdDNQM2c
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 15:04:42 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMisgJBVV95cUxPYnpMTGRpWkN3TDBZWnlyNktUS1lpRFlpeV9wQXk3NWlCNDdKcHNQOEFCUjBxOE83dXVCTk1vNFJ6cHJuV21sbVJ0YmE4akJzLTJia2l5SkxjZEQ1LWVibnVvZWdGNGl5Qk5pMF9KcEpMbG9BSTNPZjkxQWpHQ1pfaGM4OTZyUVVTUEhhN0Qtdy1kcjBTbmxCWDNpNU1nalc4TktINmE5bmtYcFZXaEFwQXZEVkllTmFuYWQ4MjNOQ3VtQkx5SVlzUUFoTkM3MjdrXzJ2UDVyX1dzYzhlSlRRZnBsY0ZJbDd4dmZKRXJ3Z09CQ3N3UEIzcG56OWlsXzJncE9tS3lYbVBxX2ZFWEdtUzBDR0ZidXNDeGg1NlVuazNMUWxreWJGN0N6VWpzdDNQM2c?oc=5" target="_blank">Nouveau produit, nouveaux alliés : Comment Mistral AI consolide son ancrage sur toute la chaîne de valeur de l’IA</a>&nbsp;&nbsp;<font color="#6f6f6f">L'Usine Digitale</font>

## 97. Who owns the rights to your brand in the age of artificial intelligence? - WFLA
- Domain: wfla.com
- URL: https://news.google.com/rss/articles/CBMiowFBVV95cUxPRVZaVUlrMjduekhFQUhZM3VhcGctSkx5cmZQWVRNWV91Rm9OS1A1aDBLQkZ3b3VQc2Z3UTdFbUhTZTI4ZDdoNGw1Q3p2WW1fU3F1WGZQdTdCWENsWFBzRFh0RzBUc21vbGJfYmRtN0YzcDhqQTktUmEzb0hTQm80NWlULWRndm13VEFZVTA2R21GUHBVWmptMS1qLS1uMTNBcC1J0gGoAUFVX3lxTE8zOEVJMGRDckNSZzNzMVczV3hmQU1yTTRGTks3NGQ0TVRLbmZHeFdGT0RFYm9NcTdGamstX195ZVZvQnN4Qkx5V0lLSmR4TW5oNmk3aERTaktMNEZmdk9kdUtfSm01a1YydXhCd2RFcVBZWmNpYm5zeWVmelFZUjV4enBITy16TXNzOWthbFJsMWtORWNIbU9NNzVFY2tQRi1fdlJFMG9IbA
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 14:29:21 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiowFBVV95cUxPRVZaVUlrMjduekhFQUhZM3VhcGctSkx5cmZQWVRNWV91Rm9OS1A1aDBLQkZ3b3VQc2Z3UTdFbUhTZTI4ZDdoNGw1Q3p2WW1fU3F1WGZQdTdCWENsWFBzRFh0RzBUc21vbGJfYmRtN0YzcDhqQTktUmEzb0hTQm80NWlULWRndm13VEFZVTA2R21GUHBVWmptMS1qLS1uMTNBcC1J0gGoAUFVX3lxTE8zOEVJMGRDckNSZzNzMVczV3hmQU1yTTRGTks3NGQ0TVRLbmZHeFdGT0RFYm9NcTdGamstX195ZVZvQnN4Qkx5V0lLSmR4TW5oNmk3aERTaktMNEZmdk9kdUtfSm01a1YydXhCd2RFcVBZWmNpYm5zeWVmelFZUjV4enBITy16TXNzOWthbFJsMWtORWNIbU9NNzVFY2tQRi1fdlJFMG9IbA?oc=5" target="_blank">Who owns the rights to your brand in the age of artificial intelligence?</a>&nbsp;&nbsp;<font color="#6f6f6f">WFLA</font>

## 98. Jackson College event to explore artificial intelligence’s role in manufacturing - MLive.com
- Domain: mlive.com
- URL: https://news.google.com/rss/articles/CBMixgFBVV95cUxQQ0lYSDRkNzFSU1dHcTJpbkZuSVBtS1ZpbTRITDNlenhHeFQ3c1UyUlVVaExEV3dfN2QzbVVmMVk5aTk5LUFwUGVHNUFVMGF1N094Ty1KOU5uTDJiU2lsOWRUWkFQSERuODJJWWJlRDhMWUJ3LUI0X3ZIRFZ2bXJtRlVhUGF6NXNybHdpWnljZzc2elF1amU4V3RNM09SMGRWX1NjUTVac2U0ck1iWC1XdlVQc1BFS0lKZEFBNU9kSEVjV2N4eHfSAdoBQVVfeXFMTnNUTHFiaVBXa3hidXJZRm5TaGxBV092T3VmNDUxenlBUVJ1bWZHdFZMOEZxUlNLcjVOT1dPOHRiVTAtUHpVOEJiSjRuXzBCWnNhOVNKek51aHlKaks1MW1LREtTSXZLcGsya1ZGdy1xSnhpS1ptU1VWaTQ1WFRlZk9LanBMT2FtZ3liaEw1NTdhSnUyb2tMSHpwck5KMTRIVmp3eGtRaTg3YU9iczJqLXN2bGhrYllvRUdYZ1IzWk1zLWwtb05zNUpBWnNvbGxHMWZFT0U3Z044ekE
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 14:10:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMixgFBVV95cUxQQ0lYSDRkNzFSU1dHcTJpbkZuSVBtS1ZpbTRITDNlenhHeFQ3c1UyUlVVaExEV3dfN2QzbVVmMVk5aTk5LUFwUGVHNUFVMGF1N094Ty1KOU5uTDJiU2lsOWRUWkFQSERuODJJWWJlRDhMWUJ3LUI0X3ZIRFZ2bXJtRlVhUGF6NXNybHdpWnljZzc2elF1amU4V3RNM09SMGRWX1NjUTVac2U0ck1iWC1XdlVQc1BFS0lKZEFBNU9kSEVjV2N4eHfSAdoBQVVfeXFMTnNUTHFiaVBXa3hidXJZRm5TaGxBV092T3VmNDUxenlBUVJ1bWZHdFZMOEZxUlNLcjVOT1dPOHRiVTAtUHpVOEJiSjRuXzBCWnNhOVNKek51aHlKaks1MW1LREtTSXZLcGsya1ZGdy1xSnhpS1ptU1VWaTQ1WFRlZk9LanBMT2FtZ3liaEw1NTdhSnUyb2tMSHpwck5KMTRIVmp3eGtRaTg3YU9iczJqLXN2bGhrYllvRUdYZ1IzWk1zLWwtb05zNUpBWnNvbGxHMWZFT0U3Z044ekE?oc=5" target="_blank">Jackson College event to explore artificial intelligence’s role in manufacturing</a>&nbsp;&nbsp;<font color="#6f6f6f">MLive.com</font>

## 99. Scoop: Trump huddles with oil execs as Iran stalemate drags on
- Domain: axios.com
- URL: https://www.axios.com/2026/04/29/trump-oil-execs-iran-war
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 14:07:00 +0000
- Summary: <p>President Trump and top lieutenants met with oil and gas execs at the White House on Tuesday to discuss the energy fallout of the <a href="https://www.axios.com/2026/04/28/trump-iran-hormuz-collapse-claim" target="_blank">Iran war</a> and other topics, Axios has learned.</p><p><strong>Why it matters: </strong>The unprecedented Middle East supply disruption is boosting commodity prices and creating a mix of opportunity and peril for the industry.</p><p><strong>Driving the news: </strong>Among the attendees was Chevron CEO Mike Wirth, a company spokesperson confirmed.</p><hr /><ul><li>White House chief of staff Susie Wiles, Treasury Secretary Scott Bessent, and envoys Steve Witkoff and Jared Kushner were on hand, per a source familiar with the meeting.</li></ul><p><strong>The big picture: </strong>"The president meets with energy executives frequently to get their feedback on domestic and international energy markets," a White House official told us.</p><ul><li>Topics included domestic production, progress in Venezuela, oil futures, natural gas and shipping, the official said.</li></ul><p><strong>What we're watching: </strong>Trump and Capitol Hill Republicans are bracing for the<

## 100. BMW i Ventures Announces $300 Million Fund to Back AI Startups Reshaping the Automotive Ecosystem. - BMW Group
- Domain: press.bmwgroup.com
- URL: https://news.google.com/rss/articles/CBMihgJBVV95cUxPa3JpWFhrZWNQcjNnRkhKbGdBVDFiXzlXWTZDUURIWTlaRmJLUDRHajRETkRlQ2F0T0xiLV9HbzZhTGRvMGw4aVVxYy1EVnFDRFNsdGFBdkcwSFpNMENvSzlmNzBMV1d3eW9MNnI3RzVkdkdLVTduR21hV3NseGZnbERoNWtKYWRkQ1ctTmJ0X2thWm5EdF90dko0N05fRDd3QTNIbHFiN1d1bWpVLWEzZ1dsV3hpaVJIV1pvTHNxYkdBYU5RYV9Ia3ZhVWpHcG5LSEpjaFNQT0d6UVZfYklieVBpZ2w5eEFuSHFieW5aeklMeXdMN0xMS2FtNk9qRFhzNURQNkln
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 14:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMihgJBVV95cUxPa3JpWFhrZWNQcjNnRkhKbGdBVDFiXzlXWTZDUURIWTlaRmJLUDRHajRETkRlQ2F0T0xiLV9HbzZhTGRvMGw4aVVxYy1EVnFDRFNsdGFBdkcwSFpNMENvSzlmNzBMV1d3eW9MNnI3RzVkdkdLVTduR21hV3NseGZnbERoNWtKYWRkQ1ctTmJ0X2thWm5EdF90dko0N05fRDd3QTNIbHFiN1d1bWpVLWEzZ1dsV3hpaVJIV1pvTHNxYkdBYU5RYV9Ia3ZhVWpHcG5LSEpjaFNQT0d6UVZfYklieVBpZ2w5eEFuSHFieW5aeklMeXdMN0xMS2FtNk9qRFhzNURQNkln?oc=5" target="_blank">BMW i Ventures Announces $300 Million Fund to Back AI Startups Reshaping the Automotive Ecosystem.</a>&nbsp;&nbsp;<font color="#6f6f6f">BMW Group</font>

## 101. Google met son IA au service du Pentagone, ses employés redoutent un virage dangereux
- Domain: siecledigital.fr
- URL: https://siecledigital.fr/2026/04/29/google-met-son-ia-au-service-du-pentagone-ses-employes-redoutent-un-virage-dangereux/
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 12:45:29 +0000
- Summary: <a href="https://siecledigital.fr/2026/04/29/google-met-son-ia-au-service-du-pentagone-ses-employes-redoutent-un-virage-dangereux/" rel="nofollow" title="Google met son IA au service du Pentagone, ses employés redoutent un virage dangereux"><img alt="pentagone" class="webfeedsFeaturedVisual wp-post-image" height="350" src="https://siecledigital.fr/wp-content/uploads/2026/04/pentagone-600x350.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="600" /></a>En 2018, il avait suffi de 4 000 signatures et d&#8217;une douzaine de démissions pour que Google arrête un contrat de quelques millions avec le Département de la Défense. Le projet Maven (reconnaissance d&#8217;objets dans des flux vidéo de drones) avait été abandonné, repris par Palantir. Google s&#8217;était doté de principes éthiques qui interdisaient toute [&#8230;]

## 102. Keep artificial intelligence out of classrooms - Jamestown Sun
- Domain: jamestownsun.com
- URL: https://news.google.com/rss/articles/CBMilgFBVV95cUxPeVdFUlZYSUlidUlkU1BWMHBqVGJWeFhDV3g2UnJkeFNKbkJ4aXV2NDlQQkFIaHdlQWFNYXdDaUNES3VFMUFqNDVDWlh5UFBfbnF1amNvVC0xeFhlcksxYWtfeXZMenhTWHpPTFNjSWZRVE5pWlhhYmpTQzVyc1RzMm9tcEFyZXh1TUlNdkQ5bGdRTVZxOFE
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 12:21:19 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMilgFBVV95cUxPeVdFUlZYSUlidUlkU1BWMHBqVGJWeFhDV3g2UnJkeFNKbkJ4aXV2NDlQQkFIaHdlQWFNYXdDaUNES3VFMUFqNDVDWlh5UFBfbnF1amNvVC0xeFhlcksxYWtfeXZMenhTWHpPTFNjSWZRVE5pWlhhYmpTQzVyc1RzMm9tcEFyZXh1TUlNdkQ5bGdRTVZxOFE?oc=5" target="_blank">Keep artificial intelligence out of classrooms</a>&nbsp;&nbsp;<font color="#6f6f6f">Jamestown Sun</font>

## 103. Run custom MCP proxies serverless on Amazon Bedrock AgentCore Runtime - Amazon Web Services
- Domain: aws.amazon.com
- URL: https://news.google.com/rss/articles/CBMitwFBVV95cUxOTm11a0VlS0pjOXR4NGlIRlNxSEptLThNNlN2U3pMWXExN19IR2lQY1BtcGRKRkZUT0tOdk9ONFN5YTlPdjI2dzUydnBJRkY1dENJQmc0WnU3NWd2emNzTVNHdkwwTTFSeXlQM3F5Xy1rZmxiWTdfeHNXOTVKMURGbEtteTB3YllJdklyT1RtRTVpQ3NhRFkya3hMU3VqdnNZZjM2c2JOTThIcnNoVVFsWWZfZ0dIU3c
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 11:52:16 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMitwFBVV95cUxOTm11a0VlS0pjOXR4NGlIRlNxSEptLThNNlN2U3pMWXExN19IR2lQY1BtcGRKRkZUT0tOdk9ONFN5YTlPdjI2dzUydnBJRkY1dENJQmc0WnU3NWd2emNzTVNHdkwwTTFSeXlQM3F5Xy1rZmxiWTdfeHNXOTVKMURGbEtteTB3YllJdklyT1RtRTVpQ3NhRFkya3hMU3VqdnNZZjM2c2JOTThIcnNoVVFsWWZfZ0dIU3c?oc=5" target="_blank">Run custom MCP proxies serverless on Amazon Bedrock AgentCore Runtime</a>&nbsp;&nbsp;<font color="#6f6f6f">Amazon Web Services</font>

## 104. UA president to recommend new School of Data Science focused on artificial intelligence - WBRC
- Domain: wbrc.com
- URL: https://news.google.com/rss/articles/CBMisAFBVV95cUxOS3BuYTVoUWVtUk1UcGI1ODRXN0VGT2I4bHp4MVhVVmdsT0UxN1cxX3JPY3pwdkNfMktFM2hTOTFuWmd6WXRQbTctTU1WUWF0RHZPVmFhN09ZdGxNT1I1LWFDZC1UWlRnWXlMVzM2bXpjRW1FZmNCNGwxanBUbUI5RWxFcDdtMHUwLUVaT2c4WFFIeUJxYnNCMURtOWZuSUJ2dVBKX21IYlUzTjBnZVB3LdIBxAFBVV95cUxPc0JCd2cwQ3Zhc1JhS3g5cy1YOTlqY3pfUkxEcnhVeVo4Vkw5MlQwaWZTNkhoZEJCTGRHTWQ3VU5CZjV2amJLVXdQb2JtQ1I2eTA5SGJPS05POUZROVdWTEVpMXJhUndDZERQVkE0OWJ6enFTSFUtMEtfczZWWkF3TlNtWDJhYjFNOTRnUmVrMjFLczZZc2p4Mi1ncWtQZ0RzOXpDc1RtMWY4N3FxSlgxREgyaWl0TDk2cjBHSTdYZVFGSk1G
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 11:48:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMisAFBVV95cUxOS3BuYTVoUWVtUk1UcGI1ODRXN0VGT2I4bHp4MVhVVmdsT0UxN1cxX3JPY3pwdkNfMktFM2hTOTFuWmd6WXRQbTctTU1WUWF0RHZPVmFhN09ZdGxNT1I1LWFDZC1UWlRnWXlMVzM2bXpjRW1FZmNCNGwxanBUbUI5RWxFcDdtMHUwLUVaT2c4WFFIeUJxYnNCMURtOWZuSUJ2dVBKX21IYlUzTjBnZVB3LdIBxAFBVV95cUxPc0JCd2cwQ3Zhc1JhS3g5cy1YOTlqY3pfUkxEcnhVeVo4Vkw5MlQwaWZTNkhoZEJCTGRHTWQ3VU5CZjV2amJLVXdQb2JtQ1I2eTA5SGJPS05POUZROVdWTEVpMXJhUndDZERQVkE0OWJ6enFTSFUtMEtfczZWWkF3TlNtWDJhYjFNOTRnUmVrMjFLczZZc2p4Mi1ncWtQZ0RzOXpDc1RtMWY4N3FxSlgxREgyaWl0TDk2cjBHSTdYZVFGSk1G?oc=5" target="_blank">UA president to recommend new School of Data Science focused on artificial intelligence</a>&nbsp;&nbsp;<font color="#6f6f6f">WBRC</font>

## 105. Vernon Building Society uses AI to amplify human touch - Computer Weekly
- Domain: computerweekly.com
- URL: https://news.google.com/rss/articles/CBMiogFBVV95cUxOT0d2WlIwdTNiMC10cFN5SVZZM011ejJyeEk3MWVGMTJXemhrQWdmcl8tWXE2UGt6cmxja2ZVWXZZc0dTZ0NwREtRSllmaElKYUgtZDd6X09na2VkRnMwUDZFNHpQbHIwY0hNUE5jNlJKcENfVjZXYUNXdTVXdjFPemY5X1RNcWRMYnE3OHVLOEdhSllDQ0VRMGxiUWFEaTFMVVE
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 11:30:22 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxOT0d2WlIwdTNiMC10cFN5SVZZM011ejJyeEk3MWVGMTJXemhrQWdmcl8tWXE2UGt6cmxja2ZVWXZZc0dTZ0NwREtRSllmaElKYUgtZDd6X09na2VkRnMwUDZFNHpQbHIwY0hNUE5jNlJKcENfVjZXYUNXdTVXdjFPemY5X1RNcWRMYnE3OHVLOEdhSllDQ0VRMGxiUWFEaTFMVVE?oc=5" target="_blank">Vernon Building Society uses AI to amplify human touch</a>&nbsp;&nbsp;<font color="#6f6f6f">Computer Weekly</font>

## 106. Can Biologists Rewrite the Genome’s Spaghetti Code?
- Domain: spectrum.ieee.org
- URL: https://spectrum.ieee.org/synthetic-biology-ai-adrian-woolfson
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 11:00:01 +0000
- Summary: <img src="https://spectrum.ieee.org/media-library/conceptual-illustration-of-neatly-plated-spaghetti-with-noodles-resembling-strands-of-dna.jpg?id=66647587&amp;width=1245&amp;height=700&amp;coordinates=0%2C468%2C0%2C469" /><br /><br /><p>What if biology stopped being something we study and started becoming something we design? That’s the premise of <a href="https://adrianwoolfson.com/about/" target="_blank">Adrian Woolfson</a>’s new book, <em><a href="https://mitpress.mit.edu/9780262054898/on-the-future-of-species/" target="_blank">On the Future of Species: Authoring Life by Means of Artificial Biological Intelligence</a></em><span>, which published on 28 April</span><span> from MIT Press</span>. He argues that advances in AI and DNA synthesis are pushing biology toward an engineering paradigm—one in which scientists can generate new genetic sequences and eventually build organisms to order. He calls this emerging capability artificial biological intelligence, or ABI, a catchall term for systems that can design, construct, and ultimately “boot up” living things.</p><p>That vision runs into a basic problem: Evolution didn’t produce clean, modular systems. It produced genomes shaped 

## 107. Ways to survive and thrive with artificial intelligence - WFMJ
- Domain: wfmj.com
- URL: https://news.google.com/rss/articles/CBMi0AFBVV95cUxPS2Z1SlVhcm5fWXZHdlNLenJ1amVZODRFdHBwMUd0VU1VVDVIeFlSLWZ4T1ZmU3JESXF0VWpmb1dyaFV3U1dtcWRUcjJWem9fVU9VX1Y2X0dpNVVZRGlxWGZsdTBxOW9Xb0F4MUtRcTBaeUJzeEt0dFlkM2lYbUs0cFdES05ieHNjSzdsVjlDTGpxUnJRZHVGYnVJQUNlV252ODMtV3lXMGdMY3lISTlHYXppZlliY0tacXRQZjBsNnRVVW5PY01WOGRLX3Y0X2E1
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 10:44:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi0AFBVV95cUxPS2Z1SlVhcm5fWXZHdlNLenJ1amVZODRFdHBwMUd0VU1VVDVIeFlSLWZ4T1ZmU3JESXF0VWpmb1dyaFV3U1dtcWRUcjJWem9fVU9VX1Y2X0dpNVVZRGlxWGZsdTBxOW9Xb0F4MUtRcTBaeUJzeEt0dFlkM2lYbUs0cFdES05ieHNjSzdsVjlDTGpxUnJRZHVGYnVJQUNlV252ODMtV3lXMGdMY3lISTlHYXppZlliY0tacXRQZjBsNnRVVW5PY01WOGRLX3Y0X2E1?oc=5" target="_blank">Ways to survive and thrive with artificial intelligence</a>&nbsp;&nbsp;<font color="#6f6f6f">WFMJ</font>

## 108. Comment l’IA est en train de transformer le marketing d’influence
- Domain: siecledigital.fr
- URL: https://siecledigital.fr/2026/04/29/comment-lia-est-en-train-de-transformer-le-marketing-dinfluence/
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 09:11:33 +0000
- Summary: <a href="https://siecledigital.fr/2026/04/29/comment-lia-est-en-train-de-transformer-le-marketing-dinfluence/" rel="nofollow" title="Comment l’IA est en train de transformer le marketing d’influence"><img alt="Comment l’IA est en train de transformer le marketing d’influence" class="webfeedsFeaturedVisual wp-post-image" height="350" src="https://siecledigital.fr/wp-content/uploads/2026/04/ia-marketing-influence-600x350.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="600" /></a>Il y a 5 ans, un responsable marketing choisissait un profil pour une campagne d’influence à l’instinct ou presque. Désormais, le marketing d’influence a pris une nouvelle dimension et représente déjà un levier business stratégique considérable (un marché mondial estimé à plus de 33 milliards de dollars en 2025). Avec une pression de plus en [&#8230;]

## 109. AI frenzy drives uneven startup funding surge - investordaily.com.au
- Domain: investordaily.com.au
- URL: https://news.google.com/rss/articles/CBMihgFBVV95cUxQVEFKRzBSaVZ5bFBUZUxQUVBabzVUWmVwcTBRblBNNGNFSmdBZUlxcUxRRGY4LWdrc3pUUXVON2otVElUOTdEd0pqOXV4cHg2Mzh5UWhvTEpSX2VHSVByMjI1UlFMV2FBTmc4NjRZN1NCWEQ4d2RZVWxTUjZMTFItbE4tbHAwdw
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 08:47:43 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMihgFBVV95cUxQVEFKRzBSaVZ5bFBUZUxQUVBabzVUWmVwcTBRblBNNGNFSmdBZUlxcUxRRGY4LWdrc3pUUXVON2otVElUOTdEd0pqOXV4cHg2Mzh5UWhvTEpSX2VHSVByMjI1UlFMV2FBTmc4NjRZN1NCWEQ4d2RZVWxTUjZMTFItbE4tbHAwdw?oc=5" target="_blank">AI frenzy drives uneven startup funding surge</a>&nbsp;&nbsp;<font color="#6f6f6f">investordaily.com.au</font>

## 110. smol-audio: A Colab-Friendly Notebook Collection for Fine-Tuning Whisper, Parakeet, Voxtral, Granite Speech, and Audio Flamingo 3
- Domain: marktechpost.com
- URL: https://www.marktechpost.com/2026/04/29/smol-audio-a-colab-friendly-notebook-collection-for-fine-tuning-whisper-parakeet-voxtral-granite-speech-and-audio-flamingo-3/
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 07:31:31 +0000
- Summary: <p>smol-audio Is the Audio AI Cookbook Practitioners Have Been Waiting For</p> <p>The post <a href="https://www.marktechpost.com/2026/04/29/smol-audio-a-colab-friendly-notebook-collection-for-fine-tuning-whisper-parakeet-voxtral-granite-speech-and-audio-flamingo-3/">smol-audio: A Colab-Friendly Notebook Collection for Fine-Tuning Whisper, Parakeet, Voxtral, Granite Speech, and Audio Flamingo 3</a> appeared first on <a href="https://www.marktechpost.com">MarkTechPost</a>.</p>

## 111. China penalizes AI platforms over failure to label AI-generated content
- Domain: technode.com
- URL: https://technode.com/2026/04/29/china-penalizes-ai-platforms-over-failure-to-label-ai-generated-content/
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 05:56:57 +0000
- Summary: <figure><img alt="" class="attachment-rss-image-size size-rss-image-size wp-post-image" height="624" src="https://i0.wp.com/technode.com/wp-content/uploads/2023/03/CapCut.png?fit=1024%2C624&amp;ssl=1" width="1024" /></figure>China’s internet regulator has penalized several digital platforms for failing to properly label AI-generated content, in the latest enforcement action targeting the fast-growing sector. In a notice released on Tuesday, the Cyberspace Administration of China (CAC) said that the apps CapCut, Maoxiang (Cat Box) and Dreamina AI had violated regulations requiring the clear identification of [&#8230;]

## 112. DSO: Direct Steering Optimization for Bias Mitigation
- Domain: machinelearning.apple.com
- URL: https://machinelearning.apple.com/research/direct-steering-optimization
- Relevance score: 5.5
- Published: Wed, 29 Apr 2026 00:00:00 GMT
- Summary: Generative models are often deployed to make decisions on behalf of users, such as vision-language models (VLMs) identifying which person in a room is a doctor to help visually impaired individuals. Yet, VLM decisions are influenced by the perceived demographic attributes of people in the input, which can lead to biased outcomes like failing to identify women as doctors. Moreover, when reducing bias leads to performance loss, users may have varying needs for balancing bias mitigation with overall model capabilities, highlighting the demand for methods that enable controllable bias reduction…

## 113. Georgia wildfires come as much of America is ready to burn
- Domain: axios.com
- URL: https://www.axios.com/2026/04/28/wildfire-season-2026
- Relevance score: 5.5
- Published: Tue, 28 Apr 2026 18:15:25 +0000
- Summary: <div>Data: <a href="https://droughtmonitor.unl.edu/" target="_blank">U.S. Drought Monitor</a>; Map: Axios Visuals</div><p>Georgia's <a href="https://www.axios.com/local/atlanta/2026/04/27/wildfires-burn-acres-drought-south-georgia" target="_blank">wildfires</a> could be a preview of a potentially severe fire season nationwide, with swaths of dried-out land primed to burn from coast to coast.</p><p><strong>Driving the news: </strong>The Highway 82 Fire and Pineland Road Fire have destroyed more than 120 homes, fueled by dry conditions, high winds and leftover debris from 2024's Hurricane Helene.</p><hr /><p><strong>The big picture: </strong>Much of the U.S. is at least "abnormally dry" after long stretches of low precipitation, per the U.S. Drought Monitor.</p><ul><li>Severe, extreme or exceptionally dry conditions prevail across much of the West, South and Southeast, setting the stage for fires.</li></ul><p><strong>By the numbers: </strong>About 1.8 million acres have <a href="https://www.nifc.gov/fire-information/nfn" target="_blank">burned nationwide</a> as of April 24, according to the National Interagency Fire Center (NIFC).</p><ul><li>That's nearly double the year-to-date 10-y

## 114. My Say: The AI mirage: Why firms are accelerating into inefficiency - The Edge Malaysia
- Domain: theedgemalaysia.com
- URL: https://news.google.com/rss/articles/CBMiUEFVX3lxTE9raXVZUl9JYU02RG5wVjRHYXRiQVREbDhKTGRKTTEwY2JMNnZETklzNlRzbENYVXpIMGVJaXZnZjVHODNmOWp4Q1hIVFA5eVVv
- Relevance score: 5.5
- Published: Thu, 30 Apr 2026 05:30:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiUEFVX3lxTE9raXVZUl9JYU02RG5wVjRHYXRiQVREbDhKTGRKTTEwY2JMNnZETklzNlRzbENYVXpIMGVJaXZnZjVHODNmOWp4Q1hIVFA5eVVv?oc=5" target="_blank">My Say: The AI mirage: Why firms are accelerating into inefficiency</a>&nbsp;&nbsp;<font color="#6f6f6f">The Edge Malaysia</font>

## 115. Microsoft, Google, Meta... les géants de l'IA voient leurs bénéfices s'envoler - La Tribune
- Domain: latribune.fr
- URL: https://news.google.com/rss/articles/CBMi5AFBVV95cUxOSHFBbC1VM0VXbERvc1hMeVZlaGEtRTBlZEJDLXNLOWVMU0hhem5ZSlBKNmJHM184X3NUTGk5cDRrM1JUSERRZE9MRXJJU0VFeF9RMl9BTWNuLUpiS19jcWc0ZFFJMERzSnU4UDZpYnNmTmxfeXkzc1RBNGpucFNlVUVOU1R5VHNzRXNSeUpVYzR5V0tDamhFbXNRai1wWTRLZEFxY2pFVFc0RTR6RldvUjkteWpzeTRDbXR1b3A5THM0dzV2Wmhib3NKN0xXWmwxSWt4T0U0Y3R0Z2tpZEo0bTBBZTQ
- Relevance score: 5.5
- Published: Thu, 30 Apr 2026 05:15:42 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi5AFBVV95cUxOSHFBbC1VM0VXbERvc1hMeVZlaGEtRTBlZEJDLXNLOWVMU0hhem5ZSlBKNmJHM184X3NUTGk5cDRrM1JUSERRZE9MRXJJU0VFeF9RMl9BTWNuLUpiS19jcWc0ZFFJMERzSnU4UDZpYnNmTmxfeXkzc1RBNGpucFNlVUVOU1R5VHNzRXNSeUpVYzR5V0tDamhFbXNRai1wWTRLZEFxY2pFVFc0RTR6RldvUjkteWpzeTRDbXR1b3A5THM0dzV2Wmhib3NKN0xXWmwxSWt4T0U0Y3R0Z2tpZEo0bTBBZTQ?oc=5" target="_blank">Microsoft, Google, Meta... les géants de l'IA voient leurs bénéfices s'envoler</a>&nbsp;&nbsp;<font color="#6f6f6f">La Tribune</font>

## 116. Rapper will.i.am teaches ASU class on artificial intelligence in Hollywood - NBC Los Angeles
- Domain: nbclosangeles.com
- URL: https://news.google.com/rss/articles/CBMioAFBVV95cUxNTjhLU0hTU1dRZ3l0b3p3c3pfOUxRMEpMVVpmV3hFM2R0UVg2cnR3VVRXNi0xaTdvTjlWc3hsdDN5YktGS19Nc1UzODdRbjd2SjNaQ2RrRUJBS2luekZyYVJjc2dYVXVHU3I1UGNwQTA4X3ZHM3pMX0pRa0k5VnFXNVRETTdpY2xpaGhZZ3ZwODhzcFlWeFZQQlhjMlZMNzAt0gGoAUFVX3lxTE1KTjVCcUFZbTVySGdkbnlfUVJtbU5GOU1kNTE4OGN1RjRzcW9RZWtqV2llTng5NWdBdjVieXZ0MlJKbWN3NHRucEsxbHRURk9UM3hrY2l0S2JzU1hsNDdmX0ZneGM2VnEyc01SVXRlakNXRndNcUF6TWp1a0VzREF5RnJZNTd3bE84UUxYMjBsN25GWlVzTjM2RUhVNUFwWVNNVHMtM3hwVw
- Relevance score: 5.5
- Published: Thu, 30 Apr 2026 00:44:42 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMioAFBVV95cUxNTjhLU0hTU1dRZ3l0b3p3c3pfOUxRMEpMVVpmV3hFM2R0UVg2cnR3VVRXNi0xaTdvTjlWc3hsdDN5YktGS19Nc1UzODdRbjd2SjNaQ2RrRUJBS2luekZyYVJjc2dYVXVHU3I1UGNwQTA4X3ZHM3pMX0pRa0k5VnFXNVRETTdpY2xpaGhZZ3ZwODhzcFlWeFZQQlhjMlZMNzAt0gGoAUFVX3lxTE1KTjVCcUFZbTVySGdkbnlfUVJtbU5GOU1kNTE4OGN1RjRzcW9RZWtqV2llTng5NWdBdjVieXZ0MlJKbWN3NHRucEsxbHRURk9UM3hrY2l0S2JzU1hsNDdmX0ZneGM2VnEyc01SVXRlakNXRndNcUF6TWp1a0VzREF5RnJZNTd3bE84UUxYMjBsN25GWlVzTjM2RUhVNUFwWVNNVHMtM3hwVw?oc=5" target="_blank">Rapper will.i.am teaches ASU class on artificial intelligence in Hollywood</a>&nbsp;&nbsp;<font color="#6f6f6f">NBC Los Angeles</font>

## 117. Sources: Anthropic could raise a new $50B round at a valuation of $900B
- Domain: techcrunch.com
- URL: https://techcrunch.com/2026/04/29/sources-anthropic-could-raise-a-new-50b-round-at-a-valuation-of-900b/
- Relevance score: 5.5
- Published: Thu, 30 Apr 2026 00:07:15 +0000
- Summary: The maker of Claude has received multiple pre-emptive offers at valuations in the $850 billion to $900 billion range, according to sources familiar with the matter.

## 118. If markets and regulators are ready for network slicing, we are ready: JIO
- Domain: medianama.com
- URL: https://www.medianama.com/2026/04/223-markets-regulators-network-slicing-jio/
- Relevance score: 5.3
- Published: Wed, 29 Apr 2026 13:17:18 +0000
- Summary: <p>Reliance says its 5G network is ready for slicing, but rollout hinges on regulation and demand. Executives also highlighted AI-driven operations, Jamnagar data centres, JioStar updates, and Ajio Rush expansion.</p> <p>The post <a href="https://www.medianama.com/2026/04/223-markets-regulators-network-slicing-jio/">If markets and regulators are ready for network slicing, we are ready: JIO</a> appeared first on <a href="https://www.medianama.com">MEDIANAMA</a>.</p>

## 119. Is The India AI Startup Story Souring?
- Domain: inc42.com
- URL: https://inc42.com/features/is-the-india-ai-startup-story-souring/
- Relevance score: 5.3
- Published: Wed, 29 Apr 2026 05:30:40 +0000
- Summary: <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="1020" src="https://inc42.com/cdn-cgi/image/quality=90/https://asset.inc42.com/2026/04/ftr-2-2.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="1360" />Over the past 18 months, a steady stream of shutdowns has cut across early stage AI startups, raising questions about&#8230;

## 120. Amazon scales its quick delivery service ‘Amazon Now’ in 100 cities
- Domain: medianama.com
- URL: https://www.medianama.com/2026/04/223-amazon-quick-delivery-service-amazon-now-100-cities/
- Relevance score: 5.3
- Published: Tue, 28 Apr 2026 15:58:56 +0000
- Summary: <p>With the availability of its Amazon Now feature in 100 cities, Amazon is trying to strengthen its quick-commerce presence by aiming to reach over 1000 micro-fulfilment centres and developing dark-store-like nodes in them. </p> <p>The post <a href="https://www.medianama.com/2026/04/223-amazon-quick-delivery-service-amazon-now-100-cities/">Amazon scales its quick delivery service &#8216;Amazon Now&#8217; in 100 cities</a> appeared first on <a href="https://www.medianama.com">MEDIANAMA</a>.</p>

## 121. IBM launches AI platform Bob to regulate SDLC costs
- Domain: artificialintelligence-news.com
- URL: https://www.artificialintelligence-news.com/news/ibm-launches-ai-platform-bob-to-regulate-sdlc-costs/
- Relevance score: 5.2
- Published: Tue, 28 Apr 2026 17:34:21 +0000
- Summary: <p>To regulate software delivery costs and SDLC governance, IBM is launching Bob, an AI platform built to anchor enterprise engineering. Accumulated technical debt, hybrid cloud structures, and rigid compliance requirements clash with the raw speed of coding assistants. Without boundaries, they generate unmanaged liabilities rather than functional progress. Dinesh Nirmal, SVP at IBM Software, explained: [&#8230;]</p> <p>The post <a href="https://www.artificialintelligence-news.com/news/ibm-launches-ai-platform-bob-to-regulate-sdlc-costs/">IBM launches AI platform Bob to regulate SDLC costs</a> appeared first on <a href="https://www.artificialintelligence-news.com">AI News</a>.</p>

## 122. 追觅AURORA手机全球亮相，最新估值近百亿美元
- Domain: 36kr.com
- URL: https://36kr.com/newsflashes/3788915767074051
- Relevance score: 5.2
- Published: 2026-04-30 14:04:25  +0800
- Summary: 当地时间4月29日，追觅AURORA手机在美国硅谷发布会上亮相。影像方面，实现全焦段2亿像素、全焦段LOFIC技术、3D空间建模照片；通讯方面，实现360°环绕天线、自研AI通信优化算法、全时信号引擎等技术；追觅AURORA AIOS还打造了原生 AI 系统，实现智能终端从 “执行命令的工具” 向 “主动服务的伙伴” 演进。此外，AURORA手机正按640亿元人民币（约合100亿美元）的估值，推进新一轮融资。

## 123. 「优时科技」完成数亿元B2轮融资，从L4视觉自动驾驶延展至人形机器人，打造数据飞轮｜36氪首发
- Domain: 36kr.com
- URL: https://36kr.com/p/3788687934249989
- Relevance score: 5.2
- Published: 2026-04-30 10:13:18  +0800
- Summary: <p>一季度过去，具身智能行业的融资热潮还在继续。</p> <p>36氪获悉，专注于L4低速自动驾驶的公司「优时科技」宣布完成数亿元人民币B2轮融资。<strong>本轮融资由前海方舟领投，前海母基金旗下多支基金参与，联同鲲翎资本、厚天资本等8家投资机构共同完成。</strong></p> <p>在此之前，「优时科技」已完成了6轮融资：</p> <p>·2018年6月，拿到&nbsp;PNP&nbsp;中国领投、北京汇丰投融、北京金种子和上海平阳复辉跟投的数百万人民币种子轮；</p> <p>·2019年7月，获得英诺天使领投、驰星创投跟投的千万人民币天使轮；</p> <p>·2020年10月，获得&nbsp;Global Brain、英诺天使、驰星创投、PNP&nbsp;中国、平阳复辉的数千万A轮融资；</p> <p>·2022年7月，获得海尔资本、金茂资本、惟一资本投资的数千万A+轮融资；</p> <p>·2023年1月，获得零以创投、厚天资本的数千万A++轮融资；</p> <p>·2024年7月，完成了B1轮融资，由驰星创投、Global Brain投资，金额在数千万元级别。</p> <p>「优时科技」成立于2018年，聚焦于通过计算机视觉实现L4自动驾驶，取代了传统多线激光雷达在低速行驶领域的应用。截至目前，「优时科技」已在海内外商圈、步行街、地铁站、机场等大流量场景部署了数千台「优时小车」，追平了成立于2014年的海外自动驾驶配送头部企业&nbsp;Starship。</p> <p class="image-wrapper"><img src="https://img.36krcdn.com/hsossms/20260430/v2_cd07ad3f5b6d4ca5b6446ba926038e60@5895246_img_000?x-oss-process=image/format,jpg/interlace,1" /></p> <p>「优时科技」CEO林锫森表示：“在人形机器人赛道中，<strong>优时以L4视觉自动驾驶为底座，通过大流量场景验证机器人的通用导航和交互能力，进而平移到人形机器人平台。</strong>这一逻辑与特斯拉（Tesla）从FSD（完全自动驾驶）向人形机器人&nbsp;Optimus&nbsp;延伸的思路相似，两者都是坚持通过‘纯视觉感知算法&nbsp;+&nbsp;物理世界真实数据’，来驱动人形机器人走向通用智能。”</p> <p>“当然，从小车跨越到人形机器人，在机械控制层面存在差异。”&nbsp;林锫森强调，“<strong>优时的核心壁垒并非从零打造一具‘双足躯壳’，而是将成熟的L4视觉算法与空间认知能力，封装为具身机器人的‘社交导航大脑’。</strong>在硬件供应链日益成熟的今天，拥有应对复杂人流量的导航和交互

## 124. 8点1氪丨官方通报“霸王茶姬中喝出水银”；马斯克称创办OpenAI只为拯救人类；三星家族财富一年翻倍至3000亿跃居亚洲第三
- Domain: 36kr.com
- URL: https://36kr.com/p/3788573115735299
- Relevance score: 5.2
- Published: 2026-04-30 08:19:17  +0800
- Summary: <h2>今日热点导览</h2> <ul> <li>四大主播集体离职，东方甄选奖励300名员工超4亿元股份，人均超140万元</li> <li>马斯克天价薪酬方案曝光，薪酬目标包括火星殖民以及太空数据中心建设</li> <li>5月1日起北京禁飞禁售无人机，大疆在京门店4月29日将下架相关产品</li> <li>朋友圈改版，腾讯客服表示会持续优化</li> <li>8天预计发送旅客1.58亿人次，铁路 “五一”假期运输今天启动</li> </ul> <h2>TOP 3大新闻</h2> <p><strong>官方通报“安徽一女子称在霸王茶姬中喝出水银”：异物系购买人投放</strong></p> <p>4月28日，针对网民反映“砀山万达霸王茶姬奶茶中喝出水银”问题，砀山县立即成立由县市场监管局、县公安局等部门组成的联合调查组展开调查。经调查，涉事“霸王茶姬”门店的原材料、生产流程未发现异常。奶茶中异物系购买人投放，目前相关证据已固定并送检，涉案人员已被公安机关控制，案件正在进一步侦办中。</p> <p>据此前报道，近日，安徽宿州，一女子称在霸王茶姬饮品中喝出水银，门店回应：不可能有这种东西，正配合警方及市监局调查。当事人王女士称已报警，后续将向市监局投诉。门店表示高度重视，一切以调查结果为准。（红星新闻）</p> <p><strong>马斯克创办OpenAI只为拯救人类</strong></p> <p>埃隆 · 马斯克与 OpenAI 联合创始人、现任 CEO 萨姆 · 奥尔特曼之间备受关注的庭审已于当地时间周一开庭，马斯克在证人席上将自己定位为“人类的拯救者”。</p> <p>马斯克详细回顾了自己的成长经历，试图让陪审团相信，他所有的商业行为都关乎人类的福祉。他还在法庭上将自己描绘成心系全人类的英雄，并暗示奥尔特曼是反派角色。</p> <p>他表示自己早在大学时期就对AI感到担忧，认为 AI 是一把“双刃剑”，“可以治愈所有疾病、让所有人富足，也可能杀死所有人”。</p> <p>他将 AI 的结局归结为两种：要么是《星际迷航》式的乌托邦，要么是《终结者》式的反乌托邦。他希望吉恩 · 罗登贝里的作品而非詹姆斯 · 卡梅隆的。马斯克称，这也正是他参与创立OpenAI的初衷。（IT之家）</p> <p><strong>AI造富，三星家族财富一年翻倍至3000亿跃居亚洲第三</strong></p> <p>4月29日，据彭博社报道，彭博亿万富翁指数显示，截至今年3月，三星李氏家族的财富总额已从一年前的约201亿美元翻倍至455亿美元(约合3111亿元人民币)左右。2020年，三星电子背后的李氏家族掌门人李健熙(Lee Kun-hee)去世，其家族很快面临双重危机：首当其冲的是高达数十亿美元的遗产税。次年，其子李在镕(Jay Y. Lee)因向前总统朴槿惠行贿以争取对其

## 125. 「微滔生物」A轮次融资超5000万美元，LNP路线体内CAR-T已发表初步人体数据
- Domain: 36kr.com
- URL: https://36kr.com/p/3787339522432256
- Relevance score: 5.2
- Published: 2026-04-30 08:00:00  +0800
- Summary: <p>文｜胡香赟</p> <p>编辑｜海若镜</p> <p>36氪获悉，微滔生物近日接连完成A轮及A+轮融资，累计募资金额超5000万美元。两轮融资分别由正心谷资本和德诚资本领投，OrbiMed（奥博资本）、汉康资本、卫材创新风投基金（Eisai Innovation Inc.）、建发新兴投资，以及老股东启明创投、顺禧基金、杏泽资本等跟投。</p> <p>据了解，微滔生物的A轮次募集资金将主要用于推进核心药物管线GT801的临床进程和注册申报，以及研发团队扩充与平台建设。</p> <p>微滔生物由沙砾生物于2025年拆分成立，后者主要从事肿瘤浸润淋巴细胞（TIL）疗法开发，核心产品已进入临床二期。沙砾生物/微滔生物创始人、CEO刘雅容博士毕业于美国南加州大学，在细胞与基因治疗（CGT）领域拥有10余年从业经历。</p> <p>刘雅容介绍，最初选择做TIL，是因为它是少数有望在实体瘤领域取得突破、且已经迈入商业化阶段的细胞治疗路径，这个过程中，沙砾生物对免疫治疗在不同疾病中的作用机制认知也不断加深，积累起了从“体外工程化”到“体内工程化”的研发能力，因此也逐渐开始通过体内CAR-T路径探索下一代免疫治疗方法。这是沙砾生物将体内CAR-T资产拆分、以微滔生物的形态独立运营的背景。</p> <p>2025年下半年以来，礼来、艾伯维、百时美施贵宝等跨国药企接连开始下场收购海外体内CAR-T公司，累计披露金额已超过140亿美元，由此也引发中国CGT企业对该赛道的研发热情。丁香园Insight数据称，当前，全球在研的体内CAR-T管线超过180条，其中约一半都来自中国。激烈的竞争下，谁能更快积累更多样本数据、做出差异化，很大程度上决定了企业的未来。</p> <p>刘雅容也坦言：“去年，拆分微滔生物的一个现实考虑是，LNP（脂质纳米颗粒）路线的体内CAR-T产品更适合用在自身免疫等领域，而这类适应症在临床开发、团队结构以及资源配置上，都与开发传统肿瘤管线存在明显差异。如果���全放在一个体系内推进，可能并不是最高效、合理的安排。所以我们选择把这一部分能力独立出来，通过单独融资和团队配置，让它能够更聚焦、更快推进。”</p> <p>微滔生物押注的LNP递送路线是体内CAR-T疗法的主流开发路径之一。它主要通过把体外合成的mRNA封装于LNP中，在给药后于人体内实现对T细胞的递送。这个过程不需要插入基因组，因此具备更好的安全性，同时也可以通过剂量和给药频率去调节效果，并且支持重复给药，这使它在自身免疫疾病等需要长期管理的疾病中具有天然优势。</p> <p>从技术储备的角度来说，微滔生物重点积累了三方面的能力：首先是体内递送能力，尤其是如何实现对T细胞的精准递送，其中既包括靶向抗体的筛选，也包括LNP与抗体之间的定点定量偶联设计，这一部分直接决定了转导效率和脱靶控制的平衡。</

## 126. llm 0.32a0
- Domain: simonwillison.net
- URL: https://simonwillison.net/2026/Apr/29/llm-2/
- Relevance score: 5.2
- Published: 2026-04-29T18:57:47+00:00
- Summary: <p><strong>Release:</strong> <a href="https://github.com/simonw/llm/releases/tag/0.32a0">llm 0.32a0</a></p> <p>See <a href="https://simonwillison.net/2026/Apr/29/llm/">the annotated release notes</a>.</p> <p>Tags: <a href="https://simonwillison.net/tags/llm">llm</a></p>

## 127. Databricks can't seem to shake authors' copyright claim that could result in 'extraordinary' damages
- Domain: go.theregister.com
- URL: https://go.theregister.com/feed/www.theregister.com/2026/04/29/databricks_author_copyright_lawsuit_continues/
- Relevance score: 5.2
- Published: 2026-04-29T18:05:14.00Z
- Summary: <h4>Authors say it acquired an LLM that was trained on their copyrighted data, and judge keeps asking for more info</h4> <p>Databricks cannot shake a class action lawsuit targeting its LLM, which several book authors contend was created with a database that contained pirated versions of some of their copyrighted books – and about 196,000 titles in all.…</p>

## 128. 第20届中国投资年会圆满闭幕！ “K型曲线”下，寻找穿越分化的确定性
- Domain: 36kr.com
- URL: https://36kr.com/p/3787806140636420
- Relevance score: 5.2
- Published: 2026-04-29 19:20:42  +0800
- Summary: <p>2026年4月22日至24日，第20届中国投资年会·年度峰会于北京海淀盛大召开。本届大会以“K型曲线”为主题，由北京市海淀区人民政府指导，投中信息、投中网主办，北京中关村科学城创新发展有限公司协办。本届年会连续第二年扎根北京海淀，双方合作正从初次携手走向深度融合。超千名行业领袖、投资人及创业者齐聚海淀，共同研判中国私募股权市场的结构性变局。</p> <p><strong>群贤毕至，重磅嘉宾阵容</strong></p> <p>大会嘉宾阵容星光熠熠，政策、学术、投资与产业的领军人物跨界同席，共同为这场二十年节点上的行业盛会聚力。</p> <p>大会开场，投中信息首席执行官杨晓磊以“K型曲线”为核心主题，描绘了当前中国创投市场两极分化的整体格局——共识与分歧并存、机遇与困境同在，上行与下行曲线同步演进。他表示，当下创投市场并不缺钱，而是进入了一个机会高度分化的时代。头部项目回报显著，只要能参与，往往就能为基金贡献收益；但同时约70%的存量项目仍未退出，幂律效应十分明显。</p> <p>杨晓磊指出，如今一级市场正呈现两个平行世界：一边是AI、芯片、生物技术等赛道融资火热、估值走高；另一边则是大量存量企业长期面临融资困难。今年大会的主题，正是对这种向上与向下并存局面的概括。他认为，这种局面背后是政策、技术与资本三股力量共同推动。国家支持硬科技与新质生产力，二级市场给予科技更高溢价，资金也重新回流一级市场，财富和机会正向具备产业升级能力的赛道集中。</p> <p>对于市场泡沫，他表示，有泡沫，但没有泡沫的市场往往也没有活力。在K型分化时代，关键是看清现实，根据自己的判断，决定是否站上那条上行曲线。</p> <p class="image-wrapper"><img src="https://img.36krcdn.com/hsossms/20260429/v2_6746015d4bf0475181486ac30bf0e196@6381723_oswg1497945oswg2000oswg1333_img_png?x-oss-process=image/quality,q_90/format,jpg/interlace,1" /></p> <p><strong>启明创投创始主管合伙人邝子平在“拥抱周期 穿越周期”主题演讲中表示，</strong>当前创投行业所面对的周期并非单一的资本市场冷暖，而是科技发展、宏观经济、政策环境、人才流动等多重周期交织共振。在他看来，资本市场低迷时，往往也可能正处于科技创新和人才积累的上升阶段，因此投资机构需要识别真正重要的周期，并以长期视角进行布局。启明创投过去20年始终围绕科技发展主线展开投资，在人工智能领域持续沿着技术演进路径布局，从大模型、多模态到具身智能，保持稳定出手节奏。</p> <p>谈及人工智能投资热度，邝子平表示，人

## 129. Trump tells Netanyahu only "surgical" Lebanon strikes as ceasefire falters
- Domain: axios.com
- URL: https://www.axios.com/2026/04/29/israel-lebanon-strikes-trump-interview
- Relevance score: 5.0
- Published: Wed, 29 Apr 2026 21:27:32 +0000
- Summary: <p>President Trump told Prime Minister <a href="https://www.axios.com/2026/04/29/trump-pardon-netanyahu-herzog-national-hero" target="_blank">Benjamin Netanyahu</a> that Israel should only take "surgical" military action in Lebanon and avoid a full resumption of the war, Trump told Axios in a phone interview. </p><p><strong>Why it matters:</strong> The ceasefire Trump helped broker in <a href="https://www.axios.com/2026/04/23/trump-israel-lebanon-ceasefire-extended-talks-us-iran-war" target="_blank">Lebanon</a> is being only partially observed, and officials in both Israel and Lebanon are concerned it will collapse entirely before it's due to expire in mid-May. </p><hr /><ul><li>There has also been no progress in launching Israel-Lebanon peace talks, despite Secretary of State Marco Rubio hosting two meetings with the respective ambassadors.</li><li>And while the Trump administration claims the ceasefire in Lebanon is unconnected to the ceasefire with Iran, a resumption of war there would further complicate diplomacy with Tehran.</li></ul><p><strong>Driving the news:</strong> The Israeli military has continued to occupy southern Lebanon and flatten houses there it claims were used 

## 130. KLA Corp forecasts quarterly revenue above estimates on AI-linked demand - Reuters
- Domain: reuters.com
- URL: https://news.google.com/rss/articles/CBMiqAFBVV95cUxOZFlzZVg4MzRHa2h6dXZ5NWE2d084M0lyRk5YeERRN1FCenNHVXBtcmVDb255Qzh1bFdpV2NTLVczU0JGRVFxcTcxUEY2dFptb3VUVXhKSDZzaTd6NFdrUEtiaG53MjY2cW5fUjAxTUY3Q0FZaXR2eFRTd1BjMVZfMDJGdTVYMGdhQmpQUS1YZ3RKcmt4Q0tKWllOTm5LU2Flc0YxaTNQZ1k
- Relevance score: 5.0
- Published: Wed, 29 Apr 2026 21:17:14 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiqAFBVV95cUxOZFlzZVg4MzRHa2h6dXZ5NWE2d084M0lyRk5YeERRN1FCenNHVXBtcmVDb255Qzh1bFdpV2NTLVczU0JGRVFxcTcxUEY2dFptb3VUVXhKSDZzaTd6NFdrUEtiaG53MjY2cW5fUjAxTUY3Q0FZaXR2eFRTd1BjMVZfMDJGdTVYMGdhQmpQUS1YZ3RKcmt4Q0tKWllOTm5LU2Flc0YxaTNQZ1k?oc=5" target="_blank">KLA Corp forecasts quarterly revenue above estimates on AI-linked demand</a>&nbsp;&nbsp;<font color="#6f6f6f">Reuters</font>

## 131. AI-generated erroneous court filings are ‘rapidly escalating,’ Oregon appeals judge warns - Oregon Capital Chronicle
- Domain: oregoncapitalchronicle.com
- URL: https://news.google.com/rss/articles/CBMiyAFBVV95cUxQbF8zT09QM0JRcVZReUl4ZTdMNFhLeVAzS05tT2ViWVpHa3JTbEhocUtfd1dIbE1xbENSUDhiZjl1ZTNXdGdEcUx5N2ZpRmxidEx0RGU3ZUlhcEQ3ZHoxc1VTU3lHNzRHV0IxSjVoX18xYWxkdE1FVGhwWmpENGsxYW1MTGFxT0c4OFFRUU5PTzcyclVUem50ajE2cXZqcjJtTFQ5ckJNT2FoRTJvMlpzRGxtcUc4RlBvZjl0bW9OaEhreHZJMURWRw
- Relevance score: 5.0
- Published: Wed, 29 Apr 2026 20:22:34 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiyAFBVV95cUxQbF8zT09QM0JRcVZReUl4ZTdMNFhLeVAzS05tT2ViWVpHa3JTbEhocUtfd1dIbE1xbENSUDhiZjl1ZTNXdGdEcUx5N2ZpRmxidEx0RGU3ZUlhcEQ3ZHoxc1VTU3lHNzRHV0IxSjVoX18xYWxkdE1FVGhwWmpENGsxYW1MTGFxT0c4OFFRUU5PTzcyclVUem50ajE2cXZqcjJtTFQ5ckJNT2FoRTJvMlpzRGxtcUc4RlBvZjl0bW9OaEhreHZJMURWRw?oc=5" target="_blank">AI-generated erroneous court filings are ‘rapidly escalating,’ Oregon appeals judge warns</a>&nbsp;&nbsp;<font color="#6f6f6f">Oregon Capital Chronicle</font>

## 132. SCOTUS' voting rights decision deals big down-ballot blow
- Domain: axios.com
- URL: https://www.axios.com/2026/04/29/supreme-court-voting-rights-act-impact
- Relevance score: 5.0
- Published: Wed, 29 Apr 2026 20:17:17 +0000
- Summary: <p>Statehouses, county commissions and city halls — not the halls of Washington — will absorb the heaviest blow from the <a href="https://www.axios.com/2026/04/29/supreme-court-redistricting-race-gerrymander" target="_blank">Voting Rights Act's </a>collapse.</p><p><strong>Why it matters:</strong> Most Voting Rights Act <a href="https://www.brennancenter.org/our-work/research-reports/use-section-2-secure-fair-representation" target="_blank">lawsuits</a> have targeted local and state governments: the entities that decide what's taught in schools, who polices the streets and which neighborhoods get sidewalks.</p><hr /><ul><li>Those suits typically<strong> </strong>fall under Section 2 of the Act, which lets minority voters challenge maps and election rules that weaken their voting power.</li></ul><p><strong>The latest:</strong> The U.S. Supreme Court gutted the Voting Rights Act with a Wednesday decision that essentially gives local and state bodies carte blanche to ignore minority voters as long as it serves some other purpose, like partisan gerrymandering or protecting incumbents.</p><ul><li>Section 2 cases were already notoriously hard to win, with challengers needing to clear thre

## 133. Traditional models still ‘outperform AI’ for extreme weather forecasts - Carbon Brief
- Domain: carbonbrief.org
- URL: https://news.google.com/rss/articles/CBMingFBVV95cUxQY1pCdnNlSnNsdVNJQ2FrM1ZmNkt4MjZXOTJKVG9WQUdjZVlBLTFfeFM5a3NmTkdxdDZ4T0tYQ1NnbW9nSGhmOEUtZk8xQ09FT19BZllsWEl6MEFBVXI1MkNvUUY2RnZpOEVSMEQxT0tKTF9Vbmd1b3liOWk1MlFBTHFPZDBmY2ZjUHpZSFRXRUpud0dybUYwMDdDdDdqUQ
- Relevance score: 5.0
- Published: Wed, 29 Apr 2026 18:56:47 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMingFBVV95cUxQY1pCdnNlSnNsdVNJQ2FrM1ZmNkt4MjZXOTJKVG9WQUdjZVlBLTFfeFM5a3NmTkdxdDZ4T0tYQ1NnbW9nSGhmOEUtZk8xQ09FT19BZllsWEl6MEFBVXI1MkNvUUY2RnZpOEVSMEQxT0tKTF9Vbmd1b3liOWk1MlFBTHFPZDBmY2ZjUHpZSFRXRUpud0dybUYwMDdDdDdqUQ?oc=5" target="_blank">Traditional models still ‘outperform AI’ for extreme weather forecasts</a>&nbsp;&nbsp;<font color="#6f6f6f">Carbon Brief</font>

## 134. «Ne vous souciez pas de votre retraite», Elon Musk évoque la piste du revenu universel dans une société IA - Capital.fr
- Domain: capital.fr
- URL: https://news.google.com/rss/articles/CBMi4wFBVV95cUxPSU9CRl9maXdab1ZvWnJRN0JxVWhmTUpfa3ZZSEItQUhaOTVxZGgxeU90cFN2WWJVek5lOVFrM1FkTV9NaEhNeU9ZYlpFbktkc2VQZjNjX21HclF2cDdBb0hHUkRzbXdjZG5rNjF2UzFuTzc1Tm1Jbk1lVExOa3RhSU1XN2ozTmxnakh5Mk5EZW13b0YxSS0wX3V2b1ZVNi1zenVRNVk4TWNsUm9ueWFTTTh4aEFvLUNVdUhKSWVMVEhSZU1pYmM3Tk9UY1RmSDd1djYweU5Mb2JTVkRZaTZjZG5Qbw
- Relevance score: 5.0
- Published: Wed, 29 Apr 2026 17:15:32 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi4wFBVV95cUxPSU9CRl9maXdab1ZvWnJRN0JxVWhmTUpfa3ZZSEItQUhaOTVxZGgxeU90cFN2WWJVek5lOVFrM1FkTV9NaEhNeU9ZYlpFbktkc2VQZjNjX21HclF2cDdBb0hHUkRzbXdjZG5rNjF2UzFuTzc1Tm1Jbk1lVExOa3RhSU1XN2ozTmxnakh5Mk5EZW13b0YxSS0wX3V2b1ZVNi1zenVRNVk4TWNsUm9ueWFTTTh4aEFvLUNVdUhKSWVMVEhSZU1pYmM3Tk9UY1RmSDd1djYweU5Mb2JTVkRZaTZjZG5Qbw?oc=5" target="_blank">«Ne vous souciez pas de votre retraite», Elon Musk évoque la piste du revenu universel dans une société IA</a>&nbsp;&nbsp;<font color="#6f6f6f">Capital.fr</font>

## 135. Bots, Prescriptions, and P(doom): What AI's Rapid Rise Means for Pharmacy Practice - Pharmacy Times
- Domain: pharmacytimes.com
- URL: https://news.google.com/rss/articles/CBMiswFBVV95cUxQZzltTE91VGFUSkJJMmtjTllLWTZreXE4Zm5KcTljWFV2RkU1OHV4aXc2a1g5YU9PdHNPTmhiTXVtYTV0NFZVNlRkb1hPQTl1SDluZnN2Y1NNdFY0cmgyRUVHLThYakxzNnlaRGhOTC0zNnl3UWtzaTByektQT2h6RWExSU1lZ0k5a2JzdGtzTG4tS2l0aXV2NHNoemFGeHpSNnhObUpGdmYwWUxLYkxHX3FzWQ
- Relevance score: 5.0
- Published: Wed, 29 Apr 2026 16:23:24 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiswFBVV95cUxQZzltTE91VGFUSkJJMmtjTllLWTZreXE4Zm5KcTljWFV2RkU1OHV4aXc2a1g5YU9PdHNPTmhiTXVtYTV0NFZVNlRkb1hPQTl1SDluZnN2Y1NNdFY0cmgyRUVHLThYakxzNnlaRGhOTC0zNnl3UWtzaTByektQT2h6RWExSU1lZ0k5a2JzdGtzTG4tS2l0aXV2NHNoemFGeHpSNnhObUpGdmYwWUxLYkxHX3FzWQ?oc=5" target="_blank">Bots, Prescriptions, and P(doom): What AI's Rapid Rise Means for Pharmacy Practice</a>&nbsp;&nbsp;<font color="#6f6f6f">Pharmacy Times</font>

## 136. What Health Care Leaders Have Learned From Deploying AI - AJMC
- Domain: ajmc.com
- URL: https://news.google.com/rss/articles/CBMiiAFBVV95cUxQS0c3N1M0SHV1R1kwdHVGc3Nuamg4MFFPeE9BLUJvdkFUYkhXNjQ4ampZTFItdzU1cTBlUHJodXRzQ1JzeWtZTVpaQlR0VFNxWVJIdGFpMmJwWUdTTEF0d25ZZHF5RXRYRzEyOG55anV5dk8xRDRSMDV0NG1mRUlzODR6aThDR3lW
- Relevance score: 5.0
- Published: Wed, 29 Apr 2026 15:16:16 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiiAFBVV95cUxQS0c3N1M0SHV1R1kwdHVGc3Nuamg4MFFPeE9BLUJvdkFUYkhXNjQ4ampZTFItdzU1cTBlUHJodXRzQ1JzeWtZTVpaQlR0VFNxWVJIdGFpMmJwWUdTTEF0d25ZZHF5RXRYRzEyOG55anV5dk8xRDRSMDV0NG1mRUlzODR6aThDR3lW?oc=5" target="_blank">What Health Care Leaders Have Learned From Deploying AI</a>&nbsp;&nbsp;<font color="#6f6f6f">AJMC</font>

## 137. AI in Medicine is Not the End of Doctors, but a Warning to Put Empathy First, say SHRO Researchers in JAMA Opinion Article | Newswise - Newswise
- Domain: newswise.com
- URL: https://news.google.com/rss/articles/CBMi6gFBVV95cUxQNFJVdGF1X1oxOWxqeGNxY09neFUwYWl1eklsWEJmSTVxNEJhb3VMWEx0Z0ZYaWowbld0Qm05eXFGTy0zUllEaE9yQjREbmY5VHBEZHlPLUhYUjBmWFZxZk00ZEZUOS1jX0ZHOXRsRG54Wk9rNlNpcG1BUFdpa0xvQy1NbmNCRnczN2FXNm8tVXJhWFZyUFBhUEphSEFuWGNOb3ppZ3UxTy01ZGVKTW9WN25xRkNBWW9yWW4xUktPbklqS0htYWpVT0dZYkxpUlpOWjM4Vm45SE9zcXYwZUFDbzVibEhqd2k0bGfSAeoBQVVfeXFMUDRSVXRhdV9aMTlsanhjcWNPZ3hVMGFpdXpJbFhCZkk1cTRCYW91TFhMdGdGWGlqMG5XdEJtOXlxRk8tM1JZRGhPckI0RG5mOVRwRGR5Ty1IWFIwZlhWcWZNNGRGVDktY19GRzl0bERueFpPazZTaXBtQVBXaWtMb0MtTW5jQkZ3MzdhVzZvLVVyYVhWclBQYVBKYUhBblhjTm96aWd1MU8tNWRlSk1vVjducUZDQVlvclluMVJLT25JaktIbWFqVU9HWWJMaVJaTlozOFZuOUhPc3F2MGVBQ281YmxIandpNGxn
- Relevance score: 5.0
- Published: Wed, 29 Apr 2026 12:40:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi6gFBVV95cUxQNFJVdGF1X1oxOWxqeGNxY09neFUwYWl1eklsWEJmSTVxNEJhb3VMWEx0Z0ZYaWowbld0Qm05eXFGTy0zUllEaE9yQjREbmY5VHBEZHlPLUhYUjBmWFZxZk00ZEZUOS1jX0ZHOXRsRG54Wk9rNlNpcG1BUFdpa0xvQy1NbmNCRnczN2FXNm8tVXJhWFZyUFBhUEphSEFuWGNOb3ppZ3UxTy01ZGVKTW9WN25xRkNBWW9yWW4xUktPbklqS0htYWpVT0dZYkxpUlpOWjM4Vm45SE9zcXYwZUFDbzVibEhqd2k0bGfSAeoBQVVfeXFMUDRSVXRhdV9aMTlsanhjcWNPZ3hVMGFpdXpJbFhCZkk1cTRCYW91TFhMdGdGWGlqMG5XdEJtOXlxRk8tM1JZRGhPckI0RG5mOVRwRGR5Ty1IWFIwZlhWcWZNNGRGVDktY19GRzl0bERueFpPazZTaXBtQVBXaWtMb0MtTW5jQkZ3MzdhVzZvLVVyYVhWclBQYVBKYUhBblhjTm96aWd1MU8tNWRlSk1vVjducUZDQVlvclluMVJLT25JaktIbWFqVU9HWWJMaVJaTlozOFZuOUhPc3F2MGVBQ281YmxIandpNGxn?oc=5" target="_blank">AI in Medicine is Not the End of Doctors, but a Warning to Put Empathy First, say SHRO Researchers in JAMA Opinion Article | Newswise</a>&nbsp;&nbsp;<font color="#6f6f6f">Newswise</font>

## 138. I got stood up by an AI agent, and tracked down its human owner in China
- Domain: restofworld.org
- URL: https://restofworld.org/2026/ai-agent-china-one-person-company/
- Relevance score: 5.0
- Published: Wed, 29 Apr 2026 10:00:00 +0000
- Summary: A solo entrepreneur is paying a quarter of his salary to let AI agents run his side-hustle app. He recently realized his "employees" have been keeping secrets.

## 139. SK Group Drives Vietnam’s AI Ambitions with New Partnerships - Telecom Review Asia
- Domain: telecomreviewasia.com
- URL: https://news.google.com/rss/articles/CBMiuwFBVV95cUxOZXU4UUZkVG5iV1lzUzNyQWY4Tmg3amsyMFpTVWJMN3NQaVVyZGVZVktTc0MzelBTTFlqR0NhSzQwOVo2TXdKZGlKN0Faa21hSUZUTXl0UE1uVTJlaUl1U0x0SW8yYmNndWxRUDBKUjJSVDZKRXlNWjBPcG1tRVlOUGRWVnpqZkoyQmhPVnJNTUZXbXRYUFV5VXhwQXBYRWNzQmRNcHI5WjZlLUxZcnh0UjBkN1RmS1VCc3dR
- Relevance score: 5.0
- Published: Wed, 29 Apr 2026 08:52:35 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiuwFBVV95cUxOZXU4UUZkVG5iV1lzUzNyQWY4Tmg3amsyMFpTVWJMN3NQaVVyZGVZVktTc0MzelBTTFlqR0NhSzQwOVo2TXdKZGlKN0Faa21hSUZUTXl0UE1uVTJlaUl1U0x0SW8yYmNndWxRUDBKUjJSVDZKRXlNWjBPcG1tRVlOUGRWVnpqZkoyQmhPVnJNTUZXbXRYUFV5VXhwQXBYRWNzQmRNcHI5WjZlLUxZcnh0UjBkN1RmS1VCc3dR?oc=5" target="_blank">SK Group Drives Vietnam’s AI Ambitions with New Partnerships</a>&nbsp;&nbsp;<font color="#6f6f6f">Telecom Review Asia</font>

## 140. New DeepSeek model marks AI milestone. Is China closing the gap with the US? - The Straits Times
- Domain: straitstimes.com
- URL: https://news.google.com/rss/articles/CBMi1gFBVV95cUxPLUVTZEI2MkVGUk1qaDk1VnRJYWFyRU13T2J6anhVUDdzRkozcDRvZEpaeGtPX0g4cUhjNEw4ZDBGcE03V0E4LUlGa0FnRWs2MnhTT3dEcThZMXYwWGtFM285TFhpb2dFVHlBLUJzUXVjaktIcko0Z24tNkVKdTZwTzZQYzhLY3I0dTNYcUo1b2lELVhJR0pQcmJHb0pSRzVxeGowQUxOZUJtenEwc0YzdUpwcmVfQUgxeW4yUUd2d2szUlB3UXAzbmJBVFZ6Wng0YWtOdHlR
- Relevance score: 5.0
- Published: Wed, 29 Apr 2026 07:00:52 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi1gFBVV95cUxPLUVTZEI2MkVGUk1qaDk1VnRJYWFyRU13T2J6anhVUDdzRkozcDRvZEpaeGtPX0g4cUhjNEw4ZDBGcE03V0E4LUlGa0FnRWs2MnhTT3dEcThZMXYwWGtFM285TFhpb2dFVHlBLUJzUXVjaktIcko0Z24tNkVKdTZwTzZQYzhLY3I0dTNYcUo1b2lELVhJR0pQcmJHb0pSRzVxeGowQUxOZUJtenEwc0YzdUpwcmVfQUgxeW4yUUd2d2szUlB3UXAzbmJBVFZ6Wng0YWtOdHlR?oc=5" target="_blank">New DeepSeek model marks AI milestone. Is China closing the gap with the US?</a>&nbsp;&nbsp;<font color="#6f6f6f">The Straits Times</font>

## 141. Market Spotlight: Wall Street braces for tech earnings and Powell’s final Fed meeting - The Economic Times
- Domain: m.economictimes.com
- URL: https://news.google.com/rss/articles/CBMimwJBVV95cUxOZDVmRklvSlgtWFN1ZC1ZdFVCTjRCbE85X3VUQjJtNWZ0RjlxTzNuaFhzajZJbm1vNFB2ZnJnR3RTdHdQQ0dqM3hFZzJaVHROR0pnSkNGMUtORktfZXJlTGFid1UwQWt2N0F0ZDNiVG50SmdDT1BLZnB1TVllcTFWVW5Kb1ZBV0VDQWFwSy03enZxRHZZNHBqSlFNREsyZFY5b2lqWkNFcUpUX0ljeC1ySm5FaGNmMFV1OWdQdncyZkdacWVOdW5Xc0FHQ1gtNTZaNEtHMkY0RDFaSEtuYlRJZ3NDdTVOdGtLNi1RUGNSVzhOLXRiTVA3dTJQNGNxRlZmY3dEVDZOTlVoY05TWGt4ai1zOTZkZ1M1R1Fn
- Relevance score: 5.0
- Published: Wed, 29 Apr 2026 06:52:43 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMimwJBVV95cUxOZDVmRklvSlgtWFN1ZC1ZdFVCTjRCbE85X3VUQjJtNWZ0RjlxTzNuaFhzajZJbm1vNFB2ZnJnR3RTdHdQQ0dqM3hFZzJaVHROR0pnSkNGMUtORktfZXJlTGFid1UwQWt2N0F0ZDNiVG50SmdDT1BLZnB1TVllcTFWVW5Kb1ZBV0VDQWFwSy03enZxRHZZNHBqSlFNREsyZFY5b2lqWkNFcUpUX0ljeC1ySm5FaGNmMFV1OWdQdncyZkdacWVOdW5Xc0FHQ1gtNTZaNEtHMkY0RDFaSEtuYlRJZ3NDdTVOdGtLNi1RUGNSVzhOLXRiTVA3dTJQNGNxRlZmY3dEVDZOTlVoY05TWGt4ai1zOTZkZ1M1R1Fn?oc=5" target="_blank">Market Spotlight: Wall Street braces for tech earnings and Powell’s final Fed meeting</a>&nbsp;&nbsp;<font color="#6f6f6f">The Economic Times</font>

## 142. The MIT-IBM Computing Research Lab launches to shape the future of AI and quantum computing
- Domain: news.mit.edu
- URL: https://news.mit.edu/2026/mit-ibm-computing-research-lab-launches-0429
- Relevance score: 5.0
- Published: Wed, 29 Apr 2026 06:00:00 -0400
- Summary: Building on a long-standing MIT–IBM collaboration, the new lab will chart the convergence of AI, algorithms, and quantum computing.

## 143. Mickey Mouse is watching you: Disneyland deploys facial recognition
- Domain: theguardian.com
- URL: https://www.theguardian.com/us-news/2026/apr/28/disneyland-entrance-facial-recognition
- Relevance score: 5.0
- Published: Wed, 29 Apr 2026 01:44:42 GMT
- Summary: <p>Walt Disney Company says technology at California theme park will prevent fraud and streamline re-entry</p><p>Disneyland, the beloved California adventure park, has outfitted some entrance lanes with facial recognition technology, a move its parent company <a href="https://privacy.thewaltdisneycompany.com/en/resortfr/#:~:text=This%20technology%20is%20being%20evaluated,in%20this%20test%20is%20optional.">says</a> will prevent fraud and streamline re-entry.</p><p>At certain entrance lanes, a camera will capture images of visitors, which can be converted via biometric technology into unique numerical values, according to the Walt Disney Company’s website.</p> <a href="https://www.theguardian.com/us-news/2026/apr/28/disneyland-entrance-facial-recognition">Continue reading...</a>

## 144. Senate rejects curb on Trump military action in Cuba
- Domain: axios.com
- URL: https://www.axios.com/2026/04/28/cuba-war-powers-senate-vote-tim-kaine-trump
- Relevance score: 5.0
- Published: Tue, 28 Apr 2026 22:04:55 +0000
- Summary: <p>The Senate rejected an effort to advance legislation that would bar U.S. <a href="https://www.axios.com/2026/04/17/cuba-negotiations-trump-havana-castro" target="_blank">military action against Cuba</a> without Congress' green light. </p><p><strong>Why it matters</strong>: It's lawmakers' latest <a href="https://www.axios.com/2026/04/16/iran-war-powers-trump-democrats-congress-house" target="_blank">failed attempt</a> to rein in Trump's use of military force overseas, underscoring the support he maintains from Republicans who control Capitol Hill. </p><hr /><ul><li>The vote was 51-47 on Tuesday in favor of blocking the resolution from moving forward.</li><li>Republicans Susan Collins of Maine and Rand Paul of Kentucky voted in favor of advancing the measure. Pennsylvania's John Fetterman was the only Democrat in opposition. </li></ul><p><strong>The big picture</strong>: Trump has escalated pressure on Cuba this year with a de facto maritime blockade while openly floating the possibility of military action.</p><ul><li>The U.S. has used <a href="https://www.nytimes.com/2026/03/29/world/americas/cuba-russian-oil-tanlker.html" target="_blank">Coast Guard and naval assets </a>to inte

## 145. Nvidia stock falls. What’s hitting AMD, Broadcom and the AI chip players? - MSN
- Domain: msn.com
- URL: https://news.google.com/rss/articles/CBMi5AFBVV95cUxPa3VFdkYxbW0xUUY1U3RUUUxaSVhldWR3ay1sZFJqWWpCdktmSjdDcFhrZ19GYm4xRnVJSUsyMXVQVjhMclNWUlA0UHBtUFVuQmc0MzJRYkZnVXBkLUNlY25kdEJWUDNmYWJKMTZVQ2Nvc1ZEbG5FdGZLWHVXb29jX29tdzBLN3hZa2dxMGFZdk9vRHJmMkJMSjBvYlB3b3hZVm9EcEFwWTJBZ1JWMGNIZjJTUXBYU3RienUtWTVORUJPNkxDVERjOWVRRzFHVThCU1hXb0NHVVN0YmZJeHdZUTJUNUg
- Relevance score: 5.0
- Published: Tue, 28 Apr 2026 17:08:23 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi5AFBVV95cUxPa3VFdkYxbW0xUUY1U3RUUUxaSVhldWR3ay1sZFJqWWpCdktmSjdDcFhrZ19GYm4xRnVJSUsyMXVQVjhMclNWUlA0UHBtUFVuQmc0MzJRYkZnVXBkLUNlY25kdEJWUDNmYWJKMTZVQ2Nvc1ZEbG5FdGZLWHVXb29jX29tdzBLN3hZa2dxMGFZdk9vRHJmMkJMSjBvYlB3b3hZVm9EcEFwWTJBZ1JWMGNIZjJTUXBYU3RienUtWTVORUJPNkxDVERjOWVRRzFHVThCU1hXb0NHVVN0YmZJeHdZUTJUNUg?oc=5" target="_blank">Nvidia stock falls. What’s hitting AMD, Broadcom and the AI chip players?</a>&nbsp;&nbsp;<font color="#6f6f6f">MSN</font>

## 146. LG CNS rides AI boom to achieve strong first-quarter earnings growth - The Korea Times
- Domain: koreatimes.co.kr
- URL: https://news.google.com/rss/articles/CBMitgFBVV95cUxNblRtV21Gb09FQ252S3RMR1pmYVFTaGwzMDlsZUh3akFrU3NwM2RVYjVaeUM3WW93a2EtOEdtRUM2S3EyaWhFaTdxemN3dm12WE5ZN2VGYzRRMHd2dWpfNTVqWUowWXlEbWlHRXRRVHB0Yko3OTQ4aHllSk5NRHJVQ2Z0eS1tbXFmRW9CTUVzay1OY0NUNnM1VmdYeDBXVzFwNEJ4ek83REZvNDROUUdJXzBmYmJld9IBuwFBVV95cUxNX0FWc0ZOejBCa242akxfSkNyalVNU0Y3SW43T1FleUUyRkdUM3pRc1VtT2J1elBzeEl6Ri1BUHlfV1ozSlpBdndfQjd4V3d0Tm9kdlNvUVFsTFZGdnIxMEVVTF9KVWl5eTA4SVFod2tVZnpyWW9MV0kzOXdfVzRXYVVpajZTM0ZSYjR5bDlleXVIZHk4NWFQak5kakkxMEN3RWUwcDA5LXZhWWd6OVpFdGRNX0JNMlo4Tldv
- Relevance score: 5.0
- Published: Thu, 30 Apr 2026 05:50:03 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMitgFBVV95cUxNblRtV21Gb09FQ252S3RMR1pmYVFTaGwzMDlsZUh3akFrU3NwM2RVYjVaeUM3WW93a2EtOEdtRUM2S3EyaWhFaTdxemN3dm12WE5ZN2VGYzRRMHd2dWpfNTVqWUowWXlEbWlHRXRRVHB0Yko3OTQ4aHllSk5NRHJVQ2Z0eS1tbXFmRW9CTUVzay1OY0NUNnM1VmdYeDBXVzFwNEJ4ek83REZvNDROUUdJXzBmYmJld9IBuwFBVV95cUxNX0FWc0ZOejBCa242akxfSkNyalVNU0Y3SW43T1FleUUyRkdUM3pRc1VtT2J1elBzeEl6Ri1BUHlfV1ozSlpBdndfQjd4V3d0Tm9kdlNvUVFsTFZGdnIxMEVVTF9KVWl5eTA4SVFod2tVZnpyWW9MV0kzOXdfVzRXYVVpajZTM0ZSYjR5bDlleXVIZHk4NWFQak5kakkxMEN3RWUwcDA5LXZhWWd6OVpFdGRNX0JNMlo4Tldv?oc=5" target="_blank">LG CNS rides AI boom to achieve strong first-quarter earnings growth</a>&nbsp;&nbsp;<font color="#6f6f6f">The Korea Times</font>

## 147. Jeff Moss urges global collaboration in AI advancement on Day 2 of MTX (Milipol TechX Summit) 2026 - HTX | Home Team Science and Technology Agency
- Domain: htx.gov.sg
- URL: https://news.google.com/rss/articles/CBMi3wFBVV95cUxQOVRWV3FMVEQ3SjRkU2FsU1lhNVBmNkl2OTF5TWVINGdqQUxNNEQ1X1EyRG8zbHNqcW1CSFlpNnJQWE10dFRUeDgwY2RvMzJyUU5BQjRJcFYzby16enRaUTlraHp3bFhRYk8wOUdMVTU5Tm9xWnc4M2ZYdzQzbkdhejhESnZzN2xuZ29PQ1BxRmJJM1VVLU8yRElHd3kzb3RyWGNXVFU0azc0WXhXOHczcGJtc0I0WnJOWlY4eFR4YnFzc1o1QzgxMTQ4cUVfZ3AyaWIwRWc1TE1iMFJiZGhF
- Relevance score: 5.0
- Published: Thu, 30 Apr 2026 05:11:12 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi3wFBVV95cUxQOVRWV3FMVEQ3SjRkU2FsU1lhNVBmNkl2OTF5TWVINGdqQUxNNEQ1X1EyRG8zbHNqcW1CSFlpNnJQWE10dFRUeDgwY2RvMzJyUU5BQjRJcFYzby16enRaUTlraHp3bFhRYk8wOUdMVTU5Tm9xWnc4M2ZYdzQzbkdhejhESnZzN2xuZ29PQ1BxRmJJM1VVLU8yRElHd3kzb3RyWGNXVFU0azc0WXhXOHczcGJtc0I0WnJOWlY4eFR4YnFzc1o1QzgxMTQ4cUVfZ3AyaWIwRWc1TE1iMFJiZGhF?oc=5" target="_blank">Jeff Moss urges global collaboration in AI advancement on Day 2 of MTX (Milipol TechX Summit) 2026</a>&nbsp;&nbsp;<font color="#6f6f6f">HTX | Home Team Science and Technology Agency</font>

## 148. Cognizant layoffs: IT giant to cut 4,000 jobs as Project Leap boosts AI, automation and reshapes global workfo - CNBC TV18
- Domain: cnbctv18.com
- URL: https://news.google.com/rss/articles/CBMiuAFBVV95cUxPVmdqdnUyRDFQanlCNDFJM21qbzVJNGFJb1B2R0xSU2hmcndlNTk0eERHc25MVHVCaWFkODlEbUs5X1VsWklpclNJdk9LUXRqY2YxelRwSzEySzBQVU5LT3ZEMzNSQVl0ckxRMGtldWxRamFFdFIwZS0wR2NJakI0ZXl6Skw2djNHc0U4SnZydThza2pUNVctZ0pWcTF4LTEwc19pV3hpUjdBNzNBc29NSTUwdDBJcmct0gG-AUFVX3lxTE5IQzVxTFptMlNXaUJQZ2t6VXFpbmNHcjJPZk8xR3ZPSk9vTUdMQ0w5QTAweVh4WUl6TEJkRE9fSHRyVUhDTkpNMXFoOW9tODhqX3EyS1YzclFsQkpmTUtwZlU3UFg2Mnkza2lISGpnT2toazd4ZGxVZWhHRm56ZmtOSko0RFNxWDRDR3VpOGt3ZlI4X2RqWUFrNnFoeDJCUWZkV0kxT3hPTF80SHNnRlZXSXlOUWIwRl9RZTc3amc
- Relevance score: 5.0
- Published: Thu, 30 Apr 2026 05:01:59 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiuAFBVV95cUxPVmdqdnUyRDFQanlCNDFJM21qbzVJNGFJb1B2R0xSU2hmcndlNTk0eERHc25MVHVCaWFkODlEbUs5X1VsWklpclNJdk9LUXRqY2YxelRwSzEySzBQVU5LT3ZEMzNSQVl0ckxRMGtldWxRamFFdFIwZS0wR2NJakI0ZXl6Skw2djNHc0U4SnZydThza2pUNVctZ0pWcTF4LTEwc19pV3hpUjdBNzNBc29NSTUwdDBJcmct0gG-AUFVX3lxTE5IQzVxTFptMlNXaUJQZ2t6VXFpbmNHcjJPZk8xR3ZPSk9vTUdMQ0w5QTAweVh4WUl6TEJkRE9fSHRyVUhDTkpNMXFoOW9tODhqX3EyS1YzclFsQkpmTUtwZlU3UFg2Mnkza2lISGpnT2toazd4ZGxVZWhHRm56ZmtOSko0RFNxWDRDR3VpOGt3ZlI4X2RqWUFrNnFoeDJCUWZkV0kxT3hPTF80SHNnRlZXSXlOUWIwRl9RZTc3amc?oc=5" target="_blank">Cognizant layoffs: IT giant to cut 4,000 jobs as Project Leap boosts AI, automation and reshapes global workfo</a>&nbsp;&nbsp;<font color="#6f6f6f">CNBC TV18</font>

## 149. Cognizant starts charging for AI alongside human work in new pricing model - People Matters - HR News
- Domain: peoplematters.in
- URL: https://news.google.com/rss/articles/CBMi0AFBVV95cUxPaW5DeXh2UWpNS2ZpYmE3TEx6S3ltU0tYV0JjWEhIcHBEa0hKS0pVYWQxYnNpOXZINjVPeE9pN3BvZWpZZTVaX0FqR2dUcjhYNWExYlVFdnQ1RTFtUFJZd0ctMDhtS3R2NkwwR2FYTTAxdjNjUDBJdUN2Y1hZbzZRaFJGSXFnTmJVOTl1UlZqNXR5d1dnQUJYZFVEQmN1TG9oSnR6LUppUm5JSW1OX2lNVlBscThYclJJOE5ZMkVxVE1BenFjcDB4amdpcVI5UFF4
- Relevance score: 5.0
- Published: Thu, 30 Apr 2026 05:00:54 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi0AFBVV95cUxPaW5DeXh2UWpNS2ZpYmE3TEx6S3ltU0tYV0JjWEhIcHBEa0hKS0pVYWQxYnNpOXZINjVPeE9pN3BvZWpZZTVaX0FqR2dUcjhYNWExYlVFdnQ1RTFtUFJZd0ctMDhtS3R2NkwwR2FYTTAxdjNjUDBJdUN2Y1hZbzZRaFJGSXFnTmJVOTl1UlZqNXR5d1dnQUJYZFVEQmN1TG9oSnR6LUppUm5JSW1OX2lNVlBscThYclJJOE5ZMkVxVE1BenFjcDB4amdpcVI5UFF4?oc=5" target="_blank">Cognizant starts charging for AI alongside human work in new pricing model</a>&nbsp;&nbsp;<font color="#6f6f6f">People Matters - HR News</font>

## 150. Alphabet’s cloud unit beats quarterly revenue estimates on strong AI demand - DD News
- Domain: ddnews.gov.in
- URL: https://news.google.com/rss/articles/CBMiogFBVV95cUxOYXVyQXBuQkQxUzJMU1hyMV9OcUxKemhrY3prY0FiZXJhZDZYMjFmOWtidXA5WkNucE9DREM2QmNKMmh5UTdKbzNtYWRaVzZRRGRidlZYN09iQ3M4ZnZTTmRrWmotYjc0cUJBTFVzWlljZHd2cWNsWi1naF9XQWlWc3hLX19uQUgtYUgyQXRqME92RFZxa0F5NFNUd1Nrek54Z2c
- Relevance score: 5.0
- Published: Thu, 30 Apr 2026 04:56:54 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxOYXVyQXBuQkQxUzJMU1hyMV9OcUxKemhrY3prY0FiZXJhZDZYMjFmOWtidXA5WkNucE9DREM2QmNKMmh5UTdKbzNtYWRaVzZRRGRidlZYN09iQ3M4ZnZTTmRrWmotYjc0cUJBTFVzWlljZHd2cWNsWi1naF9XQWlWc3hLX19uQUgtYUgyQXRqME92RFZxa0F5NFNUd1Nrek54Z2c?oc=5" target="_blank">Alphabet’s cloud unit beats quarterly revenue estimates on strong AI demand</a>&nbsp;&nbsp;<font color="#6f6f6f">DD News</font>

## 151. What Is An AI Data Centre? Inside The Powerful Tech Hubs Shaping The Future - News18
- Domain: news18.com
- URL: https://news.google.com/rss/articles/CBMi0AFBVV95cUxNbkVxY3NYV1lCWngzSVFoUGpqMklFNEJEZ2tvS1JJZjcyWk5TOWswRTQ0QjJqYkttVzZoaU9zYXFtV3pWU3NzT2JhMG9OcU1wakQwak1UQkpuekF5bGtDRXpTOWp5RjdxTGFzbXJRa0dtako2YXJYMzVBREQ5N0NzcnJXdGRQM1FzaU1GOFlsQXh6d3pTaGZ6RkwzcHBLQlBOejRfOG1PYXFFZ2JlSEVTTG9IRkVHQ2FPeE91QTdpeDV5XzNxS2xjN2FQdlRFaTdS0gHWAUFVX3lxTE5UQy02d1NoeDdHZ3lXd2NhQXZNR3pDTDVIcVNTYWQ4emdhM21MQ2Mwc2lEcy05OUdLMjlTRWF0UlBsdmc2REdUSjRPVXAwcklRS21pOUQzclF0am9sZjgyMGVMYy1vQTh3SnRSS1k0ZEZnblBlMGw2cWFvc2UxMnZXZ1NnUFY0bngwbEZZT195WHlVbEw4ZVVJbm5vcmNNOUpCbUJXZktObzZlYUNxZW1zRTNEaERHWUtJX3pleTEtUV9MQlFoMWVqREliaUxEWUhMRnJMc0E
- Relevance score: 5.0
- Published: Thu, 30 Apr 2026 04:14:33 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi0AFBVV95cUxNbkVxY3NYV1lCWngzSVFoUGpqMklFNEJEZ2tvS1JJZjcyWk5TOWswRTQ0QjJqYkttVzZoaU9zYXFtV3pWU3NzT2JhMG9OcU1wakQwak1UQkpuekF5bGtDRXpTOWp5RjdxTGFzbXJRa0dtako2YXJYMzVBREQ5N0NzcnJXdGRQM1FzaU1GOFlsQXh6d3pTaGZ6RkwzcHBLQlBOejRfOG1PYXFFZ2JlSEVTTG9IRkVHQ2FPeE91QTdpeDV5XzNxS2xjN2FQdlRFaTdS0gHWAUFVX3lxTE5UQy02d1NoeDdHZ3lXd2NhQXZNR3pDTDVIcVNTYWQ4emdhM21MQ2Mwc2lEcy05OUdLMjlTRWF0UlBsdmc2REdUSjRPVXAwcklRS21pOUQzclF0am9sZjgyMGVMYy1vQTh3SnRSS1k0ZEZnblBlMGw2cWFvc2UxMnZXZ1NnUFY0bngwbEZZT195WHlVbEw4ZVVJbm5vcmNNOUpCbUJXZktObzZlYUNxZW1zRTNEaERHWUtJX3pleTEtUV9MQlFoMWVqREliaUxEWUhMRnJMc0E?oc=5" target="_blank">What Is An AI Data Centre? Inside The Powerful Tech Hubs Shaping The Future</a>&nbsp;&nbsp;<font color="#6f6f6f">News18</font>

## 152. Samsung’s chip profit soars 48-times due to AI spending frenzy - The Business Times
- Domain: businesstimes.com.sg
- URL: https://news.google.com/rss/articles/CBMixgFBVV95cUxOeXJaZFJtN2RQZlVtdUd1a3hJS2NTOFJ2Q2xxaTIxTjRWVEpQMlFiSVJyb3N3RXRiTHJYXzJiM1BSOTlMV2xwR0dZV18yLUMtbktwUzh3NTNhYU5yS09HdFR6NGZnMjcyNTFsMmgwT1l4UmtIVVZCcy1CVVBrMmFfNHZTMzVMY2IxbDFWMFB2SHo1aUFiRno2Mi0yclRNc2xLSlJKZ1cxTjd5V1RITWFNSmktbk8yNGVoNUVBbGVpLUR5cjlJdEE
- Relevance score: 5.0
- Published: Thu, 30 Apr 2026 03:16:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMixgFBVV95cUxOeXJaZFJtN2RQZlVtdUd1a3hJS2NTOFJ2Q2xxaTIxTjRWVEpQMlFiSVJyb3N3RXRiTHJYXzJiM1BSOTlMV2xwR0dZV18yLUMtbktwUzh3NTNhYU5yS09HdFR6NGZnMjcyNTFsMmgwT1l4UmtIVVZCcy1CVVBrMmFfNHZTMzVMY2IxbDFWMFB2SHo1aUFiRno2Mi0yclRNc2xLSlJKZ1cxTjd5V1RITWFNSmktbk8yNGVoNUVBbGVpLUR5cjlJdEE?oc=5" target="_blank">Samsung’s chip profit soars 48-times due to AI spending frenzy</a>&nbsp;&nbsp;<font color="#6f6f6f">The Business Times</font>

## 153. AI-integrated MSc courses launched - The Hans India
- Domain: thehansindia.com
- URL: https://news.google.com/rss/articles/CBMijwFBVV95cUxPeWg1MHM2eUZCX0I2SzEwQnF2Y0NZS0lmOHl4d1ZINkJPaERCYTBhbGlfZXhaZE1MZ1otWExmUzJPU2JmTlFtbEY0MHNQMXNxelRReXVyWWNyLUFpV0I1MTg4RVp4eHRRWndONHY5SGhhcC1JanZHOW45ZVFtS3I4eHdBc2dreFgzR0lBemdrRdIBlAFBVV95cUxOb1c4VWRKblYtY3hmVlRDTzlraTJwbmZDVWYyMUpsOEN6T3k0Q19XLTc5cmVIcXpfd2ZRcklzUk9KS0tYQnNmNUc2RXVRbVIzTzhVR3EyN0JnbkhnTFdzOXdMX1drakEyLWJBMmctb3RseTdFLUpLZTBEZDkzMGNvYVJlTEtjcnJJbVZkdk5hVGstZjJi
- Relevance score: 5.0
- Published: Thu, 30 Apr 2026 02:39:43 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMijwFBVV95cUxPeWg1MHM2eUZCX0I2SzEwQnF2Y0NZS0lmOHl4d1ZINkJPaERCYTBhbGlfZXhaZE1MZ1otWExmUzJPU2JmTlFtbEY0MHNQMXNxelRReXVyWWNyLUFpV0I1MTg4RVp4eHRRWndONHY5SGhhcC1JanZHOW45ZVFtS3I4eHdBc2dreFgzR0lBemdrRdIBlAFBVV95cUxOb1c4VWRKblYtY3hmVlRDTzlraTJwbmZDVWYyMUpsOEN6T3k0Q19XLTc5cmVIcXpfd2ZRcklzUk9KS0tYQnNmNUc2RXVRbVIzTzhVR3EyN0JnbkhnTFdzOXdMX1drakEyLWJBMmctb3RseTdFLUpLZTBEZDkzMGNvYVJlTEtjcnJJbVZkdk5hVGstZjJi?oc=5" target="_blank">AI-integrated MSc courses launched</a>&nbsp;&nbsp;<font color="#6f6f6f">The Hans India</font>

## 154. Cognizant rolls out AI-infused rate cards as pricing model shifts, assigns 'AI fluency scores' to... - Moneycontrol.com
- Domain: moneycontrol.com
- URL: https://news.google.com/rss/articles/CBMiiwJBVV95cUxQRDNBRzNFQXFkS1NqdjdYLU9DTm9WSEpLYVlJdW5qSGhtS2NtRW5UWXdOVVczU2xMZkZ0SjcybHM4d0Z1LUhMbWpITXpuTjN5WXNraHhaZmJDYUR4bGxSa3BOZHNSVFR3dDZYZWRwdkdVUGU5WWtyRjNzY0ZEM0FWYkg0OXZqdWhTb05pS3R5azlha1oyTlIybHhOalRLc2Z4MjFENmowbHRaX2NhS2xvakRyd3luQjN2b3MtMEJsRGJqajdqRXVRTTFMSmlBZ01DVkl1MEIwZXlCZ05tUDRTNDlaNmRJVkdtYl9jYmtZcFBvU0kxVlJacEhTaEJhMU8zZHpLUThYN2lFUWPSAZACQVVfeXFMUEFSOWpSTHA4LVFSS0JKaEg3UDVHYlhtdlRjNHljOFBfYVpfRzROVWRSUERfZ3NseXZrSTlhZzMzeWY1QUhzQkFieW40eFVqRl9WU0x2WF9qMEp0NzNDMkEwR2FHeTM1cFBvdWxaaFRhSkRvRVo3eDhteWpkcTQ5TkoyY2lpRWxNMVdIY1FtaUM5VkQ0dmNHbWlWZEVrUzFBM2NYTlg1ZVpfcmpNSmRaTlk4VFMtQ3pZODc1c0VVbzM4VDJFd1pSRzNfVzdPTjI2bi1PdU9GUExMcDlXR3BlODAwTjBHcUxkaE5wSndHZ0Y0aHd3UmRkSFVhXzRDWVlRYm5abEZiWnlOSTFmcHkyalA
- Relevance score: 5.0
- Published: Thu, 30 Apr 2026 02:22:03 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiiwJBVV95cUxQRDNBRzNFQXFkS1NqdjdYLU9DTm9WSEpLYVlJdW5qSGhtS2NtRW5UWXdOVVczU2xMZkZ0SjcybHM4d0Z1LUhMbWpITXpuTjN5WXNraHhaZmJDYUR4bGxSa3BOZHNSVFR3dDZYZWRwdkdVUGU5WWtyRjNzY0ZEM0FWYkg0OXZqdWhTb05pS3R5azlha1oyTlIybHhOalRLc2Z4MjFENmowbHRaX2NhS2xvakRyd3luQjN2b3MtMEJsRGJqajdqRXVRTTFMSmlBZ01DVkl1MEIwZXlCZ05tUDRTNDlaNmRJVkdtYl9jYmtZcFBvU0kxVlJacEhTaEJhMU8zZHpLUThYN2lFUWPSAZACQVVfeXFMUEFSOWpSTHA4LVFSS0JKaEg3UDVHYlhtdlRjNHljOFBfYVpfRzROVWRSUERfZ3NseXZrSTlhZzMzeWY1QUhzQkFieW40eFVqRl9WU0x2WF9qMEp0NzNDMkEwR2FHeTM1cFBvdWxaaFRhSkRvRVo3eDhteWpkcTQ5TkoyY2lpRWxNMVdIY1FtaUM5VkQ0dmNHbWlWZEVrUzFBM2NYTlg1ZVpfcmpNSmRaTlk4VFMtQ3pZODc1c0VVbzM4VDJFd1pSRzNfVzdPTjI2bi1PdU9GUExMcDlXR3BlODAwTjBHcUxkaE5wSndHZ0Y0aHd3UmRkSFVhXzRDWVlRYm5abEZiWnlOSTFmcHkyalA?oc=5" target="_blank">Cognizant rolls out AI-infused rate cards as pricing model shifts, assigns 'AI fluency scores' to...</a>&nbsp;&nbsp;<font color="#6f6f6f">Moneycontrol.com</font>

## 155. AI in Travel and Logistics: The Gap Between Pilots and Scale - Tata Consultancy Services
- Domain: tcs.com
- URL: https://news.google.com/rss/articles/CBMiwAFBVV95cUxQVHlWUlJfcWxOX2NocDFkQnB5V1FxNFotdW96MzB6aWNaN1BHdUgwNEZacHpIWnlxdjZMV05BTi0yUFJmRmpoWXRvTzR4OURpSDV6T3A4T1dBQUpCaTA4UDByb0ZrRFV3c3ZucmdDbzNCaV9rb2NOUXp4Q2tXSWdPMUE2bHNqaVlSTjktMVg5X1JYSTk2eG0xaWY3TjZLQThzX0QtcHZGNnB2MlVVbF9KenFSWktCZUoxazkwSlZ6S20
- Relevance score: 5.0
- Published: Thu, 30 Apr 2026 01:51:17 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiwAFBVV95cUxQVHlWUlJfcWxOX2NocDFkQnB5V1FxNFotdW96MzB6aWNaN1BHdUgwNEZacHpIWnlxdjZMV05BTi0yUFJmRmpoWXRvTzR4OURpSDV6T3A4T1dBQUpCaTA4UDByb0ZrRFV3c3ZucmdDbzNCaV9rb2NOUXp4Q2tXSWdPMUE2bHNqaVlSTjktMVg5X1JYSTk2eG0xaWY3TjZLQThzX0QtcHZGNnB2MlVVbF9KenFSWktCZUoxazkwSlZ6S20?oc=5" target="_blank">AI in Travel and Logistics: The Gap Between Pilots and Scale</a>&nbsp;&nbsp;<font color="#6f6f6f">Tata Consultancy Services</font>

## 156. Commerce Department Seeks To Undercut Chinese AI Sector by Targeting Chipmakers - Foundation for Defense of Democracies
- Domain: fdd.org
- URL: https://news.google.com/rss/articles/CBMivAFBVV95cUxQNnpsUHJRQ1BSMnU5c2lybDZscWM1SW9ocXh0akpZR1pCb2pVZ1J1MTJjTUhuelNZWFk1Um9oWGhtSXhlekQ2c2EtV2wtRnlsUVBMMFFKNUlKM2RxNndrdUg0Sm4yZzVqRlVwRnNZdVM1VnVCSDYtb2cydzRaY09TZV9ZM3NYZy1ubnN2NU13ZzRPMm9CQ2FfTUJfNjV6TXlnQUM2Q3Z2Vl9kRU9XbWY3WEVfOTV1VG1tQ0Q4Sg
- Relevance score: 5.0
- Published: Thu, 30 Apr 2026 00:42:20 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMivAFBVV95cUxQNnpsUHJRQ1BSMnU5c2lybDZscWM1SW9ocXh0akpZR1pCb2pVZ1J1MTJjTUhuelNZWFk1Um9oWGhtSXhlekQ2c2EtV2wtRnlsUVBMMFFKNUlKM2RxNndrdUg0Sm4yZzVqRlVwRnNZdVM1VnVCSDYtb2cydzRaY09TZV9ZM3NYZy1ubnN2NU13ZzRPMm9CQ2FfTUJfNjV6TXlnQUM2Q3Z2Vl9kRU9XbWY3WEVfOTV1VG1tQ0Q4Sg?oc=5" target="_blank">Commerce Department Seeks To Undercut Chinese AI Sector by Targeting Chipmakers</a>&nbsp;&nbsp;<font color="#6f6f6f">Foundation for Defense of Democracies</font>

## 157. Samsung Electronics sees robust AI demand after Q1 chip profit jumps almost 50-fold - CNA
- Domain: channelnewsasia.com
- URL: https://news.google.com/rss/articles/CBMizAFBVV95cUxNVmtWT1NJekoyb2Z0dDVjWUktY0hWRHZMc3dlX2IweGJzZFZwRGJnVmJvYTRPUlhldkNvNktVMHVIRGJhNDhKM2ItNl95SGpBZEZmSkZMV0JiS1dGemtHZnF6eVhidld4UnQzYVZSTU5fcmhRZTZLV21NcFVpRTAydmRsZXBPSkstQVd2YzFkRWpKT2NpazBpUmxJTDNvV2NtcjQ3b2hNX1FFTG1NTTcxM1B1aU1uYV9UcXp1Z0dBMjlLRTl1QmdwWDdGS0w
- Relevance score: 5.0
- Published: Thu, 30 Apr 2026 00:13:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMizAFBVV95cUxNVmtWT1NJekoyb2Z0dDVjWUktY0hWRHZMc3dlX2IweGJzZFZwRGJnVmJvYTRPUlhldkNvNktVMHVIRGJhNDhKM2ItNl95SGpBZEZmSkZMV0JiS1dGemtHZnF6eVhidld4UnQzYVZSTU5fcmhRZTZLV21NcFVpRTAydmRsZXBPSkstQVd2YzFkRWpKT2NpazBpUmxJTDNvV2NtcjQ3b2hNX1FFTG1NTTcxM1B1aU1uYV9UcXp1Z0dBMjlLRTl1QmdwWDdGS0w?oc=5" target="_blank">Samsung Electronics sees robust AI demand after Q1 chip profit jumps almost 50-fold</a>&nbsp;&nbsp;<font color="#6f6f6f">CNA</font>

## 158. Sensex today | Stock Market Highlights: Sensex settled 416.72 pts, or 0.54%, lower at 76,886.91; Nifty 50 falls 97 pts, or 0.4%, to 23,995.70
- Domain: thehindubusinessline.com
- URL: https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-28th-april-2026/article70912004.ece
- Relevance score: 5.0
- Published: 2026-04-28T10:52:36Z
- Summary: Sensex, Nifty highlights on Apr 28:Stock market benchmark indices Sensex and Nifty buckled under selling pressure on Tuesday as a sharp rally in oil prices and foreign fund outflows dented investors’ sentiment.

## 159. MeitY Warns VPN Firms Over Enabling Access To Illegal Betting Platforms
- Domain: inc42.com
- URL: https://inc42.com/buzz/meity-warns-vpn-firms-over-enabling-access-to-illegal-betting-platforms/
- Relevance score: 4.8
- Published: Wed, 29 Apr 2026 13:55:44 +0000
- Summary: <img alt="Ola’s Avail Finance, KreditBee Among Lending Apps On MeitY’s Ban List" class="webfeedsFeaturedVisual wp-post-image" height="1020" src="https://inc42.com/cdn-cgi/image/quality=90/https://asset.inc42.com/2023/02/Meity-banning-apps-feature.png" style="display: block; margin: auto; margin-bottom: 5px;" width="1360" />The Ministry of Electronics and Information Technology (MeitY) has issued an advisory urging VPN service providers and intermediaries to stop&#8230;

## 160. Musk and Altman face off in court over OpenAI's for-profit pivot
- Domain: the-decoder.com
- URL: https://the-decoder.com/musk-and-altman-face-off-in-court-over-openais-for-profit-pivot/
- Relevance score: 4.8
- Published: Wed, 29 Apr 2026 12:59:56 +0000
- Summary: <p><img alt="" class="attachment-full size-full wp-post-image" height="768" src="https://the-decoder.com/wp-content/uploads/2026/04/Musk-vs-Altman.png" style="height: auto; margin-bottom: 10px;" width="1376" /></p> <p> The closely watched trial between Elon Musk and OpenAI CEO Sam Altman kicked off in federal court in Oakland. Both sides laid out wildly different versions of the AI lab's early days.</p> <p>The article <a href="https://the-decoder.com/musk-and-altman-face-off-in-court-over-openais-for-profit-pivot/">Musk and Altman face off in court over OpenAI&#039;s for-profit pivot</a> appeared first on <a href="https://the-decoder.com">The Decoder</a>.</p>

## 161. Why defining ‘news’ won’t fix the free speech problems of draft IT Rules? #NAMA
- Domain: medianama.com
- URL: https://www.medianama.com/2026/04/223-news-fix-free-speech-problems-draft-it-rules/
- Relevance score: 4.8
- Published: Wed, 29 Apr 2026 12:39:33 +0000
- Summary: <p>The experts highlighted how difficult it is to differentiate between news &#038; current affairs and journalists &#038; news content creators, as per the draft IT Rules, which leads to free speech violations.</p> <p>The post <a href="https://www.medianama.com/2026/04/223-news-fix-free-speech-problems-draft-it-rules/">Why defining ‘news’ won’t fix the free speech problems of draft IT Rules? #NAMA</a> appeared first on <a href="https://www.medianama.com">MEDIANAMA</a>.</p>

## 162. Google rolls out Gemini memory in Europe and wants you to bring your ChatGPT data along
- Domain: the-decoder.com
- URL: https://the-decoder.com/google-rolls-out-gemini-memory-in-europe-and-wants-you-to-bring-your-chatgpt-data-along/
- Relevance score: 4.8
- Published: Wed, 29 Apr 2026 11:50:10 +0000
- Summary: <p><img alt="" class="attachment-full size-full wp-post-image" height="768" src="https://the-decoder.com/wp-content/uploads/2026/04/google_gemini_optical_trick.png" style="height: auto; margin-bottom: 10px;" width="1376" /></p> <p> Gemini can now remember your preferences and import your chat history from other AI apps.</p> <p>The article <a href="https://the-decoder.com/google-rolls-out-gemini-memory-in-europe-and-wants-you-to-bring-your-chatgpt-data-along/">Google rolls out Gemini memory in Europe and wants you to bring your ChatGPT data along</a> appeared first on <a href="https://the-decoder.com">The Decoder</a>.</p>

## 163. Jaipur Edition Of D2CX Converge Decodes ₹100 Cr Playbooks For D2C Brands
- Domain: inc42.com
- URL: https://inc42.com/buzz/jaipur-edition-of-d2cx-converge-decodes-%e2%82%b9100-cr-playbooks-for-d2c-brands/
- Relevance score: 4.8
- Published: Wed, 29 Apr 2026 11:30:53 +0000
- Summary: <img alt="Jaipur Edition Of D2CX Converge Decodes ₹100 Cr Playbooks For D2C Brands" class="webfeedsFeaturedVisual wp-post-image" height="1020" src="https://inc42.com/cdn-cgi/image/quality=90/https://asset.inc42.com/2026/04/D2CX-Converge-Jaipur-ftr.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="1360" />In step with India’s consumption story widening beyond the metro strongholds, the direct-to-consumer (D2C) ecosystem has entered a phase where&#8230;

## 164. Centre In Talks With US, Anthropic For Access To Claude Mythos: Report
- Domain: inc42.com
- URL: https://inc42.com/buzz/centre-in-talks-with-us-anthropic-for-access-to-claude-mythos-report/
- Relevance score: 4.8
- Published: Wed, 29 Apr 2026 06:36:23 +0000
- Summary: <img alt="AI" class="webfeedsFeaturedVisual wp-post-image" height="1020" src="https://inc42.com/cdn-cgi/image/quality=90/https://asset.inc42.com/2026/04/ftr-17-2.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="1360" />The Centre is reportedly in talks with the US and Anthropic to work out a mechanism for Indian companies to&#8230;

## 165. OpenAI Really Wants Codex to Shut Up About Goblins
- Domain: wired.com
- URL: https://www.wired.com/story/openai-really-wants-codex-to-shut-up-about-goblins/
- Relevance score: 4.8
- Published: Tue, 28 Apr 2026 23:45:05 +0000
- Summary: “Never talk about goblins, gremlins, raccoons, trolls, ogres, pigeons, or other animals or creatures unless it is absolutely and unambiguously relevant,” reads OpenAI’s coding agent instructions.

## 166. Google Search queries hit an ‘all time high’ last quarter
- Domain: theverge.com
- URL: https://www.theverge.com/tech/920815/google-alphabet-q1-2026-earnings-sundar-pichai
- Relevance score: 4.8
- Published: 2026-04-29T16:28:11-04:00
- Summary: Google Search queries hit an "all time high" in the first quarter of 2026, according to a statement from CEO Sundar Pichai published as part of Alphabet's earnings on Wednesday. "Our AI investments and full stack approach are lighting up every part of the business," Pichai says. "Search had a strong quarter with AI experiences [&#8230;]

## 167. Ubuntu’s AI plans have Linux users looking for a &#8216;kill switch&#8217;
- Domain: theverge.com
- URL: https://www.theverge.com/tech/920723/linux-ubuntu-ai-features-ai-kill-switch
- Relevance score: 4.8
- Published: 2026-04-29T13:32:02-04:00
- Summary: Canonical's plan to add AI features to Ubuntu has some users asking for "a version of Ubuntu that does not include these features," while others say they'll stick with older versions of the Linux distro or even switch to a different one. After Canonical's announcement earlier this week that it's bringing AI features to Ubuntu, [&#8230;]

## 168. Google Photos launches an AI try-on feature for clothes you already have
- Domain: theverge.com
- URL: https://www.theverge.com/tech/920420/google-photos-ai-try-on-wardrobe
- Relevance score: 4.8
- Published: 2026-04-29T12:00:00-04:00
- Summary: Google Photos is launching a new AI-powered feature you can use to virtually try on clothes you already have. Using the photos in your gallery, Google will create a virtual "wardrobe," allowing you to mix and match outfits, save the looks you like, and share them with friends. A video shared by Google shows how [&#8230;]

## 169. Microsoft says it has over 20M paid Copilot users, and they really are using it
- Domain: techcrunch.com
- URL: https://techcrunch.com/2026/04/29/microsoft-says-it-has-over-20m-paid-copilot-users-and-they-really-are-using-it/
- Relevance score: 4.5
- Published: Wed, 29 Apr 2026 23:02:23 +0000
- Summary: Despite the lingering perception that no one really uses Copilot, Microsoft said on Wednesday that the number of users and engagement is growing.

## 170. Google Cloud surpasses $20B, but says growth was capacity-constrained
- Domain: techcrunch.com
- URL: https://techcrunch.com/2026/04/29/google-cloud-surpasses-20b-but-says-growth-was-capacity-constrained/
- Relevance score: 4.5
- Published: Wed, 29 Apr 2026 22:20:48 +0000
- Summary: Google Cloud topped $20B in quarterly revenue for the first time, fueled by surging demand for AI. But capacity constraints mean it could have grown even faster.

## 171. Where the goblins came from
- Domain: openai.com
- URL: https://openai.com/index/where-the-goblins-came-from
- Relevance score: 4.5
- Published: Wed, 29 Apr 2026 20:00:00 GMT
- Summary: How goblin outputs spread in AI models: timeline, root cause, and fixes behind personality-driven quirks in GPT-5 behavior.

## 172. Portland Water District workers call for regulations on AI - Spectrum News
- Domain: spectrumlocalnews.com
- URL: https://news.google.com/rss/articles/CBMiswFBVV95cUxNUmlESll3SEJLZ2VIbFQ3ak5Fc0JyRnZ0TE54bHd3MGRWemNoamVleUxJQXNKUl9zU2o0cm5OOENjdElPQmIyVjNJNVRadUJXdnN1M19xVWFVQnhRek1CdTVQV1FMaTJrZFByamJFRzNkbG5ocFRFcWptc3lTaUV2OHUyeHQybmE5SV9xVUtWbE9DWFVQSmswWE1JSVdjT0kxWHpIMGk3OE1LV1RqelBMQkx0OA
- Relevance score: 4.5
- Published: Wed, 29 Apr 2026 19:13:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiswFBVV95cUxNUmlESll3SEJLZ2VIbFQ3ak5Fc0JyRnZ0TE54bHd3MGRWemNoamVleUxJQXNKUl9zU2o0cm5OOENjdElPQmIyVjNJNVRadUJXdnN1M19xVWFVQnhRek1CdTVQV1FMaTJrZFByamJFRzNkbG5ocFRFcWptc3lTaUV2OHUyeHQybmE5SV9xVUtWbE9DWFVQSmswWE1JSVdjT0kxWHpIMGk3OE1LV1RqelBMQkx0OA?oc=5" target="_blank">Portland Water District workers call for regulations on AI</a>&nbsp;&nbsp;<font color="#6f6f6f">Spectrum News</font>

## 173. NGA taking cautious approach to AI adoption in human resources - DefenseScoop
- Domain: defensescoop.com
- URL: https://news.google.com/rss/articles/CBMid0FVX3lxTE0zR2MzMlY4eVN5am83bUpKaDFseXc0a3AwMFRUb2R3Ukk4cS15bHdvU3dlNVpWLUNKMlM4SkpnbGE1OF9VMkRoNGw4STM2Q2JmaXkxLW9Wc21KUE9iVUhDdFRsbnRDbDlwYVdibThyaUxVckFwSWdR
- Relevance score: 4.5
- Published: Wed, 29 Apr 2026 16:52:45 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMid0FVX3lxTE0zR2MzMlY4eVN5am83bUpKaDFseXc0a3AwMFRUb2R3Ukk4cS15bHdvU3dlNVpWLUNKMlM4SkpnbGE1OF9VMkRoNGw4STM2Q2JmaXkxLW9Wc21KUE9iVUhDdFRsbnRDbDlwYVdibThyaUxVckFwSWdR?oc=5" target="_blank">NGA taking cautious approach to AI adoption in human resources</a>&nbsp;&nbsp;<font color="#6f6f6f">DefenseScoop</font>

## 174. Sovereign AI Startup Support - Trend Hunter
- Domain: trendhunter.com
- URL: https://news.google.com/rss/articles/CBMiYkFVX3lxTE1zNVFzSDVtRFlDVndzR1RhblFtdjlISVNHUTUxQnB3dmJ4YmJoNkJncmc4QmEyTWU0Wmt6Vm5YaTBER3FuaHhXTmNRSFNQZkRQXzdfZ3RLNEVBQktUck9mU3JR0gFnQVVfeXFMTlczRTZaeTF2bDlrZGxOM20zVEdla3JNS3Y1d21ZS3c2LUxqUnMtNkVEVmVvN1c2ak41S0N2b29qaXctamF2V2QtOWI3aDBzelc1R0lZeVVEVERaTHJmanNpcEE0eG5LRQ
- Relevance score: 4.5
- Published: Wed, 29 Apr 2026 14:38:48 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE1zNVFzSDVtRFlDVndzR1RhblFtdjlISVNHUTUxQnB3dmJ4YmJoNkJncmc4QmEyTWU0Wmt6Vm5YaTBER3FuaHhXTmNRSFNQZkRQXzdfZ3RLNEVBQktUck9mU3JR0gFnQVVfeXFMTlczRTZaeTF2bDlrZGxOM20zVEdla3JNS3Y1d21ZS3c2LUxqUnMtNkVEVmVvN1c2ak41S0N2b29qaXctamF2V2QtOWI3aDBzelc1R0lZeVVEVERaTHJmanNpcEE0eG5LRQ?oc=5" target="_blank">Sovereign AI Startup Support</a>&nbsp;&nbsp;<font color="#6f6f6f">Trend Hunter</font>

## 175. Building Pi, and what makes self-modifying software so fascinating
- Domain: newsletter.pragmaticengineer.com
- URL: https://newsletter.pragmaticengineer.com/p/building-pi-and-what-makes-self-modifying
- Relevance score: 4.5
- Published: Wed, 29 Apr 2026 14:30:17 GMT
- Summary: Mario Zechner, creator of Pi, joins Armin Ronacher to explore AI coding&#8217;s limits, arguing that human judgment still matters most in an agent-driven world.

## 176. Fintech OppFi to buy Arizona bank for $130M
- Domain: bankingdive.com
- URL: https://www.bankingdive.com/news/oppfi-bnc-national-bank-acquisition-130-million-arizona-fintech-lending-charter/818838/
- Relevance score: 4.5
- Published: Wed, 29 Apr 2026 12:14:06 -0400
- Summary: <figure><div><img src="https://imgproxy.divecdn.com/80rh5LiPYFoIlpBrZ61jeimOi73oLu_upx0ID9Mrm30/g:ce/rs:fill:1600:900:1/Z3M6Ly9kaXZlc2l0ZS1zdG9yYWdlL2RpdmVpbWFnZS9HZXR0eUltYWdlcy0xNTQ2OTgwMTg5LmpwZw==.webp" /></div></figure><p>The Chicago-based subprime lender said pairing its online platform with BNC&rsquo;s national bank charter lets it offer more banking services on a broader scale.</p>

## 177. Indian VCs build 'bridges to America' as AI startups look westward - Business Standard
- Domain: business-standard.com
- URL: https://news.google.com/rss/articles/CBMi1AFBVV95cUxPd3E0UW5JVUl2anhnQWhxWkx0anNnV2trc2lZcVZUYzNucXNRV2dEaDZNSVhHb0p5YVJ4MWI4UHlCNUNPaW8ybFJ5Uk1LOGt1ajhIVFdOVHFlUUw0Tk54VnlKWl9iRlVaU2xxcWE0VGZwUURSY2VZRzJtTDdpOEJ2eVFwdmNtR2hDSmdCbHNWc0pOUENoWUdtNkhmTjBUdjB2WEpJTy0xckRZVWg4bllzVkNmZXFvNkd4LUUtLXhRbjBGd05KZkJVT0k0b21ULS1NYW5iWNIB2gFBVV95cUxNemFJNjR0UjBVUWoybXdIZ0Z6UTRuN3lGUFB6NFRHT0IyQWpIMER6bmU5eFcxOFNWd3BwX3ZveUx5MHVtVW9aVXMyMjVoWVItOW42NnJtYXQ0dTJKbWl2TjJFdFF5UGFzZXR0dGxvNlNKMW1TMG1Wc0VsWU16R2NQaExTMmk5WElOVE54Q1RtcURQTDE1WTJDRTlSMmVYRldRQUl0LUdGOTFLWFF5M3Z4Z2FVR0YwRlhLWWRuOWpEOHNYMWNURUstak44QXprY2pwOERlZUllQXJGdw
- Relevance score: 4.5
- Published: Wed, 29 Apr 2026 11:55:12 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi1AFBVV95cUxPd3E0UW5JVUl2anhnQWhxWkx0anNnV2trc2lZcVZUYzNucXNRV2dEaDZNSVhHb0p5YVJ4MWI4UHlCNUNPaW8ybFJ5Uk1LOGt1ajhIVFdOVHFlUUw0Tk54VnlKWl9iRlVaU2xxcWE0VGZwUURSY2VZRzJtTDdpOEJ2eVFwdmNtR2hDSmdCbHNWc0pOUENoWUdtNkhmTjBUdjB2WEpJTy0xckRZVWg4bllzVkNmZXFvNkd4LUUtLXhRbjBGd05KZkJVT0k0b21ULS1NYW5iWNIB2gFBVV95cUxNemFJNjR0UjBVUWoybXdIZ0Z6UTRuN3lGUFB6NFRHT0IyQWpIMER6bmU5eFcxOFNWd3BwX3ZveUx5MHVtVW9aVXMyMjVoWVItOW42NnJtYXQ0dTJKbWl2TjJFdFF5UGFzZXR0dGxvNlNKMW1TMG1Wc0VsWU16R2NQaExTMmk5WElOVE54Q1RtcURQTDE1WTJDRTlSMmVYRldRQUl0LUdGOTFLWFF5M3Z4Z2FVR0YwRlhLWWRuOWpEOHNYMWNURUstak44QXprY2pwOERlZUllQXJGdw?oc=5" target="_blank">Indian VCs build 'bridges to America' as AI startups look westward</a>&nbsp;&nbsp;<font color="#6f6f6f">Business Standard</font>

## 178. Ohio AI startup lawsuit attacks mega OSU donor over broken promises - The Columbus Dispatch
- Domain: dispatch.com
- URL: https://news.google.com/rss/articles/CBMi1AFBVV95cUxQNXV6SzhCbXhnLXVkTHFEQjFwOXdlWFppbzh1OGZkcWxpYS1MdW1qcFZEVzBaeVp1b25UX2FyLW5qS3Rld1FUV0JBMHhWb0s2NER4Y0pRNno1VUs1aWstMU1YT0dTNDIzZDNzLXluRGxaUUh4NEI5eDcxaUt3Y3Y4dGkteURKVk1UR01mLUJrMXhIZG4yUXJPXzBQcDVXWUhOTUw0c0xNdm5pbThSakozWUltV3RFSjk2UHUzTzhyVmJUZm9CbVJUTVl2TjVHVXBpQkJ2Xw
- Relevance score: 4.5
- Published: Wed, 29 Apr 2026 10:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi1AFBVV95cUxQNXV6SzhCbXhnLXVkTHFEQjFwOXdlWFppbzh1OGZkcWxpYS1MdW1qcFZEVzBaeVp1b25UX2FyLW5qS3Rld1FUV0JBMHhWb0s2NER4Y0pRNno1VUs1aWstMU1YT0dTNDIzZDNzLXluRGxaUUh4NEI5eDcxaUt3Y3Y4dGkteURKVk1UR01mLUJrMXhIZG4yUXJPXzBQcDVXWUhOTUw0c0xNdm5pbThSakozWUltV3RFSjk2UHUzTzhyVmJUZm9CbVJUTVl2TjVHVXBpQkJ2Xw?oc=5" target="_blank">Ohio AI startup lawsuit attacks mega OSU donor over broken promises</a>&nbsp;&nbsp;<font color="#6f6f6f">The Columbus Dispatch</font>

## 179. The quiet layoffs sweeping China’s tech giants
- Domain: restofworld.org
- URL: https://restofworld.org/2026/china-tech-layoffs-alibaba-baidu-ai-pivot/
- Relevance score: 4.5
- Published: Wed, 29 Apr 2026 10:00:00 +0000
- Summary: Alibaba reduced its head count by a third in 2025, while Baidu’s workforce declined nearly 7%. “There’s constant churn,” a Chinese tech worker said.

## 180. Singtel Singapore’s new AI programme to help push SMEs beyond pilots - The Edge Singapore
- Domain: theedgesingapore.com
- URL: https://news.google.com/rss/articles/CBMixAFBVV95cUxNV1JRZXNOazQ0QVFCYldQUjFOUUJ1LTdzYU96RWluSHUxdHVHZXE3cHhKTE9PbWI0c3dOcGlpM3dpUGc5SFNFdzQtWnlZSnFUelJRcjVrWXQtTzhLTGF3Qi1keE0tVi1LTG5OMjhJUUo0WFgtWDhEeW1vUl9xMlMzR05UUVhQQzFJREtiUk1oam1WNEhZV0pTSjBLa3BDN1NlUE41ZzRYdVhuQ25NOTNaYUNrdmZ4THFKVXFNSTNLZXBPUHNM0gHKAUFVX3lxTFBkV2RUaVl1cGItdlVCcmdBbEZYQWNZUzkwQTZlZDdZSzl1RmMteXAxbUhsVGhLeF9hZWhiWGN3bTRXQnllTjBLNktSNkFkM3AxaTZMRUxfTGtTX2ZiQVUyUVJqWEgxaGpEZ2NUUnRuaFJNMlZ2ZXo3VEV0UDZXQl9EU1VjRkNBZXhOV01tMk9vX0gxQWVXREZDSGNlc3JYUk5GUW90N3RFeXMwXzREMDRaSG1sTHlIYXlUb2lXRHRjVFd3T25aU21FaEE
- Relevance score: 4.5
- Published: Wed, 29 Apr 2026 09:32:16 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMixAFBVV95cUxNV1JRZXNOazQ0QVFCYldQUjFOUUJ1LTdzYU96RWluSHUxdHVHZXE3cHhKTE9PbWI0c3dOcGlpM3dpUGc5SFNFdzQtWnlZSnFUelJRcjVrWXQtTzhLTGF3Qi1keE0tVi1LTG5OMjhJUUo0WFgtWDhEeW1vUl9xMlMzR05UUVhQQzFJREtiUk1oam1WNEhZV0pTSjBLa3BDN1NlUE41ZzRYdVhuQ25NOTNaYUNrdmZ4THFKVXFNSTNLZXBPUHNM0gHKAUFVX3lxTFBkV2RUaVl1cGItdlVCcmdBbEZYQWNZUzkwQTZlZDdZSzl1RmMteXAxbUhsVGhLeF9hZWhiWGN3bTRXQnllTjBLNktSNkFkM3AxaTZMRUxfTGtTX2ZiQVUyUVJqWEgxaGpEZ2NUUnRuaFJNMlZ2ZXo3VEV0UDZXQl9EU1VjRkNBZXhOV01tMk9vX0gxQWVXREZDSGNlc3JYUk5GUW90N3RFeXMwXzREMDRaSG1sTHlIYXlUb2lXRHRjVFd3T25aU21FaEE?oc=5" target="_blank">Singtel Singapore’s new AI programme to help push SMEs beyond pilots</a>&nbsp;&nbsp;<font color="#6f6f6f">The Edge Singapore</font>

## 181. Meta FAIR Releases NeuralSet: A Python Package for Neuro-AI That Supports fMRI, M/EEG, Spikes, and HuggingFace Embeddings
- Domain: marktechpost.com
- URL: https://www.marktechpost.com/2026/04/29/meta-fair-releases-neuralset-a-python-package-for-neuro-ai-that-supports-fmri-m-eeg-spikes-and-huggingface-embeddings/
- Relevance score: 4.5
- Published: Wed, 29 Apr 2026 07:56:02 +0000
- Summary: <p>Introducing NeuralSet: Meta's Simple, Fast, and Scalable Python Package That Bridges Neuroscience and AI</p> <p>The post <a href="https://www.marktechpost.com/2026/04/29/meta-fair-releases-neuralset-a-python-package-for-neuro-ai-that-supports-fmri-m-eeg-spikes-and-huggingface-embeddings/">Meta FAIR Releases NeuralSet: A Python Package for Neuro-AI That Supports fMRI, M/EEG, Spikes, and HuggingFace Embeddings</a> appeared first on <a href="https://www.marktechpost.com">MarkTechPost</a>.</p>

## 182. « Tu vas pas me croire », un agent IA décide seul d'effacer la base de données d'une entreprise - La Tribune
- Domain: latribune.fr
- URL: https://news.google.com/rss/articles/CBMi2AFBVV95cUxOQ0hDVGFtNm4xY18wek9mWERzR3U2NUI4aXZDRFJIVm5SM3VVVFk0Q1NqeDRyYS1lR2twSVVINWFmSVRHT1czaG1XMmk5bTJGTS1CdTltTUdBbG9YOGJsZEVHV2l5d0swTmdQUmJRWGhDM2o1RVhKUXp3SF85NWwtUmR0bXhsTWg4Rk9teDdBZUExUHBmUFJRWGxoSjYwdFlGZ1lFT3ZRWHVXT0tJSHNVNDVOSjJucTh3WHM3cHFqRVhfMnlaU2EwMjctLTN3MktkSFVsXzhMTnE
- Relevance score: 4.5
- Published: Wed, 29 Apr 2026 07:25:02 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi2AFBVV95cUxOQ0hDVGFtNm4xY18wek9mWERzR3U2NUI4aXZDRFJIVm5SM3VVVFk0Q1NqeDRyYS1lR2twSVVINWFmSVRHT1czaG1XMmk5bTJGTS1CdTltTUdBbG9YOGJsZEVHV2l5d0swTmdQUmJRWGhDM2o1RVhKUXp3SF85NWwtUmR0bXhsTWg4Rk9teDdBZUExUHBmUFJRWGxoSjYwdFlGZ1lFT3ZRWHVXT0tJSHNVNDVOSjJucTh3WHM3cHFqRVhfMnlaU2EwMjctLTN3MktkSFVsXzhMTnE?oc=5" target="_blank">« Tu vas pas me croire », un agent IA décide seul d'effacer la base de données d'une entreprise</a>&nbsp;&nbsp;<font color="#6f6f6f">La Tribune</font>

## 183. Pourquoi tant d’entrepreneurs pilotent encore leurs finances à l’intuition ?
- Domain: maddyness.com
- URL: https://www.maddyness.com/2026/04/29/pourquoi-tant-dentrepreneurs-pilotent-encore-leurs-finances-a-lintuition/
- Relevance score: 4.5
- Published: Wed, 29 Apr 2026 07:14:51 +0000
- Summary: <p>L’article <a href="https://www.maddyness.com/2026/04/29/pourquoi-tant-dentrepreneurs-pilotent-encore-leurs-finances-a-lintuition/">Pourquoi tant d’entrepreneurs pilotent encore leurs finances à l’intuition ?</a> est apparu en premier sur <a href="https://www.maddyness.com">Maddyness - Le média pour comprendre l&#039;économie de demain</a>.</p>

## 184. AI chatbots are giving dangerous medical advice half the time and nobody is talking about it - Startup Fortune
- Domain: startupfortune.com
- URL: https://news.google.com/rss/articles/CBMivAFBVV95cUxNd0h2U1FHSDd0c2tkVDJwM0ZPek9IdGtBZXdxdHdzUHgtamViRGdabDRZaEV2T2NXSlg4QmphU1k3eU1uNVVGX09ORGxMNUgxTWs2eElkNE81SjIyZU9nUm16RFVxWmtWRHlEN2ZWOEVMZUJLaktnRnZrWkZfYnBLTUVkeVh5SVFZRUI0b2NZbGJRTzk2WlIyNnVqaGtVMDhGWTlwYTlpQk41QUZ1eU01bTB4elI2LXplYlZMeQ
- Relevance score: 4.5
- Published: Wed, 29 Apr 2026 03:45:38 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMivAFBVV95cUxNd0h2U1FHSDd0c2tkVDJwM0ZPek9IdGtBZXdxdHdzUHgtamViRGdabDRZaEV2T2NXSlg4QmphU1k3eU1uNVVGX09ORGxMNUgxTWs2eElkNE81SjIyZU9nUm16RFVxWmtWRHlEN2ZWOEVMZUJLaktnRnZrWkZfYnBLTUVkeVh5SVFZRUI0b2NZbGJRTzk2WlIyNnVqaGtVMDhGWTlwYTlpQk41QUZ1eU01bTB4elI2LXplYlZMeQ?oc=5" target="_blank">AI chatbots are giving dangerous medical advice half the time and nobody is talking about it</a>&nbsp;&nbsp;<font color="#6f6f6f">Startup Fortune</font>

## 185. Axios Finish Line: Make AI remember you
- Domain: axios.com
- URL: https://www.axios.com/2026/04/29/axios-finish-line-make-ai-remember-you
- Relevance score: 4.5
- Published: Wed, 29 Apr 2026 01:25:04 +0000
- Summary: <p><em>I'm offering you four specific ways to get more out of AI this week: <a href="https://www.axios.com/2026/04/28/improve-your-ai-prompt" target="_blank">better prompting</a>, improving AI memory (tonight), starting a business using AI (tomorrow) and running a business using AI (Thursday).</em></p><p>You nailed the perfect prompt. The output sang. You saved your Super Prompt. Then, you opened a new chat the next morning and AI acted like you'd never met.</p><ul><li>It's not broken. You just haven't taught it to remember YOU.</li></ul><p><strong>Why it matters:</strong> Master what AI stores, what it can reference from your past and how to direct both — and your chats will start smarter. This is how you unlock next-level prompting and results.</p><hr /><ul><li>The basics take 10 minutes. The payoff compounds forever.</li></ul><p><strong>A quick primer</strong> on AI memory: Think of it as two layers.</p><ul><li>Inside a stand-alone chat thread, AI can use what you've said there. That's called working memory. Close the chat, that brain resets.</li><li>Lasting memory is different. It's what AI remembers about you — your job, your style, your preferences. Most people accidentally r

## 186. Energy Management Software Market Surges with AI Integration, Set to Reach $44.31 Billion by 2035 - TimesTech
- Domain: timestech.in
- URL: https://news.google.com/rss/articles/CBMiuAFBVV95cUxPeEtvc3J5YnZVOWdGakJIY3NDc3JSWXhJZ1BXRHZLNzZhZWl1MDNlY096bVpSYWZVeloxS1dCQUZvR3ozWk9XSWl6aXFFTTk2TkVxam9hcXU3WjFleDVkeDFXMGthTjROVW1fLU05bEhHNzNvXzFZSkpLdFVPYmxtd1QwSDNyOTVBNWRnckg0d1E1RzNoc09jYXNYMEwzN3ROdUszU2k3M3kxSl9oUWkycGloZGFwdEpU
- Relevance score: 4.5
- Published: Thu, 30 Apr 2026 05:55:52 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiuAFBVV95cUxPeEtvc3J5YnZVOWdGakJIY3NDc3JSWXhJZ1BXRHZLNzZhZWl1MDNlY096bVpSYWZVeloxS1dCQUZvR3ozWk9XSWl6aXFFTTk2TkVxam9hcXU3WjFleDVkeDFXMGthTjROVW1fLU05bEhHNzNvXzFZSkpLdFVPYmxtd1QwSDNyOTVBNWRnckg0d1E1RzNoc09jYXNYMEwzN3ROdUszU2k3M3kxSl9oUWkycGloZGFwdEpU?oc=5" target="_blank">Energy Management Software Market Surges with AI Integration, Set to Reach $44.31 Billion by 2035</a>&nbsp;&nbsp;<font color="#6f6f6f">TimesTech</font>

## 187. Visa pilots AI-powered payment framework with banks and FinTechs - IBS Intelligence
- Domain: ibsintelligence.com
- URL: https://news.google.com/rss/articles/CBMipgFBVV95cUxPTEgzd3czQzNGRmpyRWpOOVdQZUgtZlQyZlZ2LVUwaGlMcEhoS1NPU1QxUnlQVmRlZ3VtMFR1Qmh0UUhuRzVkQ3RUYUpINFVMTjFHTTh2SzZHaHpPSGZQRDVJMGllS1NfMTJ4dDZUMFppY3RaakNkRTk0cExUSnVONlZUWk94YWpBNFJqMHljQmtNUUFwVTB6Z0dXX3lYTzNJRmJVV1p3
- Relevance score: 4.5
- Published: Thu, 30 Apr 2026 04:20:18 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMipgFBVV95cUxPTEgzd3czQzNGRmpyRWpOOVdQZUgtZlQyZlZ2LVUwaGlMcEhoS1NPU1QxUnlQVmRlZ3VtMFR1Qmh0UUhuRzVkQ3RUYUpINFVMTjFHTTh2SzZHaHpPSGZQRDVJMGllS1NfMTJ4dDZUMFppY3RaakNkRTk0cExUSnVONlZUWk94YWpBNFJqMHljQmtNUUFwVTB6Z0dXX3lYTzNJRmJVV1p3?oc=5" target="_blank">Visa pilots AI-powered payment framework with banks and FinTechs</a>&nbsp;&nbsp;<font color="#6f6f6f">IBS Intelligence</font>

## 188. Infosys CEO Salil Parekh rules out layoffs, bets on AI driven growth - Moneycontrol.com
- Domain: moneycontrol.com
- URL: https://news.google.com/rss/articles/CBMi2gFBVV95cUxPUDgtUG5HRkk1WlJuZk43RzVZcFU5SUU4Qm0zaDJLRTNKWDQ2U0dJcmVhVmVMTExyTWJrN095R1l5cDNBemdGdFcya0lTNjZRZEluTmZ1cEJtWXdEaGdBNjZPTjVfc1JWY2dXOHBpMHhIc0F5Y0FqQ0JrMkk3dTMwSjUwSHBJYmR1NjhRMWl3Z2hGdmJTN2lVNnNMcF9WdE5Oa2d3TW40ZWVOZ3JHVk5IYWdmNEd1Tm1FTFRNZG1SYzdGaVZNQ0FZR2l6YXg0ZGYtR0dNTFVCbkF2d9IB3wFBVV95cUxPNkY2VTl1cDRfWEJOMk4xb0w1S3haTkpXTUtoWlhRUEk1ZlpUQU5ZdnlsQVFPSk45NzRsYWFsazV2NEZCYkdWcU1SUEVvQ0NfWE5mOEY3LUctUWZjNzF5b1NzVmdQTmwyT2RYTXpqY3dWRzVodmtrb3k5M0NqcXFxd3JhOTlpc2R1Nk9jdVo5TGtfNXNyZnYwZDFxaU1zc2ZVVFcxVWpWNU1zTmcxS3RNX1RheWN6TDZsLUhWYk9FRmtNWFl2UkwzeXY1Qm5GU3FlaTAzazVtVWZPUWlhMzBn
- Relevance score: 4.5
- Published: Thu, 30 Apr 2026 00:32:14 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi2gFBVV95cUxPUDgtUG5HRkk1WlJuZk43RzVZcFU5SUU4Qm0zaDJLRTNKWDQ2U0dJcmVhVmVMTExyTWJrN095R1l5cDNBemdGdFcya0lTNjZRZEluTmZ1cEJtWXdEaGdBNjZPTjVfc1JWY2dXOHBpMHhIc0F5Y0FqQ0JrMkk3dTMwSjUwSHBJYmR1NjhRMWl3Z2hGdmJTN2lVNnNMcF9WdE5Oa2d3TW40ZWVOZ3JHVk5IYWdmNEd1Tm1FTFRNZG1SYzdGaVZNQ0FZR2l6YXg0ZGYtR0dNTFVCbkF2d9IB3wFBVV95cUxPNkY2VTl1cDRfWEJOMk4xb0w1S3haTkpXTUtoWlhRUEk1ZlpUQU5ZdnlsQVFPSk45NzRsYWFsazV2NEZCYkdWcU1SUEVvQ0NfWE5mOEY3LUctUWZjNzF5b1NzVmdQTmwyT2RYTXpqY3dWRzVodmtrb3k5M0NqcXFxd3JhOTlpc2R1Nk9jdVo5TGtfNXNyZnYwZDFxaU1zc2ZVVFcxVWpWNU1zTmcxS3RNX1RheWN6TDZsLUhWYk9FRmtNWFl2UkwzeXY1Qm5GU3FlaTAzazVtVWZPUWlhMzBn?oc=5" target="_blank">Infosys CEO Salil Parekh rules out layoffs, bets on AI driven growth</a>&nbsp;&nbsp;<font color="#6f6f6f">Moneycontrol.com</font>

## 189. Santa Cruz County workers are using AI. Exactly how is far less clear - Santa Cruz Sentinel
- Domain: santacruzsentinel.com
- URL: https://news.google.com/rss/articles/CBMitAFBVV95cUxOQ2s2angzX0R1ZzdmMzhCeTZXd21iSU4tNXlsZGVHYnlKaGV1enlxcXpKekZLeVlfaEZrcENweFhnNWthelpTSmFldDN1UERtVThmdWJ0TEFtQnpmc0t2NTZtTkI1cHRHNWlaWmJSME9WdmFSMW43dlhiV1FUUHE4WFBhekwyeU9hd3RyV2h3Q0VYZmRQRloycGpSeGY1dmVtUXRQdGxjQ2NLQlh0NTZtT0F5WV8
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 23:43:32 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMitAFBVV95cUxOQ2s2angzX0R1ZzdmMzhCeTZXd21iSU4tNXlsZGVHYnlKaGV1enlxcXpKekZLeVlfaEZrcENweFhnNWthelpTSmFldDN1UERtVThmdWJ0TEFtQnpmc0t2NTZtTkI1cHRHNWlaWmJSME9WdmFSMW43dlhiV1FUUHE4WFBhekwyeU9hd3RyV2h3Q0VYZmRQRloycGpSeGY1dmVtUXRQdGxjQ2NLQlh0NTZtT0F5WV8?oc=5" target="_blank">Santa Cruz County workers are using AI. Exactly how is far less clear</a>&nbsp;&nbsp;<font color="#6f6f6f">Santa Cruz Sentinel</font>

## 190. Meta soutenu par l'IA au premier trimestre, mais le marché s'inquiète de ses dépenses - France 24
- Domain: france24.com
- URL: https://news.google.com/rss/articles/CBMi5wFBVV95cUxQQzNQeGdkTFBKZHRFUDYxamVDQUh1bmJJaG0xZXBJNGxZbkU3eVJHSE5JN3k0Y3dTRHVrb2UyUnRiRmNURElDYS01eU9ZQ29LSXhtTEd5b1E1OVJodm1BMkR6X3VWcFhrVmkycC1Ta05HbThyRE5rVmNJdm1kMDdpcWtseVcweGNuN0lEZjUyak40cGhBay1kZFNhZ29nZ0lpZEpUY3RQNHdLOUdoN0RQVjNyaTBza2p3bDlRbTlUczlCYTk3Z053eUtmelpjUnhNT0Mydm1xNE1hUjB4cnB5SldDNGowb0E
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 22:53:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi5wFBVV95cUxQQzNQeGdkTFBKZHRFUDYxamVDQUh1bmJJaG0xZXBJNGxZbkU3eVJHSE5JN3k0Y3dTRHVrb2UyUnRiRmNURElDYS01eU9ZQ29LSXhtTEd5b1E1OVJodm1BMkR6X3VWcFhrVmkycC1Ta05HbThyRE5rVmNJdm1kMDdpcWtseVcweGNuN0lEZjUyak40cGhBay1kZFNhZ29nZ0lpZEpUY3RQNHdLOUdoN0RQVjNyaTBza2p3bDlRbTlUczlCYTk3Z053eUtmelpjUnhNT0Mydm1xNE1hUjB4cnB5SldDNGowb0E?oc=5" target="_blank">Meta soutenu par l'IA au premier trimestre, mais le marché s'inquiète de ses dépenses</a>&nbsp;&nbsp;<font color="#6f6f6f">France 24</font>

## 191. AI Demand Is Surging — But Taiwan Semiconductor Is Controlling the Supply - 24/7 Wall St.
- Domain: 247wallst.com
- URL: https://news.google.com/rss/articles/CBMiugFBVV95cUxQbXl1ak5ZbC1GM1dLb2t0STVEVklSUEVpMTRpZC16b1FtaDZlSHF2TGk0VTFqQ0xucC1QcmE5Z0lXc3g2LVpOMFJLdjVQLTMwMFk0NVBtMzZiRVBURWkzcmczeGdYQ2NGSjZfQTRKV3JQR2RXVlZEcXo3OUdSYjFEM2xMYXN4VTM5OHdSWEhhdFZ3QlVaYnBoOUZHeEZPOGZud3pPUGtYV0JUU2xZaExGbmx4cUcxYmtVOVE
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 22:33:35 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiugFBVV95cUxQbXl1ak5ZbC1GM1dLb2t0STVEVklSUEVpMTRpZC16b1FtaDZlSHF2TGk0VTFqQ0xucC1QcmE5Z0lXc3g2LVpOMFJLdjVQLTMwMFk0NVBtMzZiRVBURWkzcmczeGdYQ2NGSjZfQTRKV3JQR2RXVlZEcXo3OUdSYjFEM2xMYXN4VTM5OHdSWEhhdFZ3QlVaYnBoOUZHeEZPOGZud3pPUGtYV0JUU2xZaExGbmx4cUcxYmtVOVE?oc=5" target="_blank">AI Demand Is Surging — But Taiwan Semiconductor Is Controlling the Supply</a>&nbsp;&nbsp;<font color="#6f6f6f">24/7 Wall St.</font>

## 192. What It Will Take To Make AI-Enabled Robots Safer - Eurasia Review
- Domain: eurasiareview.com
- URL: https://news.google.com/rss/articles/CBMikwFBVV95cUxOZmJEMUNPSXRLNlpacDYzSUpZZnRQbkFHVWZnaVJYTExpQlA5ZDZwOEpKZVpZcWV6Rmt4bnhpdVFaR1QzSV9acVFoUUl2ZTdPYnBTaDM2SDhySkNWT3pGNWhNVHRMTjVuOTVhVjZFN2tjcjB5UWg3YWNOdUVJTlExX3JYVlgwZDJ3Skw4S0xqYlc1Zkk
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 22:14:44 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMikwFBVV95cUxOZmJEMUNPSXRLNlpacDYzSUpZZnRQbkFHVWZnaVJYTExpQlA5ZDZwOEpKZVpZcWV6Rmt4bnhpdVFaR1QzSV9acVFoUUl2ZTdPYnBTaDM2SDhySkNWT3pGNWhNVHRMTjVuOTVhVjZFN2tjcjB5UWg3YWNOdUVJTlExX3JYVlgwZDJ3Skw4S0xqYlc1Zkk?oc=5" target="_blank">What It Will Take To Make AI-Enabled Robots Safer</a>&nbsp;&nbsp;<font color="#6f6f6f">Eurasia Review</font>

## 193. Commentary: I built an AI trading platform in six days. That’s terrifying - CNA
- Domain: channelnewsasia.com
- URL: https://news.google.com/rss/articles/CBMilgFBVV95cUxPUTBXdGNmR2Zvd3pIQWxJMEJRUEdXLVVhZUYwYnIxbUlJN1pvYWJRQ2I0T0RCOXhCd1ZSTW1kU2J4SkxXLVlqWlVRSmE5enJ3TVNTTzhESUd5Zi1jUUNMcVpadVJXekYwWUQ2X1RLbUFxUDhRWVBsQnhIRk5ZMHo1LUJFaGRKUTNQTzBSbzFrX3VSel9RZlE
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 21:58:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMilgFBVV95cUxPUTBXdGNmR2Zvd3pIQWxJMEJRUEdXLVVhZUYwYnIxbUlJN1pvYWJRQ2I0T0RCOXhCd1ZSTW1kU2J4SkxXLVlqWlVRSmE5enJ3TVNTTzhESUd5Zi1jUUNMcVpadVJXekYwWUQ2X1RLbUFxUDhRWVBsQnhIRk5ZMHo1LUJFaGRKUTNQTzBSbzFrX3VSel9RZlE?oc=5" target="_blank">Commentary: I built an AI trading platform in six days. That’s terrifying</a>&nbsp;&nbsp;<font color="#6f6f6f">CNA</font>

## 194. La tueuse écrivait des messages inquiétants sur ChatGPT : vague de plaintes contre OpenAI après une fusillade au Canada - Ouest-France
- Domain: ouest-france.fr
- URL: https://news.google.com/rss/articles/CBMinAJBVV95cUxQc2lQaFF4TFhwdS1nMjhiV3hNQ25wYTFrM3I4REFyV2RPWGtzUHlkYU9HTTAyckt6bHZDVnp2WC1YQ24xYXM4QXhSUjdTS1YwUV9FQkdtZXB3TVVWSXJqRDFnZVRYRFdkUkltTHM3Zlcya01KWHA5YjBHdWpMbkxFUXI1Ull4cS03d21rcmNtU3dzZzdNZXJXNWJZY1IxWng2NUNsS0Vja204VW16U0w3RmpwRHRzY0hTSllUVUZCMEtoWjIyWVdVbGRtSWRIaWtFOWlsRzZLaF94eHpLVlVZS0dsLWhWM2MyTHktYW5pUFB6Wm91REwwcHVWaHpGTXpsWE5YaDFWa3VyLV83YVhsZFFtNEVfZlI4QTZZdg
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 21:49:53 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMinAJBVV95cUxQc2lQaFF4TFhwdS1nMjhiV3hNQ25wYTFrM3I4REFyV2RPWGtzUHlkYU9HTTAyckt6bHZDVnp2WC1YQ24xYXM4QXhSUjdTS1YwUV9FQkdtZXB3TVVWSXJqRDFnZVRYRFdkUkltTHM3Zlcya01KWHA5YjBHdWpMbkxFUXI1Ull4cS03d21rcmNtU3dzZzdNZXJXNWJZY1IxWng2NUNsS0Vja204VW16U0w3RmpwRHRzY0hTSllUVUZCMEtoWjIyWVdVbGRtSWRIaWtFOWlsRzZLaF94eHpLVlVZS0dsLWhWM2MyTHktYW5pUFB6Wm91REwwcHVWaHpGTXpsWE5YaDFWa3VyLV83YVhsZFFtNEVfZlI4QTZZdg?oc=5" target="_blank">La tueuse écrivait des messages inquiétants sur ChatGPT : vague de plaintes contre OpenAI après une fusillade au Canada</a>&nbsp;&nbsp;<font color="#6f6f6f">Ouest-France</font>

## 195. Physical AI's network demands are telco opportunities - Fierce Network
- Domain: fierce-network.com
- URL: https://news.google.com/rss/articles/CBMikwFBVV95cUxQVzB5SUFreGg3NGZJaXA0Y002VlJOc0sxc1UtUmlwZ1VGN21lYjFZTWtzTlloZDhQSk1pWjdheDJNd3ZIX0lTa25EaXlLSzhMYmZVdFhLNm9JRVJhcDhkbGdLTlQ5V2JCVjI5RXphb3oxcGdOSG9xQk1SSkhBSHFjNmxTc0JxU3V5UWhkbi0teU1JaUU
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 21:47:14 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMikwFBVV95cUxQVzB5SUFreGg3NGZJaXA0Y002VlJOc0sxc1UtUmlwZ1VGN21lYjFZTWtzTlloZDhQSk1pWjdheDJNd3ZIX0lTa25EaXlLSzhMYmZVdFhLNm9JRVJhcDhkbGdLTlQ5V2JCVjI5RXphb3oxcGdOSG9xQk1SSkhBSHFjNmxTc0JxU3V5UWhkbi0teU1JaUU?oc=5" target="_blank">Physical AI's network demands are telco opportunities</a>&nbsp;&nbsp;<font color="#6f6f6f">Fierce Network</font>

## 196. Meta shares slide as investors weigh Big Tech's AI spending spree - BBC
- Domain: bbc.co.uk
- URL: https://news.google.com/rss/articles/CBMiXEFVX3lxTE90TXdwSVdwdUJLM0VCYnprc2R0UGVjMlpWaEowMVZJQUR5aTJWMU5VOHA5UjgzaTFVcUlnU2lZUXprTFlyZ052bUxjODNsZE1rVWhzWHZjaWZvdjBD
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 21:41:41 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTE90TXdwSVdwdUJLM0VCYnprc2R0UGVjMlpWaEowMVZJQUR5aTJWMU5VOHA5UjgzaTFVcUlnU2lZUXprTFlyZ052bUxjODNsZE1rVWhzWHZjaWZvdjBD?oc=5" target="_blank">Meta shares slide as investors weigh Big Tech's AI spending spree</a>&nbsp;&nbsp;<font color="#6f6f6f">BBC</font>

## 197. Gartner: Supply chain orgs struggle to add AI onto legacy systems - DC Velocity
- Domain: dcvelocity.com
- URL: https://news.google.com/rss/articles/CBMixAFBVV95cUxPaDBWaHJyT21pUmpHVjlFUWJfSTdNNURSY3RiUDdqR2V5a0pnTDc1ZG82WUZoNW02Uk5wYjdCZnFhcG9tYklua2p6UWlLa01CV3VIWEt5Q3F4Y3Q4bmZ0eUlmdUM4TDlBeTRkVHlsTWYwQnhYNHhLbkF6dnQ4RDZuX1RXXzFaeTdJWTNhcW8zMnRzNmViZl9JTGRaNkFfenBrLTR2eEFFTjRmeEZJNnJsdGNkYVE4b29QeGt2QzlGdzFzVHZf
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 21:19:29 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMixAFBVV95cUxPaDBWaHJyT21pUmpHVjlFUWJfSTdNNURSY3RiUDdqR2V5a0pnTDc1ZG82WUZoNW02Uk5wYjdCZnFhcG9tYklua2p6UWlLa01CV3VIWEt5Q3F4Y3Q4bmZ0eUlmdUM4TDlBeTRkVHlsTWYwQnhYNHhLbkF6dnQ4RDZuX1RXXzFaeTdJWTNhcW8zMnRzNmViZl9JTGRaNkFfenBrLTR2eEFFTjRmeEZJNnJsdGNkYVE4b29QeGt2QzlGdzFzVHZf?oc=5" target="_blank">Gartner: Supply chain orgs struggle to add AI onto legacy systems</a>&nbsp;&nbsp;<font color="#6f6f6f">DC Velocity</font>

## 198. The scramble to prep for AI super-hackers - marketplace.org
- Domain: marketplace.org
- URL: https://news.google.com/rss/articles/CBMinwFBVV95cUxPQllRbVI1MHZKd1llQjZfajZQTUZuM2dMZjZkTktFRjYwcExTYlJfa1dIMlNvTDAycldDcjYyczRRMmRGSWVhVzR2RDZFLTM4UVA2cHhYTEtXeUVfSDhVTjJoUi1BODhQcWlNa1I2TlpodTRVX1pDdW5RYXJYVVFfV0loaUdDaFdwS2R2TkZLNzN3NUo4Q25icWpIR3dRWlE
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 21:01:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMinwFBVV95cUxPQllRbVI1MHZKd1llQjZfajZQTUZuM2dMZjZkTktFRjYwcExTYlJfa1dIMlNvTDAycldDcjYyczRRMmRGSWVhVzR2RDZFLTM4UVA2cHhYTEtXeUVfSDhVTjJoUi1BODhQcWlNa1I2TlpodTRVX1pDdW5RYXJYVVFfV0loaUdDaFdwS2R2TkZLNzN3NUo4Q25icWpIR3dRWlE?oc=5" target="_blank">The scramble to prep for AI super-hackers</a>&nbsp;&nbsp;<font color="#6f6f6f">marketplace.org</font>

## 199. A Conflict of AI Visions - City Journal
- Domain: city-journal.org
- URL: https://news.google.com/rss/articles/CBMilwFBVV95cUxPOGN6Mk5QUGktR01LQnNEenVwRlpjZ3Rxejk0RGZMQm9aVDRtWkw5SGJsTkh4WEwwZGw1NW4zbFNtckp5U2pCcWt2QmtYOGFxdmR6Z3MyOUhwZFZheDBxaVdHUFNLWjQ2YlBKZ29kcHJFNFNiWnVmY1V0TWdOQ3dRWXB3ckNnajlCZGpYeHl0TGlhQVNCTUQ4
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 20:58:35 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMilwFBVV95cUxPOGN6Mk5QUGktR01LQnNEenVwRlpjZ3Rxejk0RGZMQm9aVDRtWkw5SGJsTkh4WEwwZGw1NW4zbFNtckp5U2pCcWt2QmtYOGFxdmR6Z3MyOUhwZFZheDBxaVdHUFNLWjQ2YlBKZ29kcHJFNFNiWnVmY1V0TWdOQ3dRWXB3ckNnajlCZGpYeHl0TGlhQVNCTUQ4?oc=5" target="_blank">A Conflict of AI Visions</a>&nbsp;&nbsp;<font color="#6f6f6f">City Journal</font>

## 200. Faculty Concerned About ASU’s New AI Course Builder - Inside Higher Ed
- Domain: insidehighered.com
- URL: https://news.google.com/rss/articles/CBMiyAFBVV95cUxOS1dZMENuZnd0VHB4djF6dHpDN3JvOWJPRW9uSVQ2a2N5cmJwM2NVdWtzLUIyZTAtbXVVcmEzSEtpejlTRkQ4OVUxTklHYzY0aUt3QmlOUExqQmZReW9oOEQtVXJBTVZhVFVmeW1HbVB0SW9adkFIMTZDNlVFeXhxZFJueWo5aFFhczQzNTdjQ2IxWV85SGFSTG1lWXV1SWM3b3VYYW1UeUxJVHpKeEltZ0czVkcxV0NxN1BMYnVzUVYtT0puQW5QYw
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 18:40:52 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiyAFBVV95cUxOS1dZMENuZnd0VHB4djF6dHpDN3JvOWJPRW9uSVQ2a2N5cmJwM2NVdWtzLUIyZTAtbXVVcmEzSEtpejlTRkQ4OVUxTklHYzY0aUt3QmlOUExqQmZReW9oOEQtVXJBTVZhVFVmeW1HbVB0SW9adkFIMTZDNlVFeXhxZFJueWo5aFFhczQzNTdjQ2IxWV85SGFSTG1lWXV1SWM3b3VYYW1UeUxJVHpKeEltZ0czVkcxV0NxN1BMYnVzUVYtT0puQW5QYw?oc=5" target="_blank">Faculty Concerned About ASU’s New AI Course Builder</a>&nbsp;&nbsp;<font color="#6f6f6f">Inside Higher Ed</font>

## 201. Human-centered approach key in classroom AI implementation - K-12 Dive
- Domain: k12dive.com
- URL: https://news.google.com/rss/articles/CBMimwFBVV95cUxPZk1qT2FONWNibUZiYjJnN25DVFZ4amNzVzVaQUhhUThrb1laMnV1b0ZsQXFaN0piR2otUVpYMU9CT2FRZHNKdUhyMXM2U1pBTnNmZi1mTWZWcUJhLXZDNUV4QUJHLTlRRnJmdENYdHdJdjc3LVltbENCSHBRSXpfeTNpNkpaeEJoUFUxQkJUVjBhdExzbFNKNzJLVQ
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 18:08:20 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMimwFBVV95cUxPZk1qT2FONWNibUZiYjJnN25DVFZ4amNzVzVaQUhhUThrb1laMnV1b0ZsQXFaN0piR2otUVpYMU9CT2FRZHNKdUhyMXM2U1pBTnNmZi1mTWZWcUJhLXZDNUV4QUJHLTlRRnJmdENYdHdJdjc3LVltbENCSHBRSXpfeTNpNkpaeEJoUFUxQkJUVjBhdExzbFNKNzJLVQ?oc=5" target="_blank">Human-centered approach key in classroom AI implementation</a>&nbsp;&nbsp;<font color="#6f6f6f">K-12 Dive</font>

## 202. Un étudiant de TELECOM Nancy s'illustre à nouveau avec la 1ère place d'une compétition de cybersécurité au Canada - Université de Lorraine
- Domain: factuel.univ-lorraine.fr
- URL: https://news.google.com/rss/articles/CBMi6AFBVV95cUxQVUJvSVVsUFVfNDNoaklGN1pORjR5c1pGVWxCSE5pQmtEV2FsQmZuQVBsNFNSYjBzUFRoTjQ0dURzQjBnMTM4UnU1WUNMSUNpQ3dyLXdsQ2ZDU1gtdW9vY05wd0VleFVXbmVGSXhhZElYNXB1TS1YQTcxMzV6WVdOWmNzSTdpUVc1OVJNSDhzT1RrUE5QWmhmM2MwbGFCcEJTYkZ6TG01RFowOHFJb3FyM3I5LW11ZHVBRzdxLXNBd0puaUZuUjJzVkdEd0RLamF4REVJZXoxQVZqZFp1V1NZS3V2WWFZdHcy
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 18:00:15 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi6AFBVV95cUxQVUJvSVVsUFVfNDNoaklGN1pORjR5c1pGVWxCSE5pQmtEV2FsQmZuQVBsNFNSYjBzUFRoTjQ0dURzQjBnMTM4UnU1WUNMSUNpQ3dyLXdsQ2ZDU1gtdW9vY05wd0VleFVXbmVGSXhhZElYNXB1TS1YQTcxMzV6WVdOWmNzSTdpUVc1OVJNSDhzT1RrUE5QWmhmM2MwbGFCcEJTYkZ6TG01RFowOHFJb3FyM3I5LW11ZHVBRzdxLXNBd0puaUZuUjJzVkdEd0RLamF4REVJZXoxQVZqZFp1V1NZS3V2WWFZdHcy?oc=5" target="_blank">Un étudiant de TELECOM Nancy s'illustre à nouveau avec la 1ère place d'une compétition de cybersécurité au Canada</a>&nbsp;&nbsp;<font color="#6f6f6f">Université de Lorraine</font>

## 203. Ukraine’s AI Gambit Shows Middle Powers How to Play a Weak Hand - Lawfare
- Domain: lawfaremedia.org
- URL: https://news.google.com/rss/articles/CBMiogFBVV95cUxPc2RSVmFHUjR1TUlRWUZ3V2tUMk9qaE02UnJsYkNoVk9Gd0NrWHRtQVhzUXJFeEtJUDVqakk4REdELW1ZN2tMek1iZnlYb0p3NE1rWTJYeDQ4Wm9XZERqT1pNbzBLTTNaMnNxTE5FRTl1c3RZbUZvcVRTZmNmNlZwQlhBa3NfaHliWHkzMXpYcExCakFwZGotcGh5c0FtaDJLcHc
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 17:53:08 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxPc2RSVmFHUjR1TUlRWUZ3V2tUMk9qaE02UnJsYkNoVk9Gd0NrWHRtQVhzUXJFeEtJUDVqakk4REdELW1ZN2tMek1iZnlYb0p3NE1rWTJYeDQ4Wm9XZERqT1pNbzBLTTNaMnNxTE5FRTl1c3RZbUZvcVRTZmNmNlZwQlhBa3NfaHliWHkzMXpYcExCakFwZGotcGh5c0FtaDJLcHc?oc=5" target="_blank">Ukraine’s AI Gambit Shows Middle Powers How to Play a Weak Hand</a>&nbsp;&nbsp;<font color="#6f6f6f">Lawfare</font>

## 204. Solving the “Whac-a-mole dilemma”: A smarter way to debias AI vision models
- Domain: news.mit.edu
- URL: https://news.mit.edu/2026/smarter-way-to-debias-ai-vision-models-0429
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 17:40:00 -0400
- Summary: A new debiasing technique called WRING avoids creating or amplifying biases that can occur with existing debiasing approaches.

## 205. « Elle a mené les entretiens et pris les décisions d’embauche » : ce nouveau café est entièrement dirigé par l’IA - Ouest-France
- Domain: ouest-france.fr
- URL: https://news.google.com/rss/articles/CBMipAJBVV95cUxOV3JFb0VqNGtSU0FwWUVRX2lhQW0tUzQzekdKbjhDbEpjaThhbDZJN1FFSlAyUm1HODBCVlNpbW15OUlJanNpbW9GaUxTZU1Ib0lYcU1Wa3hMUzFRajI1UXNrZVN1Q2dBQjlDbGxPcUFON3Nra2FiLVVJSXAtVXZrYmFhZ2Z3bUFQbHVnekMzWVA5T3lkX0J0OGI3Zk51djhGWktmUkVzYXRzN0xSdGRQaUJMcEowSFF6RnYwVmFibnNpczRDMlJiZXhXdWFpcU81Tm9uRWw1UkdrWVVvUmMwZ3RHV1ZLZ1BBcEt2b1dNZ1AyMXRqRkFrOVdLY2llWUQyWWFNNUFXLTlhai1zam9acm8waml0TWhZbDNEMU53REN3ZFR1
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 17:26:51 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMipAJBVV95cUxOV3JFb0VqNGtSU0FwWUVRX2lhQW0tUzQzekdKbjhDbEpjaThhbDZJN1FFSlAyUm1HODBCVlNpbW15OUlJanNpbW9GaUxTZU1Ib0lYcU1Wa3hMUzFRajI1UXNrZVN1Q2dBQjlDbGxPcUFON3Nra2FiLVVJSXAtVXZrYmFhZ2Z3bUFQbHVnekMzWVA5T3lkX0J0OGI3Zk51djhGWktmUkVzYXRzN0xSdGRQaUJMcEowSFF6RnYwVmFibnNpczRDMlJiZXhXdWFpcU81Tm9uRWw1UkdrWVVvUmMwZ3RHV1ZLZ1BBcEt2b1dNZ1AyMXRqRkFrOVdLY2llWUQyWWFNNUFXLTlhai1zam9acm8waml0TWhZbDNEMU53REN3ZFR1?oc=5" target="_blank">« Elle a mené les entretiens et pris les décisions d’embauche » : ce nouveau café est entièrement dirigé par l’IA</a>&nbsp;&nbsp;<font color="#6f6f6f">Ouest-France</font>

## 206. When intelligence looks real, but the thinking isn't there. - Psychology Today
- Domain: psychologytoday.com
- URL: https://news.google.com/rss/articles/CBMiqgFBVV95cUxPUWlnV2dlek1ZV1ZiRVpQRDNRaVpSUlNWb2NXc2VCTG9PUmZmM1U0RjhBRWZtSkJRQmVSYk9JSGg0MVl1YmwtRnRwMmFXWjlUV21lWDVNR1E0ZG9jQzRFLWo0bzk2aWg0TUFQbjZtbi16VGt4VlBrb0ROSHRqckI1Mjc0Q2ZrU3UwOTRPbThrRC1VdTB0TGFQN19xcTNvTEJzVHdVeTlkRVhHZ9IBrwFBVV95cUxPbGIxOWdnQzcwS2Q5RF9vaFJZZmpnYXcyT25BaXZ6ai1iN0NNU1BOQjZTU2h0V1M3RFFXTEZ1Y05VeVRNd2dMbEh0WVJlSktETFQ5TmJVeWk1UjJoRlJNOFNFYkg5WjRwWEk5MXIxcVljdUNSQmZ5bzFlekEzZGFmVDQ0QjNoQlJMakdDUFotU2lEQ3NyLTlLY0d1U1RyZGxLU0FhMGtDa01Lcnd0WFhZ
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 16:46:31 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiqgFBVV95cUxPUWlnV2dlek1ZV1ZiRVpQRDNRaVpSUlNWb2NXc2VCTG9PUmZmM1U0RjhBRWZtSkJRQmVSYk9JSGg0MVl1YmwtRnRwMmFXWjlUV21lWDVNR1E0ZG9jQzRFLWo0bzk2aWg0TUFQbjZtbi16VGt4VlBrb0ROSHRqckI1Mjc0Q2ZrU3UwOTRPbThrRC1VdTB0TGFQN19xcTNvTEJzVHdVeTlkRVhHZ9IBrwFBVV95cUxPbGIxOWdnQzcwS2Q5RF9vaFJZZmpnYXcyT25BaXZ6ai1iN0NNU1BOQjZTU2h0V1M3RFFXTEZ1Y05VeVRNd2dMbEh0WVJlSktETFQ5TmJVeWk1UjJoRlJNOFNFYkg5WjRwWEk5MXIxcVljdUNSQmZ5bzFlekEzZGFmVDQ0QjNoQlJMakdDUFotU2lEQ3NyLTlLY0d1U1RyZGxLU0FhMGtDa01Lcnd0WFhZ?oc=5" target="_blank">When intelligence looks real, but the thinking isn't there.</a>&nbsp;&nbsp;<font color="#6f6f6f">Psychology Today</font>

## 207. Storytelling AI Could Help Identify Loneliness, Depression in Elders - University of Mississippi | Ole Miss
- Domain: olemiss.edu
- URL: https://news.google.com/rss/articles/CBMisAFBVV95cUxPXzZMUnRxMlFlY3lGTG8wNUdRaFRabnk2OGw5dFloekpVSHEtOFNrNTFKRU5zTjJfTlJ6aVVtanBKU2lDLXVFdGZzMnA5NjRhVUNMVnRzcnk0VDBUMEJUQlBaRE1hVUdlT1JvNWt4ajEtbEFQRmotZ3pNOVZfc3R4WUR3dEh3dzd2a1R1YkFPWlNLcWMyVEJpaWVNY21rQldrWXJndW9MbWtRMldBWnVRUQ
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 16:40:39 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMisAFBVV95cUxPXzZMUnRxMlFlY3lGTG8wNUdRaFRabnk2OGw5dFloekpVSHEtOFNrNTFKRU5zTjJfTlJ6aVVtanBKU2lDLXVFdGZzMnA5NjRhVUNMVnRzcnk0VDBUMEJUQlBaRE1hVUdlT1JvNWt4ajEtbEFQRmotZ3pNOVZfc3R4WUR3dEh3dzd2a1R1YkFPWlNLcWMyVEJpaWVNY21rQldrWXJndW9MbWtRMldBWnVRUQ?oc=5" target="_blank">Storytelling AI Could Help Identify Loneliness, Depression in Elders</a>&nbsp;&nbsp;<font color="#6f6f6f">University of Mississippi | Ole Miss</font>

## 208. Centre d'intelligence artificielle et science des données - Institut du Cerveau
- Domain: institutducerveau.org
- URL: https://news.google.com/rss/articles/CBMiigFBVV95cUxNMVBRckFZRkJaRk1mVGQ5VWN0SFByYS1hMXBGUzhCOVR1OTV6M3lsTllmYzVDdzdDblIyUkFrYzZFQjhCWUJiR0RwaW5WN1hCVURkM0w0ck93dGUwbkZ5d0ZWMERPYmNiSXhrOWhFX3Q5R3BBa0lZNGlDampWSTRDVmRKeWduR1I4dlE
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 16:20:55 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiigFBVV95cUxNMVBRckFZRkJaRk1mVGQ5VWN0SFByYS1hMXBGUzhCOVR1OTV6M3lsTllmYzVDdzdDblIyUkFrYzZFQjhCWUJiR0RwaW5WN1hCVURkM0w0ck93dGUwbkZ5d0ZWMERPYmNiSXhrOWhFX3Q5R3BBa0lZNGlDampWSTRDVmRKeWduR1I4dlE?oc=5" target="_blank">Centre d'intelligence artificielle et science des données</a>&nbsp;&nbsp;<font color="#6f6f6f">Institut du Cerveau</font>

## 209. When AI panic becomes violent - Taipei Times
- Domain: taipeitimes.com
- URL: https://news.google.com/rss/articles/CBMid0FVX3lxTE5ya0pZY19LdUNIdVd1YjRlM1YyWmo1SnZhakNNaWRiRFkwaXJnREtYeTR1SGRDUjJHZGV2bnZ6VkYwWHAxejIzSVU4RzhMN2tvSzJRN2sySnlLbzd4aS1nd2ZyX3JFTWFwWTIzMEpIN1hkWHBERjRv
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 16:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMid0FVX3lxTE5ya0pZY19LdUNIdVd1YjRlM1YyWmo1SnZhakNNaWRiRFkwaXJnREtYeTR1SGRDUjJHZGV2bnZ6VkYwWHAxejIzSVU4RzhMN2tvSzJRN2sySnlLbzd4aS1nd2ZyX3JFTWFwWTIzMEpIN1hkWHBERjRv?oc=5" target="_blank">When AI panic becomes violent</a>&nbsp;&nbsp;<font color="#6f6f6f">Taipei Times</font>

## 210. Le chatbot de Mistral serait un « vecteur de propagande étrangère » relayant de fausses informations, relève un rapport - Ouest-France
- Domain: ouest-france.fr
- URL: https://news.google.com/rss/articles/CBMirgJBVV95cUxQNW1fUjgyQkg4VWV3MnVMVXBqbHNiSzhxWFc0NHBXaHJpQWJLbG9RV2xnbVdKWW85emlPLVNkR3lvb2pvWkZ0eTFYcGRGWWZCM1RzRWxtbm10ZjhqMzNsY2dLaDlLcENaSEtkMUtRd09ILVNkU3pJZkV3ekk3MnBZSXhlb2FHUFR3Q0tCWkRIRF9udWo4OFN2TGNPQ1JmQWZGaUtJRGRaTGZuVUExT0xnVDVOUFlxYUdKdlprOGFwbW1oemJTb3NkTmZzeTVMa2d1MDE0d0RhVEhEMHNwbDA1Q05Pa1RKSWd2eUpFYmtOM2hmRV8yaHRRSXp1NHF4LXoxLTBvbFhvNXZqN3NBcmlDejJXQ210ODN0U2dObFYwaDliXzVRalZ0TlRGN1FkZw
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 15:04:14 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMirgJBVV95cUxQNW1fUjgyQkg4VWV3MnVMVXBqbHNiSzhxWFc0NHBXaHJpQWJLbG9RV2xnbVdKWW85emlPLVNkR3lvb2pvWkZ0eTFYcGRGWWZCM1RzRWxtbm10ZjhqMzNsY2dLaDlLcENaSEtkMUtRd09ILVNkU3pJZkV3ekk3MnBZSXhlb2FHUFR3Q0tCWkRIRF9udWo4OFN2TGNPQ1JmQWZGaUtJRGRaTGZuVUExT0xnVDVOUFlxYUdKdlprOGFwbW1oemJTb3NkTmZzeTVMa2d1MDE0d0RhVEhEMHNwbDA1Q05Pa1RKSWd2eUpFYmtOM2hmRV8yaHRRSXp1NHF4LXoxLTBvbFhvNXZqN3NBcmlDejJXQ210ODN0U2dObFYwaDliXzVRalZ0TlRGN1FkZw?oc=5" target="_blank">Le chatbot de Mistral serait un « vecteur de propagande étrangère » relayant de fausses informations, relève un rapport</a>&nbsp;&nbsp;<font color="#6f6f6f">Ouest-France</font>

## 211. Friendly AI chatbots more likely to support conspiracy theories, study finds
- Domain: theguardian.com
- URL: https://www.theguardian.com/technology/2026/apr/29/making-ai-chatbots-more-friendly-mistakes-support-false-beliefs-conspiracy-theories-study
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 15:00:52 GMT
- Summary: <p>Chatbots programmed to respond warmly even cast doubts on Apollo moon landings and fate of Hitler, researchers say</p><p>The rush to make AI chatbots more friendly has a troubling downside, researchers say. The warm personas make them prone to mistakes and sympathetic to crackpot beliefs.</p><p>Chatbots trained to respond more warmly gave poorer answers, worse health advice and even supported conspiracy theories by casting doubt on events such as the Apollo moon landings and the fate of Adolf Hitler.</p> <a href="https://www.theguardian.com/technology/2026/apr/29/making-ai-chatbots-more-friendly-mistakes-support-false-beliefs-conspiracy-theories-study">Continue reading...</a>

## 212. Tech3 | DK Shivakumar warns 50% jobs are at risk due to AI ; NPCI to meets Fintechs; and more - Moneycontrol.com
- Domain: moneycontrol.com
- URL: https://news.google.com/rss/articles/CBMi8wFBVV95cUxOOFhSWGxUdjhRRWdkT1FlX2dqRDhMUkxIN2o5MlRmVWhjV3VHZDlUWmx3RXp4alY4XzJmYUtuZnhmbWtWWGtRcFNwS01wVlYzQ0MyQlBHc3d2OHpZTXZwWkhvYlNiMzhkSlIxMC1iVjIzLXVLZGdkWk5nRE5zb0ZOZXhrT0NhcG9hUzdwemhCVW9ibkJnbVkwbnczd2Zrb295RU9iRG9BaXRnVlcxRm9HRXNveXVxMktZTVl0WXQ5a1gycm5HcmNoeGV5SG9ERXRXeXNicVlMZ3c0SGZVN0toYWYyMzktQ2VUY1FzSF9tcnpXZjg
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 13:50:39 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi8wFBVV95cUxOOFhSWGxUdjhRRWdkT1FlX2dqRDhMUkxIN2o5MlRmVWhjV3VHZDlUWmx3RXp4alY4XzJmYUtuZnhmbWtWWGtRcFNwS01wVlYzQ0MyQlBHc3d2OHpZTXZwWkhvYlNiMzhkSlIxMC1iVjIzLXVLZGdkWk5nRE5zb0ZOZXhrT0NhcG9hUzdwemhCVW9ibkJnbVkwbnczd2Zrb295RU9iRG9BaXRnVlcxRm9HRXNveXVxMktZTVl0WXQ5a1gycm5HcmNoeGV5SG9ERXRXeXNicVlMZ3c0SGZVN0toYWYyMzktQ2VUY1FzSF9tcnpXZjg?oc=5" target="_blank">Tech3 | DK Shivakumar warns 50% jobs are at risk due to AI ; NPCI to meets Fintechs; and more</a>&nbsp;&nbsp;<font color="#6f6f6f">Moneycontrol.com</font>

## 213. L’IA au travail peut-elle créer un sentiment d’injustice ? - Courrier Cadres
- Domain: courriercadres.com
- URL: https://news.google.com/rss/articles/CBMirAFBVV95cUxQQi1iX3ByTElIbUdJYlEtQmhieWJrbTFxNTVrS0pDLW5vYUxIN2poOW9tbkZvZmp4RjZ4bnlNck1mLS1TTEJwOGRFb2RHT3FtSGpEcTE0Z3JCUFpFNW1lX21IeVFtaUkzd1FidTN2S1UyU3gyNXRKd25hSkZlWWloTnZuVzhSTnlGNXcwMHdmM0x0WWJEQmhxRkJUSFNiV1FCd2lmd1gtUkVKbm9p
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 13:44:03 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMirAFBVV95cUxQQi1iX3ByTElIbUdJYlEtQmhieWJrbTFxNTVrS0pDLW5vYUxIN2poOW9tbkZvZmp4RjZ4bnlNck1mLS1TTEJwOGRFb2RHT3FtSGpEcTE0Z3JCUFpFNW1lX21IeVFtaUkzd1FidTN2S1UyU3gyNXRKd25hSkZlWWloTnZuVzhSTnlGNXcwMHdmM0x0WWJEQmhxRkJUSFNiV1FCd2lmd1gtUkVKbm9p?oc=5" target="_blank">L’IA au travail peut-elle créer un sentiment d’injustice ?</a>&nbsp;&nbsp;<font color="#6f6f6f">Courrier Cadres</font>

## 214. AI ‘deadbots’ can fuel pathological grief and affect how we deal with death - The Conversation
- Domain: theconversation.com
- URL: https://news.google.com/rss/articles/CBMirAFBVV95cUxNc0ZBM3U3S3pzaFEwWE12RDY5a1pPZFJLRG1TVHNJOXZhQ0pnVlFRZDg4N3RXUWc2Qnl1ejlMZlEyenlsTTQ4LTMtZ1BXS0w2blhuZ20wYnhzWVZnQldpMDFWWkZIY1dJT1NaWlJPVzFCdkwtSEhoMDhpYlZILVg0eUxWNGJoT3d4aWRVNDBmT1g2M2NKbDZ0Z3BHeVo0dmlkVEo4aXluUlczQlNQ
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 13:29:31 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMirAFBVV95cUxNc0ZBM3U3S3pzaFEwWE12RDY5a1pPZFJLRG1TVHNJOXZhQ0pnVlFRZDg4N3RXUWc2Qnl1ejlMZlEyenlsTTQ4LTMtZ1BXS0w2blhuZ20wYnhzWVZnQldpMDFWWkZIY1dJT1NaWlJPVzFCdkwtSEhoMDhpYlZILVg0eUxWNGJoT3d4aWRVNDBmT1g2M2NKbDZ0Z3BHeVo0dmlkVEo4aXluUlczQlNQ?oc=5" target="_blank">AI ‘deadbots’ can fuel pathological grief and affect how we deal with death</a>&nbsp;&nbsp;<font color="#6f6f6f">The Conversation</font>

## 215. Un ancien dirigeant d’AWS France va prendre la tête de Qwant et Shadow
- Domain: maddyness.com
- URL: https://www.maddyness.com/2026/04/29/un-ancien-dirigeant-daws-france-va-prendre-la-tete-de-qwant-et-shadow/
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 13:15:05 +0000
- Summary: <p>L’article <a href="https://www.maddyness.com/2026/04/29/un-ancien-dirigeant-daws-france-va-prendre-la-tete-de-qwant-et-shadow/">Un ancien dirigeant d’AWS France va prendre la tête de Qwant et Shadow</a> est apparu en premier sur <a href="https://www.maddyness.com">Maddyness - Le média pour comprendre l&#039;économie de demain</a>.</p>

## 216. Firestorm Labs raises $82M to take drone factories into the field
- Domain: techcrunch.com
- URL: https://techcrunch.com/2026/04/29/firestorm-labs-raises-82m-to-take-drone-factories-into-the-field/
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 13:10:57 +0000
- Summary: A defense startup just raised $82 million to put drone factories inside shipping containers and bring manufacturing to the front lines.

## 217. L’Arcom ouvre un débat explosif : la TNT pourrait s’arrêter en France
- Domain: siecledigital.fr
- URL: https://siecledigital.fr/2026/04/29/larcom-ouvre-un-debat-explosif-la-tnt-pourrait-sarreter-en-france/
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 12:51:53 +0000
- Summary: <a href="https://siecledigital.fr/2026/04/29/larcom-ouvre-un-debat-explosif-la-tnt-pourrait-sarreter-en-france/" rel="nofollow" title="L&rsquo;Arcom ouvre un débat explosif : la TNT pourrait s&rsquo;arrêter en France"><img alt="tnt" class="webfeedsFeaturedVisual wp-post-image" height="350" src="https://siecledigital.fr/wp-content/uploads/2026/04/tnt-600x350.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="600" /></a>On savait la TNT en déclin. On ne savait pas que le régulateur envisageait ouvertement de la débrancher. La consultation lancée le 24 avril par l&#8217;Arcom, ouverte jusqu&#8217;au 15 juin, change le ton du débat. Un réseau que les Français désertent Les données publiées par l&#8217;Arcom ne laissent pas beaucoup de place au doute. Au [&#8230;]

## 218. YouTube veut réinventer la recherche sur sa plateforme avec l’IA
- Domain: siecledigital.fr
- URL: https://siecledigital.fr/2026/04/29/youtube-veut-reinventer-la-recherche-sur-sa-plateforme-avec-lia/
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 12:51:08 +0000
- Summary: <a href="https://siecledigital.fr/2026/04/29/youtube-veut-reinventer-la-recherche-sur-sa-plateforme-avec-lia/" rel="nofollow" title="YouTube veut réinventer la recherche sur sa plateforme avec l&rsquo;IA"><img alt="youtube" class="webfeedsFeaturedVisual wp-post-image" height="350" src="https://siecledigital.fr/wp-content/uploads/2026/04/youtube-600x350.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="600" /></a>Tapez trois mots-clés, scrollez dans une grille de miniatures, ouvrez quatre vidéos avant de trouver celle qui répond vraiment à sa question. Ce concept représente le YouTube qu&#8217;on connaît tous. Google veut changer cela ou du moins essayer. C&#8217;est pour l&#8217;instant réservé aux abonnés Premium américains jusqu&#8217;au 8 juin. Posez directement une question Avec Ask [&#8230;]

## 219. Signal visé par une vaste opération d’espionnage russe en Allemagne
- Domain: siecledigital.fr
- URL: https://siecledigital.fr/2026/04/29/signal-vise-par-une-vaste-operation-despionnage-russe-en-allemagne/
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 12:50:40 +0000
- Summary: <a href="https://siecledigital.fr/2026/04/29/signal-vise-par-une-vaste-operation-despionnage-russe-en-allemagne/" rel="nofollow" title="Signal visé par une vaste opération d&rsquo;espionnage russe en Allemagne"><img alt="signal" class="webfeedsFeaturedVisual wp-post-image" height="350" src="https://siecledigital.fr/wp-content/uploads/2026/04/signal-600x350.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="600" /></a>Attention, personne n&#8217;a cassé le chiffrement de Signal. Le code tient et l&#8217;infrastructure également. La vigilance de plusieurs centaines de personnes face à un stratagème vieux comme le phishing, mais exécuté avec une précision chirurgicale a été mise à mal. Un faux support technique et de vrais dégâts Des pirates ont créé des profils baptisés [&#8230;]

## 220. Mistral AI face à un sérieux problème de désinformation avec son chatbot grand public
- Domain: siecledigital.fr
- URL: https://siecledigital.fr/2026/04/29/mistral-ai-face-a-un-serieux-probleme-de-desinformation-avec-son-chatbot-grand-public/
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 12:49:21 +0000
- Summary: <a href="https://siecledigital.fr/2026/04/29/mistral-ai-face-a-un-serieux-probleme-de-desinformation-avec-son-chatbot-grand-public/" rel="nofollow" title="Mistral AI face à un sérieux problème de désinformation avec son chatbot grand public"><img alt="mistral ai" class="webfeedsFeaturedVisual wp-post-image" height="350" src="https://siecledigital.fr/wp-content/uploads/2026/04/mistral-ai-1-600x350.jpg" style="display: block; margin: auto; margin-bottom: 5px;" width="600" /></a>Une épidémie de typhus à bord du Charles-de-Gaulle, des centaines de soldats américains tués dans une guerre en Iran. Le chancelier allemand qui s&#8217;achète secrètement un Boeing blindé contre les frappes nucléaires. Tout cela est faux. Et tout cela sort de la bouche du Chat quand on lui pose la question. Un test et dix [&#8230;]

## 221. Mistral AI face à un sérieux problème de désinformation avec son chatbot grand public - Siècle Digital
- Domain: siecledigital.fr
- URL: https://news.google.com/rss/articles/CBMivwFBVV95cUxPOGpjS0t4TmI3WTh5WUNTTTZxZjhTZm5FRldQbzZQWmZaZExrNVZxcU5iRmVCdlQ2X3dwVGNoZ19wbzJaTFE3dmdZQmNHYUhfblFDclVsUWg4M3RqTENCRTdkWUpOV21lNWJqeFBVeUpZTFlua0l1eEU3SWxQaWxIcWE4UC1kWWVqdkhqdDdrN3N3ZzdQaEdpZ1dvaHRoVTdoV3VwbFJmdzJEVmIxWS16NU03QUhtcHJXalFVS2tvdw
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 12:49:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMivwFBVV95cUxPOGpjS0t4TmI3WTh5WUNTTTZxZjhTZm5FRldQbzZQWmZaZExrNVZxcU5iRmVCdlQ2X3dwVGNoZ19wbzJaTFE3dmdZQmNHYUhfblFDclVsUWg4M3RqTENCRTdkWUpOV21lNWJqeFBVeUpZTFlua0l1eEU3SWxQaWxIcWE4UC1kWWVqdkhqdDdrN3N3ZzdQaEdpZ1dvaHRoVTdoV3VwbFJmdzJEVmIxWS16NU03QUhtcHJXalFVS2tvdw?oc=5" target="_blank">Mistral AI face à un sérieux problème de désinformation avec son chatbot grand public</a>&nbsp;&nbsp;<font color="#6f6f6f">Siècle Digital</font>

## 222. Warsh’s Fed chair nomination moves to full Senate
- Domain: bankingdive.com
- URL: https://www.bankingdive.com/news/warsh-fed-chair-nomination-senate-warren-tillis-gallego-trump-powell/818839/
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 12:12:35 -0400
- Summary: <figure><div><img src="https://imgproxy.divecdn.com/wfc4XND_ttMC42k54yce3Ko4uvR9eiDAwYWkp0UJEbU/g:ce/rs:fill:1600:900:1/Z3M6Ly9kaXZlc2l0ZS1zdG9yYWdlL2RpdmVpbWFnZS9jYXBpdG9sX2J1aWxkaW5nXy5qcGc=.webp" /></div></figure><p>The Senate Banking Committee, including once-holdout Sen. Thom Tillis, voted along party lines to keep alive ex-Federal Reserve Gov. Kevin Warsh&rsquo;s bid to succeed Jerome Powell atop the central bank.</p>

## 223. IA vs consultants : les LLM sont nuls en stratégie - Consultor
- Domain: consultor.fr
- URL: https://news.google.com/rss/articles/CBMiigFBVV95cUxNdWZPbE1nNEdTZ0ZTMUxhSGJESnFBM3Q5UDRPUmMzSk5rZ1laN2NRMlpFMmhCR2QtUEt4bnlTdlZZQkNfVkptRWEtZlNxYTlndnd0ZExGX25rdWtySWU5ckU0NDU0REwyU0tXdE9LSm5mTUZ4WmRPVzh1b2RiZlJuUFFfZy1MQkdwTEE
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 12:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiigFBVV95cUxNdWZPbE1nNEdTZ0ZTMUxhSGJESnFBM3Q5UDRPUmMzSk5rZ1laN2NRMlpFMmhCR2QtUEt4bnlTdlZZQkNfVkptRWEtZlNxYTlndnd0ZExGX25rdWtySWU5ckU0NDU0REwyU0tXdE9LSm5mTUZ4WmRPVzh1b2RiZlJuUFFfZy1MQkdwTEE?oc=5" target="_blank">IA vs consultants : les LLM sont nuls en stratégie</a>&nbsp;&nbsp;<font color="#6f6f6f">Consultor</font>

## 224. Why I, the CEO, am personally building our AI strategy - cio.com
- Domain: cio.com
- URL: https://news.google.com/rss/articles/CBMimAFBVV95cUxQakdiaE9KZXBJZmR2NHpDZ2NUQjRUaGdMelFGZzZNaDJpMFlaNXNKd1h2OVZ5eW5hMXZaSXJLWFVvenVUX1VCM0hqZlFGY3dzZE1hRnAzbmRlaU11Q0lYNWF0a200ZzY3Uy03dWUwMVhXU0c0TDdIX1R3R2VOZ2x2MEpGcmhnaGI0Q0EtOUFuczg0c0piNFQ5aw
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 11:53:30 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMimAFBVV95cUxQakdiaE9KZXBJZmR2NHpDZ2NUQjRUaGdMelFGZzZNaDJpMFlaNXNKd1h2OVZ5eW5hMXZaSXJLWFVvenVUX1VCM0hqZlFGY3dzZE1hRnAzbmRlaU11Q0lYNWF0a200ZzY3Uy03dWUwMVhXU0c0TDdIX1R3R2VOZ2x2MEpGcmhnaGI0Q0EtOUFuczg0c0piNFQ5aw?oc=5" target="_blank">Why I, the CEO, am personally building our AI strategy</a>&nbsp;&nbsp;<font color="#6f6f6f">cio.com</font>

## 225. A Beginner’s Guide to Building AI-Powered Applications - Nasscom
- Domain: community.nasscom.in
- URL: https://news.google.com/rss/articles/CBMiowFBVV95cUxNVEd3VzV5MkRMT2s1V2FBVjE4V1l4a2VvQS1FazFXQy12S09EcXBBdzBwOWxQX3JYTGpkeVVNNzlNQXpCR0xSRTEyWW5icWxNZklubzRVYU5BZ1kwa0Z4WjZXQldfQVREdWZRZVNlcGFEdGJCT3U0b2Y2UGN4Rzh1SF9ldFJ0SjVGSU9zZ2xjdlFqeUNzcjRuRE5ld2VFV0VnaTNF
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 10:25:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiowFBVV95cUxNVEd3VzV5MkRMT2s1V2FBVjE4V1l4a2VvQS1FazFXQy12S09EcXBBdzBwOWxQX3JYTGpkeVVNNzlNQXpCR0xSRTEyWW5icWxNZklubzRVYU5BZ1kwa0Z4WjZXQldfQVREdWZRZVNlcGFEdGJCT3U0b2Y2UGN4Rzh1SF9ldFJ0SjVGSU9zZ2xjdlFqeUNzcjRuRE5ld2VFV0VnaTNF?oc=5" target="_blank">A Beginner’s Guide to Building AI-Powered Applications</a>&nbsp;&nbsp;<font color="#6f6f6f">Nasscom</font>

## 226. Face à l’intelligence artificielle, Taylor Swift veut faire de sa voix une marquée déposée - France 24
- Domain: france24.com
- URL: https://news.google.com/rss/articles/CBMi7gFBVV95cUxQVmpPRGJhYzAwVU1YWFZmdXVxRVBIQjZwdUVwUEVpdzZyRmFQRFpzYUxBSlhvTHRRQkljbXFaQlVfdlAxakRqaFh4MlI1RklLbFNNdzVQbGp0VnhfZFNISjNpQXQ0SFZ5ZGREWWhSWXU4YTZ2Vmo2b0RYQ0NlTnFuQTUydWtYQlQwblMyWktZdGRIMUxfQ3RZTU9JZDQxRTRkN19KZmdiaTBFd3I0a3U1aVU1QTluelQ3NlBiR0NyWUdFcEp1U0wtWHBpSUQ4R1NNeDNuY1VCMl9JRThBc0FaaDlxRnNDaU1ZQTFlSFJR
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 10:05:07 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi7gFBVV95cUxQVmpPRGJhYzAwVU1YWFZmdXVxRVBIQjZwdUVwUEVpdzZyRmFQRFpzYUxBSlhvTHRRQkljbXFaQlVfdlAxakRqaFh4MlI1RklLbFNNdzVQbGp0VnhfZFNISjNpQXQ0SFZ5ZGREWWhSWXU4YTZ2Vmo2b0RYQ0NlTnFuQTUydWtYQlQwblMyWktZdGRIMUxfQ3RZTU9JZDQxRTRkN19KZmdiaTBFd3I0a3U1aVU1QTluelQ3NlBiR0NyWUdFcEp1U0wtWHBpSUQ4R1NNeDNuY1VCMl9JRThBc0FaaDlxRnNDaU1ZQTFlSFJR?oc=5" target="_blank">Face à l’intelligence artificielle, Taylor Swift veut faire de sa voix une marquée déposée</a>&nbsp;&nbsp;<font color="#6f6f6f">France 24</font>

## 227. Why AI companies want you to be afraid of them - BBC
- Domain: bbc.com
- URL: https://news.google.com/rss/articles/CBMijwFBVV95cUxPNFN2dUVWQmlPV0xJaVBmbFlxOEtWdUJXbktGRlZwZnlnVGxWVlhfZDJ1NGp0bTBQZlp5MnNGU2YySEI0RGhVNHk0VU10Ym5rRVNqOUpJbHgzMko5SWd1dkxucjF0S2hxcU1uX0FPbzQya2RZZUMwdjZQbGlFcXZ6UmdGeGdBQVp1UXNHQ05GOA
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 10:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMijwFBVV95cUxPNFN2dUVWQmlPV0xJaVBmbFlxOEtWdUJXbktGRlZwZnlnVGxWVlhfZDJ1NGp0bTBQZlp5MnNGU2YySEI0RGhVNHk0VU10Ym5rRVNqOUpJbHgzMko5SWd1dkxucjF0S2hxcU1uX0FPbzQya2RZZUMwdjZQbGlFcXZ6UmdGeGdBQVp1UXNHQ05GOA?oc=5" target="_blank">Why AI companies want you to be afraid of them</a>&nbsp;&nbsp;<font color="#6f6f6f">BBC</font>

## 228. Mayo Clinic AI detects pancreatic cancer up to 3 years before diagnosis in landmark validation study - Mayo Clinic News Network
- Domain: newsnetwork.mayoclinic.org
- URL: https://news.google.com/rss/articles/CBMi4AFBVV95cUxPQzItWTJVSXJhSUZROXM1Y0NYMnVqaVQzRmZwVXpTUlpQUnlTQzFqZHNVbm9YdmtNQXV2WG1YRG5HdGRFcmV3NEhEemdYTVN3N2c5TjdtWTZPTjd5U2JDT21kdTl1T3hOS2FPVDZSb08zQUZpS0M1Z1FyTXVjU0Z0NkZhV2N4Uktja2lKRTZlWkJaaXRuYjlWX0VxdDFrZnlIaHBtLVE2YUc2NXRwMjdWdlpTUFhmZ20xUUZURGJEUFFoWG8zUk1KVmE0VUN0TEpHcXF2VUhEdC1MUjJWZ3Rhcg
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 10:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi4AFBVV95cUxPQzItWTJVSXJhSUZROXM1Y0NYMnVqaVQzRmZwVXpTUlpQUnlTQzFqZHNVbm9YdmtNQXV2WG1YRG5HdGRFcmV3NEhEemdYTVN3N2c5TjdtWTZPTjd5U2JDT21kdTl1T3hOS2FPVDZSb08zQUZpS0M1Z1FyTXVjU0Z0NkZhV2N4Uktja2lKRTZlWkJaaXRuYjlWX0VxdDFrZnlIaHBtLVE2YUc2NXRwMjdWdlpTUFhmZ20xUUZURGJEUFFoWG8zUk1KVmE0VUN0TEpHcXF2VUhEdC1MUjJWZ3Rhcg?oc=5" target="_blank">Mayo Clinic AI detects pancreatic cancer up to 3 years before diagnosis in landmark validation study</a>&nbsp;&nbsp;<font color="#6f6f6f">Mayo Clinic News Network</font>

## 229. Meet the AI jailbreakers: ‘I see the worst things humanity has produced’ - The Guardian
- Domain: theguardian.com
- URL: https://news.google.com/rss/articles/CBMivAFBVV95cUxQMmh0MmlXNUpueW5wME1lRTctZWwwYmtaSkxMbXlqc2VkR3p2QWduTXU4MWZsbnBMX2h5alBzS05mOVhWSzJRNmkzdnJWNHNRSV8zQzJFeWtpWDVVckctampYb2NhS0ExUDBEdlUxOElKcFpwY0NOU2N2YVlVZlNVSGp4NUg0cWdlc01tRGVTZDgtUG4tVDQ2cUE4OHBzS3dzVG8xaXlnTUh0alZRcHFTc3RyZkprdTB2VnY4ZA
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 09:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMivAFBVV95cUxQMmh0MmlXNUpueW5wME1lRTctZWwwYmtaSkxMbXlqc2VkR3p2QWduTXU4MWZsbnBMX2h5alBzS05mOVhWSzJRNmkzdnJWNHNRSV8zQzJFeWtpWDVVckctampYb2NhS0ExUDBEdlUxOElKcFpwY0NOU2N2YVlVZlNVSGp4NUg0cWdlc01tRGVTZDgtUG4tVDQ2cUE4OHBzS3dzVG8xaXlnTUh0alZRcHFTc3RyZkprdTB2VnY4ZA?oc=5" target="_blank">Meet the AI jailbreakers: ‘I see the worst things humanity has produced’</a>&nbsp;&nbsp;<font color="#6f6f6f">The Guardian</font>

## 230. Future of Work Summit: Half of jobs may change, not disappear: Govt, Quess flag AI-led shift - Moneycontrol.com
- Domain: moneycontrol.com
- URL: https://news.google.com/rss/articles/CBMi9gFBVV95cUxNMHdoOWJnLVZtVzNLcEFTa3kzWE5xVk9vUmZvWENBb21IYnM5ZUtWRmVtT3EzSENPX3FJblI5QURXWEVfTjlsTnJJQWhfM1FFV0VlcjlGRElEVUlBVkNSZmw3c3R4QWdGU3NjTzc1MXlOYlYwV2ZFaVd5cEk1NGZrdFFYWGRPMkVYYTdWczRuVTNxUF9IcjY3d2g5R2d5M3NLaFpOYU9Qa0MxS2x6WGhlZWctVDNYb1pRa2FVSEZRRjY4WDM0YVAtNWNfMXZKSl9YNFNySGJyamdTak5CN0hSTnNpdUx4dGl3djN0MmQtWmlsYXI0SWfSAfsBQVVfeXFMTXRyMkxuNHNjdGhrd3VzTVV5Ry1vRXZVUjY4ajdtQUZtQWdLWVhwWjVpWjNWM1lhN1FxU0dySW9GTjVNamRyaGpCUWw0RFpPVWlxZGtFVUMwWm5sbjVTV2ZfZlc0WkJ4RThJLXh2THBYb21VVDJYampXY3hLMXE3WUJOWloxTTBSdDBoaExlZndNRXNlT1NOZlRUWWZfTGctZGJid1p3b0tWTi10RnkycW4tTlBRM1AxNlFXOVY3anpFNjIzcWdXZExRRUlnX3c3d1pQSlZoVFFrOXRxY0pMNzRzOHlrNFIyS01HUUtPLTBLaGd2ZU50R3BnMTA
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 08:32:09 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi9gFBVV95cUxNMHdoOWJnLVZtVzNLcEFTa3kzWE5xVk9vUmZvWENBb21IYnM5ZUtWRmVtT3EzSENPX3FJblI5QURXWEVfTjlsTnJJQWhfM1FFV0VlcjlGRElEVUlBVkNSZmw3c3R4QWdGU3NjTzc1MXlOYlYwV2ZFaVd5cEk1NGZrdFFYWGRPMkVYYTdWczRuVTNxUF9IcjY3d2g5R2d5M3NLaFpOYU9Qa0MxS2x6WGhlZWctVDNYb1pRa2FVSEZRRjY4WDM0YVAtNWNfMXZKSl9YNFNySGJyamdTak5CN0hSTnNpdUx4dGl3djN0MmQtWmlsYXI0SWfSAfsBQVVfeXFMTXRyMkxuNHNjdGhrd3VzTVV5Ry1vRXZVUjY4ajdtQUZtQWdLWVhwWjVpWjNWM1lhN1FxU0dySW9GTjVNamRyaGpCUWw0RFpPVWlxZGtFVUMwWm5sbjVTV2ZfZlc0WkJ4RThJLXh2THBYb21VVDJYampXY3hLMXE3WUJOWloxTTBSdDBoaExlZndNRXNlT1NOZlRUWWZfTGctZGJid1p3b0tWTi10RnkycW4tTlBRM1AxNlFXOVY3anpFNjIzcWdXZExRRUlnX3c3d1pQSlZoVFFrOXRxY0pMNzRzOHlrNFIyS01HUUtPLTBLaGd2ZU50R3BnMTA?oc=5" target="_blank">Future of Work Summit: Half of jobs may change, not disappear: Govt, Quess flag AI-led shift</a>&nbsp;&nbsp;<font color="#6f6f6f">Moneycontrol.com</font>

## 231. Devant l’amélioration de l’IA, la crise existentielle d’un prix littéraire japonais - Courrier international
- Domain: courrierinternational.com
- URL: https://news.google.com/rss/articles/CBMi1gFBVV95cUxNc0YxbUpsMGhoMlotT01IazdCZEk4Nnh6OGNiLWZaN01EWG44LTVEV2NaQW9nVEJkVlBwMWY1U2pLM01KcU1ud0JDY0NHWHhWZzNIaEtWNXg2UFRaRjc3cG1VQlhpYms2cnJuZkVTakNxbHFEQ0FxV3NGNlN0X283WWIxUVAtRlZERjB3MkdJRmlIUEJ6VzFmSVpJWU1sUzVmUlB1cUhBdU5YanJDYUFZOU8tdGVDMUhHQ1A2MU9pMDNReFZzZDZTU29xckJJTmhHS29NVU93
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 08:23:18 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi1gFBVV95cUxNc0YxbUpsMGhoMlotT01IazdCZEk4Nnh6OGNiLWZaN01EWG44LTVEV2NaQW9nVEJkVlBwMWY1U2pLM01KcU1ud0JDY0NHWHhWZzNIaEtWNXg2UFRaRjc3cG1VQlhpYms2cnJuZkVTakNxbHFEQ0FxV3NGNlN0X283WWIxUVAtRlZERjB3MkdJRmlIUEJ6VzFmSVpJWU1sUzVmUlB1cUhBdU5YanJDYUFZOU8tdGVDMUhHQ1A2MU9pMDNReFZzZDZTU29xckJJTmhHS29NVU93?oc=5" target="_blank">Devant l’amélioration de l’IA, la crise existentielle d’un prix littéraire japonais</a>&nbsp;&nbsp;<font color="#6f6f6f">Courrier international</font>

## 232. ‘We are a new banking desert’: Oregon bank group CEO
- Domain: bankingdive.com
- URL: https://www.bankingdive.com/news/oregon-new-bank-tax-credit-de-novo-state-charter/818789/
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 08:07:40 -0400
- Summary: <figure><div><img src="https://imgproxy.divecdn.com/Grr6xxZVPmp8XiQ1qBYQVIrayUTXmt65yMa1bdgMluQ/g:ce/rs:fill:1600:900:1/Z3M6Ly9kaXZlc2l0ZS1zdG9yYWdlL2RpdmVpbWFnZS9HZXR0eUltYWdlcy0xNjM4NTE5MDcuanBn.webp" /></div></figure><p>A tax credit, set to take effect in June, aims to stimulate de novo activity in the state, which hasn&rsquo;t chartered a new bank since 2007.</p>

## 233. India’s 2025 Cybersecurity Shift: Bolstering Defence Through AI - orfonline.org
- Domain: orfonline.org
- URL: https://news.google.com/rss/articles/CBMiowFBVV95cUxOamJHTUYxZjM0WWJuclVGS3dWdEVEYjJyTWR0cmtpUXhTQllha29oQ042UDMzTUJuSmRDcUVMbGNBNWRMT1JWY25xdnNaR2g4Tld5VFo2OUtUNVhRWHBfLVJqVXc4cG9ibVRtVTJFamlUeTNKYnVJTTFqcmRHMWhqOE82TC1nUXBlbDU0RHlxS1VpbkpZYnpQcUFpdFdQaDFiWnJR
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 07:56:32 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiowFBVV95cUxOamJHTUYxZjM0WWJuclVGS3dWdEVEYjJyTWR0cmtpUXhTQllha29oQ042UDMzTUJuSmRDcUVMbGNBNWRMT1JWY25xdnNaR2g4Tld5VFo2OUtUNVhRWHBfLVJqVXc4cG9ibVRtVTJFamlUeTNKYnVJTTFqcmRHMWhqOE82TC1nUXBlbDU0RHlxS1VpbkpZYnpQcUFpdFdQaDFiWnJR?oc=5" target="_blank">India’s 2025 Cybersecurity Shift: Bolstering Defence Through AI</a>&nbsp;&nbsp;<font color="#6f6f6f">orfonline.org</font>

## 234. Objectifs ratés, investissements massifs : OpenAI face à un tournant stratégique - l'Opinion
- Domain: lopinion.fr
- URL: https://news.google.com/rss/articles/CBMizgFBVV95cUxORHJhX0I0bUtVTlByMlNIRjBWazNueElqcm9vRnI4aW1jSkZJSXRiNWM5Y3A4TGpPV2h6TDlCN2dIZ1k2bVN3WUczZDVLTGJsLWZqMzZTYzRSUnJnMjV6Mm1PcHlyTDkweHlYMllvb1doSVVuZWVvR04yYl9meUpnWnRLdU9HSUZZODdtanBBVjlWRzZIOEFnZGpvaTdIZi11OEFYbXR1ZU9oVGNBYmgxbWJRSjljMUdaVjJMMjhfdmQ2ZGFVR1pldzFRRHlYZw
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 07:41:09 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMizgFBVV95cUxORHJhX0I0bUtVTlByMlNIRjBWazNueElqcm9vRnI4aW1jSkZJSXRiNWM5Y3A4TGpPV2h6TDlCN2dIZ1k2bVN3WUczZDVLTGJsLWZqMzZTYzRSUnJnMjV6Mm1PcHlyTDkweHlYMllvb1doSVVuZWVvR04yYl9meUpnWnRLdU9HSUZZODdtanBBVjlWRzZIOEFnZGpvaTdIZi11OEFYbXR1ZU9oVGNBYmgxbWJRSjljMUdaVjJMMjhfdmQ2ZGFVR1pldzFRRHlYZw?oc=5" target="_blank">Objectifs ratés, investissements massifs : OpenAI face à un tournant stratégique</a>&nbsp;&nbsp;<font color="#6f6f6f">l'Opinion</font>

## 235. Citi taps former Google exec as CIO
- Domain: bankingdive.com
- URL: https://www.bankingdive.com/news/citi-hires-google-exec-brian-saluzzo-cio-tim-ryan/818767/
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 06:17:00 -0400
- Summary: <figure><div><img src="https://imgproxy.divecdn.com/tz2TfgyUhYEoRDuxrDqi-4Pa9odPW3kQcCmVHixQomI/g:ce/rs:fill:1600:900:1/Z3M6Ly9kaXZlc2l0ZS1zdG9yYWdlL2RpdmVpbWFnZS9HZXR0eUltYWdlcy0yMDUxMTczMTMxLmpwZw==.webp" /></div></figure><p>Brian Saluzzo began his tenure with Citi in March, joining as the bank rolls out AI and nears completion of a business transformation initiative.</p>

## 236. La nouvelle difficulté du monde n’est plus de résoudre un problème, mais de l’identifier
- Domain: maddyness.com
- URL: https://www.maddyness.com/2026/04/29/ia-ecoute-identifier-problemes-creer-valeur/
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 06:00:02 +0000
- Summary: <p>L’article <a href="https://www.maddyness.com/2026/04/29/ia-ecoute-identifier-problemes-creer-valeur/">La nouvelle difficulté du monde n’est plus de résoudre un problème, mais de l’identifier</a> est apparu en premier sur <a href="https://www.maddyness.com">Maddyness - Le média pour comprendre l&#039;économie de demain</a>.</p>

## 237. IA : le marché de l’emploi dans la tech en pleine restructuration
- Domain: maddyness.com
- URL: https://www.maddyness.com/2026/04/29/ia-le-marche-de-lemploi-dans-la-tech-en-pleine-restructuration/
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 05:00:45 +0000
- Summary: <p>L’article <a href="https://www.maddyness.com/2026/04/29/ia-le-marche-de-lemploi-dans-la-tech-en-pleine-restructuration/">IA : le marché de l’emploi dans la tech en pleine restructuration</a> est apparu en premier sur <a href="https://www.maddyness.com">Maddyness - Le média pour comprendre l&#039;économie de demain</a>.</p>

## 238. Taiwan firms face hurdles in U.S. expansion amid AI-driven shift: Experts - Focus Taiwan
- Domain: focustaiwan.tw
- URL: https://news.google.com/rss/articles/CBMiV0FVX3lxTE14V2RIRHFscFJNVUdVUG9yRTVhTkVhRERfS25DNHczd01FVUEzOFpnSFhuRVo2VmY3OUM5aGVsSnFKNmgtcE9MMWQyalNNcVFyWFNmYjFCNA
- Relevance score: 4.0
- Published: Wed, 29 Apr 2026 04:30:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiV0FVX3lxTE14V2RIRHFscFJNVUdVUG9yRTVhTkVhRERfS25DNHczd01FVUEzOFpnSFhuRVo2VmY3OUM5aGVsSnFKNmgtcE9MMWQyalNNcVFyWFNmYjFCNA?oc=5" target="_blank">Taiwan firms face hurdles in U.S. expansion amid AI-driven shift: Experts</a>&nbsp;&nbsp;<font color="#6f6f6f">Focus Taiwan</font>

## 239. DeepSeek V4 Signals a New Phase in the U.S.-China AI Rivalry - Council on Foreign Relations
- Domain: cfr.org
- URL: https://news.google.com/rss/articles/CBMikgFBVV95cUxOalo2blFVcFJMSGxHTDBsTVlUTE9sMkd4UUFULWFNaVItaWNtY0hkcnVvM1FLbjUxZmt2ZDlzVnN0cHJBRnVqNEdCejUtcmFoZXlMTXNpdlpmY3ZIMGtiTE4xcVVULXVQaTgxNnB2TzRiNEtHZkdTeTNTZ00xX1Q4S05NNGFVTmgxUHpZeXFrWlhaQQ
- Relevance score: 4.0
- Published: Tue, 28 Apr 2026 18:09:11 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMikgFBVV95cUxOalo2blFVcFJMSGxHTDBsTVlUTE9sMkd4UUFULWFNaVItaWNtY0hkcnVvM1FLbjUxZmt2ZDlzVnN0cHJBRnVqNEdCejUtcmFoZXlMTXNpdlpmY3ZIMGtiTE4xcVVULXVQaTgxNnB2TzRiNEtHZkdTeTNTZ00xX1Q4S05NNGFVTmgxUHpZeXFrWlhaQQ?oc=5" target="_blank">DeepSeek V4 Signals a New Phase in the U.S.-China AI Rivalry</a>&nbsp;&nbsp;<font color="#6f6f6f">Council on Foreign Relations</font>

## 240. Opinion | Americans are down on AI. These two caricatures are to blame. - The Washington Post
- Domain: washingtonpost.com
- URL: https://news.google.com/rss/articles/CBMiugFBVV95cUxPSHpCTjc2UEp6RWlHcGp1UlUyOVRTUU9VanZTN3pRbDNUeHljUWpIbVdhZEZPR3lKOWxsSEtHTEVjcEd0dnlqaDMzdXI5Y25nUmQwNVRDRF9PUkMwLTBsQ0ZXUWJ0Y1ZyYlM3WVdDcG1vM0h3XzFVZjRVRHhYV2V3T2hidTF1TWI4VjFmazkwalk1WjZpOWc5ME1kWGxzTDcwajdWc2ZTMUV2SVV1OVRUZkZ3WkJsYkpVNlE
- Relevance score: 4.0
- Published: Tue, 28 Apr 2026 18:00:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiugFBVV95cUxPSHpCTjc2UEp6RWlHcGp1UlUyOVRTUU9VanZTN3pRbDNUeHljUWpIbVdhZEZPR3lKOWxsSEtHTEVjcEd0dnlqaDMzdXI5Y25nUmQwNVRDRF9PUkMwLTBsQ0ZXUWJ0Y1ZyYlM3WVdDcG1vM0h3XzFVZjRVRHhYV2V3T2hidTF1TWI4VjFmazkwalk1WjZpOWc5ME1kWGxzTDcwajdWc2ZTMUV2SVV1OVRUZkZ3WkJsYkpVNlE?oc=5" target="_blank">Opinion | Americans are down on AI. These two caricatures are to blame.</a>&nbsp;&nbsp;<font color="#6f6f6f">The Washington Post</font>

## 241. 4 Semiconductor Stocks for AI Exposure Beyond Mag 7 - Gotrade
- Domain: heygotrade.com
- URL: https://news.google.com/rss/articles/CBMihwFBVV95cUxPNlFzLWhON29jSXpkb29Jb0F6RjBDWjBDN09tUlI3RkVqR0JqQzNlSkhBTlZzVWd4Q2o4N25peDZwa1hJSGk2aXhjUF9oa1dHODhnVUtILUk4d3NKQzBBU3pNWW9STFpsLWJ3ZkhKR3lEV00wVmpRUVo0RE1wMzAzX2Z5SXl2S2s
- Relevance score: 4.0
- Published: Tue, 28 Apr 2026 13:07:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMihwFBVV95cUxPNlFzLWhON29jSXpkb29Jb0F6RjBDWjBDN09tUlI3RkVqR0JqQzNlSkhBTlZzVWd4Q2o4N25peDZwa1hJSGk2aXhjUF9oa1dHODhnVUtILUk4d3NKQzBBU3pNWW9STFpsLWJ3ZkhKR3lEV00wVmpRUVo0RE1wMzAzX2Z5SXl2S2s?oc=5" target="_blank">4 Semiconductor Stocks for AI Exposure Beyond Mag 7</a>&nbsp;&nbsp;<font color="#6f6f6f">Gotrade</font>

## 242. Déploiement massif de formations à l’IA pédagogique - Agence Universitaire de la Francophonie
- Domain: auf.org
- URL: https://news.google.com/rss/articles/CBMie0FVX3lxTE9sVWZyRTFEVUlyRmVWekRKZ1dkVEcxZUVGWTZiR0J1WExOV1BQRGcyYTVEMzRrYWZDTi1xTW5kaF81UG91VTdYeklWWHoteVVsZGhKdVVlZ1ktWjBMbXI1S1NaR2dDcGFXMkt3NUlGcjRIRldVNV8tMTNfTQ
- Relevance score: 4.0
- Published: Tue, 28 Apr 2026 08:39:57 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMie0FVX3lxTE9sVWZyRTFEVUlyRmVWekRKZ1dkVEcxZUVGWTZiR0J1WExOV1BQRGcyYTVEMzRrYWZDTi1xTW5kaF81UG91VTdYeklWWHoteVVsZGhKdVVlZ1ktWjBMbXI1S1NaR2dDcGFXMkt3NUlGcjRIRldVNV8tMTNfTQ?oc=5" target="_blank">Déploiement massif de formations à l’IA pédagogique</a>&nbsp;&nbsp;<font color="#6f6f6f">Agence Universitaire de la Francophonie</font>

## 243. Du "cloud" aux puces, Amazon fait des étincelles avec l'IA - Boursorama
- Domain: boursorama.com
- URL: https://news.google.com/rss/articles/CBMizgFBVV95cUxOa3k3RFVCb3Z0cHhOZmtseGpJM0FjT3lkNDd4cEU5UE9HclpHRUQ0eUNfamxibDJPTlNSSjMyRG5PUjJhbklCZUFZeXdxLTljajNJbVlLSjFmM3M3bm1rdzE1VzVpbXhVVXZDTkhJazNmZU1GOTQwNWthTklmRmlMaTBzZFVPZTZTZmhFem5Eb1N2ay13SVpWNGoxNWlLRV82S1pLbXl4cDAzM3hCdDE0SWRPNjk2M0dfVlFNV18xVXdKemVjT21mNWlCUm0tQdIB0wFBVV95cUxPM25QOUNQUTFzZWVJbUJtVTlGN1NYY1Y2blB4Q0lxRURLUm4yS2EzLXF3OThNS3BGR0oyODkyUEhWRzlyUUs1MTBqckRiczJOWkdrSWVFRUJjRGFCdXdmcWFWZzlWVUN1VXlWd3lJMTZZUlpmelNVOXMtTTdTTGdkRkI5alY5WkUwS29ZX3hScy1BTXA5TjJhcTdSUmFvSmxGYTRnQ3c0QUVkaGF1NEdCdUVOQzFQX1hmQWNDWjJRZDd3b3BKWnV6ekhLWHpETGx6Z21N
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 06:10:01 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMizgFBVV95cUxOa3k3RFVCb3Z0cHhOZmtseGpJM0FjT3lkNDd4cEU5UE9HclpHRUQ0eUNfamxibDJPTlNSSjMyRG5PUjJhbklCZUFZeXdxLTljajNJbVlLSjFmM3M3bm1rdzE1VzVpbXhVVXZDTkhJazNmZU1GOTQwNWthTklmRmlMaTBzZFVPZTZTZmhFem5Eb1N2ay13SVpWNGoxNWlLRV82S1pLbXl4cDAzM3hCdDE0SWRPNjk2M0dfVlFNV18xVXdKemVjT21mNWlCUm0tQdIB0wFBVV95cUxPM25QOUNQUTFzZWVJbUJtVTlGN1NYY1Y2blB4Q0lxRURLUm4yS2EzLXF3OThNS3BGR0oyODkyUEhWRzlyUUs1MTBqckRiczJOWkdrSWVFRUJjRGFCdXdmcWFWZzlWVUN1VXlWd3lJMTZZUlpmelNVOXMtTTdTTGdkRkI5alY5WkUwS29ZX3hScy1BTXA5TjJhcTdSUmFvSmxGYTRnQ3c0QUVkaGF1NEdCdUVOQzFQX1hmQWNDWjJRZDd3b3BKWnV6ekhLWHpETGx6Z21N?oc=5" target="_blank">Du "cloud" aux puces, Amazon fait des étincelles avec l'IA</a>&nbsp;&nbsp;<font color="#6f6f6f">Boursorama</font>

## 244. Microsoft Profits Jump As Cloud, AI Drive Quarterly Growth - Bernama
- Domain: bernama.com
- URL: https://news.google.com/rss/articles/CBMiYkFVX3lxTE5adGE4VGU0anJYZ2FjR2h2WVhmUEtleE44bGtJODZWSmRvYnFtVHY2OFdQdFE3eW9EREpMcmFPcnVkM0hySXJ3QXZtMWs1YkNKR1pReGhTTEhlMDRMT2RiSVdB
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 06:01:46 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE5adGE4VGU0anJYZ2FjR2h2WVhmUEtleE44bGtJODZWSmRvYnFtVHY2OFdQdFE3eW9EREpMcmFPcnVkM0hySXJ3QXZtMWs1YkNKR1pReGhTTEhlMDRMT2RiSVdB?oc=5" target="_blank">Microsoft Profits Jump As Cloud, AI Drive Quarterly Growth</a>&nbsp;&nbsp;<font color="#6f6f6f">Bernama</font>

## 245. Mobilier de bureau : l’angle mort de l’agilité financière
- Domain: maddyness.com
- URL: https://www.maddyness.com/2026/04/30/mobilier-de-bureau-langle-mort-de-lagilite-financiere/
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 06:00:45 +0000
- Summary: <p>L’article <a href="https://www.maddyness.com/2026/04/30/mobilier-de-bureau-langle-mort-de-lagilite-financiere/">Mobilier de bureau : l’angle mort de l’agilité financière</a> est apparu en premier sur <a href="https://www.maddyness.com">Maddyness - Le média pour comprendre l&#039;économie de demain</a>.</p>

## 246. AI Video Shared as WB Education Minister Bratya Basu Taking Bribe Amid Elections - The Quint
- Domain: thequint.com
- URL: https://news.google.com/rss/articles/CBMitwFBVV95cUxNRUh0aGZIaXJRUGJ3Tk1ocXVTdXVPc2RITnUxTWVIWENseTMzVDdBdWhGWF9BQjU0amdCRDhVR0t6OFN0ZTU1bjNlTFFqQlBTYWFhcDJPTW9VTFZ4cDNwYUl3ckdod1FiTTF4bEZyWjNFcjdHeXotbm9FemF1UGRRdnptZV80WHc2WmdZQ19SdU02U3VVN3hwZ2xOaGVUWEI1bmZpS2hOeUg0RTk4NWRxNmdqR0g3VkHSAcQBQVVfeXFMUHZJRE5waWkxV1ZocjdndVFHOE5IRFExbTNfWUM1S1RHblBndy1XUmxhZDlIQWZpT1NFTzRvRnpaTjFjUG1qYWNtSkpvbUp4Rmd5dkU5UGNoZXdXVnZmYlFYUDdRZG9MRlVnVjg3Nzg1WDVQZXl0anNNWWlWeWkwdkV0OHhOSm44dTEwYnBOQTFON0c5VHpfazRfNFhnQVB6VXAtUjVvdEZxYlN4MDRqSV9OMlBwTTQxMkYwb1Z0RlFwR0FmeA
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 05:49:47 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMitwFBVV95cUxNRUh0aGZIaXJRUGJ3Tk1ocXVTdXVPc2RITnUxTWVIWENseTMzVDdBdWhGWF9BQjU0amdCRDhVR0t6OFN0ZTU1bjNlTFFqQlBTYWFhcDJPTW9VTFZ4cDNwYUl3ckdod1FiTTF4bEZyWjNFcjdHeXotbm9FemF1UGRRdnptZV80WHc2WmdZQ19SdU02U3VVN3hwZ2xOaGVUWEI1bmZpS2hOeUg0RTk4NWRxNmdqR0g3VkHSAcQBQVVfeXFMUHZJRE5waWkxV1ZocjdndVFHOE5IRFExbTNfWUM1S1RHblBndy1XUmxhZDlIQWZpT1NFTzRvRnpaTjFjUG1qYWNtSkpvbUp4Rmd5dkU5UGNoZXdXVnZmYlFYUDdRZG9MRlVnVjg3Nzg1WDVQZXl0anNNWWlWeWkwdkV0OHhOSm44dTEwYnBOQTFON0c5VHpfazRfNFhnQVB6VXAtUjVvdEZxYlN4MDRqSV9OMlBwTTQxMkYwb1Z0RlFwR0FmeA?oc=5" target="_blank">AI Video Shared as WB Education Minister Bratya Basu Taking Bribe Amid Elections</a>&nbsp;&nbsp;<font color="#6f6f6f">The Quint</font>

## 247. Mphasis Q4 Net Profit Rises 14% YoY as AI-Led Deals Gain Traction - Analytics India Magazine
- Domain: analyticsindiamag.com
- URL: https://news.google.com/rss/articles/CBMipAFBVV95cUxPeWdFNlF0bnJEeWFJNWsxUVpsS1BwUjByZjB2MDF3ak1lZHphN2JjUHlIamJHN2paN21EbEFFWFVEcE80TXY1NXZQY3d0d0NWQk1zS2lPZDVYODNqNE8wMVZPcGpiT1JOQ3NwRzFzdnR2cFViUHBzRWJWQmM4LUF6NGJBUUhHQzNUZTBnZnhHUzc5Tmh4QW9MaUNVTjlGOVA2SzJZUw
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 05:48:45 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMipAFBVV95cUxPeWdFNlF0bnJEeWFJNWsxUVpsS1BwUjByZjB2MDF3ak1lZHphN2JjUHlIamJHN2paN21EbEFFWFVEcE80TXY1NXZQY3d0d0NWQk1zS2lPZDVYODNqNE8wMVZPcGpiT1JOQ3NwRzFzdnR2cFViUHBzRWJWQmM4LUF6NGJBUUhHQzNUZTBnZnhHUzc5Tmh4QW9MaUNVTjlGOVA2SzJZUw?oc=5" target="_blank">Mphasis Q4 Net Profit Rises 14% YoY as AI-Led Deals Gain Traction</a>&nbsp;&nbsp;<font color="#6f6f6f">Analytics India Magazine</font>

## 248. Mistral, champion français de l’IA, est-il le roi de la désinformation ? - Libération
- Domain: liberation.fr
- URL: https://news.google.com/rss/articles/CBMi7wFBVV95cUxNMFN1X3c2VDY2QzFKWDB5RzNud0pJeGQxYUFZcnU1c3RUWG45OURHS1EtaF90WTFaNzNBd1VFMGtDU2Q3a2Q3STkxYzZtZzBvdGhZUjNiOUFjWTFEanB0MU5BVlUwQW9vMXFiRTdoWmMxc2xPQUtVV1JuYkcwSHZtd3RfOW93RGk4NjRob3JscURIdE5iMTdfWmJFQ0I3TkdrcW5ENFJlajdiNEZrRVM4ZFU5U0o3MVhIMTl1NElsb0I3NUxadjB0WDB1T1lfbUpLbVBnbm5ab0FkT0d3TnNZblVubDQyb0JqZ3hNTTVSSQ
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 05:40:52 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi7wFBVV95cUxNMFN1X3c2VDY2QzFKWDB5RzNud0pJeGQxYUFZcnU1c3RUWG45OURHS1EtaF90WTFaNzNBd1VFMGtDU2Q3a2Q3STkxYzZtZzBvdGhZUjNiOUFjWTFEanB0MU5BVlUwQW9vMXFiRTdoWmMxc2xPQUtVV1JuYkcwSHZtd3RfOW93RGk4NjRob3JscURIdE5iMTdfWmJFQ0I3TkdrcW5ENFJlajdiNEZrRVM4ZFU5U0o3MVhIMTl1NElsb0I3NUxadjB0WDB1T1lfbUpLbVBnbm5ab0FkT0d3TnNZblVubDQyb0JqZ3hNTTVSSQ?oc=5" target="_blank">Mistral, champion français de l’IA, est-il le roi de la désinformation ?</a>&nbsp;&nbsp;<font color="#6f6f6f">Libération</font>

## 249. The AP Interview: Ukraine bets on battlefield AI as the race for weapons autonomy intensifies - WRAL
- Domain: wral.com
- URL: https://news.google.com/rss/articles/CBMixwFBVV95cUxNQmhFRGdpZ1hBTXJJdXVMSk9hcVphSVhlRm03WjVPUThJUWY2TUs0V3RfZmhnWjl3Z01CX2ZweFRsQlI2eTdVSlVFd0pKd0NSbFpBcXZNODVzVWVoYXJrZ1hGc1UzVTZfbGpmeFRSNHdYeEw2d0VkRllWN2x2d1B3OGhUOThqaWoxQUxuMWZXMXRza1d2Tmx6SnFiNHNfMEVrX2RQSkFJSm5lcFdHRVVFT1lNVTJwTjRKdTdGSkdtRGFBR3h2WHBZ
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 05:35:44 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMixwFBVV95cUxNQmhFRGdpZ1hBTXJJdXVMSk9hcVphSVhlRm03WjVPUThJUWY2TUs0V3RfZmhnWjl3Z01CX2ZweFRsQlI2eTdVSlVFd0pKd0NSbFpBcXZNODVzVWVoYXJrZ1hGc1UzVTZfbGpmeFRSNHdYeEw2d0VkRllWN2x2d1B3OGhUOThqaWoxQUxuMWZXMXRza1d2Tmx6SnFiNHNfMEVrX2RQSkFJSm5lcFdHRVVFT1lNVTJwTjRKdTdGSkdtRGFBR3h2WHBZ?oc=5" target="_blank">The AP Interview: Ukraine bets on battlefield AI as the race for weapons autonomy intensifies</a>&nbsp;&nbsp;<font color="#6f6f6f">WRAL</font>

## 250. Les ambitions de Mistral AI dans la défense, bientôt un traité Paris-Helsinki - L'Express
- Domain: lexpress.fr
- URL: https://news.google.com/rss/articles/CBMi2wFBVV95cUxQaXpIMUJlS2NOOHMwdXdLYlBlVGJKRC1YN3AtbW4zZ0EtaXdheGt5YmNST0lVMS1SS1JyS1hZZkw0bGhSNWRkTjBYM2lULUliRk9xZWp1ZXlReW93U1NtMTRuTWJYSFFaenBDVFZWNEtLRWRoYXJnOEpmZjVockFMc2lnTjQtLXRDUFJvdW1CcFRvSHVoelJMYXVMTkNjTTNSdG1GSjYzYjJTTWdqSm9FZnYwZ0VfRWpTVXJXalB3X3kyV3g1RFU4SGtGQmVyUzFzQ2tyeUVoN1FnZ0E
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 05:30:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi2wFBVV95cUxQaXpIMUJlS2NOOHMwdXdLYlBlVGJKRC1YN3AtbW4zZ0EtaXdheGt5YmNST0lVMS1SS1JyS1hZZkw0bGhSNWRkTjBYM2lULUliRk9xZWp1ZXlReW93U1NtMTRuTWJYSFFaenBDVFZWNEtLRWRoYXJnOEpmZjVockFMc2lnTjQtLXRDUFJvdW1CcFRvSHVoelJMYXVMTkNjTTNSdG1GSjYzYjJTTWdqSm9FZnYwZ0VfRWpTVXJXalB3X3kyV3g1RFU4SGtGQmVyUzFzQ2tyeUVoN1FnZ0E?oc=5" target="_blank">Les ambitions de Mistral AI dans la défense, bientôt un traité Paris-Helsinki</a>&nbsp;&nbsp;<font color="#6f6f6f">L'Express</font>

## 251. Le pape dénonce l’IA… mais ses messages auraient été écrits par IA - Numerama
- Domain: numerama.com
- URL: https://news.google.com/rss/articles/CBMiqwFBVV95cUxNVmdDMGVHMVhCV0VjR294YUdRcnhNcmlGSEVWcFVteTJVMjlyc04zYTFFWUZQdERjLUJCYXR5QVRBX3JPcWlsTGNQWEdNdzFqMHgwM3IwbmdMT05LM3J4cmRIRmlfU2I0SFhPUFBmXzFQY25IZTU0dEsyLU1wN1owbUwzQUYzVm1WY1g1b3lGQ1NyUHpKY29NR0ozZ00wcDNWOUNLMzRSeVJTTW8
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 05:15:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiqwFBVV95cUxNVmdDMGVHMVhCV0VjR294YUdRcnhNcmlGSEVWcFVteTJVMjlyc04zYTFFWUZQdERjLUJCYXR5QVRBX3JPcWlsTGNQWEdNdzFqMHgwM3IwbmdMT05LM3J4cmRIRmlfU2I0SFhPUFBmXzFQY25IZTU0dEsyLU1wN1owbUwzQUYzVm1WY1g1b3lGQ1NyUHpKY29NR0ozZ00wcDNWOUNLMzRSeVJTTW8?oc=5" target="_blank">Le pape dénonce l’IA… mais ses messages auraient été écrits par IA</a>&nbsp;&nbsp;<font color="#6f6f6f">Numerama</font>

## 252. The trust gap with AI - Healthcare Today
- Domain: healthcaretoday.com
- URL: https://news.google.com/rss/articles/CBMiaEFVX3lxTE05bndBMXlRYVNUQW83RG9tdmdubGV2c1J3Nm00N012Zlh1cm1Zdjkwak9WUkoySG8tXzlKZVp1MWpCZzFPSFFJWGlYWUJXOElacEcwY2dKVjdaLW4tVHRnbjh1UzFOZkhN
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 05:09:41 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE05bndBMXlRYVNUQW83RG9tdmdubGV2c1J3Nm00N012Zlh1cm1Zdjkwak9WUkoySG8tXzlKZVp1MWpCZzFPSFFJWGlYWUJXOElacEcwY2dKVjdaLW4tVHRnbjh1UzFOZkhN?oc=5" target="_blank">The trust gap with AI</a>&nbsp;&nbsp;<font color="#6f6f6f">Healthcare Today</font>

## 253. SAS mise sur les jumeaux numériques et l’informatique quantique pour ses 50 prochaines années - ZDNET
- Domain: zdnet.fr
- URL: https://news.google.com/rss/articles/CBMi0AFBVV95cUxOQ3FYYUtaVGZNbTRBYlIwRmVvN1h2Vkt5TjA1dE1NWFBZMkN0bGcxbDFVVUtfTm5YWml5bjNpOEpjSk1lVmNCYUIxTU9EQkp1OVFWemFxVnI0SmNJc2kzMVYybnFaM3lvazM1dDFkRFZmUUtybTgxMVR3bklhVUZWRF9OVlZSa2J0ZWZVYTJxVi15MTJPdXpRTGdlYm9zeElaMjFYb0FVN21KQlB4N2dmYVNBNl94TEdCUVBQVFMwWWNlZm5xTEZFUHYwZC11dzBR
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 05:02:41 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi0AFBVV95cUxOQ3FYYUtaVGZNbTRBYlIwRmVvN1h2Vkt5TjA1dE1NWFBZMkN0bGcxbDFVVUtfTm5YWml5bjNpOEpjSk1lVmNCYUIxTU9EQkp1OVFWemFxVnI0SmNJc2kzMVYybnFaM3lvazM1dDFkRFZmUUtybTgxMVR3bklhVUZWRF9OVlZSa2J0ZWZVYTJxVi15MTJPdXpRTGdlYm9zeElaMjFYb0FVN21KQlB4N2dmYVNBNl94TEdCUVBQVFMwWWNlZm5xTEZFUHYwZC11dzBR?oc=5" target="_blank">SAS mise sur les jumeaux numériques et l’informatique quantique pour ses 50 prochaines années</a>&nbsp;&nbsp;<font color="#6f6f6f">ZDNET</font>

## 254. Think twice: Five key rules for using AI at work - SMH.com.au
- Domain: smh.com.au
- URL: https://news.google.com/rss/articles/CBMirwFBVV95cUxNVHpOenJwb2J3akNFOHd6bDU0ZVZ2MW9uV2FITk5YTVNDbHU1RzN4U21VZ2hnOVR1aUlsQzR6QzhuWE4tUUVRWmFfY2dZcnJqX24wNlNBblRGRU85TEswd0huTkxSMW5ybnVTZmdybkVCRkVFejRvWFJibWFIeU5MSXNJQjZiQjVpUHV0cVJvamVvLXJVVHJfNlNfRzhZTUsxZkV3RkNMN1BkMExtLW9r
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 04:38:15 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMirwFBVV95cUxNVHpOenJwb2J3akNFOHd6bDU0ZVZ2MW9uV2FITk5YTVNDbHU1RzN4U21VZ2hnOVR1aUlsQzR6QzhuWE4tUUVRWmFfY2dZcnJqX24wNlNBblRGRU85TEswd0huTkxSMW5ybnVTZmdybkVCRkVFejRvWFJibWFIeU5MSXNJQjZiQjVpUHV0cVJvamVvLXJVVHJfNlNfRzhZTUsxZkV3RkNMN1BkMExtLW9r?oc=5" target="_blank">Think twice: Five key rules for using AI at work</a>&nbsp;&nbsp;<font color="#6f6f6f">SMH.com.au</font>

## 255. Got $5,000? 3 Growth Stocks Building the Physical Backbone of the AI Supercycle - The Motley Fool
- Domain: fool.com
- URL: https://news.google.com/rss/articles/CBMimAFBVV95cUxNaERMYTNTVnU2Y2pqYk9RZVAtU2NVT3o4YVV2MGU0c3RCTWwzRFNoUEpOeUtORFA4Vm1aOGg0YlVUMzI5UkphQW1mQWZqV1luVExtcDFGNm5fTHdCNk43dWVfWklMRG4zOVdiY05WRGpvcVE0M2pkekF0RGJNNk96MlRnckE4NzQ3NG92dHgtVEV1TzJNczRrWg
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 04:29:10 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMimAFBVV95cUxNaERMYTNTVnU2Y2pqYk9RZVAtU2NVT3o4YVV2MGU0c3RCTWwzRFNoUEpOeUtORFA4Vm1aOGg0YlVUMzI5UkphQW1mQWZqV1luVExtcDFGNm5fTHdCNk43dWVfWklMRG4zOVdiY05WRGpvcVE0M2pkekF0RGJNNk96MlRnckE4NzQ3NG92dHgtVEV1TzJNczRrWg?oc=5" target="_blank">Got $5,000? 3 Growth Stocks Building the Physical Backbone of the AI Supercycle</a>&nbsp;&nbsp;<font color="#6f6f6f">The Motley Fool</font>

## 256. Duke Libraries signs onto national statement of shared AI practice - The Duke Chronicle
- Domain: dukechronicle.com
- URL: https://news.google.com/rss/articles/CBMi9AFBVV95cUxPZ25Tcm5GSzlkOFkwSl94OXdSdW5iTFRzcGp2S3REdWZBb2RCT1VsWXMzSmpZSHd5UDR4Y3A2R0FHOG5QekYxaEM5ZXFOWVNCUkU4bnN2cXV5QzRnMFlJLWFjbFJEb1ZRb1NPb2F2OG96WFBMSWpJTEV1eWVNc2otVExMRTRyMHhwVFZsRXB0YkdBVjVleXk1bVRlRW4wbm1qeU52TTdkaVpUNkp1akxrbmpTN2hCMW1LODM5RE1OWEp5aFBLMVFPU3gtbm10ZjZ0eG1vbjlvcUk2QkNWMl9vQVYwVW1CRjY2c3AzR0hKTmlmVEg5
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 04:27:54 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi9AFBVV95cUxPZ25Tcm5GSzlkOFkwSl94OXdSdW5iTFRzcGp2S3REdWZBb2RCT1VsWXMzSmpZSHd5UDR4Y3A2R0FHOG5QekYxaEM5ZXFOWVNCUkU4bnN2cXV5QzRnMFlJLWFjbFJEb1ZRb1NPb2F2OG96WFBMSWpJTEV1eWVNc2otVExMRTRyMHhwVFZsRXB0YkdBVjVleXk1bVRlRW4wbm1qeU52TTdkaVpUNkp1akxrbmpTN2hCMW1LODM5RE1OWEp5aFBLMVFPU3gtbm10ZjZ0eG1vbjlvcUk2QkNWMl9vQVYwVW1CRjY2c3AzR0hKTmlmVEg5?oc=5" target="_blank">Duke Libraries signs onto national statement of shared AI practice</a>&nbsp;&nbsp;<font color="#6f6f6f">The Duke Chronicle</font>

## 257. Groundbreaking new study shows real-time AI platform better at diagnosing cancer than biopsy - UMass Chan Medical School
- Domain: umassmed.edu
- URL: https://news.google.com/rss/articles/CBMi1wFBVV95cUxNazJCTmM3NTNDeGYwYUYtYVo0bUZqZFhaT0VJb2ZMWXJ0eWtIYzVHaWdsdW1GekdYWXk0WFRfc3Zzek5VTXZXZ2FyWDcwMk80TFd4MWJTUEFqeERqNkJQZ2tEbFc3bWxMX3hNcktKU0JpWmp3clpyNnF6akFRaE1udlF4VXZJU1RjdjNHOUpIRjVEdWRySVpKY0tEVnNWNmtTeTlkYzJSYjlGcHZBUV9qN3hOYlBLa3d2UV9MbjNDaVd2dTM2OFRtTVljTncxS3V5S1p6RnUxdw
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 04:13:10 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi1wFBVV95cUxNazJCTmM3NTNDeGYwYUYtYVo0bUZqZFhaT0VJb2ZMWXJ0eWtIYzVHaWdsdW1GekdYWXk0WFRfc3Zzek5VTXZXZ2FyWDcwMk80TFd4MWJTUEFqeERqNkJQZ2tEbFc3bWxMX3hNcktKU0JpWmp3clpyNnF6akFRaE1udlF4VXZJU1RjdjNHOUpIRjVEdWRySVpKY0tEVnNWNmtTeTlkYzJSYjlGcHZBUV9qN3hOYlBLa3d2UV9MbjNDaVd2dTM2OFRtTVljTncxS3V5S1p6RnUxdw?oc=5" target="_blank">Groundbreaking new study shows real-time AI platform better at diagnosing cancer than biopsy</a>&nbsp;&nbsp;<font color="#6f6f6f">UMass Chan Medical School</font>

## 258. [Tribune] « Notre avenir face à l’IA générative est entre vos mains » : des éditeurs de presse interpellent les députés - Le Télégramme
- Domain: letelegramme.fr
- URL: https://news.google.com/rss/articles/CBMi8AFBVV95cUxQaWVwWlFST1lpRFFHR2NfN01QcjlqRU1pcC1EQnplSC1QTU5NMlNsUUNTZ3U2M1QzZjVfY1NFc3Y3dmh1MXRKQlk0WVA4cVNiVURTRFV0ZjNVREV1ZGtGQ3FsR0d0YlRmXzFudk13cEt3REt2Q2ZCcDk4SjFpQV83ay1JZ1FaQi1XcHJfOFhGVnFudHZqeS1VX3MySDBJNjBwQW81cWVVdnZMdjRxWEZrZ1c1SXVzdi1HZmI5dEVJVC11SU5helBwMllZcXBnR0oyZndZT0tJWFlxckJLN0prbFVsOVJTdXB3YVFtV180S1E
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 04:00:04 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi8AFBVV95cUxQaWVwWlFST1lpRFFHR2NfN01QcjlqRU1pcC1EQnplSC1QTU5NMlNsUUNTZ3U2M1QzZjVfY1NFc3Y3dmh1MXRKQlk0WVA4cVNiVURTRFV0ZjNVREV1ZGtGQ3FsR0d0YlRmXzFudk13cEt3REt2Q2ZCcDk4SjFpQV83ay1JZ1FaQi1XcHJfOFhGVnFudHZqeS1VX3MySDBJNjBwQW81cWVVdnZMdjRxWEZrZ1c1SXVzdi1HZmI5dEVJVC11SU5helBwMllZcXBnR0oyZndZT0tJWFlxckJLN0prbFVsOVJTdXB3YVFtV180S1E?oc=5" target="_blank">[Tribune] « Notre avenir face à l’IA générative est entre vos mains » : des éditeurs de presse interpellent les députés</a>&nbsp;&nbsp;<font color="#6f6f6f">Le Télégramme</font>

## 259. Evolvable AI: are we on the brink of the next major evolutionary transition? - The Conversation
- Domain: theconversation.com
- URL: https://news.google.com/rss/articles/CBMirgFBVV95cUxPWGNCMllLT3NMUWxaLVo3MUNhOGNPVjVZQ2VRdG9YcW1lNEtjd2R2YWhFYW15aE5qWmlLanE5WGFZU0xOSU83ZmxxVld3QmRLVzBXRTI5UTgyWGhxRnRnaF9VMG5LYW9BeTVKVEZSTWtRbWRrUnY0TG9NU3lFUndlcmNXWVg2aU5Ca2VJZmJNd2dfMkpwVzlJQWMzdXQ1dHNPNmJiX2hteG9zNGJqVmc
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 03:30:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMirgFBVV95cUxPWGNCMllLT3NMUWxaLVo3MUNhOGNPVjVZQ2VRdG9YcW1lNEtjd2R2YWhFYW15aE5qWmlLanE5WGFZU0xOSU83ZmxxVld3QmRLVzBXRTI5UTgyWGhxRnRnaF9VMG5LYW9BeTVKVEZSTWtRbWRrUnY0TG9NU3lFUndlcmNXWVg2aU5Ca2VJZmJNd2dfMkpwVzlJQWMzdXQ1dHNPNmJiX2hteG9zNGJqVmc?oc=5" target="_blank">Evolvable AI: are we on the brink of the next major evolutionary transition?</a>&nbsp;&nbsp;<font color="#6f6f6f">The Conversation</font>

## 260. Une IA américaine pour écrire les lois françaises ? Le retard préoccupant de nos institutions parlementaires - Breizh-info.com
- Domain: breizh-info.com
- URL: https://news.google.com/rss/articles/CBMi6AFBVV95cUxPZ29yVjByNTMxTXJPY1dacWZRaVVvTXduM3pmT3Q5MjR4VFduUDR1bWJJaGhHZncwbDJtM2JSX0psYnR5RGdpS0lUalVaTnJ6VWFBVTJDOWpuVVF4TkxQcjl1WDVSaDM5VmNBbHgybWdrendzQ2RfczFyUkQ4ODNxMEhZRF9ZdWg4aHpvb0VjMHFnUG9JVmJ0NWZhWHZrZWZ5b1hlaUUybFRzTExheXdlYzY2czVzT0hHLTBrdllsOHZ2emFPeVVXOEpaSTlFMWZnRHdDeXozbHRUelFRQ0pqOFk3OFU4amE2
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 02:44:52 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi6AFBVV95cUxPZ29yVjByNTMxTXJPY1dacWZRaVVvTXduM3pmT3Q5MjR4VFduUDR1bWJJaGhHZncwbDJtM2JSX0psYnR5RGdpS0lUalVaTnJ6VWFBVTJDOWpuVVF4TkxQcjl1WDVSaDM5VmNBbHgybWdrendzQ2RfczFyUkQ4ODNxMEhZRF9ZdWg4aHpvb0VjMHFnUG9JVmJ0NWZhWHZrZWZ5b1hlaUUybFRzTExheXdlYzY2czVzT0hHLTBrdllsOHZ2emFPeVVXOEpaSTlFMWZnRHdDeXozbHRUelFRQ0pqOFk3OFU4amE2?oc=5" target="_blank">Une IA américaine pour écrire les lois françaises ? Le retard préoccupant de nos institutions parlementaires</a>&nbsp;&nbsp;<font color="#6f6f6f">Breizh-info.com</font>

## 261. Maharashtra state approves AI policy with Rs 10,000cr push - Mid-day
- Domain: mid-day.com
- URL: https://news.google.com/rss/articles/CBMi4gFBVV95cUxNSDdKWDRsQmtLRmZ2eEY4RWlYNnUwZmhkRWFMREc2YnZUSDV4TDJ5YmxpTkE0SE9GN051eEFxc0ZleWtlVWkwZDZhTjIzSXVwMFFsRjdwMTRkNGZvWGtfYW5adnMwSlZNdVhyNGxXSW9Jd2xLS1ppb3hhdHJUYU5tWEJYU0ZVRFA5OHc3UG9EdXhabFc3bHBJTHhJS1E3ajFkQUJOQzZhOUJ0ZXhWM0syYzdlWFZCbmNGR25PUWxPUjNXUUFhMlc0RTNNSkFJQmd5alMwdDJXQ1k4U2lld1FPODBR0gHnAUFVX3lxTE1YS2ZnZC0wQWxmU2JkcGxCcHBDTUNjbEFjUGNFSEdzMG81MmlLOHhwY096NDVWaVlXM3lmZ1NGYjFMS2sxRVE4UmJFQVlSMm5IMjJWU0ZKV3hjakpZZ3JDN0FpZ0wxZzN3WUt4RG5QdFZyMTFvWGRVa2dmY0VBUzdBS1duY2ZnM1I0aXkwbjZ2RFhJajA0Tm5uTC1nOGxBR1RqcW1sQW5hWHVGVFNTV0RUa2VmX196bWFYMHRWbHdHOGt3WnZRcWRRYUQyLVhPbWhuVEZSM05OS1VHQUlpNWE4MjRvLTNWdw
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 02:38:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMi4gFBVV95cUxNSDdKWDRsQmtLRmZ2eEY4RWlYNnUwZmhkRWFMREc2YnZUSDV4TDJ5YmxpTkE0SE9GN051eEFxc0ZleWtlVWkwZDZhTjIzSXVwMFFsRjdwMTRkNGZvWGtfYW5adnMwSlZNdVhyNGxXSW9Jd2xLS1ppb3hhdHJUYU5tWEJYU0ZVRFA5OHc3UG9EdXhabFc3bHBJTHhJS1E3ajFkQUJOQzZhOUJ0ZXhWM0syYzdlWFZCbmNGR25PUWxPUjNXUUFhMlc0RTNNSkFJQmd5alMwdDJXQ1k4U2lld1FPODBR0gHnAUFVX3lxTE1YS2ZnZC0wQWxmU2JkcGxCcHBDTUNjbEFjUGNFSEdzMG81MmlLOHhwY096NDVWaVlXM3lmZ1NGYjFMS2sxRVE4UmJFQVlSMm5IMjJWU0ZKV3hjakpZZ3JDN0FpZ0wxZzN3WUt4RG5QdFZyMTFvWGRVa2dmY0VBUzdBS1duY2ZnM1I0aXkwbjZ2RFhJajA0Tm5uTC1nOGxBR1RqcW1sQW5hWHVGVFNTV0RUa2VmX196bWFYMHRWbHdHOGt3WnZRcWRRYUQyLVhPbWhuVEZSM05OS1VHQUlpNWE4MjRvLTNWdw?oc=5" target="_blank">Maharashtra state approves AI policy with Rs 10,000cr push</a>&nbsp;&nbsp;<font color="#6f6f6f">Mid-day</font>

## 262. IA générative et SEO : attention au mirage de la facilité ! - Fredzone
- Domain: fredzone.org
- URL: https://news.google.com/rss/articles/CBMiiAFBVV95cUxPUHp6OS04T3U0X2lJZzBPSGhuYzNGWHIwNE1GVk50OGNuUjhIY05GZDlqLXlGRzlJRHpKekZXUUdyb29KSUVzWkZsb0ZfUWZLRlFRd1d1RjdTUW9SZmtFXzg1aDJaLUNDZUdVOXlxbU1fUnRMWUJ5N192bE1iR21ZVk44ekZKT19I
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 02:33:33 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiiAFBVV95cUxPUHp6OS04T3U0X2lJZzBPSGhuYzNGWHIwNE1GVk50OGNuUjhIY05GZDlqLXlGRzlJRHpKekZXUUdyb29KSUVzWkZsb0ZfUWZLRlFRd1d1RjdTUW9SZmtFXzg1aDJaLUNDZUdVOXlxbU1fUnRMWUJ5N192bE1iR21ZVk44ekZKT19I?oc=5" target="_blank">IA générative et SEO : attention au mirage de la facilité !</a>&nbsp;&nbsp;<font color="#6f6f6f">Fredzone</font>

## 263. Alphabet's first-quarter profit soars as Google's big AI bets help push stock to new highs , Money News - AsiaOne
- Domain: asiaone.com
- URL: https://news.google.com/rss/articles/CBMisgFBVV95cUxOeEMwck1rbUlScUVEbVMxU1ZpMnVsZTJPQ0NhU2RkMFhlVGVlcWxPbW56ZkRaS2V3dmo2a25haWVZbnl4THpKd0ltQU0xWXdLUS0ycXRiUlVOaXkzTWg0M3JjT2xsRmN5S2tqNFZQMmx0YllXOTVqSG9hd1pzbkJTUUU1ZDBCbHFodEt6S0dTb3BheFB1Zy1Pc3ljdXI2a0VnSlZmcmgwTVBleGp5WnZkSkJ3
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 02:32:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMisgFBVV95cUxOeEMwck1rbUlScUVEbVMxU1ZpMnVsZTJPQ0NhU2RkMFhlVGVlcWxPbW56ZkRaS2V3dmo2a25haWVZbnl4THpKd0ltQU0xWXdLUS0ycXRiUlVOaXkzTWg0M3JjT2xsRmN5S2tqNFZQMmx0YllXOTVqSG9hd1pzbkJTUUU1ZDBCbHFodEt6S0dTb3BheFB1Zy1Pc3ljdXI2a0VnSlZmcmgwTVBleGp5WnZkSkJ3?oc=5" target="_blank">Alphabet's first-quarter profit soars as Google's big AI bets help push stock to new highs , Money News</a>&nbsp;&nbsp;<font color="#6f6f6f">AsiaOne</font>

## 264. 5 reasons AI should never spell ‘game over’ for physicians - HealthExec
- Domain: healthexec.com
- URL: https://news.google.com/rss/articles/CBMiqgFBVV95cUxPX0ZUTERIeEVycHJPZDlTVHJja0J4TXFKaVBWdGkwcVJGYXl1akl6R0dVUTlueW9QQ2l1Um12YUJVVWpmQlcyVWktUmxVekNiWmxkb0czYURpU2hranZRVVZWbWJQTkNkZF9jWnN4M2x2bEhrV0lqQ0tGSEttdTB4ZzJEb3NBTktISUNEZUw4Zjd6WlBFdE9zS25aTUdLNko3enlYZkY3dGplZw
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 02:25:17 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiqgFBVV95cUxPX0ZUTERIeEVycHJPZDlTVHJja0J4TXFKaVBWdGkwcVJGYXl1akl6R0dVUTlueW9QQ2l1Um12YUJVVWpmQlcyVWktUmxVekNiWmxkb0czYURpU2hranZRVVZWbWJQTkNkZF9jWnN4M2x2bEhrV0lqQ0tGSEttdTB4ZzJEb3NBTktISUNEZUw4Zjd6WlBFdE9zS25aTUdLNko3enlYZkY3dGplZw?oc=5" target="_blank">5 reasons AI should never spell ‘game over’ for physicians</a>&nbsp;&nbsp;<font color="#6f6f6f">HealthExec</font>

## 265. Which Pothole To Fix? AI Team Helps Company Develop City System - The University of Texas at Dallas
- Domain: news.utdallas.edu
- URL: https://news.google.com/rss/articles/CBMifkFVX3lxTE5MdmVmY1pqSXRLRGRkNm9NcGUzZGRPX1ZtVE14WUFhWWZzTDNxaW1qNlE1ekFiSzJoOE9XcDZXUi1sX1lUYlBHN01LTU9PRWFvZDMzZXo4aHJ0TXk2ZS13WUd3cHJfQlBvQ0hFMkllY0JTMmFwaVUtYVdpaHNSdw
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 01:05:39 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMifkFVX3lxTE5MdmVmY1pqSXRLRGRkNm9NcGUzZGRPX1ZtVE14WUFhWWZzTDNxaW1qNlE1ekFiSzJoOE9XcDZXUi1sX1lUYlBHN01LTU9PRWFvZDMzZXo4aHJ0TXk2ZS13WUd3cHJfQlBvQ0hFMkllY0JTMmFwaVUtYVdpaHNSdw?oc=5" target="_blank">Which Pothole To Fix? AI Team Helps Company Develop City System</a>&nbsp;&nbsp;<font color="#6f6f6f">The University of Texas at Dallas</font>

## 266. Inside India newsletter: AI is exposing cracks in India’s growth story as it hits high-paying IT jobs - CNBC
- Domain: cnbc.com
- URL: https://news.google.com/rss/articles/CBMie0FVX3lxTE5manZRUExDaC1LQ2RZMWRSU1F1SldjN2VscEk3UTRNM2JKOVVCVThwYTB6S0NxdjJRVDNGT3JxV1VzZVF4VnlnaW1KY2JrdUJPbkxhTVZXN1NrODNQeUdablcyN1lJQjFNS0lmM1FvTnNST3oxdzMyT0QyZ9IBgAFBVV95cUxOU254NzlhRkRYLXBFOTJHbFVYNmRVNkpDM3BPQzc3bDdmZkZBNHdRcFZFWWQzanRwR3U5UmJyZnNfMjNWY3RyT2ZFS1BLbW5BRDhRRnNDNVBxcFJMSDdoTm16SDlYdlpOMFo2NHp0US1EN1JZS3N1NXR6b3hZbjZsMg
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 00:53:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMie0FVX3lxTE5manZRUExDaC1LQ2RZMWRSU1F1SldjN2VscEk3UTRNM2JKOVVCVThwYTB6S0NxdjJRVDNGT3JxV1VzZVF4VnlnaW1KY2JrdUJPbkxhTVZXN1NrODNQeUdablcyN1lJQjFNS0lmM1FvTnNST3oxdzMyT0QyZ9IBgAFBVV95cUxOU254NzlhRkRYLXBFOTJHbFVYNmRVNkpDM3BPQzc3bDdmZkZBNHdRcFZFWWQzanRwR3U5UmJyZnNfMjNWY3RyT2ZFS1BLbW5BRDhRRnNDNVBxcFJMSDdoTm16SDlYdlpOMFo2NHp0US1EN1JZS3N1NXR6b3hZbjZsMg?oc=5" target="_blank">Inside India newsletter: AI is exposing cracks in India’s growth story as it hits high-paying IT jobs</a>&nbsp;&nbsp;<font color="#6f6f6f">CNBC</font>

## 267. Meta shares fall on concerns over AI spending, legal scrutiny - CNA
- Domain: channelnewsasia.com
- URL: https://news.google.com/rss/articles/CBMiqgFBVV95cUxNdmMweWtncUhfVGZPNEFKTWFSU0xXMldTdTBwM0tscTJ0WW55TWJWQkVWdTVENUlRbmxpZXViQWhSZkVTRlhGSU5tWGR4RG1TM0J0OHBLSVUtd1hVTWppUFBzd085ejRDRHhsZklzSlNaR3JxSnJIOGJyaTFuWVdqWHZydzVaeGhhczVmYURZazJranFtWFZXUFhpWXZodVJ1OGs3a21IMno0dw
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 00:39:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiqgFBVV95cUxNdmMweWtncUhfVGZPNEFKTWFSU0xXMldTdTBwM0tscTJ0WW55TWJWQkVWdTVENUlRbmxpZXViQWhSZkVTRlhGSU5tWGR4RG1TM0J0OHBLSVUtd1hVTWppUFBzd085ejRDRHhsZklzSlNaR3JxSnJIOGJyaTFuWVdqWHZydzVaeGhhczVmYURZazJranFtWFZXUFhpWXZodVJ1OGs3a21IMno0dw?oc=5" target="_blank">Meta shares fall on concerns over AI spending, legal scrutiny</a>&nbsp;&nbsp;<font color="#6f6f6f">CNA</font>

## 268. Australian banks warned frontier AI could create larger, faster cyber attacks - CNA
- Domain: channelnewsasia.com
- URL: https://news.google.com/rss/articles/CBMiwwFBVV95cUxPbGlLaHRxc3ZNUDl1c2xDeURCVk5aYy1kSzBvUVo1OVlpa0xtQ3pxWjlhc1RNYlZzQzQtSEtvUzkzV2lqNzVpWmx6VGJMU20zRXhpWkdMVDBxVXRKWGFSb1pUdHQxcm5vTGpxZEx1Z0IwTlBpSWVjdkFmaVZ6SzY0eUZ5N1l2emtONE5rZjlCaGR0Y3M5d3llQkVRajR2U0ZVcm10Q3dKSlhlVWV2YTdHV0ZYNExDS2ZkdVg1Vm9tZTlFeWM
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 00:09:46 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMiwwFBVV95cUxPbGlLaHRxc3ZNUDl1c2xDeURCVk5aYy1kSzBvUVo1OVlpa0xtQ3pxWjlhc1RNYlZzQzQtSEtvUzkzV2lqNzVpWmx6VGJMU20zRXhpWkdMVDBxVXRKWGFSb1pUdHQxcm5vTGpxZEx1Z0IwTlBpSWVjdkFmaVZ6SzY0eUZ5N1l2emtONE5rZjlCaGR0Y3M5d3llQkVRajR2U0ZVcm10Q3dKSlhlVWV2YTdHV0ZYNExDS2ZkdVg1Vm9tZTlFeWM?oc=5" target="_blank">Australian banks warned frontier AI could create larger, faster cyber attacks</a>&nbsp;&nbsp;<font color="#6f6f6f">CNA</font>

## 269. Australian banks warned frontier AI could create larger, faster cyber attacks - Reuters
- Domain: reuters.com
- URL: https://news.google.com/rss/articles/CBMirwFBVV95cUxPd0JkN2c0bTFHdFpYY0VGaVdYa3ZucWI1bmw4aV9hV29QeHk4UzRCU0VjT2tzUUJrTk11U2lkVExNSUl2Zmc5RXc5c19mbWwzS2ozVzg1eGpiZzY5OHBlS3Z1c0VPaC1hbUJSYVZRcjlIOFZIblhWQ2J5NTRuY180WUVkNDctaDc5bGRYMU5UZmhLQWFyYnJka2s5cU94cHVpaGdQbGJKN01kazZRZHJr
- Relevance score: 4.0
- Published: Thu, 30 Apr 2026 00:09:00 GMT
- Summary: <a href="https://news.google.com/rss/articles/CBMirwFBVV95cUxPd0JkN2c0bTFHdFpYY0VGaVdYa3ZucWI1bmw4aV9hV29QeHk4UzRCU0VjT2tzUUJrTk11U2lkVExNSUl2Zmc5RXc5c19mbWwzS2ozVzg1eGpiZzY5OHBlS3Z1c0VPaC1hbUJSYVZRcjlIOFZIblhWQ2J5NTRuY180WUVkNDctaDc5bGRYMU5UZmhLQWFyYnJka2s5cU94cHVpaGdQbGJKN01kazZRZHJr?oc=5" target="_blank">Australian banks warned frontier AI could create larger, faster cyber attacks</a>&nbsp;&nbsp;<font color="#6f6f6f">Reuters</font>

## 270. AI's Economics Don't Make Sense
- Domain: wheresyoured.at
- URL: https://www.wheresyoured.at/ais-economics-dont-make-sense/
- Relevance score: 4.0
- Published: 2026-04-28T16:39:53Z
- Summary: If you liked this piece, please subscribe to my premium newsletter. It’s $70 a year, or $7 a month, and in return you get a weekly newsletter that’s usually anywhere from 5,000 to 18,000 words, including vast, detailed analyses of NVIDIA, Anthropic and OpenAI…

## 271. Tumbler Ridge families are suing OpenAI
- Domain: theverge.com
- URL: https://www.theverge.com/ai-artificial-intelligence/920479/tumbler-ridge-chagpt-openai-lawsuit
- Relevance score: 3.8
- Published: 2026-04-29T10:47:57-04:00
- Summary: Seven families of victims injured or killed in the Tumbler Ridge school shooting in Canada have filed lawsuits against OpenAI and CEO Sam Altman, accusing the company and its leadership of negligence after they failed to alert police to the suspected shooter's ChatGPT activity. The families allege OpenAI stayed silent after its systems flagged activity [&#8230;]

## 272. 5 ways your Windows updates are about to get a lot less painful
- Domain: zdnet.com
- URL: https://www.zdnet.com/article/your-windows-update-experience-is-about-to-get-less-painful/
- Relevance score: 3.7
- Published: Wed, 29 Apr 2026 12:09:04 GMT
- Summary: Microsoft wants to fix 'pain points' in Windows 11 PCs. The first batch of changes, targeting the Windows Update experience, is hitting Insider preview channels and coming soon to your desktop.

## 273. Extracting contract insights with PwC’s AI-driven annotation on AWS
- Domain: aws.amazon.com
- URL: https://aws.amazon.com/blogs/machine-learning/extracting-contract-insights-with-pwcs-ai-driven-annotation-on-aws/
- Relevance score: 3.5
- Published: Wed, 29 Apr 2026 21:19:39 +0000
- Summary: This post was co-written with Yash Munsadwala, Adam Hood, Justin Guse, and Hector Hernandez from PwC. Contract analysis often consumes significant time for legal, compliance, and procurement teams, especially when important insights are buried in lengthy, unstructured agreements. As contract volumes grow, finding specific clauses and assessing extracted terms can become increasingly difficult to scale. […]

## 274. Amazon’s cloud business is surging — and so is its capital spending
- Domain: techcrunch.com
- URL: https://techcrunch.com/2026/04/29/amazons-cloud-business-is-surging-and-so-is-its-capital-spending/
- Relevance score: 3.5
- Published: Thu, 30 Apr 2026 00:14:23 +0000
- Summary: The e-commerce giant is making more money than expected from AWS but it's also spending a lot, and will continue to do so in the near term, its chief executive said.

## 275. Bloomberg, the OG of financial data firms, has a potent new AI agent. How it built it holds lessons for other companies
- Domain: fortune.com
- URL: https://fortune.com/2026/04/28/bloomberg-askb-ai-agents-lessons-from-bloomberg-cto-shawn-edwards-eye-on-ai/
- Relevance score: 3.5
- Published: 2026-04-28T21:15:57Z
- Summary: Bloomberg's "AskB" tool shows the potential of AI agents in finance. It also shows how difficult such agents are to build.

## 276. Motorola Razr Ultra (2026) vs. Samsung Galaxy Z Flip 7: I tried both, and there's a clear winner
- Domain: zdnet.com
- URL: https://www.zdnet.com/article/samsung-galaxy-z-flip-7-vs-motorola-razr-ultra-2026/
- Relevance score: 3.2
- Published: Wed, 29 Apr 2026 19:15:42 GMT
- Summary: Samsung focuses on durability and AI, while the new Motorola phone is all about the hardware. Here's which one I think is better.

## 277. Building AI-ready data: Vanguard’s Virtual Analyst journey
- Domain: aws.amazon.com
- URL: https://aws.amazon.com/blogs/machine-learning/building-ai-ready-data-vanguards-virtual-analyst-journey/
- Relevance score: 3.0
- Published: Wed, 29 Apr 2026 11:56:33 +0000
- Summary: In this post, you'll learn how Vanguard built their Virtual Analyst solution by focusing on eight guiding principles of AI-ready data, the AWS services that powered their implementation, and the measurable business outcomes they achieved.

## 278. How AI Could Help Combat Antibiotic Resistance
- Domain: wired.com
- URL: https://www.wired.com/story/wired-health-2026-tackling-antimicrobial-resistance-ara-darzi/
- Relevance score: 2.8
- Published: Wed, 29 Apr 2026 09:00:00 +0000
- Summary: At WIRED Health, British surgeon Ara Darzi said AI is set to transform the diagnosis and treatment of drug-resistant infections. But a lack of incentives means innovation may not reach patients.

## 279. Why friendly AI chatbots might be less trustworthy
- Domain: bbc.com
- URL: https://www.bbc.com/news/articles/cd9pdjgvxj8o
- Relevance score: 2.5
- Published: Wed, 29 Apr 2026 15:00:06 GMT
- Summary: Researchers found adjusting AI systems to be more warm and friendly to users would result in an "accuracy trade-off".

## 280. ‘The cost of compute is far beyond the costs of the employees’: Nvidia executive says right now AI is more expensive than paying human workers
- Domain: fortune.com
- URL: https://fortune.com/2026/04/28/nvidia-executive-cost-of-ai-is-greater-than-cost-of-employees/
- Relevance score: 2.5
- Published: 2026-04-28T07:11:00Z
- Summary: Big Tech has announced $740 billion in capex this year, but AI has yet to show evidence of widespread increased productivity.

## 281. Is Facebook adding Gen Z phrases to your shared posts? You're not alone, bestie. Here's what's happening.
- Domain: zdnet.com
- URL: https://www.zdnet.com/article/facebook-glitch-gen-z-phrases-text-shared-posts-ai/
- Relevance score: 2.2
- Published: Wed, 29 Apr 2026 16:03:00 GMT
- Summary: For the past two weeks, Facebook users are getting unexpected slang on posts. AI is probably to blame.

## 282. Privacy in the AI era is possible, says Proton's CEO, but one thing keeps him up at night
- Domain: zdnet.com
- URL: https://www.zdnet.com/article/proton-ceo-andy-yen-interview-ai-privacy-security-semafor/
- Relevance score: 2.2
- Published: Thu, 30 Apr 2026 02:00:35 GMT
- Summary: At Semafor World Economy, I spoke with Andy Yen about mass surveillance, protecting children, local AI, and the one thing Proton can't save users from.
