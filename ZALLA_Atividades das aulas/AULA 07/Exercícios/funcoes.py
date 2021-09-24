def arbitrary(x, y, more):
    '''Criando uma função que recebe mais parâmetros.'''

print(arbitrary.__doc__)

######################

def mensagemDeErro():
    '''Não retorna nada, mas mostra na tela uma mensagem de erro clássica.'''
    print("Tudo o que você colocou no programa está errado desde o começo.\n")
    print("Favor, começar tudo do zero.")

mensagemDeErro()

######################

def add(x, y):
    '''Return x plus y'''
    return x + y

primeiroParametro = int(input("Digite o primeiro número: "))
segundoParametro = int(input("Digite o segundo número: "))

print(add(primeiroParametro, segundoParametro))

#####################

def arbitrary(x, y, *more):
    '''Criando uma função que recebe mais parâmetros.'''
    print("x=",x,", y=",y)
    print("arbitrary: ", more)

arbitrary(3,4)
arbitrary(3,4,"Hello, World!",3,4)

#####################

def my_func():
    x = 10
    print("Value inside function: ",x)

x = 20
my_func()
print("Value outside funciton: ",x)

#####################

def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

####################

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple","banana","cherry"]

my_function(fruits)

####################

def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion example Results")
tri_recursion(6)

####################

cube = lambda x: x*x*x
print(cube(7))
