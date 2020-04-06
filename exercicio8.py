# fórmula (°C × 9/5) + 32 = °F
def celToFah(cel):
    return ((cel * 9/5) + 32)


celsius = float(input('Digite a temperatura em ºC: '))
print('{}ºC = {}ºF'.format(celsius, celToFah(celsius)))
