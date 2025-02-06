# Information Retrieval Assignment - Search System

## Overview
This assignment develops a simple search system using an **Inverted Index** for Boolean query processing. The project consists of two main parts:

### 1. Preprocessing and Indexing (`main1.py`)
   - Reads stopwords and punctuation files.
   - Loads an inverted index from a JSON file.
   - Tokenizes, removes stopwords and punctuation, and applies stemming.

### 2. Query Processing (`main2.py`)
   - Reads user queries from a file.
   - Generates all possible Boolean query combinations (`AND`, `OR`).
   - Retrieves matching document numbers from the inverted index.
   - Displays the results in a structured format.

---

## Installation & Setup
### Prerequisites
- Required dependencies (install using `pip`):

```sh
pip install nltk
```

### Files & Structure
```
IR-search-system/
├── main1.py          # Generates inverted index
├── main2.py          # Processes queries
├── inverted_index.json  # Inverted index file generated after running main1.py
├── queries.txt       # List of queries
├── stopwords.txt     # Stop words file
├── special-chars.txt # Punctuation file
├── documents         # Folder for document files
├── README.md         # Project documentation
```

---

## Usage Instructions
### Step 1: Generate the Inverted Index
Navigate to the project directory and run:

```sh
python main1.py
```
This creates the `inverted_index.json` file, which stores tokenized and indexed document data.

### Step 2: Process Queries
To execute query processing, run:

```sh
python main2.py
```
The script will:
- Read queries from `queries.txt`
- Preprocess and tokenize queries
- Generate Boolean combinations
- Retrieve and display relevant document numbers

---

## Query Format
Queries in `queries.txt` should be written in natural language (e.g., `data science`). The script automatically generates all Boolean query combinations using `AND` and `OR`.

**Example:**
```
machine learning
information retrieval
```
**Generated query combinations:**
```
machine AND learning
machine OR learning
```

---

## Example Output
```
================== User Query 1: machine learning =================
============= Results for: machine AND learning =================
file 3
file 7
==================================================
============= Results for: machine OR learning =================
file 1
file 3
file 5
file 7
==================================================
```

