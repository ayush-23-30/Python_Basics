# print("this is day 2 [Question solving] "); 

# Part 1 -- If else Questions 
# question 1. after two number and print the greatest .

# one = int(input("enter first number ")); 
# two = int(input("enter second number ")); 

def greatest(one , two) :
  if one > two : 
    print("One is greatest" , one); 
  else : 
    print("Second is greatest")

# greatest(one,two); 

# Question 2 , print greeting wish according to gender
 
def greetingWish(gender) : 
  if gender == 'male': 
    print("Good morning Sir,");
  elif gender == 'female' : 
    print("Good morning Ma'am"); 
  else : 
   print("good morining")  

# greetingWish("hd")

# Question 3 number is even or odd 

# no = int(input("Enter a Number ")); 
def evenOdd (no): 
  if(no % 2 == 0) : 
    print("Even Number" , no); 
  else : 
    print("Odd", no); 

# evenOdd(232);

def leapYear (year) : 
  if(year % 4 == 0 and year % 100 != 0) : 
    print("This is a Leap Year"); 
  elif year % 100 == 0 and year % 400 == 0 : 
    print("leap year"); 
  else : 
    print("not A leap year"); 

# leapYear(2002); 

def vowelOrNot(aphla) : 
  if(aphla == 'a' or aphla == 'i' or aphla == 'o' or aphla == 'u' or aphla == 'e') : 
    print ("this is a vowel"); 
  else :
    print ("This is a Consonant");

def vowel (a) : 
  if a in 'aeiouAEIOU' : 
    print("Vowel"); 
  else : 
    print("Consonent");   

# vowel('A')
# vowelOrNot('d');

# Part 2 Loops Question --- 

# Question Print Natural No. up to n; 

def naturalPrint(n) : 
  for n in range(1,n): 
    print (n); 

# naturalPrint(29); 

def reversePrint(n):
  for n in range(n, 0, -1): 
    print(n); 

# reversePrint(10); 

# Question Print a table 

def table (t) : 
  for i in range(1,11):
    print(f" {t} x {i} = {t * i} "); 

# table(12);


def sum_up_to(s):
    total = 0
    for i in range(1, s + 1):
        total += i
    print(f"Sum of numbers from 1 to {s} is {total}")

# sum_up_to(10)

def fact (f) : 
  facted = 1; 
  for a in range(1,  f + 1) :
    facted *= a; 
  print(f'the factiorail of {f} is {facted}');

# fact(5);

def factor (n) : 
  cnt = 0; 
  for i in range(1, n+1) : 
    if n % i == 0 : 
     cnt += 1; 
  return cnt; 
    
# print(factor(7)); 

def perfect(p) :
  sumPerfect = 0; 
  for i in range (1, p): 
    if( p % i == 0 ) : 
      sumPerfect += i; 
  if(sumPerfect == p) : 
    print("perfect"); 
  else : print("Not perfect");

# perfect(6);

def prime(n) :
  cnt = 0; 
  for i in range(1, n+1): 
    if(n % i == 0) : 
      cnt += 1; 
  if(cnt == 2) : 
    print("prime"); 
  else: print("Composite Number"); 

# prime(30);

def takeoutNo (n): 
  while n > 0 :
    print( n % 10); 
    n = n // 10; 

# takeoutNo(12345);

def is_palindrome(n):
    copy = n
    res = 0
    while n > 0:
        res = res * 10 + n % 10; # Add the last digit to res
        n = n // 10;  # Remove the last digit from n
    return copy == res;

number = 121
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")




  






# Question  Strong Number Programme [sum of factorial of all digits] 