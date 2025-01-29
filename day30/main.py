

# try:
#     file = open('a_file.txt')
#     a_dictionary = {'sdfdf' : 'value'}
#     print((a_dictionary['sdfdf']))
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write("Something")
# except KeyError as error_message:
#     print(f" The key {error_message} not found")
# else: 
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("The is an error")


height = float(input("Height: "))
weight = int(input("Weight: "))

bmi = weight / height 

if height > 3:
    raise ValueError("Humman should no t be over 3 meters")



