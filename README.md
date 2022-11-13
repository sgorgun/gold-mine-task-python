# Elements of dynamical programming

## Purpose

The coding exercise is designed to test knowledge of the following concepts:
* Dynamical Programming
* Optimal substructure

## Overview

The coding exercise covers the following practical problem:
* The Gold Mine Problem

## Coding exercises

### Exercise 1: The Gold mine problem

The Gold Mine Problem could be defined as follows:
* The gold mine is represented by a matrix of dimensions $n\times m$. 
* Each entry in this matrix contains a positive integer which is the amount of gold. 
* The miner starts at any cell of the **first column** and must finish his path in the **last column**. 
* The miner can move only **to the right** or **to the right-and-down** from a cell to the next one. 
* The miner's goal is to collect the maximum amount of gold along the way. 


The first part of the exercise is for you to think on how to approach the Gold Mine Problem (described above) using dynamical programming.

The second part of the exercise is for you to implement the following function that finds the maximal amount of gold that could be gathered

```python
def get_gold_count(mines: List[List[int]]) -> int:
    """Returns the maximal amount of gold that could be gathered by the miner.
    
    The rules for mining:
    * each entry of a given matrix accounts for amount of gold that could be gathered in there
    * the miner starts in the first column and ends his route in the last column
    * there are only two eligible moves for the miner: to the right, to the right-and-down
    
    Args:
        mines: List[List[int]], a given mines configuration with corresponding amounts of gold for each mine
    Returns:
        int, the maximal amount of gold that could be gathered.
    """
    pass

```


**Example 1:**

The source matrix of size $3\times 3$ is:

|   i/j   |   1   |   2   |   3   |   4   |
|:-------:|:-----:|:-----:|:-----:|:-----:|
|  **1**  |   3   |   2   |   1   |   6   |
|  **2**  | **4** |   1   |   1   |   8   |
|  **3**  |   1   | **6** | **2** | **4** |

The optimal itinerary is highlighted by bold. The total amount of gold is 16.

**Example 2:**

The source matrix of size $4\times 4$ is: 

|   i/j   |   1   |   2   |   3   |   4   |
|:-------:|:-----:|:-----:|:-----:|:-----:|
|  **1**  | **4** | **1** | **6** |   1   |
|  **2**  |   4   |   1   |   5   | **3** |
|  **3**  |   6   |   5   |   1   |   1   |
|  **4**  |   7   |   1   |   1   |   1   |

A possible optimal itinerary is highlighted by bold (there are multiple optimal itineraries for this example).
The target value of any optimal path is equal to 14. 

<br>

Please use a template for the implementation `(task/gold_mine.py:get_gold_count)`.
