#include <iostream>
int add(int a, int b){
    return a + b;
}
int main(){
    for( int ii=0; ii<10; ++ii ){
        int input1;
        int input2;
        std::cin >> input1>>input2;
        std::cout << add(input1, input2) << std::endl;
        std::cout.flush();
    }
}