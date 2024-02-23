import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
import numpy as np
import pandas as pd
# text preprocessing
from nltk.tokenize import word_tokenize
import re
import nltk
nltk.download('punkt')

import random
classnames= ['joy', 'fear', 'anger', 'sadness', 'neutral']
max_seq_len=500


data_train = pd.read_csv('DataSet\data_train.csv', encoding='utf-8')
data_test = pd.read_csv('DataSet\data_test.csv', encoding='utf-8')

data = data_train.append(data_test, ignore_index=True)
def clean_text(data):
    
    # remove hashtags and @usernames
    data = re.sub(r"(#[\d\w\.]+)", '', data)
    data = re.sub(r"(@[\d\w\.]+)", '', data)
    
    # tekenization using nltk
    data = word_tokenize(data)
    
    return data


texts = [' '.join(clean_text(text)) for text in data.Text]

import time

tokenizerr = Tokenizer()
tokenizerr.fit_on_texts(texts)

MODEL = tf.keras.models.load_model('anie.h5')
xy=["i won the lottery"]
seq = tokenizerr.texts_to_sequences(xy)
print(seq)
padded = pad_sequences(seq, maxlen=max_seq_len)
print(padded)
x=MODEL.predict(padded)
emotion99=classnames[np.argmax(x)]
print(xy)
print(x)
print(emotion99)
type(emotion99)
ajoy=["Your close ones will be very happy knowing that you should share this news with them also!","I am so proud of you, and I hope you are too!","You're an awesome friend.","You’re so kind everyone instantly feels like your friend and I hope people become more like you"]
afear=["Try focusing on how to fight your fears.","If you are so afraid of this then actually you should face it more and overcome it because staying in fear won't help","You’re allowed to feel anxious, even if you don’t know the reason why. but don't let it get heavy on you"]
aanger=["Stop stressing out, things will change with time","The more you think about it, it will disturb you. ","You should rather concentrate on other things","You have every right to be mad, but try to talk this through with them.","don't let your anger consume you, its would be your loss again","sometimes we need to also understand other person's perspective and their situation that would help you deal with your feelings in a better way"]
asad=["The more you think about it, it will disturb you. You should rather concentrate on other things","I suggest you to go and meet your friends, and spent some quality time with them","Do something that you like, like whatever is your hobby and shift your attention towards other things.","You can go out for a walk and give yourself some time and space to get through this tough time.","sometimes we think that bad happens to us only but that's not the case we all suffer through things but should understand and learn from things to give our life a better direction"]
aneutral=["you are doing great,Keep it up!!","Keep it up!!"]


def predict(y):
    doo=[y]
    seq = tokenizerr.texts_to_sequences(doo)
    padded = pad_sequences(seq, maxlen=max_seq_len)
    x=MODEL.predict(padded)
    emotion99=classnames[np.argmax(x)]
    emotion9=emotion99
    if emotion9=="joy":
        v=random.choice(ajoy)
    elif emotion9=="sadness":
        v=random.choice(asad)
    elif emotion9=="fear":
        v=random.choice(afear)
    elif emotion9=="angry":
        v=random.choice(aanger)
    else:
        v=random.choice(aneutral)
    u="(Emotion detected is : "+emotion99+") "+v

    # answer="Keep it up!!"
    return u

# def predict(txt):
#     u= "Reply is"+txt
#     return u