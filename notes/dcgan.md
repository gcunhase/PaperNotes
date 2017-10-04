## [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks](https://arxiv.org/abs/1511.06434)
Alec Radford, Luke Metz and Soumith Chintala, Submitted on 19 Nov 2015

TLDR; GAN model using a CNN as D and DCGAN as G.

### Key Points
* DCGAN generates an image from random parameters
* Opposite of CNN, which transforms an image to a class label (list of probabilities)
* Model: CNN is used to classify authentic and fake images (DISCRIMINATOR) and DCGAN is trained to generate images classified as authentic by CNN (GENERATOR)

### Notes / Questions
* See these [slides](https://www.slideshare.net/enakai/dcgan-how-does-it-work)
* Vector arithmetic for visual concepts: "smiling woman - neutral woman + neutral man = similing man"

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

* [DCGAN2](https://github.com/jacobgil/keras-dcgan/blob/master/dcgan.py)

* [carpedm20's dcgan-tensorflow](https://github.com/carpedm20/DCGAN-tensorflow)

```
python download.py mnist
python main.py --dataset mnist --input_height=28 --output_height=28 --train
python main.py --dataset mnist --input_height=28 --output_height=28
```
