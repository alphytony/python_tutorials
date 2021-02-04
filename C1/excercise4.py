
# def igpay(a_string):
#     vowels = ["a","e","i","o","u"]
#     consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
#     string_for_vowel = "way"
#     string_for_consonant = "ay"

#     if a_string[0].lower() in vowels:

#         new_string = a_string + string_for_vowel
#         print("Translation of {0} is {1} ".format(a_string,new_string))
#     elif a_string[0].lower() in consonants:


#         consonat_string = a_string[1:] + a_string[0] + string_for_consonant
#         print("Transalation of {0} is {1} ".format(a_string,consonat_string))
#     else :

#         print ("Invalid Word")

# name = input("Enter a word \n")
# igpay(name)    


def numerous(s):
    roman_arabic_values = {'i':1,'v':5,'x':10,'l':50,'c':100,'m':1000}
    total_value = 0
    count=0
    for j in range(len(s)):
        if (count < len(s)-1):

            if roman_arabic_values[s[j]]  >= roman_arabic_values[s[j+1]]:
                total_value += roman_arabic_values[s[j]]
            else:
                total_value -= roman_arabic_values[s[j]]
            count+=1
        else:
            total_value += roman_arabic_values[s[j]]
    return total_value
roman_value = input("Enter roman numeral value : ")
arabic_value = numerous(roman_value)
print("Arabic numeral value of {0} is {1}".format(roman_value,arabic_value))
        
            

            







