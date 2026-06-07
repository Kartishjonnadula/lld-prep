from dataclasses import dataclass

from payment.payment_status import PaymentStatus


@dataclass
class Payment:

    payment_id: str

    booking_id: str

    amount: float

    status: PaymentStatus
