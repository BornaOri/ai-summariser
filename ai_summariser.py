import pandas as pd
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, session
from openai import OpenAI
from dotenv import load_dotenv
client = OpenAI(
  api_key= os.getenv("CHATGPT_API_KEY")
)

app = Flask(__name__)
app.secret_key = os.urandom(24)
word_limit = 5000
contents = ""

def calculate_length(content):
    words_num = content.split()
    if len(words_num) > word_limit:
        return "Please insert a file of 5000 words or less"
    
    return "Document fits size"

#def summarise_file(content):
  

@app.route('/upload', methods=["POST"])
def upload_file():
    if "file" not in request.files or request.files['file'].filename == '':
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
    limit_status = calculate_length(file_content)
    if limit_status != "Document fits size":
        flash(limit_status)
        return redirect(url_for('home'))

    flash("File uploaded and processed")
    
    flash(contents)
    session['contents'] = file_content
    return redirect(url_for('AI_summary'))

@app.route('/summary_page')
def AI_summary():
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        store = True,
        messages= [
                {"role": "system", "content":"You are a kawaii e-girl that uwuifies and summarises text for revision purposes"},
                {"role": "user", "content": contents}
        ]
    )
    summary = completion['choices'][0]['message']['content']
    return render_template('summary.html', summary = summary)
    #send to AI and recieve the feedback 

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)



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

