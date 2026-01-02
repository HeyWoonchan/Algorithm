sentence=input()
vowel = ['a','e','i','o','u']
for i in range(len(sentence)-1):
    if sentence[i] in vowel and sentence[i+1] in vowel:
        print(0)
        exit(0)
    if sentence[i] not in vowel and sentence[i+1] not in vowel:
        print(0)
        exit(0)
print(1)