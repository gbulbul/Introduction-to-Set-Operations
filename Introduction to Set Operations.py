# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 08:27:58 2024

@author: gbulb
"""
class set_of_functions:
    
    def A_U_B(A,B):
        A_U_B_list=[]
        for i, idx in enumerate(A):
            for j, idy in enumerate(B):
                if idx!=idy and idx not in A_U_B_list:
                   A_U_B_list.append(idx)
                elif idx!=idy and idy not in A_U_B_list:
                   A_U_B_list.append(idy)
                elif idx==idy and idx not in A_U_B_list:
                   A_U_B_list.append(idx)
        return set(A_U_B_list)


    def A_B_intersection(A,B):
        A_B_list=[]
        for i, idx in enumerate(A):
            for j, idy in enumerate(B):
                if idx==idy and idx not in A_B_list:
                   A_B_list.append(idx)
        return set(A_B_list)


    def A_difference_B(A,B):
        A_B_list=[]
        for i, idx in enumerate(A):
            for j, idy in enumerate(B):
                if idx!=idy and idx not in A_B_list and idx not in B:
                   A_B_list.append(idx)
        return set(A_B_list)




    def B_difference_A(A,B):
        A_B_list=[]
        for i, idx in enumerate(A):
            for j, idy in enumerate(B):
                if idx!=idy and idy not in A_B_list and idy not in A:
                   A_B_list.append(idy)
        return set(A_B_list)



    def A_complement(full_set,A):
        A_B_list=[]
        for i, idx in enumerate(full_set):
            for j, idy in enumerate(A):
                if idx!=idy and idx not in A_B_list and idx not in A:
                   A_B_list.append(idx)
        return set(A_B_list)


    def B_complement(full_set,B):
        A_B_list=[]
        for i, idx in enumerate(full_set):
            for j, idy in enumerate(B):
                if idx!=idy and idx not in A_B_list and idx not in B:
                   A_B_list.append(idx)
        return set(A_B_list)

if __name__ == "__main__": 
    n=10
    full_set=[i for i in range(1,n+1,1)]
    A=[1, 2, 3, 4, 5]
    B=[2, 8, 5, 10]
    print(set_of_functions.A_U_B(A,B))
    print(set_of_functions.A_difference_B(A,B))
    print(set_of_functions.B_difference_A(A,B))
    print(set_of_functions.A_complement(full_set,A))
    print(set_of_functions.B_complement(full_set,B))