def fail_table(pattern):
    result = [None]

    for i in range(len(pattern)):
        j = i

        while True:
            if j == 0:
                result.append(0)
                break

            if pattern[result[j]] == pattern[i]:
                result.append(result[j] + 1)
                break

            j = result[j]

    return result


# We compute the failure table, which
# is done above.  Next, we iterate across the string, keeping track of a
# candidate start point and length matched so far.  Whenever a match occurs, we
# update the length of the match we've made.  On a failure, we update these
# values by trying to preserve the maximum proper border of the string we were
# able to manage by that point.
def knuth_morris_pratt_str_match(pattern, string):
    # Compute the failure table for the pattern we're looking up.
    fail = fail_table(pattern)

    # Keep track of the start index and next match position, both of which
    # start at zero since our candidate match is at the beginning and is trying
    # to match the first character.
    index = 0
    match = 0

    # Loop until we fall off the string or match.
    while index + match < len(string):

        # If the current character matches the expected character, then bump up
        # the match index.
        if string[index + match] == pattern[match]:
            match = match + 1

            # If we completely matched everything, we're done.
            if match == len(pattern):
                return index

        # Otherwise, we need to look at the fail table to determine what to do
        # next.
        else:
            # If we couldn't match the first character, then just advance the
            # start index.  We need to try again.
            if match == 0:
                index = index + 1

            # Otherwise, see how much we need to skip forward before we have
            # another feasible match.
            else:
                index = index + match - fail[match]
                match = fail[match]

    # If we made it here, then no match was found.
    return -1


if __name__ == '__main__':
    res = knuth_morris_pratt_str_match("aoa", "ooooooooaaaaoooaoa")
    print(res)