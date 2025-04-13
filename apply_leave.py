
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime

def apply_for_leave(driver, start_date, start_time, end_date, end_time, destination, leave_reason):
    try:
        #  Navigation to leave application form
        driver.find_element(By.XPATH, '/html/body/div[2]/aside[1]/section/ul/li[2]/a').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[2]/aside[1]/section/ul/li[2]/ul/li[1]/a').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="btnNewLeave"]').click()
        time.sleep(2)

        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)

        # Month abbreviation to number mapping
        MONTHS = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4,
            'May': 5, 'June': 6, 'July': 7, 'August': 8,
            'September': 9, 'October': 10, 'November': 11, 'December': 12
        }

        def select_date_with_picker(field_id, date_str):

            # Parse date (format: "13-Apr-2025")

            day, month_abbr, year = date_str.split('-')
            target_month = MONTHS[month_abbr]
            target_year = int(year)
            target_day = int(day)
            
            # Click date field to open picker
            date_field = wait.until(EC.element_to_be_clickable((By.ID, field_id)))
            print("date picker bhai")
            date_field.click()
            print("opeend date picker")
            time.sleep(1)
            
            # Wait for datepicker to appear
            datepicker = wait.until(EC.visibility_of_element_located(
                (By.CLASS_NAME, 'datepicker-days')
            ))
            
            # Navigate to correct month and year
            while True:
                current_month_year = datepicker.find_element(By.CLASS_NAME, 'datepicker-switch').text
                current_month, current_year = current_month_year.split()
                current_month_num = MONTHS[current_month]
                current_year_num = int(current_year)
                
                # Check if  reached the target month/year

                if current_month_num == target_month and current_year_num == target_year:
                    break
                
                # Determine if  need to go forward or backward

                if (current_year_num < target_year) or (current_year_num == target_year and current_month_num < target_month):
                    datepicker.find_element(By.CLASS_NAME, 'next').click()
                else:
                    datepicker.find_element(By.CLASS_NAME, 'prev').click()
                time.sleep(0.5)
            
            # Select the day

            day_element = wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//td[contains(@class, 'day') and not(contains(@class, 'old')) and not(contains(@class, 'new')) and text()='{target_day}']")
            ))
            day_element.click()
            time.sleep(0.5)
        
        def select_time_with_picker(field_id, time_str):
            my=0
            # Parse target time (format: "18:00")
            
            target_hour, target_minute = map(int, time_str.split(':'))
            
            # Click time field to open picker

            time_field = wait.until(EC.element_to_be_clickable((By.ID, field_id)))
            time_field.click()
            print("clicked bro")
            time.sleep(1)
            print("after sleep")
            
            # Wait for timepicker to appear

            timepicker = wait.until(EC.visibility_of_element_located(
                (By.CLASS_NAME, 'bootstrap-timepicker-widget.dropdown-menu.open')
            ))
            print("time picker appeard")
            print(timepicker)
         

            # Get current time values

            current_hour = int(timepicker.find_element(By.CLASS_NAME, 'bootstrap-timepicker-hour').text)
            current_minute = int(timepicker.find_element(By.CLASS_NAME, 'bootstrap-timepicker-minute').text)
            
            # Calculate needed adjustments
            
            hour_diff = target_hour - current_hour
            minute_diff = target_minute - current_minute
            
            # Get control elements
            hour_up = timepicker.find_element(By.XPATH, f"//div[contains(@class, 'bootstrap-timepicker-widget') and contains(@class, 'open')]//a[@data-action='incrementHour']")
            hour_down = timepicker.find_element(By.XPATH, f"//div[contains(@class, 'bootstrap-timepicker-widget') and contains(@class, 'open')]//a[@data-action='decrementHour']")
            minute_up = timepicker.find_element(By.XPATH, f"//div[contains(@class, 'bootstrap-timepicker-widget') and contains(@class, 'open')]//a[@data-action='incrementMinute']")
            minute_down = timepicker.find_element(By.XPATH, f"//div[contains(@class, 'bootstrap-timepicker-widget') and contains(@class, 'open')]//a[@data-action='decrementMinute']")
            
            # Adjust hours
            for _ in range(abs(hour_diff)):
                if hour_diff > 0:
                    hour_up.click()
                else:
                    hour_down.click()
                time.sleep(0.1)
            
            # Adjust minutes (in 5-minute increments)
            minute_steps = abs(minute_diff) // 5
            for _ in range(minute_steps):
                if minute_diff > 0:
                    minute_up.click()
                else:
                    minute_down.click()
                time.sleep(0.1)
            
            # Click outside to close
            time_field.click()
            time.sleep(0.5)


        #  Fill date and time fields
        select_date_with_picker("leaveDateFrom", start_date)
        select_time_with_picker("leaveTimeFrom", start_time)
        select_date_with_picker("leaveDateTo", end_date)
        select_time_with_picker("leaveTimeTo", end_time)



        #  Fill Destination
        dest = driver.find_element(By.ID, "txtdestination")
        dest.send_keys(Keys.CONTROL + "a")
        dest.send_keys(Keys.DELETE)
        dest.send_keys(destination)
        time.sleep(0.5)

        #Fill Reason

        if(len(leave_reason)<20):
             return "reason length should be grater than 20"
        rsn = driver.find_element(By.ID, "txtLeaveReason")
        rsn.send_keys(Keys.CONTROL + "a")
        rsn.send_keys(Keys.DELETE)
        rsn.send_keys(leave_reason)
        time.sleep(1)

        # Click "Apply"
        apply_btn = driver.find_element(By.ID, "btnApplyLeave")
        apply_btn.click()
        time.sleep(2)

        print(" Leave applied successfully!")

    except Exception as e:
        print(f" Error applying leave: {str(e)}")
       