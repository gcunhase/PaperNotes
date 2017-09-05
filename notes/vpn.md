## [Video Pixel Networks](https://arxiv.org/abs/1610.00527)
Nal Kalchbrenner et al., Submitted on Oct 2016

TLDR; Generative video model based on deep neural networks that reflects the factorization of the joint distribution of the pixel values in a video.

### Key Points
* 4D tensor: time dimension, 2 space dimensions of each frame and colour channels of a pixel
* Operates on pixels without preprocessing and predicts discrete multinomial distributions over raw pixel intensities, allowing the model to estimate distributions of any shape.
* Model: $ p(x) = \prod_{t=0}^{T}\prod_{i=0}^{N}\prod_{j=0}^{N} p(x_{t,i,j,B} | x_{<}, x_{t,i,j,R}, x_{t,i,j,G}) p(x_{t,i,j,G} | x_{<}, x_{t,i,j,R}) p(x_{t,i,j,R} | x_{<}) $, where $x_{<} = x_{(t,<i,<j,:)} \cup x_{(t,:,:,:)}$ comprises the RGB values of all pixels to the left and above the pixel at position $(i,j)$ as well as the RGB values of all the pixels from all the previous frames.

* Architecture: 2 parts
    * Resolution preserving CNN encoders: dilated convolutions (larger receptive fields and better capture of global motion), preserves spacial resolution at all layers in order to maximize representational capacity.
    * PixelCNN decoders: use masked convolutions to capture space and colour dependencies, use a softmax layer to model the multinomial distributions over raw pixel values.
* Newly defined multiplicative units (MU) and corresponding residual blocks (RMB).
[insert both images]
<!---
<figure>
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/cGRUatt_blocks2.png" width="600" alt="cGRUatt">
<figcaption><p align="center">cGRUatt structure</p></figcaption>
</p>
</figure>
---!>


* Applications / paper evaluations:
    * [Moving MNIST dataset](http://www.cs.toronto.edu/~nitish/unsupervised_video/)
    * [Robotic Pushing dataset](https://sites.google.com/site/brainrobotdata/home/push-dataset)


### Notes / Questions
* Google Deepmind, same authors as [PixelCNN](https://github.com/gcunhase/PaperNotes/blob/master/notes/pixelcnn.md).
* 4D tensor: $x_{t,i,j,c}$
   * $t \in {0, ..., T}$: one of the frames of the video
   * $i,j \in {0, ..., N}$: row $i$ and column $j$ in frame $t$
   * $c \in{R, G, B}$: one of the three RGB channels of the pixel
* Order of prediction: R, G and B by convention


### Results
* No code available
