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

int algo_dynamic(vector<Bloc> B) 
{
    int number_of_bloc = B.size();
    int max_stack_height[number_of_bloc];

    for( int i = 0; i < number_of_bloc; i++)
    {
        max_stack_height[i] = B[i].getH();
    }
    for (int i = 1; i < number_of_bloc; i++ ) 
        for (int j = 0; j < i; j++ ) 
            if ( B[i].getL() < B[j].getL() && B[i].getP() < B[j].getP() && max_stack_height[i] < max_stack_height[j] + B[i].getH()) 
            { 
                max_stack_height[i] = max_stack_height[j] + B[i].getH(); 
            } 
    int max = -1; 
    for ( int i = 0; i < number_of_bloc; i++ ) 
      if ( max < max_stack_height[i] ) 
         max = max_stack_height[i]; 
  
   return max;
}

// int main() 
// {
//     vector<Bloc> arr = {Bloc(10, 12, 32), {32, 10, 12}, Bloc(4, 6, 7), Bloc(4, 5, 6), Bloc(6, 4, 5), Bloc(1, 2, 3), Bloc(3, 1, 2)};
//     int a = algo_dynamic(arr);
//     cout<<a<<endl;

// }



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

      m.def("algo_glouton", &algo_glouton, "Build the tallest bloc tower with naive algo.");
      m.def("algo_dynamic", &algo_dynamic, "Build the tallest bloc tower with dynamic algo.");

}
