#include <iostream>
using namespace std;

// By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

int main()
{
    int fib1 = 1;
    int fib2 = 1;
    int sum = 0;
    int result = 0;

    while ( result < 4000000)
    {
        if (result % 2 ==0)
        {
            sum += result;
        }
        
        result = fib1 + fib2;
        fib2 = fib1;
        fib1 = result;
    }
    
    cout << sum << endl;

    return 0;
}
