# 한 문장으로 만들기
import pandas as pd
from tqdm import tqdm as tq

df = pd.read_csv('D:\\Github\\han\\movie_for_you_team\\crawling_data\\cleaned_review.csv')

df.dropna(inplace=True)
df.info()
print(df.head(10))

one_sentences = []
for title in tq(df['title'].unique()):
    temp = df[df['title']==title]
    one_sentence = ' '.join(temp['cleaned_sentences'])
    one_sentences.append(one_sentence)

df_one = pd.DataFrame({'titles':df['title'].unique(), 'reviews':one_sentences})

print(df_one.head())
df_one.info()
df_one.to_csv('./crawling_data/cleaned_review.csv', index= False)