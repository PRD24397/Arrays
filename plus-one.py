''' https://leetcode.com/problems/plus-one/'''
''' 66. Plus One '''

array = list(map(int,input('Enter the space seperated list of numbers').split(' ')))
array[-1]+=1
print(array)