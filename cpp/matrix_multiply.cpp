#include <iostream>
# include <vector>
# include <chrono>
# include <cstdlib>

using namespace std;
using namespace chrono;

// Function to multiply two matrices
vector<vector<double>> multiply(vector<vector<double>>& A,
                                 vector<vector<double>>& B,
                                 int n) {
    vector<vector<double>> C(n, vector<double>(n, 0.0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            for (int k =0; k < n; k++)
                C[i][j] += A[i][k] * B[k][j];
    return C;                                        
}

int main() {
    int n = 200; // 200x200 matrix

    // Create two random matrices
    vector<vector<double>> A(n, vector<double>(n));
    vector<vector<double>> B(n, vector<double>(n));

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)  {
            A[i][j] = rand() % 100;
            B[i][j] = rand() % 100;
        }

    // Time the multiplication
    auto start = high_resolution_clock::now();
    vector<vector<double>> C = multiply( A, B, n);
    auto end = high_resolution_clock::now();

    duration<double> elapsed = end - start;

    cout << "Matrix size " << n << "x" << n << endl; 
    cout << "C++ execution time: " << elapsed.count() << " seconds" << endl;

    return 0;
}
