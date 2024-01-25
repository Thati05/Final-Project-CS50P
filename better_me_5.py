import csv
from art import text2art
import re
from tabulate import tabulate

class ToDoList:
    def __init__(self):
        # Initialize an empty list to store tasks and a mapping of tasks to emojis
        self.tasks = []
        self.emoji_mapping = {
            # Domestic work
            "Clean": "🧹",
            "Cook": "🍽️",
            "Laundry": "🧺",
            "Wash": "🧽",
            "House": "🏠 ",
            "Bathroom": "🚽",
            "Organizing": "🛋️",
            "Grocery": "🛒",
            "Dishwasher": "🚰",
            "Garden": "🌱",
            "Scrubbing": "🧼",
            "Fold": "🧺",
            "Bed": "🛏️",
            "Shower": "🚿",
            "Sweep": "🧹",
            "Tidying up": "🚪",
            "Trash": "🗑️",
            "Errands": "🚗",
            "Repairs": "🛠️",
            "Maintenance": "💡",

            # School
            "Books": "📚",
            "Note-taking": "📝",
            "Backpack": "🎒",
            "Planner": "📅",
            "Pens and pencils": "🖊️",
            "Reading": "📖",
            "Notebooks": "📓",
            "Computer": "🖥️",
            "Graduation": "🎓",
            "Classroom": "🏫",
            "Stationery": "📐",
            "Ruler": "📏",
            "Folders": "📁",
            "Homework": "📝",
            "Art supplies": "🎨",
            "Library": "📚",
            "Mathematics": "🧮",
            "Science": "🔬",
            "Organization": "🗂️",
            "Education": "🍎",

            # Male things
            "Sports": "🏀",
            "Gaming": "🎮",
            "Cars": "🚗",
            "DIY Projects": "🛠️",
            "Pizza": "🍕",
            "Music": "🎸",
            "Motorcycles": "🏍️",
            "hair grooming": "🧔",
            "Photography": "📸",
            "TV shows or movies": "📺",
            "Outdoor activities": "🏹",
            "Grilling": "🍔",
            "Gadgets": "🚁",
            "Video games": "🕹️",
            "Beverages": "🍺",
            "Camping": "🏞️",
            "Mountain biking": "🚵‍♂️",
            "Karaoke": "🎤",
            "Caps": "🧢",
            "Fitness": "🏋️‍♂️",

            # Female things
            "Nail care": "💅",
            "Makeup": "💄",
            "Fashion": "👗",
            "Accessories": "👛",
            "Beauty": "🌸",
            "Hair styling": "🎀",
            "Shopping": "🛍️",
            "Baking": "🍰",
            "Creative": "🎨",
            "Floral arrangements": "🌷",
            "Celebrations": "🎉",
            "Self-care": "💕",
            "Photography": "📸",
            "Music playlists": "🎵",
            "Reading": "📚",
            "Girls' night out": "🍹",
            "Ribbons and bows": "🎀",
            "Stationery": "💌",
            "Spa day": "🛀",
            "Desserts": "🍧",
        }

    def add_task(self, task):
         #Add a task to the to-do list, replacing words with corresponding emojis
        # Check if the task already exists to avoid duplicates
        task_lower = task.lower()
        if task_lower not in [t.lower() for t in self.tasks]:
            for word, emoji in self.emoji_mapping.items():
                task = task.replace(word.lower(), emoji)
                task = task.replace(word.capitalize(), emoji)
            self.tasks.append(task)
            print(f"Task '{task.capitalize()}' added to the to-do list.")
        else:
            print(f"Task '{task}' already exists in the to-do list.")

    def remove_task(self, task):
        # Remove a task from the to-do list
        task_lower = task.lower()
        original_task = task
        for word, emoji in self.emoji_mapping.items():
            task = task.replace(emoji.lower(), word.lower())
            task = task.replace(emoji.capitalize(), word.capitalize())
        if task_lower in [t.lower() for t in self.tasks]:
            self.tasks.remove(task)
            print(f"Task '{original_task}' removed from the to-do list.")
        else:
            print(f"Task '{original_task}' not found in the to-do list.")

    def show_tasks(self):
        # Display the current tasks in a tabulated format
        print("To-Do List:")
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            table_data = []
            for index, task in enumerate(self.tasks, start=1):
                table_data.append([index, task.capitalize()])

            headers = ["#", "Task"]
            table = tabulate(table_data, headers=headers, tablefmt="grid")
            print(table)


