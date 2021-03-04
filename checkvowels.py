def check_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    for char in string:
        if char not in vowels:
            print(f"{string}:Not Accepted")
            break
    else:
        print(f"{string}:Accepted")


string1 = "Aeiouaeeu"
string2 = "NehaSingh"
check_vowels(string1)
check_vowels(string2)