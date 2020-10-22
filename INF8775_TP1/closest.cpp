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

void printPoint(Point p)
{
    cout << p.x << endl;
}

int compareX(const void* a, const void* b)
{
    Point *p1 = (Point *)a, *p2 = (Point *)b;
    return (p1->x - p2->x);
}

int compareY(const void* a, const void* b)
{
    Point *p1 = (Point *)a, *p2 = (Point *)b;
    return (p1->y - p2->y);
}

float dist(Point p1, Point p2)
{
    return sqrt((p1.x -p2.x) * (p1.x -p2.x) + (p1.y -p2.y) * (p1.y -p2.y));
}

float bruteForce(Point P[], int n)
{
    float min = FLT_MAX;
    for (int i = 0; i < n; ++i)
        for (int j = i+1; j < n; ++j)
            if (dist(P[i], P[j]) < min)
                min = dist(P[i], P[j]);
            
    return min;
}

float callBruteForce(vector<Point> P, vector<Point> unUsed, int unUsed1, int unUsed2)
{
    Point* p = &P[0];

    return bruteForce(p, P.size());
}



float min(float x, float y)
{
    return (x < y)? x : y;
}

float stripClosest(Point strip[], int size, float d)
{
    float min = d;  // Initialize the minimum distance as d

    // Pick all points one by one and try the next points till the difference
    // between y coordinates is smaller than d.
    // This is a proven fact that this loop runs at most 6 times
    for (int i = 0; i < size; ++i)
        for (int j = i+1; j < size && (strip[j].y - strip[i].y) < min; ++j)
            if (dist(strip[i],strip[j]) < min)
                min = dist(strip[i], strip[j]);

    return min;
}

float closestUtil(Point Px[], Point Py[], int n, int rec)
{
    // If there are 2 or 3 points, then use brute force
    if (n <= rec)
        return bruteForce(Px, n);

    // Find the middle point
    int mid = n/2;
    Point midPoint = Px[mid];


    // Divide points in y sorted array around the vertical line.
    // Assumption: All x coordinates are distinct.
    Point Pyl[mid];   // y sorted points on left of vertical line
    Point Pyr[n-mid];  // y sorted points on right of vertical line
    int li = 0, ri = 0;  // indexes of left and right subarrays
    for (int i = 0; i < n; i++)
    {
        if (Py[i].x <= midPoint.x && li<mid)
            Pyl[li++] = Py[i];
        else
            Pyr[ri++] = Py[i];
    }

    // Consider the vertical line passing through the middle point
    // calculate the smallest distance dl on left of middle point and
    // dr on right side
    float dl = closestUtil(Px, Pyl, mid, rec);
    float dr = closestUtil(Px + mid, Pyr, n-mid, rec);

    // Find the smaller of two distances
    float d = min(dl, dr);

    // Build an array strip[] that contains points close (closer than d)
    // to the line passing through the middle point
    Point strip[n];
    int j = 0;
    for (int i = 0; i < n; i++)
        if (abs(Py[i].x - midPoint.x) < d)
            strip[j] = Py[i], j++;

    // Find the closest points in strip.  Return the minimum of d and closest
    // distance is strip[]
    return stripClosest(strip, j, d);
}

float call_closest(vector<Point> Px, vector<Point> Py, int recursion, int nb_point)
{
    Point* px = &Px[0];
    Point* py = &Py[0];

    return closestUtil(px, py, nb_point, recursion);
}



//float closest(Point P[], int n)
//{
//    Point Px[n];
//    Point Py[n];
//    for (int i = 0; i < n; i++)
//    {
//        Px[i] = P[i];
//        Py[i] = P[i];
//    }
//
//    qsort(Px, n, sizeof(Point), compareX);
//    qsort(Py, n, sizeof(Point), compareY);
//
//    // Use recursive function closestUtil() to find the smallest distance
//    return closestUtil(Px, Py, n);
//}

//float find_closest_distance()
//{
//    Point P[] = {{2, 3}, {12, 30}, {40, 50}, {5, 1}, {12, 10}, {3, 4}};
//    int n = sizeof(P) / sizeof(P[0]);
//    return closest(P, n);
//}

PYBIND11_MODULE(closest, m) {

    py::class_<Point>(m, "Point")
            .def(py::init<int, int>())
            .def("setX", &Point::setX)
            .def("setY", &Point::setY)
            .def("getX", &Point::getX)
            .def("getY", &Point::getY);

//    m.def("closest", &find_closest_distance, "Finds the closest distance between two points in a list");
    m.def("call_recursive", &call_closest, "Finds the closest distance between two points in a list");
    m.def("call_brute_force", &callBruteForce, "Taco Bell");
}
