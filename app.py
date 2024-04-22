from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('predict.html')


@app.route('/predict', methods=['POST'])
def predict():
    return 




if __name__ == '__main__':
    app.run(debug=True)