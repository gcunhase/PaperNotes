## [Evaluating Natural Language Understanding Services for Conversational Question Answering Systems](https://www.aclweb.org/anthology/W17-5522)
Daniel Braun et al., Aug 2017, SIGDIAL 2017

TLDR; Evaluation corpora to test NLU services for the task of Intent Classification. Contains three corpus: Chatbot, Ask Ubuntu and Web Applications.

### Key Points
* Chatbot
  * German Telegram chatbot for public transportation
  * 2 intents (train/test): Find Connection (57/35) and Departure Time (43/71)

* Ask Ubuntu
  * Web crawling the StackExchange platform
  * 5 intents

  <p align="center">
  <img src="./imgs/nlu_evaluation_corpora_askubuntu.png" width="150" alt="Ask Ubuntu">
  </p>

* Web Applications
  * Web crawling the StackExchange platform
  * 8 intents

  <p align="center">
  <img src="./imgs/nlu_evaluation_corpora_webapps.png" width="150" alt="Web Applications">
  </p>

### Notes
* Entity slots also available in datasets
         
### Results
* [Dataset](https://github.com/sebischair/NLU-Evaluation-Corpora)
* NLU services: LUIS, Watson, Api.ai, RASA
