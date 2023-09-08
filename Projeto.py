import statistics

def converter_para_float(numero_com_virgula):
    
        numero_com_ponto = numero_com_virgula.replace(',', '.')
        valor_float = float(numero_com_ponto)
        return valor_float

def ler_arquivo(nome_arquivo):
    try:
        with open("2023.1 (2P)\Estatistica\CPU.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            dados = [converter_para_float(linha.strip()) for linha in linhas]
        return dados
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Verifique o arquivo.")
        return None

nome_do_arquivo = "2023.1 (2P)\Estatistica\CPU.txt"  
dados = ler_arquivo(nome_do_arquivo)

if dados is not None:

    media = statistics.mean(dados)
    mediana = statistics.median(dados)

    desvio_padrao = statistics.stdev(dados)

    print("Medidas de Centralidade:")
    print(f"\tMedia: {media}")
    print(f"\tMediana: {mediana}")
    print("Medidas de Dispersao:")
    print(f"\tDesvio Padrao: {desvio_padrao}")