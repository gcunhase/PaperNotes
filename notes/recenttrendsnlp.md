## [Recent Trends in Deep Learning Based Natural Language Processing](https://arxiv.org/abs/1708.02709)
Tom Young et al., 10 Oct 2018 version

TLDR; This paper covers a little bit of history and the most popular deep learning methods in NLP research today.

### Key Points
* "Deep learning enables multi-level automatic feature representation learning" instead of hand-crafted features that are time-consuming and often incomplete.

#### Distributed representation
* Important due to the curse of dimensionality when learning joint probability functions of language models.
* Word embeddings
    * Distributional hypothesis: "words with similar meanings tend to occur in similar context"
    * Vectors exhibit compositionality (man+royal=king)
    * Able "to capture syntactic and semantic information"
* Word2vec
    * Sentiment specific word emebedding (SSWE)
    * Limitations: inability to represent phrases, learning embeddings based only on a small window of surrounding words (*good* and *bad* might have similar embeddings, bad for sentiment analysis), highly dependent on the applications in which it is used, and unable to account for polysemy.
* Character embeddings
    * Solves unkown (UNK) or out-of-vocabulary (OOV) issue since the embedding is really only on the alphabet
* Doubt in "how well the word vectors capture the necessary facets of conceptual meaning"

#### Convolutional Neural Networks
* Extracts higher level features
* "CNNs have the ability to extract salient n-gram features from the input sentence to create an informative latent semantic representation of the sentence for downstream tasks."
* Sentence modeling (embedding matrix): "allows for modeling of complete sentences into sentence representations"
* Window approach (word-based predictions): NER, POS tagging, SRL. 
* CNNs were used in NLP for sentiment, subjectivity and question type classification, but with "many shortcomings with the CNN's inability to model long distance dependencies"
    * Requires high context information to solve this problem
    * "Denil et al. applied DCNN to map meanings of words that constitute a sentence to that of documents for summarization."
* Limitations:
    1. "Inability to model long-distance contextual information and preserving sequential order in their representations", essential for NLP tasks.
    2. Data heavy model, requiring huge training data
    
#### Recurrent Neural Networks
* The meaning of a word depends on its surrounding words (context): "dog" vs "hot dog"
* Advantages:
    * Ability to process sequential information: language modeling, machine translation, speech recognition, image caption.
    * Able to model variable length of text
    * Summarization: units (characters into words, words into sentences or sentences into documents) are summarized to a fixed vector and then mapped back to a variable-length target sequence.
* DO NOT always assume RNN to be superior to other deep networks. "Recently, several works provided contrasting evidence on the superiority of CNNs over RNNs."
    * Yin et al.: there's no clear winner, "the performance of each network depends on the global semantics required by the task itself"
* RNN models: Simple RNN (vanishing/exploding gradient problem), LSTM (added input, forget and output gates), GRU (reset and update gates), ResNet.
    * LSTM and GRU perform similarly most of the time and are thus chosen heuristically depending on the application and computing power available.
* Applications: word and sentence-level classification, language generation (machine translation, image captioning with CNN-LSTM), 
* Attention Mechanism:
    * In the traditional encoder-decoder setting, "the encoder at times is forced to encode information which might not be fully relevant to the task at hand", or the input is too long or very information-rich.
    * Selective encoding
    * Decoder receives the hidden state, generated token, and a context vector "calculated based on the input hidden state sequence", allowing the decoder to refer back to the input sequence. 
   
#### Recursive Neural Networks
* Constituency parsing trees
* "The representation of each non-terminal node in a parsing tree is determined by the representations of all of its children."
* Applications: parsing

#### Deep Reinforced Models and Deep Unsupervised Learning
* Reinforcement learning
    * "Method of training an agent to perform discrete actions before obtaining a reward"
    * Problem in with training the model with word-level maximum likelihood strategy: "models, is that the training objective is different from the test metric".
    * Shortcomings: there's need "to carefully handle the state and action space" and "training the reward functions" means this approach has increased complexity.
* Unsupervised Learning
    * Skip-thought: "auxiliary task was to predict two adjacent sentences (before and after) based on the given sentence."
    * Language modeling as auxiliary task:
        i. "pre-training the sentence encoder on a large unsupervised corpus yielded better accuracy than only pre-training word embeddings."
        ii. "predicting the next token turned out to be a worse auxiliary objective than reconstructing the sentence itself, as the LSTM hidden state was only responsible for a rather short-term objective."
* Generative Models
    * VAE + GAN
    * "Encoder and generator networks which encode data examples to latent representation and generate samples from the latent space"
    * "One problem with applying GAN to text is that the gradients from the discriminator cannot properly back-propagate through discrete variables."

#### Memory-Augmented Networks
* "Hidden vectors of the encoder can be seen as entries of the model’s 'internal memory'"
* Memory consists of commonsense knowledge, such as (subject, relation, object) triples
* *Hops*: multiple rounds of information retrieval from memory
* Memory module is also applicable to visual signals

### Notes / Questions
* Parsing: dependency vs constituency parsing
    * Dependency parsing: "connects individual words with their relations"
    * Constituency parsing: "iteratively breaks text into sub-phrases"
* Named-Entity Recognition (NER)
    * CoNLL 2013: people, locations, organizations and miscellaneous entities.
    * Lexicons can be very useful
* Semantic Role Labeling (SRL)
    * "aims to discover the predicate-argument structure of each predicate in a sentence"
    * CoNLL 2005&2012 datasets
* Sentiment Classification: Stanford Sentiment Treebank (SST) dataset, CMU-MOSI (multimodal setup)
* Machine Translation: reinforcement learning with BLEU score does not reflect human evaluation 
* Question Answering: SQuAD and bAbI datasets
* Dialogue Systems: generation-based vs retrieval-based models
* AI research is expected to go in the direction of making better use of unlabled data. 
* Internal memory: "bottom-up knowledge from the data"
* External memory: "top-down knowledge inherited from a KB"
