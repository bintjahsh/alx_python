def best_score(a_dictionary):
    scores = list(a_dictionary)
    biggest = [i for i, j in a_dictionary.items() if j == max(scores)]
    # for i, j in a_dictionary.items:
    #     if j == None:
    #         return None
    #     else:
    #         biggest = 
    # biggest = max(scores)
    return biggest

# a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
# best_key = best_score(a_dictionary)
# print("Best score: {}".format(best_key))

# best_key = best_score(None)
# print("Best score: {}".format(best_key))
    



