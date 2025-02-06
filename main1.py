"""
CSC790 Assignment 1
Serene Zan

Instructions:
Open the terminal in the "HW02 Zan" folder.
Type "py .\main1.py" on the command line.
The function calls for displaying n most frequent terms and size have been commented out.
"""


import nltk as tk
import sys
import json
import os
tk.download('punkt')



def read_folder(folder_path):
    """
    Reads document files from the folder.
    Parameters:
    1. folder_path : str
        Path of the folder containing documents.
    Returns:
    1. docs : list
        A list of text strings read from the docucuments.
    """
    docs = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            docs.append(file.read())

    return docs



def read_file(file_path):
    """
    Reads strings from the file and stores in a list.
    Parameters:
    1. file_path : str
        Path of the stop words folder.
    Returns:
    1. doc : list
        A list of strings read from the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        doc = file.read().splitlines()

    return doc



def tokenization(doc):
    """
    Tokenizes the string by calling the nltk method.
    Parameters:
    1. doc : string
        A text string.
    Returns:
    1. tokens : list
        A list of tokenzied terms.
    """
    tokens = tk.word_tokenize(doc)
    return tokens




def removing(tokens, to_be_removed):
    """
    Removing stop words/punctuation from the list of tokens.
    Parameters:
    1. tokens : list
        A list of tokenized terms.
    2. to_be_removed : list
        A list of stopwords/punctuation to be removed.
    Returns:
    1. processed_tokens : list
        A list of tokenized terms without stop words.
    """
    processed_tokens = [word for word in tokens if not word in to_be_removed]
    return processed_tokens



def stemming(tokens):
    """
    Stemming the tokens to match.
    Parameters:
    1. tokens : list
        A list of tokenized terms.
    Returns:
    1. stem_tokens : list
        A list of tokenized and stemmed terms without stopwords or punctuations.
    """
    stem_tokens = [tk.stem.PorterStemmer().stem(word) for word in tokens]
    return stem_tokens



def preprocess_doc(doc, stop_words, punctuation):
    """
    Preprocess the terms by calling functions for tokenization, stemming, and removing stopwords and punctuations.
    Parameters:
    1. doc : string
        A text string.
    2. stop_words : list
        A list of stop words.
    3. punctuation : list
        A list of punctuations.
    Returns:
    1. processed_tokens : list
        A list of lowercase tokenized, stemmed terms without stopwords or punctuations.
    """
    # Tokenization.
    tokens = tokenization(doc)
    # Converting to lowercase.
    tokens = [word.lower() for word in tokens]
    # Removes punctuation.
    no_punctuation = removing(tokens, punctuation)
    # Removes stop words.
    no_stopwords = removing(no_punctuation, stop_words)
    # Stemming.
    processed_tokens = stemming(no_stopwords)

    return processed_tokens



def create_inverted_index(docs, stop_words, punctuation):
    """
    Creates the inverted index in the dictionary data structure after passing the docs to the preprocessing function.
    Parameters:
    1. docs : list
        A list of string texts.
    2. stop_words : list
        A list of stop words.
    3. punctuation : list
        A list of punctuation.
    Returns:
    1. inverted_index_dict : dictionary
        The dictionary containing the tokens and their postings.
    """
    inverted_index_dict = {}
    # Iterates over the docs.
    for doc_id, doc in enumerate(docs):
        tokens = preprocess_doc(doc, stop_words, punctuation)
        # Only appends the doc_id once per document for each token.
        for token in set(tokens):
            if token not in inverted_index_dict:
                inverted_index_dict[token] = []
            inverted_index_dict[token].append(doc_id)

    return inverted_index_dict



def display_info():
    """
    Displays course and name.
    """
    print("\n=================== CSC790-IR Homework 02 ===================")
    print("First Name: Serene")
    print("Last Name: Zan")
    print("============================================================")



def display_tokens(inverted_index_dict, number):
    """
    Displays the top n frequently appearded tokens.
    Parameters:
    1. inverted_index_dict : dictionary
        A dictionary of tokens and postings.
    2. number : int
        The number of tokens we wish to display.
    """
    sorted_toks = sorted(inverted_index_dict.items(), key=lambda x: len(x[1]), reverse=True)[:number]
    print(f"\nDisplaying top {number} terms:")
    for token, posting in sorted_toks:
        print(f"{token}: {len(posting)} occurrences")



def display_size(inverted_index_dict):
    size_bytes = sys.getsizeof(inverted_index_dict)
    size_mb = size_bytes / (1024 * 1024)
    print(f"\nSize in Bytes: {size_bytes} bytes")
    print(f"Size in MB: {size_mb:} MB")



def save_file(inverted_index_dict, save_path):
    """
    Saves the inverted index to a new file.
    Parameters:
    1. inverted_index_dict : dictionary
        The dictionary of tokens and postings.
    """
    with open(save_path, 'w') as json_file:
        json.dump(inverted_index_dict, json_file)
    print("\nThe inverted intex is saved successfully in folder.")



def main():
    if __name__ == "__main__":
        
        # Reads from files.
        documents_folder_path = "documents"
        stopwords_path = "stopwords.txt"
        punctuation_path = "special-chars.txt"
        docs = read_folder(documents_folder_path)
        stop_words = read_file(stopwords_path)
        punctuation = read_file(punctuation_path)

        # Creates the dictionary for inverted index.
        inverted_index_dict = create_inverted_index(docs, stop_words, punctuation)
        
        display_info()
        # Can change the value assigned to "number" to display more or less tokens.
        # number = 20
        # display_tokens(inverted_index_dict, number)
        # display_size(inverted_index_dict)
        # Can change the path for saving file.
        save_path = 'inverted_index.json'
        save_file(inverted_index_dict, save_path)



main()