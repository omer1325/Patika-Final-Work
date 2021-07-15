def reverseList(list1):
    #Listeyi ters çeviriyoruz.
    list1.reverse()
    #Listeyi döngüye alıp tek tek elemanlarına bakıyoruz.
    for item in list1:
        #Eğer listenin elemanları içinde başka bir liste varsa, bu listeyi de ters çeviriyoruz.
        if type(item) == type([]):
            item.reverse()
    return list1
        
        
list1 = [[1, 2], [3, 4], [5, 6, 7]]
print(reverseList(list1))



