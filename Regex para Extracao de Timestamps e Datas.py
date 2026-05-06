#!/usr/bin/env python3
"""
Atividade 2-3 — Extracao de timestamps de logs
UC01482 - OA-09
Nao e necessario modificar este script.
"""
import re

LOGS = [
    "Feb 10 08:23:01 srv sshd[1234]: Failed password for root from 192.168.1.100",
    "2025-02-10T08:23:01Z firewall BLOCK src=203.0.113.45 dst=10.0.0.1",
    "10/Feb/2025:08:23:01 +0000 \"GET /login HTTP/1.1\" 401 512",
    "2025-02-10 08:23:01 Security EventID=4625 LogonType=3 User=admin",
    "1739176981 fw DROP src=192.168.1.100 dst=8.8.8.8 proto=TCP",
]

# Padroes para cada formato
padroes = {
    "Syslog":   r"[A-Z][a-z]{2}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}",
    "ISO 8601": r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z?",
    "Apache":   r"\d{2}/[A-Z][a-z]{2}/\d{4}:\d{2}:\d{2}:\d{2}",
    "Windows":  r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
    "Epoch":    r"^\d{10}\b",
}

print("=" * 65)
print("EXTRACAO DE TIMESTAMPS")
print("=" * 65)

for i, linha in enumerate(LOGS, 1):
    print(f"\nLinha {i}: {linha[:60]}...")
    encontrou = False
    for nome_formato, padrao in padroes.items():
        resultado = re.search(padrao, linha)
        if resultado:
            print(f"  Formato: {nome_formato}")
            print(f"  Timestamp extraido: {resultado.group()}")
            encontrou = True
            break
    if not encontrou:
        print("  AVISO: Nenhum timestamp reconhecido")

print("\n" + "=" * 65)