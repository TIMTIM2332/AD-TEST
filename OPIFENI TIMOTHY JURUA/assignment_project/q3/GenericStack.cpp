#include <iostream>
#include <vector>
#include <string>
using namespace std;

template<typename T>
class Stack {
    vector<T> data;
public:
    void push(const T& val) { data.push_back(val); }
    void pop() { if(!data.empty()) data.pop_back(); }
    T top() const { if(!data.empty()) return data.back(); throw runtime_error("Empty"); }
    bool empty() const { return data.empty(); }
};

int main() {
    Stack<int> s1;
    s1.push(10); s1.push(20);
    cout << "Top int: " << s1.top() << endl;
    s1.pop();
    cout << "Top int after pop: " << s1.top() << endl;

    Stack<string> s2;
    s2.push("hello"); s2.push("world");
    cout << "Top string: " << s2.top() << endl;
    return 0;
}
