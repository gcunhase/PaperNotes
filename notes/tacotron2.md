## [Natural TTS Synthesis by Conditioning WaveNet on Mel Spectrogram Predictions](https://arxiv.org/abs/1712.05884)
Jonathan Shen et al., Submitted on 16 Dec 2017

TLDR; Neural network architecture for speech synthesis directly from text.

### Key Points
* Model:
  * Recurrent sequence-to-sequence feature prediction network mapping character embeddings to mel-scale spectrograms
  * Modified WaveNet model acting as a vocoder to synthesize timedomain waveforms from those spectrograms  
* Demonstrates ``that using a compact acoustic intermediate representation enables significant simplification of the WaveNet architecture.''

### Notes / Questions
* Check notes on [Tacotron](https://github.com/gcunhase/PaperNotes/blob/master/notes/tacotron.md)
* Vocoder: ``category of voice codec that analyzes and synthesizes the human voice signal for audio data compression, multiplexing, voice encryption, voice transformation, etc.''

### Results
* Model achieves a mean opinion score (MOS) of 4.53 comparable to a MOS of 4.58 for professionally recorded speech.
* Check out some [demos](https://google.github.io/tacotron/publications/tacotron2/index.html).

