



import random
import csv
import os
import time

questions = {
    "Mathematics": {
        "What is 2 + 2?\n (a)22 (b)4 (c)8\nAnswer: ": "b",
        "What is 5 * 6?\n (a)11 (b)56 (c)30 (d)1\nAnswer: ": "c",
        "What is 10 / 2?\n (a)3 (b)5 (c)12\nAnswer: ": "b",
        "What is the square root of 16?\n (a)4 (b)64 (c)36 (d)2\nAnswer: ": "a",
        "Solve for x: 3x + 7 = 22\n (a)10 (b)2 (c)5 (d)7\nAnswer: ": "c",
        "What is 12 - 7?\n (a)19 (b)5 (c)7\nAnswer: ": "b",
        "What is 7 * 8?\n (a)56 (b)64 (c)49\nAnswer: ": "a",
        "What is 15 % 4?\n (a)3 (b)4 (c)1\nAnswer: ": "a",
        "What is 9 ** 2?\n (a)81 (b)18 (c)92\nAnswer: ": "a",
        "What is 100 / 25?\n (a)2 (b)3 (c)4\nAnswer: ": "c"
    },
    "English": {
        "Which word is a noun?\n (a)Run (b)Happiness (c)Quickly\nAnswer: ": "b",
        "Choose the correct verb: She ____ to school.\n (a)go (b)goes (c)gone\nAnswer: ": "b",
        "What is the opposite of 'hot'?\n (a)cold (b)warm (c)heat\nAnswer: ": "a",
        "Which is a pronoun?\n (a)book (b)they (c)jump\nAnswer: ": "b",
        "Which is an adjective?\n (a)fast (b)run (c)happily\nAnswer: ": "a",
        "What is the plural of 'child'?\n (a)childs (b)children (c)childrens\nAnswer: ": "b",
        "Which is a preposition?\n (a)on (b)eat (c)dog\nAnswer: ": "a",
        "What is the past tense of 'go'?\n (a)goed (b)went (c)gone\nAnswer: ": "b",
        "Which sentence is correct?\n (a)She are happy (b)She is happy (c)She am happy\nAnswer: ": "b",
        "Which is a conjunction?\n (a)and (b)fast (c)happy\nAnswer: ": "a"
    },
    "Biology": {
        "What is the basic unit of life?\n (a)Cell (b)Atom (c)Organ\nAnswer: ": "a",
        "Which organ pumps blood?\n (a)Heart (b)Lung (c)Liver\nAnswer: ": "a",
        "What gas do plants release during photosynthesis?\n (a)Oxygen (b)Carbon dioxide (c)Nitrogen\nAnswer: ": "a",
        "Which vitamin is produced by sunlight?\n (a)A (b)D (c)C\nAnswer: ": "b",
        "What part of the plant makes food?\n (a)Root (b)Leaf (c)Stem\nAnswer: ": "b",
        "Which blood cells fight disease?\n (a)Red (b)White (c)Platelets\nAnswer: ": "b",
        "Where does digestion begin?\n (a)Mouth (b)Stomach (c)Small intestine\nAnswer: ": "a",
        "What is the powerhouse of the cell?\n (a)Nucleus (b)Mitochondria (c)Chloroplast\nAnswer: ": "b",
        "What transports water in plants?\n (a)Xylem (b)Phloem (c)Stem\nAnswer: ": "a",
        "Which blood type is universal donor?\n (a)A (b)B (c)O\nAnswer: ": "c"
    },
    "Chemistry": {
        "What is H2O?\n (a)Oxygen (b)Water (c)Hydrogen\nAnswer: ": "b",
        "What is NaCl?\n (a)Salt (b)Sugar (c)Acid\nAnswer: ": "a",
        "Atomic number of Carbon?\n (a)6 (b)8 (c)12\nAnswer: ": "a",
        "pH of neutral substance?\n (a)7 (b)0 (c)14\nAnswer: ": "a",
        "What is the chemical symbol for gold?\n (a)Au (b)Ag (c)Gd\nAnswer: ": "a",
        "Gas used in photosynthesis?\n (a)CO2 (b)O2 (c)N2\nAnswer: ": "a",
        "Most abundant gas in atmosphere?\n (a)Oxygen (b)Nitrogen (c)Carbon dioxide\nAnswer: ": "b",
        "What type of bond in water?\n (a)Ionic (b)Covalent (c)Metallic\nAnswer: ": "b",
        "Formula of methane?\n (a)CH4 (b)C2H6 (c)CO2\nAnswer: ": "a",
        "Process of liquid → gas?\n (a)Condensation (b)Evaporation (c)Melting\nAnswer: ": "b"
    },
    "Government": {
        "Which branch makes laws?\n (a)Executive (b)Legislative (c)Judiciary\nAnswer: ": "b",
        "Who is the head of state?\n (a)Governor (b)President (c)Minister\nAnswer: ": "b",
        "What is democracy?\n (a)Rule by one (b)Rule by few (c)Rule by people\nAnswer: ": "c",
        "Nigeria became independent in?\n (a)1960 (b)1970 (c)1980\nAnswer: ": "a",
        "What is constitution?\n (a)Laws (b)Supreme law (c)Policy\nAnswer: ": "b",
        "Who interprets laws?\n (a)Judiciary (b)Executive (c)Legislative\nAnswer: ": "a",
        "Local govt is closest to?\n (a)Federal (b)Community (c)State\nAnswer: ": "b",
        "Head of state govt?\n (a)Governor (b)President (c)Senator\nAnswer: ": "a",
        "What is suffrage?\n (a)Voting right (b)Rule (c)Court\nAnswer: ": "a",
        "Which organ enforces laws?\n (a)Executive (b)Judiciary (c)Legislative\nAnswer: ": "a"
    },
    "Economics": {
        "Study of scarce resources?\n (a)Biology (b)Economics (c)Chemistry\nAnswer: ": "b",
        "Which is a factor of production?\n (a)Land (b)Oxygen (c)Sunlight\nAnswer: ": "a",
        "Demand law: price ↑, demand?\n (a)Increase (b)Decrease (c)Constant\nAnswer: ": "b",
        "What is GDP?\n (a)Growth (b)Domestic product (c)Output\nAnswer: ": "b",
        "Money is a medium of?\n (a)Storage (b)Exchange (c)Production\nAnswer: ": "b",
        "Which is capital?\n (a)Machine (b)Water (c)Air\nAnswer: ": "a",
        "Market with 1 seller?\n (a)Monopoly (b)Oligopoly (c)Perfect\nAnswer: ": "a",
        "Who controls centrally planned economy?\n (a)Government (b)People (c)Firms\nAnswer: ": "a",
        "Unemployment means?\n (a)No education (b)No job (c)No house\nAnswer: ": "b",
        "Balance of trade = Export – ?\n (a)Import (b)Savings (c)Investment\nAnswer: ": "a"
    },
    "Commerce": {
        "Buying and selling is?\n (a)Commerce (b)Economics (c)Law\nAnswer: ": "a",
        "Which is not a means of transport?\n (a)Air (b)Road (c)Tree\nAnswer: ": "c",
        "Insurance spreads?\n (a)Profit (b)Risk (c)Loss\nAnswer: ": "b",
        "Wholesaler sells to?\n (a)Retailer (b)Consumer (c)Producer\nAnswer: ": "a",
        "Bank provides?\n (a)Money (b)Food (c)Clothes\nAnswer: ": "a",
        "Advertising creates?\n (a)Awareness (b)Hunger (c)Food\nAnswer: ": "a",
        "Cheque is a?\n (a)Money (b)Document (c)Risk\nAnswer: ": "b",
        "Import means?\n (a)Bring in (b)Send out (c)Save\nAnswer: ": "a",
        "Export means?\n (a)Send out (b)Bring in (c)Eat\nAnswer: ": "a",
        "Retailer sells to?\n (a)Consumer (b)Producer (c)Bank\nAnswer: ": "a"
    },
    "Literature": {
        "Author of 'Things Fall Apart'?\n (a)Achebe (b)Soyinka (c)Okigbo\nAnswer: ": "a",
        "Poetry is written in?\n (a)Prose (b)Verse (c)Drama\nAnswer: ": "b",
        "Play is for?\n (a)Stage (b)Book (c)Poem\nAnswer: ": "a",
        "Simile compares using?\n (a)Like/as (b)Is (c)Has\nAnswer: ": "a",
        "Drama involves?\n (a)Acting (b)Singing (c)Drawing\nAnswer: ": "a",
        "Fiction means?\n (a)True (b)Imaginary (c)Law\nAnswer: ": "b",
        "Sonnet has how many lines?\n (a)14 (b)12 (c)10\nAnswer: ": "a",
        "Prose means?\n (a)Poem (b)Novel (c)Play\nAnswer: ": "b",
        "Metaphor is?\n (a)Direct (b)Indirect comparison (c)Action\nAnswer: ": "b",
        "Epic is?\n (a)Short (b)Long poem (c)Novel\nAnswer: ": "b"
    },
    "CRS": {
        "Who led Israel out of Egypt?\n (a)Moses (b)David (c)Joseph\nAnswer: ": "a",
        "Who was crucified?\n (a)Paul (b)Jesus (c)Peter\nAnswer: ": "b",
        "Jesus fed ___ with 5 loaves?\n (a)5000 (b)2000 (c)1000\nAnswer: ": "a",
        "First man?\n (a)Adam (b)Moses (c)Noah\nAnswer: ": "a",
        "Ten Commandments on?\n (a)Stone (b)Paper (c)Wood\nAnswer: ": "a",
        "Who denied Jesus?\n (a)Peter (b)Paul (c)John\nAnswer: ": "a",
        "First miracle of Jesus?\n (a)Water to wine (b)Healing (c)Walking\nAnswer: ": "a",
        "Jesus was born in?\n (a)Nazareth (b)Bethlehem (c)Jerusalem\nAnswer: ": "b",
        "Mother of Jesus?\n (a)Mary (b)Elizabeth (c)Martha\nAnswer: ": "a",
        "Jesus rose on?\n (a)3rd day (b)2nd day (c)1st day\nAnswer: ": "a"
    },
    "IRS": {
        "Holy book of Islam?\n (a)Bible (b)Quran (c)Torah\nAnswer: ": "b",
        "Prophet of Islam?\n (a)Moses (b)Muhammad (c)Jesus\nAnswer: ": "b",
        "Prayer in Islam called?\n (a)Salat (b)Zakat (c)Hajj\nAnswer: ": "a",
        "Fasting month?\n (a)Shawwal (b)Ramadan (c)Hajj\nAnswer: ": "b",
        "Charity in Islam?\n (a)Salah (b)Zakat (c)Hajj\nAnswer: ": "b",
        "Pilgrimage to?\n (a)Jerusalem (b)Mecca (c)Medina\nAnswer: ": "b",
        "Friday prayer called?\n (a)Salat (b)Jummah (c)Eid\nAnswer: ": "b",
        "First pillar of Islam?\n (a)Shahada (b)Salat (c)Hajj\nAnswer: ": "a",
        "Direction of prayer?\n (a)East (b)Qibla (c)North\nAnswer: ": "b",
        "Islam means?\n (a)Peace (b)War (c)Rule\nAnswer: ": "a"
    }
}

