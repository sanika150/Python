# main function is caaling other 2 functions
def demo():
    print("Inside Demo1")

def demo1():
    print("Inside Demo2")

def main():
    demo()
    demo1()

if __name__ == "__main__":
    main()