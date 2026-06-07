import uuid
from payment.payment import Payment
from payment.payment_status import PaymentStatus


class PaymentService:
    #  In a real implementation, this would integrate with a payment gateway
    def process_payment(self, booking_id: str, amount: float) -> Payment:

        return Payment(
            payment_id=str(uuid.uuid4()),
            booking_id=booking_id,
            amount=amount,
            status=PaymentStatus.SUCCESS,
        )
