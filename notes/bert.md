## [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)
 et al., Oct 2018 version, 

TLDR; Bidirectional transformer 

### Key Points
* Bidirectional Encoder Representations from Transformers
      
* Motivation: initialization (pre-trained knowledge is in embeddings, everything else is 'from zero', needs large training set)

* Successor to [ELMo](https://arxiv.org/abs/1802.05365): "concatenation of independently trained left-to-right and right-to-left LSTM"
* BERT is based on OpenAI's [Transformer model](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf):
    * Left-to-right transformer
    * Based on [Google's Transformer](https://github.com/gcunhase/PaperNotes/blob/master/notes/attentionisallyouneed.md)
    * Authors demonstrate gains in performance by *pre-training* the model with general data (i.e. Wiki data) followed by additional *training on specific data* (i.e. movie reviews) and then followed by a discriminative *fine-tuning on a specific task* (i.e. sentiment analysis on movie reviews)
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/bert_architecture.png" width="500" alt="BERT">
</p>

* Pre-training tasks
    * Masked Language Model (MLM):
        * Problem trying to solve: "standard conditional language models can only be trained left-to-right or right-to-left, since bidirectional conditioning would allow each word to indirectly “see itself” in a multi-layered context"
        * Used during *pre-training* to train a deep bidirectional representation
        * Randomly masks 15% of the input tokens and then tries to predict only those masked tokens (*Cloze task*)
        * Downsides
            * Mismatch between pre-training and fine-tuning. The solution is to not always substitute the masked token by a prediction. 
            * 15% of words are predicted in each batch -> longer converging time but increased performance makes it worth it            
    * Next Sentence Prediction:
        * Initial pre-trained language model is unable to understand relationships between sentences
        * Solution: pre-training of "binarized next sentence prediction task that can be trivially generated from any monolingual corpus"
        * What??? read paper in more detail

* Huge model architecture
    * 24 transformer blocks, 1024 hidden layers, 16 heads, 340M parameters
    * Training: 40 epochs, 3.3 billion word corpus, 16 TPUs 
    * 40-70 days on 8 GPUs

### Notes / Questions
* Byte-pair encoding:
    * Built upon character encoding
    * *SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing*: [paper](https://arxiv.org/abs/1808.06226), [code](https://github.com/google/sentencepiece)

### Results
* Codes:
    * [Tensorflow](http://goo.gl/language/bert)
    * [PyTorch](https://github.com/huggingface/pytorch-pretrained-BERT) -> [My PyTorch Colab Notebook for Cloze Task](https://colab.research.google.com/drive/1q2n3siETypCOCLDH6AR3AXsE76alb9-d) (How to train BERT for translation tasks???)
* SoTA in 11 NLP tasks, for example:
    * GLUE benchmark: 80.4% (+7.6%)
    * MultiNLI: 86.7% (+5.6%)
    * SQuAD v1.1 (Test F1): 93.2% (+1.5)

### References
* [1] [Language Learning with BERT](https://www.youtube.com/watch?v=0EtD5ybnh_s) by Martin Andrews (Tensorflow and Deep Learning Singapore, Nov 2018)
* [2] [Synced Blog](https://syncedreview.com/2018/10/16/best-nlp-model-ever-google-bert-sets-new-standards-in-11-language-tasks/): highlights from paper
