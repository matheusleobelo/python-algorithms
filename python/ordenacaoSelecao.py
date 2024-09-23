def buscaMenor(arr):
    menor = arr[0]
    menorIndice = 0

    for i in range(1,len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menorIndice = i

    return menorIndice

def ordenacaoSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print (ordenacaoSelecao([5,3,6,2,10]))



# # Finds the smallest value in an array
# def findSmallest(arr):
#   # Stores the smallest value
#   smallest = arr[0]
#   # Stores the index of the smallest value
#   smallest_index = 0
#   for i in range(1, len(arr)):
#     if arr[i] < smallest:
#       smallest_index = i
#       smallest = arr[i]      
#   return smallest_index

# # Sort array
# def selectionSort(arr):
#   newArr = []
#   for i in range(len(arr)):
#       # Finds the smallest element in the array and adds it to the new array
#       smallest = findSmallest(arr)
#       newArr.append(arr.pop(smallest))
#   return newArr

# print(selectionSort([5, 3, 6, 2, 10]))