## [Efficient Neural Audio Synthesis](https://arxiv.org/abs/1802.08435)
Nal Kalchbrenner, Aaron van den Oord, et al., Submitted on 23 Feb 2018 (v1), last revised 25 Jun 2018, ICML

TLDR; WaveRNN applied on TTS synthesis, raw audio at 24 kHz in 16-bit format

### Key Points
* Limitation of previous models:
  * "The serial aspect of the sampling process can make it slow and impractical to use these models to generate high-dimensional data like speech and video."

* **Goal**: "to increase the efficiency of sampling from sequential models without compromising their quality."

* Novelty:
  * "Describe a set of general techniques for reducing sampling time while maintaining high output quality."
  * WaveRNN
    * Single-layer RNN with a dual softmax layer that matches the quality of the state-of-the-art WaveNet model.
  * Sparse WaveRNN
    * "Weight pruning technique to reduce the number of weights in the WaveRNN"
    * Capable of real-time audio synthesis on mobile CPUs
    * WaveRNN vs Sparse WaveRNN: "large sparse WaveRNNs significantly outperform small dense WaveRNNs" with the same number of parameters
  * Subscale WaveRNN
    * "New generation scheme based on subscaling that folds a long sequence into a batch of shorter sequences and allows one to generate multiple samples at once."
  
### Notes / Questions
* 16-bits: 8 coarses *c_t* (more significant), 8 fine *f_t* (least significant)

### Results
* Performance measures: NLL of ground-truth audio, MOS between 1 (bad) and 5 (excellent), and A/B comparison tests between pair of models as rated by human subjects on a scale between -3 (much worse than) and +3 (much better than).
* Dataset: 44 hours of North American English speech recorded by a professional speaker
* [Pytorch code](https://github.com/fatchord/WaveRNN)
