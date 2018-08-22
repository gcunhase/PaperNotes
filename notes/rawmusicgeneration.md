## [The challenge of realistic music generation: modelling raw audio at scale](https://arxiv.org/abs/1806.10474)
Sander Dieleman, Aäron van den Oord and Karen Simonyan, Submitted on 26 Jun 2018
DeepMind UK

TLDR; 

### Key Points

<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/rawmusicgeneration_summary.png" width="500" alt="Summary table">
</p>

* Model: ADA
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/rawmusicgeneration_model.png" width="400" alt="Model">
</p>

* VQ-VAE

* AMAE

* **Evaluation metrics** in other domains: measure realism of generated images (Inception Score and Frechet Inception Distance), machine translation (BLEU). "So far no such metric has been developed for music." Authors conclusion is that listening to samples is essential to meaningfully compare models.
* Authors use *NLL* for quantitative metric and Fidelity and Musicality human scores for qualitative
  * Definition of qualitative measures are not defined

### Notes on *Waveform vs Symbolic*
* "The use of symbolic representations comes with limitations: the nuances abstracted away by such representations are often musically quite important and greatly impact our enjoyment of music."
* Extraction of timing, timbre and volume is difficult and impractical for most instruments except piano.
* "Symbolic representations are often tailored to particular instruments, which reduces their generality and implies that a lot of work is required to apply existing modelling techniques to new instruments."
* "Models of audio waveforms are also much more general and can be applied to recordings of any set of instruments, or non-musical audio signals such as speech."
* Because of its *complexity*, modelling raw audio signals have received relatively little attention. In recent times research has been done resulting in models such as *WaveNet*, *Magenta*, *Tacotron* and *SampleRNN*, but that's still minimal in comparison to its counterpart models which consider symbolic representations of the audio.
* "Previous work on music modelling in the raw audio domain has shown that capturing local structure is feasible, but capturing higher-level structure has proven difficult."
* "SampleRNN and WaveNet have been applied to music generation, but in neither case do the samples exhibit interesting structure at timescales of seconds and beyond."

### Notes / Questions
* RF: receptive fields
* Hop size (h): "ratio between the sample rates of the conditioning signal and the input."
* PBT (population based training): optimization of hyperparemeters to maximize performance.

### Results
* "Capable of modelling structure across 400,000 timesteps, or about 25 seconds of audio sampled at 16 kHz"
* [Generated audios](https://drive.google.com/drive/folders/1NY3MTkOSodz_5eCkjtoHUGYSulR25QGU)
