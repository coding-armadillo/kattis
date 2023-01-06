#include <iostream>

using namespace std;

int main(){
    int n, s, m, curspace, cnt = -1;
    cin >> n >> s >> m;
    int board[n];

    for (int i = 0; i < n; i++){
        int tmp;
        cin >> tmp;
        board[i] = tmp;
    }
    curspace = s - 1;

    while (true){
        int temp = 0;
        cnt += 1;
        temp += board[curspace];
        board[curspace] = 0;
        curspace += temp;

        if (temp == 0){
            cout << "cycle" << endl;
            break;
        }
        else if (temp == m){
            cout << "magic" << endl;
            break;
        }
        else if (curspace < 0){
            cout << "left" << endl;
            break;
        }
        else if (curspace > n-1){
            cout << "right" << endl;
            break;
        }
    }
    cout << cnt << endl;
}