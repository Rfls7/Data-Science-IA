# Escreva um programa que converta uma temperatura digitada em °C e converta em °F

temperatura = int(input('Digite a temperatura em °C: '))
def converter_temp(a):
    far = (a*1.8) + 32
    return far

far_calc = converter_temp(temperatura)
print(f'A temperatura informada é de {temperatura}°C, ou {far_calc}°F')