from word_count import counting_words
import unittest
import sys
import unittest

file_path = sys.argv[1]

# Define a class to test the word_count function
class TestWordCount(unittest.TestCase):
    # Test if the function raises an error when no file name is provided
    def test_no_file_name(self):
        with self.assertRaises(SystemExit):
            counting_words(file_path='')

    # Test if the function raises an error when the file name is invalid
    def test_invalid_file_name(self):
        with self.assertRaises(SystemExit):
            counting_words("invalid_file_name.txt")

    # Test if the function raises an error when the file is empty
    def test_empty_file(self):
        with self.assertRaises(SystemExit):
            counting_words("empty_file.txt")

    # Test if the function raises an error when the file is not a text file
    def test_non_text_file(self):
        with self.assertRaises(SystemExit):
            counting_words("non_text_file.csv")

    # Test if the function raises an error when the file path is invalid
    def test_invalid_file_path(self):
        with self.assertRaises(SystemExit):
            counting_words("invalid_file_path.txt")

    # Test if the function prints the correct word count
    def test_word_count(self):
        self.assertEqual(counting_words("sample_words.txt"), None)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)   




    


    
    

