from flask import Flask
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> Working </h1>'

@app.route('/predict')
def predict():
    import joblib
    import pandas as pd
    model = joblib.load('../Models/chicago_model.ml')
    column_labels = ['sqfeet', 'beds', 'baths', 'cats_allowed', 'dogs_allowed','smoking_allowed', 'wheelchair_access','electric_vehicle_charge','comes_furnished', 'laundry_options', 'parking_options', 'region']
    apartment_info = pd.DataFrame(data=[[1250, 2, 1, 1, 1, 0, 0, 0, 1, 'laundry in bldg', 'street parking', 9]], columns=X.columns)
    
    price_predict = model.predict(apartment_info)
    
    #model_predict = model.predict([[request.args['region'],
    #                                request.args['type'],
    #                                request.args['sqfeet'],
    #                                request.args['beds'],
    #                                request.args['baths'],
    #                                request.args['cats_allowed'],
    #                                request.args['dogs_allowed'],
    #                                request.args['comes_furnished'],
    #                                request.args['laundry_options'],
    #                                request.args['parking_options']]])
    
    return str(price_predict)

if __name__ == '__main__':
    app.run(debug=True)