class PaymentProcessor:
    def __init__(self):
        self.total_amount = 0.0

    def add_items(self, items):
        """Add items to calculate the total payment amount."""
        self.total_amount = sum(items)

    def display_total(self):
        print(f"Total Amount to Pay: ${self.total_amount:.2f}")

    def process_payment(self):
        """Simulate payment process."""
        if self.total_amount <= 0:
            print("No items to pay for. Please add items to your cart.")
            return

        print("\nPayment Options:")
        print("1. Credit Card")
        print("2. Debit Card")
        print("3. Mobile Payment")

        try:
            option = int(input("Choose a payment method (1/2/3): "))
            if option not in [1, 2, 3]:
                raise ValueError("Invalid option. Please select 1, 2, or 3.")

            print("\nProcessing your payment...")
            # Simulate processing delay
            import time
            time.sleep(2)

            print("Payment successful! Thank you for your purchase.")
        except ValueError as e:
            print(f"Error: {e}")

# Example Usage
if __name__ == "__main__":
    print("Welcome to the Payment System\n")
    items = []
    while True:
        try:
            item_price = input("Enter the price of an item (or type 'done' to finish): ")
            if item_price.lower() == 'done':
                break
            items.append(float(item_price))
        except ValueError:
            print("Please enter a valid price.")

    payment_processor = PaymentProcessor()
    payment_processor.add_items(items)
    payment_processor.display_total()
    payment_processor.process_payment()
