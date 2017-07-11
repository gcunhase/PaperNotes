
## [Tacotron: Towards End-to-End Speech Synthesis](https://arxiv.org/abs/1703.10135)
Yuxuan Wang et al., Submitted on 29 Mar 2017

TLDR; Tacotron is an end-to-end generative text-to-speech (TTS) model that synthesizes speech directly from characters. Tacotron achieves a 3.82/5 mean opinion score (MOS) on US English, outperforming a production parametric system in terms of naturalness. In addition, since Tacotron generates speech at the frame level, it's substantially faster than sample-level autoregressive methods.

### Key Points
* Given <text, audio> pairs, the model can be trained completely from scratch with random initialization.

### Notes / Questions
* ***Wavenet*** vs Tacotron: "WaveNet (van den Oord et al., 2016) is a powerful generative model of audio. It works well for TTS, but is **slow due to its sample-level autoregressive nature**. It also requires conditioning on linguistic features from an existing TTS frontend, and thus is **not end-to-end**: it only replaces the vocoder and acoustic model.
* ***DeepVoice*** vs Tacotron: "Another recently-developed neural model is DeepVoice (Arik et al., 2017), which replaces every component in a typical TTS pipeline by a corresponding neural network. However, each component is independently trained, and it’s nontrivial to change the system to train in an end-to-end fashion."


### Results
* Check out some [demos](https://github.com/google/tacotron).
* My trials: 

