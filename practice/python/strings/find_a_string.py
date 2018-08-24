
def count_substring(string, sub_string):
    count = 0
    i = 0
    substr_len = len(sub_string)

    while i < len(string):
        sample = string[i: i + substr_len]

        if len(sample) < substr_len:
            break

        if sub_string == sample:
            count += 1
        
        i += 1

    return count
