from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        return f"Olá, {nome}! Você tem {idade} anos."
    return '''
        <form method="POST">
            <label for="nome">Nome:</label>
            <input type="text" name="nome" id="nome"><br>
            <label for="idade">Idade:</label>
            <input type="text" name="idade" id="idade"><br>
            <input type="submit" value="Enviar">
        </form>
    '''

if __name__ == '__main__':
    app.run()
