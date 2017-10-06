#!python3

#This function finds perfect numbers
def perfect(n):
    divsum = 0
    for i in range(1, n):
        if n % i == 0:
            divsum = divsum + i
    if divsum == n:
        return True
    else:
        return False

#This function searches for perfect numbers in a range
def main():
    print("Enter the lower bound.")
    lowBound = int(input())
    print("Enter the upper bound.")
    upBound = int(input())
    for num in range(lowBound, upBound+1):
        if perfect(num) == True:
            print(num)



if __name__ == '__main__':
    main()
