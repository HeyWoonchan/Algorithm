textToMorse = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".",
"F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---",
"K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---",
"P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-",
"U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--",
"Z":"--..", "_":"..--", ".":"---.", ",":".-.-", "?":"----"}

morseToText = {}
for a in textToMorse.keys():
    morseToText[textToMorse[a]]=a

import sys
input = sys.stdin.readline

n = int(input())
for tc in range(n):
    cypherText=input().rstrip()
    cypherMorseArr=[textToMorse[a] for a in cypherText]
    cypherMorseLenArr = [len(a) for a in cypherMorseArr]
    cypherMorseLenArr.reverse()
    cypherMorse="".join(cypherMorseArr)
    nowIndex = 0
    plainText=""
    for i in range(len(cypherMorseLenArr)):
        plainText+=morseToText[cypherMorse[nowIndex:nowIndex+cypherMorseLenArr[i]]]
        nowIndex=nowIndex+cypherMorseLenArr[i]
    print(f"{tc+1}: {plainText}")
    

