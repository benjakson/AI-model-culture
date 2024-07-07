import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Function to load the tokenizer and model based on user choice
def load_model(model_choice):
    models = [
        "norallm/norBLOOM-7b-scratch",
        "norallm/normistral-7b-scratch",
        "norallm/normistral-7b-warm",
        "norallm/normistral-7b-warm-instruct"
    ]
    model_name = models[model_choice]
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map='auto', load_in_8bit=True, torch_dtype=torch.bfloat16)
    return tokenizer, model

# Display AI model choices and ask the user to select one
print("Please select an AI model to use:")
print("0: norallm/norBLOOM-7b-scratch")
print("1: norallm/normistral-7b-scratch")
print("2: norallm/normistral-7b-warm")
print("3: norallm/normistral-7b-warm-instruct")
model_choice = int(input("Enter the number corresponding to the AI model (0, 1, 2, or 3): "))

# Load the selected tokenizer and model
tokenizer, model = load_model(model_choice)

# Define the zero-shot prompt template
prompt = """Spørsmål: {0}
Svar:"""

# A function that will take care of generating the output
@torch.no_grad()
def generate(text):
    text = prompt.format(text)
    input_ids = tokenizer(text, return_tensors='pt').input_ids.cuda()
    prediction = model.generate(
        input_ids,
        max_new_tokens=64,
        do_sample=False,
        eos_token_id=tokenizer('\n').input_ids
    )
    return tokenizer.decode(prediction[0, input_ids.size(1):]).strip()

# Read the CSV file
input_csv_path = input("Enter questions csv filepath:")
df = pd.read_csv(input_csv_path)
results = []

# Generate answers for each Norwegian question
for question in df['Question_NO']:
    generated_answer = generate(question)
    results.append({'Question_NO': question, 'Generated_Answer': generated_answer})

# # Generate answers for each English question
# for question in df['Question_EN']:
#     generated_answer = generate(question)
#     results.append({'Question_EN': question, 'Generated_Answer': generated_answer})


# Create a new DataFrame from the results
output_df = pd.DataFrame(results)
# Save the output DataFrame to a new CSV file
output_csv_path = input("Enter output Filepath w/ .csv: ") # Replace with your desired output file path
output_df.to_csv(output_csv_path, index=False)

print(f"Generated answers saved to {output_csv_path}")