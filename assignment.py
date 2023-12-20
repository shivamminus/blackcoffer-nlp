from bs4 import BeautifulSoup
import os
import requests
import pandas as pd
import nltk
import re


def read_excel_file():
    file = pd.read_excel("Input.xlsx")
    url_list = [{k:v} for k,v in file.iloc[:,[0,1]].values]

    for file_obj in url_list:
        file_name = list(file_obj.keys())[0]
        url = list(file_obj.values())[0]
        print("FILE NAME: ", file_name)
        print("URL:", url)
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        text = soup.text
        # print(soup.title)
        
        with open(f"data\{file_name}.txt", "w", encoding="utf-8") as f:
            f.write(text)
            
        
def load_custom_stopwords(directory_path):
    # nltk.download('stopwords')
    
    custom_stopwords = set()

    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return custom_stopwords

    # Loop through files in the directory
    for filename in os.listdir(directory_path):
        # if filename.endswith("_stopwords.txt"):
        file_path = os.path.join(directory_path, filename)
        print(file_path)
        # Read stopwords from the file and add them to the set
        with open(file_path, "r") as sw_file:
            stopwords_list = sw_file.readlines()
            stopwords_list = map(lambda s: s.strip(), stopwords_list)
            custom_stopwords.update(stopwords_list)

    return custom_stopwords

def cleaning_using_stopwords(custom_stopwords):
    
    for file in os.listdir("data/"):
        print(file)
        words=[]
        with open("data/" + file, "r", encoding="utf-8") as f:
            words.extend([text.strip() for text in f.readlines() if text.strip() != ''])
        combined_text = ' '.join(words)
        words = combined_text.split()
        print(words)
        
        filtered_words = [word for word in words if word.lower() not in custom_stopwords]
        filtered_text = ' '.join(filtered_words)
        
        with open("data/" + file, "w", encoding="utf-8") as f:
            f.write(filtered_text)
        


if __name__ == "__main__":
    # read_excel_file()
    stopwords_directory = r"StopWords/"
    # master_dictionary = 
    custom_stopwords = load_and_parsing_through_stopwords(stopwords_directory)
    
    cleaning_using_stopwords(custom_stopwords)
    
    # print(custom_stopwords)
    
    
    