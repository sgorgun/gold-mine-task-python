from typing import List


def get_maximum_amount_of_gold(mines: List[List[int]]) -> int:
    """Returns the maximum amount of gold that could be gathered by the miner.
    
    The rules for mining:
    * each entry of a given matrix accounts for amount of gold that could be gathered in there
    * the miner starts in the first column and ends his route in the last column
    * there are only two eligible moves for the miner: to the right, to the right-and-down
    
    Args:
        mines: List[List[int]], a given mines configuration with corresponding amounts of gold for each mine
    Returns:
        int, the maximum amount of gold that could be gathered.
    """
    pass
