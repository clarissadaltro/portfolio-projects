import pandas as pd
import os

caminho_base_inicial = "Base_Inicial/BASE INICIAL.xlsx"
caminho_base_out24 = "Base_OUT24/BASE_OUT24.xlsx"
caminho_base_nov24 = "Base_NOV24/BASE_NOV24.xlsx"
caminho_base_dez24 = "Base_DEZ24/BASE_DEZ24.xlsx"


base_inicial = pd.read_excel(caminho_base_inicial, header=2, usecols='A:K')
base_out24 = pd.read_excel(caminho_base_out24, header=2, usecols='A:K')
base_nov24 = pd.read_excel(caminho_base_nov24, header=2, usecols='A:K')
base_dez24 = pd.read_excel(caminho_base_dez24, header=2, usecols='A:K')


base_inicial = pd.concat([base_inicial, base_out24, base_nov24, base_dez24], ignore_index=True)


base_consolidada = base_inicial.drop_duplicates(subset='ID_UNICO')


pasta_consolidado = "CONSOLIDADO"
os.makedirs(pasta_consolidado, exist_ok=True)

base_consolidada.to_excel(f"{pasta_consolidado}/CONSOLIDADO.xlsx", index=False)



if os.path.exists(f"{pasta_consolidado}/CONSOLIDADO.xlsx"):
    print("Processo concluído: O arquivo CONSOLIDADO.xlsx foi salvo com sucesso.")
else:
    print("Erro: O arquivo CONSOLIDADO.xlsx não foi salvo.")