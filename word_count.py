import sys
import os
from collections import Counter
import logging

logging.basicConfig(filename="logs_word_count.log", level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

# Get the file path from the first command-line argument
def get_file_path():
    try:
        file_path = sys.argv[1]
    except IndexError:
        print("Please provide a file name as an argument.")
        logging.debug("Please provide a file name as an argument.".format())
        sys.exit(1)
    return file_path
file_path = get_file_path()
        
# Define the counting words function 
def counting_words(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print("File not found")
        logging.debug("File not found".format())
        sys.exit()

    # # Check if the file is empty
    elif os.stat(file_path).st_size == 0:
        print("File is empty")
        logging.debug("File is empty".format())
        sys.exit()

    # # Check if the file is a text file
    elif not file_path.endswith(".txt"):
        print("File format not supported, use a text file with .txt extension")
        logging.debug("File format not supported, use a text file with .txt extension".format())
        sys.exit()

    else:
    # Check if the file path is valid
        try:
            with open(file_path, "r") as f: 
                content = f.read()
        except Exception as e:
            print("An error occurred during program execution:", e)
            logging.debug("An error occurred during program execution: ".format(e))
            sys.exit()
        else:
        # Split the content into words and count the number of times each word occurs
            words = content.split()
            word_count = Counter(words)

            # Sort the words by their counts in descending order
            sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

            # Print each word and its count
            for word, count in sorted_words:
                print(word, ':', count)
            # Log successful execution
            logging.info("Word count print succesfull!")
counting_words(file_path)
