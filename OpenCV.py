import cv2
from cv2 import ml
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

print(len(ldata))
print(len(ltarget))

# svm classification
param = dict( kernel_type = ml.SVM_RBF,
	      svm_type = ml.SVM_C_SVC,
	      C = 1000, gamma = 0.01)

# parse dataset
digit = np.array(np.fromstring(ldata[0],sep=","))

for line in ldata[1:]:
    try:
        sample = np.fromstring(line,sep=",")
        digit = np.vstack((digit,sample))
    except:
        pass

t = np.array(ltarget)


x,y = digit.astype(np.float32),t.astype(np.int32)

svm = ml.SVM_create()
svm.setC(1000)
svm.setGamma(0.01)
svm.setKernel(ml.SVM_RBF)
svm.setType(ml.SVM_C_SVC)

svm.train(x,ml.ROW_SAMPLE,y)


print("TRAINED")

print(len(svm.getSupportVectors()))

# test
lines = open("test.csv").read().split("\n")

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
    
print(len(ldata))
print(len(ltarget))

questions = np.array(np.fromstring(ldata[0],sep=","))
answers = np.array(ltarget)

for q in ldata[1:]:
    try:
        q1 = np.fromstring(q,sep=",")
        questions = np.vstack((questions,q1))
    except:
        pass
print("PREDICTING")

predicted = svm.predict(questions.astype(np.float32))
