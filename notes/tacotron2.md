## [Natural TTS Synthesis by Conditioning WaveNet on Mel Spectrogram Predictions](https://arxiv.org/abs/1712.05884)
Jonathan Shen et al., Submitted on 16 Dec 2017

TLDR; Neural network architecture for speech synthesis directly from text.

### Key Points
* End-to-end learning
* Model:
  * Recurrent sequence-to-sequence [Tacotron](https://github.com/gcunhase/PaperNotes/blob/master/notes/tacotron.md)-style model that generates mel spectrograms
  * Modified WaveNet model acting as a vocoder to synthesize timedomain waveforms from those spectrograms  
  
  <p align="center">
  <img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/tacotron2_architecture.png" width="400" alt="Tacotron 2">
  </p>
  
* In comparison to the linguistic and acoustic features used in WaveNet, the mel spectrogram is a simpler, lower-level acoustic representation of audio signals.  
* Demonstrates ``that using a compact acoustic intermediate representation enables significant simplification of the WaveNet architecture.''

### Notes / Questions
* Vocoder: ``category of voice codec that analyzes and synthesizes the human voice signal for audio data compression, multiplexing, voice encryption, voice transformation, etc.''
* A mel-frequency spectrogram is related to the linear-frequency spectrogram, i.e. the short-time Fourier transform (STFT) magnitude.

### Results
* Model achieves a mean opinion score (MOS) of 4.53 comparable to a MOS of 4.58 for professionally recorded speech.
* Check out some [demos](https://google.github.io/tacotron/publications/tacotron2/index.html).

