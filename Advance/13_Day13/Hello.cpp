#include <iostream>
#include <string>

class Math
{
public:
    int add(int a, int b)
    {
        std::cout << "this: " << this << "\n";
        return a + b;
    }
private:
    int m_var = 0;    
};


class Crash 
{
public:
    void foo()
    {
        std::cout << "fooo " << this->a << "\n";
        
    }
private:
    int a;
};


int main()
{

    Crash* p = nullptr;
    p->foo(); // Crash::foo(&p)

    // Math* p = new Math;
    // std::cout << "&p: " << p << "\n";
    // p->add(10, 20); // Math::add(&p, 10, 20)

    // Math* p2 = new Math;
    // p2->add(30, 40);

    // delete p;
    // delete p2;

}