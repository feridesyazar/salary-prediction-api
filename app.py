from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
model=pickle.load(open('maas.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')   
@app.route('/predict', methods=['POST'])
def predict():  
    tecrube = float(request.form['tecrube'])
    yazili = float(request.form['yazili'])
    mulakat = float(request.form['mulakat'])
    
    prediction = model.predict([[tecrube, yazili, mulakat]])
   #
    return render_template('index.html', prediction=prediction[0][0])
if __name__ == "__main__":
    app.run(debug=True)
