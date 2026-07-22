# Faça um programa que leia um número e mostre sua tabuada

numero = float(input("Digite um número qualquer: "))

def tabuada(a):
    for i in range(11):  # de 0 a 10
        print(f"{a} x {i} = {a * i}")

tabuada(numero)