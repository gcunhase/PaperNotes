## [Learning to Discriminate Noises for Incorporating External Information in Neural Machine Translation](https://arxiv.org/abs/1810.10317)
Zaixiang Zheng et al., Submitted on 24 Oct 2018

TLDR; Authors propose a framework to tackle the noise problem for diverse scenarios of external information.

### Key Points
* 2 kinds of noise
  * **global**: "Words in the external words that are generally irrelevant to the translations of the words of the whole sentence"
  * **local**: "words in the external words that are irrelevant to the translation of a specific (current) word"
* 3 different external information: *human* interactice suggestions, *dictionary translation* of word, translation from Statistic Machine Translation (*SMT*)
* External information could come from a machine translation model, lexical table of an SMT system, wor-dbased translation from a bilingual dictionary, BoW of target sentence, ...
* Novelty:
  * Uses general form of external information
  * Training is simpler: "only uses word sampling from the original parallel data and requires no external resources"
* Reading-fusion framework
  * Way to copy the external word $y^E_j$ as the next generated word
  * Pointer Networks + Copying Mechanism
  * Reading: attention between concatenation of decoding state $s_t$ and source context $c_t$ and the embedding of each external words.
  * Fusion: scalar fusion gate $\beta_t$ is used to determine the relevance between the external content $c^E_t$ and the translation at the current time step.
* Discriminating the Noise in External Words
  * Before decoding: "supervised global word discriminator is designed to determine whether each given external words is relevant to the current translation"
  * During decoding (reading stage): "attention mechanism is performed to select the correct external words or an extra <null> token"
  * During fusion stage: "supervised local word discriminator decides whether to use the obtained information for the translation of current word"
  
### Notes / Questions
* External information doesn't have to be in a sequence, which is assumed to be arbitrary
* Construct a self-generated synthetic dataset of external words $D_2$

### Results
* Case- insensitive BLEU
* Chinese-to-English (LDC, 1.6M sentences) and English-to-German (WMT17, 5.6M sentence pairs)
