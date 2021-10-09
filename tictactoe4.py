import random
import time
time.sleep(1)
print("\t\t\t\tTIC TAC TOE\n")
print(" Read the instructions.\n")
print("\tInstructions:-\n")
print("\t1.You will be given a reference board with numbers on them like given below:-")
print("\n\t\t\t1 | 2 | 3")
print("\t\t\t--+---+--")
print("\t\t\t4 | 5 | 6")
print("\t\t\t--+---+--")
print("\t\t\t7 | 8 | 9\n")
print("\t2.Select the position and enter the corresponding numbers of the position when prompted\n")
print("\t3.That's All! Enjoy The Game.\t")
time.sleep(2)
inp=input("\n\tPress enter to proceed!")
start='y'
while start=='y':
    count=0
    a,b,c,d,e,f,g,h,i=' ',' ',' ',' ',' ',' ',' ',' ',' '
    board={1:a,2:b,3:c,4:d,5:e,6:f,7:g,8:h,9:i}
    sel=input("\n\tSelect X or O\n\t   ")
    sel=sel.upper() 
    try:
        if sel!='X' and sel!='O':
            raise Exception()
    except:
        print("\n\tEnter only X or O")
        sel=input("\n\tSelect X or O\n\t   ")
        sel=sel.upper()           
    turn=[]
    pmem=[]
    cmem=[]
    mark=0
    c_turn=[]
    pmtrx=[]
    tot_turn=[x for x in range(1,10)]
    csel=' '
    print("\tyou are ",sel,'\n')
    if sel=='X':
        csel='O'
        turn=[1,3,5,7,9]        
        print("\t\t  |   |  \t\t\t1 | 2 | 3")
        print("\t\t--+---+--\t\t\t--+---+--")
        print("\t\t  |   |  \t\t\t4 | 5 | 6")
        print("\t\t--+---+--\t\t\t--+---+--")
        print("\t\t  |   |  \t\t\t7 | 8 | 9\n")
    elif sel=='O':
        csel='X'
        turn=[2,4,6,8]    
    for i in range(1,10):
        if i in turn:
            if i!=9:
                p=int(input(f'\t{sel} Should play now. Enter the no. of the position:-\n\t   '))
                try:
                    if p not in tot_turn:
                        raise exception()
                except:
                    print("\n\tEnter the correct position\n")
                    p=int(input("\tEnter the position again:-\n\t   "))            
                pmem.append(p)
                board.update({p:sel})
                tot_turn.remove(p)
            else:
                p=tot_turn[0]
                board.update({p:sel})
                tot_turn.remove(p)                
        else:
            if i==1:
                p=random.choice(tot_turn)
                cmem.append(p)
                board.update({p:csel})
                tot_turn.remove(p)
            elif i==2:
                if  pmem[0]==5:
                    pmtrx=[1,3,7,9]                    
                    p=random.choice(pmtrx)
                    cmem.append(p)
                    board.update({p:csel})
                    tot_turn.remove(p)
                elif pmem[0] in [1,3,7,9]:
                    p=5
                    cmem.append(p)
                    board.update({p:csel})
                    tot_turn.remove(p)
                elif pmem[0] in [2,4,6,8]:
                    if pmem[0]==2:
                        pmtrx=[1,3,5,8]
                        p=random.choice(pmtrx)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif pmem[0]==4:
                        pmtrx=[1,7,5,6]
                        p=random.choice(pmtrx)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif pmem[0]==6:
                        pmtrx=[3,9,4,5]
                        p=random.choice(pmtrx)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif pmem[0]==8:
                        pmtrx=[9,7,5,2]
                        p=random.choice(pmtrx)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)                 
            elif i==3:
                if  pmem[0]==5:
                    pmtrx=[1,3,7,9]                    
                    p=random.choice(pmtrx)
                    if board[p]!=' ':
                        pmtrx.remove(p)
                        p=random.choice(pmtrx)
                    cmem.append(p)
                    board.update({p:csel})
                    tot_turn.remove(p)
                elif pmem[0] in [1,3,7,9] and board[5]==' ':
                    p=5
                    cmem.append(p)
                    board.update({p:csel})
                    tot_turn.remove(p)
                elif pmem[0] in [1,3,7,9] and board[5]!=' ':
                    p=random.choice(tot_turn)                    
                    cmem.append(p)
                    board.update({p:csel})
                    tot_turn.remove(p)
                elif pmem[0] in [2,4,6,8]:
                    if pmem[0]==2:
                        pmtrx=[1,3,5,8]
                        p=random.choice(pmtrx)
                        if board[p]!=' ':
                            pmtrx.remove(p)
                            p=random.choice(pmtrx)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif pmem[0]==4:
                        pmtrx=[1,7,5,6]
                        p=random.choice(pmtrx)
                        if board[p]!=' ':
                            pmtrx.remove(p)
                            p=random.choice(pmtrx)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif pmem[0]==6:
                        pmtrx=[3,9,4,5]
                        p=random.choice(pmtrx)
                        if board[p]!=' ':
                            pmtrx.remove(p)
                            p=random.choice(pmtrx)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif pmem[0]==8:
                        pmtrx=[9,7,5,2]
                        p=random.choice(pmtrx)
                        if board[p]!=' ':
                            pmtrx.remove(p)
                            p=random.choice(pmtrx)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
            elif i==4:
                k=pmem[0]
                l=pmem[1]
                if k==1:                
                    if l==2 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==3 and board[2]==' ':
                        p=2
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==4 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==7 and board[4]==' ':
                        p=4
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==5 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==9 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                elif k==2:                
                    if l==8 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==5 and board[8]==' ':
                        p=8
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==1 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==3 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                elif k==3:                
                    if l==2 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==1 and board[2]==' ':
                        p=2
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==5 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==7 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==6 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==9 and board[6]==' ':
                        p=6
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                elif k==4:                
                    if l==5 and board[6]==' ':
                        p=6
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==6 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==1 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==7 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                elif k==5:                
                    if l==2 and board[8]==' ':
                        p=8
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==8 and board[2]==' ':
                        p=2
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==4 and board[6]==' ':
                        p=6
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==6 and board[4]==' ':
                        p=4
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==1 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==9 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==7 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==3 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                elif k==6:                
                    if l==5 and board[4]==' ':
                        p=4
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==4 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==3 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==9 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                elif k==7:                
                    if l==9 and board[3]==' ':
                        p=8
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==8 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==5 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==3 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==1 and board[4]==' ':
                        p=4
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==4 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                elif k==8:                
                    if l==9 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==7 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==5 and board[2]==' ':
                        p=2
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==2 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                elif k==9:                
                    if l==7 and board[8]==' ':
                        p=8
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==8 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==3 and board[6]==' ':
                        p=6
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==6 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==1 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==5 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
           ##########i=5             
            elif i==5:
                k=pmem[0]
                l=pmem[1]
                if k==1:                
                    if l==2 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==3 and board[2]==' ':
                        p=2
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==4 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==7 and board[4]==' ':
                        p=4
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==5 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==9 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                elif k==2:                
                    if l==8 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==5 and board[8]==' ':
                        p=8
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==1 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==3 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                elif k==3:                
                    if l==2 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==1 and board[2]==' ':
                        p=2
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==5 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==7 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==6 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==9 and board[6]==' ':
                        p=6
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                elif k==4:                
                    if l==5 and board[6]==' ':
                        p=6
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==6 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==1 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==7 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                elif k==5:                
                    if l==2 and board[8]==' ':
                        p=8
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==8 and board[2]==' ':
                        p=2
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==4 and board[6]==' ':
                        p=6
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==6 and board[4]==' ':
                        p=4
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==1 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==9 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==7 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==3 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                elif k==6:                
                    if l==5 and board[4]==' ':
                        p=4
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==4 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==3 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==9 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                elif k==7:                
                    if l==9 and board[8]==' ':
                        p=8
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==8 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==5 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==3 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==1 and board[4]==' ':
                        p=4
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==4 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                elif k==8:                
                    if l==9 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==7 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==5:
                        p=2
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==2 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                elif k==9:                
                    if l==7 and board[8]==' ':
                        p=8
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==8 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==3 and board[6]==' ':
                        p=6
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==6 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==1 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==5 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    else:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
            #####i=6
            elif i==6:
                flag=0
                k=cmem[0]
                l=cmem[1]                
                if k==1:                
                    if l==2 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==3 and board[2]==' ':
                        p=2
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==4 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==7 and board[4]==' ':
                        p=4
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==5 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==9 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1                    
                elif k==2:                
                    if l==8 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==5 and board[8]==' ':
                        p=8
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==1 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==3 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1                    
                elif k==3:                
                    if l==2 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==1 and board[2]==' ':
                        p=2
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==5 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                    elif l==7 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==6 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==9 and board[6]==' ':
                        p=6
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1                    
                elif k==4:                
                    if l==5 and board[6]==' ':
                        p=6
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==6 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==1 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==7 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1                    
                elif k==5:                
                    if l==2 and board[8]==' ':
                        p=8
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==8 and board[2]==' ':
                        p=2
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==4 and board[6]==' ':
                        p=6
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==6 and board[4]==' ':
                        p=4
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==1 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==9 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==7 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==3 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1                    
                elif k==6:                
                    if l==5 and board[4]==' ':
                        p=4
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==4 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==3 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==9 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1                    
                elif k==7:                
                    if l==9 and board[8]==' ':
                        p=8
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==8 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==5 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==3 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==1 and board[4]==' ':
                        p=4
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==4 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1                    
                elif k==8:                
                    if l==9 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==7 and board[9]==' ':
                        p=9
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==5 and board[2]==' ':
                        p=2
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==2 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1                    
                elif k==9:                
                    if l==7 and board[8]==' ':
                        p=8
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==8 and board[7]==' ':
                        p=7
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==3 and board[6]==' ':
                        p=6
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==6 and board[3]==' ':
                        p=3
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==1 and board[5]==' ':
                        p=5
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    elif l==5 and board[1]==' ':
                        p=1
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1                    
                if flag!=1:
                    flag1=0
                    check=1
                    k=pmem[0]
                    m=pmem[1]
                    l=pmem[2]                    
                    while flag1!=1:
                        if check==3:
                            p=random.choice(tot_turn)
                            cmem.append(p)
                            board.update({p:csel})
                            tot_turn.remove(p)
                            flag1=1
                        if check==1:
                            check+=1
                            if k==1:                    
                                if l==2 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[2]==' ':
                                    p=2
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==4 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[4]==' ':
                                    p=4
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==9 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif k==2:                
                                if l==8 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[8]==' ':
                                    p=8
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif k==3:                
                                if l==2 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[2]==' ':
                                    p=2
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==6 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==9 and board[6]==' ':
                                    p=6
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif k==4:                
                                if l==5 and board[6]==' ':
                                    p=6
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==6 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif k==5:                
                                if l==2 and board[8]==' ':
                                    p=8
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==8 and board[2]==' ':
                                    p=2
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==4 and board[6]==' ':
                                    p=6
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==6 and board[4]==' ':
                                    p=4
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==9 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif k==6:                
                                if l==5 and board[4]==' ':
                                    p=4
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==4 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==9 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif k==7:                
                                if l==9 and board[8]==' ':
                                    p=8
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==8 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[4]==' ':
                                    p=4
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==4 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif k==8:                
                                if l==9 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[2]==' ':
                                    p=2
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==2 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif k==9:                
                                if l==7 and board[8]==' ':
                                    p=8
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==8 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[6]==' ':
                                    p=6
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==6 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1                            
                        elif check==2:
                            check+=1
                            if m==1:                    
                                if l==2 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[2]==' ':
                                    p=2
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==4 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[4]==' ':
                                    p=4
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==9 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif m==2:                
                                if l==8 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[8]==' ':
                                    p=8
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif m==3:                
                                if l==2 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[2]==' ':
                                    p=2
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==6 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==9 and board[6]==' ':
                                    p=6
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif m==4:                
                                if l==5 and board[6]==' ':
                                    p=6
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==6 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif m==5:                
                                if l==2 and board[8]==' ':
                                    p=8
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==8 and board[2]==' ':
                                    p=2
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==4 and board[6]==' ':
                                    p=6
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==6 and board[4]==' ':
                                    p=4
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==9 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif m==6:                
                                if l==5 and board[4]==' ':
                                    p=4
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==4 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==9 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif m==7:                
                                if l==9 and board[8]==' ':
                                    p=8
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==8 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[4]==' ':
                                    p=4
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==4 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif m==8:                
                                if l==9 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[2]==' ':
                                    p=2
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==2 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif m==9:                
                                if l==7 and board[8]==' ':
                                    p=8
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==8 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[6]==' ':
                                    p=6
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==6 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1                    
            #######i=7
            elif i==7:
                flag=0
                flag1=0
                check=1
                k=cmem[0]
                m=cmem[1]
                l=cmem[2]                    
                while flag1!=1 and check<=2:
                    if check==1:
                        check+=1
                        if k==1:                    
                            if l==2 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==3 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==4 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==7 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==5 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==9 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                        elif k==2:                
                            if l==8 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==5 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==1 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==3 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                        elif k==3:                
                            if l==2 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==1 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==5 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==7 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==6 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==9 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                        elif k==4:                
                            if l==5 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==6 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==1 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==7 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                        elif k==5:                
                            if l==2 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==8 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==4 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==6 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==1 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==9 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==7 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==3 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                        elif k==6:                
                            if l==5 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==4 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==3 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==9 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                        elif k==7:                
                            if l==9 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==8 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==5 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==3 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==1 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==4 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                        elif k==8:                
                            if l==9 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==7 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==5 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==2 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                        elif k==9:                
                            if l==7 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==8 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==3 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==6 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==1 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==5 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1                            
                    elif check==2:
                        check+=1
                        if m==1:                    
                            if l==2 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==3 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==4 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==7 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==5 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==9 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                        elif m==2:                
                            if l==8 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==5 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==1 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==3 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                        elif m==3:                
                            if l==2 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==1 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==5 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==7 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==6 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==9 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                        elif m==4:                
                            if l==5 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==6 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==1 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==7 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                        elif m==5:                
                            if l==2 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==8 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==4 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==6 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==1 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==9 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==7 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==3 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                        elif m==6:                
                            if l==5 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==4 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==3 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==9 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                        elif m==7:                
                            if l==9 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==8 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==5 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==3 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==1 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==4 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                        elif m==8:                
                            if l==9 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==7 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==5 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==2 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                        elif m==9:                
                            if l==7 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==8 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==3 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==6 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==1 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1
                            elif l==5 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                                flag1=1                    
                if flag!=1:
                    flag1=0
                    check=1
                    k=pmem[0]
                    m=pmem[1]
                    l=pmem[2]                    
                    while flag1!=1:
                        if check==3:
                            p=random.choice(tot_turn)
                            cmem.append(p)
                            board.update({p:csel})
                            tot_turn.remove(p)
                            flag1=1
                        if check==1:
                            check+=1
                            if k==1:                    
                                if l==2 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[2]==' ':
                                    p=2
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==4 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[4]==' ':
                                    p=4
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==9 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif k==2:                
                                if l==8 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[8]==' ':
                                    p=8
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif k==3:                
                                if l==2 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[2]==' ':
                                    p=2
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==6 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==9 and board[6]==' ':
                                    p=6
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif k==4:                
                                if l==5 and board[6]==' ':
                                    p=6
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==6 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif k==5:                
                                if l==2 and board[8]==' ':
                                    p=8
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==8 and board[2]==' ':
                                    p=2
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==4 and board[6]==' ':
                                    p=6
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==6 and board[4]==' ':
                                    p=4
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==9 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif k==6:                
                                if l==5 and board[4]==' ':
                                    p=4
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==4 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==9 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif k==7:                
                                if l==9 and board[8]==' ':
                                    p=8
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==8 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[4]==' ':
                                    p=4
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==4 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif k==8:                
                                if l==9 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[2]==' ':
                                    p=2
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==2 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif k==9:                
                                if l==7 and board[8]==' ':
                                    p=8
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==8 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[6]==' ':
                                    p=6
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==6 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1                            
                        elif check==2:
                            check+=1
                            if m==1:                    
                                if l==2 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[2]==' ':
                                    p=2
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==4 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag=1
                                elif l==7 and board[4]==' ':
                                    p=4
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==9 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif m==2:                
                                if l==8 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[8]==' ':
                                    p=8
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif m==3:                
                                if l==2 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[2]==' ':
                                    p=2
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==6 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==9 and board[6]==' ':
                                    p=6
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif m==4:                
                                if l==5 and board[6]==' ':
                                    p=6
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==6 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif m==5:                
                                if l==2 and board[8]==' ':
                                    p=8
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==8 and board[2]==' ':
                                    p=2
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==4 and board[6]==' ':
                                    p=6
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==6 and board[4]==' ':
                                    p=4
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag=1
                                elif l==1 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==9 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif m==6:                
                                if l==5 and board[4]==' ':
                                    p=4
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==4 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==9 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif m==7:                
                                if l==9 and board[8]==' ':
                                    p=8
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==8 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[4]==' ':
                                    p=4
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==4 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif m==8:                
                                if l==9 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==7 and board[9]==' ':
                                    p=9
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[2]==' ':
                                    p=2
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==2 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                            elif m==9:                
                                if l==7 and board[8]==' ':
                                    p=8
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==8 and board[7]==' ':
                                    p=7
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==3 and board[6]==' ':
                                    p=6
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==6 and board[3]==' ':
                                    p=3
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==1 and board[5]==' ':
                                    p=5
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
                                elif l==5 and board[1]==' ':
                                    p=1
                                    cmem.append(p)
                                    board.update({p:csel})
                                    tot_turn.remove(p)
                                    flag1=1
            elif i==8:
                flag=0
                check=1
                k=pmem[0]
                m=pmem[1]
                n=pmem[2]
                l=pmem[3]
                while flag!=1:
                    if check==4:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    if check==1:
                        if k==1:                    
                            if l==2 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif k==2:                
                            if l==8 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif k==3:                
                            if l==2 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif k==4:                
                            if l==5 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif k==5:                
                            if l==2 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif k==6:                
                            if l==5 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif k==7:                
                            if l==9 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                            elif l==1 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif k==8:                
                            if l==9 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==2 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif k==9:                
                            if l==7 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        check+=1
                    elif check==2:
                        if m==1:                    
                            if l==2 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif m==2:                
                            if l==8 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif m==3:                
                            if l==2 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif m==4:                
                            if l==5 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif m==5:                
                            if l==2 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif m==6:                
                            if l==5 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif m==7:                
                            if l==9 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                            elif l==1 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif m==8:                
                            if l==9 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==2 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif m==9:                
                            if l==7 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        check+=1
                    elif check==3:
                        if n==1:                    
                            if l==2 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif n==2:                
                            if l==8 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif n==3:                
                            if l==2 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif n==4:                
                            if l==5 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif n==5:                
                            if l==2 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif n==6:                
                            if l==5 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif n==7:                
                            if l==9 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                            elif l==1 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif n==8:                
                            if l==9 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==2 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif n==9:                
                            if l==7 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        check+=1
                        
                mark=1
                val=[]
                for key,value in board.items():
                    val.append(value)
                time.sleep(1)
                print("\n\t\t\t\t\t   Game Controls:-") 
                print("\n\t\t",val[0],"|",val[1],"|",val[2],"\t\t\t1 | 2 | 3")
                print("\t\t --+---+--\t\t\t--+---+--")
                print("\t\t",val[3],"|",val[4],"|",val[5],"\t\t\t4 | 5 | 6")
                print("\t\t --+---+--\t\t\t--+---+--")
                print("\t\t",val[6],"|",val[7],"|",val[8],"\t\t\t7 | 8 | 9\n")
                if board[7]==board[8]==board[9]==sel or board[7]==board[4]==board[1]==sel or board[4]==board[5]==board[6]==sel or board[8]==board[5]==board[2]==sel or board[9]==board[6]==board[3]==sel or board[1]==board[2]==board[3]==sel or board[1]==board[5]==board[9]==sel or board[7]==board[5]==board[3]==sel:
                    time.sleep(1)
                    print(f"\t{sel} Player Wins the match")
                    break
                elif board[7]==board[8]==board[9]==csel or board[7]==board[4]==board[1]==csel or board[4]==board[5]==board[6]==csel or board[8]==board[5]==board[2]==csel or board[9]==board[6]==board[3]==csel or board[1]==board[2]==board[3]==csel or board[1]==board[5]==board[9]==csel or board[7]==board[5]==board[3]==csel:
                    time.sleep(1)
                    print(f"\t{csel} Computer Wins the match")
                    break
                continue
            elif i==9 and mark==0:
                flag=0
                check=1
                k=cmem[0]
                m=cmem[1]
                n=cmem[2]
                l=cmem[3]
                while flag!=1:
                    if check==4:
                        p=random.choice(tot_turn)
                        cmem.append(p)
                        board.update({p:csel})
                        tot_turn.remove(p)
                        flag=1
                    if check==1:
                        if k==1:                    
                            if l==2 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif k==2:                
                            if l==8 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif k==3:                
                            if l==2 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif k==4:                
                            if l==5 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif k==5:                
                            if l==2 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif k==6:                
                            if l==5 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif k==7:                
                            if l==9 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                            elif l==1 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif k==8:                
                            if l==9 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==2 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif k==9:                
                            if l==7 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        check+=1
                    elif check==2:
                        if m==1:                    
                            if l==2 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif m==2:                
                            if l==8 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif m==3:                
                            if l==2 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif m==4:                
                            if l==5 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif m==5:                
                            if l==2 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif m==6:                
                            if l==5 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif m==7:                
                            if l==9 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                            elif l==1 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif m==8:                
                            if l==9 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==2 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif m==9:                
                            if l==7 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        check+=1
                    elif check==3:
                        if n==1:                    
                            if l==2 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif n==2:                
                            if l==8 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif n==3:                
                            if l==2 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif n==4:                
                            if l==5 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif n==5:                
                            if l==2 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif n==6:                
                            if l==5 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==9 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif n==7:                
                            if l==9 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                            elif l==1 and board[4]==' ':
                                p=4
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==4 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif n==8:                
                            if l==9 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==7 and board[9]==' ':
                                p=9
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[2]==' ':
                                p=2
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==2 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        elif n==9:                
                            if l==7 and board[8]==' ':
                                p=8
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==8 and board[7]==' ':
                                p=7
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==3 and board[6]==' ':
                                p=6
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==6 and board[3]==' ':
                                p=3
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==1 and board[5]==' ':
                                p=5
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                            elif l==5 and board[1]==' ':
                                p=1
                                cmem.append(p)
                                board.update({p:csel})
                                tot_turn.remove(p)
                                flag=1
                        check+=1
                if board[7]==board[8]==board[9]==sel or board[7]==board[4]==board[1]==sel or board[4]==board[5]==board[6]==sel or board[8]==board[5]==board[2]==sel or board[9]==board[6]==board[3]==sel or board[1]==board[2]==board[3]==sel or board[1]==board[5]==board[9]==sel or board[7]==board[5]==board[3]==sel:
                    time.sleep(1)
                    print(f"\t{sel} Player Wins the match")
                    break
                elif board[7]==board[8]==board[9]==csel or board[7]==board[4]==board[1]==csel or board[4]==board[5]==board[6]==csel or board[8]==board[5]==board[2]==csel or board[9]==board[6]==board[3]==csel or board[1]==board[2]==board[3]==csel or board[1]==board[5]==board[9]==csel or board[7]==board[5]==board[3]==csel:
                    time.sleep(1)
                    print(f"\t{csel} Computer Wins the match")
                    break                
                mark=1
        val=[]
        for key,value in board.items():
            val.append(value)
        time.sleep(1)
        print("\n\t\t\t\t\t   Game Controls:-") 
        print("\n\t\t",val[0],"|",val[1],"|",val[2],"\t\t\t1 | 2 | 3")
        print("\t\t --+---+--\t\t\t--+---+--")
        print("\t\t",val[3],"|",val[4],"|",val[5],"\t\t\t4 | 5 | 6")
        print("\t\t --+---+--\t\t\t--+---+--")
        print("\t\t",val[6],"|",val[7],"|",val[8],"\t\t\t7 | 8 | 9\n")
        if mark==1:
            time.sleep(1)
            print("\tIt's a draw")
            break
        if i>=5 and (board[7]==board[8]==board[9]==sel or board[7]==board[4]==board[1]==sel or board[4]==board[5]==board[6]==sel or board[8]==board[5]==board[2]==sel or board[9]==board[6]==board[3]==sel or board[1]==board[2]==board[3]==sel or board[1]==board[5]==board[9]==sel or board[7]==board[5]==board[3]==sel):
            time.sleep(1)
            print(f"\t{sel} Player Wins the match")
            break
        elif i>=5 and (board[7]==board[8]==board[9]==csel or board[7]==board[4]==board[1]==csel or board[4]==board[5]==board[6]==csel or board[8]==board[5]==board[2]==csel or board[9]==board[6]==board[3]==csel or board[1]==board[2]==board[3]==csel or board[1]==board[5]==board[9]==csel or board[7]==board[5]==board[3]==csel):
            time.sleep(1)
            print(f"\t{csel} Computer Wins the match")
            break
    start=input("\n\tDo you want to play again?(y/n)\n\t   ")
    start=start.lower()
    try:
        if start!='y' and start!='n':
            raise exception()
    except:
        start=input("\tDo you want to play again?(y/n)\n\t   ")
        start=start.lower()
print("_______________________________________________________________________________________")
print("\tSelf Exiting in:-")
facts=['**Code Written by sk**','fun fact: An early variation of tic-tac-toe was played in the Roman Empire','fun fact: Tic-tac-toe, played perfectly, will always end in a draw','fun fact: Children as young as 3 years of age can play this game','fun fact: Tic-tac-toe is one of the first games to be played by children']
for i in range(5,0,-1):
    p=random.choice(facts)
    facts.remove(p)
    print(f"\t{i}: {p} ")
    time.sleep(2)
            
                
                
                    
                
                    
                        
                    
                        
                
                
                
                
                    
                    
                    
                    
                
                        
                
                
            
