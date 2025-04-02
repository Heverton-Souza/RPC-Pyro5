import Pyro5.api

# Conectar ao servidor Pyro5
proxy = Pyro5.api.Proxy("PYRONAME:financeira.juros")

# Solicitar dados ao usuário
investimento = float(input("Digite o valor do investimento inicial: "))
taxa = float(input("Digite a taxa de juros mensal (em %): "))
meses = int(input("Digite a quantidade de meses do investimento: "))

# Chamar o método remoto
resultado = proxy.calcular_juros_compostos(investimento, taxa, meses)

# Exibir resultados
print("\nResultados do investimento:")
print(f"Montante total a ser recebido: R$ {resultado['montante_total']}")
print(f"Total de juros ganhos: R$ {resultado['juros_totais']}")
print("Juros acumulados por mês:")
for i, juros in enumerate(resultado['juros_mensais'], start=1):
    print(f"Mês {i}: R$ {juros}")