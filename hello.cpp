#include <iostream>
#include <vector>
#include <fstream>
#include <string>
int add(int a, int b){
    return a + b;
}
int main(){
    for( int ii=0; ii<10; ++ii ){
        int i;
        int input1;
        int input2;
        std::vector<int> c;
        std::cin >>i >> input1>>input2;
        int result = add(input1, input2);
        c.push_back(result);
        std::ofstream myfile;
        std::string name = "example" + std::to_string(i) +".txt";
        myfile.open (name);
        myfile << "output: "<<result<<"\n";
        myfile.close();
        std::cout << c[0] << std::endl;
        std::cout.flush();
        //return 0;
    }
}