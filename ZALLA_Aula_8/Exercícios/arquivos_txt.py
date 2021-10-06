F = open("workfile","w")
print(F)

#####################

arquivo = open("workfile","w")

arquivo.write("Hello, World!\n")
arquivo.write("This is our new text file\n")
arquivo.write("and this is another line.\n")
arquivo.write("Why? Because we can.\n")

arquivo.close()

arquivo = open("workfile","r")
print(arquivo.read())

#####################

arquivo = open("workfile","r")
print(arquivo.read(5))

arquivo = open("workfile","r")
print(arquivo.readline())
print(arquivo.readline())

arquivo = open("workfile","r")
print(arquivo.readline(3))

arquivo = open("workfile","r")
print(arquivo.readlines())

#####################

arquivo = open("workfile","r")
for linha in arquivo:
    print(linha)

#####################

arquivo = open("workfile","w")
linhasDoTexto = ["Uma linha do texto aqui\n", "e outra linha do texto aqui\n",
"mais uma linha do texto\n","quarta linha\n"]
arquivo.writelines(linhasDoTexto)
arquivo.close()
arquivo = open("workfile","r")
for linha in arquivo:
    print(linha)
arquivo.close()

#####################

arquivo = open("workfile","w")
linhasDoTexto = ["Uma linha do texto aqui\n", "e outra linha do texto aqui\n",
"mais uma linha do texto\n","quarta linha\n"]
arquivo.writelines(linhasDoTexto)
arquivo.close()

with open("workfile") as arquivo:
    for line in arquivo:
        print(line)

####################

with open("hello","w") as f:
    linhasDoTexto = ["Uma linha do texto aqui\n", "e outra linha do texto aqui\n",
"mais uma linha do texto\n","quarta linha\n"]
    f.writelines(linhasDoTexto)

with open("hello","r") as f:
    data = f.readlines()

for line in data:
    words = line.split()
    print(words)