RESULTS_FILE = "results.csv"
registered_students = {}

def save_results(name, matric,email, results, total, average):
    file_exists = os.path.isfile(RESULTS_FILE)

    with open(RESULTS_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            header = ["Name", "Matric", "Email"] + list(results.keys()) + ["Total", "Average"]
            writer.writerow(header)

        row = [name, matric,email] + [results.get(c, "N/A") for c in results] + [total, average]
        writer.writerow(row)
        
def login():
    email=input("Enter your email address: ")
    if email not in registered_students:
        print("Email not found... register first")
        return None, None
    password=input("Enter your password: ")
    if registered_students[email]["password"] != password:
        print("Incorrect password")
        return None, None
    return email, registered_students[email]

def register_student():
    name = input("Enter student  full name: ").strip()
    if name in registered_students:
        print("Student already exists.")
        return
    while True:
        email=input("Enter your email address: ")
        if '@'in email and email.endswith(".com"):
            if email in registered_students:
                print('Email already exist')
                return
            else:
                print("Valid email... continue the registration")
                break
        else:
            print("Invalid email, enter the correct email.")
            
        # for student in registered_students.values():
        #     if email[student] == email:
        #         print("Email already exist.")
        #         return
        
    matric = input("Enter matric number: ").strip()
    for student in registered_students.values():
        if student["matric"] == matric:
            print("Matric number already exists.")
            return
    password= input("Create a password: ")
    registered_students[email] = {"name":name,"matric": matric,"password":password, "courses": [], "scores": {}}
    print(f"{name} registered successfully!")

def register_courses():
    email, student= login()
    if not student:
        print("No students found. Register first.")
        return
    
    available_courses = list(questions.keys())
    print("\nAvailable Courses:")
    for i, course in enumerate(available_courses, 1):
        print(f"{i}. {course}")

    chosen_courses = []
    while len(chosen_courses) < 5:
        try:
            choice = int(input(f"Select course {len(chosen_courses)+1} (1-{len(available_courses)}): "))
            if 1 <= choice <= len(available_courses):
                course = available_courses[choice-1]
                if course not in chosen_courses:
                    chosen_courses.append(course)
                else:
                    print("Already selected.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter a number.")

    registered_students[email]["courses"] = chosen_courses
    print(f"{email} registered courses: {', '.join(chosen_courses)}")

def take_test():
    email, student= login()
    if not student:
        print("No students found. Register first.")
        return

    if not student["courses"]:
        print("You have not registered for any courses.")
        return

    for course in student["courses"]:
        if course in student["scores"]:
            print(f"Already completed {course}. Skipping...")
            continue
        ready=input("Are you ready to take the questions(yes/no):").strip().lower()
        if ready != 'yes':
            return

        print(f"\n--- {course} Test ---")
        score = 0
        random_questions = random.sample(list(questions[course].items()), 5)

        for q, correct in random_questions:
            answer = input(q).strip().lower()
            if answer == correct:
                score += 10

        student["scores"][course] = score
        print(f"{email}, you scored {score}/50 in {course}.")

    total = sum(student["scores"].values())
    average = total / len(student["scores"])
    save_results(student["name"], student["matric"], email,student["scores"], total, average)

def get_result():
    email, student= login()
    
    if not student:
        print("No students found. Register first.")
        return

    if not student["scores"]:
        print("No results yet.")
        return

    print(f"\n--- Results for {student['name']} ---")
    print(f"Matric Number: {student['matric']}")
    for course, score in student["scores"].items():
        print(f"{course}: {score}/50")

    total = sum(student["scores"].values())
    avg = total / len(student["scores"])
    print("-" * 30)
    print(f"TOTAL SCORE: {total}/{len(student['scores'])*100}")
    print(f"AVERAGE: {avg:.2f}%")

def main():
    while True:
        print("""
        WELCOME TO DESTINY GROUP OF SCHOOL
        1. Register Student
        2. Register Courses
        3. Take Test
        4. Get Result
        5. Exit
        """)

        option = input("Enter option (1-5): ").strip()
        if option == "1":
            register_student()
        elif option == "2":
            register_courses()
        elif option == "3":
            take_test()
        elif option == "4":
            get_result()
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
main()
