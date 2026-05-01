a = float(input("Insira o valor do primeiro lado do Triângulo: "))
b = float(input("Insira o valor do segundo lado do Triângulo: "))
c = float(input("Insira o valor do terceiro lado do Triângulo: "))
triangulo = [a, b, c]

if b > a:
    a, b = b, a
if c > a:
    a, c = c, a
if c > b:
    b, c = c, b

print("\n")
if a >= b+c:
    print(f"NAO FORMA TRIANGULO: A = {a}, B = {b}, C = {c}")
elif a**2 == b**2 + c**2:
    print(f"TRIANGULO RETANGULO: A² = {a**2}, B² = {b**2}, C² = {c**2}")
elif a**2 > b**2 + c**2:
    print(f"TRIANGULO OBTUSANGULO: A² = {a**2}, B² = {b**2}, C² = {c**2}")
elif a**2 < b**2 + c**2:
    if a == b and b == c:
        print(f"TRIANGULO EQUILATERO: A = {a}, B = {b}, C = {c}")
    elif a == b and b != c or a == c and c != b:
        print(f"TRIANGULO ISOSCELES: A = {a}, B = {b}, C = {c}")
    else:
        print(f"TRIANGULO ACUTANGULO: A² = {a**2}, B² = {b**2}, C² = {c**2}")
else:
    print("Algo deu Errado!")