# Employee Wellness Desktop Application

A Python-based desktop application designed to promote employee health and well-being by providing regular hydration reminders. This project demonstrates practical skills in desktop automation, notifications, and cross-platform Python development.

---

## Project Overview

The **Employee Wellness Desktop Application** is a lightweight tool that reminds users to drink water at regular intervals. It leverages desktop notifications and text-to-speech to encourage healthy hydration habits, supporting workplace wellness initiatives.

---

## Key Features

- **Automated Hydration Reminders**:  
  - Sends a desktop notification every 2 hours with a health message and recommended daily fluid intake.
- **Text-to-Speech Alerts**:  
  - Uses the system's voice engine to audibly remind users to drink water.
- **Customizable Notification**:  
  - Includes a custom icon and message for a user-friendly experience.
- **Error Handling**:  
  - Robust exception handling ensures the application runs smoothly.

---

## Technologies Used

- Python 3
- plyer (for cross-platform desktop notifications)
- pywin32 (for Windows text-to-speech)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/employee-wellness-desktop-application.git
   cd employee-wellness-desktop-application
   ```
2. Install the required packages:
   ```bash
   pip install -r requirement.txt
   ```

---

## Usage

1. Run the application:
   ```bash
   python wellness_reminder.py
   ```
2. The application will send a desktop notification and play a voice reminder every 2 hours.
3. To stop the application, simply close the terminal or interrupt the process.

---

## File Structure

- `wellness_reminder.py`  
  Main script for sending notifications and voice reminders.
- `requirement.txt`  
  List of required Python packages.

---

## Example Notification

- **Title:** Please Drink Water
- **Message:** The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men.
- **Voice Alert:** "Please drink water now for your health"

---

## Skills Demonstrated

- Desktop automation and notifications in Python
- Integration of third-party libraries (plyer, pywin32)
- Exception handling and robust scripting
- Promoting workplace wellness through technology

---

## Contact

For any queries or collaboration opportunities, please reach out via GitHub or LinkedIn.

---

**Promote healthy habits and showcase your Python automation skills with this project!**
