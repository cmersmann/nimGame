#!/usr/bin/env python
# coding: utf-8

# In[1]:

import py_compile
py_compile.compile('nim_compile.py')


def setup():
    p=select_pile_num()
    s_list=select_stones_loop(p)
    print("Success! Here is the starting board.")
    display_board(s_list)
    return s_list


# In[2]:


def select_pile_num():
    p_str=input("Choose a number of piles 1-10:")
    try:
        p=int(p_str)
    except ValueError:
        print("Could not convert data to an integer. Please enter a number 1-10: ")
        p=select_pile_num()
    else:
        if p>10 or p<1:
            print("Error: number must be between 1 and 10.")
            p=select_pile_num()
    return p


# In[3]:


def select_stones_loop(p):
    s_list=[0]*p
    for i in range(p):
        si=select_stones(i)
        s_list[i]=si
    return s_list
    
        
    


# In[4]:


def select_stones(i):
    ask_str="Choose a number of stones (1-10) for pile "+str(i+1)+": "
    si_str=input(ask_str)
    try:
        s=int(si_str)
    except ValueError:
        print("Could not convert data to an integer. Please enter a number 1-10: ")
    if s>10 or s<1:
        print("Error. The number of stones in each pile must be between 1 and 10")
        select_stones(i)
        
    return s


# In[5]:


def display_board(s_list):
    for i in range(len(s_list)):
        line_display(i,s_list[i])
        
def line_display(j,i):
    if i==0:
        print_str=" "
    elif i%2==0:
        print_str="o "*(i-1)+"o"
    else:
        print_str="o "*(i-1)+"o "
  
    sub=round(len(print_str)/2)
    pad_str=" "*(20-sub)
    if j!=9:
        start_str="Pile  "+str(j+1)+":"
        print(start_str,pad_str,print_str)
    else:
        start_str="Pile "+str(j+1)+":"
        print(start_str,pad_str,print_str)


# In[6]:


def first_turn():
    ans=input("Who goes first--you or the computer? Enter 1 for you and 2 for the computer.")
    try:
        ft=int(ans)
    except ValueError:
        print("Error: You didn't enter a number.")
        ft=first_turn()
    else:
        if ft!=1 and ft!=2:
            print("Error: You didn't enter 1 or 2.")
            ft=first_turn()
    return ft    


# In[7]:


from time import *

def choose_pile(n):
    ans=input("From what pile would you like to remove stones? ")
    try:
        pile_no=int(ans)
    except ValueError:
        print("Error: You didn't enter a number.")
        pile_no=choose_pile(n)
    else:
        if pile_no>n or pile_no<=0:
            print("Error: There is no such pile.")
            pile_no=choose_pile(n)
    return(pile_no)

def choose_stones(n):
    ans=input("How many stones would you like to remove? Choose a number between 1 and "+str(n)+": ")
    try:
        stone_no=int(ans)
    except ValueError:
        print("Error: You didn't enter a number.")
        stone_no=choose_stones(n)
    else:
        if stone_no>n or stone_no<=0:
            print("Error: That choice is not possible.")
            stone_no=choose_stones(n)
    return(stone_no)

def user_turn(s_list):
    n=len(s_list)
    pile_no=choose_pile(n)
    stone_no=choose_stones(s_list[pile_no-1])
    s_list[pile_no-1]=s_list[pile_no-1]-stone_no
    if stone_no!=1:
        print("You chose to remove",stone_no,"stones from pile",pile_no              ,". Here is the new board.")
    else: 
        print("You chose to remove ",stone_no," stone from pile ",pile_no              ,". Here is the new board.")
    display_board(s_list)
    return s_list
        


# In[8]:


from math import *
from random import *
def binary(num):
    if num==0:
        bin_list=[0]
    elif num==1:
        bin_list=[1]
    else:
        sig_dig=int(log(num)/log(2))
        bin_list=[0]*(sig_dig+1)
        bin_list[sig_dig]=1
        while num%(2**sig_dig)!=0:
            num=num-2**sig_dig
            sig_dig=int(log(num)/log(2))
            bin_list[sig_dig]=1
    return bin_list

