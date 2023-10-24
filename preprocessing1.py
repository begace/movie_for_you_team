import pandas as pd
from konlpy.tag import Okt
import re
from tqdm import tqdm as tqdm_progress

df = pd.read_csv('D:\\Github\\han\\movie_for_you_team\\final_review_0.csv')
df.info()

okt = Okt()

df_stopwords = pd.read_csv('./stopwords.csv')
stopwords = list(df_stopwords['stopword'])
cleaned_sentences = []

for review in tqdm_progress(df.review):
    review = re.sub('[^가-힣]',' ', review)
    tokened_review = okt.pos(review, stem= True)

    df_token = pd.DataFrame(tokened_review, columns=['word', 'class'])
    df_token = df_token[(df_token['class']=='Noun') |
                        (df_token['class']=='Verb') |
                        (df_token['class']=='Adjective')]

    words = []
    for word in df_token.word:
        if 1 < len(word):
            if word not in stopwords:
                words.append(word)

    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)

df['cleaned_sentences'] = cleaned_sentences
df = df[['title', 'cleaned_sentences']]
print(df.head())
df.info()

df.to_csv('./crawling_data/cleaned_review.csv', index_label=False)