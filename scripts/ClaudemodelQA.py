import pandas as pd
import anthropic
from anthropic import Anthropic

# Function to load the Anthropic API key
def load_anthropic_api_key():
    return "Enter Your API Key"  # Replace with your actual Anthropic API key

# Initialize the Anthropic client
client = Anthropic(api_key=load_anthropic_api_key())

# Display AI model choices and ask the user to select one
print("Please select an AI model to use:")
print("0: claude-3-haiku")
print("1: claude-3-opus")
print("2: claude-3-5-sonnet")
model_choices = ["claude-3-haiku-20240307", "claude-3-opus-20240229", "claude-3-5-sonnet-20240620"]
model_choice = int(input("Enter the number corresponding to the AI model (0, 1, or 2): "))
model_name = model_choices[model_choice]

# Define the zero-shot prompt template
prompt_template = """Question: {0}
Answer:"""

# A function that will take care of generating the output
def generate(text):
    prompt = prompt_template.format(text)
    response = client.completions.create(
        model=model_name,
        prompt=prompt,
        max_tokens_to_sample=64,
        stop_sequences=["\n\n"],
        temperature=0.0
    )
    return response['completion'].strip()

# Read the CSV file
input_csv_path = input("Enter questions csv filepath: ")
df = pd.read_csv(input_csv_path)
results = []
count = 0

# Generate answers for each question
for question in df['Question_EN']:
    generated_answer = generate(question)
    results.append({'Question_EN': question, 'Generated_Answer': generated_answer}) 
  
    if count % 10 == 0: 
        print(count, "/", len(df['Question_EN']), "Completed")
        print(generated_answer)
    count += 1 

# Create a new DataFrame from the results
output_df = pd.DataFrame(results)

# Save the output DataFrame to a new CSV file
output_csv_path = input("Enter output filepath (with .csv extension): ")
output_df.to_csv(output_csv_path, index=False)

print(f"Generated answers saved to {output_csv_path}")
