import sklearn
from sklearn import svm
import numpy as np

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
clf = svm.SVC(gamma=0.01, C=100)

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
clf.fit(x,y)

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

predicted = clf.predict(questions)
        
target_names = ['Nothing','One pair','Two pair','Three of a kind',
                'Straight','Flush','Full house','Four of a kind',
                'Straight flush','Royal flush']

# performance
print ("Classification report for %s" % clf)
print (sklearn.metrics.classification_report(answers, predicted))

