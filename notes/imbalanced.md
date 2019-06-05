## My Notes on Solutions for Imbalanced data

TLDR; Two main techniques are used to improved accuracy classification tasks using imbalanced data: under-sampling of majority classes and over-sampling of minority classes.

### Problem
* *Description*: "A dataset is called imbalanced when the number of instances belonging to the class of interest (minor class) is much lower than the ones of other classes (major classes). Association rules belonging to minor classes are rare as compared with ones that predict major classes. Consequently, this yields to a misclassification of the testing samples belonging to minor classes." [8]

* *Classical classifiers* [8]: 
    * "aim to minimize the error rate and maximize the accuracy"
    * "assume a balanced class distribution and an equal cost of misclassification errors"

* *Solution*: "Alter the class distributions toward a more balanced distribution" (data level) [4] or modify the classifier itself (algorithm level)

### Data-level approaches
Re-balancing of data before applying algorithm
> [A (PyTorch) imbalanced dataset sampler for oversampling low frequent classes and undersampling high frequent ones.](https://github.com/ufoym/imbalanced-dataset-sampler)

#### Under-sampling
* Goal: "decrease the population of the majority class by ignoring a large number of its instances" [8]
* (+) Less computationally expensive 
* (-) "potentially useful information may be lost during the sampling process" [8]
* Approaches:
    * Under-sampling in sentiment analysis: remove similar, remove farthest, and remove by clustering [1]
    * Tomek Link [6]:
      * Distance between a and b: d(a,b)
      * "A(a,b) is a Tomek Link if there is not an example c such that d(a,c)<d(a,b) or d(b,c)<d(a,b). If two examples form a Tomek link, then either one of these examples is noise or both examples are border-line." [4] 
    * One-sided selection (OSS) [7]: "samples of majority class are removed that are considered either noisy or redundant"

#### Over-sampling
* Goal: "increase the population of minority class by replicating its instances" [8]
* (+) No loss of data
* (-) Possible overfitting and computational overhead
* Approaches:
    * [EDA](./eda.md) (2019): data augmentation for text (synonym replacement, random insertion, random swap and random deletion) [2]
    * [SMOTE](./smote.md) (2002): over-sampling of minority class with sample generation in the feature space via feature vector and k-nearest neighbour manipulation [3]
    * [SMRT](https://github.com/tgsmith61591/smrt) (Synthetic Minority Reconstruction Technique): younger version of SMOTE, uses variational auto-encoders to generate synthetic observations of minority class
    * VOS (2018) [11]: Variational oversampling of imbalanced data with VAE
    * Evolutionary-SVM Algorithm [4]: use of "mutation and crossover operators to decrease the imbalance ratio" + "clustering for both classes to delete redundant and noisy samples"
    * [S-VAE](https://nicola-decao.github.io/s-vae) (2018) [12]: "variational auto-encoder with a hyperspherical latent space" (instead of a conventional gaussian)
    * Collection of GAN for image ([PyTorch](https://github.com/znxlwm/pytorch-generative-model-collections)) 
    
### Algorithm-level approaches
* Modifies the classifier itself
* *Cost-sensitive learning*:
    * apply "a misclassification cost to the incorrectly classified instance" [8]
    * "cost of misclassifying minority samples is higher than the majority samples" [4]
    * "consists in only learning from the minor class by treating major class’ instances as outliers" [8]
    * Examples:
        * RIPPER (Repeated Incremental Pruning to Produce Error Reduction): rule induction learning algorithm
        * HIPPO
        * Class weights in loss function ([PyTorch](https://github.com/emredog/FCNN-example), 2018)
* *Input weighting*:    
    * [*Learning to Reweight Examples for Robust Deep Learning*](https://arxiv.org/pdf/1803.09050.pdf) (ICML 2018) [[PyTorch](https://github.com/danieltan07/learning-to-reweight-examples)]
    * Term weighting in text (2007) [13]
 
* *Boosting algorithm*: such as Adaboost (ensemble learning model). "In every iteration, weights are modified with the objective of correctly classifying examples in the next iteration". "[...] weighted vote to classify unlabeled examples".
    * [CUSBoost](https://github.com/farshidrayhanuiu/CUSBoost) (CSITSS 2017): "clustering-based under-sampling approach with boosting (AdaBoost) algorithm"
    * RAMOBoost (2010): ranked minority oversampling in Boosting
    * RUSBoost (2008): random under-sampling with AdaBoost
    * SMOTEBoost (2003): synthetic minority over-sampling with AdaBoost
    * Minimalist Python-based implementations of algorithms ([Tensorflow](https://github.com/dialnd/imbalanced-algorithms)): under and over-sampling and ensemble sampling (RAMOBoost, RUSBoost, SMOTEBoost)

### Evaluation metrics
* F-score: "combines Precision and Recall into a single measure that reflects the goodness of a classifier in the presence of rare classes" [9]
* Geometric mean (Gmean) [10]
  * "one of standard evaluation measures used in an imbalanced dataset classifier"
  * "product of the prediction accuracies of minor and major classes"
* Confusion matrix
* Per-class accuracy of minor class
* Bayes Imbalance Impact Index [5]
  * "Measurement about the extent of influence of class imbalance on the classification performance of imbalanced data"
  * Indicates which "data factor is actually the main barrier for classification"
  * Theoretical
  * "highly consistent with the improvement of F1 score made by the imbalance recovery methods on both synthetic and real benchmark datasets"
* ROC: receiver operating characteristics curve
* AUC: area under the ROC curve

### Applications with imbalanced data
* Fraudulent telephone calls
* Text classification (sentiment analysis, intent classification)
* Information retrieval and filtering tasks
* Data mining for direct marketing
* Medical diagnostics: disease cases are less than healthy cases
* Security: network intrusion detection, counter-terrorism

### References
* [1] [Addressing the problem of Unbalanced Data sets in Sentiment Analysis](https://www.academia.edu/5505329/Addressing_the_problem_of_Unbalanced_Data_sets_in_Sentiment_Analysis) (Mountassir et al., 2012)
* [2] [EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks](./eda.md) (Jan 2019)
* [3] [SMOTE: Synthetic Minority Over-sampling Technique](./notes/smote.md) (Jun 2002, JAIR)
* [4] [A New approach for Classification of Highly Imbalanced Datasets using Evolutionary Algorithms](https://pdfs.semanticscholar.org/2402/969387dd0ab0113be2ebd4437d79598389ee.pdf) (July 2011)
* [5] [Bayes Imbalance Impact Index: A Measure of Class Imbalanced Dataset for Classification Problem](http://arxiv.org/abs/1901.10173) (Jan 2019)
* [6] [Two Modifications of CNN](https://ieeexplore.ieee.org/document/4309452) (IEEE Trans. Systems, Man and Cybernetics 6, 1976)
* [7] [Addressing the Curse of Imbalanced Training Sets: One-Sided Selection](https://sci2s.ugr.es/keel/pdf/algorithm/congreso/kubat97addressing.pdf) (ICML, Jul 1997)
* [8] [ARCID: A new approach to deal with imbalanced datasets classification](./arcid.md) (Jan 2018)
* [9] Rijsbergen, C.J.V.: [*"Information Retrieval"*](http://openlib.org/home/krichel/courses/lis618/readings/rijsbergen79_infor_retriev.pdf). Butterworth (1979)
* [10] Kubat, M., Holte, R.C., Matwin, S.: [*"Machine learning for the detection of oil spills in satellite radar images"*](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.308.2361&rep=rep1&type=pdf). Machine Learning 30(2-3), 195–215 (1998)
* [11] Fajardo, Val Andrei, et al. [*"Vos: a method for variational oversampling of imbalanced data"*](https://arxiv.org/pdf/1809.02596.pdf). arXiv preprint arXiv:1809.02596 (2018).
* [12] Davidson, Tim R., et al. [*"Hyperspherical variational auto-encoders"*](https://arxiv.org/abs/1804.00891). arXiv preprint arXiv:1804.00891 (2018). [[blog](https://nicola-decao.github.io/s-vae), [PyTorch](https://github.com/nicola-decao/s-vae-pytorch), [Tensorflow](https://github.com/nicola-decao/s-vae-tf)]
* [13] Liu, Ying, Han Tong Loh, and Aixin Sun. [*"Imbalanced text classification: A term weighting approach"*](https://ccc.inaoep.mx/~villasen/bib/Imbalanced%20text%20classification-%20A%20term%20weighting%20approach.pdf). Expert systems with Applications 36.1 (2009): 690-701.
