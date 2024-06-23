
#ifndef ELIPSE_CIRCLE_HPP
#define ELIPSE_CIRCLE_HPP

#include <iostream>
#include <vector>
#include <cassert>


namespace elipse_circle {


struct func_constant{
    double consA = 0;
    double consB = 0;
    double consC = 0;

    func_constant(const double a, const double b, const double c, const double r) {
        assert(r <= c + a);     // if false, elipse is in circle. no intersection.
        assert(r + a <= c);     // if false, elipse is out of circle. no intersection.
        consA = b * b - a * a;
        consB = -2. * c * a;
        consC = a * a * (r * r - b * b - c * c);
    }
};


// the function format nlopt requires
double objfunc_elipse_circle(const std::vector<double>& x, std::vector<double>& grad, void* cons) {
    auto data = (func_constant*)cons;
    double A = data -> consA;
    double B = data -> consB;
    double C = data -> consC;
    double res = A * std::pow(x[0], 2.) + B * x[0] + C;

    std::cout << res << std::endl;

    return res * res;
}


}   // namespace elipse_circle


#endif


