MorseCode = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".",
"F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---",
"K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---",
"P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-",
"U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--",
"Z":"--..", "0":"-----", "1":".----", "2":"..---", "3":"...--",
"4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..",
"9":"----."}

def isPelindrome(s, l,r):
    if l>=r:
        return True
    if s[l]==s[r]:
        return isPelindrome(s,l+1,r-1)
    else:
        return False

a = input()
s = ''
for i in a:
    if 'a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9':
        s+=MorseCode[i.upper()]
# print(s)
if s!='' and isPelindrome(s,0,len(s)-1):
    print("YES")
else:
    print("NO")