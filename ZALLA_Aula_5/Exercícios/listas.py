lista = []
print(lista)

lista = ["O carro", "peixe", 123, 111]
print(lista)

nova_lista = ["pedra", lista]
print(nova_lista)

######################

lista = ["O carro", "peixe", 123, 111]
nova_lista = ["pedra", lista]
print(lista[0])
print(lista[2])
print(nova_lista[1])
print(nova_lista[1][2])

print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])

######################

lista = ["O carro", "peixe", 123, 111]
nova_lista = ["pedra", lista]
print(len(nova_lista))

print(lista+nova_lista)
print(lista*3)

######################

lista = ["O carro", "peixe", 123, 111]
print("peixe" in lista)

numeros = [14.55, 67, 89.88, 10, 21.5]

print(min(numeros))
print(max(numeros))
print(sum(numeros))

######################

livros = ["Java", "SqlServer", "Delphi", "Python"]
livros.append("Android")
print(livros)

livros.insert(0, "Oracle")
print(livros)

livros = ["Java", "SqlServer", "Delphi", "Python"]
print(livros)
print(livros.pop())
print(livros)

livros = ["Java", "SqlServer", "Delphi", "Python"]
print(livros.pop(1))
print(livros)

#######################

livros = ["Oracle", "Java", "SqlServer", "Delphi", "Python", "Android", "Oracle"]
print(livros)
livros.remove("Oracle")
print(livros)
livros.remove("Oracle")
print(livros)
#livros.remove("Oracle") (se deixasse como algo executável pelo programa, iria dar erro)
#print(livros) (se deixasse como algo executável pelo programa, iria dar erro)

lista = [66.25, 333, -1, 333, 1, 1234.5, 333]
print(lista.index(333))

######################

livros = ["Oracle", "Java", "SqlServer", "Delphi", "Python", "Android", "Oracle"]
livros.sort()
print(livros)

livros = ["Oracle", "Java", "SqlServer", "Delphi", "Python", "Android", "Oracle"]
livros.reverse()
print(livros)

livros = ["Oracle", "Java", "SqlServer", "Delphi", "Python", "Android", "Oracle"]
print(livros.count("Oracle"))

######################

a = [81,82,83]
b = a
print(a is b)

a = [81,82,83]
b = [81,82,83]

print(a == b)
print(a is b)

b = a
print(a == b)
print(a is b)

b[0] = 5
print(a)

#####################

a = [81,82,83]

b = a[:]
print(a == b)
print(a is b)

b[0] = 5
print(a)
print(b)