def maximum(s_list):
    m_ax=s_list[0]
    for s in s_list:
        if s>m_ax:
            m_ax=s
    return m_ax

def binary_list(s_list):
    m_ax=maximum(s_list)
    binary_m=[0]*len(s_list)
    m=int(log(m_ax)/log(2))+1
    for i in range(len(s_list)):
        sig_bin=binary(s_list[i])
        num_pad=m-len(sig_bin)
        sig_bin.extend([0]*num_pad)
        binary_m[i]=sig_bin
        
    return binary_m

def nim_sum(s_list):
    bin_m=binary_list(s_list)
    bit_sum=[0]*len(bin_m[0])
    nim_sum=[0]*len(bin_m[0])
    for j in range(len(bin_m[0])):
        for i in range(len(s_list)):  
            bit_sum[j]+=bin_m[i][j]
    for i in range(len(bit_sum)):
        nim_sum[i]=bit_sum[i]%2
    return nim_sum

def leave_amount(a,b):
    xor=[0]*len(a)
    leave=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            xor[i]=1
    for i in range(len(xor)):
        leave+=xor[i]*2**i
    return leave

def signif_digit(nim_sum):
    idx=0
    for i in range(len(nim_sum)):
        if nim_sum[i]==1:
            idx=i
    return idx

def find_pile(idx, s_list, bin_m):
    pile_opts=[]
    for i in range(len(s_list)):
        if bin_m[i][idx]==1:
            pile_opts.append(i)
    return pile_opts

def find_rand_pile(s_list):
    pile_opts=[]
    for i in range(len(s_list)):
        if s_list[i]!=0:
            pile_opts.append(i)
    pile_idx_idx=randint(0,len(pile_opts)-1)
    pile_idx=pile_opts[pile_idx_idx]
    return pile_idx

def computer_turn(s_list):
    for i in range(3):
        sleep(.3)
        print("\n")
    bin_m=binary_list(s_list)
    n_s=nim_sum(s_list)
    if all(n==0 for n in n_s):
        pile_idx=find_rand_pile(s_list)
        rem_k=randint(1,s_list[pile_idx])
        yk=s_list[pile_idx]-rem_k
    else:
        idx=signif_digit(n_s)
    
        pile_options=find_pile(idx,s_list,bin_m)
        
        if len(pile_options)>1:
            pile_idx=randint(0,len(pile_options)-1)
        else: pile_idx=pile_options[0]
       
        yk=leave_amount(bin_m[pile_idx],n_s)
        rem_k=s_list[pile_idx]-yk
    
    print("The computer elects to remove",rem_k,"stones from pile", pile_idx+1,".")
    print("Here is the new board.")
    s_list[pile_idx]=yk
    display_board(s_list)
    return s_list


# In[9]:


def win_check(player_id,s_list):
    sum_c=0
    for s in s_list:
        sum_c+=s
    if sum_c==0:
        if player_id==1:
            print("\n","Congratulations--you won!")
        else:
            print("The computer won!")
        return 1
    else:
        return 0
    
def player_turn(p_id,s_list):
    if p_id==1:
        s_list=user_turn(s_list)
    else:
        s_list=computer_turn(s_list)
    return s_list    
        
def play_nim():
    s_list=setup()
    win_cond=0
    a=first_turn()
    while win_cond==0:
        s_list=player_turn(a,s_list)
        win_cond=win_check(a,s_list)
        if win_cond==1:
                    print("Do you want to play again?")
                    play_again=input("Enter 'y' or 'n'.")
                    if play_again=='y':
                        play_nim()
                    else:
                        print("Enjoy your day!")
        else:
            if a==1:
                a=2
            elif a==2:
                a=1


# In[ ]:


play_nim()


# In[ ]:




