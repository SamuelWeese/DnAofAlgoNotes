def AltEuclid(n, m):
    a = max(n,m)
    b = min(n,m)
    print(a, b)
    if (b == 0):
        return(a)
    else:
        AltEuclid(a-b,b)

def AltAltEuclid(n, m):
    a = max(n,m)
    b = min(n,m)
    if ()

AltEuclid(10,10000)
# Yes, this algorithm always will return GCD since either a-b =
# Reason clear, formula is equivalant to n%m, or euclid's
/*
function BinarySearch (L[0:n – 1],X)
Input: L[0:n – 1] (a sorted array of n list elements)
X (a search item)
Output: returns the index of an occurrence of X in the list, or -1 if X is not in the list
Found ← .false.
low ← 0
high ← n – 1
while .not. Found .and. low ≤ high do
mid ← 􏰀(low + high)/2􏰁
if X = L[mid] then Found ← .true. else if X < L[mid] then
high ← mid – 1 else
low ← mid + 1 endif
endif endwhile
if Found then return(mid)
else return(-1)*/
endif
end BinarySearch

def binarySearch(aList, x):
    low = 0
    high = len(aList) -1
    found = False
    while (not Found) and low <= high:
        mid = floor((low+high)/2)
        if (X == aList[mid]):
            found = True
        else if (x < Lmid):
            high = mid - 1
        else:
            low = mid + 1
    if Found:
        return(mid)
    else:
        return(-1)

def altBinarySearch(aList, x):
    low = 0
    high = len(aList) -1
    found = False
    while (not Found) and low <= high:
        mid = floor((low+high*3)/4)
        if (X == aList[mid]):
            found = True
        else if (x < Lmid):
            high = mid - 1
        else:
            low = mid + 1
    if Found:
        return(mid)
    else:
        return(-1)
