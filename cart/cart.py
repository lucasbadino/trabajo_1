class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            self.session["cart"] = {}
            self.cart = self.session["cart"]
        else:
            self.cart = cart

    def add(self, product):
        if product.category == 2:
            id = str(product.id)
            if id not in self.cart.keys():
                self.cart[id]={
                    "product_id": product.id,
                    "name": product.name,
                    "amount": product.price,
                    "price": product.price,
                    "description": product.description,
                    "quantity": 1,
                    "stock": int(product.stock),
                    "image": product.image.url,
                }
            else:
                self.cart[id]["quantity"] += 1
                self.cart[id]["amount"] += product.price
            self.save_cart()
        elif product.category == 3:
            id = str(product.id)
            if id not in self.cart.keys():
                self.cart[id] = {
                    "product_id": product.id,
                    "name": product.name,
                    "amount": product.price,
                    "quantity": 1,
                    "image": product.image.url,
                }
            else:
                self.cart[id]["quantity"] += 1
                self.cart[id]["amount"] += product.price
            self.save_cart()
        elif product.category == 1:
            id = str(product.id)
            if id not in self.cart.keys():
                self.cart[id] = {
                    "product_id": product.id,
                    "name": product.name,
                    "amount": product.price,
                    "quantity": 1,
                    "image": product.image.url,
                }
            else:
                self.cart[id]["quantity"] += 1
                self.cart[id]["amount"] += product.price
            self.save_cart()
        
    def save_cart(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    
    def delete(self, product):
        if product.category== 2:
            id = str(product.id)
            if id in self.cart:
                del self.cart[id]
                self.save_cart()

        elif product.category == 3:
            id = str(product.id)
            if id in self.cart:
                del self.cart[id]
                self.save_cart()

        elif product.category == 1:
            id = str(product.id)
            if id in self.cart:
                del self.cart[id]
                self.save_cart()
    
    def subtract(self, product):
        if product.category == 2:
            id = str(product.id)
            if id in self.cart.keys():
                self.cart[id]["quantity"] -=1
                self.cart[id]["amount"] -= product.price
                if self.cart[id]["quantity"] <= 0: self.delete(product)
                self.save_cart()
        
        elif product.category == 3:
            id = str(product.id)
            if id in self.cart.keys():
                self.cart[id]["quantity"] -= 1
                self.cart[id]["amount"] -= product.price
                if self.cart[id]["quantity"] <= 0:
                    self.delete(product)
                self.save_cart()

        elif product.category == 1:
            id = str(product.id)
            if id in self.cart.keys():
                self.cart[id]["quantity"] -= 1
                self.cart[id]["amount"] -= product.price
                if self.cart[id]["quantity"] <= 0:
                    self.delete(product)
                self.save_cart()

    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True

