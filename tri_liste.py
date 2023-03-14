liste = [9,7,6,8,4,3,5,2,1]

def tri_selection(liste):
   for i in range(len(liste)):
       min = i
       for j in range(i+1, len(liste)):
           if liste[min] > liste[j]:
               min = j

       tmp = liste[i]
       liste[i] = liste[min]
       liste[min] = tmp0
   return liste

#################################################################

def tri_insertion(liste):
    for i in range(1, len(liste)):
        k = liste[i]
        j = i-1
        while j >= 0 and k < liste[j] :
                liste[j + 1] = liste[j]
                j -= 1
        liste[j + 1] = k
    return liste

tri_insertion(liste)

#################################################################