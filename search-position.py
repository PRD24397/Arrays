''' https://leetcode.com/problems/search-insert-position/'''
''' 35. Search Insert Position'''

def searchInsertPosition(string,number_to_search):
    for i in range(len(string)):
        if string[i] == number_to_search:
            return i+1
            break
        else:
            pass




string = list(map(int,input().split(' ')))
number_to_search = int(input())
print(searchInsertPosition(string,number_to_search))