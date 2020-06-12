
def hello5():
    print('hello')
    print('hello')
    print('hello')
    print('hello')
    print('hello')

def greet(person):
    print('hello '+ person)


def addNums(num1,num2):
    return num1 + num2



def factorise(num):
    for i in range(1,num+1):
        if(num%i ==0):
            print(str(i) + ' is a factor')

factorise(1238)
