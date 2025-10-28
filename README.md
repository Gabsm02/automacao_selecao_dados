# 📊 Disponibilidade Bahia - Processamento de Indicadores

Este repositório contém um script Python para automatizar o processamento de indicadores de disponibilidade de rede móvel (2G, 3G, 4G, 5G) por município e por site no estado da Bahia. O script lê planilhas específicas, filtra os dados relevantes e exporta os resultados em novos arquivos Excel.

---

## 🧰 Funcionalidades

- Filtro por UF (Bahia)
- Filtro por data, mês, semana ou ano atual
- Remoção de registros nulos
- Formatação de datas
- Exportação dos dados filtrados para arquivos Excel
- Reinício automático em caso de erro ou arquivo não reconhecido

---

## 📁 Estrutura de Arquivos Esperados

O script reconhece os seguintes arquivos:

- `cdt_diario_municipio_hmm.xlsx` – Indicadores diários por município
- `cdt_municipios_mensal_hmm.xlsx` – Indicadores mensais por município
- `cdt_municipios_semanal_hmm.xlsx` – Indicadores semanais por município
- `cdt_diario_site_hmm.xlsx` – Indicadores diários por site

Os arquivos devem estar localizados em diretórios específicos conforme definidos no script.

---

## ▶️ Como Executar

1. Certifique-se de ter o Python instalado.
2. Instale as dependências:
   ```bash
   pip install pandas openpyxl
   ```
3. Execute o script:
   ```bash
   python disponibilidade_bahia.py
   ```
4. Insira o caminho completo do arquivo solicitado.

---

## 📦 Saídas Geradas

- `registros_diario_municipio.xlsx`
- `registros_mensal_municipio.xlsx`
- `registros_semanal_municipio.xlsx`
- `registros_diario_site.xlsx`

---

## 🛠️ Requisitos

- Python 3.8+
- Pandas
- Openpyxl

---

## 👨‍💻 Autor

Gabriel De Oliveira Mendes
Estagiário - Telefônica

---

## 📌 Observações

- O script reinicia automaticamente se o arquivo informado não for reconhecido.
- Certifique-se de que os nomes dos arquivos estejam corretos e que as colunas esperadas estejam presentes.

---

## 📄 Licença

Este projeto é de uso interno e não possui uma licença pública definida.
