# 1. Inicialização das Listas (Armazenamento)
tipos_eventos = []
paises = []
regioes = []
cidades = []
areas_afetadas = []
intensidades = []
ocorrencias = []

# 2. Entrada de Dados
quantidade = int(input("Insira a quantidade de eventos a serem registrados: "))

for i in range(quantidade):
    print(f"\n--- Registro do Evento {i + 1} ---")

    tipo = str(input("Tipo de evento (ex: desmatamento, queimada): "))
    pais = str(input("País: "))
    regiao = str(input("Região: "))
    cidade = str(input("Cidade: "))

    # Validação da Área (deve ser maior que zero)
    area = float(input("Área afetada (km²): "))
    while area <= 0:
        print("Erro: A área deve ser maior que zero.")
        area = float(input("Digite a área novamente (km²): "))

    # Validação da Intensidade (entre 1 e 10)
    intensidade = int(input("Intensidade do impacto (1 a 10): "))
    while intensidade < 1 or intensidade > 10:
        print("Erro: A intensidade deve estar entre 1 e 10.")
        intensidade = int(input("Digite a intensidade novamente (1-10): "))

    num_ocorrencias = int(input("Número de ocorrências detectadas: "))

    # Armazenamento nas listas conforme solicitado [2]
    tipos_eventos.append(tipo)
    paises.append(pais)
    regioes.append(regiao)
    cidades.append(cidade)
    areas_afetadas.append(area)
    intensidades.append(intensidade)
    ocorrencias.append(num_ocorrencias)

# 3. Análise de Dados
total_eventos = len(tipos_eventos)
area_total = sum(areas_afetadas)
media_intensidade = sum(intensidades) / total_eventos

# Localizando o evento com maior área afetada usando max() e index() [1, 3]
indice_maior_area = areas_afetadas.index(max(areas_afetadas))

# Região com maior número de ocorrências
indice_mais_ocorrencias = ocorrencias.index(max(ocorrencias))
regiao_critica = regioes[indice_mais_ocorrencias]

# Densidade média (Ocorrências totais / Área total) [2]
densidade_media = sum(ocorrencias) / area_total

# Contagem de eventos acima da média de intensidade
eventos_acima_media = 0
for valor in intensidades:
    if valor > media_intensidade:
        eventos_acima_media += 1

# Identificação do Evento Mais Crítico (Maior Intensidade)
# Nota: Em caso de empate na intensidade, a lógica abaixo pega o primeiro encontrado
indice_critico = intensidades.index(max(intensidades))

# 4. Relatório de Resultados (Formatação f-string conforme Aula 03) [4-6]
print("\n" + "=" * 40)
print(f"{'RELATÓRIO DE ANÁLISE ESPACIAL':^40}")
print("=" * 40)
print(f"Total de eventos registrados: {total_eventos}")
print("-" * 40)
print("Resumo Geral")
print("-" * 40)
print(f"Área total afetada: {area_total:.2f} km²")
print(f"Média de intensidade: {media_intensidade:.2f}")
print("-" * 40)
print("Análises Específicas")
print("-" * 40)
print(f"Região com mais ocorrências: {regiao_critica}")
print(f"Eventos acima da média de intensidade: {eventos_acima_media}")
print(f"Densidade média: {densidade_media:.2f} ocorrências/km²")
print("-" * 40)
print("Evento Mais Crítico")
print("-" * 40)
print(f"Tipo: {tipos_eventos[indice_critico]}")
print(f"Local: {cidades[indice_critico]}, {regioes[indice_critico]}, {paises[indice_critico]}")
print(f"Intensidade: {intensidades[indice_critico]}")
print(f"Área afetada: {areas_afetadas[indice_critico]} km²")
print("=" * 40)