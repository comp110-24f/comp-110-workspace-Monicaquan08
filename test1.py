def update_attendance(
    attendance_dict: dict[str, list[str]], day: str, student: str
) -> None:

    if day not in attendance_dict:
        attendance_dict[day] = []
        # If day is NOT in attendance_dict; add it with an empty list

    if student not in attendance_dict[day]:
        attendance_dict[day].append(student)
    # If student is NOT already in attendance_dict values; append student


attendance_dict: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Vrinda"]}
update_attendance(attendance_dict, "Tuesday", "Vrinda")
update_attendance(attendance_dict, "Wednesday", "Kaleb")
print(attendance_dict)
