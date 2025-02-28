import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
import os
credentials = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(os.getcwd(), 'lojapratasheets-6cb2a4d5f428.json'), scope)

client = gspread.authorize(credentials)

spreadsheet = client.open('peças cadastradas')
sheet = spreadsheet.worksheet('Página1')

code = input('Digite o código da peça: ')
desc = input('Digite a descrição da peça: ')
dados = [code, desc]

sheet.append_row(dados)
print('✅ Dados enviados com sucesso para o Google Sheets!')
