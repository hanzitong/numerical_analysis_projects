

#include <iostream>
#include <fstream>
#include <vector>
#include <elipse_circle/elipse_circle.hpp>


int main() {
    // using namespace elipse_circle;
    elipse_circle::func_constant cons(1.0, 1.0, 1.0, 2.0);  // Change parameters as needed
    std::vector<double> grad;  // Not used in this example
    std::ofstream outfile("output.dat");

    for (double x = -10; x <= 10; x += 0.1) {
        std::vector<double> x_vec = {x};
        double result = elipse_circle::objfunc_elipse_circle(x_vec, grad, &cons);
        outfile << x << " " << result << std::endl;
    }

    outfile.close();
    return 0;
}




