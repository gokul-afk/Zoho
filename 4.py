def check_vow(count):
    for j in count:
        if count[0] != j:
            return False
    return True

my_string = input("enter the string: ")
vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}

res = [my_string[i: j] for i in range(len(my_string))
    for j in range(i + 1, len(my_string) + 1)]
res3 = []     

for word in res:
    vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}
    for letter in word:
        if letter in vowels.keys():
            vowels[letter]+=1
    count = list(vowels.values())
    if(check_vow(count)):
        res3.append(word)

s = ", ".join(res3)
print(s)


'''
Q4. VoWstrings
If a string has equal number of every vowels in it, then it is voWstring.
Example "aioeu", "aeoui" "aaoouuiiee" , "usaeio", "", "d" are voWstrings.
Given a string of lowercase letters (a-z), output the non-empty voWstring substrings of the given
string.
Input
Input consists of a line containing a string of length L.
Output
Output all non-empty voWstring substrings
Example 1:
input : aeiou
output : aeiou
Example 2:
input : aeoui
output : aeoui
Example 3:
input : aeiouiaeo
output : aeiou, ouiae, uiaeo
Example 4:
input : daeiouiaeo
output : d, daeiou, aeiou, ouiae, uiaeo
Example 5 :
input : aeiouiaeou
output : aeiou, ouiae, uiaeo, iaeou, aeiouiaeou

'''