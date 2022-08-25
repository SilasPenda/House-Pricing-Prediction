import pandas as pd
import streamlit as st
import joblib

model = joblib.load('house_pricing_joblib')

@st.cache

def predict(bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, sqft_above, sqft_basement, zipcode, sqft_living15, sqft_lot15, yr_built, yr_renovated):
    if waterfront == 'Yes':
        waterfront = 1
    else:
        waterfront = 0

    if view == 'No View':
        view = 0
    elif view == 'Fair':
        view = 1
    elif view == 'Good':
        view = 2
    elif view == 'Very Good':
        view = 3
    else:
        view = 4

    if condition == 'Fair':
        condition = 2
    elif condition == 'Good':
        condition = 3
    elif condition == 'Very Good':
        condition = 4
    else:
        condition = 5

    prediction = model.predict(pd.DataFrame([[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, sqft_above, sqft_basement, zipcode, sqft_living15, sqft_lot15, yr_built, yr_renovated]], columns=['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade', 'sqft_above', 'sqft_basement', 'zipcode', 'sqft_living15', 'sqft_lot15', 'yr_built', 'yr_renovated']))
    return prediction



st.title('Housing Price Predictor')
st.image("""https://wi.wallpapertip.com/wsimgs/184-1844063_beautiful-modern-house.jpg""")
st.header('Enter the specifications of the house:')


bedrooms = st.number_input('Bedrooms:', min_value=1.0)
bathrooms = st.number_input('Bathrooms:', min_value=1.0)
sqft_living = st.number_input('Square Feet (Living):', min_value=50.0)
sqft_lot =  st.number_input('Square Feet (Lot):', min_value=0.0)
floors = st.number_input('Floors:', min_value=1.0, max_value=6.0)
waterfront = st.selectbox('Waterfront:', ['Yes', 'No'])
view = st.selectbox('View:', ['No View', 'Fair', 'Good', 'Very Good', 'Excellent'])
condition = st.selectbox('House Condition:', ['Fair', 'Good', 'Very Good', 'Excellent'])
grade = st.number_input('Grade:', min_value=1.0)
sqft_above  = st.number_input('Square Feet (Above):', min_value=0.0)
sqft_basement = st.number_input('Square Feet (Basement):', min_value=0.0)
zipcode = st.number_input('Zipcode:', min_value=0.0)
sqft_living15 = st.number_input('Square Feet (Living15):', min_value=50.0)
sqft_lot15 = st.number_input('Square Feet (Lot15):', min_value=50.0)
yr_built = st.number_input('Year Built:', min_value=0.0)
yr_renovated = st.number_input('Year Renovated:', min_value=0.0)


if st.button('Predict Price'):
    price = predict(bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, sqft_above, sqft_basement, zipcode, sqft_living15, sqft_lot15, yr_built, yr_renovated)
    st.success(f'Based on these specifications, this house should cost ${price[0]:.2f}')