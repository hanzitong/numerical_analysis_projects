


#include <iostream>
#include <cmath>
#include <vector>
#include <nlopt.hpp>
#include <elipse_circle/elipse_circle.hpp>


int main() {
    auto opt_obj = nlopt::opt(nlopt::LN_COBYLA, 1);
    opt_obj.set_min_objective(elipse_circle::objfunc_example, );



    return 0;
}




