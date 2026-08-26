# Default argument(default value is  assigned to  parameter names)
#if value is not provided then it will use default,it must be placed after required arg
def demo(Name,Age=11):
    print("Name is :",Name)
    print("Age is :",Age)
    
    

def main():
    
    
    demo("ABC")

if __name__ == "__main__":
    main()