def pathlength(src,des,cost = 0):
    if(src,des) in edges:
        print(str(cost + edgeValue[(src,des)]) + ' ') 
 
    for(i,j) in edges:
        if i == src:
            pathlength(j,des, cost + edgeValue[(i,j)])
            
edges = [('a', 'b'), ('a', 'c'), ('b', 'e'), ('b', 'f'), ('c', 'f'), ('c', 'g'), ('c', 'h'), ('e', 'f'), ('e', 'i'), ('f', 'i')] 
 
edgeValue = {('a', 'b') : 30, ('a', 'c') : 45, ('b', 'e') : 20, ('b', 'f') : 39, 
            ('c', 'f') : 21, ('c', 'g') : 31, ('c', 'h') : 27, ('e', 'f') : 35, 
            ('e', 'i') : 47, ('f', 'i') : 20} 
 
src = str(input('Enter Starting Node: '))
des = str(input('Enter Ending Node: '))
print('The length of path is: ')
pathlength(src, des)
