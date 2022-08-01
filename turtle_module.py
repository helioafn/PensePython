import turtle

bob = turtle.Turtle()
print(bob)


# fd, bk (mover pra frente e pra trás em pixels(arg), respectivamente). lt, rt 
# (virar para esquerda e direita, arg é um angulo em graus). pu, pd
#  (pd deixa rastro enquanto se move, pu não deixa rastro enquanto se move)


# desenhando um ângulo reto

#bob.fd(100)
#bob.lt(90)
#bob.fd(100)


# desenhando um quadrado
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)


# desenhando um quadrado usando repetições 

# for i in range(4):
    # bob.fd(100)
    # bob.lt(90)

# desenhando um triângulo

# for i in range(2):
#     bob.fd(100)
#     bob.lt(120)

# bob.fd(100)
# bob.lt(90)

def triangle(t):
    '''
        Essa função recebe um objeto turtle t
        e desenha um triângulo de lados 100px
    '''

    for i in range(2):
        t.fd(100)
        t.lt(120)
    t.fd(100)
    t.lt(90)



# Exercícios 4.3

# 4.3.1

def square(t):
    ''' 
        Essa função recebe um objeto turtle t
        e desenha um quadrado na tela.
    '''
    
    for i in range(4):
        t.fd(100)
        t.lt(90)


square(bob)

# método que espera alguma ação do usuário, sem essa instrução o  
# script encerraria depois de desenhar o quadrado.
turtle.mainloop()