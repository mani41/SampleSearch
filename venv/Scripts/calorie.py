def maxCalorieCalculator(n,sortedArr):
    #pass
    calorieSum = 0
    i = 0
    for km in sortedArr:
        p = i
        p = p<<1
        #print(i)
        calorieSum = calorieSum + p + km
        i = i+km
    return calorieSum

if __name__ == "__main__":
    T = int(input())
    # print(T)
    for t in range(T):
        n = int(input())
        # print(n)
        arr = list(map(int, input().split()))
        sortedArr = sorted(arr,reverse = True)
        #print(sortedArr)
        result = maxCalorieCalculator(n, sortedArr)
        print(result)