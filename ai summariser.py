import pandas as pd
import os

word_limit = 5000




def calculate_length(file):
    if file == ".csv":
        #later can change to make the function that would repeat the first 2 lines of this function 
        df = pd.read_csv(r"C:\Users\Borna\OneDrive\Desktop\MOCK_DATA.csv")
        converted_strings = df.to_string(index=False)
        document_length = len(converted_strings.split())
        if document_length > word_limit:
            raise ValueError(f"document exceeds {word_limit} words! Please shorten it.")
        return print("CSV file checked successfully")
    print("wong") 
    if file == ".txt":
        with open(r"C:\Users\Borna\OneDrive\Desktop\MOCK_DATA.txt", "r", encoding = "utf-8") as file:
            content = file.read()
            document_length = len(content.split())
            if document_length > word_limit:
                raise ValueError(f"document exceeds {word_limit} words! Please shorten it.")
        return print("TXT file checked successfully")



file_path = r"C:\Users\Borna\OneDrive\Desktop\MOCK_DATA.txt"
file_extension = os.path.splitext(file_path)[1].lower()
print(file_extension)
calculate_length(file_extension)