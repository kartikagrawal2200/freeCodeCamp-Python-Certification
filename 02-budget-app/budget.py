class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name[:30]:*^30}"
        rows = []
        for item in self.ledger:
            desc = f"{item['description'][:23]:<23}"
            amt = f"{item['amount']:>7.2f}"
            rows.append(f"{desc}{amt}")
        total = f"Total: {self.get_balance():.2f}"
        return "\n".join([title, *rows, total])


def create_spend_chart(categories):
    res = "Percentage spent by category\n"

    # Calculate spending (withdrawals only)
    withdrawals = []
    for cat in categories:
        spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        withdrawals.append(spent)

    total_spent = sum(withdrawals)

    # Calculate percentages rounded down to nearest 10
    if total_spent == 0:
        percentages = [0 for _ in categories]
    else:
        percentages = [int((spent / total_spent) * 100) // 10 * 10 for spent in withdrawals]

    # Build y-axis and bars (100 down to 0)
    for level in range(100, -1, -10):
        res += f"{level:>3}| "
        for pct in percentages:
            res += "o  " if pct >= level else "   "
        res += "\n"

    # Horizontal divider line (3 dashes per category + 2 extra spaces)
    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical category names
    max_len = max((len(cat.name) for cat in categories), default=0)
    for i in range(max_len):
        res += "     "
        for cat in categories:
            ch = cat.name[i] if i < len(cat.name) else " "
            res += f"{ch}  "
        res += "\n"

    return res.rstrip("\n")
