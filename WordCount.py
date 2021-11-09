def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(word_count(input()))

# definitely did not find this script here https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php