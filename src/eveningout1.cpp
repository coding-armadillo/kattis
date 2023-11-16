#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
    long int a, b;
    cin >> a >> b;
    long int c = a % b;
    cout << std::min(c, b - c);
    return 0;
}
