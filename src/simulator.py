import random


def creation_of_prediction(r):

    predictions = []

    for coin in range(r):

        coin = random.choice(["H", "T"])
        predictions.append(coin)

    return predictions


def streaks(predictions):

    streak_h = 0
    streak_h_max = 0

    streak_t = 0
    streak_t_max = 0

    for i in predictions:

        if i == "H":
            streak_h += 1
            if streak_t > streak_t_max:
                streak_t_max = streak_t
            streak_t = 0

        if i == "T":
            streak_t += 1
            if streak_h > streak_h_max:
                streak_h_max = streak_h
            streak_h = 0

    if streak_h > streak_h_max:
        streak_h_max = streak_h

    if streak_t > streak_t_max:
        streak_t_max = streak_t

    return streak_h_max, streak_t_max
