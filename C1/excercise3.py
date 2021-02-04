card_type =["Spade","Diamond","Club","Hearts"]
card_values=["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
for c in card_type:
    for cv in card_values:
        print(str(c)+" "+str(cv))


number = 1
it=0
while number<=1000000000000 :
    number*=2
    it+=1
    if it>1:
        print(str(number))
    else:
        break
print("number of iterations :",str(it))



