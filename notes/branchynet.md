## [Fast Intent Classification for Spoken Language Understanding](http://arxiv.org/abs/1912.01728)
Akshit Tyagi et al., 3 Dec 2019 version

TLDR; BranchyNet scheme to reduce complexity and latency while retaining accuracy in SLU systems by inserting exit points throughout the model. 

### Key Points
* Previous works:
    * Regularization (reduce number of model parameters, prevents over-fitting), model distillation, compression
    * **Limitations**: "all attempt to modify the modeling architecture to reduce computational complexity", resulting in *accuracy loss*

* **Approach**:
    * [BranchyNet (ICPR 2016)](https://arxiv.org/pdf/1709.01686.pdf) scheme in SLU systems to reduce complexity and latency (by allowing early decision making when possible) while retaining accuracy in said systems.
    * Candidate architectures: 3-layer DNN and Stacked LSTM (3 exit points each)   
    * Minimal modification:
        * Exit points added whenever the user wants (say at each hidden layer in DNN)
        * This allows the model to make "a decision as soon as it is confident in its prediction"
        * Loss function: weighted sum of cross entropy losses from every exit point. The weight $\alpha_n$ is a linearly decreasing function that "encourages the learning discriminative representations in earlier layers, thereby encouraging early exit".
        * Decision: after training, "an entropy threshold H^T_n is defined for each exit point *n*". If the entropy at point *n < H^T_n*, a decision is made.  
    
<p align="center">
<img src="./imgs/branchynet_dnn.png" height="200" alt="DNN with BranchyNet">
<img src="./imgs/branchynet_stackedlstm.png" height="200" alt="Stacked LSTM with BranchyNet" hspace="20">
</p>

### Notes
* **Dataset**:
    * [Facebook Semantic Parsing Systems (FSPS) [[paper](https://arxiv.org/abs/1810.07942)] [[download](http://fb.me/semanticparsingdialog)]
    * 44.7k annotated queries (31.2k train, 4.4k validation, 9k test)
    * 25 intents
* Questions:
    1. What is *r* in Eq. 2?
    2. What is *T* in Fig. 1 and 2? After the entropy check and exit.
        * Activation function?
        * Threshold number?
    3. How is *H^T_n* defined?
    
### Results
* Boost in performance (regularization effect and tailored representations from each layer with exit). The introduction of BranchyNet in DNN and Stacked LSTM does not lead to accuracy loss.
* Reduces computational complexity