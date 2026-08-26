# Keyword argument(arg pass using parameter names)
#order does not matter
def demo(Name,Age):
    print("Name is :",Name)
    print("Age is :",Age)
    
    

def main():
    
    
    demo(Name = "ABC",Age = 11)

if __name__ == "__main__":
    main()