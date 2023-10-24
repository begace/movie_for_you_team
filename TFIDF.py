import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread
import pickle

df_reviews = pd.read_csv('./crawling_data/cleaned_review.csv')
df_reviews.info()

Tfidf = TfidfVectorizer(sublinear_tf=True)
Tfdif_matrix = Tfidf.fit_transform(df_reviews['reviews'])

print(Tfdif_matrix.shape)

with open('./models/tfidf.pickle', 'wb') as f:
    pickle.dump(Tfidf, f)

mmwrite('./models/Tfidf_movie_review.mtx', Tfdif_matrix)
