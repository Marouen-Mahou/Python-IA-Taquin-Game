import itertools

class taquin :
  def __init__(self,table):
    self.table=table
    self.g = 0
    
  def h1(self):
    correct = [[0,1,2],[3,4,5],[6,7,8]]
    h = 0;
    for i in range(len(self.table)):
        for j in range(len(self.table)):
            if self.table[i][j] != 0 and self.table[i][j] != correct[i][j]:
                h = h+1
    return h

  def h2(self):
    correct = {
      0: (0,0),
      1: (0,1),
      2: (0,2),
      3: (1,0),
      4: (1,1),
      5: (1,2),
      6: (2,0),
      7: (2,1),
      8: (2,2),
    }
    
    h = 0;
    for i in range(len(self.table)):
        for j in range(len(self.table)):
           if self.table[i][j] != 0:
            ic, jc = correct[self.table[i][j]]
            h = h + abs(i-ic) + abs(j-jc)
            
    return h
      
  
  def display(self):
    #for  i,j in itertools.product(range(len(self.table)),range(len(self.table))) :
     # print(i,j) 
     for i in range(len(self.table)):
       print()
       print("----------")
       for j in range(len(self.table)) : 
         print("|",self.table[i][j],end='')
  
  def isfinal (self) : 
        flist = []
        result = True
       
        for i in range (len(self.table)):
	         flist.extend(self.table[i]);

        return flist == [0,1,2,3,4,5,6,7,8]
      
  def actions(self) :
    moves=[];
    for i,j in itertools.product(range(len(self.table)),range(len(self.table))) :
        if(self.table[i][j]==0) :
            break
    if(j!=(len(self.table)-1)) :
      moves.append([(i,j),(i,j+1)])
    if(i!=(len(self.table)-1)):
      moves.append([(i,j),(i+1,j)])    
    if(i!=0) :
      moves.append([(i,j),(i-1,j)])
    if(j!=0) :
      moves.append([(i,j),(i,j-1)])
    
    
    return moves


  def copy(self):
        table = []
        for row in self.table:
            table.append([x for x in row])
        return taquin(table)
 
  def move(self,pos) :
        

        copy = self.copy()
        i, j = pos[0]
        r, c = pos[1]
        copy.table[i][j], copy.table[r][c] = copy.table[r][c], copy.table[i][j]
        
        copy.g = copy.g + 1
        return copy
    
def common_data(list1, list2):
    result = False
  
    # traverse in the 1st list
    for x in list1:
  
        # traverse in the 2nd list
        for y in list2:
    
            # if one common
            if x == y:
                result = True
                return result 
                  
    return result


def DFS(taquin, o, c):
    o = [taquin]
    
    while(len(o) != 0):
        if(taquin.isfinal() == True) :
                taquin.display()
                
                print('\n found solution \n \n')
                print("Taille Open: ",len(o),"Taille Closed: ",len(c))
                return

        while taquin.table in c:
            o.pop(0)
            taquin = o[0]
        
        c.append(taquin.table)
        
        
        actions = taquin.actions()
        
        o.pop(0)
        
        for i in range(len(actions)):
            nexttaquin = taquin.move(actions[i])
            
            if common_data([nexttaquin.table], c) == False:
                o.insert(0,nexttaquin)

        taquin = o[0]
        
    print("-- Pas de solution --")
    return
    
def BFS(taquin, o, c):
    o = [taquin]
    
    while(len(o) != 0):
        if(taquin.isfinal() == True) :
               
                taquin.display()
                
                print('\n found solution \n \n')
                print("Taille Open: ",len(o),"Taille Closed: ",len(c))
                return

        while taquin.table in c:
            o.pop(0)
            taquin = o[0]
        
        c.append(taquin.table)
        
        
        actions = taquin.actions()
        
        o.pop(0)
        
        for i in range(len(actions)):
            nexttaquin = taquin.move(actions[i])
            
            if common_data([nexttaquin.table], c) == False:
                o.append(nexttaquin)

        taquin = o[0]
    
    
