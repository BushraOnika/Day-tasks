import  re
import  nltk # this module for tokenization interms of spaces

# taking user input for breakdown then to
# turn them into tokens the input and identify the keywords

a = input("Enter your program or code or sentences: ");
tokens = nltk.wordpunct_tokenize(a);
print(tokens);

# storing the keywords operators, digits, special characters , idenntifiers
keys=("printf|while|void|unsigned|union|typedef|switch|struct|"
     "static|sizeof|signed|short|return|register|input|scanf"
     "long|int|if|goto|for|float|extern|enum|else|double|main|"
     "do|default|continue|const|char|case|break|auto|volatile");
op= "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)";
digit="^(\d+)$";
symbols= "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\"";
names= "^[a-zA-Z_]+[a-zA-Z0-9_]*";
headers = "([a-zA-Z]+\.[h])";

# Identify the Seperated tokens and Name those tokens
# Using re for the regular expression matching
for i in tokens:
    if(re.findall(keys,i)):
        print(i," --> Keyword")
    elif(re.findall(op,i)):
        print(i," --> Operator")
    elif (re.findall(digit, i)):
        print(i, " --> Digit/Number/Numeric")
    elif (re.findall(names, i)):
        print(i, " --> Naming Variables/Identifier")
    elif (re.findall(symbols, i)):
        print(i, " --> Symbol")
    elif (re.findall(headers, i)):
        print(i, " --> Header")
    else:
        print(i," --> Unknown")
