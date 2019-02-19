## [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)
Jacob Devlin et al., Oct 2018 version, Google AI Language

TLDR; Trained bidirectional transformer encoder, with the main appeal being that it is a very well trained language model (prediction on masked word), so that to use it for other downstream tasks all one needs to do is fine-tune it.

### Key Points
* Bidirectional Encoder Representations from Transformers
      
* Motivation: initialization (pre-trained knowledge is in embeddings, everything else is 'from zero', needs large training set)

* Successor to [ELMo](https://arxiv.org/abs/1802.05365) with contextualized word embedding and [ULMFit](https://arxiv.org/pdf/1801.06146.pdf) with transfer learning
    * Issues: ELMo is bidirectional but OpenAI's Transformer trains a forward language model
    
* BERT is based on OpenAI's [Transformer model](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf):
    * Stack of transformer blocks (encoder) + FFN
    * Left-to-right transformer
    * Based on [Google's Transformer](https://github.com/gcunhase/PaperNotes/blob/master/notes/attentionisallyouneed.md)
    * Authors demonstrate gains in performance by *pre-training* the model with general data (i.e. Wiki data) followed by additional *training on specific data* (i.e. movie reviews) and then followed by a discriminative *fine-tuning on a specific task* (i.e. sentiment analysis on movie reviews)
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/bert_architecture.png" width="500" alt="BERT">
</p>

* Pre-training tasks
    * Masked Language Model (MLM):
        * Uses the output of the masked words position to predict the masked word [5]
        * Problem trying to solve: "standard conditional language models can only be trained left-to-right or right-to-left, since bidirectional conditioning would allow each word to indirectly “see itself” in a multi-layered context"
        * Used during *pre-training* to train a deep bidirectional representation
        * Randomly masks 15% of the input tokens and then tries to predict only those masked tokens (*Cloze task*)
        * Downsides
            * Mismatch between pre-training and fine-tuning. The solution is to not always substitute the masked token by a prediction. 
            * 15% of words are predicted in each batch -> longer converging time but increased performance makes it worth it            
    * Next Sentence Prediction:
        * Predicts likelihood that sentence B belongs after A [5]
        * Initial pre-trained language model is unable to understand relationships between sentences
        * Solution: pre-training of "binarized next sentence prediction task that can be trivially generated from any monolingual corpus"
        
* BERT used for different tasks
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/bert_tasks.png" width="400" alt="BERT tasks">
</p>

### Notes / Questions
* *[CLS]*: first input token, stands for Classification

* Downstream tasks: "supervised-learning tasks that utilize a pre-trained model or component"

* Byte-pair encoding:
    * Built upon character encoding
    * *SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing*: [paper](https://arxiv.org/abs/1808.06226), [code](https://github.com/google/sentencepiece)

* BERT uses WordPiece (chunks of words) as tokens rather than words

* Training on specific tasks: [5]
    1. Semi-supervised learning: BERT learns huge dataset (Wikipedia for example)
    2. Supervised training on specific task (fine-tuning): i.e. text classification (BERT+FFN+Softmax)
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/bert_train_steps.png" width="700" alt="BERT train steps">
</p>
     
* Original transformer: 6 encoder layers, 512 hidden units in FNN, and 8 attention heads
   
* 2 BERT models:
    * Base: Comparable in size to the OpenAI Transformer
        * 12 transformer blocks (encoder layers), 768 hidden units (FFN), 12 attention heads
    * Large: Huge model which achieves SoTA in 11 tasks
        * 24 transformer blocks (encoder layers), 1024 hidden units (FFN), 16 attention heads, 340M parameters
        * Training: 40 epochs, 3.3 billion word corpus, 16 TPUs 
        * 40-70 days on 8 GPUs

* Maximum length of words: 512, not suitable to handle long text such as news articles

* BERT works better on sentences than words, so it wouldn't be as good for spelling error correction ([link](https://www.reddit.com/r/MachineLearning/comments/9vpue6/r_bert_explained_state_of_the_art_language_model/))
 
### Results
* Codes:
    * [Tensorflow](http://goo.gl/language/bert)
    * [PyTorch](https://github.com/huggingface/pytorch-pretrained-BERT)
        * [My PyTorch Colab Notebook for Cloze Task](https://colab.research.google.com/drive/1q2n3siETypCOCLDH6AR3AXsE76alb9-d)
        * Training BERT for sentence classification
        * Check article in [6]

* SoTA in 11 NLP tasks, for example:
    * GLUE benchmark: 80.4% (+7.6%)
    * MultiNLI: 86.7% (+5.6%)
    * SQuAD v1.1 (Test F1): 93.2% (+1.5)

### References
* [1] [Language Learning with BERT](https://www.youtube.com/watch?v=0EtD5ybnh_s) by Martin Andrews (Tensorflow and Deep Learning Singapore, Nov 2018)
* [2] [Synced Blog](https://syncedreview.com/2018/10/16/best-nlp-model-ever-google-bert-sets-new-standards-in-11-language-tasks/): highlights from paper
* [3] Dissecting BERT: [Encoder](https://medium.com/@mromerocalvo/dissecting-bert-part1-6dcf5360b07f) and [Decoder](https://medium.com/dissecting-bert/dissecting-bert-appendix-the-decoder-3b86f66b0e5f)
* [4] [BERT explained](https://towardsdatascience.com/bert-explained-state-of-the-art-language-model-for-nlp-f8b21a9b6270)
* **[5]** [The Illustrated BERT, ELMo, and co](http://jalammar.github.io/illustrated-bert/) by Jay Alammar: very easy to follow explanation on BERT, source for the second image used here
* [6] [Hallo multilingual BERT, como funcionas?](https://medium.com/omnius/hallo-multilingual-bert-c%C3%B3mo-funcionas-2b3406cc4dc2): using HuggingFace's PyTorch code for German language
* [7] Using BERT for classification: [Fine-tuning Sentence Pair Classification with BERT](https://gluon-nlp.mxnet.io/examples/sentence_embedding/bert.html), [Adding classifier after encoder](https://github.com/google-research/bert/issues/253)
