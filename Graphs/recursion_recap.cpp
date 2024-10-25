#include <iostream>

using namespace std;

void printNums(int nTimes) {
    if (!(nTimes > 0)) { return; }
    cout << "printing " << nTimes << endl;
    return printNums(nTimes -1);
}

int fibonacci(int n) {
    if (n <= 1) { return n; }
    return fibonacci(n-1) + fibonacci(n-2);
}

int factorial(int n) {
    if (!(n >= 1)) { return 1; }
    return n * factorial (n-1);
}

int main() {
    printNums(10);
    int n = 4;
    int fibSum = fibonacci(n);
    cout << "fibSum for " << n << " = " << fibSum << endl;
    n = 10;
    fibSum = fibonacci(n);
    cout << "fibSum for " << n << " = " << fibSum << endl;
    fibSum = fibonacci(20);
    cout << "fibSum for " << n << " = " << fibSum << endl;

    int fac = factorial(12);
    cout << "factorial(5) = " << fac << endl;
}