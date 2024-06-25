

#include <iostream>
#include <vector>
#include <nlopt.hpp>
#include <elipse_circle/elipse_circle.hpp>


int main() {
    // need to set a, b, c, r parameters to calculate
    double a = 20.;
    double b = 10.;
    double c = 15.;
    double r = 30.;
    std::cout << "input: a=" << a << ", b=" << b << ", c=" << c
              << ", r=" << r << std::endl;

    double opt_x = elipse_circle::calc_intersection(a, b, c, r);
    double ysq = r*r - std::pow(opt_x + c, 2.);
    double y_upper = std::sqrt(ysq);  
    double y_lower = -1. * std::sqrt(ysq);  
    std::cout << "intersection(upper): x=" << opt_x << ", y=" << y_upper << std::endl;
    std::cout << "intersection(lower): x=" << opt_x << ", y=" << y_lower << std::endl;

    return 0;
}


