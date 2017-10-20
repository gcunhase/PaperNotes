## [C-RNN-GAN: Continuous recurrent neural networks with adversarial training](https://arxiv.org/abs/1611.09904)
Olof Mogren, Submitted on 29 Nov 2016

TLDR; GAN that works on continuous sequential data, training done on a collection of classical music (MIDI files).

### Key Points
* Trained with adversarial training to model the whole joint probability of a sequence
* *"Yu et al. [2016] trained an RNN with adversarial training, applying policy gradient methods to cope with the discrete nature of the symbolic representation they employed. In contrast to this, our work represents tones using real valued continuous quadruplets of **frequency**, **tone length**, **intensity**, and **time** spent since the previous tone."*: allows use of standard backpropagation to train the whole model end-to-end.
* G: input is a random vector concatenated with the output of the previous cell
* D: bidirectional LSTM

### Notes / Questions
* What is Beam-search??
* LSTM: "has an internal structure with gates that help with the vanishing gradient problem, and to learn longer dependencies"


### Results
* Evaluation: uses metrics such as scale consistency and tone range
* Dataset: 3697 MIDI files from 160 different composers of classical music.
* [Code](https://github.com/olofmogren/c-rnn-gan)
   1. Install [python-midi](https://github.com/vishnubob/python-midi)
   ```
   sudo -H pip install python-midi
   ```
   2. Download data
      * In *music_data_utils.py*:
         * A few sources that are giving error (not found or multiple choice): delete them or surround *response = urllib2.urlopen(url)* with try and catch and ignore those files.
         * Modify *datadir=filename* instead of *datadir=None* in *main()*.
         * New [*music_data_utils.py*]() file is attached.
      * Run ```python music_data_utils.py [name of folder to save data]```
       
   3. Run code
      * Change in [*tf.split*](https://stackoverflow.com/questions/41842440/tensorflow-input-split-dim-of-split-op-has-type-float32-that-does-not-matc)
      * From TensorFlow 1.0 onwards, tf.concat() takes the arguments values and axis. Replacing concat_dim with axis will fix the problem.
      * tf.pack -> tf.stack
   ```
   python rnn_gan.py --datadir data --traindir train
   ```
 
