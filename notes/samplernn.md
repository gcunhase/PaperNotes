## [SampleRNN: An Unconditional End-to-End Neural Audio Generation Model](https://arxiv.org/abs/1612.07837)
Soroush Mehri, Yoshua Bengio, et al., Submitted on 22 Dec 2016 (v1), last revised 11 Feb 2017 (v2)
ICLR 2017

TLDR; Music generation with SampleRNN, network with 2 RNNs (frame-level) and 1 MLP (sample-level)

### Key Points
* Sample-level memory-less MLP + 2 frame-level modules of stateful RNNs
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/SampleRNN.png" width="300" alt="SampleRNN">
</p>

* Captures long-term dependencies

### Notes / Questions
* Training
  * Input: audio sequence divided into non-overlapping frames of size $FS^{k}$.
  * Tier 3 input: $FS^{3}=16$ audio samples
  * Higher level: larger receptive field (models longer dependencies)
  * Tiers 2 and 1: $FS^{k}=4$ audio samples
  * Lower levels: models samples that are closer together in time
  
* Testing / Generating
  * Input: array of zeros of size $N$
  * Trained model generates samples and sequentially adds them to the array

### Results
* Performance comparable to WaveNet according to Human Evaluation
* Tested on 3 different datasets:
* [Author's code](https://github.com/soroushmehr/sampleRNN_ICLR2017)
* [Pytorch code](https://github.com/deepsound-project/samplernn-pytorch), [my fork](https://github.com/gcunhase/samplernn-pytorch)
