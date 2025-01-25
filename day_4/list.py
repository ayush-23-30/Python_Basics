# array Question [List]; 

lis = []; 
# count = int(input("No. of element you want ")); 

# for i in range(count): 
#   z = int(input("Enter your No and Enter ")); 
#   lis.append(z); 

# print(lis); 

# for i in range(0,len(lis)):
#   print (lis[i]); 

# one = [1,2,3,4,5]; 

# for i in range(len(one)-1, -1 , -1):
#   print(one[i]);
List = [-2,32,4,-42,43,66,2,-432] ; 
pos = [];
neg = [];

for i in range(0,len(List)):
  if(List[i] > 0) : 
    pos.append(List[i]); 
  else : neg.append(List[i]); 

# print('neg' , neg)
# print('Pos' , pos)



def greatest(List):
  lag = 0; 
  ind = 0; 
  for i in range (0, len(List)):
    if(List[i] > lag):
      lag = List[i];
      ind = i; 
    else : continue;
  return print(f'Index :  {ind} value : {lag}');


# greatest(List)
def is_sorted(lst):
    for i in range(1, len(lst)):
        if lst[i-1] > lst[i]:
            return False
    return True


l = [1,2,3,4,6,7]
# print(is_sorted(l))

def secondGreatest(no):
  lag = 0; 
  Lagind = 0;
  sec = 0; 
  secInd = 0; 
  for i in range(0, len(no)):
    if(no[i] > lag):
      sec = lag; 
      lag = no[i]; 
      secInd = Lagind;
      Lagind = i; 
    elif (no[i] < lag and no[i] > sec):
      sec = no[i]; 
      secInd = i; 
  return print(f'Second Lagrest {sec} and Index is {secInd}'); 


# secondGreatest([5,3,54,33,53,23,44]);

# check a list palindromic or not --

def ListPalindromic (l) : 
  length = len(l)//2; 
  fir = []; 
  sec = []; 

  for i in range (0, length) :
    fir.append(l[i]);
  for i in range (len(l)-1, length-1 , -1):
    sec.append(l[i]); 
  if(fir == sec) :
    print("pailindromic");
  else : print ("not ")

listinng = [2,3,4,4,3,2];

ListPalindromic(listinng);