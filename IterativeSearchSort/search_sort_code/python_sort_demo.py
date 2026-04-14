def inPlaceSorting():
    a = [5, 2, 3, 1, 4]
    a.sort()
    print(a) #[1, 2, 3, 4, 5]

    a.sort(reverse=True)
    print(a) #[5, 4, 3, 2, 1]

def newSortedList():
    a = [5, 2, 3, 1, 4]
    b = sorted(a)
    print(b) #[1, 2, 3, 4, 5]
    print(a) #[5, 2, 3, 1, 4]

    b = sorted(a, reverse=True)
    print(b) #[5, 4, 3, 2, 1]

def customKey():
    words =["apple", "grapes", "bananas", "pear"]
    words.sort(key=lambda word:word[1])
    print(words)
    print(sorted(words, key = lambda word:len(word)))

if __name__ == "__main__":

    print("Sorting in-place")
    inPlaceSorting()

    print("Returning a new sorted list")
    newSortedList()

    print("Custom sorting key")
    customKey()
