class OrderStatus:
    Shipped = 6
    Delivered = 7
    Canceled = 8
    OutForDelivery = 17
    InTransit = 18
    choices = (
        (Shipped, 'Shipped'),
        (Delivered, 'Delivered'),
        (Canceled, 'Canceled'),
        (OutForDelivery,'Out for delivery'),
        (InTransit, 'In transit'),
    )

class PaymentStatus:
    Prepaid = 'prepaid'
    CashOnDelivery = 'cod'
    choices = (
        (Prepaid, 'Prepaid'),
        (CashOnDelivery, 'Cash on delivery'),
    )