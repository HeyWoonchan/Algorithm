#include <iostream>
#include <map>

using namespace std;

bool isPelindrome(string s,int l, int r){
    if (l>r){
        return true;
    }
    if (s[l]==s[r]){
        return isPelindrome(s,l+1,r-1);
    }
    return false;
}
int main(){
    map<string, string> mp = {
        {"A",".-"}, {"B" , "-..."}, {"C" , "-.-."}, {"D" , "-.."}, {"E" , "."},
        {"F" , "..-."}, {"G" , "--."}, {"H" , "...."}, {"I" , ".."}, {"J" , ".---"},
        {"K" , "-.-"}, {"L" , ".-.."}, {"M" , "--"}, {"N" , "-."}, {"O" , "---"},
        {"P" , ".--."}, {"Q" , "--.-"}, {"R" , ".-."}, {"S" , "..."}, {"T" , "-"},
        {"U" , "..-"}, {"V" , "...-"}, {"W" , ".--"}, {"X" , "-..-"}, {"Y" , "-.--"},
        {"Z" , "--.."}, {"0" , "-----"}, {"1" , ".----"}, {"2" , "..---"}, {"3" , "...--"},
        {"4" , "....-"}, {"5" , "....."}, {"6" , "-...."}, {"7" , "--..."}, {"8" , "---.."},
        {"9" , "----."}
    };

    string s;
    getline(cin,s);
    string masked="";
    // cout<<"최초입력:"<<s<<'\n';
    for (int i=0;i<s.length();i++){
        if ((s[i]>='A' && s[i]<='Z')||(s[i]<='z'&&s[i]>='a')||(s[i]>='0'&&s[i]<='9')){
                masked+=mp[string(1,toupper(s[i]))];
            
        }
    }
    // cout<<"maksed: "<<masked<<'\n';
    if (masked.length()>0 and isPelindrome(masked,0,masked.length()-1)==true){
        cout<<"YES";
    }
    else{
        cout<<"NO";
    }
    // cout<<masked;



}



