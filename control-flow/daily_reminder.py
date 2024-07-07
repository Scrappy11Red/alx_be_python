#To prompt the user to input a task description
task = input("Enter your task: ")

#To prompt for the task’s priority
priority = input("Priority (high/medium/low): ").lower()

#To ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

#To provide a customized reminder based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the reminder
print(f"Reminder: {reminder}")