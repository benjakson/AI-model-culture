import pandas as pd
import openai
from openai import OpenAI

# Function to load the OpenAI API key


# Display AI model choices and ask the user to select one
print("Please select an AI model to use:")
print("0: text-davinci-003")
print("1: gpt-3.5-turbo")
print("2: gpt-4")
model_choices = ["text-davinci-003", "gpt-3.5-turbo", "gpt-4"]
model_choice = int(input("Enter the number corresponding to the AI model (0, 1, or 2): "))
model_name = model_choices[model_choice]


# Define the zero-shot prompt template
#Change the template to Norwegian or English
prompt_template = """Question: {0}
Answer:"""

client = OpenAI()
# A function that will take care of generating the output
def generate(text):
    prompt = prompt_template.format(text)
    if model_name == "text-davinci-003":
        response = openai.Completion.create(
            engine=model_name,
            prompt=prompt,
            max_tokens=64,
            n=1,
            stop=None,
            temperature=0.0
        )
        return response.choices[0].text.strip()
    else:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful Assistant"}, #Change the prompt to Norwegian or English
                {"role": "user", "content": prompt}
            ],
            max_tokens=64,
            n=1,
            stop=None,
            temperature=0.0
        )
        return response.choices[0].message.content

# Read the CSV file
input_csv_path = input("Enter questions csv filepath: ")
df = pd.read_csv(input_csv_path)
results = []
count = 0
# Generate answers for each Norwegian question 
for question in df['Question_NO']:
    generated_answer = generate(question)
    results.append({'Question_NO': question, 'Generated_Answer': generated_answer}) 
  
    if count % 10 == 0: 
        print(count, "/",len(df['Question_NO']), "Completed")
        print(generated_answer)
    count += 1 


# # Generate answers for each English question
# for question in df['Question_EN']:
#     generated_answer = generate(question)
#     results.append({'Question_EN': question, 'Generated_Answer': generated_answer}) 
  
#     if count % 10 == 0: 
#         print(count, "/",len(df['Question_EN']), "Completed")
#         print(generated_answer)
#     count += 1 


# Create a new DataFrame from the results
output_df = pd.DataFrame(results)
# Save the output DataFrame to a new CSV file
output_csv_path = input("Enter output filepath (with .csv extension): ")
output_df.to_csv(output_csv_path, index=False)

print(f"Generated answers saved to {output_csv_path}")
