#writing the loop that will first match the manufacturer,
#then if successful try to find the model name in the description
#will modify if this leads to incorrect results

#the eventual output of the program
matchar = []


#attempting manufacturer matching
i = 1
S1 = products[i][m]; S2 = products[i][mo]
F1 = kmp.fa(S1); F2 = kmp.fa(S2)

matchtemp = []

for j in range(len(listings)):
    TF1 = kmp.match(listings[i][m],S1,F1)

    if TF1:
        TF2 = kmp.match(listings[i][t],S2,F2)
        if TF2: matchtemp.append(j)


matchar.append(
{
pn : product[i][pn],
"listings" : [listings[k] for k in mathtemp]
}
)

for k in range(len(mathtemp)):
    del listings[mathtemp[-k-1]]
