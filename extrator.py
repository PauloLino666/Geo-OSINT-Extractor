from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def extrair_metadados(caminho_imagem):
    print(f"A iniciar a análise do ficheiro: {caminho_imagem}...")

    try:
        # Tenta abrir a imagem com o Pillow
        imagem = Image.open(caminho_imagem)

        # Puxa os dados brutos
        dados_brutos = imagem._getexif()

        # Verifica se existem dados
        if dados_brutos is None:
            print("Resultado: Nenhum dado EXIF encontrado nesta imagem. Tenta outra fotografia.")
        else:
            print(f"Sucesso! Foram encontrados {len(dados_brutos)} registos de metadados ocultos.")

            # Bloco que limpa e retorna os dados
            print("\n--- INÍCIO DO RELATÓRIO FORENSE ---")
            for codigo, valor in dados_brutos.items():
                nome_tag = TAGS.get(codigo, codigo)

                # 1. Filtro de limpeza: Só imprime a tag geral se NÃO for o GPS
                if nome_tag != 'GPSInfo':
                    print(f"{nome_tag}: {valor}")

                # 2. Quando for o GPS, extrair os dados relativos a localização
                elif nome_tag == 'GPSInfo':
                    print("\n--- ALERTA: DADOS DE LOCALIZAÇÃO ENCONTRADOS ---")

                    # Imprimindo as sub-tags do GPS de forma legível
                    for gps_codigo, gps_valor in valor.items():
                        gps_nome_tag = GPSTAGS.get(gps_codigo, gps_codigo)
                        print(f"  -> {gps_nome_tag}: {gps_valor}")

                    # Coletando os dados exatos para a matemática
                    lat_ref = valor.get(1)  # Traz a letra 'S' ou 'N'
                    lat = valor.get(2)  # Traz a tupla da Latitude
                    lon_ref = valor.get(3)  # Traz a letra 'E' ou 'W'
                    lon = valor.get(4)  # Traz a tupla da Longitude

                    # Matemática da Latitude
                    lat_graus = lat[0]
                    lat_minutos = lat[1]
                    lat_segundos = lat[2]
                    lat_decimal = lat_graus + (lat_minutos / 60) + (lat_segundos / 3600)

                    # Checando a referência (lat_ref)
                    if lat_ref == 'S':
                        lat_decimal = lat_decimal * -1

                    # Matemática da Longitude
                    lon_graus = lon[0]
                    lon_minutos = lon[1]
                    lon_segundos = lon[2]
                    lon_decimal = lon_graus + (lon_minutos / 60) + (lon_segundos / 3600)

                    # Checando a referência (lon_ref)
                    if lon_ref == 'W':
                        lon_decimal = lon_decimal * -1


                    print(
                        f"\nLink do Google Maps: https://www.google.com/maps?q={lat_decimal},{lon_decimal}")
                    print("------------------------------------------------\n")

        print("\n--- FIM DO RELATÓORIO FORENSE ---")


    except Exception as e:
        print(f"Erro ao tentar abrir a imagem: {e}")


# Executa a função apontando para a imagem de teste
extrair_metadados("imagem.jpg")