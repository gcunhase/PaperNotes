## [Generative Adversarial Network](https://arxiv.org/abs/1406.2661)
Ian J. Goodfellow et al., Submitted on 10 Jun 2014

TLDR; GAN consists of a generative net G and a discriminative model D, both MLPs, where G is trying to trick D into thinking the data it's produced is real.

### Key Points
* Discriminative net D: learns to distinguish whether a given data instance is real or not, distinguishes real images from synthesized ones.
* Generative net G: learns to confuse D by generating high quality data, synthesize images resembling real images.
* Both the generative and discriminative models are realized as multilayer perceptrons.

<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/GAN.png" width="300" alt="GAN">
</p>

### Notes / Questions
* Z is the noise vector used to initilize G.
* How to condition GAN in order to choose a desired Z?
  - Solution: MLP, VAE, Stacked Autoencoder

### Results
* [keras-adversarial](https://github.com/bstriner/keras-adversarial): MNIST, CIFAR-10, bidirectional models and AAE
   * MNIST
   * CIFAR-10
