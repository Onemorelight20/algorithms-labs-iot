from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.10f} seconds')
        return result
    return timeit_wrapper


# O(n) for building fail table
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
# O(m) for finding pattern match, where m is the length of text
# together O(m + n)
@timeit
def knuth_morris_pratt_str_match(pattern, text):
    # Compute the failure table for the pattern we're looking up.
    fail = fail_table(pattern)

    # Keep track of the start index and next match position, both of which
    # start at zero since our candidate match is at the beginning and is trying
    # to match the first character.
    index = 0
    match = 0

    # Loop until we fall off the string or match.
    while index + match < len(text):

        # If the current character matches the expected character, then increment the match index.
        if text[index + match] == pattern[match]:
            match = match + 1

            # If we completely matched everything, we're done.
            if match == len(pattern):
                return index

        # Otherwise, we need to look at the fail table to determine what to do next.
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
    res1 = knuth_morris_pratt_str_match("aoa", "ooooooooaaaaoooaoa")
    print("res1 match index is", res1)