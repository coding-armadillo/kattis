#include <iostream>

using namespace std;

int main()
{
    int wc, hc, ws, hs;
    cin >> wc >> hc >> ws >> hs;
    if (wc - 2 >= ws && hc - 2 >= hs)
    {
        cout << 1 << endl;
    }
    else
    {
        cout << 0 << endl;
    }
    return 0;
}
