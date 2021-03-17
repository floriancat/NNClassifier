print("Welcome to Florian Catalan's Feature Selection Algorithm")
print("Type in the name of the file to test:")
fileName = input()
#print(fileName)
print("Type the number of the algorithm you want to run")
print("   1) Forward Selection")
print("   2) Backward Elimination")
algorithmSelect = input()
#print(algorithmSelect)

import pandas as pd
import random

df = pd.read_fwf("CS170_SMALLtestdata__51.txt", index_col=0, header=None)
df.head()

print("This dataset has", len(df.columns)-1, "features (not including the class attribute), with", df.shape[0], "instances")

def validation(df, current_features, feature_to_add):
  validation_copy = df
  #code to set features not being used to 0
  numCorrectClass = 0
  for i in validation_copy.shape[0]:

    
  return

def forward_search(df):
    df_copy = df
    current_features = []
    for i in df_copy.columns:
        print('On level', i, 'of the search tree')
        feature_to_add = []
        best_accuracy = 0
        for j in df_copy.columns:
            listCount = current_features.count(j)
            if(listCount == 0):
                print('   Considering adding feature', j)
                accuracy = validation(df_copy, current_features, feature_to_add)
                if(accuracy > best_accuracy):
                    best_accuracy = accuracy
                    feature_to_add = j
        current_features.append(feature_to_add)
        #print('feature to add column:', feature_to_add)
        #print(df_copy[feature_to_add].head())
        #print('current features:', current_features)
        print('On level', i, ', added feature', feature_to_add, 'to current set')

forward_search(df)

#features = [1, 5, 7]
#features.count(2)
