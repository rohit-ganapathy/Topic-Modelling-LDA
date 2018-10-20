# Topic-Modelling using LDA (Latent Dirichlet Allocation)
A topic modeller that uses Latent Dirichlet Allocation to identify multiple clusters(or topics) of key-phrases within a collection of documents. This  technique is especially useful when it comes to tasks like document classification and article reccommendation.

The following link offers a concise intuitive explanation of what LDA achieves and the math going on under the hood:
https://towardsdatascience.com/light-on-math-machine-learning-intuitive-guide-to-latent-dirichlet-allocation-437c81220158

### Dependencies

* python 3+
* numpy
* pandas
* gensim==3.4.0
* nltk==3.3
* glob2==0.6
* autocorrect==0.3.0


## Getting Started
 * run.py --n_topics -> create database and run topic modeller
 * view_topics.py --n_topics -> view topics  


### Notes

* I have tried my best to pre-process the documents (eg remove stopwords) but I encourage further tweaking in that respect.
* I have designed the program to generate two models. One that uses only unigrams and one that utilizes both unigrams as well as   bigrams.
* Although setting the number of topics is an arbitrary hyper-parameter,there are a number of heuristics that can be used to set  the optimum number of topics:https://cran.r-project.org/web/packages/ldatuning/vignettes/topics.html
* I have skipped over that part but might incorporate it in a future update.
