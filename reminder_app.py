import time
import datetime
import threading
import os

try:
    import winsound  # For sound alerts (Windows)
except ImportError:
    winsound = None  # For macOS/Linux


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def banner():
    print("=" * 60)
    print("⏰  WELCOME TO YOUR SMART REMINDER APP  ⏰".center(60))
    print("=" * 60)


def remind(task, remind_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == remind_time:
            print(f"\n🔔 Reminder: {task} at {remind_time}!")
            if winsound:
                for _ in range(3):
                    winsound.Beep(1000, 500)
            else:
                print("🔊 *ding ding ding* (Sound alert)")
            break
        time.sleep(10)


def main():
    clear_console()
    banner()
    reminders = []

    while True:
        task = input("\n📝 Enter your reminder (or type 'done' to finish): ")
        if task.lower() == 'done':
            break

        remind_time = input("⏱ Enter time (HH:MM, 24-hour format): ")
        reminders.append((task, remind_time))
        print(f"✅ Reminder '{task}' set for {remind_time}!")

    print("\n🎯 All reminders are set. I’ll notify you at the right time!\n")

    for task, remind_time in reminders:
        threading.Thread(target=remind, args=(task, remind_time)).start()


if name == "main":
    main()
