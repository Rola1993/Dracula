# Dracula

Use the plain text copy from Project Gutenburg: http://www.gutenberg.org/cache/epub/345/pg345.txt

## 2 credit hour students:

Your job will be to parse through this document, find the individual chapters, and write those out as separate files.

1.	The file names should be “Dracula-Chapter-#” where you fill in the chapter number, but as a number and not a roman numeral.  
	o	For example, your file names should be Dracula-Chapter-1.txt, Dracula-Chapter-2.txt, etc.  
	o	No need for leading 0s.
2.	Each chapter file should start with “CHAPTER…” as the first line and contain exactly the text content of that chapter.  
	o	Example: Dracula-Chapter-1.txt should start with “CHAPTER I” and the last line should be “sky.”  
	o	This means you’ll need to retain the newlines within the text file as they appear.
3.	You may not hard code any line numbers, position numbers, or chapter numbers into your script.  You must use conditionals to check for everything. You will need to find a way to auto detect where the text starts and ends (warning: there is more text after the book, which you will need to figure out how to get rid of).

## 4 credit hour students:

Same as 2 credit hour students, but you will also need to detect the chapter titles from the beginning of the file and include them in the file names.  You can find these chapter numbers in the CONTENTS section of the file.  

1.	You may not hard code these chapter names anywhere in your script.  You must write something that detects them and then can match them up with the chapter numbers.  You will not need to write something that parses roman numerals into digits to do this.  
2.	You will also need to clean these titles so they can be appropriate file names.  
	o	Example:  spaces should be replaced with _ (an underscore), and all punctuation removed.
	o	So your file names should be “Dracula-Chapter-1-Jonathan_Harkers_Journal.txt, …, Dracula-Chapter-7-Cutting_from_The_Dailygraph_8_August.txt.

## Extra credit (open to all students):

Create a data file that includes how many lines, words, and letters there are in each chapter.  Example (with obviously made up numbers):

Chapter, characters, words, lines
1, 100000, 10000, 1000


