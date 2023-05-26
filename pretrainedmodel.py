from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from torch.utils.data import Dataset, DataLoader

class CloudFormationDataset(Dataset):
    def __init__(self, templates, tokenizer, block_size):
        self.tokenizer = tokenizer
        self.block_size = block_size
        self.examples = []
        
        for template in templates:
            tokens = tokenizer.encode(template)
            self.examples.extend(tokens[i:i+block_size] for i in range(0, len(tokens), block_size))

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, i):
        return torch.tensor(self.examples[i])

# Initialize a pretrained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Create a dataset from your templates
templates = [...]  # Replace with your list of templates
dataset = CloudFormationDataset(templates, tokenizer, block_size=128)

# Create a dataloader
dataloader = DataLoader(dataset, batch_size=1, shuffle=True)

# Train the model
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model.to(device)

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
epochs = 5
for epoch in range(epochs):
    for batch in dataloader:
        batch = batch.to(device)
        outputs = model(batch, labels=batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

# Save the fine-tuned model
model.save_pretrained('my_model')
