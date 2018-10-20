
from gensim.parsing.preprocessing import STOPWORDS


remove=["empty","computer","cry","bill"]
stopwords=list(STOPWORDS)

for i in remove:stopwords.remove(i)

contractions = {
"ain't": "am not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": " he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how is",
"i'd": "I would",
"i'd've": "I would have",
"i'll": "I will",
"i'll've": "I will have",
"i'm": "I am",
"i've": "I have",
"isn't": "is not",
"it'd": "it would",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she would",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so is",
"that'd": "that would",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there would",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what will",
"what'll've": "what will have",
"what're": "what are",
"what's": "what is",
"what've": "what have",
"when's": "when is",
"when've": "when have",
"where'd": "where did",
"where's": "where is",
"where've": "where have",
"who'll": "who will",
"who'll've": "who will have",
"who's": "who is",
"who've": "who have",
"why's": "why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you would",
"you'd've": "you would have",
"you'll": "you will",
"you'll've": "you will have",
"you're": "you are",
"you've": "you have"
}

contractions_no_punc = {'aint': 'am not', 'arent': 'are not', 'cant': 'cannot',
                        'cantve': 'cannot have', 'cause': 'because',
                        'couldve': 'could have', 'couldnt': 'could not', 
                        'couldntve': 'could not have', 'didnt': 'did not',
                        'doesnt': 'does not', 'dont': 'do not', 'hadnt': 'had not'
                        , 'hadntve': 'had not have', 'hasnt': 'has not', 'havent': 'have not',
                        'hed': ' he would', 'hedve': 'he would have', 'hell': 'he will',
                        'hellve': 'he will have', 'hes': 'he is', 'howd': 'how did', 'howdy': 
                        'how do you', 'howll': 'how will', 'hows': 'how is', 'id': 'I would', 
                        'idve': 'I would have', 'ill': 'I will', 'illve': 'I will have', 'im': 'I am'
                        , 'ive': 'I have', 'isnt': 'is not', 'itd': 'it would', 'itdve': 'it would have', 
                        'itll': 'it will', 'itllve': 'it will have', 'its': 'it is', 'lets': 'let us', 
                        'maam': 'madam', 'maynt': 'may not', 'mightve': 'might have', 'mightnt': 'might not'
                        , 'mightntve': 'might not have', 'mustve': 'must have', 'mustnt': 'must not', 'mustntve': 'must not have'
                        , 'neednt': 'need not', 'needntve': 'need not have', 'oclock': 'of the clock', 'oughtnt': 'ought not', 'oughtntve': 'ought not have', 'shant': 'shall not', 'shantve': 'shall not have', 'shed': 'she would', 'shedve': 'she would have', 'shell': 'she will', 'shellve': 'she will have', 'shes': 'she is', 'shouldve': 'should have', 'shouldnt': 'should not', 'shouldntve': 'should not have', 'sove': 'so have', 'sos': 'so is', 'thatd': 'that would', 'thatdve': 'that would have', 'thats': 'that is', 'thered': 'there would', 'theredve': 'there would have', 'theres': 'there is', 'theyd': 'they would', 'theydve': 'they would have', 'theyll': 'they will', 'theyllve': 'they will have', 'theyre': 'they are', 'theyve': 'they have', 'tove': 'to have', 'wasnt': 'was not', 'wed': 'we would', 'wedve': 'we would have', 'well': 'we will', 'wellve': 'we will have', 'were': 'we are', 'weve': 'we have', 'werent': 'were not', 'whatll': 'what will', 'whatllve': 'what will have', 'whatre': 'what are', 'whats': 'what is', 'whatve': 'what have', 'whens': 'when is', 'whenve': 'when have', 'whered': 'where did', 'wheres': 'where is', 'whereve': 'where have', 'wholl': 'who will', 'whollve': 'who will have', 'whos': 'who is', 'whove': 'who have', 'whys': 'why is', 'whyve': 'why have', 'willve': 'will have', 'wont': 'will not', 'wontve': 'will not have', 'wouldve': 'would have', 'wouldnt': 'would not', 'wouldntve': 'would not have', 'yall': 'you all', 'yalld': 'you all would', 'yalldve': 'you all would have', 'yallre': 'you all are', 'yallve': 'you all have', 'youd': 'you would', 'youdve': 'you would have', 'youll': 'you will', 'youllve': 'you will have', 'youre': 'you are', 'youve': 'you have'}


greetings=["hi","hello","thanks","thank","sure","alright","ok","please","oh",
           "ok","okay","alright","yes","agree","welcome","hey","question",
           "no","yes","know","need","want","require","morning","afternoon","noon"
           "today","evening","good","having"]












