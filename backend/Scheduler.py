services/scheduler.py(Core Logic) 

appointments = []

def book_slot(name, date, time):
    for a in appointments:
        if a["date"] == date and a["time"] == time:
            return "❌ Slot already booked"

    appointments.append({
        "name": name,
        "date": date,
        "time": time
    })

    return f"✅ Appointment confirmed for {date} at {time}"
