# cafe_order.py
from datetime import datetime

menu = {
    "coffee": 50,
    "tea": 30,
    "sandwich": 80,
    "burger": 120,
    "pasta": 150,
    "cake": 90
}

def show_menu(menu):
    print("\n💖 Welcome to Neeru's Café 💖")
    print("------ MENU ------")
    for item, price in menu.items():
        print(f"{item.title():15} : ₹{price}")
    print("------------------\n")

def take_orders(menu):
    orders = {}  # item -> quantity
    while True:
        choice = input("Enter item name (or type 'done' to finish): ").strip().lower()
        if choice == "done":
            break
        if choice not in menu:
            print("❌ Item not found. Please choose from the menu.")
            continue
        qty_input = input(f"How many {choice.title()} do you want? ").strip()
        if not qty_input.isdigit() or int(qty_input) <= 0:
            print("❌ Enter a valid positive number for quantity.")
            continue
        qty = int(qty_input)
        orders[choice] = orders.get(choice, 0) + qty
        print(f"✅ {qty} x {choice.title()} added.")
    return orders

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

def print_and_save_receipt(orders, menu, bill):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []
    lines.append("Neeru's Café - Receipt")
    lines.append(f"Date: {now}")
    lines.append("------------------------------")
    for item, qty in orders.items():
        lines.append(f"{item.title():15} x {qty:2}  = ₹{menu[item]*qty}")
    lines.append("------------------------------")
    lines.append(f"Subtotal : ₹{bill['subtotal']}")
    lines.append(f"Discount : -₹{bill['discount']}")
    lines.append(f"Tax      : +₹{bill['tax']}")
    lines.append(f"Total    : ₹{bill['total']}")
    lines.append("\nThank you for visiting Neeru's Café! ☕💖")

    receipt_text = "\n".join(lines)
    print("\n" + receipt_text)

    with open("orders_receipt.txt", "a", encoding="utf-8") as f:
        f.write(receipt_text + "\n\n")
    print("\n✅ Receipt saved to orders_receipt.txt")

def main():
    show_menu(menu)
    orders = take_orders(menu)
    if not orders:
        print("You didn't order anything. Come back soon!")
        return
    bill = calculate_bill(orders, menu)
    print_and_save_receipt(orders, menu, bill)

if __name__ == "__main__":
    main()
