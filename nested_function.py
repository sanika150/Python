# nested function it will display only inside demo 
#as we declared demo1 but not called the demo1 function
def demo():
    print("Inside Demo")
    
    def demo1():
        print("Inside Demo1")
    

def main():
    demo()

if __name__ == "__main__":
    main()