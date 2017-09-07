## [Get To The Point: Summarization with Pointer-Generator Networks](https://arxiv.org/abs/1704.04368)
Abigail See et al., Submitted on 14 Apr 2017

TLDR; Novel architecture that augments the standard seq2seq attentional model in two orthogonal ways: pointing (for UNK) and coverage (to discourage repetition). Applied in the context of multi-sentence summaries.

### Key Points
* Abstractive text summarization: generates original text, not just selecting and rearranging passages form the original text.
* Problem with seq2seq models:
    * Liable to produce factual details inaccurately
    * Inability to deal with Out-Of-Vocabulary (OOV) words
    * Tend to repeat themselves
* Model:
    * Similar to Gu et al.'s [CopyNet](https://arxiv.org/abs/1603.06393) and Miao and Blunsom's [Forced-Attention Sentence Compression](https://arxiv.org/abs/1609.07317), applied to short-text summarization.
    * Proposes novel variant of the coverage vector from Neural Machine Translation
* Architecture:
    * Hybrid pointer-generator network: can copy words from the source text via *pointintg* and still *generate* words. Can be viewed as a balance between extractive and abstractive approaches.
    * *Coverage*: keeps track of what has been summarized (discouraging repetitions)

### Notes / Questions

### Results
* Applied to the CNN / Daily Mail summarization task
    * News article (39 sentences on average) paired with multi-sentence summaries.
    * Outperforms the state-of-the-art abstractive system by at least 2 ROUGE points.

