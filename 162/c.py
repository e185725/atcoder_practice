


import math
def main():
    K = int(input())
    ans = 0
    for a in range(1,K+1):
        for b in range(1,K+1):
            for c in range(1,K+1):
                ans += math.gcd(math.gcd(a,b),c)

    print(ans)

if __name__ == "__main__":
    main()
