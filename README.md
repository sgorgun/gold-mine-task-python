# The Gold Mine Problem

## Purpose
The coding exercise is designed to test your knowledge of the dynamic programming for solving
a certain problem. 

## Overview
You are proposed to realize an approach for solving so called Gold Mine Problem. The gold mine is presented by the matrix of dimensions $n\times m$. Each entry in this matrix contains a positive integer which is the amount of gold. The miner starts at any cell of the first column and must finish his itenerary in the last column. 
The miner can move only right or right down from a cell to the next one. The aim is to find out the maximum amount of gold that he can gather. 

Let's consider a few examples.

### First example

The source matrix of sizes $3\times 3$ is:

|   i/j   |   1 |   2 |   3 |   4 |
|:-------:|:---:|:---:|:---:|:---:|
|  **1**  |   3 |  2  |  1  | 6   |
|  **2**  |   **4** |   1 |  1  |  8  |
|  **3**  |   1 |   **6** |   **2** |  **4**  |

The optimal itenerary is highlighed by bold. The total of these items is equals to 16.

### Second example

The source matrix of sizes $4\times 4$ is: 

|   i/j   |   1 |   2 |   3 |   4 |
|:-------:|:---:|:---:|:---:|:---:|
|  **1**  |   **4** |  **1**  |  **6**  | 1   |
|  **2**  |   4 |   1 |  5  |  **3**  |
|  **3**  |   6 |   5 |   1 |  1  |
|  **4**  |   7 |   1 |  1  |  1  |

One of the optimal itenerary is highlighted by bold. It is not unique. Try to find out another one by yourself.
The target value of any optimal path is equal to 14.

## Modelling exercise
- come up with the optimal substructure of the problem
- select siutable data structure for storing subproblems
- realize an approach for computing the optimal substructure
- find out the subproblem that gives the maximum amount of gold

## Coding exercise

Carry out the following exercise for proving that your ideas are correct and efficient.
Your aim is to implement the following function:

```python
def get_gold_count(mines: list[list[int]]) -> int:
    """
    :param mines: a list of lists of integers. Each entry represents itself the number of gold
    :return: the maximum number of gold which the miner can gather
    """
    pass
```

It is guaranteed that the dimensions of mine matrix are not less than 1.

Please use a template for the implementation `(task/solution.py:get_gold_count)`.
