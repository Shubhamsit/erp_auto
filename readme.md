# 🏫 ERP Auto Leave Application 

This project automates the process of applying for leave on the [Silicon Institute ERP Portal](https://erp.silicon.ac.in/estcampus/) using Python and Selenium.  
It logs into the ERP system, navigates to the leave application section, fills in the leave form, and submits it — all hands-free 🚀

---

## 📁 Folder Structure
```
erp_auto/
├── .env
├── .gitignore
├── apply_leave.py
├── leave_data.py
├── login.py
├── main.py
└── README.md
```

## 🚀 1. For Setup
###  First ` Clone the repository`

 ## -> Create `.env` file with these exact values:
   ```bash
ERP_USERNAME="22bcsi31" // your sic
ERP_PASSWORD="erp_password" // your password

   ```

## 2. Activating the Virtual Environment

Make sure you're in the project directory (`erp_auto`) before running these commands.

### 🪟 On Windows (CMD)
```
venv\Scripts\activate
```

### 💻 On macOS / Linux / Windows (PowerShell)
```
source venv/bin/activate
```
## Edit leave_data.py (add your leave info)

```
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
    leave_reason="going to relative house" 
)

Note-> leave reason should be greater than  length 20

```

## Running (Ensure you should be in the erp_auto folder)

```
python main.py
```

✅ **It will:**  
> Log in to the college ERP using your credentials 

> Navigate to the  sections one by one 

> Fill out the necessary info using leave_data.py

> Leave applied sucessfully


