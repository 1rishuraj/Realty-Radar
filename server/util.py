import pickle
import json
import numpy as np

# global variables as outside fxn
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        # __data_columns is python list that finds 'location.lower()'s index in itself
        # here location.lower() converts location into lowercase as all present in __data_columns
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)
    # here [x] is a 2d array & by [0] we take only its value
    # round(n,2) rounds the predicted value for 2 places of decimal


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        # loading our dict's key 'data_columns' values onto __data_columns python list
        __data_columns = json.load(f)['data_columns'] 
        __locations = __data_columns[3:]  
        # first 3 columns are sqft, bath, bhk; hence taking from 4th column till last

    global __model
    if __model is None:
        with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f: 
            #loading our 'rb' ie. binary pickle model
            __model = pickle.load(f) 
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts() # puts columns and model into '__locations ' and '__model' rspt firstly via _main_
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location