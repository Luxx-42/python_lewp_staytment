import random

moody_human = ["happy", "sad", "energetic", "calm"]

days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for days in range(len(days_of_the_week)):
    timez_of_day = ["morning", "afternoon", "evening"]
    for time in timez_of_day:
        mood = random.choice(moody_human)
        print("On " + days_of_the_week[days] + " in the " + time + ", you were feeling " + mood + ".")