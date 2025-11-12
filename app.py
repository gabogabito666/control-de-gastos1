from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gastos")
def gastos():
    # Aquí iría la lógica para calcular y mostrar los gastos
    gastos_semanales = [] # Reemplazar con datos reales
    total = 0 # Reemplazar con el cálculo real
    return render_template("gastos.html", gastos=gastos_semanales, total=total)

@app.route("/ahorro", methods=['GET', 'POST'])
def ahorro():
    capital = 0
    ahorro = 0
    total = 0

    if request.method == 'POST':
        try:
            capital = float(request.form['capital'])
            ahorro = float(request.form['ahorro'])
            total = capital + ahorro
        except ValueError:
            #Manejar el error si no se ingresan números
            total = "Entrada inválida"

    return render_template("ahorro.html", capital=capital, ahorro=ahorro, total=total)


@app.route("/tips")
def tips():
    # Aquí irían los consejos de ahorro
    consejos = [
        "Haz un presupuesto mensual.",
        "Reduce gastos innecesarios.",
        "Compara precios antes de comprar.",
        "Automatiza tus ahorros."
    ]
    return render_template("tips.html", consejos=consejos)

if __name__ == "__main__":
    app.run(debug=True)