#include <string>
#include <cmath>
#include <iostream>

std::string get_middle(std::string input) 
{   
    std::string answer = "";
    if (input.size() % 2 == 0) {
        int middle = floor(input.size() / 2);
        std::cout << middle;
        answer = input[middle-1] + input[middle];
    }
    else {
        int middle = floor(input.size() / 2); 
        answer = input[middle];
    }

    return answer;
}

int main ()
{
    std::string test = "test";
    std::cout << get_middle(test) << std::endl;
    return 0;
}