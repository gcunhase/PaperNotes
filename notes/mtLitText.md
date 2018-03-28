## [What Level of Quality can Neural Machine Translation Attain on Literary Text?](https://arxiv.org/abs/1801.04962)
Antonio Toral and Andy Way, Submitted on 15 Jan 2018

TLDR; The authors present a literary-adpated NMT system applied to novels (literary text) in the English-Catalan language domain.

### Key Points
* Literary text: greatest challenge for Machine Translation (MT)
* Neural (Attention-based encoder-decoder) vs Phrase-based Statistical MT (PBSMT) 
* Recent emergence of two unrelated technologies opens a window of opportunity to explore this topic:
  * E-books for building dataset
  * NMT: performance seems to be especially promising for lexically-rich texts  and there are claims that it “can, rather than do a literal translation, find the cultural equivalent in another language”.
* Previous work: Spanish-Catalan. Current: English-Catalan
* *Goal of paper*: assess the performance that can be offered by state- of-the-art MT for literary texts  
* *Dataset*: trained on large amounts of literary texts (over 100 million words) and evaluated on a set of 12 novels from the 1920s to the present day
  * In-domain vs out-of-domain: literary vs non-literary text
  * Parallel: same text in both English and Catalan
  * Monolingual: text in either only English or Catalan

### Notes / Questions
* State-of-the-Art in MT of Literary Text

### Results
* BLEU score: NMT is significantly better than PBSMT (3-14% improvement)
* BLEU score
  * PBSMT model: 0.3473  
  * NMT Model:
    * Ensemble of 4 attention-based encoder-decoder (0.3561)
    * 2 additional functionalities: use of subwords instead of words (0.3689) and right-to-left NMT (0.3948)
* Evaluation:
  * NMT always better than PBSMT    
  * Improvement varies widely (from 3% to up to 14%)
* Analysis:
  * Lexical richness: type-token ration (TTR) measure. The higher the ratio, the less repetitive the text and hence it can be considered lexically more varied, and thus richer.
    * Novel that only had 3% improvement had the longest average sentence length
  * Sentence length: *the relative improvement of NMT over PBSMT decreases with sentence length*
  * Novelty of data between test and training set: n-gram overlap.
* Human evaluation:
  * 1 source-language sentence and 3 translated sentences (human translation, PBSMT and NMT translations)
  * Annotators perceive the NMT translations to be of equivalent quality to the human translation more often than PBSMT's
