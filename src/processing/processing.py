from typing import List, Dict
from datetime import datetime

def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Filters a list of dictionaries by the specified state.

    Args:
        data (List[Dict]): List of transactions.
        state (str, optional): The state to filter by. Defaults to "EXECUTED".

    Returns:
        List[Dict]: Filtered list of transactions.
    """
    if not isinstance(data, list):
        raise ValueError("The 'data' argument must be a list of dictionaries.")
    return [item for item in data if isinstance(item, dict) and item.get("state") == state]

def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Sorts a list of dictionaries by date.

    Args:
        data (List[Dict]): List of transactions.
        descending (bool, optional): Whether to sort in descending order. Defaults to True.

    Returns:
        List[Dict]: Sorted list of transactions.
    """
    if not isinstance(data, list):
        raise ValueError("The 'data' argument must be a list of dictionaries.")
    try:
        return sorted(
            data,
            key=lambda x: datetime.fromisoformat(x.get("date", "")) if "date" in x else datetime.min,
            reverse=descending,
        )
    except ValueError:
        raise ValueError("Ensure all 'date' fields are in ISO 8601 format.")
