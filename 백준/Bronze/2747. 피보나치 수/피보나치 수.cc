#include <iostream>

using namespace std;

int main() {
	int n;

    cin>>n;
	
    int f, s;
    f = 0; s = 1;
    int tmp;
    
    for(int i=0;i<n;i++){
        tmp = f+s;
        s = f;
        f = tmp;
    }
    
    cout<<f;
	return 0;

}