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
    ll x = 0;
    for (ll i = 1; i <= 9; i++) {
        ll y = i * 10 + 9;
        if(y <= n){
            x++;
        }
    }
    cout << x;
}