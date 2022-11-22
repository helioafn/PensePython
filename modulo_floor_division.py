# x % y == 0 -> x é divisível por y
# pode-se usar '%' para extrair dígitos mais a direita de um número(na base 10)
# ex: 123 % 10 -> 3. 123 % 100 -> 23

# Divisão pelo piso (floor division) e modulo 
# o operador '//' divide dois números e arredonda o resultado para um inteiro
# para baixo
minutes = 105
print(minutes / 60)  # 1.75  [de minutos para horas]
hours = minutes // 60  # 1

remainder = minutes - hours * 60  # obtendo o tempo restante
print(remainder)

# Uma alternativa é usar o operador módulo '%', que divide os dois números
# e devolve o resto
remainder = minutes % 60
print(remainder)