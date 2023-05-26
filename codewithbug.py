'''
Created on 26 May 2023
s
@author: jimli
'''


from transformers import BartTokenizer, BartForConditionalGeneration
from torch import cuda

# Load pre-trained model and tokenizer
model_name = 'facebook/bart-large-cnn'
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Check if GPU is available and if not, use CPU
device = 'cuda' if cuda.is_available() else 'cpu'
model.to(device)

# Your text to be summarized
text = """
long ago , the mice had a general council to consider what measures they could take to outwit their common enemy , the cat . some said this , and some said that but at last a young mouse got up and said he had a proposal to make , which he thought would meet the case . you will all agree , said he , that our chief danger consists in the sly and treacherous manner in which the enemy approaches us . now , if we could receive some signal of her approach , we could easily escape from her . i venture , therefore , to propose that a small bell be procured , and attached by a ribbon round the neck of the cat . by this means we should always know when she was about , and could easily retire while she was in the neighbourhood . this proposal met with general applause , until an old mouse got up and said that is all very well , but who is to bell the cat ? the mice looked at one another and nobody spoke . then the old mouse said it is easy to propose impossible remedies
"""

# Tokenize the text
inputs = tokenizer([text], max_length=1024, return_tensors='pt')

# Generate the summary
summary_ids = model.generate(inputs['input_ids'].to(device), num_beams=4, max_length=5, early_stopping=True)
summary = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]

print(summary)
