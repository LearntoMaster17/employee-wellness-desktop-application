# Shows notification and plays text-to-speech reminder every 2 hours from plyer
from plyer import notification
import win32com.client as wincl
import time

if __name__ == "__main__":
    spk = wincl.Dispatch("SAPI.SpVoice")
    while True:
        try:
            notification.notify(
                title="*** Please Drink Water ***",
                message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men.",
                app_icon="C:/Users/a/Downloads/venev/os module/file_ico.ico",
                timeout=10)
            spk.Speak("Please drink water now for your health")
            time.sleep(60 * 60 * 2)  # Notification will be shown after every 2 hours
            print("Notification sent successfully!")

        except Exception as e:
            print(f"Notification error: {e}")