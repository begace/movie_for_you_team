# 201309_201609_reviews0.csv
# 201309_201609_reviews1.csv
# 201610_201809_reviews.csv
# 201810_202009_reviews.csv
# 202010_202309_reviews.csv

import pandas as pd
import glob

data_paths = glob.glob('./crawling_data/*')
print(data_paths)

df = pd.DataFrame()
for npath in data_paths:
    df_temp = pd.read_csv(npath)
    df_temp.dropna(inplace=True)
    df_temp.drop_duplicates(inplace=True)
    df = pd.concat([df,df_temp], ignore_index=True)
df.drop_duplicates(inplace=True)

df.info()
df.to_csv('./crawling_data/merged_review.csv')