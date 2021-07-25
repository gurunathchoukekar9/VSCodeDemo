import random


def giveMeMyIQ():
    return random.randint(70, 230)

def descMyIQ(iq_val):
    if iq_val in range(70, 80):
        return "Cognitively impaired"
    elif iq_val in range(80, 90):
        return "Below average intelligence"
    elif iq_val in range(90, 111):
        return "Average intelligence"
    elif iq_val in range(111, 121):
        return "Above average intelligence"
    elif iq_val in range(121, 131):
        return "Gifted"
    else:
        return "Very gifted"
