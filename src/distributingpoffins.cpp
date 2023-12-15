#include <iostream>

using namespace std;

int main()
{
    long long n, m;
    cin >> n >> m;

    if (m % n == 0)
    {
        cout << 0;
    }
    else
    {
        cout << 1;
    }

    return 0;
}
