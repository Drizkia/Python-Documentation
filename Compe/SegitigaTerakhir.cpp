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

    ll x, y, z;
    cin >> x >> y >> z;
    
    bool luas_positif = (x + y > z) && (y + z > x) && (x + z > y);
    bool kondisi_terakhir = false;
    vector<ll> sisi = {x, y, z};
    sort(sisi.begin(), sisi.end());
    if (sisi[0] == sisi[1] && sisi[2] == sisi[0] + 1) {
        kondisi_terakhir = true;
    }
    
    if (luas_positif && kondisi_terakhir) {
        cout << "Ya";
    } else {
        cout << "Tidak";
    }

    return 0;
}