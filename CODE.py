def insertionSort(array):
     for i in range(len(array)):
          curr =i
          while curr>0:
               if array[curr[0]]<array[curr-1[0]]:
                    buffer = array[curr]
                    array[curr] = array[curr-1]
                    array[cur-1]=buffer
                    curr = curr-1
               else:
                    break
     return
