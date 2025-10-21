#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
/*
  __
<(o )___
 ( ._> /
  `---'
*/
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    ll n;
    cin >> n;
    bool valid = true;
    while (n > 0) {
        ll digit = n % 5;
        if (digit <= 2) {
            if (digit == 2) {
                valid = false;
                break;
            }
        } else {
            if (digit == 3) {
                valid = false;
                break;
            }
            n++;
        }
        n /= 5;
    }
    if (valid) {
        cout << "YES";
    } else {
        cout << "NO";
    }
}