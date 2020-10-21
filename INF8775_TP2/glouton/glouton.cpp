// Your First C++ Program
#include <iostream>
#include "vector"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
namespace py = pybind11;

struct Bloc
{
    Bloc(int h, int l, int p): h(h), l(l), p(p) {}
    Bloc(): h(0), l(0), p(0) {}
    void setH(int h_) {h = h_; }
    void setL(int l_) {l = l_; }
    void setP(int p_) {p = p_; }

    int getH() { return h; }
    int getL() { return l; }
    int getP() { return p; }
    int getArea() { return h*l;}
    int h, l, p;
};


PYBIND11_MODULE(Glouton, m) {

    py::class_<Bloc>(m, "Bloc")
            .def(py::init<int, int, int>())
            .def("setH", &Bloc::setH)
            .def("setL", &Bloc::setL)
            .def("setP", &Bloc::setP)
            .def("getH", &Bloc::getH)
            .def("getL", &Bloc::getL)
            .def("getArea", &Bloc::getArea)
            .def("getP", &Bloc::getP);

//    m.def("closest", &find_closest_distance, "Finds the closest distance between two points in a list");
//    m.def("call_recursive", &call_closest, "Finds the closest distance between two points in a list");
//    m.def("call_brute_force", &callBruteForce, "Taco Bell");
}
