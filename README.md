# Final-Project-CS50P
Final project for CS50P Course with Harvard University

#### Video Demo: https://youtu.be/kUp-RuUJ1PE
#### Description:
The provided Python program is a comprehensive interactive console application that combines a to-do list manager, goal-setting functionality, a motivation program, and ASCII art for a personalized user experience. Let's break down the main components and functionalities of the program:

1. ToDoList Class:
The ToDoList class represents a to-do list manager. It includes the following attributes and methods:

Attributes:
tasks: A list to store tasks.
emoji_mapping: A dictionary mapping task keywords to corresponding emojis.
Methods:
__init__(self): Initializes an empty task list and the emoji mapping.
add_task(self, task): Adds a task to the to-do list, replacing words with corresponding emojis.
remove_task(self, task): Removes a task from the to-do list.
show_tasks(self): Displays the current tasks in a tabulated format.
2. Functions:
create_goal(): Takes user input to create a goal with a name, description, and deadline.
save_goals_to_csv(goals, file_path): Saves a list of goals to a CSV file and displays the content in a tabulated format.
choose_goal(user_name): Presents predefined goals, allows the user to choose one, and prompts for a deadline.
create_and_save_goal(): Allows the user to create and save multiple goals.
motivation_program(): Asks the user how they feel and provides motivational quotes based on their choice.
3. Main Program (main()):
Initializes a ToDoList object.
Greets the user with ASCII art and prompts for their name.
It presents a menu with options to choose a goal, create and save a goal, manage the to-do list, experience motivation, or quit.
Processes user choices and calls relevant functions.
4. Process Functions:
process_choose_goal(user_name, todo_list): Calls choose_goal() and adds the chosen goal to the to-do list.
process_create_and_save_goal(): Calls create_and_save_goal() function.
process_todo_list(todo_list): Allows the user to add, remove, or show tasks from the to-do list.
process_motivation_program(): Calls the motivation_program() function.
process_quit(user_name): Displays a goodbye message and ASCII art.
5. Execution:
The __main__ block initializes the program by calling the main() function.

6. Libraries Used:
The program utilizes several external libraries to enhance its functionality:

csv: Provides functionality to read and write CSV files.
art: Used for generating ASCII art from text.
re: Regular expression library for pattern matching.
tabulate: Used for formatting data into tables.
7. Goal Suggestions and Descriptions:
The choose_goal() function offers predefined goals and specific suggestions for achieving each goal. This adds a personalized touch by providing actionable steps based on the user's selection.

8. Goal Creation and Saving:
The create_and_save_goal() function allows users to create multiple goals interactively. The goals are then saved to a CSV file, providing persistence across program executions.

9. Motivation Program:
The motivation_program() function prompts users to express their feelings and responds with motivational quotes based on their emotional state. This feature adds a positive and supportive aspect to the program.

10. ASCII Art Greetings and Farewells:
The program incorporates ASCII art to dynamically generate personalized greetings and farewell messages for the user, enhancing the overall user experience.

11. Error Handling:
The program includes error handling mechanisms, such as checking for invalid input formats and providing appropriate error messages. For instance, when entering the deadline for a goal, the program validates the format to ensure it matches expected patterns.

12. User Interaction:
The program maintains an interactive loop, continually presenting the user with a menu of options until they choose to quit. This loop structure ensures a seamless and engaging user experience.

13. Code Organization:
The code is well-organized, with clear separation of concerns. Each class and function has a specific purpose, making the code modular and easy to understand. This design promotes code maintainability and extensibility.

14. User Interface:
The program provides a friendly and intuitive command-line interface, making it accessible for users who prefer a text-based environment. The use of ASCII art adds a visually appealing element to the interface.

15. Data Persistence:
Goals created by users are saved to a CSV file, allowing the program to retain user data across different sessions. This adds a practical and convenient aspect to the program.

Conclusion:
In summary, the Python program is not only a to-do list manager but also a goal-setting tool with motivational features. Its thoughtful design, interactive nature, and incorporation of external libraries contribute to a well-rounded and enjoyable user experience.It leverages external libraries like art for ASCII art and tabulate for table formatting. The code structure is well-organized, and user interactions are handled gracefully, making it a user-friendly and feature-rich console application.
