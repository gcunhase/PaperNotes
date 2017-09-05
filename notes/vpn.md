## [Video Pixel Networks](https://arxiv.org/abs/1610.00527)
Nal Kalchbrenner et al., Submitted on Oct 2016

TLDR; "Generative video model based on deep neural networks, that reflects the factorization of the joint distribution of the pixel values in a video."

### Key Points
* 4D tensor: time dimension, 2 space dimensions of each frame and colour channels of a pixel
* Operates on pixels without preprocessing and predicts discrete multinomial distributions over raw pixel intensities, allowing the model to estimate distributions of any shape.
* Model:

* Architecture: 2 parts
    * Resolution preserving CNN encoders: dilated convolutions (larger receptive fields and better capture of global motion), preserves spacial resolution at all layers in order to maximize representational capacity.
    * PixelCNN decoders: use masked convolutions to capture space and colour dependencies, use a softmax layer to model the multinomial distributions over raw pixel values.
* Newly defined multiplicative units and corresponding residual blocks.
* Applications / paper evaluations:
    * [Moving MNIST dataset](http://www.cs.toronto.edu/~nitish/unsupervised_video/)
    * [Robotic Pushing dataset](https://sites.google.com/site/brainrobotdata/home/push-dataset)


### Notes / Questions
* Google Deepmind, same authors as [PixelCNN](https://github.com/gcunhase/PaperNotes/blob/master/notes/pixelcnn.md).

### Results
* No code available
