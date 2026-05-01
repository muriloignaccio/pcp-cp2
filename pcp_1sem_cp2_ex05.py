# Exercício 05 - Sistema de Financiamento Bancário

def pode_aprovar(idade, renda, valor):
    return idade > 18 and valor <= (renda * 20)

def definir_taxa(parcelas):
    if 3 <= parcelas <= 6:
        return 0.05
    elif 7 <= parcelas <= 12:
        return 0.08
    elif 13 <= parcelas <= 24:
        return 0.10
    else:
        return None

def calcular_parcela(valor, taxa, numero_parcelas):
    fator = (1 + taxa) ** numero_parcelas

    numerador = taxa * fator
    denominador = fator - 1

    parcela = valor * (numerador / denominador)

    return parcela

def calcular_total(valor_parcela, numero_total_parcelas):
    return valor_parcela * numero_total_parcelas

def calcular_juros(total, valor):
    return total - valor

nome_cliente = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
renda_mensal = float(input("Digite sua renda mensal: "))
valor_emprestimo = float(input("Digite o valor desejado para o empréstimo: "))
numero_parcelas = int(input("Digite o número de parcelas (3 até 24): "))

taxa = definir_taxa(numero_parcelas)

print("\n=== RESULTADO DO FINANCIAMENTO ===")

if taxa is None:
    print("Número de parcelas inválido.")
elif pode_aprovar(idade, renda_mensal, valor_emprestimo):
    print("Empréstimo aprovado.")
    parcela = calcular_parcela(valor_emprestimo, taxa, numero_parcelas)
    total = calcular_total(parcela, numero_parcelas)
    juros = calcular_juros(total, valor_emprestimo)

    print(f"\nCliente: {nome_cliente}")
    print(f"Valor financiado: R$ {valor_emprestimo:.2f}")
    print(f"Taxa de juros: {taxa * 100:.0f}% ao mês")
    print(f"Valor da parcela: R$ {parcela:.2f}")
    print(f"Total pago: R$ {total:.2f}")
    print(f"Total de juros: R$ {juros:.2f}")
else:
    print("Empréstimo não aprovado.")