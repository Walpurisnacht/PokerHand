import numpy as np
import sklearn
import os

#SVM import
from sklearn import svm


#Set up ML and scikit-learn
clf = svm.SVC(gamma=0.01, C=100)

#Training data(digits: questions, target: answers)
#digits = open("trainD.csv").read().split("\n")
#target = open("trainR.csv").read().split("\n")

print("Digits: ",len(digits))
print("Target: ",len(target))

#Init numpy arrays
digitsD = np.array(np.fromstring(digits[0], sep=","))

#Parse digits var
for line in digits[0:]:
    try:
        sample = np.fromstring(line, sep=",")
        digitsD = np.vstack((digitsD,sample))
    except:
        pass

#Parse target var
t = np.array(target)

"""------------Training------------"""

#Training
x,y = digitsD,t
print("Training...")
clf.fit(x,y)
print("DONE Training")

#Answer: 1
print("Prediction: ",clf.predict(np.array([1,2,1,3,1,4,1,5,1,6])))
