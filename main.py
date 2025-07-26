import sys
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_txt(book_path):
	with open(book_path) as f:
		contents = f.read()
		return contents

from stats import number_of_words
from stats import number_of_characters
from stats import get_sorted_char_list


def main():
	contents = get_book_txt(sys.argv[1])
	num_words = number_of_words(contents)
	print(f"{num_words} words found in the document")
	num_char = number_of_characters(contents)
        
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	results = get_sorted_char_list(num_char)
	for result in results:
		char = result["char"]
		if char.isalpha():
			print(f"{result['char']}: {result['num']}")
	print("============= END ===============")


main()
