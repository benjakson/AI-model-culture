from easynmt import EasyNMT
import pandas as pd
# Define the model
bart_en = EasyNMT('m2m_100_1.2B')

# Load the Excel file
def load_excel(file_path):
    return pd.read_excel(file_path)

# Save the Excel file
def save_excel(dataframe, file_path):
    dataframe.to_excel(file_path, index=False)

# Main function
def process_excel(file_path):
    # Load the data
    df = load_excel(file_path)
    
    # Display columns to the user and let them choose one
    print("Available columns:")
    for idx, col in enumerate(df.columns):
        print(f"{idx}: {col}")

    col_index = int(input("Enter the index of the column you want to process: "))
    selected_col = df.columns[col_index]

    # Initialize a new column for the processed data
    new_column_name = f"{selected_col}_processed"
    df[new_column_name] = None

    # Iterate through each row of the selected column
    for i in range(len(df)):
        original_value = df.at[i, selected_col]
        processed_value = bart_en.translate(str(original_value), source_lang = 'no', target_lang='en')
        df.at[i, new_column_name] = processed_value
        
        if i%15 == 0:
            print(f"{i}/{len(df)} Translated!")
            print("Org -",original_value)
            print("Translated -",processed_value)
            
    # Save the updated DataFrame back to Excel
    save_excel(df, file_path)
    print(f"Processed data has been saved to {file_path} with the new column '{new_column_name}'.")


    # Save the updated DataFrame back to Excel
    save_excel(df, file_path)
    print(f"Processed data has been saved to {file_path} with the new column '{new_column_name}'.")
    return "done"


file_path = 'Excel document with columns to translate'
process_excel(file_path)