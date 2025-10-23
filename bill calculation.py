def calculate_bill(orders, menu, discount_threshold=500, discount_percent=10, tax_percent=5):
    subtotal = sum(menu[item] * qty for item, qty in orders.items())
    discount = 0
    if subtotal >= discount_threshold:
        discount = (discount_percent / 100) * subtotal
    taxed_amount = (tax_percent / 100) * (subtotal - discount)
    total = subtotal - discount + taxed_amount
    return {
        "subtotal": subtotal,
        "discount": round(discount, 2),
        "tax": round(taxed_amount, 2),
        "total": round(total, 2)
    }
