import create_data
import LDA
import argparse



parser = argparse.ArgumentParser(description='Enter number of topics')
parser.add_argument('--n_topics', help='Number of Topics')

args = parser.parse_args()

path="news-articles.txt"

create_data.create(path)
LDA.modeller(args.n_topics)