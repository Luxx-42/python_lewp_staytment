import random

moody_human = ["happy", "sad", "energetic", "calm"]

days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for days in range(len(days_of_the_week)):
    print("On " + days_of_the_week[days] + " your were feeling " + random.choice(moody_human) + ".")
