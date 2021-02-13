from flask  import Flask ,render_template,jsonify,request
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd

application=Flask(__name__)

@application.route('/',methods=['GET'])
@cross_origin()
def homepage():
    return render_template("index.html")

@application.route('/predict',methods=['POST','GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            print('Hello')
            Pregnancies = int(request.form['Pregnancies'])
            Glucose = int(request.form['Glucose'])
            BloodPressure = int(request.form['BloodPressure'])
            SkinThickness = int(request.form['SkinThickness'])
            Insulin = int(request.form['Insulin'])
            BMI = float(request.form['BMI'])
            DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
            Age = int(request.form['Age'])


            with open("StandardScaler.sav", 'rb') as f:
                scalar = pickle.load(f)
            with open("Log_Model.sav",'rb') as f:
                model=pickle.load(f)

            data=pd.DataFrame()
            data=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
            scaled_data=scalar.transform([data])
            predict=model.predict(scaled_data)

            if predict[0]==1:
                result='Diabetic'
            else :
                result='Non-Diabetic'

            return render_template('result.html',result=result)

        except Exception as e:
            print('The Exception message is : ', e)
            return 'Something is Wrong '

    else :
        return render_template("index.html")


if __name__ == '__main__':
    application.run(debug=True)


