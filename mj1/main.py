import flet as ft
import json

users = []
current_user = {}

def load_users():
    with open("data.json", "r") as file:
        data = json.load(file)
    for user in data:
        users.append(user)

def save_users():
    with open("data.json", "w") as file:
        json.dump(users, file)
#use json file to save user and other data

def main(page:ft.Page):
    page.title = "The Super Dates"
    page.window.width = 1200
    page.window.height = 800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        image = ft.DecorationImage(
            src="background.jpeg",
            fit= ft.BoxFit.FILL
        )
    )
    page.scroll = ft.ScrollMode.ALWAYS

    load_users()
    def login_page():
        page.controls.clear()
        title = ft.Text("The Super Dates", size=28)
        username = ft.TextField(label="Username")
        password = ft.TextField(label="Password", password=True)
        message = ft.Text("")

        def login_click(e):
            found = False
            for user in users:
                if (user["username"] == username.value and user["password"] == password.value):
                    current_user.clear()
                    current_user["username"] = user["username"]
                    current_user["password"] = user["password"]
                    current_user["first_name"] = user["first_name"]
                    current_user["last_name"] = user["last_name"]
                    current_user["age"] = user["age"]
                    current_user["gender"] = user["gender"]
                    current_user["answers"] = user["answers"]
                    found = True
            if found == True:
                menu_page()
            else:
                message.value = "Account not found. Please try again."

        def go_register(e):
            register_page()
        page.add(
            ft.Column(
                controls=[
                    title,
                    username,
                    password,
                    ft.Button("Log In", on_click=login_click),
                    ft.Button("Register", on_click=go_register),
                    message
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    def register_page():
        page.controls.clear()
        title = ft.Text("Create an Account", size=24)
        username = ft.TextField(label="Username")
        password = ft.TextField(label="Password", password=True)
        first_name = ft.TextField(label="First Name")
        last_name = ft.TextField(label="Last Name")
        age = ft.TextField(label="Age")

        gender = ft.RadioGroup(
            content=ft.Column(
                controls=[
                    ft.Radio(value="Male", label="Male"),
                    ft.Radio(value="Female", label="Female"),
                    ft.Radio(value="Other", label="Other")
                ]
            )
        )
        message = ft.Text("")
        def register_click(e):
            if username.value == "" or password.value == "":
                message.value = "Please enter a username and password."
            elif (first_name.value == ""or last_name.value == ""or age.value == ""):
                message.value = "Please fill in all personal information."
            elif gender.value == None:
                message.value = "Please choose your gender."
            else:
                name_used = False
                for user in users:
                    if user["username"] == username.value:
                        name_used = True
                if name_used == True:
                    message.value = "This username is already used."
                else:
                    new_user = {
                        "username": username.value,
                        "password": password.value,
                        "first_name": first_name.value,
                        "last_name": last_name.value,
                        "age": age.value,
                        "gender": gender.value,
                        "answers": {}
                    }
                    users.append(new_user)
                    current_user.clear()
                    current_user["username"] = username.value
                    current_user["password"] = password.value
                    current_user["first_name"] = first_name.value
                    current_user["last_name"] = last_name.value
                    current_user["age"] = age.value
                    current_user["gender"] = gender.value
                    current_user["answers"] = {}
                    save_users()
                    menu_page()

        def go_login(e):
            login_page()
        page.add(
            ft.Column(
                controls=[
                    title,
                    username,
                    password,
                    first_name,
                    last_name,
                    age,
                    ft.Text("Gender"),
                    gender,
                    ft.Button("Create Account", on_click=register_click),
                    ft.Button("Back to Log In", on_click=go_login),
                    message
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    def menu_page():
        page.controls.clear()
        title = ft.Text("Welcome to The Super Dates", size=24)
        greeting = ft.Text(
            "Hello, " + current_user["first_name"] + "!"
        )
        def start_survey(e):
            question_page()
        def see_matches(e):
            match_page()
        def log_out(e):
            current_user.clear()
            login_page()
        page.add(
            ft.Column(
                controls=[
                    title,
                    greeting,
                    ft.Text("Find someone with similar interests!"),
                    ft.Button(
                        "Start / Update Questions",
                        on_click=start_survey
                    ),
                    ft.Button("View Matches", on_click=see_matches),
                    ft.Button("Log Out", on_click=log_out)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        
    def question_page():
        page.controls.clear()
        title = ft.Text("Personality and Interests Survey", size=22)
        q1 = ft.RadioGroup(
            content=ft.Column(
                controls=[
                    ft.Radio(value="Introvert", label="Introvert"),
                    ft.Radio(value="Extrovert", label="Extrovert"),
                    ft.Radio(value="Both", label="A bit of both")
                ]
            )
        )

        q2 = ft.RadioGroup(
            content=ft.Column(
                controls=[
                    ft.Radio(value="Sports", label="Sports"),
                    ft.Radio(value="Gaming", label="Gaming"),
                    ft.Radio(value="Music", label="Music"),
                    ft.Radio(value="Reading", label="Reading")
                ]
            )
        )

        q3 = ft.RadioGroup(
            content=ft.Column(
                controls=[
                    ft.Radio(value="Restaurant", label="Restaurant"),
                    ft.Radio(value="Movie", label="Movie"),
                    ft.Radio(value="Outdoor", label="Outdoor activity"),
                    ft.Radio(value="Home", label="Stay at home")
                ]
            )
        )

        q4 = ft.RadioGroup(
            content=ft.Column(
                controls=[
                    ft.Radio(value="Yes", label="Yes"),
                    ft.Radio(value="No", label="No")
                ]
            )
        )

        q5 = ft.RadioGroup(
            content=ft.Column(
                controls=[
                    ft.Radio(value="Yes", label="Yes"),
                    ft.Radio(value="No", label="No")
                ]
            )
        )

        q6 = ft.RadioGroup(
            content=ft.Column(
                controls=[
                    ft.Radio(value="Text", label="Text messages"),
                    ft.Radio(value="Phone", label="Phone calls"),
                    ft.Radio(value="In person", label="In person")
                ]
            )
        )

        q7 = ft.RadioGroup(
            content=ft.Column(
                controls=[
                    ft.Radio(value="Relax", label="Relax at home"),
                    ft.Radio(value="Go out", label="Go out with friends"),
                    ft.Radio(value="Sports", label="Play sports")
                ]
            )
        )

        q8 = ft.RadioGroup(
            content=ft.Column(
                controls=[
                    ft.Radio(value="Yes", label="Yes"),
                    ft.Radio(value="No", label="No")
                ]
            )
        )

        q9 = ft.RadioGroup(
            content=ft.Column(
                controls=[
                    ft.Radio(
                        value="Long-term",
                        label="Long-term relationship"
                    ),
                    ft.Radio(
                        value="Friendship first",
                        label="Friendship first"
                    ),
                    ft.Radio(
                        value="Getting to know people",
                        label="Still getting to know people"
                    )
                ]
            )
        )

        q10 = ft.RadioGroup(
            content=ft.Column(
                controls=[
                    ft.Radio(value="Yes", label="Yes"),
                    ft.Radio(value="No", label="No")
                ]
            )
        )

        question_groups = [
            q1, q2, q3, q4, q5,
            q6, q7, q8, q9, q10
        ]
        message = ft.Text("")

        def submit_survey(e):
            all_answered = True
            for group in question_groups:
                if group.value == None:
                    all_answered = False
            if all_answered == False:
                message.value = "Please answer all 10 questions."
            else:
                current_user["answers"] = {
                    "personality": q1.value,
                    "hobby": q2.value,
                    "date": q3.value,
                    "animals": q4.value,
                    "new_people": q5.value,
                    "communication": q6.value,
                    "weekend": q7.value,
                    "new_things": q8.value,
                    "relationship": q9.value,
                    "places": q10.value
                }
                for user in users:
                    if user["username"] == current_user["username"]:
                        user["answers"] = current_user["answers"]
                save_users()
                menu_page()
        def back_menu(e):
            menu_page()
        page.add(
             ft.Container(      
                content = ft.Column(
                    controls=[
                        title,
                        ft.Text("1. What is your personality?"),
                        q1,
                        ft.Text("2. What is your favourite hobby?"),
                        q2,
                        ft.Text("3. What is your ideal date?"),
                        q3,
                        ft.Text("4. Do you like animals?"),
                        q4,
                        ft.Text("5. Do you enjoy meeting new people?"),
                        q5,
                        ft.Text("6. How do you prefer to communicate?"),
                        q6,
                        ft.Text("7. What do you like doing on weekends?"),
                        q7,
                        ft.Text("8. Do you enjoy trying new things?"),
                        q8,
                        ft.Text("9. What kind of relationship do you want?"),
                        q9,
                        ft.Text("10. Do you like planning everything?"),
                        q10,
                        ft.Button("Save Answers", on_click=submit_survey),
                        ft.Button("Back to Menu", on_click=back_menu),
                        message
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                padding=10
             )
        )
    def match_page():
        page.controls.clear()
        title = ft.Text("Your Matches", size=24)
        results = ft.Column()
        current_answers = current_user["answers"]
        if len(current_answers) == 0:
            results.controls.append(
                ft.Text("Please complete the survey first.")
            )
        else:
            match_list = []
            for user in users:
                if user["username"] != current_user["username"]:
                    if user["gender"] != current_user["gender"]:
                        if int(user["age"]) >= int(current_user["age"])-5 or int(user["age"]) <= int(current_user["age"])+5:
                            if len(user["answers"]) > 0:
                                score = 0
                                other_answers = user["answers"]
                                if current_answers["personality"] == other_answers["personality"]:
                                    score = score + 1
                                if current_answers["hobby"] == other_answers["hobby"]:
                                    score = score + 1
                                if current_answers["date"] == other_answers["date"]:
                                    score = score + 1
                                if current_answers["animals"] == other_answers["animals"]:
                                    score = score + 1
                                if current_answers["new_people"] == other_answers["new_people"]:
                                    score = score + 1
                                if current_answers["communication"] == other_answers["communication"]:
                                    score = score + 1
                                if current_answers["weekend"] == other_answers["weekend"]:
                                    score = score + 1
                                if current_answers["new_things"] == other_answers["new_things"]:
                                    score = score + 1
                                if current_answers["relationship"] == other_answers["relationship"]:
                                    score = score + 1
                                if current_answers["places"] == other_answers["places"]:
                                    score = score + 1
                                match_list.append({
                                    "name": user["first_name"] + " " + user["last_name"],
                                    "username": user["username"],
                                    "score": score
                                })
            for i in range(len(match_list)):
                for j in range(i + 1, len(match_list)):
                    if match_list[j]["score"] > match_list[i]["score"]:
                        temp = match_list[i]
                        match_list[i] = match_list[j]
                        match_list[j] = temp

            if len(match_list) == 0:
                results.controls.append(
                    ft.Text("No matches found yet. Please check again later.")
                )
            else:
                results.controls.append(ft.Text("Your best match is:"))
                results.controls.append(
                    ft.Text(
                        match_list[0]["name"]
                        + " ("
                        + match_list[0]["username"]
                        + ")"
                    )
                )
                results.controls.append(
                    ft.Text(
                        "Compatibility: "
                        + str(match_list[0]["score"])
                        + "/10"
                    )
                )
                results.controls.append(ft.Text("All Matches:"))
                for match in match_list:
                    results.controls.append(
                        ft.Text(
                            match["name"]
                            + " ("
                            + match["username"]
                            + ") - "
                            + str(match["score"])
                            + "/10"
                        )
                    )
        def back_menu(e):
            menu_page()
        page.add(
            ft.Container(
                content = ft.Column(
                    controls=[
                        title,
                        results,
                        ft.Button("Back to Menu", on_click=back_menu)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        )


    login_page()
ft.run(main)
   
