This is a simple command-line application which takes a path to a file as an argument and prints
a word count of its contents. The printed output consist of a line for each word, alongside the number of
times each word occurs in the file. It is sorted by the number of occurrences in a descending order - starting with the most frequest word. The app includes error handling, unit tests and logging. 

To run the app:
1 - Download and unzip the folder 
2 - On your terminal or Command-Line Interface cd or change directory into the downloaded / unzipped folder
3 - Run the command:
    $ python3 word_count.py /path-name/sample_words.txt
For example:
    $ python3 word_count.py /home/user/Downloads/word_count_app/sample_words.txt
4 - To run Unit Tests:
    $ python3 test_word_count.py /pathname/sample_words.txt
for example:
    $ python3 test_word_count.py /home/user/Downloads/word_count_app/sample_words.txt

Assumptions 
The solutions was implemented with Python on a Linux computer. So a Python installation will be needed.
The application expects to recieve a text file with the .txt extention as an argument and will return an error if other file types are used.

Note
Information gathered while the program is being executed is saved in the log file - logs_word_count.log


