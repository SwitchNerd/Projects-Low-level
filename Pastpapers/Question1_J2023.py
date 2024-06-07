#Declare Animals:ARRAY[1:10] OF STRING

Animals = ['horse', 'lion', 'rabbit', 'mouse', 'bird', 'deer', 'whale', 'elephant', 'kangaroo', 'tiger']

def SortDescending(Animals):
    #Declare ArrayLength : Integer
    #Declare Temp : String
    ArrayLength = len(Animals)
    for x in range(0,ArrayLength-1):
        for y in range(0,ArrayLength-x-1):
            if Animals[y][0:1] < Animals[y+1][0:1]:
                Temp = Animals[y]
                Animals[y] = Animals[y+1]
                Animals[y+1] = Temp

SortDescending(Animals)
for i in Animals:
    print(i)