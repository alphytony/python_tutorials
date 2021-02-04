colors = ["Red","Orange", "Yellow","Blue","Purple"]
sentence= "The amazing Grace how sweet thy sound."
print(sentence[0])
print(colors[1])
print(sentence[-2])
print(colors[1:4])
print(sentence[4:11])
print(sentence[4:]) 
print(sentence[::2])
print(colors[::2])
print(sentence[4:-1:2])
#colors[1]="Black"
#print(colors)
#colors[2:]=["Black"]*4
print(colors)
print(sentence.split(' '))
print('-'.join(colors))
print('-'.join(colors).split('-'))
for color in colors:
    print("Is " + color +" is your favourite color?")
for number in [1,2,3,4,5,6]:
    double = number*2
    print("Twice of " + str(number) + " is " + str(double))
modifiers =["Dark","Light","Brownish"]
for c in colors:
    for m in modifiers:
        print(m +" "+ c)
countdown = 10
while(countdown>=0):
    print(str(countdown))
    countdown-=1