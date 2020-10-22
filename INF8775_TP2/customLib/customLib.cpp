// Your First C++ Program
#include <iostream>
#include "vector"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
namespace py = pybind11;
using namespace std;
struct Bloc
{
    Bloc(unsigned long long h, unsigned long long l, unsigned long long p): h(h), l(l), p(p) {}
    Bloc(): h(0), l(0), p(0) {}
    void setH(unsigned long long h_) {h = h_; }
    void setL(unsigned long long l_) {l = l_; }
    void setP(unsigned long long p_) {p = p_; }

    unsigned long long getH() { return h; }
    unsigned long long getL() { return l; }
    unsigned long long getP() { return p; }
    unsigned long long getArea() { return p*l;}
    unsigned long long h, l, p;
};


tuple<vector<Bloc>, int> algo_glouton(vector<Bloc> B) {
    // On assume que la liste est trier
    int hauteur = 0;
    int index = 1; 
    int vect_size = B.size();
    vector<Bloc> solution;
    solution.push_back(B[0]);
    hauteur += B[0].h;
    while(index < vect_size)
    {
        
        if (B[index].p < solution.back().p && B[index].l < solution.back().l) 
        {
            solution.push_back(B[index]);
            hauteur += B[index].h;
        }
        index++;
    }


    return make_tuple(solution, hauteur);
}



PYBIND11_MODULE(CustomLib, m) {

    py::class_<Bloc>(m, "Bloc")
            .def(py::init<unsigned long long, unsigned long long, unsigned long long>())
            .def("setH", &Bloc::setH)
            .def("setL", &Bloc::setL)
            .def("setP", &Bloc::setP)
            .def("getH", &Bloc::getH)
            .def("getL", &Bloc::getL)
            .def("getArea", &Bloc::getArea)
            .def("getP", &Bloc::getP);

      m.def("algo_glouton", &algo_glouton, "Build the tallest!");
//    m.def("call_recursive", &call_closest, "Finds the closest distance between two points in a list");
//    m.def("call_brute_force", &callBruteForce, "Taco Bell");
}
