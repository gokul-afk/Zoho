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
