a = int(input('interruptor a: '))
b = int(input('interruptor b: '))
c = int(input('interruptor c: '))

# Proceso
encendido = 0
if (a==1):
    if (b==1 or c ==1):
        encendido = 1
else:
    if (b==1):
        if (c==1):
            encendido = 1
# Salida
print('estado del foco: ',encendido)