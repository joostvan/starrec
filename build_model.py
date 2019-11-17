import pandas as pd
import numpy as np
import joblib
import os
import missingno as msno
from sklearn.neighbors import NearestNeighbors

def value(name, spot, speed, bright, describe):
    ind = joblib.load("indices_model.pkl", mmap_mode = 'r')
    dis = joblib.load("dis_model.pkl", mmap_mode = 'r')
    df = pd.read_csv("HYG-Database-master/df_small_v1.csv")

    #what is your name
    speed = round(speed)
    bright = round(bright)
    name = round(sum(map(ord, name)))
    #what is your birth constellation
    spot_val = round(sum(map(ord, spot))/len(spot))
    ## on a scale of 0 to 4, how fast are you?
    speed_val = speed
    ## how bright are you on a scale from 0 to 4
    bright_val = bright
    ## describe yourself in 10 words:
    describe_val = round(sum(map(ord, describe))/len(describe))
    value = 5 * name + 30*spot_val + 10*speed_val + 10*bright_val + describe_val
    ## you are:
    results = ind[value][0:]

    message = (
            "In the whole universe, your unique star-- the one that is especially yours-- is star number "+ str(results[0]) + ".\n"
           + "It is " + str(round(df.iloc[results[0]]['dist']*3.262, 2)) + " light years away" + "\n"
           + "and it is " + str(round(df.iloc[results[0]]['lum'], 2)) + " times the luminousity of the sun!" + "\n"
           + "It exists in the " + str(df.iloc[results[0]]['con']) + " constellation" + ".\n"
           + "To see it in the sky: it's right ascension is " + str(round(df.iloc[results[0]]['ra'],2)) + " degrees" + "\n"
           + "and it's declination is " + str(round(df.iloc[results[0]]['dec'],2)) + " degrees" + ".\n"

            + "The most similar star to your star is star number "+ str(results[1]) + ".\n"
           + "This one is " + str(round(df.iloc[results[1]]['dist']*3.262, 2)) + " light years away" + "\n"
           + "and it is " + str(round(df.iloc[results[1]]['lum'], 2)) + " times the luminousity of the sun!" + "\n"
           + "It exists in the " + str(df.iloc[results[1]]['con']) + " constellation" + ".\n"
           + "To see it in the sky: it's right ascension is " + str(round(df.iloc[results[1]]['ra'],2)) + " degrees" + "\n"
           + "and it's declination is " + str(round(df.iloc[results[1]]['dec'],2)) + " degrees" + ".\n"

             + "The second most similar star to yours is star number "+ str(results[2]) + ".\n"
           + "This one is " + str(round(df.iloc[results[2]]['dist']*3.262, 2)) + " light years away" + "\n"
           + "and it is " + str(round(df.iloc[results[2]]['lum'], 2)) + " times the luminousity of the sun!" + "\n"
           + "It  exists in the " + str(df.iloc[results[2]]['con']) + " constellation" + ".\n"
           + "To see it in the sky: it's right ascension is " + str(round(df.iloc[results[2]]['ra'],2)) + " degrees" + "\n"
           + "and it's declination is " + str(round(df.iloc[results[2]]['dec'],2)) + " degrees" + ".\n"
    )

    return(message)

#import pickle

#save the model to disk
#filename = 'modelsmall.pkl'
#pickle.dump(nbrs, open(filename, 'wb'))
# load the model from disk
#loaded_model = pickle.load(open(filename, 'rb'))

# joblib.dump(value, "mod3.pkl")
