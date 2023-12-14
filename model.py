from huggingface_hub import login

login("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")

# Importing necessary libraries
from transformers import AutoTokenizer, AutoModelForCausalLM

# Loading the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("yentinglin/Taiwan-LLM-7B-v2.0-chat")
model = AutoModelForCausalLM.from_pretrained("yentinglin/Taiwan-LLM-7B-v2.0-chat", load_in_4bit=True)

def generate_text(prompt_text):
    # Encoding the input text to tensor
    input_ids = tokenizer.encode(prompt_text, return_tensors='pt')
    
    # Generating a sequence of text
    output = model.generate(input_ids, max_length=2048, num_beams=5, temperature=0.1, pad_token_id=50256)
    
    # Decoding the generated sequence to text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    
    return generated_text