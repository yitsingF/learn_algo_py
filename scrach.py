# -*- coding: utf-8 -*-
def int2roman(num):
   roman_mapper = {
       '1':I
   }

def num_islands(mat):
    if not mat:
        return 0
    m,n = len(mat),len(mat[0])
    cnt = 0

    for row in range(m):
        for col in range(n):
            if mat[row][col] == 1:
                check_connection(mat,row,col,m,n)
                cnt += 1
    return cnt


def check_connection(mat,row,col):
    s = [[row,col]]
    while len(s) >0:
        cur = s.pop()
        neibs = [[cur[0]+x,cur[1]+y] for x in [-1,1] for y in [-1,1]]
        for nerb in nerbs:
            if 0<nerb[0]<m and 0<nerb[1]<n:
                if mat[nerb[0]][nerb[1]] == 1:
                    s.append(nerb)
                    mat[nerb[0]][nerb[1]] = "#"

