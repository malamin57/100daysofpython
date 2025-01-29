
import time




flavor = input('What type of drink would you like - espresso, latte,  cappuciino ')


inventory = {'milk' : 1000,
             'water': 1000,
             'coffe': 1000             
             }

recipe_flavor = { 'espresso' :  { 
                                  'milk' : 100,
                                  'water' : 50,
                                  'cofee' : 76, 
                                  'money' : .50
                                },
                    'latte' :  {
                                  'milk' : 200,
                                  'water' : 70,
                                  'cofee' : 85, 
                                  'money' : .75

                               },

                    'cappuciino' : {
                                   'milk' : 195,
                                  'water' : 80,
                                  'cofee' : 95, 
                                  'money' : 1.00



                    }

}

amount = input('Enter the money into the machine \n ')
c_amount = recipe_flavor['cappuciino']['money']


if flavor == 'cappuciino' :
    print('recipe_flavor['cappuciino']['money']')
    milk_amount = inventory['milk'] - recipe_flavor['cappuciino']['milk']
    water_amount = inventory['water'] - recipe_flavor['cappuciino']['water']
    cofee_amount = inventory['coffe'] - recipe_flavor['cappuciino']['cofee']
    inventory.update({'milk': milk_amount})
    inventory.update({'water': water_amount})
    inventory.update({'coffe': cofee_amount})
    print(inventory)
    #print(recipe_flavor['cappuciino'])
elif flavor == 'latte':
    milk_amount = inventory['milk'] - recipe_flavor['cappuciino']['milk']
    water_amount = inventory['water'] - recipe_flavor['cappuciino']['water']
    cofee_amount = inventory['coffe'] - recipe_flavor['cappuciino']['cofee']
    inventory.update({'milk': milk_amount})
    inventory.update({'water': water_amount})
    inventory.update({'coffe': cofee_amount})
    print(inventory)
elif flavor == 'espresso':
    milk_amount = inventory['milk'] - recipe_flavor['cappuciino']['milk']
    water_amount = inventory['water'] - recipe_flavor['cappuciino']['water']
    cofee_amount = inventory['coffe'] - recipe_flavor['cappuciino']['cofee']
    inventory.update({'milk': milk_amount})
    inventory.update({'water': water_amount})
    inventory.update({'coffe': cofee_amount})
    print(inventory)
else: 
    print("Make a valid choice")





    