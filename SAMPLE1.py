text="myfrienD9is 8great8 D9beautifuL 80courageous"
t="123"
AL="ASDS"
NUM=89.8776
num=13
low="low"
L=[1,2,3,4,5]
print("casefold=",text.casefold())#changes all the letters to lowercase
print("center=",text.center(20))#centers the text
print("count=",text.count("friend"))#counts the number of letters in the word
print("encode=",text.encode())#encodes the text
print("endswith=",text.endswith(","))# if the text ends with the character
print("expand tabs=",text.expandtabs(90))
print("INDEX=",text.index("my"))#finds the index value of the letter
print("ALPHA=",AL.isalpha())#checks if there is only alphabets
print("alnum=",text.isalnum())#checks if there is only alphabets and numbers
print("is ascii=",text.isascii())#checks if there ascii characters for the text
print("digit=",t.isdigit())#checks if there is only numbers
print("decimal=",text.isdecimal())#checks if there is only numbers with decimal 
print("upper=",AL.isupper())#checks if all the letters are in uppercase
print("lower=",low.islower())#checks if all the letters are in lowercase
mytrans=str.maketrans("D","d")
print("translate",text.translate(mytrans))#changes the givunn letter to another letter mentioned
print("partition",text.partition("8"))#seperates the words before,the word,the words after
print("replace",text.replace("8","100"))#replaces the old value with new value
print("rfind",text.rfind("my"))#find the starting index of the word mentioned from right
print("rindex",text.rindex("my"))#finds the index value of the letter right
print("rpartition",text.rpartition("8"))#seperates the words before,the word,the words after from right
print("rsplit",text.rsplit())#SPLITS A STRING INTO A LIST
print("rstrip",text.rstrip())# remove the trailing White Space in the right
print("split",text.split())#Split the Word into Smaller one according to character Specified in  parantheSiS
print("splitlines",text.splitlines())#Split TWO SENTENCES SEPERATELY according to character Specified in  parantheSiS
print("is identifier",text.isidentifier())# CHECKS IF THE TEXT CAN BE USED AS A IDENTIFIER
print("is lower:",text.islower())#CHECKS IF ALL THE LETTERS ARE IN LOWERCASE
print("is numeric",t.isnumeric())#CHECKS IF ALL THE CHARACTERS ARE IN NUMERIC
print("isprintablle",text.isprintable())#CHECKS IF THE TEXT IS PRINTABLE
print("is space",text.isspace())#CHECKS IF SPACE IS PRESENT BETWEEN THE WORDS IN THE TEXT
print("is title",text.istitle())#CHECKS IF THE WORDS ARE IN TITLE CASE
print("isupper",text.isupper())#CHECKS IF ALL THE LETTERS ARE IN UPPERCASE
print("#".join("text"))#ADDS THE "#" BETWEEEN THE TEXT MENTIONED 
P=text.rjust(70,"*")#ADDS THE TEXT MENTIONED IN THE PRINT STATEMENT TO THE ORIGINAL TEXT IN THE RIGHT OF THE TEXT
print(P,"my friend's name is roshini")
X=text.ljust(70,"*")#ADDS THE TEXT MENTIONED IN THE PRINT STATEMENT TO THE ORIGINAL TEXT IN THE LEFT OF THE TEXT
print(X,"my friend's name is roshini")
X=text.lstrip()
print("my friend's",X,"name is roshini")#REMOVES THE TRAILLING WHITE SPPACES IN THE LEFT
print("title",text.title())#CHANGES ALL THE WORDS TO TITLE CASE
print("upper",text.upper())#CHANGES ALL THE WORDS TO UPPER CASE
print("fill:",text.zfill(10))#adds 0 to the string to reach specified length
print("startswith=",text.endswith(","))# if the text starts with the character
print("swapcase",text.swapcase())#swaps uppercase to lower and vice versa

