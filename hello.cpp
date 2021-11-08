#include <iostream>
#include <vector>
int add(int a, int b){
    return a + b;
}
int main(){
    for( int ii=0; ii<10; ++ii ){
        int input1;
        int input2;
        std::vector<int> c;
        std::cin >> input1>>input2;
        int result = add(input1, input2);
        c.push_back(result);
        std::cout << c[0] << std::endl;
        std::cout.flush();
    }
}