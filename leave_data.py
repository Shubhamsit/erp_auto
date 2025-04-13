

from dataclasses import dataclass

@dataclass
class LeaveApplication:
    start_date: str
    start_time: str
    end_date: str
    end_time: str
    destination: str
    leave_reason: str

leave = LeaveApplication(
    start_date="13-June-2026",
    start_time="09:00",
    end_date="15-July-2026",
    end_time="22:50",
    destination="Bhubaneswar",
    leave_reason="going to"
)
