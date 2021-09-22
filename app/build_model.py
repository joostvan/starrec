import pandas as pd
import joblib


def value(name, spot, speed, bright, describe):
    ind = joblib.load("/home/joostvan/StarRec/indices_model.pkl", mmap_mode = 'r')
    dis = joblib.load("/home/joostvan/StarRec/dis_model.pkl", mmap_mode = 'r')
    df = pd.read_csv("/home/joostvan/StarRec/HYG-Database-master/df_small_v1.csv")

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

    ys = (
            "In the whole universe, your unique star-- the one that is especially yours-- is star number "+ str(results[0]) + ".\n"
           + "It is " + str(round(df.iloc[results[0]]['dist']*3.262, 2)) + " light years away" + "\n"
           + "and it is " + str(round(df.iloc[results[0]]['lum'], 2)) + " times the luminousity of the sun!" + "\n"
           + "It exists in the " + str(df.iloc[results[0]]['con']) + " constellation" + ".\n"
           + "To see it in the sky: it's right ascension is " + str(round(df.iloc[results[0]]['ra'],2)) + " degrees" + "\n"
           + "and it's declination is " + str(round(df.iloc[results[0]]['dec'],2)) + " degrees" + ".\n"
    )
    ysrec = (str(round(df.iloc[results[0]]['ra'],2)))
    ysdec = (str(round(df.iloc[results[0]]['dec'],2)))
    ysurl = (
        "https://skyview.gsfc.nasa.gov/current/cgi/runquery.pl?survey=DSS&coordinates=J2000.0&projection=Tan&scaling=Log&sampler=Default&lut=colortables/b-w-linear.bin&size=0.07083333,0.07083333&pixels=500&position=" + ysrec + "," + ysdec)
    fs = (
        "The most similar star to your star is star number "+ str(results[1]) + ".\n"
           + "This one is " + str(round(df.iloc[results[1]]['dist']*3.262, 2)) + " light years away" + "\n"
           + "and it is " + str(round(df.iloc[results[1]]['lum'], 2)) + " times the luminousity of the sun!" + "\n"
           + "It exists in the " + str(df.iloc[results[1]]['con']) + " constellation" + ".\n"
           + "To see it in the sky: it's right ascension is " + str(round(df.iloc[results[1]]['ra'],2)) + " degrees" + "\n"
           + "and it's declination is " + str(round(df.iloc[results[1]]['dec'],2)) + " degrees" + ".\n"
    )
    fsrec = (str(round(df.iloc[results[1]]['ra'],2)))
    fsdec = str(round(df.iloc[results[1]]['dec'],2))
    fsurl = ("https://skyview.gsfc.nasa.gov/current/cgi/runquery.pl?survey=DSS&coordinates=J2000.0&projection=Tan&scaling=Log&sampler=Default&lut=colortables/b-w-linear.bin&size=0.07083333,0.07083333&pixels=500&position=" + fsrec + "," + fsdec)
    ss = (
        "The second most similar star to yours is star number "+ str(results[2]) + ".\n"
           + "This one is " + str(round(df.iloc[results[2]]['dist']*3.262, 2)) + " light years away" + "\n"
           + "and it is " + str(round(df.iloc[results[2]]['lum'], 2)) + " times the luminousity of the sun!" + "\n"
           + "It  exists in the " + str(df.iloc[results[2]]['con']) + " constellation" + ".\n"
           + "To see it in the sky: it's right ascension is " + str(round(df.iloc[results[2]]['ra'],2)) + " degrees" + "\n"
           + "and it's declination is " + str(round(df.iloc[results[2]]['dec'],2)) + " degrees" + ".\n"
    )
    ssrec = str(round(df.iloc[results[2]]['ra'],2))
    ssdec = str(round(df.iloc[results[2]]['dec'],2))
    ssurl = ("https://skyview.gsfc.nasa.gov/current/cgi/runquery.pl?survey=DSS&coordinates=J2000.0&projection=Tan&scaling=Log&sampler=Default&lut=colortables/b-w-linear.bin&size=0.07083333,0.07083333&pixels=500&position=" + ssrec + "," + ssdec)
    return ys, fs, ss, ysurl, fsurl, ssurl, ysrec, ysdec, fsrec, fsdec, ssrec, ssdec

#import pickle

#save the model to disk
#filename = 'modelsmall.pkl'
#pickle.dump(nbrs, open(filename, 'wb'))
# load the model from disk
#loaded_model = pickle.load(open(filename, 'rb'))

# joblib.dump(value, "mod3.pkl")
