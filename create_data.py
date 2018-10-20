import pandas as pd
from clean import clean
from preprocess import preproc,bigram
from gensim import corpora 




def create(path):
    links,articles=clean(path)
    
    data = pd.DataFrame()
    
    
    data["articles"]=articles
    data["links"]=links
    
    data.to_csv('./data/data.csv',index=False)
        
    processed_docs_uni=data["articles"].map(preproc)# list of unigrams from all documents
    processed_docs_bi=data["articles"].map(bigram) #list of bigrams from all documents
    
    """
     create and save dictionary including only unigrams
    """
    
    user_dict=corpora.Dictionary(processed_docs_uni)
    user_dict.save("./data/dictionary_uni.pkl")
    
    
    """create and save dictionary including unigrams and bigrams
    """
    agent_dict=corpora.Dictionary(pd.concat([processed_docs_uni,processed_docs_bi],ignore_index=True))
    agent_dict.save("./data/dictionary_uni+bi.pkl")
    