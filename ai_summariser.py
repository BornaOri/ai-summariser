import pandas as pd
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash

app = Flask(__name__)

word_limit = 5000

def calculate_length(content):
    words_num = content.split()
    if len(words_num) > word_limit:
        return "Please insert a file of 5000 words or less"
    return "Document fits size"

#def summarise_file(content):
   

@app.route('/upload', methods=["POST"])
def upload_file():
    if "file" not in request.files:
        flash("Please upload a document, that is CSV or TXT.")
        return redirect(url_for('home'))    
    file = request.files['file']
    
    file_ext = os.path.splitext(file.filename)[1].lower()

    if file_ext == ".csv":
        df = pd.read_csv(file)
        file_content = df.to_string(index = False)
    elif file_ext == ".txt":
        file_content = file.read().decode('utf-8')
    else:
        flash("Unsupported filetype, upload a .txt or .csv file.")
        return redirect(url_for('home'))
@app.route('/')
def home():
    return render_template('index.html')





"""def calculate_length(file):
    if file == ".csv":
        #later can change to make the function that would repeat the first 2 lines of this function 
        df = pd.read_csv("MOCK_DATA.csv")
        converted_strings = df.to_string(index=False)
        document_length = len(converted_strings.split())
        if document_length > word_limit:
            raise ValueError(f"document exceeds {word_limit} words! Please shorten it.")
        return print("CSV file checked successfully")
    print("wong") 
    if file == ".txt":
        with open("MOCK_DATA.txt", "r", encoding = "utf-8") as file:
            content = file.read()
            document_length = len(content.split())
            if document_length > word_limit:
                raise ValueError(f"document exceeds {word_limit} words! Please shorten it.")
        return print("TXT file checked successfully")"""


#file_path = "MOCK_DATA.txt"
#file_extension = os.path.splitext(file_path)[1].lower()
#print(file_extension)
#calculate_length(file_extension)

