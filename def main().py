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
