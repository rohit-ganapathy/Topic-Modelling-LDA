from gensim.models import LdaMulticore as LDA
import os
import argparse



parser = argparse.ArgumentParser(description='View generated topics')
parser.add_argument('--n_topics', help='Number of Topics')
parser.add_argument('--gram', help='unigram or both')
args = parser.parse_args()

model=LDA.load(os.getcwd() +"/LDA models/{}/{}-topics".format(args.gram,args.n_topics))

for (a,b) in model.show_topics():
    print("Topic-{} \n".format(a))
    print(b)
    print("\n")
    