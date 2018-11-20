## [Read + Verify: Machine Reading Comprehension with Unanswerable Questions](https://arxiv.org/abs/1808.05759)
Minghao Hu et al., Submitted on 17 Aug 2018

TLDR; Proposes a read-then-verify system to validate the answerability of a question by verifying the legitimacy of a predicted answer instead of simply answering with the most likely answer.

### Key Points
* **Task**: "Given a context passage and a question, the machine needs to not only find answers to answerable questions but also detect unanswerable cases."
* Model should abstain from answering when no answer can be inferred
* **Novelty**: previous works "fail to validate the answerability of the question by verifying the legitimacy of the predicted answer"
  * Answerability: whether the question has an answer
  * Legitimacy: whether the extracted text can be supported by the passage and the question
  * "Human [...] tends to first find a plausible answer given a question, and then checks if there exists any contra- dictory semantics."
* "To deal with unanswerable cases, systems must learn to identify a wide range of linguistic phenomena such as negation, antonymy and entity changes between the passage and the question."
* 2 independent losses: span (concentrates on answer extraction) and no-answer (prediction on no-answer detection) loss
  * $L = L_{join} + \game * L_{span} + \delta * L_{noanswer}$
* Answer Verifier:
  * Model 1: Sequential architecture using a [multi-layer Transformer decoder](https://arxiv.org/abs/1801.10198) (Google, ICLR 2018)
  * Model 2: Interactive architecture 
  * Model 3: Hybrid
  
### Notes / Questions
* Machine Reading Comprehension datasets:
  * Deepmind's [*Teaching machines to read and comprehend*](https://papers.nips.cc/paper/5945-teaching-machines-to-read-and-comprehend) (NIPS 2015, Hermann et al.), CNN/Daily Mail dataset [[dataset](https://github.com/deepmind/rc-data/)]
  * Microsoft Bing's [*MS MARCO datase*t](https://arxiv.org/abs/1611.09268) (NIPS 2016, Nguyen et al.), "a question in the MS MARCO dataset may have multiple answers or no answers at all" [[dataset](http://www.msmarco.org/dataset.aspx)] 
  * Allen Institute for Artificial Intelligence's [*TriviaQA*](https://arxiv.org/abs/1705.03551) (ACL 2017, Joshi)  [[dataset](http://nlp.cs.washington.edu/triviaqa/)]
  * Deepmind's [*NarrativeQA dataset*](https://arxiv.org/abs/1712.07040) (ACL 2018, Kocisky), "questions created by editors based on summaries of movie scripts and books" [[dataset](https://github.com/deepmind/narrativeqa)]

<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/MRC_datasets_narrativeqa.png" width="500" alt="MRC Datasets">
</p>

<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/MRC_datasets_msmarco.png" width="400" alt="MRC Datasets 2">
</p>

* [Must-read papers on Machine Reading Comprehension](https://github.com/thunlp/RCPapers)

### Results
* SQuAD (Stanford Question Answering Dataset) 2.0 dataset
* Achieves SOTA results: 74.2 F1 performance
