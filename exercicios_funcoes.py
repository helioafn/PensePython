# 3.14 - Exercicios
# Exercicio 3.1
def right_justify(s):
    spaces = (70 - len(s)) * ' '
    print(spaces + s)

right_justify('helio')

# Exercício 3.2
# Variação 2
def do_twice(f, value):  
    f(value)
    f(value)

# Variação 1 
#def print_spam():
#    print('spam')

# Variação 3 
def print_twice(s):
    print(s)
    print(s)

# Variação 5
def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

# Variação 4 
# do_twice(print_twice, 'spam')

# Variação 5 
# do_four(print_twice, 'spam')


