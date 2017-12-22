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
*  In a nutshell: sequence-to-sequence model optimized for TTS to map a sequence of letters to a sequence of features that encode the audio. These features, an 80-dimensional audio spectrogram with frames computed every 12.5 milliseconds, capture not only pronunciation of words, but also various subtleties of human speech, including volume, speed and intonation. Finally these features are converted to a 24 kHz waveform using a WaveNet-like architecture. [Source](https://research.googleblog.com/2017/12/tacotron-2-generating-human-like-speech.html?m=1).
* In comparison to the linguistic and acoustic features used in WaveNet, the mel spectrogram is a simpler, lower-level acoustic representation of audio signals.  

### Notes / Questions
* Vocoder: category of voice codec that analyzes and synthesizes the human voice signal for audio data compression, multiplexing, voice encryption, voice transformation, etc.
* A mel-frequency spectrogram is related to the linear-frequency spectrogram, i.e. the short-time Fourier transform (STFT) magnitude.

### Results
* Model achieves a mean opinion score (MOS) of 4.53 comparable to a MOS of 4.58 for professionally recorded speech.
* Conclusion: the use of a compact acoustic intermediate representation enables significant simplification of the WaveNet architecture.
* Problems:
  * System has difficulties pronouncing complex words (such as “decorum” and “merlot”)
  * In extreme cases it can even randomly generate strange noises
  * System cannot yet generate audio in realtime
  * Cannot yet control the generated speech, such as directing it to sound happy or sad
* Check out some [demos](https://google.github.io/tacotron/publications/tacotron2/index.html).

