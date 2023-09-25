def best_score(a_dictionary):
    scores = []
    for i, j in a_dictionary.items():
        scores.append(j)
        if j == None:
            return None
    biggest = max(scores)
    for i, j in a_dictionary.items():
        if j == biggest:
            return i
    # biggest = max(scores)
    # return biggest

# a_dictionary = {'John': None, 'Bob': None, 'Mike': None, 'Molly': None, 'Adam': None}
# best_key = best_score(a_dictionary)
# print("Best score: {}".format(best_key))

# best_key = best_score(None)
# print("Best score: {}".format(best_key))
    



