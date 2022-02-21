#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void print(const vector<int>& v)
{
    for (int e : v) {
        cout << "" << e;
    }
    cout << endl;
}

int main()
{
    vector<int> v = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int i = 1;
    while (i < 1000000)
    {
        i++;
        next_permutation(v.begin(), v.end());
    }
    print(v);
}