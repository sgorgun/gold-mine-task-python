# The Gold Mine Problem

## Purpose
The coding exercise is designed to test your knowledge of the dynamic programming for solving
a certain problem. 

## Overview
You are proposed to realize an approach for solving so-called Gold Mine Problem. The gold mine is presented by the
matrix of dimensions $n\times m$. Each entry in this matrix contains a positive integer which is the amount of gold. 
The miner starts at any cell of the first column and must finish his path in the last column. 
The miner can move only right or right down from a cell to the next one. The aim is to find out 
the maximum amount of gold that can be gathered. 


## Modelling exercise
- come up with the optimal substructure of the problem
- select suitable data structure for storing sub-problems
- realize an approach for computing the optimal substructure
- find out the sub-problem that gives the maximum amount of gold

## Coding exercise

Carry out the following exercise to prove that your ideas proposed in modelling exercise 
are correct and efficient. Your aim is to implement the following function that
must return the maximum number of gold that can be gathered by the miner.

```python
def get_gold_count(mines: list[list[int]]) -> int:
    """
    :param mines: a list of lists of integers. Each entry represents the number of gold
    :return: the maximum number of gold which the miner can gather
    """
    pass
```



It is guaranteed that the dimensions of mine matrix are not less than 1.

Please use a template for the implementation `(task/solution.py:get_gold_count)`.
