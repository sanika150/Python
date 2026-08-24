# created demo1 object for nested function
def demo():
    print("Inside Demo")
    
    def demo1():
        print("Inside Demo1")

    demo1()
    

def main():
    demo()

if __name__ == "__main__":
    main()