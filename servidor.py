import Pyro5.api
import time


@Pyro5.api.expose
class CalculadoraJuros:
    def calcular_juros_compostos(self, investimento, taxa, meses):
        inicio = time.time()
        
        taxa = taxa / 100  # Converter para decimal
        montante = investimento * ((1 + taxa) ** meses)
        juros_totais = montante - investimento
        
        juros_mensais = [(investimento * ((1 + taxa) ** i)) - investimento for i in range(1, meses + 1)]

        fim = time.time()
        tempo_processamento = fim - inicio
        ip_cliente = Pyro5.server.current_context.client_sock_addr[0]  # Pegar IP do cliente

        print(f"Requisição do cliente {ip_cliente} processada em {tempo_processamento:.6f} segundos.")

        return {
            "montante_total": round(montante, 2),
            "juros_totais": round(juros_totais, 2),
            "juros_mensais": [round(j, 2) for j in juros_mensais]
        }

# Inicializar o daemon e registrar o serviço
daemon = Pyro5.api.Daemon()
ns = Pyro5.api.locate_ns()
uri = daemon.register(CalculadoraJuros)
ns.register("financeira.juros", uri)

print("Servidor aguardando requisições...")
daemon.requestLoop()