#include <iostream>

using namespace std;

int main()
{
    int n, s, m, curspace, cnt = 0;
    cin >> n >> s >> m;
    int board[n];

    for (int i = 0; i < n; i++)
    {
        int tmp;
        cin >> tmp;
        board[i] = tmp;
    }
    curspace = s - 1;

    while (true)
    {
        if (curspace < 0)
        {
            cout << "left" << endl;
            break;
        }
        else if (curspace > n - 1)
        {
            cout << "right" << endl;
            break;
        }
        int temp = board[curspace];
        if (temp == 999)
        {
            cout << "cycle" << endl;
            break;
        }
        else if (temp == m)
        {
            cout << "magic" << endl;
            break;
        }
        else
        {
            cnt += 1;
            board[curspace] = 999;
            curspace += temp;
        }
    }
    cout << cnt << endl;
}
