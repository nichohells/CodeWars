Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.


string_ = ""
def disemvowel(string_):
    no_vowels = string_
    no_vowels = no_vowels.replace("a", "").replace("A", "")
    no_vowels = no_vowels.replace("e", "").replace("E", "")
    no_vowels = no_vowels.replace("i", "").replace("I", "")
    no_vowels = no_vowels.replace("o", "").replace("O", "")
    no_vowels = no_vowels.replace("u", "").replace("U", "")
    return no_vowels