## [NLP's ImageNet moment has arrived](http://ruder.io/nlp-imagenet/)
Sebastian Ruder, Jul 2018

TLDR; Blog post about how ULMFiT, ELMo and OpenAI's Transformer are the ImageNet of NLP and how it's only a matter of time until researchers start downloading pretrained language models instead of word embeddings. 

### ImageNet
* ImageNet: sufficiently large and representative of the problem

* ImageNet Large Scale Visual Recognition Challenge (ILSVRC)
    * 2012: deep neural network submitted by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton performed 41% better than the next best competitor
    * Importance:
        * Demonstrated that "deep learning was a viable strategy for machine learning and arguably triggering the explosion of deep learning in ML research"
        * Transfer learning via pretraining on ImageNet: networks can be fine-tuned for tasks it wasn't trained for

### Up-to-now NLP
* Word2Vec: shallow representation of data
* Equivalent to modeling just edges in images, not giving attention to other properties such as pattern, structures, objects...

### New NLP
* Embeddings from Language Models (ELMo), Universal Language Model Fine-tuning (ULMFiT), and OpenAI Transformer
* ULMFit, ELMo, OpenAI key paradigm shift: "going from just initializing the first layer of our models to pretraining the entire model with hierarchical representations"
* "The success of ImageNet highlighted that in the era of deep learning, data was at least as important as algorithms."
* Limitations: 
    * Proxy to true language understanding, and a single network can't capture all features to model all tasks
    * Language model can only capture what they have seen
    * External information might be required for some tasks 
* Open question: "How to transfer the information from a pre-trained language model to a downstream task?"
    * ULMFit: Fine-tune
    * ELMo: "use the pre-trained language model as a fixed feature extractor and incorporate its representation as features into a randomly initialized model"

### Datasets

| Task | Explanation | Dataset |
| ---- | ----------- | ------- |
| Reading comprehension | *Answering a natural language question about a paragraph* | Stanford Question Answering Dataset (SQuAD) |
| Natural language inference | *Identifying the relation (entailment, contradiction, and neutral) that holds between a piece of text and a hypothesis* | Stanford Natural Language Inference (SNLI) Corpus |
| Machine Translation | *Translating text in one language to text in another language* | WMT |
| Constituency parsing | *extract syntactic structure of sentence into a parsing tree* | WSJ, OntoNotes, English Web Treebank, Question Treebank |
| Language Modeling | *predict the next word given its previous word* | 1 Billion Word Language Model Benchmark |
> Check out [GLUE Benchmark](https://gluebenchmark.com/) for more Natural Language Understanding tasks
