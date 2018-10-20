from nltk.tokenize import TweetTokenizer
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import autocorrect
from contractions import contractions,greetings,stopwords
from contractions import contractions_no_punc as nopunc
import nltk
from nltk.util import ngrams

"""
->tokenize
->correct spelling
->contract (isn't -> is not)
-> remove stop words
->lemmatize/stem

"""


def pos_convert(treebank_tag):
   if treebank_tag.startswith('J'):
        return "a"
   elif treebank_tag.startswith('V'):
        return "v"
   elif treebank_tag.startswith('N'):
        return "n"
   elif treebank_tag.startswith('R'):
        return "r"
   else:
        return 'v'
    
def stem(text):
    
    return SnowballStemmer("english").stem(text)

def lemmatize(text,pos='V'):
    
    p=pos_convert(text)
    return WordNetLemmatizer().lemmatize(text, pos=p)

def lemstem(text):
    return stem(lemmatize(text))

def spell(text):
    
    return autocorrect.spell(text)

def expand(text):
     
        try:
          return contractions[text].split(" ")
        except:
          try:
            return nopunc[text].split(" ")
          except:
            return [text]

"""
slb=s/l/b=stem/lemmatize/both

"""
def preproc(text,slb='l'):
    
    text=str(text)
    result = []
    tokens=TweetTokenizer(preserve_case=False).tokenize(text)
    pos_tags=nltk.pos_tag(tokens)

    for token,pos in pos_tags:
        expanded=expand(token)
        for item in expanded:
            word=spell(item)
            if word not in stopwords and word not in greetings and len(word)>1 :
                #result.append(item)
                if slb=="b":
                  result.append(lemstem(word))
                
                elif slb=="l":
                  result.append(lemmatize(word))
 
                elif slb=="s":
                  result.append(stem(word))
  
                else:
                  raise Exception("invalid value assigned to slb!")
                    
                
    return result
    

def bigram(text):
   
   text=str(text)
   text=expand_sent(text)
   tokens=TweetTokenizer(preserve_case=False).tokenize(text)
   bigrams=ngrams(tokens,2)
   results=[]
   
   for gram in bigrams:
       
       lent=[len(x) for x in gram]
       
       
       if all(x>1 for x in lent):
           if all(word not in stopwords and word not in greetings for word in gram):
              
               join=gram[0]+"_"+gram[1]
               
               if any([any(char.isdigit() for char in join),("@" in join)])==False:
                results.append(join)
   
   return results



"""
expand sentence(aren't -> are not) and 
drop possesive pronouns (my,his,her,your)

"""
def expand_sent(text):
    
    new=""
    tokens=TweetTokenizer(preserve_case=False).tokenize(text)
    pos_tags=nltk.pos_tag(tokens)
    
    for token,pos in pos_tags:
        if not(pos.startswith("PRP")):
            for word in expand(token):
                new=new+word+" "
     
    return new    

      











    
