from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        rdspend = float(request.form['rdspend'])
        administration=float(request.form['administration'])
        marketing_Spend=float(request.form['marketing_Spend'])
        
        state_type=request.form['state_type']
        state_Florida = 0
        state_New_York = 0
        
        if state_type == 'state_Florida':
            state_Florida = 1
            state_New_York = 0
        elif state_type == 'state_New_York':
            state_Florida = 0
            state_New_York = 1
        
        prediction=model.predict([[rdspend,administration,marketing_Spend,state_Florida,state_New_York]])
        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text='Campany Profits should be $ {}'.format(output))
        
if __name__ == "__main__":
    app.run()