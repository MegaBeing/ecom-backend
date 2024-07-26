class OrderStatus:
    Ordered = 0
    Shipped = 6
    Delivered = 7
    Canceled = 8
    OutForDelivery = 17
    InTransit = 18
    choices = (
        (Ordered,'Ordered'),
        (Shipped, 'Shipped'),
        (Delivered, 'Delivered'),
        (Canceled, 'Canceled'),
        (OutForDelivery,'Out for delivery'),
        (InTransit, 'In transit'),
    )

class PaymentStatus:
    Accepted = 'accepted'
    Pending = 'pending'
    choices = (
        (Accepted,'Accepted'),
        (Pending,'Pending')
    )