#include <iostream>

using namespace std;

int main()
{
    int h, m;
    cin >> h >> m;

    int mm = m - 45;
    int borrow = 0;
    if (mm < 0)
    {
        mm += 60;
        borrow = 1;
    }
    int hh = h - borrow;
    if (hh < 0)
    {
        hh += 24;
    }
    cout << hh << " " << mm << endl;
    return 0;
}
