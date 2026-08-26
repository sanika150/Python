# variable no of args
#used when no of arg is not fixed
#all value store under tuple
def demo(*No):
    ans=0
    for i in No:
        ans = ans + i
    return ans
    
    

def main():
    print(demo(10,20,30))

if __name__ == "__main__":
    main()