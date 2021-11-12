print("Given word:")
word = input()
print("Candidates")
candidates = input()

def findAnagram(candidates):
    anagrams = []
    for candidate in candidates:
        if len(candidate) == len(word):
            sorted_word = sorted(word)
            sorted_candidate = sorted(candidate)
            if sorted_word == sorted_candidate:
                anagrams.append(candidate)
    return anagrams

print(f"List of anagrams matching {word}", findAnagram(candidates.split()))
