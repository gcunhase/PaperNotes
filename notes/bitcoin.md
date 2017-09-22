## [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/en/bitcoin-paper)
Satoshi Nakamoto, 2008

TLDR; Transfer money without double-spending and without needing a trusted third-party such as financial insitutions. In the online world, this trust would be substituted by a cryptographic proof.

### Key Points
* Double-spending problem solved with a peer-to-peer network that generates a hash
* Hash: computational proof of the chronological order of transactions (transactions timestamp)
* Fraud protection: transactions that are computationally impractical to reverse
* "The system is secure as long as honest nodes collectively control more CPU power than any cooperating group of attacker nodes"
* Proof-of-work: *one-CPU-one-vote*
* Reclaiming *disk space*: "Once the latest transaction in a coin is buried under enough blocks, the spent transactions before
it [...] are hashed in a Merkle Tree, with only the root included in the block's hash."
* Broadcast + Anonymous public keys: public can see that someone is sending an amount to someone else, but no information about the sender/receiver is available
* New key pair for every transaction, risk goes up in multi-input transactions

### Notes / Questions
* 1 electronic coin: chain of digital signatures
* "If a greedy attacker is able to assemble more CPU power than all the honest nodes, he would have to choose between using it
to defraud people by *stealing back his payments*, or using it to *generate new coins*. He ought to find it more profitable to play by the rules, such rules that favour him with more new coins than everyone else combined, than to undermine the system and the validity of his own wealth."
* Binomial Random Walk: race between the honest chain and an attacker chain
