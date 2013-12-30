############################################################################
# Author: Martin SAVESKI
# Date: May 2009
# License: MIT
#
# AI Agent for Connect Four
#
# CON4UTILS.PY
# * Utility functions for printing the board and reading input
############################################################################


#CON4UTILS.PY
#All functions work on reversed table
import re

#represnts the table
def draw(a=[]):
    def tc(a):
        if a==0: return " "
        if a==1: return "X"
        if a==2: return "Y"

    print "\n\n           --------------------------- "
    print "           [%s] [%s] [%s] [%s] [%s] [%s] [%s] "%(tc(a[5][0]),tc(a[5][1]),tc(a[5][2]),tc(a[5][3]),tc(a[5][4]),tc(a[5][5]),tc(a[5][6]))
    print "           [%s] [%s] [%s] [%s] [%s] [%s] [%s] "%(tc(a[4][0]),tc(a[4][1]),tc(a[4][2]),tc(a[4][3]),tc(a[4][4]),tc(a[4][5]),tc(a[4][6]))
    print "           [%s] [%s] [%s] [%s] [%s] [%s] [%s] "%(tc(a[3][0]),tc(a[3][1]),tc(a[3][2]),tc(a[3][3]),tc(a[3][4]),tc(a[3][5]),tc(a[3][6]))
    print "           [%s] [%s] [%s] [%s] [%s] [%s] [%s] "%(tc(a[2][0]),tc(a[2][1]),tc(a[2][2]),tc(a[2][3]),tc(a[2][4]),tc(a[2][5]),tc(a[2][6]))
    print "           [%s] [%s] [%s] [%s] [%s] [%s] [%s] "%(tc(a[1][0]),tc(a[1][1]),tc(a[1][2]),tc(a[1][3]),tc(a[1][4]),tc(a[1][5]),tc(a[1][6]))
    print "           [%s] [%s] [%s] [%s] [%s] [%s] [%s] "%(tc(a[0][0]),tc(a[0][1]),tc(a[0][2]),tc(a[0][3]),tc(a[0][4]),tc(a[0][5]),tc(a[0][6]))
    print "           --------------------------- "
    print "            1   2   3   4   5   6   7    \n\n"

#computes string hash value of the state of the table
def toHash(table):
    out="";
    for j in range(7):
        for i in range(6):
            if table[i][j]==0: break
            else: out+=str(table[i][j])
        out+="|"
    return out


#determines whether there is a winner
def win(intable=[]):
    w1=[1,1,1,1]
    w2=[2,2,2,2]

    #horizontal
    for i in range(6):
        for j in range(4):
            if [intable[i][j],intable[i][j+1],intable[i][j+2],intable[i][j+3]]==w1:
                return 1
            if [intable[i][j],intable[i][j+1],intable[i][j+2],intable[i][j+3]]==w2:
                return 2

    #vertical
    for i in range(7):
        for j in range(3):
            if [intable[j][i], intable[j+1][i], intable[j+2][i], intable[j+3][i]]==w1:
                return 1
            if [intable[j][i], intable[j+1][i], intable[j+2][i], intable[j+3][i]]==w2:
                return 2

    #left to right
    for j in range(3):
        for i in range(4):
            if [intable[j][i], intable[j+1][i+1], intable[j+2][i+2], intable[j+3][i+3]]==w1:
                return 1
            if [intable[j][i], intable[j+1][i+1], intable[j+2][i+2], intable[j+3][i+3]]==w2:
                return 2


    #right to left
    for j in range(3):
        for i in range(6,2,-1):
            if [intable[j][i], intable[j+1][i-1], intable[j+2][i-2], intable[j+3][i-3]]==w1:
                return 1
            if [intable[j][i], intable[j+1][i-1], intable[j+2][i-2], intable[j+3][i-3]]==w2:
                return 2

#simular to validMoves but with None if the move of that col in not valid
def humanMoves(intable=[]):
    cols=[]; rows=[]
    for col in range(7):
        for row in range(6):
            if intable[row][col]==0:
                cols.append(col)
                rows.append(row)
                break
    return cols, rows

isNum=re.compile("[^0-9]")
#human move for a given col
def hmove(intable, x):
    cols, rows = humanMoves(intable)
    if isNum.match(x)==None and x!='': x=int(x)-1
    while x not in cols:
        print "INVALID MOVE!!!"
        x=raw_input('n: ')
        if isNum.match(x)==None and x!='': x=int(x)-1
    intable[rows[cols.index(x)]][x]=2
