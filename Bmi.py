from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    """
    Calcul de l'IMC (Indice de Masse Corporelle)
    Formule: poids (kg) / (taille (m) * taille (m))
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interprétation de l'IMC
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = calculate_bmi(weight, height)
        bmi_category = interpret_bmi(bmi)
        return render_template('result.html', bmi=bmi, category=bmi_category)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
