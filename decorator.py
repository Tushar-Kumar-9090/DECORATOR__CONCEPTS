

## Scenario:-1
## Nested Function Returning Integer as output

def Outer(self):    ## self=50
    print("First line of outer")
    print(self)
    def inner():
        print("First Line of inner")
        print(self)
        print("last line of inner")
    inner()
    print("last line of outer")
    return 100          ## when return returning 100 it will store in result

result=Outer(50)
print(result)       ##  100








#% Scenario-2
## Returning inner function addressfrom outer function space to main space

def Outer(self):    ## self=100
    print("First line of outer")
    print(self)
    def inner():
        print("First line of inner")
        print(self)
        print("Last Line Of inner")
    print("Last line of outer")
    return inner

result=Outer(100)   ## result=inner function address
print(result)
result()









#% Scenario-3
## Passing another function address as a value to the arguments

def Outer(self):    ## self=hai function address
    print("First line of outer")
    print(self)
    def inner():
        print("First line of inner")
        print(self)
        self()
        print("Last Line Of inner")
    print("Last line of outer")
    return inner

def hai():
    print("hai is started")
    print("end of hai")

result=Outer(hai)
print(result)
result()






##---------------------------------------------------------------------------------------------------





#* Advance Decorator
##--------------------------------------------------
## Function Decorators:-
#$ Example-1

def smart_divide(func):
    def swap(a,b):
        if a<b:
            a,b=b,a
        func(a,b)
    return swap

@smart_divide
def divide(a,b):
    print(a//b)
divide(10,2)
divide(2,10)






## Function Decorators:-
#$ Example-2
def smart_sub(func):
    def swap(a,b):
        if a<b:
            a,b=b,a
        func(a,b)
    return swap

@smart_sub
def subtract(a,b):
    print(a-b)
subtract(10,2)
subtract(2,10)