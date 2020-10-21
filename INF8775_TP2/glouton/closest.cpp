#include <iostream>
#include <cfloat>
#include <cstdlib>
#include <cmath>
#include "vector"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
//#include <pybind11/complex.h>

using namespace std;
namespace py = pybind11;


struct Point
{
    Point(int x, int y): x(x), y(y) {}
    Point(): x(0), y(0) {}
    void setX(int x_) {x = x_; }
    void setY(int y_) {y = y_; }
    int getX() { return x; }
    int getY() { return y; }

    int x, y;
};


PYBIND11_MODULE(closest, m) {

    py::class_<Point>(m, "Point")
            .def(py::init<int, int>())
            .def("setX", &Point::setX)
            .def("setY", &Point::setY)
            .def("getX", &Point::getX)
            .def("getY", &Point::getY);

//    m.def("closest", &find_closest_distance, "Finds the closest distance between two points in a list");
//    m.def("call_recursive", &call_closest, "Finds the closest distance between two points in a list");
//    m.def("call_brute_force", &callBruteForce, "Taco Bell");
}