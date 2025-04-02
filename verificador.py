# Função para calcular juros compostos
def calcular_juros_compostos(investimento, taxa, meses):
    taxa = taxa / 100  # Converter taxa para decimal
    montante = investimento * ((1 + taxa) ** meses)
    juros_totais = montante - investimento
    
    juros_mensais = [(investimento * ((1 + taxa) ** i)) - investimento for i in range(1, meses + 1)]
    
    # Exibindo os resultados
    print(f"Montante total a ser recebido: R$ {round(montante, 2)}")
    print(f"Total de juros ganhos: R$ {round(juros_totais, 2)}")
    print("Juros acumulados por mês:")
    for i, juros in enumerate(juros_mensais, start=1):
        print(f"Mês {i}: R$ {round(juros, 2)}")
    
    return round(montante, 2), round(juros_totais, 2), [round(j, 2) for j in juros_mensais]

# Dados para o teste
investimento = 1000
taxa = 5
meses = 12

# Calcular e exibir os resultados
montante_total, juros_totais, juros_mensais = calcular_juros_compostos(investimento, taxa, meses)
