def show_menu(menu):
    print("\n💖 Welcome to Neeru's Café 💖")
    print("------ MENU ------")
    for item, price in menu.items():
        print(f"{item.title():15} : ₹{price}")
    print("------------------\n")
