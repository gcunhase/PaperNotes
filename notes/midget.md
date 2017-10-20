## [MidiNet: A Convolutional Generative Adversarial Network for Symbolic-domain Music Generation](https://arxiv.org/abs/1703.10847)
Li-Chia Yang, Szu-Yu Chou, and Yi-Hsuan Yang, Submitted on 31 Mar 2017

TLDR; CNNs, GAN, MIDI notes

### Key Points
* Investigate using CNNs for generating melody (a series of MIDI notes) one bar after another in the symbolic domain.
* Novel conditional mechanism to exploit available prior knowledge, so that the model can generate melodies either from scratch, by following a chord sequence, or by conditioning on the melody of previous bars (e.g. a priming melody).

### Notes / Questions


### Results
* Melody of eight-bar long generated: MidiNet vs Google's MelodyRNN
* [Tensorflow 0.12 code](https://github.com/RichardYang40148/MidiNet)
