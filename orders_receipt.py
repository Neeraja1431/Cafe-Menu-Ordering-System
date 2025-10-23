from datetime import datetime

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

    # save to file
    with open("orders_receipt.txt", "a", encoding="utf-8") as f:
        f.write(receipt_text + "\n\n")
    print("\n✅ Receipt saved to orders_receipt.txt")
