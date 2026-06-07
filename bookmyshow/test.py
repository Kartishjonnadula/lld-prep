from booking.booking_status import BookingStatus
from booking_system import BookingService
from movie import Movie
from payment.payment_service import PaymentService
from screen import Screen
from seats.seat import Seat
from seats.seat_category import SeatCategory
from seats.seat_state import SeatState
from show import Show


def test_successful_booking():

    # Create Seat Layout
    seats = [
        Seat("A1", SeatCategory.PLATINUM),
        Seat("A2", SeatCategory.PLATINUM),
        Seat("B1", SeatCategory.GOLD),
        Seat("B2", SeatCategory.GOLD),
    ]

    screen = Screen(
        screen_id="SCREEN_1",
        seats=seats,
    )

    movie = Movie(
        movie_id="MOVIE_1",
        title="Interstellar",
        duration_minutes=180,
    )

    show = Show(
        show_id="SHOW_1",
        movie=movie,
        screen=screen,
        category_prices={
            SeatCategory.PLATINUM: 300,
            SeatCategory.GOLD: 200,
            SeatCategory.SILVER: 100,
        },
    )

    payment_service = PaymentService()

    booking_service = BookingService(payment_service=payment_service)

    # Act
    booking = booking_service.create_booking(
        user_id="USER_1",
        show=show,
        seat_ids=["A1", "A2"],
    )

    # Assert booking
    assert booking.status == BookingStatus.CONFIRMED

    # Assert seats booked
    assert show.show_seats["A1"].state == SeatState.BOOKED

    assert show.show_seats["A2"].state == SeatState.BOOKED

    print("Booking successful")


test_successful_booking()
