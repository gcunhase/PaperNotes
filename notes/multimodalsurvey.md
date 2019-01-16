## [Multimodal Machine Learning: A Survey and Taxonomy](https://arxiv.org/abs/1705.09406)
Tadas Baltrusaitis, Chaitanya Ahuja, and Louis-Philippe Morency, 1 Aug 2017, Carnegie Mellon University, IEEE PAMI

TLDR; Survey paper for research in the field of Multimodal Machine Learning, deemed necessary for AI to better understand the world around us

### Definitions
* Modality: "refers to the way in which something happens or is experienced"
* Multimodal Research: "it includes multiple such modalities"
* Taxonomy: scheme of classification
* AVSR: Audio-Visual Speech Recognition

### Key Points
* Authors **propose** new vocabulary (taxonomy) for multimodality research and extensive survey
* **Motivation**: necessary for AI to better understand the world around us
* **Paper focuses** on 3 modalities:
    1. Natural language: written or spoken
    2. Visual signals: images or videos
    3. Vocal signals: sounds and para-verbal information (prosody and vocal expressions)
* **5 core technical challenges**: representation (heterogeneity of the data), translation, alignment, fusion, and co-learning
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/multimodal_scheme.png" width="300" alt="Multimodal Scheme">
</p>

### Applications: A Historical Perspective
* The McGurk effect
    * [Hearing lips and seeing voices](https://www.nature.com/articles/264746a0): *"When human subjects heard the syllable /ba-ba/ while watching the lips of a person saying /ga-ga/, they perceived a third sound: /da-da/."*
    * Motivated researchers in the speech community to extend their approaches with visual information
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/multimodal_applications.png" width="500" alt="Multimodal Applications">
</p>

### 1. Multimodal Representations
* Learning how to represent and summarize heterogeneous (multimodal) data
* "A multimodal representation is a representation of data using information from multiple such entities."
* Challenges: combining heterogeneous data, different levels of noise, and missing data.
* Properties for good representation:
    * Bengio: "smoothness, temporal and spatial coherence, sparsity, and natural clustering amongst others"
    * Srivastava and Salakhutdinov: "*similarity in the representation space* should reflect the similarity of the corresponding concepts, the representation should be *easy to obtain* even in the absence of some modalities, and finally, it should be possible to *fill-in missing modalities* given the observed ones"
* Multimodal representations used to be a simple concatenation of unimodal ones
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/multimodal_representation.png" width="500" alt="Multimodal Representations">
</p>

* Joint representations:
    * "combine the unimodal signals into the same representation space"
    * same dimensions -> x_m = f(x_1, ..., x_n)
    * Simplest case: early fusion, or concatenation of individual modality features
    * Neural Networks:
        * Advantages: superior performance, able to re-train the representations in an unsupervised manner
        * Disadvantages: not able to naturally handle missing data
    * Probabilistic graphical models: use of latent random variables
        * Deep Boltzmann machines: no need for supervised data for training, enabling the use of unlabeled data
        * "Multimodal DBMs are capable of learning joint representations from multiple modalities by merging two or more undirected graphs using a binary layer of hidden units on top of them."
        * Generative nature, allowing for missing data handling or to generate samples of one modality in the presence of the other one
        * Disadvantage: difficult to train - "high computational cost, and the need to use approximate variational training methods" (see Multimodal Learning with DBM, NIPS 2012, Srivastava and Salakhutdinov)
    * Sequential representation:
        * Able to represent sequences of variable length (sentences, videos, audio streams)
        * Hidden state of RNN at time *t* can be seen as a summarization of the sequence up to that timestep
* Coordinated representations:
    * Mostly limited to 2 modalities
    * "process unimodal signals separately, but enforce certain similarity constraints on them"
    * "learn separate representations for each modality but coordinate them through a constraint"
    * f(x_1) ~ g(x_2) -> "each modality has a corresponding projection function"
    * Examples: "minimizing cosine distance, maximizing correlation, and enforcing a partial order between the resulting spaces"
    * Enforces similarity between representations
        * *DeViSE: A deep visual-semantic embedding model* (Frome at al., NIPS, 2013)
        * *Unifying Visual-Semantic Embeddings with Multimodal Neural Language Models* (Kiros et al., 2014)
        * *Jointly Modeling Embedding and Translation to Bridge Video and Language* (Pan at al., CVPR, 2016)
    * Enforces additional constraints between the modality representations
        * Cross-modal hashing: same object in different modalities has to have the same has code
            * *Deep Visual-Semantic Hashing for Cross-Modal Retrieval* (Cao et al., KDD, 2016)
            * *Learning Deep Structure-Preserving Image-Text Embeddings* (Wang et al., CVPR, 2016)
        * Cross-modal retrieval:
            * *Canonical correlation analysis; An overview with application to learning methods* (Hardoon et al., Tech. Rep., 2003)
            * [*Audiovisual synchronization and fusion using canonical correlation analysis*](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=4351913) (Sargin et al., IEEE Trans. Multimedia, 2007)
            * [*Deep canonical correlation analysis*](http://ttic.uchicago.edu/~klivescu/papers/andrew_icml2013.pdf) (Andrew et al., ICML, 2013) [[Pytorch Code](https://github.com/Michaelvll/DeepCCA)]
            * [*Bridging Languages through Images with Deep Partial Canonical Correlation Analysis*](https://github.com/Michaelvll/DeepCCA) (Rotman et al., ACL, 2018) [[Pytorch Code](https://github.com/rotmanguy/DPCCA)]
            * *On deep multiview representation learning* (Wang et al., ICML, 2015)
            * [*Deep Canonically Correlated LSTM*](https://arxiv.org/pdf/1801.05407.pdf) (Mallinar and Rosset, arXiv, 2018)

### 2. Translation
* Translation (mapping) from one modality to another, subjective relationships
* Example: there are many ways to describe an image, and no correct way
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/multimodal_translation.png" width="500" alt="Translation">
</p>

* Example-based:
    * Uses dictionary
    * Retrieval-based
        * Direct use of retrieved translation
        * Unimodal: "finds the closest instances in the dictionary in the space of the source", "similarity in unimodal space does not always imply a good translation"
        * Intermediate semantic space: coordinated representation
        * Limitations: large model, slow inference (alleviated by hashing optimization), unrealistic to expect a perfect translation to pre-exist in dictionary for every scenario
    * Combination-based:
        * Combines retrieved translations and outputs the final one
        * "Able to construct more complex structures"
        * Hand crafted or based on heuristics
        * Limitation: "only able to perform translation in one direction, while semantic space retrieval-based models are able to perform it both ways"
* Generative
    * Construct model able to produce novel translation
    * Understands the source modality and generates an appropriate signal
    * Large space of possible correct answers, difficult to evaluate
    * Grammar-based
        * Simplifies task but enforcing a grammar constraint
        * Advantage: "more likely to generate syntactically or logically correct target instances"
        * Limitation: no creativity
    * Encoder-decoder
        * Encodes source modality into a vectorial representation and decodes it into the new modality
        * "beneficial to pre-train a decoder LSTM for image captioning before fine-tuning it to video description" (Venugopalan et al.)
        * Limitation: large training dataset, doubts whether the network memorizing or learning the data
    * Continuous generation
        * "Generates the target modality continuously based on a stream of source modality inputs"
        * "Suited for translating between temporal sequences"
        * Sequence translation, produces output at every timestep
        * Challenge of data: temporal consistency between modalities
        * Being substituted by encoder-decoder approaches
* Difficult to evaluate: human evaluation
    * Likert scale
        * Naturalness, MOS (speech synthesis)
        * Realism (visual speech synthesis)
        * Grammatical and semantic correctness, relevance, order, detail (media description)
    * Preference studies: compare 2 or more samples and ask which the user prefers
    * Time consuming, costly, and care when preparing and conducting surveys to avoid biases (language fluency, age, gender, culture)
    
### 3. Alignment
* "Identify the direct relations between (sub)elements from two or more different modalities"
* Example: align the steps in a recipe to a cooking video, align movie with script, or find the parts of an image corresponding to its caption
* Explicit
    * Explicitly aligning sub-components
    * Example: recipe-video example
    * Unsupervised (doesn't require any direct alignment labels): DTW, deep canonical time warping (deep CCA+DTW), HMM 
    * Weakly supervised (rely on labeled aligned instances): [aligning movies+books](https://arxiv.org/pdf/1506.06724.pdf)
* Implicit
    * Intermediate step for another task
    * Example: "image retrieval based on text description can include an alignment step between words and image regions"
    * Can be used to improve translation, otherwise "it ends up putting a lot of weight on the encoder module" to summarize the data in a single vectorial representation.
    * Graphical models: require manual construction for mapping (traning data and human expertise)
    * Neural network models: attention ([hierarchical](https://arxiv.org/abs/1606.00061), [stacked](https://arxiv.org/abs/1511.02274), [episodic memory](https://arxiv.org/abs/1603.01417)), [dot product similarity measure](https://cs.stanford.edu/people/karpathy/cvpr2015.pdf) (extracts latent alignment).
* Difficulties: 
    * Few datasets with explicitly annotated alignments
    * Difficult to design similarity metrics between modalities
    * Multiple possible alignments, not all elements in one modality have correspondences in another
    
### 4. Fusion
* Fuse/integrate "information from two or more modalities to perform a prediction": class (classification) or continuous value (regression)
* Example: predicting spoken words in audio-visual speech recognition
* Benefits: robust predictions, robust to missing data, captures complementary information
* Fusion category: "multimodal integration is performed at the later prediction stages, with the goal of predicting outcome measures"
* Multimodal representation and fusion are interlaced in Neural Networks, division isn't as clear

<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/multimodal_fusion.png" width="500" alt="Fusion">
</p>

* Model-agnostic
    * Independent from ML method
    * Early: feature-based
        * "integrates features immediately after they are extracted" (concatenation)
        * Pos: training of single model
    * Late: decision-based
        * "performs integration after each of the modalities has made a decision" (classification, regression)
        * Pos: robust to missing data, allows for training when no parallel data is available
        * Neg: ignores low level interaction between modalities
    * Hybrid: "combines outputs from early fusion and individual unimodal predictors"
* Model-based
    * Addresses fusion in their construction
    * Kernel-based methods
        * MKL (extension of SVM for multimodalities), better fusion of heterogeneous data
        * Neg: "reliance on training data (support vectors) during test time" -> slow inference, large memory footprint
    * Graphical models (shallow)
        * Generative: models joint probability
        * Discriminative: models conditional probability
        * Pos: interpretability, can "easily exploit spatial and temporal structure of the data"
    * Neural networks
        * Information fusion: joint hidden layer
        * [Multi-view LSTM (MV-LSTM)](https://pdfs.semanticscholar.org/24e8/2815ff0a27fac7c69157fa602d5dbc0198e7.pdf) (no code?)
        * Pos: learn from large data, end-to-end training, "able to learn complex decision boundaries that other approaches struggle with"
        * Neg: lack of interpretability, large training dataset

### 5. Co-learning
* "Transfer knowledge between modalities, their representation, and their predictive models"
* "Aiding the modeling of a (resource poor) modality by exploiting knowledge from another (resource rich) modality"
* Limited/poor resources can mean: lack of annotated data, noisy input, or unreliable labels
* Helper modality is used only during training
* Task independent: "could be used to create better fusion, translation, and alignment models"
* Example: relevant with limited resources such as annotated data

<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/multimodal_colearning.png" width="500" alt="Co-learning">
</p>

* Parallel data
    * Modalities are from the same dataset
    * "Require training datasets where the observations from one modality are directly linked to the observations from other modalities"
    * Co-learning:
        * Creates more labeled training samples when there's few labeled samples
        * Neg: "can lead to biased training samples resulting in overfitting"
    * Transfer learning:
        * Deep Boltzmann machines, Multimodal autoencoders
* Non-parallel data
    * Modalities are from different datasets, "no overlapping instances, overlap in general categories or concepts"
    * Transfer leaning
    * Conceptual grounding
        * Learning semantic meanings on language +additional modalities (vision, sound, smell...)
        * Overlapping with alignment
        * Does not always improve performance, only use when it makes sense
    * Zero shot learning (ZSL)
        * "Recognize a concept without having explicitly seen any examples of it"
        * Ex: find a cat in an image without ever having presented labeled images of cats to the model
* Hybrid data
    * Pivot dataset/modality: "Instances or concepts are bridged by a third modality or a dataset"
    * [Bridge Correlational Neural Network](https://arxiv.org/pdf/1510.03519.pdf)
