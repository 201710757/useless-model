from tensorflow.keras import layers
from tensorflow import keras

class Calc:
    def __init__(self):
        pass

    def build_model(self):
        n_numbers = 2

        model = keras.Sequential()
        model.add(layers.LSTM(6, input_shape=(n_numbers, 1), return_sequences=True))
        model.add(layers.LSTM(6))
        model.add(layers.Dense(1))
        model.compile(loss='mean_squared_error', optimizer='adam')


        #model.add(layers.Dense(4, activation='relu', input_shape=(2,)))
        #model.add(layers.Dense(8, activation='relu'))
        #model.add(layers.Dense(4, activation='relu'))
        #model.add(layers.Dense(1))
        #model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
        return model
    
