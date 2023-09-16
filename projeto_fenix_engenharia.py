import math
empresa = "Fênix Engenharia e Serviços"; ano = 2023; autor = "Ariel Reises"

print(f"Bem-vindo à {empresa}!")
print(f"Esse é o nosso simulador de economia para sistemas fotovoltaicos.\nPor: {autor}.\n")

def calcular_valor_parcela(valor, num_parcelas, taxa_juros):
    taxa_juros_decimal = taxa_juros / 100
    valor_parcela = valor * (1 + taxa_juros_decimal) / num_parcelas
    return valor_parcela

# Entrada de dados do usuário
try:
    consumo_mensal = int(input("Digite o consumo mensal aproximado (em kW): "))
    custo_mensal = float(input("Digite o custo mensal aproximado: R$ "))
except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número válido.")

# Cálculo da média de valor por kW
media_valor_por_kW = custo_mensal / consumo_mensal

print(f"\nMédia de valor por kW: R$ {media_valor_por_kW:.2f}")

# Entrada de dados para dimensionamento do projeto
try:
    dimensionamento_projeto = float(input("\nDigite o dimensionamento do projeto (em kW): "))
    valor_projeto = float(input("Digite o valor de custo estimado do projeto: R$ "))
except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número válido.")

# Avaliação do dimensionamento do projeto
if dimensionamento_projeto > consumo_mensal:
    print("\nSeu projeto é maior que o consumo atual do cliente.")
    print("Isso gerará créditos com a companhia elétrica nos sistemas on-grid.\n")

# Cálculo do valor atual do consumo mensal
valor_atual_consumo_mensal = consumo_mensal * media_valor_por_kW

# Previsão de tempo de retorno do investimento
previsao_tempo_retorno = valor_projeto / valor_atual_consumo_mensal

print(f"\nPrevisão de tempo de retorno do investimento: aproximadamente {math.ceil(previsao_tempo_retorno)} meses\n")

# Taxas de juros
print("=" * 45)
print("Taxas de juros para parcelamento:")
print("- até 24x: 1.45% ao mês")
print("- de 25x à 96x: 1.59% ao mês")
print("=" * 45)
# Condições de pagamento
print("\nCondições de pagamento:")
print(f"- À vista: R$ {valor_projeto:.2f}")
print(f"- Em até 10x sem juros de: R$ {(valor_projeto / 10):.2f}")
print("- Parcelamento: de 12x à 96x pelo Banco BTG")
print("=" * 45)

# Opção para pagamento à vista
try:
    opcao_pagamento = input("\nEscolha a forma de pagamento ([1] - à vista ou [2] - parcelado): ").lower()

    if opcao_pagamento == "1":
        num_parcelas = 1
        taxa_juros = 0
    elif opcao_pagamento == "2":
        # Entrada de dados para parcelamento
        num_parcelas = int(input("\nDigite o número de parcelas desejado (até 96x): "))

        if num_parcelas <= 10:
            taxa_juros = 0
        elif num_parcelas <= 24:
            taxa_juros = 1.45
        else:
            taxa_juros = 1.59
except ValueError:
    print("Opção inválida. Por favor, escolha [1] para à vista ou [2] para parcelado.")


valor_parcela = calcular_valor_parcela(valor_projeto, num_parcelas, taxa_juros)

# Cálculo de economia mensal e tempo de retorno do investimento
economia_mensal = valor_atual_consumo_mensal - valor_parcela

# Valor gasto sem o sistema fotovoltaico
valor_gasto_sem_sistema = valor_atual_consumo_mensal * 300

# Cálculo do valor total que o cliente pagará em 25 anos
valor_total_cliente = valor_parcela * num_parcelas * (1 + taxa_juros / 100)

# Economia total após quitar o investimento
economia_total_apos_quitar = valor_gasto_sem_sistema - valor_total_cliente

# Custo mensal atual
print(f"\nSem o sistema, você pagaria por mês: R$ {custo_mensal:.2f}")
print(f"Isso daria cerca de R$ {valor_gasto_sem_sistema:.2f} em 25 anos.\n")

# Valor da parcela mensal
print(f"Feche conosco agora mesmo e você vai pagar por mês apenas: R$ {valor_parcela:.2f}")
print(f"Uma economia mensal estimada em: R$ {economia_mensal:.2f}\n")

# Valor total que o cliente vai pagar (investimento + juros)
print(f"Valor total que você vai pagar: R$ {valor_total_cliente:.2f}\n(Referente ao valor total do Projeto, instalação e juros ao banco)")
print(f"\nEconomia total estimada em 25 anos: R$ {economia_total_apos_quitar:.2f}\n")

# Copyright
print(f"2023 - Todos os direitos reservados - Autor: {autor}")