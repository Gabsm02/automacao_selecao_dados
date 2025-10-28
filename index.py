
from datetime import datetime, timedelta
import pandas as pd
import os

# Datas úteis
hoje = datetime.now()
ano_atual = hoje.year
mes_atual = hoje.month
semana_atual = hoje.isocalendar()[1]
data_anterior = hoje - timedelta(days=1)

# Funções utilitárias
def carregar_planilha(caminho):
    return pd.read_excel(caminho, engine='openpyxl')

def filtrar_bahia(df):
    return df[df["UF"] == "BA"] if "UF" in df.columns else df

def remover_nulos(df, coluna):
    return df.dropna(subset=[coluna])

def formatar_data(df, coluna):
    df[coluna] = pd.to_datetime(df[coluna])
    df["dia"] = df[coluna].dt.day
    df[coluna] = df[coluna].dt.strftime("%d/%m/%Y")
    return df

def salvar_planilha(df, nome_arquivo):
    df.to_excel(nome_arquivo, index=False)
    print(f"Registros salvos em '{nome_arquivo}'")

# Processamentos específicos
def processar_diario_municipio(df):
    df = filtrar_bahia(df)
    if "DATA_REFERENCIA" in df.columns:
        df["DATA_REFERENCIA"] = pd.to_datetime(df["DATA_REFERENCIA"])
        df = df[df["DATA_REFERENCIA"].dt.date == data_anterior.date()]
    df = remover_nulos(df, "DISP_GERAL")
    df = formatar_data(df, "DATA_REFERENCIA")
    df = df.drop_duplicates(subset=["MUNICIPIO", "DATA_REFERENCIA"])
    salvar_planilha(df, "registros_diario_municipio.xlsx")

def processar_mensal_municipio(df):
    df = filtrar_bahia(df)
    df = df[df["ANO"] == ano_atual]
    df = df[df["MES"] == mes_atual]
    df = remover_nulos(df, "DISPONIBILIDADE_GERAL")
    df = df.drop_duplicates(subset=["MES", "MUNICIPIO"])
    salvar_planilha(df, "registros_mensal_municipio.xlsx")

def processar_semanal_municipio(df):
    df = filtrar_bahia(df)
    df = df[df["ANO"] == ano_atual]
    df = df[df["SEMANA"] == semana_atual]
    df = remover_nulos(df, "DISPONIBILIDADE_GERAL")
    df = df.drop_duplicates(subset=["SEMANA", "MUNICIPIO"])
    salvar_planilha(df, "registros_semanal_municipio.xlsx")

def processar_diario_site(df):
    df = filtrar_bahia(df)
    df = remover_nulos(df, "DISP_GERAL")
    df["DATA_REFERENCIA"] = pd.to_datetime(df["DATA_REFERENCIA"])
    data_mais_recente = df["DATA_REFERENCIA"].max()
    df = df[df["DATA_REFERENCIA"] == data_mais_recente]
    df = formatar_data(df, "DATA_REFERENCIA")
    df = df.drop_duplicates(subset=["SITE", "DATA_REFERENCIA"])
    salvar_planilha(df, "registros_diario_site.xlsx")

# Loop principal
while True:
    try:
        arquivo = input("Envie o caminho do arquivo: ").strip()
        nome_arquivo = os.path.basename(arquivo)
        df = carregar_planilha(arquivo)

        if nome_arquivo == "cdt_diario_municipio_hmm.xlsx":
            processar_diario_municipio(df)

        elif nome_arquivo == "cdt_municipios_mensal_hmm.xlsx":
            processar_mensal_municipio(df)

        elif nome_arquivo == "cdt_municipios_semanal_hmm.xlsx":
            processar_semanal_municipio(df)

        elif nome_arquivo == "cdt_diario_site_hmm.xlsx":
            processar_diario_site(df)

        else:
            print("Arquivo não reconhecido. Tente novamente.\n")
            continue  # Reinicia o loop

        break  # Sai do loop se tudo deu certo

    except Exception as e:
        print(f"Ocorreu um erro: {e}\nTente novamente.\n")
        continue
