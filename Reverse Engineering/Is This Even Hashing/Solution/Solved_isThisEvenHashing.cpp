#include <iostream>
#include <chrono>
#include <thread>
#define ll long long
using namespace std;

ll hashIt(ll n, ll x, ll m){
    ll ans = 0;
    for (int i=0; i<x; i++){
        ans += n;
        ans %=m;
    }
    return ans;
}

ll hashHash(ll n){
    std::this_thread::sleep_for(std::chrono::milliseconds(50));
    return (n << 32) + (n >> 32);
}

int main(int argc, char *argv[]){
    if (argc == 1) cout << "Enter atleast 1 argument \n";
    else {
        for (int i=1; i<argc; i++){
            // cout << hashHash(hashIt(stoll(argv[i]), 961798719, 1000000000)) << "\n";
            cout << hashIt(hashHash(stoll(argv[i])), 279954879, 1000000000) << "\n";
        }
    }
    return 0;
}