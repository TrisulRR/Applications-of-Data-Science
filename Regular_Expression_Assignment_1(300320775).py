Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re #Importing Regular Expression Library
... given_word = ["hello", "hi", "helo","helllo","helloo"] #Query words
... text = "helllllooo"
... wordscount=0
... a=""
... for i in given_word:
...     j = re.findall(r"((\w)\2*)", i) #Regular Expression
...     a = "^" 
...     for k in j:
...         a += "("+k[1]+"{3,}|"+k[0]+")"
...     a += "$"
...     if(re.search(a,text)):
...         wordscount += 1
