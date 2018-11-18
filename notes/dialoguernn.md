## [DialogueRNN: An Attentive RNN for Emotion Detection in Conversations](https://arxiv.org/abs/1811.00405)
Navonil Majumder et al., Submitted on 1 Nov 2018

TLDR; Emotion detection in dyadic conversations modeling speaker, context and emotion separately in a model using 3 task-specific GRUs.

### Key Points
* In dyadic conversations "the parties have distinct roles. Hence, to extract the context, it is crucial to consider the preceding turns of both speaker"

* Assumes that the emotion of an utterance in a conversation depends on 3 major factors: *speaker*, *context* (preceding utterances), and the *emotion behind the preceding utterances*

* Novelty: separate modeling of the 3 mentioned aspects

* DialogueRNN: 3 GRU to model speaker, context and emotion
  * **Global State** GRU (shared among the parties): "the context of an utterance is modeled using a global state, where the preceding utterances and the party states are jointly encoded for context representation"
  * **Party State** GRU (party specific, generates speaker state *q*): "each party is modeled using a party state which changes as and when that party utters an utterance"
  * **Emotion Representation** GRU: "model infers emotion representation from the party state of the speaker along with the preceding speakers’ states as context"
  * **Speaker Update** GRU (attention block): response based on context.
    * Calculates attention scores alpha: previous global states *g* and current utterance *u_t*
    * Context vector *c_t*: alpha (softmax score) * previous global states
    * Context vector and utterance: encoded with Global GRU into the speaker's state
  * **Listener Update**: models the listener's change of state to the speaker's utterance (keeps the state of the listener unchanged)
  
<p align="center">
<img src="https://github.com/gcunhase/PaperNotes/blob/master/notes/imgs/DialogueRNN.png" width="600" alt="DialogueRNN">
</p>

* Speaker and global GRUs (GRU_P, GRU_G) jointly act similar to an encoder and emotion GRU serves as a decoder

### Notes / Questions
* 6 emotions: happy, sad, neutral, angry, excited, and frustrated
* Input:
  * Speech utterances transformed into utterance representations, obtained using feature extractors
  * Feature extractors:
    * Textual (T) Feature Extraction: CNN from utterances
    * Audio (A) and Visual (V) Feature Extraction: 3D-CNN and openSMILE (open source Speech & Music Interpretation by Large-space Extraction code)
* In *Listener Update*:
  * Authors compared GRU based on visual cues and listener context
  * This approach gave similar results to when they just kept the same state (unless the listener was speaking) but with incresed number of parameters
  * Conclusion: no GRU was used to update the listener's state

### Results
* Datasets used:
  * IEMOCAP (2008)
    * 2-way conversations of 10 unique speakers
    * Contains single dyadic dialogue segmented into utterances
    * Annotated with 1 of 6 emotion labels, unbalanced
  * AVEC (2012)
    * Modification of SEMAINE database (2012)
    * Contains interactions between humans and artificially intelligent agents
    * Annotated with 4 real valued affective attributes: valence, arousal, expectancy [-1, 1] and power [0, inf)
  * (train+val)/test 80/20
* Compared with c-LSTM, c-LSTM+Att, TFN, MFN, CNN, Memnet, CMN (SOTA)
* Significantly outperforms the state of the art 
* [PyTorch code](https://github.com/senticnet/conv-emotion) from authors
