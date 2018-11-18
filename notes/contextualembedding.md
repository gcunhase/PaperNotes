## [Using sparse semantic embeddings learned from multimodal text and image data to model human conceptual knowledge](https://arxiv.org/abs/1809.02534)
Steven Derby et al., Submitted on 7 Sep 2018

TLDR; Producing sparse, interpretable representation vectors from multimodal information (text and image) using JNNSE

### Key Points
* Novelty: produces sparse, interpretable representation vectors from multimodal information (text and image) using Joint Non-Negative Sparse Embedding (JNNSE, Fyshe et al., 2014)

* Sparse = interpretability (NNSE)

* JNNSE produces sparse multimodal distribution from text and image data, extended NNSE which incorporates other sources of semantic information

* "one aspect of cognitive plausibility that is lacking in dense representations is in their interpretability, something that could be solved using sparsity"

* Multimodal model: concat(0.5 * TextEmbedding, 0.5 * ImageEmbedding)

### Notes / Questions
* Semantics: "neurocognitive research suggests that semantics is deeply linked to both language and perception"
* Non-Negative Sparse Embedding code was provided by Partha Talukdar and JNNSE was provided by Alona Fyshe (no links provided)

### Results
* The authors "show that these models attain a structural composition and semantic representation that is closer to the way humans represent concepts, evaluated using human similarity judgements, human semantic feature knowledge, and neuroimaging data"
* Semantic similarity evaluation benchmarks: WordSim353 (2001), MEN (2012), SimLex999 (2015)
* Average cross-validation F1 ×100 scores for each model
* Evaluation on brain data (fMRI and MEG): BrainBench (2016)
