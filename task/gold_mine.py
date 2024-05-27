from typing import List


def get_maximum_amount_of_gold(mines: List[List[int]]) -> int:
    """Returns the maximum amount of gold that can be gathered by the miner.
    
    The rules for mining:
    * each entry in the matrix accounts for the amount of gold that can be gathered
    * the miner starts in the first column and ends his route in the last column
    * the miner has only two eligible moves: to the right and to the right and down
    
    Args:
        mines: List[List[int]], a given configuration of mines with amounts of gold for each mine
    Returns:
        int, the maximum amount of gold that can be gathered.
    """
    num_rows = len(mines)
    num_cols = len(mines[0])
    goldMatrix = [[0] * num_cols for _ in range(num_rows)]
    
    for row in range(num_rows):
        goldMatrix[row][0] = mines[row][0]
    
    for col in range(1, num_cols):
        for row in range(num_rows):
            if row == 0:
                goldMatrix[row][col] = mines[row][col] + goldMatrix[row][col-1]
            else:
                goldMatrix[row][col] = mines[row][col] + max(goldMatrix[row][col-1], goldMatrix[row-1][col-1])
    
    max_gold = max(goldMatrix[row][num_cols-1] for row in range(num_rows))
    return max_gold
