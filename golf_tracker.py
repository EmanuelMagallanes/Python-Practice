golfer = {
    "name": "eman",
    "handicap": 18,
    "scores": [92, 85, 97, 88, 90]
}

golfer["scores"].append(83)
print("Golfer: ", golfer["name"])

all_scores = sum(golfer["scores"])
num_scores = len(golfer["scores"])
smallest_number = min(golfer["scores"])

print("Rounds Played: ", num_scores)

average_num = all_scores / num_scores

average_num = round(average_num, 2)

print("Average Score: ", average_num)
print("Lowest Score: ", smallest_number)