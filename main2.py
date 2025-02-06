"""
CSC790 Assignment 2
Serene Zan

Instructions:
Open the terminal in the "HW02 Zan" folder.
First type "py .\main1.py" to run the homework 1 part and generate inverted index.
Type "py .\main2.py" to run the query related part of the assignemtn.
"""


import nltk as tk
import json



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



def load_index(file_path):
    """
    Load inverted index from the JSON file and stores in a dictionary.
    Parameters:
    1. file_path : str
        Path of the inverted index file.
    Returns:
    1. inverted_index : dict
        A dictionary of inverted index.
    """
    with open(file_path, 'r') as file:
        inverted_index = json.load(file)

    return inverted_index



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
    1. result : list
        A list of lowercase tokenized, stemmed terms without stopwords or punctuations.
    """
    result = []
    for str in doc:
        # Tokenization.
        tokens = tokenization(str)
        # Converting to lowercase.
        tokens = [word.lower() for word in tokens]
        # Removes punctuation.
        no_punctuation = removing(tokens, punctuation)
        # Removes stop words.
        no_stopwords = removing(no_punctuation, stop_words)
        # Stemming.
        processed_tokens = stemming(no_stopwords)
        result.append(processed_tokens)

    return result



def query_result(query, inverted_index):
    """
    Generates the docs number by intersection and union.
    Parameters:
    1. query : string
        A query string.
    2. inverted_index : dictionary
        The dictionary containing tokens and document number.
    Returns:
    1. docs_number : list
        A list of document numbers.
    """
    query_list = query.split()
    num = set(inverted_index[query_list[0]])
    for i in range(0, len(query_list)-2, 2):
        if query_list[i+1] == "AND":
            num = set(num.intersection(inverted_index[query_list[i+2]]))
        elif query_list[i+1] == "OR":
            num = set(num.union(inverted_index[query_list[i+2]]))
    docs_number = list(num)
    return docs_number



def generate_result(query):
    """
    Generates all possible query combinations.
    Parameters:
    1. query : list
        A list of query tokens.
    Returns:
    1. result : list
        A list of lists of all query combinations.
    """
    result = []
    if len(query) == 1:
        result = query
    if len(query) == 2:
        result.append(query[0] + " AND " + query[1])
        result.append(query[0] + " OR " + query[1])
    if len(query) == 3:
        result.append(query[0] + " AND " + query[1] + " AND " + query[2])
        result.append(query[0] + " AND " + query[1] + " OR " + query[2])
        result.append(query[0] + " OR " + query[1] + " AND " + query[2])
        result.append(query[0] + " OR " + query[1] + " OR " + query[2])
    if len(query) == 4:
        result.append(query[0] + " AND " + query[1] + " AND " + query[2] + " AND " + query[3])
        result.append(query[0] + " AND " + query[1] + " OR " + query[2] + " AND " + query[3])
        result.append(query[0] + " AND " + query[1] + " AND " + query[2] + " OR " + query[3])
        result.append(query[0] + " AND " + query[1] + " OR " + query[2] + " OR " + query[3])
        result.append(query[0] + " OR " + query[1] + " AND " + query[2] + " AND " + query[3])
        result.append(query[0] + " OR " + query[1] + " OR " + query[2] + " AND " + query[3])
        result.append(query[0] + " OR " + query[1] + " AND " + query[2] + " OR " + query[3])
        result.append(query[0] + " OR " + query[1] + " OR " + query[2] + " OR " + query[3])
    
    return result



def display_info():
    """
    Displays course and name.
    """
    print("\n=================== CSC790-IR Homework 02 ===================")
    print("First Name: Serene")
    print("Last Name: Zan")
    print("============================================================")



def display_query(queries, all_results):
    """
    Displays result for each query.
    Parameters:
    1. queries : list
        A list of query combintions.
    2. all_result : dictionary
        A dictionary with query combination as keys and list of document number as value.
    """
    for query in queries:
        print(f"============= Results for: {query} =================")
        doc_nums = sorted(all_results[query])
        for doc_num in doc_nums:
            print(f"file {doc_num}")
        print("==================================================")
        


def main():
    if __name__ == "__main__":

        # Reads from files.
        inverted_index_path = "inverted_index.json"
        queries_path = "queries.txt"
        stopwords_path = "stopwords.txt"
        punctuation_path = "special-chars.txt"
        stop_words = read_file(stopwords_path)
        punctuation = read_file(punctuation_path)
        queries = read_file(queries_path)
        inverted_index = load_index(inverted_index_path)

        # Process the query.
        processed_queries = preprocess_doc(queries, stop_words, punctuation)
        print(processed_queries)
        display_info()

        # Generates all query combinatoins.
        queries_combination = []
        for query in processed_queries:
            queries_combination.append(generate_result(query))

        # Generates all documents based on query and inverted index.
        all_queries_and_results = {}
        for query in queries_combination:
            for ele in query:
                doc_num = query_result(ele, inverted_index)
                all_queries_and_results[ele] = doc_num

        # Display.
        query_num = 1
        for query in queries_combination:
            print(f"\n================== User Query {query_num}: {queries[query_num-1]} =================")
            display_query(query, all_queries_and_results)
            query_num += 1



main()