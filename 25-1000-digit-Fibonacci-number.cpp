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

// Asssumes that a is leq to b
vector<int> add(vector<int>& a, vector<int>& b)
{
    vector<int> c = b;
    for (int i = 0; i < a.size(); i++)
    {
        c[c.size() - i - 1] += a[a.size() - i - 1];
    }
    reverse(c.begin(), c.end());
    int l = c.size();
    for (int i = 0; i < c.size() - 1; i++)
    {
        if (c[i] > 9)
        {
            c[i + 1] += 1;
            c[i] %= 10;
        }
    }

    if (c.back() > 9)
    {
        c.back() %= 10;
        c.push_back(1);
    }
    reverse(c.begin(), c.end());
    if (c.front() == 0)
    {
        c.erase(c.begin());
    }

    return c;
}
int main()
{
    vector<int> x = {0};
    vector<int> y = {1};
    vector<int> temp = y;
    

    add(x, y);
    // print(add(x, y));
    int index = 1;
    while (x.size() < 1000)
    {
        temp = x;
        x = y;
        y = add(temp, y);
        cout << index << " : ";
        print(x);
        index++;
    }
}


