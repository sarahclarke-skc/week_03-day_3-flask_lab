class Order:
    def __init__(self, customer_name, order_date, book, total_cost):
        self.customer_name = customer_name
        self.order_date = order_date
        self.book = book
        self.total_cost = total_cost

    def pence_to_pounds(self):
        corrected_format = self.total_cost / 100
        return f"{corrected_format:.2f}"