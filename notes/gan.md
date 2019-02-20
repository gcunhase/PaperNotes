## [Generative Adversarial Network](https://arxiv.org/abs/1406.2661)
Ian J. Goodfellow et al., Submitted on 10 Jun 2014

TLDR; GAN consists of a generative net G and a discriminative model D, both MLPs, where G is trying to trick D into thinking the data it's produced is real.

### Key Points
* G maximizes the probability of D making a mistake = minimize $log(1 - D(G(z)))$
    * Log: used because it stretches the range of the function from -inf to 0, making it easier to compute the gradient since error will be bigger
* Discriminative net D: output ranges between 0 to 1, learns to distinguish whether a given data instance is real or not, distinguishes real images from synthesized ones.
* Generative net G: learns to confuse D by generating high quality data, synthesize images resembling real images.
* Both the generative and discriminative models are realized as multilayer perceptrons: meaning it can be trained with *backpropagation*.

<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/GAN.png" width="300" alt="GAN">
</p>

### Notes / Questions
* The rate with which D and G are updated can influence the result.
* Z is the noise vector used to initilize G: only has 1 domain, needs random vector (similar to RNN's initial hidden state)
* *Conditional generative model*: How to condition GAN in order to choose a desired Z?
  - Solution: MLP, VAE, Stacked Autoencoder
* ﻿Question on Adversarial Loss (AL)

* Adversarial loss
    * MinMax: G tries to maximize the amount of times D classifies the generated samples as real and D wants to minimize the amount of times it makes a mistake
    * Police vs faake cash/ID problem
    * L_{GAN} (G, D_Y, X, Y) = E_{y ~ p_{data}(y)}[log D_Y(y)] + E_{x ~ p_{data}(x)}[log D_Y(G((x))]
    * E = Expectation of the formula with samples x drawn from the distribution of p_{data}
    * E(x) = \integral x p(x) dx
    * E(f(x)) = \integral f(x) p(x) dx
    * However, p(x) is what we're trying to model, so we don't have it yet. Taking the idea of Monte Carlo of sampling from the data, the integral can be approximated to a discrete sum
    * E(f(x)) = 1/N * \sum_{n=1}^N f(x), where N = batch size
  
### Results
* Datasets: MNIST, The Toronto Face Database and CIFAR-10
* [bstriner's keras-adversarial](https://github.com/bstriner/keras-adversarial): MNIST, CIFAR-10, bidirectional models and AAE


<table align="center"> 
  <tr>
    <td align="center"><b>MNIST</b><p><i>example_gan.py</i></p></td><td align="center"><b>MNIST Conv</b><p><i>example_gan_convolutional.py</i></p></td><td align="center"><b>CIFAR-10</b><p><i>example_gan_cifar10.py</i></p></td>
  </tr>
  <tr>
    <td align="center">58.7 minutes, 100 epochs</td><td align="center">322 minutes, 100 epochs</td><td>Stopped, 2603 epochs</td>
  </tr>
  <tr>
    <td align="center"><img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/gan_epoch99.png" width="150" alt="GAN 100 epochs"></td><td align="center"><img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/gan_conv_epoch99.png" width="150" alt="GAN Conv 100 epochs"></td><td align="center"><img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/gan_cifar10_epoch2602.png" width="150" alt="GAN CIFAR-10 2603 epochs"></td>
  </tr>
</table>


