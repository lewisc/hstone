
import random as rnd

def num_games(wins_list, count=25):
    wins = 0
    for ix, val in enumerate(wins_list):
        wins = wins + val
        if wins > count:
            return ix
    return 0
        

def calculate_probabilities(percent, count=10000, approx_duration=10000):
    
    time_taken = {i: 0 for i in range(count)}
    
    for i in range(approx_duration):
        wins_losses = [1 if rnd.random() < percent else -1 for i in range(count)]
        time_taken[num_games(wins_losses)] += 1

    accumulator = 0

    for ix, value in time_taken.iteritems():
        accumulator += value
        if ix % 50 == 0:   
            if accumulator != 0:
                print ix, accumulator
            accumulator = 0

if __name__ == "__main__":
    calculate_probabilities(0.6)
