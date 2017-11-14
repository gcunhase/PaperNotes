## [How to Construct Deep Recurrent Neural Networks](https://arxiv.org/abs/1312.6026)
Yoshua Bengio et al., Submitted on 20 Dec 2013

TLDR; The depth of an RNN is characterized by its input-to-hidden function, hidden-to-hidden transition and hidden-to-output function.

### Key Points
* Propose two novel architectures of a deep RNN which are orthogonal to an earlier attempt of stacking multiple recurrent layers to build a deep RNN (Schmidhuber, 1992; El Hihi and Bengio, 1996).
* Conventional RNN: transitions are not deep, but are only results of a linear projection followed by an element-wise nonlinearity. "It is clear that the hidden-to-hidden (ht−1 → ht), hidden- to-output (ht → yt) and input-to-hidden (xt → ht) functions are all shallow in the sense that there exists no intermediate, nonlinear hidden layer."
* *Deep Input-to-Hidden Function*: This approach of making the input-to-hidden function deeper is in the line with the standard practice of replacing input with extracted features in order to improve the performance of a machine learning model.
* *Deep Hidden-to-Output Function*: A deep hidden-to-output function can be useful to disentangle the factors of variations in the hidden state, making it easier to predict the output.
* *Deep Hidden-to-Hidden Transition*: This nonlinear transition could allow the hidden state of an RNN to rapidly adapt to quickly changing modes of the input, while still preserving a useful summary of the past.

<figure>
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/deeprnn_models.png" width="600" alt="Deep RNNs">
</p>
</figure>

### Notes / Questions

### Results
* Evaluated on the tasks of polyphonic music prediction and language modeling

