# El codigo se ejecutara hasta que i deje de ser menor que 6
i=1
while i<=6:
    print(i)
    i+=1

# Con la sentencia break podemos detener el bucle incluos si la condicion while es verdadera
i=1
while i<=6:
    print(i)
    i+=1
    if i ==3:
        continue
    print(i)