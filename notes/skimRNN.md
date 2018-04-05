## [Neural Speed Reading via Skim-RNN](https://arxiv.org/abs/1711.02085)
Minjoon Seo et al., Submitted on 6 Nov 2017

TLDR; Speed reading RNN

### Key Points
* Network dynamically decides wheteher to use the big RNN (read) or the small RNN (skim) at each time step, depending on the importance of the input.
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/skim_rnn.png" width="600" alt="Skim RNN's Architecture">
</p>

* Novelty:
  * Skip RNN and Jump LSTM both have discrete objectives
  * Skim-RNN introduces Gumbel-softmax parametrization trick that makes the skimming objective differentiable
* Advantages:
  * Lower computational cost than RNN
  * Accuracy is on par with or better than standard RNNs, LSTM-Jump and VCRNN
  * Same input and output interface as RNN, making it easy to replace in existing applications

### Notes / Questions
* Published as conference paper at ICLR 2018
* Used for classification, not for intense tasks such as sequence generation

### Results
* Experiments:
  * Sentiment Analysis: Stanford Sentiment Treebank (SST), Rotten Tomatoes and IMDb
  * Text classification: AGNews
  * Q&A: Stanford Question Answering Dataset (SQuAD), Named Entity dataset of Children Book Test (CBT-NE) and Common Noun of CBT (CBT-CN)
* [schelotto's PyTorch Code](https://github.com/schelotto/Neural_Speed_Reading_via_Skim-RNN_PyTorch)
  * IMDb dataset is used by default and stored in the ./data folder.
  * 300 dimensional GloVe word embedding trained under 840 billion words is used.

