from flask import Flask, render_template, request, jsonify
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

app = Flask(__name__)

class NumericalMethods:
    # Métodos de cálculo aqui
    # Por exemplo, apenas a bisseção:
    @staticmethod
    def bisseccao(f, a, b, tol=1e-6, max_iter=100):
        # Implementação do método de Bisseção
        pass

    # Adicione os outros métodos conforme necessário

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    method = data['method']
    
    # Condições para selecionar o método e processar os dados
    if method == "bisseccao":
        f = lambda x: eval(data['function'])
        a = float(data['a'])
        b = float(data['b'])
        tol = float(data.get('tol', 1e-6))
        result = NumericalMethods.bisseccao(f, a, b, tol)

        # Retornar a raiz e o gráfico como json
        x_values = np.linspace(a, b, 100)
        y_values = [f(x) for x in x_values]
        
        return jsonify({
            'result': result,
            'x_values': x_values.tolist(),
            'y_values': y_values
        })

if __name__ == '__main__':
    app.run(debug=True)
