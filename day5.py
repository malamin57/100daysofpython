import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
l1 = len(letters)
n1 = len(numbers)
s1 = len(symbols)

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

u = []
for x in range( 1 , nr_letters +1 ):
       y =  random.randint(1,x)
       z = letters[y]
       u.append(z)
     #  print(u)



for f in range( 1 , nr_symbols +1 ):
       t =  random.randint(1, f)
       k = symbols[t]
       u.append(k)
      # print(q)5
       



for x in range( 1 , nr_numbers +1 ):
       b =  random.randint(1,x)
       c = numbers[b]
       u.append(c)
      # print(j)
print(u)
s_len = len(u)
for x in range (1, s_len ):
       v = random.randint(1,x)
       h = u[v]
       print(h)
print(random.shuffle(u))
       
