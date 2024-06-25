
#ifndef ELIPSE_CIRCLE_HPP
#define ELIPSE_CIRCLE_HPP

#include <iostream>
#include <vector>
#include <nlopt.hpp>
#include <cassert>
#include <cmath>


namespace elipse_circle {


struct FuncConstant{
    double consA = 0;
    double consB = 0;
    double consC = 0;

    FuncConstant(const double a, const double b, const double c, const double r) {
        assert(r <= c + a);     // if false, elipse is in circle. no intersection.
        assert(r + a >= c);     // if false, elipse is out of circle. no intersection.

        consA = b * b - a * a;
        consB = -2. * c * a * a;
        consC = a * a * (r * r - b * b - c * c);
    }
};


double objfunc_elipse_circle(const std::vector<double>& x, std::vector<double>& grad, void* cons) {
    auto data = (FuncConstant*)cons;
    double A = data -> consA;
    double B = data -> consB;
    double C = data -> consC;
    double res = A * std::pow(x[0], 2.) + B * x[0] + C;

    return res * res;
}


double calc_intersection(const double a, const double b, const double c, const double r) {
    auto opt_obj = nlopt::opt(nlopt::LN_COBYLA, 1);    // nlopt::opt(nlopt::algorithm, unsigned n);
    FuncConstant cons(a, b, c, r);
    double min_val = 0;
    std::vector<double> ini_val(1, a / 2.);

    opt_obj.set_min_objective(objfunc_elipse_circle, &cons);
    // opt_obj.set_lower_bounds(std::vector<double>(1, -a));
    // opt_obj.set_upper_bounds(std::vector<double>(1, a));
    opt_obj.set_stopval(1e-6);
    std::cout << "before optimization: " << ini_val[0] << std::endl;
    opt_obj.optimize(ini_val, min_val);
    std::cout << "after optimization: " << ini_val[0] << std::endl;

    // for safety
    assert(std::abs(min_val) < 0.00001);


    return ini_val[0];
}


}   // namespace elipse_circle


#endif


