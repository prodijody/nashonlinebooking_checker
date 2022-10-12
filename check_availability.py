import contextlib
import time
from tkinter import E

from playwright.sync_api import Playwright, expect, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    page = context.new_page()
    try:
        page.goto("https://nashonlinebooking.com/onlinebookingsystem/en/?hbref=7303069")
        time.sleep(5)
        page.get_by_role("link", name="Continue to online booking").click()
        with contextlib.suppress(Exception):
            page.get_by_role("link", name="Continue to online booking").click()
        page.wait_for_url(
            "https://nashonlinebooking.com/onlinebookingsystem/en/appointments/booking/index#"
        )
        time.sleep(1)
        page.get_by_role("link", name=" Book Book appointment").click()
        page.wait_for_url(
            "https://nashonlinebooking.com/onlinebookingsystem/en/appointments/booking/create"
        )

        time.sleep(1)
        page.locator("#appointmentFieldGender").select_option("7303040")

        page.get_by_placeholder("Please enter ...").click()

        page.get_by_placeholder("Please enter ...").fill("07445248840")

        page.get_by_placeholder("Please confirm your mobile number ...").click()

        page.get_by_placeholder("Please confirm your mobile number ...").click()

        page.get_by_placeholder("Please confirm your mobile number ...").fill(
            "07445248840"
        )

        page.locator("#appointmentFieldDateOfBirthDay").select_option("2")

        page.locator("#appointmentFieldDateOfBirthMonth").select_option("1")

        page.locator("#appointmentFieldDateOfBirthYear").select_option("1994")
        time.sleep(1)
        page.get_by_role("link", name="Continue ").click()
        page.get_by_role("link", name="Continue ").click()
        page.wait_for_url(
            "https://nashonlinebooking.com/onlinebookingsystem/en/appointments/booking/create#step-2"
        )

        page.locator("#appointmentFieldPostcode").click()

        page.locator("#appointmentFieldPostcode").fill("g1 5ez")
        time.sleep(1)
        page.get_by_role("link", name="Continue ").click()
        page.get_by_role("link", name="Continue ").click()
        time.sleep(1)
        with contextlib.suppress(Exception):
            page.get_by_role("link", name="Continue ").click()
        page.wait_for_url(
            "https://nashonlinebooking.com/onlinebookingsystem/en/appointments/booking/create#step-3"
        )
        page.locator("#appointmentFieldService").select_option("7303016")
        page.locator("#appointmentFieldSubService").select_option("7303023")
        time.sleep(1)
        page.get_by_role("link", name="Continue ").click()
        page.wait_for_url(
            "https://nashonlinebooking.com/onlinebookingsystem/en/appointments/booking/create#step-4"
        )
        page.get_by_role("link", name="Search ").click()
        page.wait_for_url(
            "https://nashonlinebooking.com/onlinebookingsystem/en/appointments/booking/create#"
        )
        time.sleep(5)
        try:
            expect(
                page.get_by_text(
                    "We are sorry we have no IUD appointments currently available. We open clinics on"
                )
            )
            page.screenshot(path="screenshot.png")
            print("No Appointments")
        except Exception:
            print("Found an appointment")
            page.screenshot(path="screenshot_appointments.png")
    except:
        page.screenshot(path="screenshot_error.png")
        print("Error")
        raise
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    while True:
        try:
            run(playwright)
            break
        except Exception as e:
            print(f"Error - {e}")
            time.sleep(5)
