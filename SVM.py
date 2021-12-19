import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import cross_val_score
from sklearn import svm
from sklearn import preprocessing

#load data
data = pd.read_csv("NewData.tsv", delimiter="\t")
# Feature Engineering with TFIDF
word_vectorizer = TfidfVectorizer(
    sublinear_tf=True,
    strip_accents='unicode',
    analyzer='word',
    ngram_range=(1, 1),
    max_features =10000)

unigramdataGet= word_vectorizer.fit_transform(data['tweets'].astype('str'))
unigramdataGet = unigramdataGet.toarray()

vocab = word_vectorizer.get_feature_names()
unigramdata_features=pd.DataFrame(np.round(unigramdataGet, 1), columns=vocab)
unigramdata_features[unigramdata_features>0] = 1
#data feature and target
row=unigramdataGet
typecol=data['type']

# label_encoder object knows how to understand word labels.
pro= preprocessing.LabelEncoder()
encpro=pro.fit_transform(data['type'])
data['type'] = encpro

#svm
SVMmodel=svm.SVC(C=1,kernel="linear",random_state=20)

#cross validation for splitting and shuffling data
cross_val_svm = cross_val_score(SVMmodel,row,typecol,cv=20)
print(format(np.mean(cross_val_svm)))
