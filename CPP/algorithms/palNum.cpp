#include <cmath>
#include <iostream>

#include <vector>

bool isPalindrome(int x) {
    if (x < 0) return false; // Negative numbers are not palindromes
    if (x == 0) return true;

    // std::cout << "hm" << x << std::endl;

    // Corrected number of digits calculation
    int numDigits = (x > 0) ? ((log10(x)) + 1) : 1;
    int highMod = pow(10, numDigits - 1);

    int lowMod = 1;

    std::vector<int> myVec = {0,1,3};
    // myVec = std::vector<int>{0,1,2};
    // myVec = {0,1,2};

    for (int i = 0; i < numDigits / 2; i++) {
        int highDigit = (x / highMod) % 10; // Extract leftmost digit
        int lowDigit = (x / lowMod) % 10;   // Extract rightmost digit

        if (highDigit != lowDigit) {
            return false;
        }

        highMod /= 10;
        lowMod *= 10;
    }

    return true;
}

int main() {
    int testArray[5] = {1, 123, 35, 101010, 10101};
    int length = sizeof(testArray) / sizeof(testArray[0]);

    for (int i = 0; i < length; i++) {
        std::cout << "Test " << i << ": " << testArray[i] << ", " << isPalindrome(testArray[i]) << std::endl;
    }

    return 0;
}
