print(" O animal está habituado?  sim ou nao ")
c=input()
if c == "sim":
    habituado=True
    print("Avance para o Regime de aproximações sucessivas")
    print("Houve aproximação do animal?  sim ou nao?" )
    a=input()
    if a == "sim":
        print("Liberar 0,5 ml de recompensa\n")
        print("O animal tocou na barra 20x?")
        t=input()
        if t == "sim":
            print("O som1 foi emitido e o animal tocou na basimrra esquerda?")
            be=input()
            if be=="sim":
                print("Liberar 0,5 ml de recompensa\n")
                print("O som2 foi emitido e o animal tocou na barra direita?")
                bd=input()
                if bd=="sim":
                    print("Liberar 0,5 ml de recompensa\n")
                    print(" O experimento foi realizado 50x em 30 minutos?")
                    cinquentax=input()
                    if cinquentax=="sim":
                        print("Passar para a próxima fase do experimento")
                    elif cinquentax=="nao":
                        print( "Ainda não sera possível passar para próxima fase.")
                elif bd=="nao":
                    print("Não liberar recompensa")    
            elif be=="nao":
                print("Não liberar recompensa")
                
            

                


    elif a=="nao":
        print("Não liberar recompensa ")



elif c == "nao":
    print("não é possivel avançar no experimento") 
    habituado=False
else:
    print("digite algo")    
    
