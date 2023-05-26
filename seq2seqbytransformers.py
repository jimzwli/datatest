from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-de")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-de")

# Tokenize input (replace with your requirements)
input_text = "Here is some input text"
input_tokenized = tokenizer.encode(input_text, return_tensors='pt')

# Generate output sequence
output_tokenized = model.generate(input_tokenized)
output_text = tokenizer.decode(output_tokenized[0], skip_special_tokens=True)

print(output_text)
