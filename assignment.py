def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    :param price: Original price of the item.
    :param discount_percent: Discount percentage to apply.
    :return: Final price after discount if discount is 20% or more, else original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

# Get user input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print the result
print(f"Final price after discount: {final_price:.2f}")
