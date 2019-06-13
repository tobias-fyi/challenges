import os
import datetime
import time


root_dir = "/Users/Tobias/workshop/Challenges/100DaysofX/01-Code"

start_date = datetime.date(2019, 3, 3)
new_year = datetime.date(2019, 1, 1)

for td in range(73, 101):
    os.chdir(root_dir)

    # Turn the day# into 3 char string
    day_num = str(td).zfill(3)

    # Find the date corresponding to current 'td'
    time_d = datetime.timedelta(days=td)
    date = start_date + time_d

    # Extract + format individual datetime objects
    year = str(date.year)
    month = str(date.month).zfill(2)
    day = str(date.day).zfill(2)

    # Calculate the day of the year
    time_since_nye = date - new_year
    yeardate_diff = str(time_since_nye)
    year_total_days = yeardate_diff[0:3]

    # Create the day's directory + path
    dir_name = f"{day_num}"
    os.makedirs(dir_name)
    dir_path = os.path.join(root_dir, dir_name)

    body_content = f"""# {date} | #100DaysofCode

    GOAL-{month}-{day} ~ Session Goal

## Day {day_num}/100 | {year_total_days}/365

Table of Contents

---- Tasks ----


---- Notes ----


---- Resources ----


---- Selects ----


---- Sojourn ----

"""

    # Create the journal entry
    journal_name = f"{day_num}-journal.md"

    os.chdir(dir_path)
    with open(journal_name, "w") as j:
        j.write(body_content)

    print(f"Successfully created {journal_name}.")
    print(f"Located at {dir_path}.")
