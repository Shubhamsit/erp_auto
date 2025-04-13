from login import login_to_erp
from apply_leave import apply_for_leave
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    driver = login_to_erp()
    warning=apply_for_leave(
    driver,
    start_date=os.getenv("start_date"),
    start_time=os.getenv("start_time"),
    end_date=os.getenv("end_date"),
    end_time=os.getenv("end_time"),
    destination=os.getenv("destination"),
    leave_reason=os.getenv("leave_reason")
)

    print(warning)
