import pandas as pd
import random
import math
import numpy as np
from copy import deepcopy

# VALIDATION FOR FORWARD SELECTION
def validationF(df, current_features, feature_to_add):
    all_features = []
    all_features = [0] + current_features
    all_features.append(feature_to_add)
    all_features.sort()
    #print(all_features)
    #if not all_features:
    #    validation_copy = df
    #elif all_features:
    #    validation_copy = df.iloc[:,all_features]
    validation_copy = df[:,all_features]
    #print(validation_copy)
    #validation_copy = df
    #code to set features not being used to 0
    numCorrectClass = 0
    for i in range(0, validation_copy.shape[0]):
        features_to_classify = validation_copy[i,1:]
        label_features = validation_copy[i,0]
        nn_distance = math.inf
        nn_location = math.inf
        for k in range(0, validation_copy.shape[0]):
            if(k != i):
                distance = math.sqrt(sum(pow((features_to_classify - validation_copy[k,1:]), 2)))
                if(distance < nn_distance):
                    nn_distance = distance
                    nn_location = k
                    nn_label = validation_copy[k,0]
                #print("Ask if", i, "is nearest neighbor with", k)
        #print("Looping over i, at location", i)
        #print("Object", i, "is in class", label_features)
        #print("Object", i, "is class", label_features)
        #print("Its nearest neighbor is", nn_location, "which is in class", nn_label)
        if(label_features == nn_label):
            numCorrectClass = numCorrectClass + 1
    return numCorrectClass / validation_copy.shape[0]

# VALIDATION FOR BACKWARDS ELIMINATION
def validationB(df, current_features, feature_to_add):
    all_features = []
    all_features = deepcopy(current_features)
    all_features.remove(feature_to_add)
    all_features.append(0)
    all_features.sort()
    #print(all_features)
    #if not all_features:
    #    validation_copy = df
    #elif all_features:
    #    validation_copy = df.iloc[:,all_features]
    validation_copy = df[:,all_features]
    #print(validation_copy)
    #validation_copy = df
    #code to set features not being used to 0
    numCorrectClass = 0
    for i in range(0, validation_copy.shape[0]):
        features_to_classify = validation_copy[i,1:]
        label_features = validation_copy[i,0]
        nn_distance = math.inf
        nn_location = math.inf
        for k in range(0, validation_copy.shape[0]):
            if(k != i):
                distance = math.sqrt(sum(pow((features_to_classify - validation_copy[k,1:]), 2)))
                if(distance < nn_distance):
                    nn_distance = distance
                    nn_location = k
                    nn_label = validation_copy[k,0]
                #print("Ask if", i, "is nearest neighbor with", k)
        #print("Looping over i, at location", i)
        #print("Object", i, "is in class", label_features)
        #print("Object", i, "is class", label_features)
        #print("Its nearest neighbor is", nn_location, "which is in class", nn_label)
        if(label_features == nn_label):
            numCorrectClass = numCorrectClass + 1
    return numCorrectClass / validation_copy.shape[0]

# FORWARD SELECTION
def forward_search(df):
    #df_copy = df
    current_features = []
    final_best = 0
    final_set = []
    for i in range(1,df.shape[1]): #df.columns[1:]: #_copy.columns[1:]:
        print('On level', i, 'of the search tree')
        feature_to_add = 0
        best_accuracy = 0
        for j in range(1,df.shape[1]): #df.columns[1:]: #_copy.columns[1:]:
            #listCount = current_features.count(j)
            #if(listCount == 0):
            if(current_features.count(j) == 0):
                print('   Considering adding feature', j)
                accuracy = validationF(df, current_features, j) #random.randrange(1, 50, 1)
                if(accuracy > best_accuracy):
                    best_accuracy = accuracy
                    feature_to_add = j
                    print("      Change in accuracy:", best_accuracy)
                    #feature_to_add.clear()
                    #feature_to_add.append(j)
        current_features.append(feature_to_add) #= current_features + feature_to_add
        #print('feature to add column:', feature_to_add)
        #print(df_copy[feature_to_add].head())
        #print('current features:', current_features)
        print('On level', i, ', added feature', feature_to_add, 'to current set')
        print("Current set is", current_features, "with", best_accuracy*100, "% accuracy")
        if(best_accuracy > final_best):
            final_best = best_accuracy
            final_set = current_features.copy()
    print("Best set is", final_set, "with ", final_best*100, "% accuracy")

