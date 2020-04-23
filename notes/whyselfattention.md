## [Why Self-Attention? A Targeted Evaluation of Neural Machine Translation Architectures](http://arxiv.org/abs/1808.08946)
Gongbo Tang et al., Nov 2018 version, EMNLP 2018

TLDR; Survey paper comparing RNNs, CNNs and Self-attention (new SoTA in MT with Transformer) models in encoder-decoder format for MT tasks, specifically subject-verb agreement (long-range dependencies) and word sense disambiguation (semantic features). Their conclusion is that Transformers are strong feature extractors and that the number of heads in the transformer affects their ability to model long-range dependency, but they do not outperform RNN in this aspect.

### Contributions
* Empirically testing of long-range dependency strength with subject-verb agreement task -> no evidence that Transformers or CNNs are better than RNNs in this regard
* Empirically shows that the number of attention heads in Transformer impact its ability to capture long-distance dependencies
* Empirically shows that Transformers excel at word sense disambiguation (WSD) task -> strong semantic feature extractors

### Key Points
* Paper motivation:
    * Transformer achieved SoTA in many MT tasks according to BLEU score.
    * But is BLEU score that reliable?
        * Coarse-grained, not refined
        * "Offers no insight as to which aspects of translation are improved by different architectures"    
        * "Does not correlate well with the targeted evaluation of long-range distance interactions." -> "due to the locality of BLEU, which only measures on the level of n- grams"
    
* Statement: CNNs and self-attention models outperformed RNNs in NMT tasks

* Hypothesis 1 (Transformer authors):
    * CNNs and self-attention networks are better than RNNs at modeling **long-range dependency** due to shorter connecting path between co-dependent elements
        * Based on theoretical argument, not empirically tested (this paper aims to test it)
    * Task used for testing: **subject-verb agreement**
    * Conclusion: self-attentional networks and CNNs do not outperform RNNs

* Hypothesis 2 (paper authors):
    * CNNs and self-attention networks are able to better "**extract semantic features** from the source text"
    * Task used for testing: **word sense disambiguation** (WSD, semantic feature extraction is required)
    * Conclusion: self-attention >> RNNs and CNNs

### Notes
* RNN:
    * Models variable-length input, GRUs and LSTMs for long-range dependency modelling
    * Sequentially encodes sentences, updating its hidden state at every timestep
    
* CNN:
    * Parallelization, CNN Encoder-Decoder outperforms RNN-based NMT models (Gehring et al., 2017)
    * "Summarizes fixed size context through multiple layers"
    * ConvS2S: needs positional embedding for sequence modelling, use of GLU
    
* Self-attention:
    * Transformer built solely with attention layers (Vaswani et al., 2017)
    * Summarizes all context by comparing each word to every word in the sentence -> Any 2 tokens are connected directly
    * Also needs positional encoding

* Related works:
    * Yin at al. (2017): CNNs are better than LSTMs and GRUs at tasks related to semantics, while RNNs are better at syntax-related tasks
    * Bernardy and Lappin (2017): RNNs perform better than CNNs on a subject-verb agreement task
    * Tran et al. (2018): Transformer performs worse than an RNN language model on a subject-verb agreement task, gets worse as the distance between subject and verb grows
    * Tang et al. (2018): Transformer surpasses RNN models only in high-resource conditions in the historical to modern spelling translation task
    
### Experiments
* Training:
    * [Sockeye toolkit](https://github.com/awslabs/sockeye/tree/acl18)
    * 2 GPUs
    * Training data: [WMT'17](http://www.statmt.org/wmt17/translation-task.html)
    * Validation set: *newstest2013*
    * Test set: *newstest2014* and *newstest2017*
    * Eval: [Sacre-BLEU](https://arxiv.org/abs/1804.08771) (WMT18)
    
* Doesn't compare with *fairseq*, but uses pre-trained model trained with *fairseq* in the post-publication experiments section
    
* Contrastive testing: 
    * "Contrastive evaluation tests the sensitivity of NMT models to specific translation errors"
    * Lingeval97 (Sennrich, 2017): 35,105 instances of EN-DE subject-verb agreement
    * [Europarl](http://opus.nlpl.eu/Europarl.php) and [ContraWSD](http://data.statmt.org/ContraWSD/) (Rios et al., 2017): 7,200 DE-EN and 6,700 DE-FR lexical ambiguities

* TransRNN (Transformer encoder + RNN decoder)
    * Chen et al. (2018): TransRNN outperforms a pure Transformer -> Transformer is better at encoding features and RNN is better at conditional language modeling
    * This paper: WSD task -> TransRNN outperforms RNNS2S but not pure Transformer, indicating that "WSD is not only done in the encoder, but that the decoder also affects WSD performance"

* P.S.: WikiText-103 (dataset with longer-term dependencies), CNN/DailyMail (long input and output sentences)