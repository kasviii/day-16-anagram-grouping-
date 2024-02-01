from collections import defaultdict

def group_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)
    return list(anagram_groups.values())

def main():
    input_list = input("Enter a list of strings separated by space: ").split()
    grouped_anagrams = group_anagrams(input_list)
    print("Output:", grouped_anagrams)

if __name__ == "__main__":
    main()
