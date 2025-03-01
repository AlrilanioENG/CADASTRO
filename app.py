from flask import Flask, render_template, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

app = Flask(__name__)

# Configuração da API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(os.getcwd(), 'lojapratasheets-6cb2a4d5f428.json'), scope)
client = gspread.authorize(credentials)
spreadsheet = client.open('peças cadastradas')
sheet = spreadsheet.worksheet('Página1')

@app.route('/')
def index():
    return render_template('index.html', success=False)

@app.route('/submit', methods=['POST'])
def submit():
    code = request.form['code']
    desc = request.form['desc']
    if code and desc:
        dados = [code, desc]
        sheet.append_row(dados)
        return render_template('index.html', success=True)
    else:
        return '⚠️ Preencha todos os campos!'

if __name__ == '__main__':
    app.run(debug=True)

