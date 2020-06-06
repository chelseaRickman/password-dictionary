# Python Dictionary Attack Example

The password_dictionary_creator.py script creates a list of possible password combinations based on a list of keywords it is provided. In other words, a personalized dictionary of a target.

## How it works
- Create a keyword file. You can use the sample file that is included, harry_potter.txt, or create your own.
- If creating your own, create a text file containing keywords related to the target. Preferably one word per line of the text file, or words separated by spaces.  Dates should be entered in MM.DD.YYYY format. Examples of keywords are: spouse/siginifant other name, children's names, birthdates, anniversary dates, favorite tv show/movie, favorite number, favorite color, etc.
- From the command line, run the password_dictionary_creator.py script
- Type in the name of the keyword file: harry_potter.txt
- The program will run and create a new txt file titled "target_dictionary.txt"
- Open this file and this will contain a list of all possible password combinations using two, three, and four of the keywords


## What I Learned From This Project
This script is a great demonstration of how easily passwords can be guessed and generated when people use weak passwords containing personal information/references.

I had a volunteer be the "target" in this scenario. I created a keyword file based on information I know about this volunteer and, using this script, was able to successfully guess three of their passwords.

