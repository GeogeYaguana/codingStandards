"""
Este módulo define una clase Item para representar un artículo
y una clase ShoppinCart para gestionar un carrito de compras.
Incluye funciones para calcular subtotales, aplicar descuentos
y calcular el total final.
"""

class Item:
    """
    Clase que representa un artículo en el carrito de compras.

    Atributos:
        name (str): El nombre del artículo.
        price (float): El precio unitario del artículo.
        qty (int): La cantidad del artículo.
        category (str): La categoría del artículo, por defecto 'general'.
        env_fee (float): Cualquier tasa ambiental asociada al artículo, por defecto 0.
    """
    def __init__(self, name, price, qty, category="general"):
        """
        Inicializa un nuevo objeto Item con nombre, precio, cantidad y categoría.
        
        Args:
            name (str): El nombre del producto.
            price (float): El precio del producto.
            qty (int): La cantidad de productos.
            category (str): La categoría del producto.
        """
        self.name = name
        self.price = price
        self.qty = qty
        self.category = category
        self.env_fee = 0

        if self.category == "electronics":
            self.env_fee = 5  # Tarifa ambiental de $5 por artículo

    def get_total(self):
        """
        Calcula el total del costo del item, incluyendo la tarifa ambiental si aplica.
        
        Returns:
            float: El costo total del item basado en el precio, cantidad y tarifa ambiental.
        """
        total_price = (self.price * self.qty) + (self.env_fee * self.qty)
        return total_price

    def get_most_prices(self):
        """
        Calcula el costo con un descuento del 40%.
        
        Returns:
            float: El costo con el descuento aplicado.
        """
        return self.price * self.qty * 0.6


class ShoppinCart:
    """
    Clase que representa un carrito de compras.

    Atributos:
        items (list): Lista de objetos Item añadidos al carrito.
        tax_rate (float): Tasa de impuestos a aplicar.
        member_discount (float): Descuento de miembro.
        big_spender_discount (float): Descuento por grandes compras.
        coupon_discount (float): Descuento de cupón.
        currency (str): Moneda usada, por defecto "USD".
    """
    def __init__(self):
        """
        Inicializa un nuevo carrito de compras con la tasa de impuestos,
        descuentos y moneda predeterminada.
        """
        self.items = []
        self.tax_rate = 0.08
        self.member_discount = 0.05
        self.big_spender_discount = 10
        self.coupon_discount = 0.15
        self.currency = "USD"

    def add_item(self, item):
        """
        Añade un nuevo ítem al carrito de compras.

        Args:
            item (Item): El objeto item a añadir al carrito.
        """
        self.items.append(item)

    def calculate_subtotal(self):
        """
        Calcula el subtotal de todos los ítems en el carrito.
        
        Returns:
            float: El subtotal de los ítems.
        """
        subtotal = 0
        for item in self.items:
            subtotal += item.get_total()
        return subtotal

    def apply_discounts(self, subtotal, is_member):
        """
        Aplica descuentos al subtotal basado en la membresía y el total.

        Args:
            subtotal (float): El subtotal antes de los descuentos.
            is_member (bool): Si el usuario es miembro para aplicar el descuento.
        
        Returns:
            float: El subtotal después de aplicar los descuentos.
        """
        if is_member:
            subtotal -= subtotal * self.member_discount
        if subtotal > 100:
            subtotal -= self.big_spender_discount
        return subtotal

    def calculate_total(self, is_member, has_coupon):
        """
        Calcula el total después de aplicar impuestos y descuentos.

        Args:
            is_member (bool): Si el usuario es miembro para aplicar el descuento.
            has_coupon (bool): Si el usuario tiene un cupón para aplicar.

        Returns:
            float: El total final incluyendo impuestos y descuentos.
        """
        subtotal = self.calculate_subtotal()
        subtotal = self.apply_discounts(subtotal, is_member)
        total = subtotal + (subtotal * self.tax_rate)
        if has_coupon:
            total -= total * self.coupon_discount
        return total


def main():
    """
    Función principal que simula el proceso de añadir ítems al carrito y 
    calcular el total de la compra.
    """
    cart = ShoppinCart()
    item1 = Item("Apple", 1.5, 10)
    item2 = Item("Banana", 0.5, 5)
    item3 = Item("Laptop", 1000, 1, category="electronics")

    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)

    is_member = True
    has_coupon = True

    total = cart.calculate_total(is_member, has_coupon)

    if total < 0:
        print("Error in calculation!")
    else:
        print("The total price is: $" + str(round(total, 2)))


if __name__ == "__main__":
    main()
