import torch
from transformers import pipeline 
import sentencepiece as spm 

print(torch.cuda.is_available())


classifier = pipeline('sentiment-analysis') 
results = classifier(["We are very happy to show you the 🤗 Transformers library.", 
           "We hope you don't hate it."]) 
for result in results: 
    print(f"label: {result['label']}, with score: {round(result['score'], 4)}")

