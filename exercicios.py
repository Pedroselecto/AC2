# Exercício 1:
    # Equação de segundo grau:

def eq_seg_grau(a, b, c):
    x1 = (-b + (b**2 - 4*a*c)**(1/2)) / 2*a
    x2 = (-b - (b**2 - 4*a*c)**(1/2)) / 2*a
    print(x1)
    print (x2)

eq_seg_grau(1, 2, -15)

    # Anos bissextos

def bissexto(ano):
    print (bool(ano % 100 != 0 and ano % 4 == 0) or (ano % 100 == 0 and ano % 400 == 0))

bissexto(1950)

# Exercício 2: Salários

def calcula_salario(valor_hora, num_horas):
    irpf =0.275
    salario =(valor_hora * num_horas) / irpf
    print(salario)

calcula_salario(100, 100)