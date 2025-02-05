x = ('Masala', 'Lemon ', 'ginger'); 
y = enumerate(x); 

print(y); 
z = list(y); 
print(z); 

file = open('text.py'); 
try:
  file.write('chai aur code'); 
finally: 
  file.close();

with open('txt.py') as file:
  file.write('chai aur code'); 
