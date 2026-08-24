# =demo1 function is calling other demo function
def demo():
    print("Inside Demo1")

def demo1():
    print("Inside Demo2")
    demo()

def main():
    demo1()

if __name__ == "__main__":
    main()