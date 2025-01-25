# print string in reverse, its length , in uppercase and lowercase and copy into another string 

str = "AyushKumaR"; 

# print(str.lower());
# print(str.upper());

b = str; 
# print(b);

# for i in range (len(str)-1, -1,-1) :
  # print(str[i]);

# print(str[::-1]);

#arrange lower case first then upper case in a string

def lowerUpper(s):
    lower = ""
    upper = ""
    for i in s:
        if i.islower():
            lower += i
        else:
            upper += i
    # print(lower)
    # print(upper)
    return lower + upper

# Example usage
# print(lowerUpper("HeLLoWorLD"))


character = "P@#yn26at#6%j0^$"

def counted(s):
    dig = 0
    char = 0
    sym = 0
    for i in s:
        if i.isdigit():
            dig += 1
        elif i.isalpha():
            char += 1
        else:
            sym += 1
    print(f"No. of Digits: {dig}, No. of Characters: {char}, No. of Symbols: {sym}")

# counted(character)

line = "hello i am ayush and who you are "
def vowles (cnt):
    vow = 0; 
    for i in cnt:
        if i in 'aioeuAIOEU':
            vow+= 1; 
    return vow;

# print(vowles(line)); 

# palindrome checking


# def palindrome (a) :
#     print (a == a[:: -1]); 

def palindrome(a):
    b = ""
    for i in range(len(a) - 1, -1, -1):
        b += a[i]
    return a == b

# Example usage
print(palindrome("madam"))  
print(palindrome("hello"))  



palindrome('naman');
        






