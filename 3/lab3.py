import random
def Sym(A,B):
        size_A = len(A)
        size_B = len(B)
        result = []
        resultWithoutDuplicate = []
        for i in range(size_A):
                j = 0
                while j < size_B and B[j] != A[i]:
                        j+=1
                if(j==size_B):
                        if(A[i] not in result):
                           result.append(A[i])
        for i in range(size_B):
                j = 0
                while j < size_A and A[j] != B[i]:
                        j+=1
                if(j==size_A):
                        if(B[i] not in result):
                           result.append(B[i])
                
        a = set(A)
        b = set(B)
        #print(a^b)
        #print('symDif without:')
        #print(resultWithoutDuplicate)
        return(result)
def MinElem(arr1):
        min = arr1[0]
        for i in arr1:
                if(i<min):
                        min=i
        return(min)
                
def SymDiff(arr1, arr2, maxSize):
    result = [None] * maxSize
    ai = 0
    bi = 0
    count = 0
    while ai < len(arr1) and bi < len(arr2):
            if(arr1[ai] < arr2[bi]):
               if(count < maxSize):
                       result[count]=arr1[ai]
                       #result.append(arr1[ai])
                       count+=1
                       ai+=1
               else:
                  break
            elif(arr1[ai]>arr2[bi]):
                if(count < maxSize):
                        #print(count)
                        result[count] = arr2[bi]
                        #result.append(arr2[bi])
                        count+=1
                        bi+=1
                else:
                  break     
            else:
                    ai+=1
                    bi+=1
    while ai < len(arr1):
            if(count<maxSize):
                    result[count]=arr1[ai]
                    #result.append(arr1[ai])
                    count+=1
                    ai+=1
            else:
               break 
    while bi < len(arr2):
            if(count<maxSize):
                    result[count]=arr2[bi]
                    #result.append(arr2[bi])
                    count+=1
                    bi+=1
            else:
               break 
    print(result)
first = []
second = []
f = 10
s = 20
for i in range(f):
        first.append(random.randint(0, 20))
for i in range(s):
    second.append(random.randint(0, 20))
print('first array:')
print(first)
print('second array:')
print(second)
print('My SymDiff:')
print(Sym(first,second))
print('True SymDiff:')
print(set(first)^set(second))
print('My MinElem:')
print(MinElem(Sym(first,second)))
print('True MinElem:')
print(min(float(s) for s in Sym(first,second)))
