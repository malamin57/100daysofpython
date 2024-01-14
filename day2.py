total1 = input("Enter the total of the bill  ")
total2 = int(total1)
people1 = input("Enter the number of people  ")
people2 = int(people1)
tip1 = {1:.10,2:.20,3:.30}
tip2 = input("choose tip 1 -.10,2 - 20, 3 - .30 ")
tip3 = int(tip2)
bill = total2 / people2 
final_bill = bill * tip1[tip3]
final_final_bill = final_bill + bill
final_final_bill1 = str(final_final_bill)
print("Each Person will pay " + final_final_bill1)
