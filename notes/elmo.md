## [ELMo: Deep contextualized word representations](https://arxiv.org/abs/1802.0536)
Matthew E. Peters et al. 22 Mar 2018 version, NAACL 2018, Allen Institute

TLDR; Contextualized word embedding

### Key Points
* Contextualized word embedding
* Concatenates hidden states and initial embedding from forward and backward LSTMs + weighted summation based on task
* "concatenation of independently trained left-to-right and right-to-left LSTM"
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/elmo_embedding.png" width="500" alt="ELMo">
</p>

### References
* [1] [slides](https://www.slideshare.net/shuntaroy/a-review-of-deep-contextualized-word-representations-peters-2018)
* [2] [The Illustrated BERT, ELMo, and co](http://jalammar.github.io/illustrated-bert/) by Jay Alammar: image source
