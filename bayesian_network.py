###########################################################
#   Author  : Sagar Surendran
#   Created : 11/23/2019
#   Brief   : This program calculates the various
#             probabilities for the Bayesian Network given 
#             in the figure.
###########################################################

#Data values of variable are read from below.
f = open("input_probability_values.txt","r")

a = []  # baseball_game_on_TV
b = []  # George_watches_TV
c = []  # out_of_cat_food
d = []  # George_feeds_cat

for x in f:
    y = x.rstrip("\n")
    p, q, r, s = [int(v) for v in y.split()]
    a.append(p)
    b.append(q)
    c.append(r)
    d.append(s)

anum = 0
atot = 0
for i in a:
    atot+=1
    if 1 == i:
        anum+=1

aval = anum/atot
print("P (baseball_game_on_TV) : ", aval)

b1num = 0
b1tot = 0
b0num = 0
b0tot = 0
tot = 0
for i in a:
    if 1 == i:
        b1tot += 1
        if 1 == b[tot]:
            b1num+=1
    elif 0 == i:
        b0tot += 1
        if 1 == b[tot]:
            b0num += 1
    tot+=1

b1val = b1num/b1tot
b0val = b0num/b0tot
print("P (George_watches_TV | baseball_game_on_TV) : ", b1val)
print("P (George_watches_TV | ! baseball_game_on_TV) : ", b0val)

cnum = 0
ctot = 0
for i in c:
    ctot+=1
    if 1 == i:
        cnum+=1

cval = cnum/ctot
print("P (out_of_cat_food) : ", cval)


d11num = 0
d111num = 0
d110num = 0
d10num = 0
d101num = 0
d100num = 0
d01num = 0
d011num = 0
d010num = 0
d00num = 0
d001num = 0
d000num = 0
dtot = 0
for i in b:
    if 1 == i:
        if 1 == c[dtot]:
            d11num+=1
            if 1 == d[dtot]:
                d111num+=1
            elif 0 == d[dtot]:
                d110num+=1
        elif 0 == c[dtot]:
            d10num+=1
            if 1 == d[dtot]:
                d101num+=1
            elif 0 == d[dtot]:
                d100num+=1
    elif 0 == i:
        if 1 == c[dtot]:
            d01num+=1
            if 1 == d[dtot]:
                d011num+=1
            elif 0 == d[dtot]:
                d010num+=1
        elif 0 == c[dtot]:
            d00num+=1
            if 1 == d[dtot]:
                d001num+=1
            elif 0 == d[dtot]:
                d000num+=1

    dtot+=1

d11val = d111num/d11num
d110val = d110num/d11num

d10val = d101num/d10num
d100val = d100num/d10num

d01val = d011num/d01num
d010val = d010num/d01num

d00val = d001num/d00num
d000val = d000num/d00num

print("P (George_feeds_cat | George_watches_TV, out_of_cat_food) : ", d11val)
print("P ( !George_feeds_cat | George_watches_TV, out_of_cat_food) : ", d110val)

print("P (George_feeds_cat | George_watches_TV, ! out_of_cat_food) : ", d10val)
print("P ( !George_feeds_cat | George_watches_TV, ! out_of_cat_food) : ", d100val)

print("P (George_feeds_cat | ! George_watches_TV, out_of_cat_food) : ", d01val)
print("P ( !George_feeds_cat | ! George_watches_TV, out_of_cat_food) : ", d010val)

print("P (George_feeds_cat | ! George_watches_TV, ! out_of_cat_food) : ", d00val)
print("P ( !George_feeds_cat | ! George_watches_TV, ! out_of_cat_food) : ", d000val)
