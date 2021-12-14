import csv
import re

import pandas as pd

data = pd.read_csv("AllData.tsv", delimiter="\t")
tsv_file = open("NewData.tsv", "w", encoding='utf-8')
writer = csv.writer(tsv_file, delimiter="\t")
stopwords = pd.read_csv("arabic.csv")
newfile = []

stopwordsList = stopwords['word'].values.tolist()
emoji = re.compile("["
                  u"\U0001F600-\U0001F64F"  # emoticons
                  u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                  u"\U0001F680-\U0001F6FF"  # transport & map symbols
                  u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                  u"\U00002500-\U00002BEF"  # chinese char
                  u"\U00002702-\U000027B0"
                  u"\U00002702-\U000027B0"
                  u"\U000024C2-\U0001F251"
                  u"\U0001f926-\U0001f937"
                  u"\U00010000-\U0010ffff"
                  u"\u2640-\u2642"
                  u"\u2600-\u2B55"
                  u"\u200d"
                  u"\u23cf"
                  u"\u23e9"
                  u"\u231a"
                  u"\ufe0f"  # dingbats
                  u"\u3030"
                  "]+",re.UNICODE)
englishwords = re.compile(r'\s*[A-Za-z]+\b' )
num = re.compile(r'[0-9\(\)/]+')
special = re.compile('[^\w]+')
underscore = re.compile('[\_]+')
repeated = re.compile(r'(.)\1{1,}', re.IGNORECASE)
aranum = re.compile(r'[٠-٩\(\)/]+')
j = 0
writer.writerow(["type","tweets"])
for i in data['tweets']:
    line = emoji.sub(r'',i)
    line = num.sub('',line)
    line = aranum.sub('',line)
    line = special.sub(' ',line)
    line = underscore.sub(' ',line)
    line = repeated.sub(r'\1',line)
    line = englishwords.sub('', line)
    line = line.rstrip()
    stringList = line.split()
    newtext = [x for x in stringList if x not in stopwordsList]
    new = ' '.join(newtext)
    writer.writerow([data.iloc[j]['type'],new])
    j = j+1
tsv_file.close()
