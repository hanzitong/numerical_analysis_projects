

#include <iostream>
#include <vector>
#include <nlopt.hpp>
#include <elipse_circle/elipse_circle.hpp>


int main() {
    // auto opt_obj = nlopt::opt(nlopt::LN_COBYLA, 1);    // nlopt::opt(nlopt::algorithm, unsigned n);
    auto opt_obj = nlopt::opt(nlopt::GN_DIRECT, 1);    // nlopt::opt(nlopt::algorithm, unsigned n);
    const char* name_algo = opt_obj.get_algorithm_name();

    std::cout << name_algo << std::endl;
    std::cout << "dimension: " << opt_obj.get_dimension() << std::endl;

    // need to set a, b, c, r parameters to calculate
    double a = 20.;
    double b = 10.;
    double c = 15.;
    double r = 30.;
    elipse_circle::func_constant cons(a, b, r, r);
    opt_obj.set_min_objective(elipse_circle::objfunc_elipse_circle, &cons);
    opt_obj.set_lower_bounds(std::vector<double>(1, 0.));
    opt_obj.set_upper_bounds(std::vector<double>(1, r));

    double min_val = 0;
    std::vector<double> ini_val(1, 0.);  // initial value should be in elipse or circle
    std::cout << ini_val[0] << std::endl;
    opt_obj.optimize(ini_val, min_val);


    return 0;
}


