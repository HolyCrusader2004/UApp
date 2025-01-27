from parking_func.models import ParkingRequest, ParkingSlots
from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler

# Create your views here.

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(checkSlots, 'interval', minutes=1)
    scheduler.start()


def checkSlots():
    all_slots = ParkingSlots.objects.all()
    # print("yesss")
    for slot in all_slots:
        try:
            pending_request = ParkingRequest.objects.filter(
                parking_slot_number=slot.id, status='ApprovedPending').order_by('start_date').first()

            if slot.status == 'Occupied' and slot.end_date <= timezone.now().date():
                slot.status = 'Available'
                slot.student_name = None
                slot.registration_plate = None
                slot.start_date = None
                slot.end_date = None
                slot.save()

            if pending_request:
                if pending_request.start_date <= timezone.now().date():
                    slot.status = 'Occupied'
                    slot.student_name = pending_request.student_name
                    slot.registration_plate = pending_request.registration_plate
                    slot.start_date = pending_request.start_date
                    slot.end_date = pending_request.end_date
                    slot.save()
                    pending_request.status = 'Approved'
                    pending_request.save()

                    print(f'Successfully updated parking slot {slot.id} with customer {pending_request.student_name}.')
                else:
                    print(f'Slot {slot.id} remains available, no valid requests for today.')

            # print(f'Checked parking slot {slot.id} successfully.')

        except Exception as e:
            print(f"Error processing parking slot {slot.id}: {str(e)}")
