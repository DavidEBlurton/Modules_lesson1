# Our football team has finished the championship.

# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

# For example: ["3:1", "2:2", "0:1", ...]

# Points are awarded for each match as follows:

# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
# We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

# Notes:

# our team always plays 10 matches in the championship

# 1 define a function that takes in a list
# 2 create variables for the scores that are given
# 3 loop through scores ( we can index or use the .split method)
# 4 check for the condityions listed above
# 5 return the number of points for our teams total


def solution(scores):

    home_team = 0
    for game in scores:
        x = int(game[0])
        y = int(game[2])
        if x > y:
            home_team += 3
        elif x == y:
            home_team += 1
    return home_team