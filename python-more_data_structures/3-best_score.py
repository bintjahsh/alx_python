def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    else:
        scores = []
        for i, j in a_dictionary.items():
            scores.append(j)
            biggest = max(scores)
        for i, j in a_dictionary.items():
            if j == biggest:
                return i
    # biggest = max(scores)
    # return biggest

# a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
# best_key = best_score(a_dictionary)
# print("Best score: {}".format(best_key))

# best_key = best_score(None)
# print("Best score: {}".format(best_key))
    



