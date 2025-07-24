import re
import pandas as pd

def preprocess(data):
    messages = []
    dates = []
    pattern = r'\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2}\s?[AP]M(?=\s-\s)'

    for line in data.splitlines():
        match = re.match(pattern, line)
        if match:
            date = match.group(0)
            message = line[match.end():].strip()
            dates.append(date)
            messages.append(message)
    dataFrame = pd.DataFrame({'message': messages, 'date': dates})
    dataFrame['date'] = pd.to_datetime(dataFrame['date'], format='%d/%m/%y, %I:%M\u202f%p', errors='coerce', dayfirst=True)
    dataFrame.dropna(subset=['date'], inplace=True)
    user = []
    message = []
    for line in dataFrame['message']:
        line = re.split(r'([\w\W]+?):\s', line)
        if (line[1:]):
            user.append(line[1])
            message.append(line[2])
        else:
            user.append('group_notification')
            message.append(line[0])
    dataFrame['user'] = user
    dataFrame['message'] = message
    dataFrame['year'] = dataFrame['date'].dt.year
    dataFrame['month_num']=dataFrame['date'].dt.month
    dataFrame['month'] = dataFrame['date'].dt.month_name()
    dataFrame['day'] = dataFrame['date'].dt.day
    dataFrame['hour'] = dataFrame['date'].dt.hour
    dataFrame['minute'] = dataFrame['date'].dt.minute
    dataFrame['only_date']=dataFrame['date'].dt.date
    dataFrame['day_name']=dataFrame['date'].dt.day_name()
    return dataFrame