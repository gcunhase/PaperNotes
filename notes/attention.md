## My Notes on Attention in NLP

TLDR; My notes on Attention in NLP 

### Main Key Points
* Originally used for visual imaging (90s)
* Became trendy in 2014: Google Mind released paper for [RNN+attention](https://papers.nips.cc/paper/5542-recurrent-models-of-visual-attention.pdf) in image classification and Bahdanau used attention for [MT](https://arxiv.org/abs/1409.0473)
* Weight is used to indicate the importance of each word
* (Encoded vector) + (Context based on the attention weights) are used to compute a different embedding to be given to a decoder
* [Attention model](https://arxiv.org/abs/1409.0473) [6,5]
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/attention_model.png" width="450" alt="Attention Model" hspace="20">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/attention_model_distill.png" width="350" alt="Attention Model">
</p>

### Further Explanation
* What problem does Attention solve?
    * Long term memorization: seq2seq encodes all the information into a fixed-length vector, so the longer the sentence, the more difficult it is to obtain an acceptable embedding.
    * Better interpretability: scores help visualize what's learned

* Structure: Encoder - (Attention - Decoder)
    * Regular RNN encoder-decoder: "decoder’s hidden state is computed with a context vector, the previous output and the previous hidden state." [3]
    * RNN+attention encoder-decoder: "use not a single context vector c, but a separate context vector $c_i$ for each target word." [3]

* How it works:
    * "Each decoder output word $y_t$ depends on a weighted combination of all the input states, not just the last state." [2]
    * Weights are computed by an alignment model (such as MLP) [3]
    * "if $\alpha_{3,2}$ is a large number, [...] the decoder pays a lot of attention to the second state in the source sentence while producing the third word of the target sentence." [2]
    * Attention weights $\alpha$: **softmax**, should sum to 1 and are trained end-to-end for each timestep [1]

* Alternative interpretation: "attention mechanism is simply giving the network access to its *internal memory*, which is the hidden state of the encoder." [2]

* How to merge the output of the last unit $y_(t-1)$ and the new attention context $c_t$?
    * Depends on programmer: sum, concatenate, addition of new set of weights

* The cost of attention [2]: counter-intuitive, unlike humans, "essentially looks at everything in detail before deciding what to focus on"

* Soft vs Hard attention [4]: different regions, deterministic vs one region, stochastic
* Implementations: [Google’s Tensorflow](https://github.com/google/seq2seq) and [IBM’s PyTorch](https://github.com/IBM/pytorch-seq2seq).

* Extensions:
    * [Two-way attention](https://arxiv.org/abs/1509.06664) (2015): source to target and target to source attention, helpful in hypothesis-premise scnarios
    * [Coattention](https://arxiv.org/abs/1611.01604) (2016): "computed as an alignment matrix on all pairs of context and query words"
    * [Self-attention](https://arxiv.org/abs/1706.03762) (2017)
    * [Key-Value(-Predict) attention](https://arxiv.org/abs/1702.04521) (2017): "model outputs 3 vectors at each time step - 1st is used to encode the next-word distribution, 2nd serves as key to compute the attention vector, and 3rd as value for an attention mechanism."
    * [Hierarchical attention](http://www.aclweb.org/anthology/N16-1174) (2016): sentence and word level attention, [word and character level](https://arxiv.org/abs/1707.00896)
    * [Nested attention](https://arxiv.org/abs/1607.04423) (2016): attention-over-attention, importance of attention
    * [Attention flow](https://arxiv.org/abs/1611.01603) (2016): "reduce information loss caused by early summarization"


### References
* [1] [C5W3L08 Attention Model](https://www.youtube.com/watch?v=quoGRI-1l0A) by Andrew Ng, DeepLearning.ai (Feb 2018)
* [2] [Attention and Memory in Deep Learning and NLP](http://www.wildml.com/2016/01/attention-and-memory-in-deep-learning-and-nlp/) by Denny Britz, WildML (Jan 2016)
* [3] [Attention in NLP](https://medium.com/@joealato/attention-in-nlp-734c6fa9d983) by Kate Loginova (Jun 2018): covers attention, self-attention, two-way attention, key-value-predict models and hierarchical attention.
* [4] [Attention in Neural Networks](https://www.youtube.com/watch?v=W2rWgXJBZhU) by CodeEmporium (Mar 2018)
* [5] [Attention and Augmented Recurrent Neural Networks](https://distill.pub/2016/augmented-rnns/) by Olah & Carter, Google Brain, Distill (2016): interactive visualization
* [6] [Understanding and Applying Self-Attention for NLP](https://www.youtube.com/watch?v=OYygPG4d9H0) by Ivan Bilan (PyData Berlin, Aug 2018)
