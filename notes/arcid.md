## [ARCID: A new approach to deal with imbalanced datasets classification](https://www.researchgate.net/publication/322010034_ARCID_A_New_Approach_to_Deal_with_Imbalanced_Datasets_Classification)
Safa Abdellatif et al., Jan 2018, SOFSEM 2018

TLDR; Algorithm-level approach to imbalanced data case.

### Key Points
* Handles two class problems
* Association Rule-based Classification for Imbalanced Datasets (ARCID)
* Algorithmic based strategy: cost-sensitive learning
* emphasizes "information extracted from minor classes without drastically impacting the predictive accuracy of the classifier"

* 3 phases:
  * Rule generation: "generating frequent rules from each class of the training set using a local support"
    * IGB algorithm
  * Filtering: "filtering rules generated during the first phase" (novel ranking and pruning technique)
    * Ranking then selecting top k rules:
      * "Rules that have a very high predictive accuracy (because of their high support value) and generally belong to major classes."
      * "Rules that are rare (because of their low support value), interesting in many applications and generally belong to minor classes." 
  * Class prediction: "predicting the class label of the new data"

### Notes
* Imbalance ratio: "ratio of major class’ instances divided by the minor class’ instances"
* Code not found

### Results
* 5 real-world datasets from UCI repository [1]: breast-cancer, post-operator, Mofn, tic-tac-toe and german
* Baseline:
  * non-rule-based: Naive Bayes, Random Forest
  * rule-based: C4.5, CBA
  * Handling class imbalance: Fitcare [2], RIPPER
* CPU: Windows 8 PC equipped with an Intel Core i7-4720, 2.6 GHz processor and 8 GB of RAM
* WEKA Software System [3]
* Assessment metrics: Global accuracy, Gmean, F-measure and per-class accuracy of minor class

### References
* [1] Merz, C.: [*Uci repository of machine learning databases*](http://www.ics.uci.edu/~mlearn/MLRepository.html) (1996)
* [2] Cerf, L., Gay, D., Selmaoui-Folcher, N., Cremilleux, B., Boulicaut, J.: [*Parameter-free classification in multi-class imbalanced data sets*](https://www.sciencedirect.com/science/article/pii/S0169023X13000682?via%3Dihub). Data Knowl. Eng. 87, 109– 129 (2013)
* [3] Hall, M., Frank, E., Holmes, G., Pfahringer, B., Reutemann, P., Witten, I.H.: [*The weka data mining software: an update*](https://www.kdd.org/exploration_files/p2V11n1.pdf). ACM SIGKDD explorations newsletter 11(1), 10–18 (2009)