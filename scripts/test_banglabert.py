from transformers import AutoTokenizer, AutoModel

MODEL_NAME = "csebuetnlp/banglabert"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

print("Loading model...")
model = AutoModel.from_pretrained(MODEL_NAME)

print("Success!")
print(model.config.hidden_size)