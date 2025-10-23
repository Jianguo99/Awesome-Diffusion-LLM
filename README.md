# Awesome-Diffusion-LLM

This repository (Daily updating) provides a curated list of papers on Diffusion Large Language Models (dLLMs), a rapidly emerging field in generative AI. The collection is organized to track advancements from foundational theory to state-of-the-art applications.

The field is evolving quickly, and this list is a living document. **We welcome community contributions.** If you know of a relevant paper we've missed, please feel free to **submit a pull request**.

---

- [Theoretical Basis](#theoretical-basis)
- [Foundation Model](#foundation-model)
- [Inference Method](#inference-method)
- [Multimodal Model](#multimodal-model)
- [Reinforcement Learning](#reinforcement-learning)
- [Variable Length](#variable-length)
- [Others](#others)

## Theoretical Basis
**Deep Unsupervised Learning using Nonequilibrium Thermodynamics**  
2015-3-12, [Paper](https://arxiv.org/abs/1503.03585)

**Structured Denoising Diffusion Models in Discrete State-Spaces**  
2021-7-7, [Paper](https://arxiv.org/abs/2107.03006)

**Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution**  
2023-10-25, [Paper](https://arxiv.org/abs/2310.16834)

**Your Absorbing Discrete Diffusion Secretly Models the Conditional Distributions of Clean Data**  
2024-6-6, [Paper](https://arxiv.org/abs/2406.03736)

**Simplified and Generalized Masked Diffusion for Discrete Data**  
2024-6-6, [Paper](https://arxiv.org/abs/2406.04329)

**Simple and Effective Masked Diffusion Language Models**   
2024-6-11, [Paper](https://arxiv.org/abs/2406.07524)

**Next Semantic Scale Prediction via Hierarchical Diffusion Language Models**  
2025-10-13, [Paper](https://arxiv.org/abs/2510.08632)


## Foundation Model

**LLaDA: Large Language Diffusion Models**  
2025-2-14, [Paper](https://arxiv.org/abs/2502.09992)

**Dream 7B**  
2025-4-2, [Paper](https://hkunlp.github.io/blog/2025/dream/)

**Seed Diffusion: A Large-Scale Diffusion Language Model with High-Speed Inference**  
2025-8-4, [Paper](https://www.arxiv.org/abs/2508.02193)  

**Gemini Diffusion**   
2025-05-20, [Link](https://deepmind.google/models/gemini-diffusion/)

**Soft-Masked Diffusion Language Models**   
2025-10-20, [Paper](https://arxiv.org/abs/2510.17206)

### Autoregressive vs. Diffusion LLMs
**Closing the Data-Efficiency Gap Between Autoregressive and Masked Diffusion LLMs**   
2025-10-10, [Paper](https://arxiv.org/abs/2510.09885)


## Inference Method

**Planner and Executor: Collaboration between Discrete Diffusion And Autoregressive Models in Reasoning**   
2025-10-17, [Paper](https://arxiv.org/abs/2510.15244)

### Enable KV Cache
**dKV-Cache: The Cache for Diffusion Language Models**  
2025-5-21, [Paper](https://arxiv.org/abs/2505.15781)

**dLLM-Cache: Accelerating Diffusion Large Language Models with Adaptive Caching**  
2025-5-22, [Paper](https://github.com/maomaocun/dLLM-cache?tab=readme-ov-file)

**Accelerating Diffusion Language Model Inference via Efficient KV Caching and Guided Diffusion**  
2025-5-27, [Paper](https://arxiv.org/pdf/2505.21467)

**Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding**  
2025-5-28, [Paper](https://nvlabs.github.io/Fast-dLLM/paper/fast_dllm.pdf)

**Esoteric Language Models**  
2025-6-2, [Paper](https://arxiv.org/abs/2506.01928)

**Sparse-dLLM: Accelerating Diffusion LLMs with Dynamic Cache Eviction**  
2025-8-4, [Paper](https://arxiv.org/abs/2508.02558)

**DPad: Efficient Diffusion Language Models with Suffix Dropout**  
2025-8-19, [Paper](https://arxiv.org/abs/2508.14148)

**dInfer: An Efficient Inference Framework for Diffusion Language Models**
2025-10-13, [Paper](https://arxiv.org/abs/2510.08666)

**Attention Is All You Need for KV Cache in Diffusion LLMs**  
2025-10-16, [Paper](https://arxiv.org/abs/2510.14973)

### Advanced Sampling Method

**Remasking Discrete Diffusion Models with Inference-Time Scaling**  
2025-05-22, [Paper](https://arxiv.org/abs/2503.00307)

**Dimple: Discrete Diffusion Multimodal Large Language Model with Parallel Decoding**  
2025-05-22, [Paper](https://arxiv.org/abs/2505.16990)

**Variational Autoencoding Discrete Diffusion with Enhanced Dimensional Correlations Modeling**  
2025-05-23, [Paper](https://arxiv.org/abs/2505.17384)

**Accelerating Diffusion Language Model Inference via Efficient KV Caching and Guided Diffusion**  
2025-05-27, [Paper](https://arxiv.org/pdf/2505.21467)

**Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding**  
2025-05-28, [Paper](https://nvlabs.github.io/Fast-dLLM/paper/fast_dllm.pdf)

**Accelerated Sampling from Masked Diffusion Models via Entropy Bounded Unmasking**  
2025-05-30, [Paper](https://arxiv.org/abs/2505.24857)

**Accelerating Diffusion LLMs via Adaptive Parallel Decoding**  
2025-05-31, [Paper](https://arxiv.org/abs/2506.00413)

**Accelerating Diffusion Large Language Models with SlowFast Sampling: The Three Golden Principles**  
2025-06-12, [Paper](https://arxiv.org/abs/2506.10848)

**Wide-In, Narrow-Out: Revokable Decoding for Efficient and Effective DLLMs**  
2025-07-24，[Paper](https://arxiv.org/abs/2507.18578)

**DPad: Efficient Diffusion Language Models with Suffix Dropout**  
2025-08-19, [Paper](https://arxiv.org/abs/2508.14148)

**Mask Tokens as Prophet: Fine-Grained Cache Eviction for Efficient dLLM Inference**    
2025-10-13, [Paper](https://arxiv.org/abs/2510.09309)

**Guided Star-Shaped Masked Diffusion**   
2025-10-09, [Paper](https://arxiv.org/abs/2510.08369)

**Efficient Parallel Samplers for Recurrent-Depth Models and Their Connection to Diffusion Language Models**   
2025-10-16, [Paper](https://arxiv.org/abs/2510.14961)

**Planned Diffusion**    
2025-10-21, [Paper](https://arxiv.org/abs/2510.18087)

**How Efficient Are Diffusion Language Models? A Critical Examination of Efficiency Evaluation Practices**  
2025-10-21, [Paper](https://arxiv.org/abs/2510.18480)

**Saber: An Efficient Sampling with Adaptive Acceleration and Backtracking Enhanced Remasking for Diffusion Language Model**  
2025-10-20, [Paper](https://arxiv.org/abs/2510.18165)



## Multimodal Model
### Multimodal Understanding
**LLaDA-V: Large Language Diffusion Models with Visual Instruction Tuning**  
2025-5-22, [Paper](https://arxiv.org/abs/2505.16933)

**LaViDa: A Large Diffusion Language Model for Multimodal Understanding**  
2025-5-22, [Paper](https://arxiv.org/abs/2505.16839)

**Dimple: Discrete Diffusion Multimodal Large Language Model with Parallel Decoding**  
2025-5-22, [Paper](https://arxiv.org/abs/2505.16990)

### Unified Multimodal Model
**MMaDA: Multimodal Large Diffusion Language Models**  
2025-5-21, [Paper](https://arxiv.org/abs/2505.15809)

### Speech / ASR
**Whisfusion: Parallel ASR Decoding via a Diffusion Transformer**  
2025-8-9, [Paper](https://arxiv.org/abs/2508.07048)

## Reinforcement Learning
**d1: Scaling Reasoning in Diffusion Large Language Models via Reinforcement Learning**  
2025-4-16, [Paper](https://arxiv.org/abs/2504.12216)

**Reinforcing the Diffusion Chain of Lateral Thought with Diffusion Language Models**  
2025-5-15, [Paper](https://arxiv.org/abs/2505.10446)

**LLaDA 1.5: Variance-Reduced Preference Optimization for Large Language Diffusion Models**  
2025-5-25, [Paper](https://arxiv.org/abs/2505.19223)

**wd1: Weighted Policy Optimization for Reasoning in Diffusion Language Models**     
2025-07-07, [Paper](https://arxiv.org/abs/2507.08838)

**DiffuCoder: Understanding and Improving Masked Diffusion Models for Code Generation**  
2025-7-25, [Paper](https://arxiv.org/abs/2506.20639)

**MDPO: Overcoming the Training-Inference Divide of Masked Diffusion Language Models**  
2025-8-18, [Paper](https://arxiv.org/pdf/2508.13148)

**Revolutionizing Reinforcement Learning Framework for Diffusion Large Language Models**  
2025-9-8, [Paper](https://arxiv.org/pdf/2509.06949)

**Inpainting-Guided Policy Optimization for Diffusion Large Language Models**  
2025-9-12, [Paper](https://arxiv.org/pdf/2509.10396)

**Improving Reasoning for Diffusion Language Models via Group Diffusion Policy Optimization**   
2025-10-09, [Paper](https://arxiv.org/abs/2510.08554)

**SPG: Sandwiched Policy Gradient for Masked Diffusion Language Models**    
2025-10-13, [Paper](https://arxiv.org/abs/2510.09541)

**Boundary-Guided Policy Optimization for Memory-efficient RL of Diffusion Large Language Models**   
2025-10-14, [Paper](https://arxiv.org/abs/2510.11683)




## Variable Length
**Edit Flows: Flow Matching with Edit Operations**  
2025-6-10, [Paper](https://arxiv.org/abs/2506.09018)

**DreamOn: Diffusion Language Models For Code Infilling Beyond Fixed-Size Canvas**  
2025-7-15, [Paper](https://hkunlp.github.io/blog/2025/dreamon/)

**Beyond Fixed: Variable-Length Denoising for Diffusion Large Language Models**  
2025-8-4, [Paper](https://arxiv.org/abs/2508.00819)

**Any-Order Flexible Length Masked Diffusion**  
2025-8-31, [Paper](https://arxiv.org/pdf/2509.01025)

## Others
**Time Is a Feature: Exploiting Temporal Dynamics in Diffusion Language Models**  
2025-8-12, [Paper](https://arxiv.org/abs/2508.09138)  

**Thinking Inside the Mask: In-Place Prompting in Diffusion LLMs**  
2025-8-14, [Paper](https://arxiv.org/pdf/2508.10736)  

**Symbolic-Diffusion: Deep Learning Based Symbolic Regression with D3PM Discrete Token Diffusion**   
2025-10-08, [Paper](https://arxiv.org/abs/2510.07570)

**Unveiling the Potential of Diffusion Large Language Model in Controllable Generation**   
2025-09-26, [Paper](https://arxiv.org/abs/2507.04504)

**Attention Sinks in Diffusion Language Models**   
2025-10-17, [Paper](https://arxiv.org/abs/2510.15731)


### Long Context
**LongLLaDA: Unlocking Long Context Capabilities in Diffusion LLMs**  
2025-6-17, [Paper](https://arxiv.org/abs/2506.14429)