def sortbox(given):
    list1 = list(given)
    list1.sort()
    list1 = ''.join(list1)
    return list1

with open('dictionary.words.txt', 'r') as f:
    dic = []
    list_for_search = []
    for word in f:
        word = word.rstrip('\n')
        dic.append(word)
    dic2 = {sortbox(word2.lower()) : word2 for word2 in dic}
    list_for_search = list(dic2.keys())
    list_for_search.sort()
    
def binary_search(mylist, myitem):
    length = len(mylist)
    if length == 0 or mylist[0] > myitem:
        pass
    else:
        if mylist[(length)//2] == myitem:
            return True
        elif mylist[(length)//2] < myitem:
            return binary_search(mylist[(length)//2 +1:],myitem)
        elif mylist[(length)//2] > myitem:
            return binary_search(mylist[0:((length)//2)],myitem)
    return False

def find_words(given_words):
    if binary_search(list_for_search, sortbox(given_words)) == True:
        return dic2[sortbox(given_words)]
    else:
        print('None')

word3 = input()
print(find_words(word3))
