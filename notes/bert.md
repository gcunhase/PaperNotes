## [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)
Jacob Devlin et al., Oct 2018 version, Google AI Language

TLDR; Trained bidirectional transformer encoder, with the main appeal being that it is a very well trained language model (prediction on masked word), so that to use it for other downstream tasks all one needs to do is fine-tune it.

[Key Points](#key-points) • [Embedding](#notes-on-bert's-embedding-layers) • [Notes](#notes-/-questions) • [Results](#results) • [References](#references) 

### Key Points
* Bidirectional Encoder Representations from Transformers
    * Reads the entire sequence of words at once, therefore considered bidirectional (more accurate to say non-directional) [4]
    
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

* Training on specific tasks: [5]
    1. Semi-supervised learning: BERT learns huge dataset (Wikipedia for example)
    2. Supervised training on specific task (fine-tuning): i.e. text classification (BERT+FFN+Softmax)
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/bert_training_steps.png" width="600" alt="BERT train steps">
</p>

* Pre-training tasks
    * "When training language models, there is a challenge of defining a prediction goal" [4]
        * "The child came home from ___"
        * Predicting the next word in a sequence limits context learning
        * BERT uses the following 2 strategies to solve this
    * Masked Language Model (MLM):
        * Learns masked words in random places in sentence, not just next word
        * Uses the output of the masked words position to predict the masked word [5]
        * Problem trying to solve: "standard conditional language models can only be trained left-to-right or right-to-left, since bidirectional conditioning would allow each word to indirectly “see itself” in a multi-layered context"
        * Used during *pre-training* to train a deep bidirectional representation
        * Randomly masks 15% of the input tokens and then tries to predict only those masked tokens (*Cloze task*)
        * Downsides
            * Mismatch between pre-training and fine-tuning. The solution is to not always substitute the masked token by a prediction. 
            * 15% of words are predicted in each batch -> longer converging time but increased performance makes it worth it            
    * Next Sentence Prediction (NSP):
        * Predicts likelihood that sentence B belongs after A [5]
        * Initial pre-trained language model is unable to understand relationships between sentences
        * Solution: pre-training of "binarized next sentence prediction task that can be trivially generated from any monolingual corpus"
    * Adding MLM and NSP make the training slower but it greatly increases context awareness
            
* BERT used for different tasks
<p align="center">
<img src="./bert_tasks.png" width="400" alt="BERT tasks">
</p>

> Section 3.5 of paper has further details on hyper-parameter tuning

### Notes on BERT's embedding layers
> Sources: [8], [9]

<p align="center">
<img src="./imgs/bert_embedding.png" width="400" alt="BERT embedding layers steps">
</p>
    
* Input text: words in input sentence
    
* Input token: input text tokenized
    * WordPiece tokenization
    * [CLS]: first input token, stands for Classification
    * [SEP]: separate sentences
        
* Embedding layers [8]:
    * Token embedding: input token is transformed into vector representations of dimension 768
        <p align="center">
        <img src="./bert_emb_token.png" width="300" alt="BERT Token Embedding">
        </p>

    * Segment embedding: necessary in sentence similarity tasks, where 2 sentences are given as input. In cases of just 1 sentence being given the segment embedding has a mask of all zeros.
        <p align="center">
        <img src="./bert_emb_seg.png" width="300" alt="BERT Segment Embedding">
        </p>
                    
    * Positional embedding: lookup table of size (512, 768), where the max length of a sequence is 512.

* All 3 representations have shape (bs, seq_length, 768) and are summed element-wise to produce a tensor of same shape.

### Notes / Questions
* Downstream tasks: "supervised-learning tasks that utilize a pre-trained model or component"

* Byte-pair encoding:
    * Built upon character encoding
    * *SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing*: [paper](https://arxiv.org/abs/1808.06226), [code](https://github.com/google/sentencepiece)

* Original transformer: 6 encoder layers, 512 hidden units in FNN, and 8 attention heads
   
* 2 BERT models:
    * Base: Comparable in size to the OpenAI Transformer
        * 12 transformer blocks (encoder layers), 768 hidden units (FFN), 12 attention heads
        * Training: 4 Cloud TPUS for 4 days [4]
        * Usage: 1 GPU
    * Large: Huge model which achieves SoTA in 11 tasks
        * 24 transformer blocks (encoder layers), 1024 hidden units (FFN), 16 attention heads, 340M parameters
        * Training: 40 epochs, 3.3 billion word corpus, 16 Cloud TPUs for 4 days 
        * Training on GPU: 40-70 days on 8 GPUs
        * Usage: 1 TPU

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
* [3] [Dissecting BERT Encoder](https://medium.com/@mromerocalvo/dissecting-bert-part1-6dcf5360b07f) by Francisco Ingham and Miguel Romero: really good source for complete details about the Transformer encoder
* [4] [BERT explained](https://towardsdatascience.com/bert-explained-state-of-the-art-language-model-for-nlp-f8b21a9b6270) by Rani Horev: interesting BERT explanation and how to use for fine-tuning, takeaways section, Devlin's insight on Word Masking
* **[5]** [The Illustrated BERT, ELMo, and co](http://jalammar.github.io/illustrated-bert/) by Jay Alammar: very easy to follow explanation on BERT, source for the second image used here
* [6] [Hallo multilingual BERT, como funcionas?](https://medium.com/omnius/hallo-multilingual-bert-c%C3%B3mo-funcionas-2b3406cc4dc2) by Marianne Stecklina: using HuggingFace's PyTorch code for German language, exploring multi-language BERT vocabulary
* [7] [Fine-tuning Sentence Pair Classification with BERT](https://gluon-nlp.mxnet.io/examples/sentence_embedding/bert.html) and [Adding classifier after encoder](https://github.com/google-research/bert/issues/253): details on using BERT for classification
* [8] [How the Embedding Layers in BERT Were Implemented](https://medium.com/@_init_/why-bert-has-3-embedding-layers-and-their-implementation-details-9c261108e28a) (Feb 2019): Bert embedding
* [9] [Bert-embedding’s documentation](https://bert-embedding.readthedocs.io/en/latest/) (2019): MXNet implementation to obtain BERT's embeddings for use in other projects
