def flatten(list1):
    flattenList = []
    #Listemizi döngüye alıp, elemanları bakıyoruz.
    for e in list1:
        #Eğer listenin elemanı, başka bir liste değilse flattenList'imize listemize ekliyoruz.
        if type(e) != type([]):
            flattenList.append(e)
        #Eğer listenin elemanı, başka bir liste ise, bu sefer onu flatten fonksiyonuna sokuyoruz ve 
        # liste olma özelliğini kaybedene kadar bu işlemi yapıyoruz. En sonunda flattenList'imize ekliyoruz.
        else:
            flattenList.extend(flatten(e))
    return flattenList
    

list1 = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
list1=flatten(list1)
print(list1)