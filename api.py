import pandas as pd
import numpy as np
import joblib
import uvicorn
from fastapi import FastAPI
from Houses import Houses

app = FastAPI()
model = joblib.load('house_pricing_joblib')


@app.post('/predict')
def predict_prices(data:Houses):
    data = data.dict()
    bedrooms = data['bedrooms']
    bathrooms = data['bathrooms']
    sqft_living = data['sqft_living']
    sqft_lot = data['sqft_lot']
    floors = data['floors']
    waterfront = data['waterfront']
    view = data['view']
    condition = data['condition']
    grade = data['grade']
    sqft_above = data['sqft_above']
    sqft_basement = data['sqft_basement']
    yr_built = data['yr_built']
    yr_renovated = data['yr_renovated']
    zipcode = data['zipcode']
    sqft_living15 = data['sqft_living15']
    sqft_lot15 = data['sqft_lot15']
    prediction = model.predict([bedrooms, bathrooms, sqft_living, sqft_lot,
                                floors, waterfront, view, condition, grade,
                                sqft_above, sqft_basement, yr_built, yr_renovated,
                                zipcode, sqft_living15, sqft_lot15])
    return {
        f'Based on these specifications, this house should cost ${prediction:.2f}'
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
