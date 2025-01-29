import pandas as pd
import random 
'''
number = [1, ]
new_list = []
for n in range(number):
    add_1 = n * 2 

new_list.append(add_1)

print(new_list)


range_list = [num * 2 for num in range(1,5)]
names = ["alex","Mikes", "Richard", "Mustafa"]
long_name = [ name.upper() for name in names if len(name) > 5 ]
print(long_name)


names = [ 'Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_score = { x:random.randint(1,100) for x in names

}

pass_student = { student:score for (student, score) in student_score.items() if score >= 60 }


s_data =  pd.DataFrame(pass_student)
#print(pass_student)
print(s_data)

'''

nato_df = pd.read_csv('/Users/malamin/100days/100days/bin/day26/nato_phonetic_alphabet.csv')
#print(nato_df.head())

nato_dictionary = {row.letter: row.code for (index, row) in nato_df.iterrows()}
print(nato_dictionary)

word = input('Enter a word').upper()
ouput_list = [nato_dictionary[letter] for letter in word ]
print(ouput_list)



