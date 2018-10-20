import pandas as pd 
from gensim import corpora 
from preprocess import preproc,bigram
from gensim.models import LdaMulticore as LDA
import os
import glob
    

def modeller(n_topics):
    
    
    paths=glob.glob("./data/*.pkl")
    data=pd.read_csv("./data/data.csv")
    data.apply(str)
    
    
    
    for path in paths:
        
                        
            if "uni+bi" in path:
              
              p_uni = data['articles'].map(preproc)
              p_bi =  data['links'].map(bigram)
              processed_docs=p_uni.append(p_bi,ignore_index=True)
              dic=corpora.Dictionary.load(path)            
              dic.filter_extremes(no_above=0.5, keep_n=100000)
              bow_corpus = [dic.doc2bow(doc) for doc in processed_docs]
              train_save(n_topics,"both",bow_corpus,dic)
    
            else:
              
              processed_docs = data['articles'].map(preproc)
              dic=corpora.Dictionary.load(path)            
              dic.filter_extremes(no_above=0.5, keep_n=100000)
              bow_corpus = [dic.doc2bow(doc) for doc in processed_docs]
              train_save(n_topics,"unigram",bow_corpus,dic)
            
        
    
def train_save(n_topics,uni_or_bi,bow_corpus,dic):
    
     
     
        name=str(n_topics)+"-topics"
        lda_model = LDA(bow_corpus, num_topics=n_topics, id2word=dic, passes=2)
        lda_model.save(os.getcwd()+"/LDA models/{}/{}".format(uni_or_bi,name))
     
     
     
     
     
     