# First Unique Letter Finder
This is a command-line interface (CLI) tool that finds the first unique letter in a given text. It works in two steps:

1. The tool identifies the first unique letter in every word of the text.
2. The tool identifies the first unique letter in a string composed of first unique letters of every word of the text.

## Essentials
* **Word**: A class that represents a word in a text. It can compute the frequency of each letter in the word and identify the first letter that only appears once.

* **Text**: A class that represents a text. It can find the first unique letter of the text by using the Word class.

* **CLI Application**: A simple command-line tool that accepts a text file and outputs the first unique letter in the whole text.

## Features
* The register <ins>is considered</ins>, therefore "A" and "a" are different letters.
* Numbers are considered <ins>as words</ins>, therefore there 2 words in "5 bananas" text.

## Installation
You can install this application by cloning the repository and running it locally. 
```bash
git clone <repo-url>
cd <repo-directory>
```

## Usage
### Library
You can use the Word and Text classes in your python script like this:
```python
from unique_letter_finder import Word, Text

word = Word("hello")
unique_letter = word.get_first_unique_letter()
print(unique_letter) # Output: h

text = Text("hello world")
unique_letter = text.get_first_unique_letter()
print(unique_letter) # Output: h

```

### CLI Application
You can use the CLI tool by running the python script with the command line argument for the file path.

```bash
python unique_letter_finder.py --file /path/to/text/file.txt
```

For help on using the CLI tool, you can use the help command:

```bash
python unique_letter_finder.py --help
```

This will print a message about how to use the application and what each option does.

