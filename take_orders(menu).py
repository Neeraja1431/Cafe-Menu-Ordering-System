def take_orders(menu):
    orders = {}  # item -> quantity
    while True:
        choice = input("Enter item name (or type 'done' to finish): ").strip().lower()
        if choice == "done":
            break
        if choice not in menu:
            print("❌ Item not found. Please choose from the menu.")
            continue
        # quantity input
        qty_input = input(f"How many {choice.title()} do you want? ").strip()
        if not qty_input.isdigit() or int(qty_input) <= 0:
            print("❌ Enter a valid positive number for quantity.")
            continue
        qty = int(qty_input)
        orders[choice] = orders.get(choice, 0) + qty
        print(f"✅ {qty} x {choice.title()} added.")
    return orders
