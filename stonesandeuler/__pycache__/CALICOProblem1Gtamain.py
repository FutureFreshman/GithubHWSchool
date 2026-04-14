def solve(E: str, D: int, M: int, Y: int) -> str:
    """

    E: The name of the event
    Y: Year
    M: Month
    D: Day
    """
    eventbefore = True
    if Y < 2026:
            eventbefore = True
    if Y > 2026:
          eventbefore = False
    if Y == 2026:
        if M < 11:
                eventbefore= True
        elif M > 11:
                eventbefore = False
        elif M == 11:
            if D > 19:
                eventbefore = False
            elif D < 19:
                 eventbefore = True       
    if eventbefore == True:
        return "we got " + E + " before gta6"
    elif eventbefore == False:
        return "we got gta6 before " + E

def main():
    T = int(input())
    for _ in range(T):
        E = input()
        temp = input().split()
        Y, M, D = int(temp[0]), int(temp[1]), int(temp[2])
        print(solve(E, D, M, Y))

if __name__ == '__main__':
    main()