def create_goal():
    name = input("Name of goal: ").strip()
    description = input("How are you going to achieve the goal: ").strip()

    while True:
        try:
            deadline = input("When is the goal's deadline: ").strip()

            if re.match(r"^\d+ (minutes?|mins?|hours?|days?|weeks?|months?|years?)$", deadline, re.IGNORECASE):
                return {"Name": name, "Description": description, "Deadline": deadline}
            else:
                print("Invalid deadline format. Please use a format like '3 days', '2 weeks', etc.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def save_goals_to_csv(goals, file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Description", "Deadline"])
        for goal in goals:
            writer.writerow([goal["Name"], goal["Description"], goal["Deadline"]])

    with open(file_path, 'r') as read_file:
        data = [line.split(',') for line in read_file.readlines()]
        print(tabulate(data, headers="firstrow", tablefmt="grid"))
        

def choose_goal(user_name):
    goals = ["Improve physical fitness", "Learn a new skill or hobby", "Build stronger relationships", "Read more books", "Save money and budget wisely"]
    goal_suggestions = {
        "Improve physical fitness": "Start with a consistent exercise routine, such as walking or jogging, and gradually increase intensity. Consider incorporating strength training and flexibility exercises.",
        "Learn a new skill or hobby": "Explore your interests and pick up a new skill or hobby. You can take online courses, join local classes, or use tutorials to get started.",
        "Build stronger relationships": "Make an effort to connect with friends and family regularly. Plan social activities, listen actively, and express your thoughts and feelings openly.",
        "Read more books": "Set aside dedicated time for reading each day. Create a reading list, explore different genres, and consider joining a book club for discussion.",
        "Save money and budget wisely": "Create a budget to track your expenses and set financial goals. Cut unnecessary expenses, explore ways to increase income, and consider setting up an emergency fund."
    }
    while True:
        for index, goal in enumerate(goals, start=1):
            print(f"{index}. {goal}")

        try:
            choice = int(input(f"\n\nPlease choose the following goal you would like to achieve:  "))

            if 1 <= choice <= len(goals):
                selected_goal = goals[choice - 1]
                suggestion = goal_suggestions.get(selected_goal, "No specific suggestion available.")

                while True:
                    duration = input("When is the goal's deadline: ")

                    if re.match(r"^\d+ (minutes?|mins?|hours?|days?|weeks?|months?|years?)$", duration, re.IGNORECASE):
                        print(f"Great choice, {user_name}! Your goal is to {selected_goal.lower()}.\n\nYou can achieve the goal the following way: {suggestion}")
                        print(f"\nHere is a declaration:")
                        print(f"\nI, {user_name}, will {selected_goal.lower()} in {duration}!")
                        return {"Name": selected_goal, "Deadline": duration}
                    else:
                        print("Invalid deadline format. Please use a format like '3 days', '2 weeks', etc.")
            else:
                print("Invalid choice. Please select a valid goal number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def create_and_save_goal():
    goals = []
    while True:
        create_choice = input("Do you want to create a new goal? (yes/no): ").lower()
        if create_choice != 'yes':
            break

        goal = create_goal()
        goals.append(goal)

    csv_file_path = input("Enter the file name to save goals: ")
    save_goals_to_csv(goals, csv_file_path)

    print("Goals saved successfully!")

def motivation_program():
    feelings = {
        "Happy": " \n 1.'A happy heart makes the face cheerful, but heartache crushes the spirit.'~ King Solomon  \n\n 2.'Live life to the fullest, and focus on the positive.'~ Uknown \n\n 3.'Every good and perfect gift is from above, coming down from the Father of the heavenly lights, who does not change like shifting shadows.'~ James",
        "Sad": "\n 1.'The Lord is close to the brokenhearted and saves those who are crushed in spirit.' ~ King David \n\n 2.'Blessed are those who mourn, for they will be comforted.'~ Matthew\n\n 3.'He heals the brokenhearted and binds up their wounds.'~ King David",
        "Anxious" : "\n 1.'For the Spirit God gave us does not make us timid, but gives us power, love, and self-discipline.' ~Timothy \n\n 2.'Cast all your anxiety on him because he cares for you.'~ Peter\n\n 3.'So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand.'~ Prophet Isaiah",
        "Angry": "\n 1.'A person's wisdom yields patience; it is to one's glory to overlook an offense.' ~ King Solomon \n\n 2.'Refrain from anger and turn from wrath; do not fret—it leads only to evil.'~ King David\n\n 3.'A gentle answer turns away wrath, but a harsh word stirs up anger.'~ King Solomon",
    }

    print("How do you feel?")

    for index, emotion in enumerate(feelings, start=1):
        print(f"{index}. {emotion.capitalize()}")

    try:
        choice = int(input("Choose a number: "))
        if choice == 1:
            print(f"\n Great :), here are  words to make you feel even happier:\n{feelings['Happy']}")
        elif choice == 2:
            print(f"\n Oh no :( but here are words that will make you feel better:\n{feelings['Sad']}")
        elif choice == 3:
            print(f"\n Oh no :( but here are words that will make you feel better:\n{feelings['Anxious']}")
        elif choice == 4:
            print(f"\n Oh no :( but here are words that will make you feel better:\n{feelings['Angry']}")
        else:
            print("Invalid choice. Please choose 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
      # Initialize ToDoList and get user's name
    todo_list = ToDoList()

    user_name = input("Hello there :), What is your name?: ")
    ascii_art = text2art(f"Welcome  {user_name}!")
    print(ascii_art)

    while True:
        # Display menu options and process user's choice
        print("\nOptions:")
        print("1. Choose a Goal")
        print("2. Create and Save a Goal")
        print("3. To-Do List")
        print("4. Motivation")
        print("5. Quit")

        program_choice = input("Enter your choice (1-5): ").strip()

        if program_choice == "1":
            process_choose_goal(user_name, todo_list)
        elif program_choice == "2":
            process_create_and_save_goal()
        elif program_choice == "3":
            process_todo_list(todo_list)
        elif program_choice == "4":
            process_motivation_program()
        elif program_choice == "5":
            process_quit(user_name)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def process_choose_goal(user_name, todo_list):
    goal = choose_goal(user_name)
    todo_list.add_task(f"Achieve goal: {goal['Name']} by {goal['Deadline']}")

def process_create_and_save_goal():
    create_and_save_goal()

def process_todo_list(todo_list):
    todo_list_option = input("Do you want to:  \n 1. Add   \n 2. Remove  \n 3. Show tasks \n").lower()
    if todo_list_option == "1":
        task = input("Enter the task: ")
        todo_list.add_task(task)
    elif todo_list_option == "2":
        task = input("Enter the task to remove: ")
        todo_list.remove_task(task)
    elif todo_list_option == "3":
        todo_list.show_tasks()
    else:
        print("Invalid option for the to-do list. Please choose add, remove, or show.")

def process_motivation_program():
    motivation_program()

def process_quit(user_name):
    ascii_art = text2art(f"Goodbye, {user_name}!")
    print(ascii_art)
    print("  *****   *****")
    print(" ******* *******")
    print("  *************")
    print("   ***********")
    print("    *********")
    print("      *****")
    print("        *")

if __name__ == "__main__":
    main()

