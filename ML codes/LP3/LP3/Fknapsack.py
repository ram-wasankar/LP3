#DAA exp3: Write a program to solve a fractional Knapsack problem using a greedy method.		

class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

    # Define a function to calculate profit/weight ratio
    def ratio(self):
        return self.profit / self.weight


def fractionalKnapsack(capacity, items):
    # Sort items by ratio (profit per weight) in descending order
    items.sort(key=Item.ratio, reverse=True)

    totalValue = 0.0

    for item in items:
        if capacity >= item.weight:
            totalValue += item.profit
            capacity -= item.weight
        else:
            totalValue += item.profit * (capacity / item.weight)
            break

    return totalValue


# ---- Main Program ----
if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    items = []

    for i in range(n):
        profit = int(input(f"Enter profit of item {i + 1}: "))
        weight = int(input(f"Enter weight of item {i + 1}: "))
        items.append(Item(profit, weight))

    capacity = int(input("Enter capacity of knapsack: "))

    print("Maximum value in knapsack:", fractionalKnapsack(capacity, items))



