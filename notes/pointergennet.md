## [Get To The Point: Summarization with Pointer-Generator Networks](https://arxiv.org/abs/1704.04368)
Abigail See et al., Submitted on 14 Apr 2017

TLDR; Novel architecture that augments the standard seq2seq attentional model in two orthogonal ways: pointing (for UNK) and coverage (to discourage repetition).

### Key Points
* Abstractive text summarization: generates original text, not just selecting and rearranging passages form the original text.
* Seq2seq: liable to produce factual details inaccurately and they tend to repeat themselves.
* Architecture:
    * Hybrid pointer-generator network: can copy words from the source text via *pointintg*
    * *Coverage*: keeps track of what has been summarized (discouraging repetitions)

### Notes / Questions

### Results
* Applied to the CNN / Daily Mail summarization task

