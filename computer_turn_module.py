#!/usr/bin/env python
# coding: utf-8

# In[1]:
from time import *
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
        sleep(0.5)
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
            pile_idx_idx=randint(0,len(pile_options)-1)
            pile_idx=pile_options[pile_idx_idx]
        else: pile_idx=pile_options[0]
            
        yk=leave_amount(bin_m[pile_idx],n_s)
        rem_k=s_list[pile_idx]-yk
        s_list[pile_idx]=yk
    
    return rem_k,pile_idx,s_list



# In[ ]:




