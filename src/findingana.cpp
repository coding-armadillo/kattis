#include <iostream>

using namespace std;

int main()
{
    string a;
    cin >> a;

    int found = a.find_first_of("a");

    cout << a.substr(found);

    return 0;
}
