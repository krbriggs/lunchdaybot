from datetime import datetime, timedelta


def byteCafeUrl():
    today = datetime.today()
    weekday = today.weekday()

    if weekday == 0:
        last_monday = today
    else:
        last_monday = today - timedelta(days=weekday)

    monday_month = str(last_monday.month)
    monday_day = str(last_monday.day)
    monday_year = str(last_monday.year)

    if int(monday_day) < 10:
        monday_day = "0" + monday_day
    if int(monday_month) < 10:
        monday_month = "0" + monday_month

    byte_url = "http://dining.guckenheimer.com/clients/npcholdings/fss/fss.nsf/" + \
                "weeklyMenuLaunch/9W4S24~" + monday_month + "-" + monday_day + \
                "-" + monday_year + "/%24file/cafehome.htm"
    return byte_url