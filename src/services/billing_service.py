# services/billing_service.py
import time
import os
from typing import List
from src.models.cart_item import CartItem
from src.repositories.product_repository import fetch_active_products_for_billing

DISCOUNT_RATE = 0.05

class BillingService:
    @staticmethod
    def generate_invoice_id() -> int:
        return int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))

    @staticmethod
    def calculate_totals(cart_items: List[CartItem]) -> tuple[float, float, float]:
        """Returns (bill_amount, discount, net_pay)"""
        bill_amount = sum(item.total_price for item in cart_items)
        discount = bill_amount * DISCOUNT_RATE
        net_pay = bill_amount - discount
        return bill_amount, discount, net_pay

    @staticmethod
    def get_active_products() -> List[tuple]:
        """For billClass product table - returns raw tuples for compatibility"""
        return fetch_active_products_for_billing()
