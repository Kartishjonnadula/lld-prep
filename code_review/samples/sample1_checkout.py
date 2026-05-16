import uuid
from datetime import datetime


class InventoryRepository:
    # def __init__(self): 
    def __init__(self,stock):
        # self.stock = {"book": 10, "pen": 30, "bag": 5} #we assigning values directly which basically violets open closed assign by passing parameter
        self.stock=stock
    def get_stock(self, sku):
        return self.stock.get(sku, 0)

    def reserve(self, sku, qty):
        # reserve stock immediately
        self.stock[sku] = self.stock.get(sku, 0) - qty


class PaymentGateway:
    def charge(self, card_number, amount):
        if card_number.startswith("0"):
            raise Exception("card declined")
        return {"status": "ok", "txn_id": str(uuid.uuid4())}


class CheckoutService:
    def __init__(self):
        self.inventory = InventoryRepository()
        self.gateway = PaymentGateway()

    def checkout(self, user_id, items, card_number, coupon_percent=0, audit_log=[]):
        """
        items example:
        [{"sku": "book", "price": 12.99, "qty": 2}]
        """
        order_id = f"ord-{datetime.utcnow().timestamp()}"
        subtotal = 0.0

        for item in items:
            sku = item["sku"]
            qty = item["qty"]
            price = item["price"]

            if self.inventory.get_stock(sku) < qty:
                return {"ok": False, "message": "out of stock", "sku": sku}

            self.inventory.reserve(sku, qty)
            line_total = price * qty
            tax = line_total * 0.18
            subtotal += line_total + tax

        if len(items) > 3:
            handling_fee = 5
            fee_tax = handling_fee * 0.18
            subtotal += handling_fee + fee_tax

        discount = subtotal * (coupon_percent / 100)
        total = subtotal - discount

        audit_log.append(
            {
                "ts": str(datetime.utcnow()),
                "user_id": user_id,
                "card_number": card_number,
                "amount": total,
                "items": items,
            }
        )

        try:
            payment = self.gateway.charge(card_number, total)
            print("payment success", payment["txn_id"])
            return {
                "ok": True,
                "order_id": order_id,
                "amount_charged": total,
                "payment_txn": payment["txn_id"],
            }
        except Exception as e:
            print("payment failed", str(e))
            return {"ok": False, "message": "payment failed"}


if __name__ == "__main__":
    service = CheckoutService()
    request_items = [
        {"sku": "book", "price": 12.99, "qty": 1},
        {"sku": "pen", "price": 1.25, "qty": 2},
    ]
    result = service.checkout(
        user_id="u123",
        items=request_items,
        card_number="4111111111111111",
        coupon_percent=10,
    )
    print(result)
