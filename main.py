def total_expenses(file_name: str) -> int:
    """
    Calculate the total expenses
    Args:
        file_name: str
    Returns:
        total_expenses: total expenses
    """
    total_expenses = 0
    with open(file_name, 'r') as f:
        for line in f:
            line_expenses = line.strip().split(',')
            for expense in line_expenses:
                total_expenses += int(expense)
    return total_expenses
print(total_expenses(total_expenses))