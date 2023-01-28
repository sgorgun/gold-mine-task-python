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
    pass
