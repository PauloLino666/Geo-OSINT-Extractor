# 📍 Geo-OSINT Extractor (Python EXIF Forensics)

Uma ferramenta de investigação digital e OSINT (Open Source Intelligence) desenvolvida em Python para extração, análise e tradução de metadados ocultos (EXIF) em arquivos de imagem. 

O foco principal do script é a identificação de dados de geolocalização (`GPSInfo`), realizando a conversão matemática de coordenadas brutas (Graus, Minutos e Segundos) para graus decimais e gerando automaticamente um link clicável e preciso para o Google Maps.

## ⚙️ Funcionalidades
- **Extração de Metadados Brutos:** Varredura completa da imagem em busca de tags EXIF ocultas (Data/Hora, Marca do dispositivo, Modelo, Resolução, etc.).
- **Tradução de Tags:** Conversão de códigos numéricos estruturais para dicionários legíveis humanos.
- **Forense de Localização:** Isolamento e identificação de sub-tags de GPS.
- **Conversão Matemática Automatizada:** O algoritmo acessa as tuplas de coordenadas, aplica a conversão de DMS (Degrees, Minutes, Seconds) para Decimal e ajusta automaticamente a polaridade com base no hemisfério (N/S, E/W).
- **Mapeamento Direto:** Geração de URL dinâmica do Google Maps com pino de localização exata da captura da evidência.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3
- **Bibliotecas:** `Pillow` (PIL - Python Imaging Library)
- **Conceitos Aplicados:** Manipulação de Dicionários aninhados, extração de índices em Tuplas, Estruturas de Repetição/Condição, Tratamento de Exceções (`try/except`) e Lógica Matemática.
