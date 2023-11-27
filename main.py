import requests
import json
import pickle

with open('classMap.pkl', 'rb') as f:
    classMap = pickle.load(f)


print(classMap['AEB3510'])

