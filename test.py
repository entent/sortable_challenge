import json
import kmp

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
pn='product_name'; f='family'; m='model'; ad='announced_date'






