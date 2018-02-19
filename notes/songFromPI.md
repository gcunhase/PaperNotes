## [Song From PI: A Musically Plausible Network for Pop Music Generation](https://arxiv.org/abs/1611.03477)
Hang Chu, Raquel Urtasun and Sanja Fidler, Submitted on 10 Nov 2016

TLDR; Hierarchical Recurrent Neural Networks for pop music generation, where the bottom layers generate the melody and the higher ones produce the drums and chords.

### Key Points
* Aim: how far can a computer get to be a real composer
* [Inspiration](https://youtu.be/OMq9he-5HUU): Song from \pi by Mcdonald, where pleasing music is created from a sequence of digits of \pi
* LSTM captures more global music structure across the song
    * Eck and Scmidhuber (2002) were first to use LSTMs to generate both melody and chord
* Previous works:
    * Most researchers produce only one note at a time with the exception of Boulanger-lewandowski (2012) who generated polyphonic music although still single-track (only produces melody)
    * Huang and Wu (2016): 2-layer LSTM that produces music that is more complex thana  single note sequence and is able to produce chords
    * Kang et al. (2012) build upon the randomness of melody by trying to accompany it with drums, however scale type is enforced
* Novelty:
    * "Unlike most other neural network approaches, this work encodes music knowledge into the representation"
    * "Hierarchical model that incorporates knowledge from music theory to build the neural architecture and produces multi-track pop music (melody, chord and drum)"
* Framework:
    * Generation conditioned on the scale type (4 types)
    * **Melody** is encoded with two random variables at each time step, representing which key is being played (*key layer*) and the duration that the key will be pressed (*press layer*)
    * Assumption: drums and chords are independent given the melody
    * **Drums** and **chords** are generated at each time step conditioned on the melody
    
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/songFromPiFramework.png" width="500" alt="Framework">
</p>

* More details about framework
    * *key layer*: 2-layer LSTM with 512-dimensional hidden state
        * Input: vector that concatenates multiple features
            1. one-hot encoding of the previous generated note $y_{key}^{t-1}$
            2. lookback features proposed by Google Magenta: include skip connections from 2 and 1 bar ago represented by the red lines (skip connections for the current time step *t*), 2 additional features indicating if last used key was from 1 or 2 bars ago and 5-dim feature indicating binary enconding of the current time *t*
            3. melody profile (new feature): 10-dimensional one-hot vector representation of the cluster id for each time step obtained by computing the local note histogram at each time step with width of 2 bars and clustering them into 10 clusters via k-means
    * *press layer*: 2-layer LSTM with 512-dimensional hidden state
        * Press count: 1, 2, 3, 4
        * Reset to 1 when key is released
        * $y_{prs}^{t}$: 8-dimensional one-hot vector
        * Input: $y_{prs}^{t-1}$ + 37-dim one-hot encoding of the melody key $y_{key}^{t}$
    * *chord layer*: 2-layer LSTM with 512-dimensional hidden state
        * Chord is strongly related with melody 
        * $y_{chd}^{t}$: one-hot encoding with 72 classes
        * Input: $y_{chd}^{t-4}$ + $y_{key}^{t-3:t}$
    * *drum layer*: 2-layer LSTM with 512-dimensional hidden state
        * one-hot encoding: 100 unique one-bar-long drum patterns
        * Input: $y_{drm}^{t-4}$ + $y_{key}^{t-3:t}$
    * softmax
    * Cost function to train each layer: cross-entropy with Adam Optimizer, learning rate of 2e-3, learning rate decay of 0.99 after each epoch for 10 epochs
    * Music synthesis


### Notes / Questions
* [website](https://www.cs.toronto.edu/songfrompi/)
* [ICLR 2017 workshop](https://openreview.net/forum?id=ByBwSPcex)
* Concepts from music theory: Sectionn 3
    * Identifying the scale of a song: Section 4.1
    * Range of notes: C3 to C6
    * Bar: 8 consecutively played notes

### Results
* Dataset: 100 hours of midi music (user-composed pop songs and video game music)
* Experiments:
    * 120 beat per minute with 4 time steps per beat
    * MIDI 9th channel reserved for drums
* Results:    
    * 27 participants presented with several pairs of 30-second music clips (10 songs per method) and asked to vote which clip in the pair sounds better or neutral vote
    * Human studies with 27 participants show strong preference of the authors' generated music over that produced by Gogle's Magenta (2016).
    * Further improvement can still be made: "drums sound too different and do not participate to the melody perfectly"
* 2 novel applications:
    * Neural dancing and karaoke
        * Stickman dancing to author's music and lyrics that can be sung with
        * 1 hour of *Just Dance* vidoes used to learn relationship between music and dance
            * Generate stickman dancing by adding another dancing layer on top of the key layer
        * 50 hours of lyrics data from the internet + 1 hour of *Just Dance* videos: relationship between music and lyrics
            * Select words that appear at least 4 times (vocabulary size of 3390 inclkuding UNK and EOS)
            * Generate 1 word per beat using another lyrics layer on top of the key layer
    * Neural story singing
        * Condition on output of neural storyteller Kiros et al. (2015)
        * Writes a story about an image and converts it into a pop song
        * 1 hour of videos from *Just Dance*
        * 1 beat per word and short pause of EOS (next sentence starting from new bar)
        * UNK replaced with *Ooh*

