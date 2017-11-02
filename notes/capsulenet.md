## [Dynamic Routing Between Capsules](https://arxiv.org/abs/1710.09829)
Sara Sabour, Nicholas Frosst, Geoffrey E Hinton, Submitted on 26 Oct 2017

TLDR; Capsules are small group of neurons, a Capsule Netowrk is a twist on neural networks intended to make machines better able to understand the world through images or video.

### Key Points
* Current networks need a large number of example photos to learn to reliably recognize objects in all kinds of situations. "That’s because the software isn’t very good at generalizing what it learns to new scenarios, for example understanding that an object is the same when seen from a new viewpoint."
* Hinton’s idea for narrowing the gulf between the best AI systems and ordinary toddlers is to build a little more knowledge of the world into computer-vision software. 
* Capsules—small groups of crude virtual neurons—are designed to track different parts of an object, such as a cat’s nose and ears, and their relative positions in space.
* Capsule Net is able to understand when a new scene is in fact a different view of something it has seen before.

* Model:
   1. All but the last layers on the capsules are *convolutional*
   2. Replaces the scalar-output feature detectors of CNNs with *vector-output capsules* (output of the capsule is a vector)
   3. Replaces max-pooling with *routing-by-agreement*
* Dynamic routing mechanism, segmenting highly overlapping objects

* Assumption: our multi-layer visual system creates something like a parse tree on each fixation
* Multiple fixations: allows us to ignore the issue of how these single-fixation parse trees are coordinated
* Instantiation parameters: hue, pose, deformation, velocity...


### Notes / Questions
* ICLR 2018 submission: [Matrix capsules with EM routing](https://openreview.net/forum?id=HJWLfGWRb&noteId=HJWLfGWRb)
* [News](https://www.wired.com/story/googles-ai-wizard-unveils-a-new-twist-on-neural-networks/)
* [Capsules in MNIST](http://www.cs.toronto.edu/~fritz/absps/transauto6.pdf)

### Results
* State-of-the-art performance on MNIST

