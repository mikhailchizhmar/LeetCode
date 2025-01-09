

def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in groups:
            groups[sorted_word] = []
        groups[sorted_word].append(word)

    answer = [group for group in groups.values()]
    return answer


assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
assert group_anagrams([""]) == [['']]
assert group_anagrams(["a"]) == [['a']]

