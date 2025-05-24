def anagrams(words):
    groups = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return (groups.values())
n = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
result = anagrams(n)
print(result)