# error as demo1 is not a fuction object
def demo():
    print("Inside Demo")
    
    def demo1():
        print("Inside Demo1")
    

def main():
    demo.demo1()

if __name__ == "__main__":
    main()