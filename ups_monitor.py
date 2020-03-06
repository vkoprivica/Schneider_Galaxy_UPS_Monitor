import re
import requests
import requests.exceptions
import bs4
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep
from datetime import datetime


def send_email(subject_text, report_text):
    """ Send email via email realay. Takes two string arguments:
    subject_text will pressent suject line of email
    report_text will pressent body of the email. 
    """
    fromaddr = "sender@domain.com"
    toaddr = "recipient@domain.com"
    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg["To"] = toaddr
    msg["Subject"] = str(subject_text)
    body = str(report_text)
    msg.attach(MIMEText(body, "plain"))
    server = smtplib.SMTP("relay.domain.com", 25)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr.split(","), text)


# URL of site we want to scrape
URL = "http://10.10.10.10/UPS/ups_prop.htm"


def get_ups_reading():
    """Calling this function will access webgui of the UPS
    device and return all data in the string format.
    """
    try:
        raw_site_page = requests.get(URL)  # Pull down the site.
        raw_site_page.raise_for_status()  # Confirm if site was pulled. Error if not.
        raw_site_page.close()
        return raw_site_page
    except requests.exceptions.ConnectionError:
        return "ERROR: Could not find UPS device. Check your network connection."


def get_battery_charge(get_ups_reading):
    """Function grabs UPS rading, parse and extract battery
    charge value.
    """
    try:
        soup = bs4.BeautifulSoup(get_ups_reading().content, "html.parser")
        table = soup.find_all("table")[7]
        # Parse battery charge level and convert into integer.
        battery_charge = [div for div in table.find_all("div")]
        return int(battery_charge[0].string.strip(" %"))
    except AttributeError:
        return "ERROR: Not able to parse battery_charge data."


def get_remaining_backup_time(get_ups_reading):
    """Function grabs UPS rading, parse and extract remaining
    backup time.
    """
    try:
        soup = bs4.BeautifulSoup(get_ups_reading().content, "html.parser")
        table = soup.find_all("table")[7]

        remaining_backup_time = [div for div in table.find_all("div")][1].string

        remaining_backup_time_converted = re.findall(r"\d+", remaining_backup_time)
        remaining_backup_time_converted = " ".join(remaining_backup_time_converted)
        try:
            ups_time = datetime.strptime(
                remaining_backup_time_converted, "%H %M %S"
            ).time()
        except:
            pass
        try:
            ups_time = datetime.strptime(
                remaining_backup_time_converted, "%M %S"
            ).time()
        except:
            pass
        try:
            ups_time = datetime.strptime(remaining_backup_time_converted, "%M").time()
        except:
            pass

        return ups_time
    except AttributeError:
        return "ERROR: Not able to parse remaining_backup_time data."


# if __name__ == "__main__":
#     print(get_battery_charge(get_ups_reading))
#     print(get_remaining_backup_time(get_ups_reading))
