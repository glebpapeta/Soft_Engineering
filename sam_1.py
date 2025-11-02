class CoffeeDrink:
    def __init__(self, name, price, size="средний"):
        self.name = name
        self.price = price
        self.size = size
        self.is_available = True

    def display_info(self):
        status = "доступен" if self.is_available else "не доступен"
        print(f"☕ {self.name} - {self.price} руб. ({self.size}) - {status}")

    def apply_discount(self, percent):
        new_price = self.price * (100 - percent) / 100
        print(f"Скидка {percent}%: {self.price} → {new_price:.0f} руб.")
        return new_price


latte = CoffeeDrink("Латте", 250)
espresso = CoffeeDrink("Эспрессо", 150, "маленький")

print("=== КОФЕЙНАЯ КАРТА ===")
latte.display_info()
espresso.display_info()

print("\n=== АКЦИИ ===")
latte.apply_discount(15)
espresso.is_available = False
espresso.display_info()
