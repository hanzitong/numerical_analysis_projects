
#include <iostream>
#include <string>
#include <vector>
#include <nlopt.hpp>
#include <cassert>
#include <elipse_circle/elipse_circle.hpp>



int main() {
    auto opt_obj = nlopt::opt(nlopt::LN_COBYLA, 1);    // nlopt::opt(nlopt::algorithm, unsigned n);
    const char* name_algo = opt_obj.get_algorithm_name();

    std::cout << name_algo << std::endl;
    std::cout << "dimension: " << opt_obj.get_dimension() << std::endl;

    // need to set a, b, c, r parameters to calculate
    elipse_circle::func_constant cons(20., 10., 10., 30.);
    opt_obj.set_min_objective(elipse_circle::objfunc_elipse_circle, &cons);
    opt_obj.set_lower_bounds(std::vector<double>(1, 0.));
    opt_obj.set_upper_bounds(std::vector<double>(1, 100.));

    double min_val = 0;
    std::vector<double> ini_val(1, 50.);
    opt_obj.optimize(ini_val, min_val);


    return 0;
}


