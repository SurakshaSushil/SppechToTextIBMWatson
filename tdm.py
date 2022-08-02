from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import csv



def construct_tdm(listOfDocs):
    docs = listOfDocs
    vec = CountVectorizer()
    X = vec.fit_transform(docs)
    df = pd.DataFrame(X.toarray(), columns=vec.get_feature_names())
    print(df.head())
    pf = df.transpose()
    matrix = pf.sum(axis = 1, skipna=True)
    value = list(matrix)
    key = list(pf.index)
    my_dict = {}
    for i in range(len(key)):
        my_dict.update({key[i]:value[i]})
    print(my_dict)
    with open('test.csv', 'w') as f:
        for key in my_dict.keys():
            f.write("%s,%s\n"%(key,my_dict[key]))
    print(sorted(my_dict.items(), key=
    lambda kv: (kv[1], kv[0]), reverse=True))
