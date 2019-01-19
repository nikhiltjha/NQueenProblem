# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 23:00:24 2018

@author: Nikhil
"""
def initializeBoard(Board,n):
    for key in ["queen","row","column","nw2se","sw2ne"]:
        Board[key]={}
    for i in range(n):
        Board["queen"][i]=-1
        Board["row"][i]=0
        Board["column"][i]=0
    for i in range(-(n-1),n):
        Board["nw2se"][i]=0
    for i in range(0,2*n-1):
        Board["sw2ne"][i]=0

def printBoard(Board):
    for row in sorted(Board["queen"].keys()):
        print((row,Board["queen"][row]),end=" ")
    else:
        print()


def free(i,j,Board):
    return (Board["row"][i]==0 
            and Board["column"][j]==0 
            and Board["nw2se"][j-i]==0
            and Board["sw2ne"][i+j]==0)

def addqueen(i,j,Board):
    Board["queen"][i]=j
    Board["row"][i]=1
    Board["column"][j]=1
    Board["nw2se"][j-i]=1
    Board["sw2ne"][i+j]=1

def undoqueen(i,j,Board):
    Board["queen"][i]=-1
    Board["row"][i]=0
    Board["column"][j]=0
    Board["nw2se"][j-i]=0
    Board["sw2ne"][i+j]=0

def placequeen(i,Board):
    n =len(Board["queen"].keys())
    for j in range(0,n):
        if free(i,j,Board):
            addqueen(i,j,Board)
            if i==n-1:
                return True
            else: 
                extendsolution=placequeen(i+1,Board)
            if extendsolution:
                return True
            else:
                undoqueen(i,j,Board)
    else:
        return False
def solveQueen(Board):
    if placequeen(0,Board):
        printBoard(Board)
    else: print("No Solution")    
    
while 1:
    Board={}
    while True:
        try:
            N=int(input("Enter the value of N to solve for N Queen Problem: \n"))
        except:
            print("Enter the valid input")
        else:
            break
    
    initializeBoard(Board, N)
    solveQueen(Board)
    

    
    
