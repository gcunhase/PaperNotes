## [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
Ashish Vaswani et al., 6 Dec 2017 version, Google Brain, NIPS 2017

TLDR; It's possible to do sequence translation solely with attention.

### Key Points
* Self-attention
    * Intra-attention, computes a representation of a sequence by relating different positions of that sequence. [1]
    * In other words, it compares each word to each other to obtain their similarity
    
* Transformer
    * "First transduction model relying entirely on self-attention to compute representations of its input and output without using sequence aligned RNNs or convolution." [1]
    <p align="center">
    <img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/selfattention_model.png" width="700" alt="Transformer model">
    </p>
    
    * Positional encoding
        * Responsible for the sequence encoding
        * If you use typical positional embedding techniques, the maximum length of the sentence is fixed/limited
        * But if you do *encoding based on waves (sin and cos)* there's no limit to that length
        <p align="center">
        <img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/selfattention_sinecos.png" width="400" alt="Sine and cos encoding">
        </p>
        <p align="center">
        <img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/selfattention_encoding.png" width="400" alt="Transformer Encoding">
        </p>
        
    * Scaled dot-product attention
        * Matrices
            * Q: what the network is looking for, words, encoding
            * K, V: memory
                * Each key K is associated with a value V, think of K as being a vector of norm V [5]
                * K is used for indexing, contains similarity weights
        * Indexing scheme
            * Use queries Q to extract output using available information (V-K pair)
            * Selects most important value based on distribution (softmax) obtained from dot product <K, Q>
        * How it works
            * Add embedded input (dim 512) with positional embedding (same shape as input)
            * Apply compatibility function (attention function)
            * Scale (normalize): division by square root of $d_k$
            * Masking: used in decoder to prevent leftward information flow in order to preserve auto-regressive property 
            * Obtain probability distribution of similarities (softmax) so 1 key is selected
            * $z$ vector: continuous representation, similar to an RNN sentence embedding, but without using an RNN        
        * Separate matrices help comparing words faster
        <p align="center">
        <img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/selfattention_singleattention.png" height="200" alt="Single attention"  hspace="20">
        <img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/selfattention_singleattention2.png" height="200" alt="Single attention">
        </p>        
        <p align="center">
        <img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/selfattention_singleattention3.png" width="350" alt="Single attention"">
        </p>

    * Multi-head attention
        * Single attention performed $h$ times: spliced single-attention
        * Allows the model to learn important information over different embeddings at different positions     
        <p align="center">
        <img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/selfattention_multihead.png" width="350" alt="Multi-head attention"  hspace="20">
        </p>
          
    * Encoder:
        * Builds (key, value) pairs
        * K, V and Q comes from the output of the previous layer
    
    * Decoder
        * Builds queries
        * Masked attention: "Self-attention layers in the decoder allow each position in the decoder to attend to all positions in the decoder up to and including that position."
        * Has an extra multi-head attention layer to combine the source sentence (V, K) with the target sentence produced so far (Q)
            * Uses $z$ vector to generate output, one element at a time
            * Combines the source sentence (V, K) with the target sentence produced so far (Q)
            * Q: comes from the previous decoder layer
            * V, K: come from the output of the encoder
        
    * Add and norm: add information from residual connection and perform layer normalization
    * Position-wise feed forward network: two linear transformations (convolution with kernel size 1) + ReLU activation in between
   
### Notes
* Issues with implementation [3]
    * A lot of details, constants
    * Can't train it the usual way, needs learning rate warm-up
        * Start training with lr 0 and increase it gradually over 4,000 epochs and then start decaying it
        * Trained over 300,000 epochs
    * Don't start from scratch
        * [tensor2tensor](https://github.com/tensorflow/tensor2tensor), [Tensorflow](https://gist.github.com/tokestermw/eaa08f0637343ce55b022d9c5c73b872)
        * [PyTorch](https://github.com/jadore801120/attention-is-all-you-need-pytorch)

* Relation Extraction with Self-Attention Encoder [3] [[arXiv](https://arxiv.org/pdf/1807.03052.pdf)]
    * Modification of Transformer: self-attention encoder + position aware attention layer (from Stanford)
    * Trial and error for the new modifications: one residual connection, relative position encoding, random relu instead of relu, batch normalization instead of layer normalization
    * Less training needed (60 epochs, 1 hour for good results), new SoTA by 0.1-1%
    * [PyTorch](https://github.com/ivan-bilan/tac-self-attention)
    
### Results
* Tasks applied: English to German and French translations
    * German: SoTA by +2.0 BLEU, 28.4
    * French: SoTA 41.0
* Training: 3.5 days (300,000 steps) on 8 NVIDIA P100 GPUs

### References
* [1] [The Annotated Transformer Guide](http://nlp.seas.harvard.edu/2018/04/03/attention.html): with code explanation, sine and cos curves figure
* [2] [Attention is all you need attentional neural network models](https://www.youtube.com/watch?v=rBCqOTEfxvg) by Lukasz Kaiser (Co-author of original paper, PiSchool, Oct 2017)
* [3] [Understanding and Applying Self-Attention for NLP](https://www.youtube.com/watch?v=OYygPG4d9H0) by Ivan Bilan (PyData Berlin, Aug 2018): images obtained here
* [4] [Self-Attention Mechanisms in Natural Language Processing](https://dzone.com/articles/self-attention-mechanisms-in-natural-language-proc) by Leona Zhang (Sep 2018)
* [5] [Attention is All You Need](https://www.youtube.com/watch?v=iDulhoQ2pro) by Yannic Kilcher (Nov 2017): good explanation about scaled dot-product attention
