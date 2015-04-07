#The main program, for matching the listing items to products in the 
#products list

import json
import kmp #for the kmp algorithm
import charmod #fr differently formatted instances of the model names

#loading the data

with open('products.txt','r') as json_file1:
    content1 = json_file1.readlines()

products = []

for json_obj in content1:
    products.append(json.loads(json_obj))

del(content1)

with open('listings.txt','r') as json_file2:
    content2 = json_file2.readlines()

listings = []

for json_obj in content2:
    listings.append(json.loads(json_obj))

del(content2)

#shorthands for the listings and products keys
t='title'; m='manufacturer'; c='currency'; p='price'
pn='product_name'; f='family'; mo='model'; ad='announced_date'



### The main loop of the program ###

#will containg the eventual output of the program
matchar = []

#we make all strings and text upper case to compensate for variation 
#in capitalization

for i in range(len(products)):
    S1 = products[i][m].upper()
    S2 = products[i][mo].upper()
    S3 = charmod.repSpace(products[i][mo]).upper()
    S4 = charmod.rmSpace(products[i][mo]).upper()
    F1 = kmp.fa(S1); F2 = kmp.fa(S2)
    F3 = kmp.fa(S3); F4 = kmp.fa(S4)
    
    matchtemp = [] #stores indices of matching listings
    
    for j in range(len(listings)):
#attempting manufacturer matching
        TF1 = kmp.match(S1,listings[j][m].upper(),F1) 
#if manufacturer matches, we attempt to match the model number in the 
#title of the listings text
        if TF1:
            TF2 = kmp.match(S2,listings[j][t].upper(),F2)
            TF3 = kmp.match(S3,listings[j][t].upper(),F3)
            TF4 = kmp.match(S4,listings[j][t].upper(),F4)
            if TF2: matchtemp.append(j)
            elif TF3: matchtemp.append(j)
            elif TF4: matchtemp.append(j)
    
#save product name and list matching listings
    matchar.append(
    {
    pn : products[i][pn],
    "listings" : [listings[k] for k in matchtemp]
    })
# delete matching listings to shorten listings list for future loops
    for k in range(len(matchtemp)):
        del listings[matchtemp[-k-1]]

#writing the output

with open('output.txt', 'w') as outfile:
    json.dump(matchar, outfile)
