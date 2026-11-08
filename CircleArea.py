#include<stdio.h>

def Area(Radius):

    Ans = 0
    PI=3.14
    Ans = PI * Radius * Radius;
    return Ans;


def main():


    Value = 0
    Res = 0
    print("Enter the raduis of circle:")
    Value = float(input())

    Res = Area(Value)
    print("Area of circle is :",Res)
    
if __name__ == "__main__":
    main()
