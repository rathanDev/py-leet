from decimal import Decimal

expenses: list[Decimal] = []

def add_expenses(amount: str) -> None:
    expenses.append(Decimal(amount))

def get_total() -> Decimal:
    total = Decimal(0)
    for exp in expenses:
        total += exp
    return total
    
if __name__ == "__main__":
    add_expenses("20.50")
    add_expenses("10.25")
    total = get_total()
    print(f"TotalExpenses:{total}")

