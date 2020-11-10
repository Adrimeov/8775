#include "vector"
#include <iostream>
#include <random>
#include <list>
#include <assert.h>

using namespace std;

struct Bloc
{
    Bloc(unsigned long long h, unsigned long long l, unsigned long long p): h(h), l(l), p(p) {}
    Bloc(): h(0), l(0), p(0) {}

    bool operator==(Bloc const& other) {
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
    solution.insert(itr++, candidate);

    default_random_engine generator;
    uniform_int_distribution<int> distribution(7, 10);

    for (; itr != solution.end();) {
        if (itr->getL() < candidate.getL() && itr->getP() < candidate.getP()) {
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

int TabuSearch(list<Bloc> candidates){

    int heuristic_counter = 0;
    list<Bloc> global_solution;
    list<Bloc> local_solution;
    list<Bloc> tabu;

    while (heuristic_counter < 100) {
        heuristic_counter++;
        UpdateTabu(tabu, candidates);

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

        cout << "New height: " << best_height << endl;

        if (CalculateHeight(global_solution) < best_height) {
            global_solution = list<Bloc>(local_solution);
            heuristic_counter = 0;
        }
    }

    return CalculateHeight(global_solution);
}
