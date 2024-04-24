from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    result = dict(request.form)
    print(result)
    if 'No' in result['brand']:
        return render_template('error.html', attr='марку автомобиля')
    elif 'No' in result['fuel_type']:
        return render_template('error.html', attr='тип топлива')
    elif 'No' in result['engine']:
        return render_template('error.html', attr='объем двигателя')
    elif 'No' in result['color']:
        return render_template('error.html', attr='цвет кузова')
    elif 'accident' not in result.keys():
        return render_template('error.html', attr='информацию о авариях')

    return render_template('predict.html', cost=2)




if __name__ == '__main__':
    app.run(debug=True)