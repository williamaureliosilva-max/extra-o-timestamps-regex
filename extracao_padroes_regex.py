import re

# Caminho para o ficheiro de logs que criaste na pasta 'logs'
caminho_ficheiro = 'logs/exemplo_logs.txt'

try:
    with open(caminho_ficheiro, 'r') as file:
        logs = file.read()

    # Definição dos padrões Regex
    padroes = {
        "Padrão A - Dígitos": r"\d+",
        "Padrão B - Hora": r"\d{2}:\d{2}:\d{2}",
        "Padrão C - IP": r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
        "Padrão D - Falhas": r"Failed \w+",
        "Padrão E - Portas": r"port \d+"
    }

    print(f"{'PADRÃO':<25} | {'ENCONTROS':<10}")
    print("-" * 40)

    for nome, regex in padroes.items():
        matches = re.findall(regex, logs)
        print(f"{nome:<25} | {len(matches):<10}")

except FileNotFoundError:
    print(f"Erro: O ficheiro '{caminho_ficheiro}' não foi encontrado. Garante que a pasta e o ficheiro existem!")
