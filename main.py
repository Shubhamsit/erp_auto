from login import login_to_erp
from apply_leave import apply_for_leave
from dotenv import load_dotenv
import os
from leave_data import leave

load_dotenv()

if __name__ == "__main__":
    driver = login_to_erp()
    warning=apply_for_leave(
    driver,
    leave.start_date,
    leave.start_time,
    leave.end_date,
    leave.end_time,
    leave.destination,
    leave.leave_reason
)

    print(warning)
