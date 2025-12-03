# Awesome-Diffusion-LLM

This repository (Daily updating) provides a curated list of papers on Diffusion Large Language Models (dLLMs), a rapidly emerging field in generative AI. The collection is organized to track advancements from foundational theory to state-of-the-art applications.

The field is evolving quickly, and this list is a living document. **We welcome community contributions.** If you know of a relevant paper we've missed, please feel free to **submit a pull request**.

---

- [Theoretical Basis](#theoretical-basis)
- [Foundation Model](#foundation-model)
- [Inference Method](#inference-method)
- [Training Method](#training-method)
- [Multimodal Model](#multimodal-model)
- [Variable Length](#variable-length)
- [Others](#others)

## 1 Theoretical Basis <a id="theoretical-basis"></a>
| Date       | Title                                                                 | Abstract | Link                                                                                                                                              | Remark       |
|------------|-----------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| 2025-02-13 | Theoretical Benefit and Limitation of Diffusion Language Model       | -        | [Paper](https://arxiv.org/abs/2502.09622)                                                                                                         | NeurIPS 2025 |
| 2015-03-12 | Deep Unsupervised Learning using Nonequilibrium Thermodynamics        | -        | [Paper](https://arxiv.org/abs/1503.03585)                                                                                                         | -            |
| 2021-07-07 | Structured Denoising Diffusion Models in Discrete State-Spaces        | -        | [Paper](https://arxiv.org/abs/2107.03006)                                                                                                         | -            |
| 2023-10-25 | Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution | - | [Paper](https://arxiv.org/abs/2310.16834)                                                                                                         | -            |
| 2024-06-06 | Your Absorbing Discrete Diffusion Secretly Models the Conditional Distributions of Clean Data | - | [Paper](https://arxiv.org/abs/2406.03736)                                                                                                         | -            |
| 2024-06-06 | Simplified and Generalized Masked Diffusion for Discrete Data         | -        | [Paper](https://arxiv.org/abs/2406.04329)                                                                                                         | -            |
| 2024-06-11 | Simple and Effective Masked Diffusion Language Models                 | -        | [Paper](https://arxiv.org/abs/2406.07524)                                                                                                         | -            |
| 2025-09-19 | Breaking AR’s Sampling Bottleneck: Provable Acceleration via Diffusion Language Models | - | [Paper](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=ynnb3QcAAAAJ&sortby=pubdate&citation_for_view=ynnb3QcAAAAJ:mVmsd5A6BfQC) | NeurIPS 2025 |
| 2025-10-13 | Next Semantic Scale Prediction via Hierarchical Diffusion Language Models | -     | [Paper](https://arxiv.org/abs/2510.08632)                                                                                                         | NeurIPS 2025 |
| 2025-10-29 | Error Bounds and Optimal Schedules for Masked Diffusions with Factorized Approximations | - | [Paper](https://www.arxiv.org/abs/2510.25544)                                                                                                     | -            |


## 2 Foundation Model <a id="foundation-model"></a>

| Date       | Title                                                                 | Abstract | Link                                                                                                                                              | Remark       |
|------------|-----------------------------------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| 2025-02-13 | Theoretical Benefit and Limitation of Diffusion Language Model       | -        | [Paper](https://arxiv.org/abs/2502.09622)                                                                                                         | NeurIPS 2025 |
| 2015-03-12 | Deep Unsupervised Learning using Nonequilibrium Thermodynamics        | -        | [Paper](https://arxiv.org/abs/1503.03585)                                                                                                         | -            |
| 2021-07-07 | Structured Denoising Diffusion Models in Discrete State-Spaces        | -        | [Paper](https://arxiv.org/abs/2107.03006)                                                                                                         | -            |
| 2023-10-25 | Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution | - | [Paper](https://arxiv.org/abs/2310.16834)                                                                                                         | -            |
| 2024-06-06 | Your Absorbing Discrete Diffusion Secretly Models the Conditional Distributions of Clean Data | - | [Paper](https://arxiv.org/abs/2406.03736)                                                                                                         | -            |
| 2024-06-06 | Simplified and Generalized Masked Diffusion for Discrete Data         | -        | [Paper](https://arxiv.org/abs/2406.04329)                                                                                                         | -            |
| 2024-06-11 | Simple and Effective Masked Diffusion Language Models                 | -        | [Paper](https://arxiv.org/abs/2406.07524)                                                                                                         | -            |
| 2025-09-19 | Breaking AR’s Sampling Bottleneck: Provable Acceleration via Diffusion Language Models | - | [Paper](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=ynnb3QcAAAAJ&sortby=pubdate&citation_for_view=ynnb3QcAAAAJ:mVmsd5A6BfQC) | NeurIPS 2025 |
| 2025-10-13 | Next Semantic Scale Prediction via Hierarchical Diffusion Language Models | -     | [Paper](https://arxiv.org/abs/2510.08632)                                                                                                         | NeurIPS 2025 |
| 2025-10-29 | Error Bounds and Optimal Schedules for Masked Diffusions with Factorized Approximations | - | [Paper](https://www.arxiv.org/abs/2510.25544)                                                                                                     | -            |


### 2.1 New model structure

| Date       | Title                                                                 | Abstract | Link                                      | Remark |
|------------|-----------------------------------------------------------------------|----------|-------------------------------------------|--------|
| 2025-11-23 | Breaking the Bottleneck with DiffuApriel: High-Throughput Diffusion LMs with Mamba Backbone | - | [Paper](https://arxiv.org/abs/2511.15927) | -      |




### 2.2 Continuous DLM

| Date       | Title                                                                 | Abstract | Link                                      | Remark |
|------------|-----------------------------------------------------------------------|----------|-------------------------------------------|--------|
| 2022-05-27 | Diffusion-LM Improves Controllable Text Generation                    | -        | [Paper](https://arxiv.org/abs/2205.14217) | -      |
| 2025-05-30 | DLM-One: Diffusion Language Models for One-Step Sequence Generation   | -        | [Paper](https://arxiv.org/abs/2506.00290) | -      |
| 2025-10-03 | Coevolutionary Continuous Discrete Diffusion: Make Your Diffusion Language Model a Latent Reasoner | - | [Paper](https://arxiv.org/abs/2510.03206) | -      |



### 2.3 Autoregressive vs. Diffusion LLMs
| Date       | Title                                                                 | Abstract | Link                                      | Remark |
|------------|-----------------------------------------------------------------------|----------|-------------------------------------------|--------|
| 2025-10-10 | Closing the Data-Efficiency Gap Between Autoregressive and Masked Diffusion LLMs | - | [Paper](https://arxiv.org/abs/2510.09885) | -      |



## 3. Inference Method <a id="inference-method"></a>

| Date       | Title                                                                 | Abstract | Link                                      | Remark |
|------------|-----------------------------------------------------------------------|----------|-------------------------------------------|--------|
| 2025-10-17 | Planner and Executor: Collaboration between Discrete Diffusion And Autoregressive Models in Reasoning | - | [Paper](https://arxiv.org/abs/2510.15244) | -      |
| 2025-10-31 | Diffuse Thinking: Exploring Diffusion Language Models as Efficient Thought Proposers for Reasoning | - | [Paper](https://arxiv.org/abs/2510.27469) | -      |
| 2025-11-04 | Effective Test-Time Scaling of Discrete Diffusion through Iterative Refinement | - | [Paper](https://arxiv.org/abs/2511.05562) | -      |
| 2025-11-04 | Lookahead Unmasking Elicits Accurate Decoding in Diffusion Language Models | - | [Paper](https://arxiv.org/abs/2511.05563) | -      |
| 2025-11-12 | TiDAR: Think in Diffusion, Talk in Autoregression                     | -        | [Paper](https://arxiv.org/abs/2511.08923) | -      |


### 3.1 Enable KV Cache
| Date       | Title                                                                 | Abstract | Link                                                                                      | Remark       |
|------------|-----------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------|--------------|
| 2025-05-21 | dKV-Cache: The Cache for Diffusion Language Models                    | -        | [Paper](https://arxiv.org/abs/2505.15781)                                                | NeurIPS 2025 |
| 2025-05-22 | dLLM-Cache: Accelerating Diffusion Large Language Models with Adaptive Caching | - | [GitHub](https://github.com/maomaocun/dLLM-cache?tab=readme-ov-file)                     | -            |
| 2025-05-27 | Accelerating Diffusion Language Model Inference via Efficient KV Caching and Guided Diffusion | - | [PDF](https://arxiv.org/pdf/2505.21467)                                                  | -            |
| 2025-05-28 | Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding | - | [PDF](https://nvlabs.github.io/Fast-dLLM/paper/fast_dllm.pdf)                            | -            |
| 2025-06-02 | Esoteric Language Models                                              | -        | [Paper](https://arxiv.org/abs/2506.01928)                                                | -            |
| 2025-08-04 | Sparse-dLLM: Accelerating Diffusion LLMs with Dynamic Cache Eviction  | -        | [Paper](https://arxiv.org/abs/2508.02558)                                                | -            |
| 2025-08-19 | DPad: Efficient Diffusion Language Models with Suffix Dropout         | -        | [Paper](https://arxiv.org/abs/2508.14148)                                                | -            |
| 2025-10-13 | dInfer: An Efficient Inference Framework for Diffusion Language Models | -       | [Paper](https://arxiv.org/abs/2510.08666)                                                | -            |
| 2025-10-16 | Attention Is All You Need for KV Cache in Diffusion LLMs             | -        | [Paper](https://arxiv.org/abs/2510.14973)                                                | -            |
| 2025-11-24 | Orchestrating Dual-Boundaries: An Arithmetic Intensity Inspired Acceleration Framework for Diffusion Language Models | - | [Paper](https://arxiv.org/abs/2511.21759) | -            |



### 3.2 Advanced Sampling Method

| Date       | Title                                                                 | Abstract | Link                                                                                      | Remark |
|------------|-----------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------|--------|
| 2025-05-22 | Remasking Discrete Diffusion Models with Inference-Time Scaling       | -        | [Paper](https://arxiv.org/abs/2503.00307)                                                | -      |
| 2025-05-22 | Dimple: Discrete Diffusion Multimodal Large Language Model with Parallel Decoding | - | [Paper](https://arxiv.org/abs/2505.16990)                                                | -      |
| 2025-05-23 | Variational Autoencoding Discrete Diffusion with Enhanced Dimensional Correlations Modeling | - | [Paper](https://arxiv.org/abs/2505.17384)                                                | -      |
| 2025-05-27 | Accelerating Diffusion Language Model Inference via Efficient KV Caching and Guided Diffusion | - | [PDF](https://arxiv.org/pdf/2505.21467)                                                  | -      |
| 2025-05-28 | Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding | - | [PDF](https://nvlabs.github.io/Fast-dLLM/paper/fast_dllm.pdf)                            | -      |
| 2025-05-30 | Accelerated Sampling from Masked Diffusion Models via Entropy Bounded Unmasking | - | [Paper](https://arxiv.org/abs/2505.24857)                                                | -      |
| 2025-05-31 | Accelerating Diffusion LLMs via Adaptive Parallel Decoding            | -        | [Paper](https://arxiv.org/abs/2506.00413)                                                | -      |
| 2025-06-12 | Accelerating Diffusion Large Language Models with SlowFast Sampling: The Three Golden Principles | - | [Paper](https://arxiv.org/abs/2506.10848)                                                | -      |
| 2025-07-24 | Wide-In, Narrow-Out: Revokable Decoding for Efficient and Effective DLLMs | -     | [Paper](https://arxiv.org/abs/2507.18578)                                                | -      |
| 2025-08-19 | DPad: Efficient Diffusion Language Models with Suffix Dropout         | -        | [Paper](https://arxiv.org/abs/2508.14148)                                                | -      |
| 2025-10-13 | Mask Tokens as Prophet: Fine-Grained Cache Eviction for Efficient dLLM Inference | - | [Paper](https://arxiv.org/abs/2510.09309)                                                | -      |
| 2025-10-09 | Guided Star-Shaped Masked Diffusion                                   | -        | [Paper](https://arxiv.org/abs/2510.08369)                                                | -      |
| 2025-10-16 | Efficient Parallel Samplers for Recurrent-Depth Models and Their Connection to Diffusion Language Models | - | [Paper](https://arxiv.org/abs/2510.14961) | -      |
| 2025-10-21 | Planned Diffusion                                                     | -        | [Paper](https://arxiv.org/abs/2510.18087)                                                | -      |
| 2025-10-21 | How Efficient Are Diffusion Language Models? A Critical Examination of Efficiency Evaluation Practices | - | [Paper](https://arxiv.org/abs/2510.18480)                                                | -      |
| 2025-10-20 | Saber: An Efficient Sampling with Adaptive Acceleration and Backtracking Enhanced Remasking for Diffusion Language Model | - | [Paper](https://arxiv.org/abs/2510.18165)                                                | -      |
| 2025-11-03 | Beyond Static Cutoffs: One-Shot Dynamic Thresholding for Diffusion Language Models | - | [Paper](https://arxiv.org/abs/2511.02077)                                                | -      |
| 2025-11-07 | KLASS: KL-Guided Fast Inference in Masked Diffusion Models            | -        | [Paper](https://arxiv.org/abs/2511.05664)                                                | -      |
| 2025-11-26 | From Bits to Rounds: Parallel Decoding with Exploration for Diffusion Language Models | - | [Paper](https://arxiv.org/abs/2511.21103)                                                | -      |


## 4 Training Method <a id="training-method"></a>
| Date       | Title                                                                 | Abstract | Link                                      | Remark       |
|------------|-----------------------------------------------------------------------|----------|-------------------------------------------|--------------|
| 2025-04-16 | d1: Scaling Reasoning in Diffusion Large Language Models via Reinforcement Learning | - | [Paper](https://arxiv.org/abs/2504.12216) | -            |
| 2025-05-15 | Reinforcing the Diffusion Chain of Lateral Thought with Diffusion Language Models | - | [Paper](https://arxiv.org/abs/2505.10446) | NeurIPS 2025 |
| 2025-05-24 | Anchored Diffusion Language Model                                     | -        | [Paper](https://arxiv.org/abs/2505.18456) | NeurIPS 2025 |
| 2025-05-25 | LLaDA 1.5: Variance-Reduced Preference Optimization for Large Language Diffusion Models | - | [Paper](https://arxiv.org/abs/2505.19223) | -            |
| 2025-07-07 | wd1: Weighted Policy Optimization for Reasoning in Diffusion Language Models | - | [Paper](https://arxiv.org/abs/2507.08838) | -            |
| 2025-07-25 | DiffuCoder: Understanding and Improving Masked Diffusion Models for Code Generation | - | [Paper](https://arxiv.org/abs/2506.20639) | -            |
| 2025-08-18 | MDPO: Overcoming the Training-Inference Divide of Masked Diffusion Language Models | - | [PDF](https://arxiv.org/pdf/2508.13148)   | -            |
| 2025-09-08 | Revolutionizing Reinforcement Learning Framework for Diffusion Large Language Models | - | [PDF](https://arxiv.org/pdf/2509.06949)   | -            |
| 2025-09-12 | Inpainting-Guided Policy Optimization for Diffusion Large Language Models | - | [PDF](https://arxiv.org/pdf/2509.10396)   | -            |
| 2025-09-28 | d2: Improved Techniques for Training Reasoning Diffusion Language Models | - | [Paper](https://arxiv.org/abs/2509.21474) | -            |
| 2025-10-09 | Improving Reasoning for Diffusion Language Models via Group Diffusion Policy Optimization | - | [Paper](https://arxiv.org/abs/2510.08554) | -            |
| 2025-10-13 | SPG: Sandwiched Policy Gradient for Masked Diffusion Language Models  | -        | [Paper](https://arxiv.org/abs/2510.09541) | -            |
| 2025-10-14 | Boundary-Guided Policy Optimization for Memory-efficient RL of Diffusion Large Language Models | - | [Paper](https://arxiv.org/abs/2510.11683) | -            |
| 2025-10-23 | Blockwise SFT for Diffusion Language Models: Reconciling Bidirectional Attention and Autoregressive Decoding | - | [Paper](https://arxiv.org/abs/2508.19529) | -            |
| 2025-10-24 | MRO: Enhancing Reasoning in Diffusion Language Models via Multi-Reward Optimization | - | [Paper](https://arxiv.org/abs/2510.21473) | NeurIPS 2025 |
| 2025-10-26 | Encoder-Decoder Diffusion Language Models for Efficient Training and Inference | - | [Paper](https://arxiv.org/abs/2510.22852) | NeurIPS 2025 |
| 2025-11-24 | CDLM: Consistency Diffusion Language Models For Faster Sampling        | -        | [Paper](https://arxiv.org/abs/2511.19269) | -            |
| 2025-11-26 | Masks Can Be Distracting: On Context Comprehension in Diffusion Language Models | - | [Paper](https://arxiv.org/abs/2511.21338) | -            |
| 2025-11-27 | C^2DLM: Causal Concept-Guided Diffusion Large Language Models         | -        | [Paper](https://arxiv.org/abs/2511.22146) | -            |
| 2025-11-29 | EDIT: Early Diffusion Inference Termination for dLLMs Based on Dynamics of Training Gradients | - | [Paper](https://www.arxiv.org/abs/2512.00670) | -        |
| 2025-11-26 | Beyond Confidence: Adaptive and Coherent Decoding for Diffusion Language Models | - | [Paper](https://arxiv.org/abs/2512.02044) | -            |
| 2025-12-02 | Fast-Decoding Diffusion Language Models via Progress-Aware Confidence Schedules | - | [Paper](https://arxiv.org/abs/2512.02892) | -            |




## 5 Multimodal Model <a id="multimodal-model"></a>


### 5.1 Multimodal Understanding
| Date       | Title                                                                 | Abstract | Link                                      | Remark |
|------------|-----------------------------------------------------------------------|----------|-------------------------------------------|--------|
| 2025-05-22 | LLaDA-V: Large Language Diffusion Models with Visual Instruction Tuning | -      | [Paper](https://arxiv.org/abs/2505.16933) | -      |
| 2025-05-22 | LaViDa: A Large Diffusion Language Model for Multimodal Understanding | -        | [Paper](https://arxiv.org/abs/2505.16839) | -      |
| 2025-05-22 | Dimple: Discrete Diffusion Multimodal Large Language Model with Parallel Decoding | - | [Paper](https://arxiv.org/abs/2505.16990) | -      |
| 2025-10-30 | Masked Diffusion Captioning for Visual Feature Learning               | -        | [Paper](https://arxiv.org/abs/2510.26799) | -      |
| 2025-11-12 | MMaDA-Parallel: Multimodal Large Diffusion Language Models for Thinking-Aware Editing and Generation | - | [Paper](https://arxiv.org/abs/2511.09611) | -      |


### 5.2 Unified Multimodal Model
| Date       | Title                                                                 | Abstract | Link                                      | Remark       |
|------------|-----------------------------------------------------------------------|----------|-------------------------------------------|--------------|
| 2025-05-21 | MMaDA: Multimodal Large Diffusion Language Models                     | -        | [Paper](https://arxiv.org/abs/2505.15809) | NeurIPS 2025 |


### 5.3 Speech / ASR
| Date       | Title                                                                 | Abstract | Link                                      | Remark |
|------------|-----------------------------------------------------------------------|----------|-------------------------------------------|--------|
| 2025-08-09 | Whisfusion: Parallel ASR Decoding via a Diffusion Transformer         | -        | [Paper](https://arxiv.org/abs/2508.07048) | -      |



## 6 Variable Length <a id="variable-length"></a>

| Date       | Title                                                                 | Abstract | Link                                      | Remark |
|------------|-----------------------------------------------------------------------|----------|-------------------------------------------|--------|
| 2023-05-24 | David helps Goliath: Inference-Time Collaboration Between Small Specialized and Large General Diffusion LMs | - | [Paper](https://arxiv.org/abs/2305.14771) | -      |
| 2025-06-10 | Edit Flows: Flow Matching with Edit Operations                       | -        | [Paper](https://arxiv.org/abs/2506.09018) | -      |
| 2025-07-15 | DreamOn: Diffusion Language Models For Code Infilling Beyond Fixed-Size Canvas | - | [Paper](https://hkunlp.github.io/blog/2025/dreamon/) | - |
| 2025-08-04 | Beyond Fixed: Variable-Length Denoising for Diffusion Large Language Models | - | [Paper](https://arxiv.org/abs/2508.00819) | -      |
| 2025-08-31 | Any-Order Flexible Length Masked Diffusion                           | -        | [PDF](https://arxiv.org/pdf/2509.01025)   | -      |
| 2025-10-28 | Diffusion LLM with Native Variable Generation Lengths: Let [EOS] Lead the Way | - | [Paper](https://arxiv.org/abs/2510.24605) | -      |



## 7 Others <a id="others"></a>
| Date       | Title                                                                 | Abstract | Link                                      | Remark       |
|------------|-----------------------------------------------------------------------|----------|-------------------------------------------|--------------|
| 2025-08-12 | Time Is a Feature: Exploiting Temporal Dynamics in Diffusion Language Models | - | [Paper](https://arxiv.org/abs/2508.09138) | -            |
| 2025-08-14 | Thinking Inside the Mask: In-Place Prompting in Diffusion LLMs       | -        | [PDF](https://arxiv.org/pdf/2508.10736)   | -            |
| 2025-10-08 | Symbolic-Diffusion: Deep Learning Based Symbolic Regression with D3PM Discrete Token Diffusion | - | [Paper](https://arxiv.org/abs/2510.07570) | -      |
| 2025-09-26 | Unveiling the Potential of Diffusion Large Language Model in Controllable Generation | - | [Paper](https://arxiv.org/abs/2507.04504) | -            |
| 2025-10-17 | Attention Sinks in Diffusion Language Models                          | -        | [Paper](https://arxiv.org/abs/2510.15731) | -            |
| 2025-10-30 | Don't Let It Fade: Preserving Edits in Diffusion Language Models via Token Timestep Allocation | - | [Paper](https://arxiv.org/abs/2510.26200) | NeurIPS 2025 |
| 2025-10-31 | Diffusion LLMs are Natural Adversaries for any LLM                    | -        | [Paper](https://arxiv.org/abs/2511.00203) | -            |
| 2025-11-11 | DiffuGR: Generative Document Retrieval with Diffusion Language Models | -        | [Paper](https://arxiv.org/abs/2511.08150) | -            |
| 2025-11-12 | Branching Flows: Discrete, Continuous, and Manifold Flow Matching with Splits and Deletions | - | [Paper](https://arxiv.org/abs/2511.09465) | -      |
| 2025-11-26 | Closed-Loop Transformers: Autoregressive Modeling as Iterative Latent Equilibrium | - | [Paper](https://arxiv.org/abs/2511.21882) | -            |
| 2025-09-19 | STEAD: Robust Provably Secure Linguistic Steganography with Diffusion Language Model | - | [Paper](https://openreview.net/forum?id=SF2POTDz2o&referrer=%5Bthe%20profile%20of%20Qiyi%20Yao%5D(%2Fprofile%3Fid%3D~Qiyi_Yao1)) | NeurIPS 2025 |


### 7.1 Watermarking
| Date       | Title                                                                 | Abstract | Link                                      | Remark |
|------------|-----------------------------------------------------------------------|----------|-------------------------------------------|--------|
| 2025-09-29 | Watermarking Diffusion Language Models                               | -        | [Paper](https://arxiv.org/abs/2509.24368) | -      |
| 2025-10-03 | DMark: Order-Agnostic Watermarking for Diffusion Large Language Models | -     | [Paper](https://arxiv.org/abs/2510.02902) | -      |
| 2025-11-03 | Watermarking Discrete Diffusion Language Models                      | -        | [Paper](https://arxiv.org/abs/2511.02083) | -      |


### 7.2 Long Context
| Date       | Title                                                                 | Abstract | Link                                      | Remark       |
|------------|-----------------------------------------------------------------------|----------|-------------------------------------------|--------------|
| 2025-06-17 | LongLLaDA: Unlocking Long Context Capabilities in Diffusion LLMs      | -        | [Paper](https://arxiv.org/abs/2506.14429) | -            |
| 2025-09-18 | Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning | - | [Paper](https://arxiv.org/abs/2509.15188) | NeurIPS 2025 |


### 7.3 Alignment

| Date       | Title                                                                 | Abstract | Link                                      | Remark |
|------------|-----------------------------------------------------------------------|----------|-------------------------------------------|--------|
| 2025-10-26 | Aligning Diffusion Language Models via Unpaired Preference Optimization | -     | [Paper](https://arxiv.org/abs/2510.23658) | -      |



### 7.4 Recommend system

| Date       | Title                                                                 | Abstract | Link                                      | Remark |
|------------|-----------------------------------------------------------------------|----------|-------------------------------------------|--------|
| 2025-11-28 | Masked Diffusion for Generative Recommendation                       | -        | [Paper](https://arxiv.org/abs/2511.23021) | -      |



### 7.5 Neighbouring Diffusion research

| Date       | Title                                                                 | Abstract | Link                                      | Remark |
|------------|-----------------------------------------------------------------------|----------|-------------------------------------------|--------|
| 2025-11-14 | LiteAttention: A Temporal Sparse Attention for Diffusion Transformers | -        | [Paper](https://www.arxiv.org/abs/2511.11062) | -   |
| 2025-11-18 | Diffusion As Self-Distillation: End-to-End Latent Diffusion In One Model | -     | [Paper](https://arxiv.org/abs/2511.14716v1) | -    |
| 2025-11-19 | Masked Auto-Regressive Variational Acceleration: Fast Inference Makes Practical Reinforcement Learning | - | [Paper](https://arxiv.org/abs/2511.15190) | - |
| 2025-11-24 | DiP: Taming Diffusion Models in Pixel Space                          | -        | [Paper](https://arxiv.org/abs/2511.18822) | -      |
| 2025-11-27 | Test-time scaling of diffusions with flow maps                       | -        | [Paper](https://arxiv.org/abs/2511.22688) | -      |
| 2025-12-01 | Efficient Training of Diffusion Mixture-of-Experts Models: A Practical Recipe | - | [Paper](https://arxiv.org/abs/2512.01252) | -      |
