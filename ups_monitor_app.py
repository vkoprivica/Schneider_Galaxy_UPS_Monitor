import ups_monitor_api
from ups_monitor_api import get_ups_reading
from ups_monitor_api import get_battery_charge
from ups_monitor_api import get_remaining_backup_time
from ups_monitor_api import send_email
from datetime import datetime, timedelta
import time
from threading import Timer
import random
import requests.exceptions
import sys
import logbook
import pytz
import os


def main():

    app_log = logbook.Logger("ups_program")

    # Define values prior to loop.
    counter_email = 0
    counter_1 = 0
    counter_100 = 0
    counter = 0
    counter_90 = 0
    counter_80 = 0
    counter_70 = 0
    counter_60 = 0
    counter_50 = 0
    counter_40 = 0
    counter_30 = 0
    counter_20 = 0
    counter_10 = 0
    thirty = "30"
    thirty_min = datetime.strptime(thirty, "%M").time()
    ups_hostname = "UPS_HOSTNAME"
    # notification = "Notification"
    previous_battery_charge = None

    while True:

        try:
            try:
                battery_charge = ups_monitor_api.get_battery_charge(
                    get_ups_reading
                )  # Read battery charge by calling function.
                # battery_charge = random.randint(65, 100)
                print(f"Battery Charge: {battery_charge}")
                app_log.notice(f"Battery Charge: {battery_charge}")  # Log value.
            except:
                app_log.warn(f"{battery_charge}")  # Log if calling function fails.

            try:
                remaining_backup_time = ups_monitor_api.get_remaining_backup_time(
                    get_ups_reading
                )  # Read remaining backup time by calling function.
                # print(f"Remaining backup time: {remaining_backup_time}")
                app_log.notice(f"Remaining Backup Time: {remaining_backup_time}")
            except:
                app_log.warn(f"{remaining_backup_time}")

            email_body = f"Current Charge: {battery_charge}%\nRemaining Time: {remaining_backup_time}"

            if battery_charge == 100:
                counter_100 += 1
                counter = 0

                if counter_100 == 1:
                    ups_monitor_api.send_email(
                        f"{ups_hostname} - Battery at 100%", email_body
                    )
                    # print(f"Counter_100 1: {counter_100}")
                    # print(f"Counter 1: {counter}")

            else:

                if previous_battery_charge is None:
                    notification = "Current Battery Charge"
                elif battery_charge > previous_battery_charge:
                    notification = "Increased Battery Charge"
                else:
                    notification = "Decreased Battery Charge"

                counter_100 = 0
                counter += 1

                if 89 < battery_charge < 100:
                    counter_90 += 1
                    counter_80 = 0
                    counter_70 = 0
                    counter_60 = 0
                    counter_50 = 0
                    counter_40 = 0
                    counter_30 = 0
                    counter_20 = 0
                    counter_10 = 0

                    if counter_90 == 1:
                        ups_monitor_api.send_email(
                            f"{ups_hostname} - {notification}", email_body
                        )
                        # print(f"Counter_100 3: {counter_100}")
                        # print(f"Counter 3: {counter_90}")

                    else:
                        pass

                elif 79 < battery_charge < 90:
                    counter_80 += 1
                    counter_90 = 0
                    counter_70 = 0
                    counter_60 = 0
                    counter_50 = 0
                    counter_40 = 0
                    counter_30 = 0
                    counter_20 = 0
                    counter_10 = 0

                    if counter_80 == 1:
                        ups_monitor_api.send_email(
                            f"{ups_hostname} - {notification}", email_body
                        )
                        # print(f"Counter_100 5: {counter_100}")
                        # print(f"Counter 5: {counter_80}")

                    else:
                        pass

                elif 69 < battery_charge < 80:
                    counter_70 += 1
                    counter_90 = 0
                    counter_80 = 0
                    counter_60 = 0
                    counter_50 = 0
                    counter_40 = 0
                    counter_30 = 0
                    counter_20 = 0
                    counter_10 = 0

                    if counter_70 == 1:
                        ups_monitor_api.send_email(
                            f"{ups_hostname} - {notification}", email_body
                        )
                        # print(f"Counter_100 7: {counter_100}")
                        # print(f"Counter 7: {counter_70}")

                    else:
                        pass

                elif 59 < battery_charge < 70:
                    counter_60 += 1
                    counter_90 = 0
                    counter_80 = 0
                    # counter_60 = 0
                    counter_50 = 0
                    counter_40 = 0
                    counter_30 = 0
                    counter_20 = 0
                    counter_10 = 0

                    if counter_60 == 1:
                        ups_monitor_api.send_email(
                            f"{ups_hostname} - {notification}", email_body
                        )
                        # print(f"Counter_100 9: {counter_100}")
                        # print(f"Counter 9: {counter_60}")

                    else:
                        pass

                elif 49 < battery_charge < 60:
                    counter_50 += 1
                    counter_90 = 0
                    counter_80 = 0
                    counter_60 = 0
                    # counter_50 = 0
                    counter_40 = 0
                    counter_30 = 0
                    counter_20 = 0
                    counter_10 = 0

                    if counter_50 == 1:
                        ups_monitor_api.send_email(
                            f"{ups_hostname} - {notification}", email_body
                        )
                        # print(f"Counter_100 11: {counter_100}")
                        # print(f"Counter 11: {counter_50}")

                    else:
                        pass

                elif 39 < battery_charge < 50:
                    counter_40 += 1
                    counter_90 = 0
                    counter_80 = 0
                    counter_60 = 0
                    counter_50 = 0
                    # counter_40 = 0
                    counter_30 = 0
                    counter_20 = 0
                    counter_10 = 0

                    if counter_40 == 1:
                        ups_monitor_api.send_email(
                            f"{ups_hostname} - {notification}", email_body
                        )
                        # print(f"Counter_100 13: {counter_100}")
                        # print(f"Counter 13: {counter_40}")

                    else:
                        pass

                elif 29 < battery_charge < 40:
                    counter_30 += 1
                    counter_90 = 0
                    counter_80 = 0
                    counter_60 = 0
                    counter_50 = 0
                    counter_40 = 0
                    # counter_30 = 0
                    counter_20 = 0
                    counter_10 = 0

                    if counter_30 == 1:
                        ups_monitor_api.send_email(
                            f"{ups_hostname} - {notification}", email_body
                        )
                        # print(f"Counter_100 15: {counter_100}")
                        # print(f"Counter 15: {counter_30}")

                    else:
                        pass

                elif 19 < battery_charge < 30:
                    counter_20 += 1
                    counter_90 = 0
                    counter_80 = 0
                    counter_60 = 0
                    counter_50 = 0
                    counter_40 = 0
                    counter_30 = 0
                    # counter_20 = 0
                    counter_10 = 0

                    if counter_20 == 1:
                        ups_monitor_api.send_email(
                            f"{ups_hostname} - {notification}", email_body
                        )
                        # print(f"Counter_100 17: {counter_100}")
                        # print(f"Counter 17: {counter_20}")

                    else:
                        pass

            previous_battery_charge = battery_charge

            # print("Thirty time")
            if thirty_min > remaining_backup_time:
                counter_1 += 1
                if counter == 1:
                    ups_monitor_api.send_email(
                        "UPS Warning", f"Remaining Time: {remaining_backup_time}"
                    )

            counter_email = 0
        except:
            counter_email += 1
            # print("General Exception")
            # print("starting timer")
            if counter_email == 1:
                try:
                    ups_monitor_api.send_email(
                        "UPS-MONITOR-APP", "Parsing Failure! Check log for more info."
                    )
                    app_log.warn("ERROR: Parsing Failure.")

                except:
                    app_log.warn("ERROR: Failed to Send Email.")
            else:
                pass

            counter_1 = 0
            counter_100 = 0
            time.sleep(60)
            continue

        # print("timer")
        time.sleep(300)


def init_logging(filename: str = None):
    """Logging function to create new logging file each day.
    """
    level = logbook.TRACE
    logbook.set_datetime_format("local")  # Logging in local timezone.

    # Set location of logs.
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, "log", filename)

    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = "Logging initialized, level: {}, mode: {}".format(
        level, "stdout mode" if not filename else "file mode: " + filename
    )
    logger = logbook.Logger("Startup")
    logger.notice(msg)


if __name__ == "__main__":
    init_logging("log-ups-program.log")
    main()
