sentence = input()
# to lower, remove duplicate characters
# Will not work if string contains numbers/special characters
if len(sorted("".join(set((sentence.lower()))))) == 27:
    print('Thats a panagram!')
else:
    print('Thats not a panagram :(')