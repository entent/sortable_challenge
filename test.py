import json
import kmp
import charmod

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

#shorthands for the listings headers
t='title'; m='manufacturer'; c='currency'; p='price'
pn='product_name'; f='family'; mo='model'; ad='announced_date'


#writing the loop that will first match the manufacturer,
#then if successful try to find the model name in the description
#will modify if this leads to incorrect results

#the eventual output of the program
matchar = []


#attempting manufacturer matching
for i in range(len(products)):
    S1 = products[i][m].upper()
    S2 = products[i][mo].upper()
    S3 = charmod.repSpace(products[i][mo]).upper()
    S4 = charmod.rmSpace(products[i][mo]).upper()
    F1 = kmp.fa(S1); F2 = kmp.fa(S2)
    F3 = kmp.fa(S3); F4 = kmp.fa(S4)
    
    matchtemp = []
    
    for j in range(len(listings)):
        TF1 = kmp.match(S1,listings[j][m].upper(),F1)
        if TF1:
            TF2 = kmp.match(S2,listings[j][t].upper(),F2)
            TF3 = kmp.match(S3,listings[j][t].upper(),F3)
            TF4 = kmp.match(S4,listings[j][t].upper(),F4)
            if TF2: matchtemp.append(j)
            elif TF3: matchtemp.append(j)
            elif TF4: matchtemp.append(j)
    
    matchar.append(
    {
    pn : products[i][pn],
    "listings" : [listings[k] for k in matchtemp]
    })

    for k in range(len(matchtemp)):
        del listings[matchtemp[-k-1]]


















