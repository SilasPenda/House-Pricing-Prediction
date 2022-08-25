from pydantic import BaseModel
class Houses(BaseModel):
    bedrooms: int
    bathrooms: int
    sqft_living: float
    sqft_lot: float
    floors: int
    waterfront: int
    view: int
    condition: int
    grade: float
    sqft_above: float
    sqft_basement: float
    yr_built: int
    yr_renovated: int
    zipcode: int
    sqft_living15: float
    sqft_lot15: float