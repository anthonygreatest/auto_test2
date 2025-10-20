from conftest import valid_booking_payload
from models.booking import CreateBookingResponse
from src.constants import BookingData


def test_create_booking(created_booking):
    try:
        parsed = CreateBookingResponse(**created_booking)
    except Exception as e:
        raise AssertionError(f'Response structure is incorrect: {e}')

    assert parsed.booking.bookingdates.checkin == '2026-01-01'



    assert created_booking['booking']['firstname'] == BookingData.FIRSTNAME.value, (
        'Returned incorrect name\n'
        f'Response:\n{created_booking}\n'
        f'Expected name: {BookingData.FIRSTNAME}'
    )
    assert created_booking['booking']['lastname'] == BookingData.LASTNAME.value, (
        'Returned incorrect lastname\n'
        f'Response:\n{created_booking}\n'
        f'Expected name: {BookingData.LASTNAME}'
    )

def test_update_booking(booking_client, created_booking, auth_token, headers, valid_booking_payload):
    booking_id = created_booking['bookingid']
    headers.update({'Cookie': f'token={auth_token}'})
    payload = valid_booking_payload.build()
    payload.update({'firstname': BookingData.UPDATE_FIRSTNAME.value})
    update_response = booking_client.update_booking(booking_id, headers, payload)
    assert update_response.json()['firstname'] == BookingData.UPDATE_FIRSTNAME.value

    print(update_response.json())