def DFSIt(taquin, o, c, vc, nmax, p, pmax):

    if p == pmax:
       print("profondeur", p)
       print('pas de solution')
       return
    else:
        
        while(len(o) and len(c) < nmax):
            
            taquin = o[0]
            if(taquin.isfinal() == True) :
                    taquin.display()
                    
                    print('\n found solution \n \n')
                    print("Taille Open: ",len(o),"Taille Closed: ",len(c))
                    return
            
            c.append(taquin.table)
            
            actions = taquin.actions()
            
            o.pop(0)
            
            if taquin.table not in vc:
                vc.append(taquin.table)
                for i in range(len(actions)):
                    nexttaquin = taquin.move(actions[i])
                    if common_data([nexttaquin.table], c) == False:
                        nmax = nmax + 1
            else:
                
                for i in range(len(actions)):
                    nexttaquin = taquin.move(actions[i])
                    if common_data([nexttaquin.table], c) == False:
                        o.insert(0,nexttaquin)
            
        
        DFSIt(taquin, [taquin], [], vc, nmax, p + 1, pmax)
        
        
def Astar1(taquin, o, c):
    o = [taquin]
    
    while(len(o) != 0):
        if(taquin.isfinal() == True) :
               
                taquin.display()
                
                print('\n found solution \n \n')
                print("Taille Open: ",len(o),"Taille Closed: ",len(c))
                return

        while taquin.table in c:
            o.pop(0)
            taquin = o[0]
        
        c.append(taquin.table)
        
        
        actions = taquin.actions()
        
        o.pop(0)
        
        for i in range(len(actions)):
            nexttaquin = taquin.move(actions[i])
            
            if common_data([nexttaquin.table], c) == False:
                o.append(nexttaquin)

        indmin = 0
        for i in range(1,len(o)):
            if((o[i].h1() + o[i].g) < (o[indmin].h1() + o[indmin].g)):
                indmin = i
        taquin = o[indmin]
        
def Astar2(taquin, o, c):
    o = [taquin]
    
    while(len(o) != 0):
        if(taquin.isfinal() == True) :
               
                taquin.display()
                
                print('\n found solution \n \n')
                print("Taille Open: ",len(o),"Taille Closed: ",len(c))
                return

        while taquin.table in c:
            o.pop(0)
            taquin = o[0]
        
        c.append(taquin.table)
        
        
        actions = taquin.actions()
        
        o.pop(0)
        
        for i in range(len(actions)):
            nexttaquin = taquin.move(actions[i])
            
            if common_data([nexttaquin.table], c) == False:
                o.append(nexttaquin)

        indmin = 0
        for i in range(1,len(o)):
            if((o[i].h2() + o[i].g) < (o[indmin].h2() + o[indmin].g)):
                indmin = i
        taquin = o[indmin]
        
    

#______MAIN_______#
#obj=taquin([[3,0,1],[6,4,2],[7,8,5]])
#obj=taquin([[3,1,2],[4,5,0],[6,7,8]])
#obj=taquin([[7,2,4],[5,0,6],[8,3,1]])
obj=taquin([[5,4,2],[7,0,6],[8,3,1]])
print("\n////////////////")
print('\n Starting taquin :')
obj.display()
print('\n\n')

print('Choose algorithme : \n'
      '1- DFS  \n'
      '2- BFS \n' 
      '3- DFS Iteratif \n' 
      '4- A* h1 (Bad placed) \n'
      '5- A* h2 (Sum of moves) \n'
      )

print('==> ')
inp = input()
print('\n')


if inp == '1':
    print("WITH DFS \n\n")
    DFS(obj,[obj],[])

if inp == '2':
    print("WITH BFS \n\n")
    BFS(obj,[obj],[])

if inp == '3':
    print("WITH DFSIt \n\n")
    DFSIt(obj, [obj], [], [], 1, 0, 10)
    
if inp == '4':
    print("WITH Astar h1\n\n")
    Astar1(obj,[obj],[])
    
if inp == '5':
    print("WITH Astar h2 \n\n")
    Astar2(obj,[obj],[])
    
