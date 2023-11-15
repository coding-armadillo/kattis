#include <iomanip>
#include <iostream>

using namespace std;

int main()
{
    int n;
    long double e, m;
    cin >> n;
    e = 1;
    m = 1;
    for (int i = 1; i <= n; i++)
    {
        m *= i;
        e += 1 / m;
    }
    cout << std::setprecision(13) << e << endl;
    return 0;
}
