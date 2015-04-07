# sortable_challenge

This directory contains three Python scripts:
*matcher.py
*kmp.py
*charmod.py

**matcher.py is the main program, which loads the "listings" and "products" data. It then attempts to match "listings" items to items in the "products" file, using functions in the "kmp" and "charmod" files.  It then takes an list of all the "products" items, paired with lists of matched "listings" items (an empty list if there are no matches), and writes it to the "output" file.

**kmp.py contains the functions for the KMP algorithm due to Knuth, Morris and Pratt, for matching strings to text.  The function "fa" creates the failure array of a string, which is then used in the "match" function to match the string to a substring of a text.

**charmod.py contains two functions for altering strings of text by either replacing a space by a hyphen, or removing the space altogether.  This is for matching model numbers which have different formattings from those occuring in the "products" data.

This directory also contains the data files
*listings.txt
*products.txt

as well as the output file of the "matcher" program
*output.txt
