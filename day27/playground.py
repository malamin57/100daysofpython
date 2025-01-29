
#args = 5
def num(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(num(3,4,5))

def cal(n, **kwargs):
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

cal(2,add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kw.get("model")

my_car = Car(make="niss")

