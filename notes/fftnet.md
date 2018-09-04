## [FFTNet: a Real-Time Speaker-Dependent Neural Vocoder](http://gfx.cs.princeton.edu/pubs/Jin_2018_FAR/)
Zeyu Jin et al., ICASSP April 2018, Princeton Uni and Adobe Research

TLDR; 

### Key Points
* Model
  * "Generates one sample at a time based on previously generated samples and an auxiliary condition"
  * "Architecture resembles the Fast Fourier Transform" 
  * "Given size-8 inputs, they are first divided into two halves; each passed through a different 1×1 convolution layer and then summed together. The summed size-4 output will pass through ReLU and then another 1×1 convolution and ReLU before repeating the the same operation."
  
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/FFTNet.png" width="250" alt="FFTNet">
</p>

* FFTNet as a vocoder: *h_t* as F0 and MCC features at time *t*

### Notes / Questions
* Vocoder: "a synthesizer that produces sounds from an analysis of speech input"
* Previous Models:
  * MLSA: baseline vocoder
  * Fast WaveNet (synthesis 1 second of audio in 1 minute)
  * Deep Voice: faster but at the cost of quality loss
  * Parallel WaveNet: parallelism on a GPU cluster
  * [WaveNet](https://github.com/gcunhase/PaperNotes/edit/master/notes/wavenet.md) as a vocoder: "generates waveform from acoustic features", meaning that the model needs a "substantially smaller corpus (roughly 1 hour)"
    * Auxiliary conditions: acoustic features such as MCC and pitch

* Subjective and objective evaluations are contradictory?

### Results
* Advantages:
  * Less parameters than WaveNet
  * Produces audio more quickly than Fast WaveNet (>70x faster, 0.81 seconds for 1 second of audio generated), meaning that "a modern CPU can generate audio samples in real-time"
  * Better MOS than WaveNet when used as a vocoder, "higher quality synthetic voices"

* Evalution:
  * MOS (bar chart) via Amazon Mechanical Turk (AMT)
  * Average spectral and cepstral distortion (dB): RMSE (frequency domain difference between 2 signals) and MCD (difference in the cepstral domain, characteristics of the original speech)

* Model specs: Adam, *lr=0.001*, 100,000 steps
