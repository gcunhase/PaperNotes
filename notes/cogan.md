## [Coupled Generative Adversarial Networks](https://arxiv.org/abs/1606.07536)
Ming-Yu Liu and Oncel Tuzel, Submitted on 24 Jun 2016

TLDR; CoGAN learns a joint distribution of multi-domain images without any tuple of corresponding images in the different domains.

### Key Points
* CoGAN consists of a pair of GANs: GAN1 and GAN2. Each has a generative model for synthesizing realistic images in one domain and a discriminative model for classifying whether an image is real or synthesized.
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/CoGAN.png" width="400" alt="CoGAN">
</p>

* Novelty: CoGAN can learn a joint distribution without tuples of corresponding images in the different domains in the training set.

* Learns a joint distribution of multi-domain images by enforcing a simple weight-sharing constraint to the layers that are responsible for decoding abstract semantics

* Unsupervised learning

### Notes / Questions
* Z vector noise

### Results
* Applied to several joint distribution learning tasks:
  - Learning a joint distribution of color and depth images
  - Learning a joint distribution of face images with different attributes
  
