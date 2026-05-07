import time


def schedule_applications(applications):
    for app in applications:

        # simulate delay to avoid spam detection
        time.sleep(2)

        print("Submitting application to:", app["job"]["title"])

    return True