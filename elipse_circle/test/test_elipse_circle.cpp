
#include <random>
#include <cassert>
#include <gtest/gtest.h>
// #include <elipse_circle/elipse_circle.hpp>
#include "../include/elipse_circle/elipse_circle.hpp"


TEST(IntersectionTest, RangeSolution) {
    /* rand num generation about a, b, c, r */
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<double> dis_a(30, 60);
    double a = dis_a(gen);
    std::uniform_real_distribution<double> dis_bdiff(5, 20);
    double b = a - dis_bdiff(gen);
    std::uniform_real_distribution<double> dis_c(a + 10, 2 * a - 10);
    double c = dis_c(gen);
    std::uniform_real_distribution<double> dis_r(c - a + 10, c + a);
    double r = dis_r(gen);

    /* skiving */
    // std::uniform_real_distribution<double> dis_a(50, 100);
    // double a = dis_a(gen);
    // double b = a * std::cos(M_PI / 4.);
    // std::uniform_real_distribution<double> dis_c(a + 10, 60);
    // double c = dis_c(gen);
    // std::uniform_real_distribution<double> dis_r(100, 225);
    // double r = dis_r(gen);

    /* check if test condition is correct */
    ASSERT_LE(r, c + a);    // if false, elipse is in circle. no intersection.
    ASSERT_GE(r + a, c);    // if false, elipse is out of circle. no intersection.

    /* calculate intersection of elipse and circle */
    elipse_circle::FuncConstant(a, b, c, r);
    double x = elipse_circle::calc_intersection(a, b, c, r);

    /* test solution range */
    ASSERT_LE(x, a);
    ASSERT_GE(x, -a);

    /* test if the intersection calculated from circle is on the elipse */
    // calculate y of solution with circle function
    double ysq = r*r - std::pow(x + c, 2.);
    ASSERT_GE(ysq, 0.);     // test true value condition
    double y_upper = std::sqrt(ysq);  
    double y_lower = -1. * y_upper; 

    // test if calculated intersection fills the elipse function 
    double elipse_upper = (x * x) / (a * a) + (y_upper * y_upper) / (b * b);
    ASSERT_NEAR(elipse_upper, 1., 1e-6);
    
    // obvious case.....
    double elipse_lower = (x * x) / (a * a) + (y_lower * y_lower) / (b * b);
    ASSERT_NEAR(elipse_lower, 1., 1e-6);
}


int main(int argc, char **argv){
    ::testing::InitGoogleTest(&argc, argv);

    for(int k = 0; k < 10000; ++k){
        RUN_ALL_TESTS();
    }

    return 0;
}

