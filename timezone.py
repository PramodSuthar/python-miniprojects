from datetime import datetime
import pytz

timezone = pytz.timezone('Asia/Kolkata')
currentTime = datetime.now(timezone)
print(currentTime.strftime("Current time in " + str(timezone) + " is %H:%M:%S")
)