#include "logicfunctions.h"

// Compute xor
void exclusive(bool x, bool y, bool &ans)
{
    ans = x != y;
}

// Compute implication
void implies(bool x, bool y, bool &ans)
{
    if (x && !y)
    {
        ans = false;
    }
    else
    {
        ans = true;
    }
}

// Compute equivalence
void equivalence(bool x, bool y, bool &ans)
{
    ans = x == y;
}
