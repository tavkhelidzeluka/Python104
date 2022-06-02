#include <iostream>
#include <chrono>
#include <vector>

using namespace std;
using namespace std::chrono;


int main() {
    auto start = high_resolution_clock::now();
    vector<int> a = vector<int>();

    for (unsigned i = 0; i < 100000000; i++)
        a.push_back(i);
    
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout << duration.count() << endl;
    return EXIT_SUCCESS;
}