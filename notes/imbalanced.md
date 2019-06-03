## My Notes on Solutions for Imbalanced data

TLDR; Two main techniques are used to improved accuracy classification tasks using imbalanced data: under-sampling of majority classes and over-sampling of minority classes.

**Solution**: "Alter the class distributions toward a more balanced distribution" [4]

### Data-level approaches
#### Under-sampling
* Remove similar, remove farthest, and remove by clustering [1]
* Tomek Link [6]:
  * Distance between a and b: d(a,b)
  * "A(a,b) is a Tomek Link if there is not an example c such that d(a,c)<d(a,b) or d(b,c)<d(a,b). If two examples form a Tomek link, then either one of these examples is noise or both examples are border-line." [4] 
* OSS [7]: "samples of majority class are removed that are considered either noisy or redundant"

#### Over-sampling
* [EDA](./eda.md): data augmentation for text (synonym replacement, random insertion, random swap and random deletion) [2]
* [SMOTE](./smote.md): over-sampling of minority class with sample generation in the feature space via feature vector and k-nearest neighbour manipulation [3]
* Evolutionary-SVM Algorithm [4]: use of "mutation and crossover operators to decrease the imbalance ratio" + "clustering for both classes to delete redundant and noisy samples"

### Algorithm-level approaches
* Cost-sensitive learning: "cost of misclassifying minority samples is higher than the majority samples"
* Boosting algorithm: such as Adaboost (ensemble learning model). "In every iteration, weights are modified with the objective of correctly classifying examples in the next iteration". "[...] weighted vote to classify unlabeled examples".

### Notes
* Bayes Imbalance Impact Index [5]
  * "Measurement about the extent of influence of class imbalance on the classification performance of imbalanced data"
  * Indicates which "data factor is actually the main barrier for classification"
  * Theoretical
  * "highly consistent with the improvement of F1 score made by the imbalance recovery methods on both synthetic and real benchmark datasets"
* ROC: receiver operating characteristics curve
* Applications with imbalanced data:
  * fraudulent telephone calls
  * text classification
  * information retrieval and filtering tasks
  * data mining for direct marketing 

### References
* [1] [Addressing the problem of Unbalanced Data sets in Sentiment Analysis](https://www.academia.edu/5505329/Addressing_the_problem_of_Unbalanced_Data_sets_in_Sentiment_Analysis) (Mountassir et al., 2012)
* [2] [EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks](./notes/eda.md) (Jan 2019)
* [3] [SMOTE: Synthetic Minority Over-sampling Technique](./notes/smote.md) (Jun 2002, JAIR)
* [4] [A New approach for Classification of Highly Imbalanced Datasets using Evolutionary Algorithms](https://pdfs.semanticscholar.org/2402/969387dd0ab0113be2ebd4437d79598389ee.pdf) (July 2011)
* [5] [Bayes Imbalance Impact Index: A Measure of Class Imbalanced Dataset for Classification Problem](http://arxiv.org/abs/1901.10173) (Jan 2019)
* [6] [Two Modifications of CNN](https://ieeexplore.ieee.org/document/4309452) (IEEE Trans. Systems, Man and Cybernetics 6, 1976)
* [7] [Addressing the Curse of Imbalanced Training Sets: One-Sided Selection](https://sci2s.ugr.es/keel/pdf/algorithm/congreso/kubat97addressing.pdf) (ICML, Jul 1997)