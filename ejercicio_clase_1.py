num1=float(input("dame un numero (dividendo): "))
num2=float(input("dame otro numero (divisor): "))

if num2==0:
    print("no puedes dividir con 0")
else:
    div=num1//num2
    print(div)