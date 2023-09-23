def multiple_returns(sentence):
    length = len(sentence)
    if sentence == "":
        first = None
    else:
        first = sentence[0]
    return (length, first)

# sentence = ""
# length, first = multiple_returns(sentence)
# print("Length: {:d} - First character: {}".format(length, first))