# BACKWARD ELIMINATION
def backward_search(df):
    #df_copy = df
    current_features = []
    for x in range(1,df.shape[1]):
        current_features.append(x)
    final_best = 0
    final_set = []
    for i in range(1,df.shape[1]): #df.columns[1:]: #_copy.columns[1:]:
        print('On level', i, 'of the search tree')
        feature_to_add = 0
        best_accuracy = 0
        for j in range(1,df.shape[1]): #df.columns[1:]: #_copy.columns[1:]:
            #listCount = current_features.count(j)
            #if(listCount == 0):
            if(current_features.count(j) != 0):
                print('   Considering removing feature', j)
                accuracy = validationB(df, current_features, j) #random.randrange(1, 50, 1)
                if(accuracy > best_accuracy):
                    best_accuracy = accuracy
                    feature_to_add = j
                    print("      Change in accuracy:", best_accuracy)
                    #feature_to_add.clear()
                    #feature_to_add.append(j)
        current_features.remove(feature_to_add) #= current_features + feature_to_add
        #print('feature to add column:', feature_to_add)
        #print(df_copy[feature_to_add].head())
        #print('current features:', current_features)
        print('On level', i, ', removed feature', feature_to_add, 'to current set')
        print("Current set is", current_features, "with", best_accuracy*100, "% accuracy")
        if(best_accuracy > final_best):
            final_best = best_accuracy
            final_set = current_features.copy()
    print("Best set is", final_set, "with ", final_best*100, "% accuracy")

# VALIDATION USING ENTIRE FEATURE SET
def base_validation(df): #, current_features, feature_to_add):
    # base iteration: accuracy using all features
    #all_features = [0,1,2,3,4,5,6,7,8,9,10]
    #print(all_features)
    #if not all_features:
    #    validation_copy = df
    #elif all_features:
    #    validation_copy = df.iloc[:,all_features]
    validation_copy = df#[:,all_features]
    #print(validation_copy)
    #validation_copy = df
    #code to set features not being used to 0
    numCorrectClass = 0
    for i in range(0, validation_copy.shape[0]):
        features_to_classify = validation_copy[i,1:]
        label_features = validation_copy[i,0]
        nn_distance = math.inf
        nn_location = math.inf
        for k in range(0, validation_copy.shape[0]):
            if(k != i):
                distance = math.sqrt(sum(pow((features_to_classify - validation_copy[k,1:]), 2)))
                if(distance < nn_distance):
                    nn_distance = distance
                    nn_location = k
                    nn_label = validation_copy[k,0]
                #print("Ask if", i, "is nearest neighbor with", k)
        #print("Looping over i, at location", i)
        #print("Object", i, "is in class", label_features)
        #print("Object", i, "is class", label_features)
        #print("Its nearest neighbor is", nn_location, "which is in class", nn_label)
        if(label_features == nn_label):
            numCorrectClass = numCorrectClass + 1
    return (numCorrectClass / validation_copy.shape[0])

# BEGINNING PROMPT
print("Welcome to Florian Catalan's Feature Selection Algorithm")
print("Type in the name of the file to test:")
fileName = input()
#print(fileName)
print("Type the number of the algorithm you want to run")
print("   1) Forward Selection")
print("   2) Backward Elimination")
algorithmSelect = input()
#print(algorithmSelect)

df = pd.read_fwf(fileName, header=None, inplace=True).values
print("This dataset has", df.shape[1]-1, "features (not including the class attribute), with", df.shape[0], "instances")
accuracy_w_all_features = base_validation(df) * 100
if(algorithmSelect == '1'):
    print("Running nearest neighbor with all", df.shape[1]-1, "features, using \"leaving-one-out\" evaluation, I get an accuracy of", accuracy_w_all_features, "%")
    forward_search(df)
elif(algorithmSelect == '2'):
    print("Running nearest neighbor with all", df.shape[1]-1, "features, using \"leaving-one-out\" evaluation, I get an accuracy of", accuracy_w_all_features, "%")
    backward_search(df)
else:
    print("Invalid algorithm selection")
#df

#df.iloc[:,0]

#for i in df.columns[1:]:
#    print(i)

#if(algorithmSelect == '1'):
#    forward_search(df)
#elif(algorithmSelect == '2'):
#    backward_search(df)
#else:
#    print("Algorithm not properly selected")

#forward_search(df)

#for i in range(0, df.shape[0]):
#    print(df.iloc[i],"\n")
#df.iloc[0:df.shape[0],]

#df.iloc[2][0]
#validation_copy[i][0]

#df.iloc[0][1:10]
#validation_copy[i][1:10]

#features = []
#features_to_add = [1]
#features = features + features_to_add
#features
#test = df.iloc[:,features]
#print(test)
#test.iloc[1] #features
#test.iloc[0][0] #label

#validation(df, [], 10)

#test = []
#for x in range(1,df.shape[1]):
#    test.append(x)
#test

#base_validation(df)
