## [SeqGAN: Sequence Generative Adversarial Nets with Policy Gradient](https://arxiv.org/abs/1609.05473)
Lantao Yu et al., Submitted on 18 Sep 2016

TLDR; SeqGAN's goal is to solve GAN's limitation of being unable to generate sequences of discrete tokens and to give score/loss before generating entire sequence by applying the Monte Carlo approach. The generator is a seq2seq model and it is modeled as a stochastic policy in reinforcement learning (RL). The discriminator is a CNN, it evaluates the sequence and gives feedback to guide the learning of the generative model.

### Key Points
* Proposed Model: extends GANs with the RL-based generator to solve the sequence generation problem, where a reward signal is provided by the discriminator at the end of each episode via Monte Carlo approach, and the generator picks the action and learns the policy using estimated overall rewards.
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/SeqGAN.png" width="400" alt="SeqGAN">
</p>

* Problems of GAN generating sequences:
  - "GAN is designed for generating real-valued, continuous data but has difficulties in directly generating sequences of discrete tokens, such as texts." Meaning that slight changes in discrete tokens wouldn't really make sense in this network (probably no corresponding token for such slight change in the limited dictionary space). -> SOLUTION: regard the generative model as a stochastic parameterized policy (applying Monte Carlo search)
  - "GAN can only give the score/loss for an entire sequence when it has been generated; for a partially generated sequence, it is non-trivial to balance how good as it is now and the future score as the entire sequence."
* Considers the sequence generation procedure as a sequential decision making process.
* Data generator: modeled as a stochastic policy in reinforcement learning (RL). That way, SeqGAN bypasses the generator differentiation problem by directly performing gradient policy update. Generative model: RNN, LSTM, GRU, etc.
* Discriminator: used to evaluate the sequence and feedback the evaluation to guide the learning of the generative model. "To evaluate the action-value for an intermediate state, we apply Monte Carlo search with a roll-out policy G_beta to sample the unknown last T-t tokens". Discriminative model: CNN.
* Limitation: generated sequence has a fixed length T. CNN is also capable of the variable-length sequence discrimination with the max-over pooling technique (Kim 2014).

### Notes / Questions
* Approximation of approximation: Monte Carlo is used to predict the score/loss and discrete tokens are being approximated to real-valued ones.
* Is there a better way to introduce Sequence to GAN without all those approximations?
* Do the authors use char-LSTM? If so, would our result improve is we use word-LSTM or just further the approximations?

### Results
#### Code1: [seqgan-text-tensorflow](https://github.com/codekansas/seqgan-text-tensorflow), samples n=100
* Batch 32, Epoch 147: *e to an  e and terent  ao   e the prosection tontrin the e the pee ae er the perira  the provect to*
* Batch 1, Epoch 33, stopped then ran again until epoch 62: *the eerer to tee  tererted to testanced the eereicipation of the provide to the e pervice the prove*
* Char-LSTM produces words and sentences that don't always make sense. Is fine tuning the solution?

#### Code2: [SeqGAN](https://github.com/LantaoYu/SeqGAN), published by authors
* Based on code3 below

#### Code3: [sequence_gan](https://github.com/ofirnachum/sequence_gan)
* Run *book_demo.py*
  * Char-based Seq-GAN on data from Moby Dick.
  * ValueError: empty range for randrange() (0,-9, -9)
    - [Solution](https://github.com/ofirnachum/sequence_gan/issues/10): Try to read the book source from this address: *http://www.gutenberg.org/files/2701/2701-0.txt*.
  * Output: 







