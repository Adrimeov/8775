// Your First C++ Program
#include <iostream>
#include "vector"
#include <list>
#include <random>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;
using namespace std;

struct Bloc
{
    Bloc(unsigned long long h, unsigned long long l, unsigned long long p): h(h), l(l), p(p) {}
    Bloc(): h(0), l(0), p(0) {}

    bool operator==(Bloc const& other) const {
        bool equal = true;

        if (h != other.h) equal = false;
        if (l != other.l) equal = false;
        if (p != other.p) equal = false;

        return equal;
    }

    void setH(unsigned long long h_) {h = h_; }
    void setL(unsigned long long l_) {l = l_; }
    void setP(unsigned long long p_) {p = p_; }
    void setCounter(int c) {counter = c; }

    unsigned long long getH() { return h; }
    unsigned long long getL() { return l; }
    unsigned long long getP() { return p; }
    unsigned long long getArea() { return p*l;}
//    int getCounter() {return counter;}

    unsigned long long h, l, p;
    int counter = 0;
};


tuple<int, vector<Bloc>> algo_glouton(vector<Bloc> B) {
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

    return make_tuple(hauteur, solution);
}

tuple<int, list<Bloc>> algo_dynamic(vector<Bloc> B)
{
    int number_of_bloc = B.size();
    int max_stack_height[number_of_bloc];
    vector<int> retrace_array (number_of_bloc, -1);


    for( int i = 0; i < number_of_bloc; i++)
    {
        max_stack_height[i] = B[i].getH();
    }

    for (int i = 1; i < number_of_bloc; i++ ) 
        for (int j = 0; j < i; j++ )
            if ( B[i].getL() < B[j].getL() && B[i].getP() < B[j].getP() && max_stack_height[i] < max_stack_height[j] + B[i].getH()) 
            { 
                max_stack_height[i] = max_stack_height[j] + B[i].getH();
                retrace_array[i] = j;
            }

    int max = -1;
    int retrace_index = -1;

    for ( int i = 0; i < number_of_bloc; i++ ) 
        if ( max < max_stack_height[i] )
        {
            max = max_stack_height[i];
            retrace_index = i;
        }

    list<Bloc> solution;

    while (retrace_index != -1) {
        solution.push_front(B[retrace_index]);
        retrace_index = retrace_array[retrace_index];
    }

   return make_tuple(max, solution);
}

void UpdateTabu(list<Bloc> &tabu_list, list<Bloc> &candidates) {
    for (auto itr = tabu_list.begin(); itr != tabu_list.end();){
        itr->setCounter(itr->counter - 1);

        if (itr->counter < 1) {
            candidates.push_back(*itr);
            itr = tabu_list.erase(itr);
        } else ++itr;
    }
}


int FindPositionFromTop(list<Bloc> solution, Bloc candidate) {
    int position = solution.size();

    if (position == 0) return 0;

    for (auto itr = solution.rbegin(); itr != solution.rend(); itr++, position--){
        if (itr->getL() > candidate.getL() && itr->getP() > candidate.getP())
            return position;

        if (position == 1 && itr->getL() < candidate.getL() && itr->getP() < candidate.getP())
            return 0;
    }

    return -1;
}

unsigned long long CalculatePotentialHeight(list<Bloc> solution, Bloc candidate, int insertPosition) {
    unsigned long long height = candidate.getH();
    int position = 0;

    for (auto itr = solution.begin(); itr != solution.end(); itr++, position++) {
        if (position < insertPosition || (itr->getL() < candidate.getL() && itr->getP() < candidate.getP()))
            height += itr->getH();
    }

    return height;
}

void InsertCandidate(list<Bloc> &solution, list<Bloc> &tabu, Bloc candidate, int insertPosition) {
    auto itr = solution.begin();
    advance(itr, insertPosition);
    solution.insert(itr, candidate);

    default_random_engine generator;
    uniform_int_distribution<int> distribution(7, 10);

    for (; itr != solution.end();) {
        if (itr->getL() >= candidate.getL() || itr->getP() >= candidate.getP()) {
            itr->setCounter(distribution(generator));
            tabu.push_back(*itr);
            itr = solution.erase(itr);
        } else itr++;
    }
}

unsigned long long CalculateHeight(list<Bloc> solution) {
    unsigned long long height = 0;

    for (auto itr : solution) height += itr.getH();

    return height;
}

tuple<int, list<Bloc>> TabuSearch(list<Bloc> candidates){

    int heuristic_counter = 0;
    list<Bloc> global_solution;
    list<Bloc> local_solution;
    list<Bloc> tabu;

    while (heuristic_counter < 100) {
        heuristic_counter++;
        UpdateTabu(tabu, candidates);

        if (candidates.empty()) {
            heuristic_counter++;
            continue;
        }

        unsigned long long best_height = 0;
        Bloc best_candidate;
        int best_candidate_position = -1;

        for (auto candidate : candidates) {
            int insert_position = FindPositionFromTop(local_solution, candidate);

            if (insert_position == -1) continue;

            unsigned long long potential_height = CalculatePotentialHeight(local_solution, candidate, insert_position);

            if (potential_height > best_height) {
                best_height = potential_height;
                best_candidate = candidate;
                best_candidate_position = insert_position;
            }
//            TODO: struct pour solution afin d'eviter literation pour le calul de hauteur
        }

        InsertCandidate(local_solution, tabu, best_candidate, best_candidate_position);
        candidates.remove(best_candidate);


        if (CalculateHeight(global_solution) < best_height) {
            global_solution = list<Bloc>(local_solution);
            heuristic_counter = 0;
        }
    }

    return make_tuple(CalculateHeight(global_solution), global_solution);
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

      m.def("algo_glouton", &algo_glouton, "Build the tallest bloc tower with naive algo.");
      m.def("algo_dynamic", &algo_dynamic, "Build the tallest bloc tower with dynamic algo.");
      m.def("algo_tabu", &TabuSearch, "Build the tallest bloc tower with tabu search.");

}

//c++ -shared -fPIC -Wl,-undefined,dynamic_lookup -std=c++11 -fPIC python3.8 -m pybind11 --includes customLib.cpp -o CustomLibpython3.8-config --extension-suffix