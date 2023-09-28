#include <iostream>

using namespace std;

int main()
{
    string a;
    cin >> a;

    if (a.find("ss") == -1)
    {
        cout << "no hiss" << endl;
    }
    else
    {
        cout << "hiss" << endl;
    }

    return 0;
}
