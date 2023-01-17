#include "vectorfunctions.h"
#include <algorithm>

void backwards(std::vector<int> &vec)
{
    vec = std::vector<int>(vec.rbegin(), vec.rend());
}

std::vector<int> everyOther(const std::vector<int> &vec)
{
    std::vector<int> ans;

    for (int i = 0; i < vec.size(); i += 2)
        ans.push_back(vec[i]);

    return ans;
}

int smallest(const std::vector<int> &vec)
{
    return *min_element(vec.begin(), vec.end());
}

int sum(const std::vector<int> &vec)
{
    int ans = 0;

    for (auto it = begin(vec); it != end(vec); ++it)
    {
        ans += *it;
    }

    return ans;
}

int veryOdd(const std::vector<int> &suchVector)
{
    int ans = 0;
    for (int i = 1; i < suchVector.size(); i += 2)
    {
        if (suchVector[i] % 2 == 1)
            ans++;
    }

    return ans;
}
