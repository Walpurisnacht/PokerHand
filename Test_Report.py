import sklearn
from sklearn import svm
from sklearn.multiclass import OneVsRestClassifier
import numpy as np
import cProfile
import re

# prepare dataset
lines = open("train.csv").read().split("\n")

ldata = []
ltarget = []

for line in lines:
    text = ""
    line = line.split(",")
    for data in line[:-1]:
        text += data
        text += ","
    if text != "":
        ldata.append(text[:-1])
        ltarget.append(line[-1])
    
print(ldata[-1])
print(len(ldata))
print(ltarget[-1])
print(len(ltarget))

# svm classification
clf = svm.SVC(C=1000,cache_size=1000,gamma=0.1)
#clf = svm.LinearSVC()
print(clf)

digit = np.array(np.fromstring(ldata[0],sep=","))

for line in ldata[1:]:
    try:
        sample = np.fromstring(line,sep=",")
        digit = np.vstack((digit,sample))
    except:
        pass

t = np.array(ltarget)

x,y = digit,t
print(x[-1])
print(len(x))
print(y[-1])
print(len(y))
cProfile.run('clf.fit(x,y)')

print("TRAINED")


# test

lines = open("test_temp.csv").read().split("\n")

ldata = []
ltarget = []

for line in lines:
    text = ""
    line = line.split(",")
    for data in line[:-1]:
        text += data
        text += ","
    if text != "":
        ldata.append(text[:-1])
        ltarget.append(line[-1])
    
print(ldata[-1])
print(len(ldata))
print(ltarget[-1])
print(len(ltarget))

questions = np.array(np.fromstring(ldata[0],sep=","))
answers = np.array(ltarget)

for q in ldata[1:]:
    try:
        q1 = np.fromstring(q,sep=",")
        questions = np.vstack((questions,q1))
    except:
        pass

cProfile.run('clf.predict(questions)')
predicted = clf.predict(questions)
        
target_names = ['Nothing','One pair','Two pair','Three of a kind',
                'Straight','Flush','Full house','Four of a kind',
                'Straight flush','Royal flush']

# performance
print ("Classification report for %s" % clf)
print (sklearn.metrics.classification_report(answers, predicted))

