import csv

import pandas as pd
df_negative =pd.read_csv("train_Arabic_tweets_negative.tsv", delimiter="\t")
df_positive =pd.read_csv("train_Arabic_tweets_positive.tsv", delimiter="\t")


tsv_file = open("AllData.tsv", "a", encoding='utf-8')
writer = csv.writer(tsv_file, delimiter="\t")
for i in range(len(df_positive)):
    r = list(df_positive.loc[i, :])
    writer.writerow(r)
for i in range(len(df_negative)):
    r = list(df_negative.loc[i, :])
    writer.writerow(r)
tsv_file.close()
