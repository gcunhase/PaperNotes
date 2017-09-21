## [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks](https://arxiv.org/abs/1511.06434)
Alec Radford, Luke Metz and Soumith Chintala, Submitted on 19 Nov 2015

TLDR; 

### Key Points
* DCGAN

### Notes / Questions

### Results

* [DCGAN on MNIST](https://github.com/roatienza/Deep-Learning-Experiments/blob/master/Experiments/Tensorflow/GAN/dcgan_mnist.py)
   * Results on MNIST
      * Step 9999, 34min: [D loss: 0.701930, acc: 0.507812]  [A loss: 0.835322, acc: 0.207031]
      * Original, step 500 and step 10,000

      <p align="left">
        <img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/dcgan_mnist.png" width="150" alt="DCGAN Original" hspace="30">
        <img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/dcgan_mnist500.png" width="150" alt="DCGAN 500">
        <img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/dcgan_mnist10000.png" width="150" alt="DCGAN 10,000" hspace="30">
      </p>

* [keras-adversarial](https://github.com/bstriner/keras-adversarial): code is more complete (MNIST, CIFAR-10 and bidirectional models)

* [DCGAN2](https://github.com/jacobgil/keras-dcgan/blob/master/dcgan.py)

