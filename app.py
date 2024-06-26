from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

application=Flask(__name__)
app = application

## Route for a home page

@app.route('/', methods=['GET', 'POST'])
def predict_expenses():
    if request.method=='GET':
        return render_template('prediction.html')
    else:
        data=CustomData(
            age=request.form.get('age'),
            sex=request.form.get('sex'),
            bmi=request.form.get('bmi'),
            children=request.form.get('children'),
            smoker=request.form.get('smoker'),
            region=request.form.get('region'),


        )
        pred_df=data.get_data_as_data_frame()
        # print(pred_df)

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        premium='Premium :'
        return render_template('prediction.html', results=results[0], premium=premium)
    

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
