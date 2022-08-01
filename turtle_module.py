import turtle

bob = turtle.Turtle()
print(bob)


# fd, bk (mover pra frente e pra trás em pixels(arg), respectivamente). lt, rt (virar para esquerda e direita, arg
# é um angulo em graus). pu, pd (pd deixa rastro enquanto se move, pu não deixa rastro enquanto se move)


# desenhando um ângulo reto

#bob.fd(100)
#bob.lt(90)
#bob.fd(100)


# desenhando um quadrado
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)

turtle.mainloop()