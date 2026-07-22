# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$ 60 por dia e R$0.15 por KM rodado.

km = int(input('Digite a quantdade de KM percorridos:'))
dias = int(input('Digite por quantos dias o carro ficou alugado:'))

def custo(a, b):
    custo_dias = b*60
    custo_km = a*0.15
    custo_total = custo_dias + custo_km
    return custo_dias, custo_km, custo_total

custo_dias_result, custo_km_result, custo_total_result = custo(km, dias)

print(f'A quantidade KM percorrido informada foi de {km}km por {dias} dias, isso gerou um custo por dia de R${custo_dias_result: .02f}, um custo por km de R${custo_km_result: .02f} e um custo total de R${custo_total_result: .02f}')