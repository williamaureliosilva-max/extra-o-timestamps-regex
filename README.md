# Análise de Logs com Expressões Regulares (Regex) 🛡️

Este repositório contém ferramentas em Python desenvolvidas para automatizar a extração e análise de informações críticas em logs de servidores, facilitando auditorias de segurança e perícias digitais.

## 🚀 Scripts Incluídos

### 1. Analisador de Padrões e Ocorrências
*   **Ficheiro:** `analisador_padroes_ocorrencias.py`
*   **Função:** Identifica e conta a frequência de elementos como endereços IP, tentativas de login falhadas e utilização de portas de rede (ex: SSH/Port 22).

### 2. Extrator de Timestamps Multiformato
*   **Ficheiro:** `extrator_timestamps_logs.py`
*   **Função:** Reconhece e extrai marcas temporais em diversos formatos padrões da indústria, incluindo:
    *   **Linux/Syslog** (ex: Feb 10 08:23:01)
    *   **ISO 8601** (ex: 2025-02-10T08:23:01Z)
    *   **Apache Web Server**
    *   **Windows Event Logs**
    *   **Unix Epoch** (Timestamps numéricos)

## 🧠 Conceitos Aplicados
*   **Regex (Regular Expressions):** Uso de metacaracteres, quantificadores e grupos de captura para filtragem de dados não estruturados.
*   **Python re module:** Implementação de lógica de pesquisa e extração eficiente.
*   **Análise Forense:** Importância da normalização de datas para a correlação de eventos em incidentes de cibersegurança.

## 🛠️ Como Utilizar
1. Garante que tens o Python instalado.
2. Executa os scripts via terminal:
   ```bash
   python nome_do_script.py
   ```
