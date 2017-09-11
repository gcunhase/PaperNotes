## [Look, Listen and Learn](https://arxiv.org/abs/1705.08168)
Relja Arandjelović and Andrew Zisserman, Submitted on 23 May 2017

TLDR; DeepMind

We consider the question: what can be learnt by looking
at and listening to a large number of unlabelled videos?
There is a valuable, but so far untapped, source of information
contained in the video itself – the correspondence
between the visual and the audio streams, and we introduce
a novel “Audio-Visual Correspondence” learning task
that makes use of this. Training visual and audio networks
from scratch, without any additional supervision other than
the raw unconstrained videos themselves, is shown to successfully
solve this task, and, more interestingly, result in
good visual and audio representations. These features set
the new state-of-the-art on two sound classification benchmarks,
and perform on par with the state-of-the-art selfsupervised
approaches on ImageNet classification. We also
demonstrate that the network is able to localize objects in
both modalities, as well as perform fine-grained recognition
tasks.

### Key Points
* Semantic Maps
  * Show us which part of the image is responsible for the sounds that we hear.
  * *Audio-vision correspondence* (AVC) detector network: Vision subnetwork + Audio subnetworks fused into fusion layers
* Unsupervised
* Audio and visual features: $L^{3}$-Net approach
  <p align="center">
  <img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/looklistenlearn_l3net.png" width="200" alt="$L^{3}$-Net architecture">
  </p>

* Dataset:
  * [Flickr-SoundNet](https://arxiv.org/abs/1610.09001)
    * Unlablled data of videos from Flickr.
    * Contains over 2 million videos (26TB) but for practical reasons the authors use a random subset of 500k videos (400k training, 50k validation and 50k test) and only use the first 10 seconds of each video.
  * [The Kinetics Human Action Video Dataset](https://arxiv.org/abs/1705.06950)
    * Labelled data, useful for quantitative evaluation
    * [Download](https://deepmind.com/research/open-source/open-source-datasets/kinetics/)
    * Subset used:
      * 19k 10 second video clips (15k training, 1.9k validation, 1.9k test)
      * 34 human action classes

### Notes / Questions
* Review also available on [Two Minute Papers #184](https://www.youtube.com/watch?v=mL3CzZcBJZU).
* How many audio/visual features are extracted with the $L^{3}$-Net approach?

