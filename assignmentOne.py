male = ['siddique','masum','raiyan','rafsan','ebon','shihab']
female = ['laila','raisa']
parent = [
('siddique','masum'),('siddique','laila'),('masum','raiyan'),('raiyan','rafsan'),
('raiyan','ebon'),('raiyan','raisa'),('rafsan','shihab')
]

#Grandparent 

def printgrandparent():
    Y = input('Person:  ')
    print('Grandparent:', end='  ')
    n = len(parent)
    for i in range(n):
        if parent[i][1] == Y:
            for j in range(n):
                if parent[i][0] == parent[j][1]:
                    print(parent[j][0], end='  ')
        i+=1

#Brother 

def printbrother():
    Y = input('Person:  ')
    print('Brother:', end='  ')
    n = len(parent)
    for i in range(n):
        if parent[i][1] == Y:
            for j in range(n):
                if (parent[i][0] == parent[j][0]) and (
                        parent[i][1] != parent[j][1]) and (parent[j][1] in male):
                   print(parent[j][1], end='  ')
        i+=1                   

#Sister 

def printsister():
    Y = input('Person:  ')
    print('Sister:', end='  ')
    n = len(parent)
    for i in range(n):
        if parent[i][1] == Y:
            for j in range(n):
                if (parent[i][0] == parent[j][0]) and (
                        parent[i][1] != parent[j][1]) and (parent[j][1] in female):
                   print(parent[j][1], end='  ')
        i+=1

#Uncle 
def printuncle():
    Y = input('Person:  ')
    print('Uncle:', end='  ')
    n = len(parent)
    for i in range(n):
        if parent[i][1] == Y:
            for j in range(n):
                if parent[i][0] == parent[j][1]:
                    for k in range(n):
                        if (parent[k][0] == parent[j][0]) and ( 
                                parent[k][1] != parent[j][1]) and (parent[k][1] in male):
                            print(parent[k][1], end='  ')
        i+=1
        

#Aunt 

def printaunt():
    Y = input('Person:  ')
    print('Aunt:', end='  ')
    n = len(parent)
    for i in range(n):
        if parent[i][1] == Y:
            for j in range(n):
                if parent[i][0] == parent[j][1]:
                    for k in range(n):
                        if (parent[k][0] == parent[j][0]) and ( 
                                parent[k][1] != parent[j][1]) and (parent[k][1] in female):
                            print(parent[k][1], end='  ')
        i+=1


printgrandparent()
printbrother()
printsister()
printuncle()
printaunt()
