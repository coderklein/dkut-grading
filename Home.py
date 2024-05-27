import streamlit as st
from PIL import Image
from pathlib import Path
import json

# STREAMLIT PAGE CONFIG.

st.set_page_config(page_title='dkut-grading', page_icon='🎓', layout="centered", initial_sidebar_state="collapsed")

hide_streamlit_style = """ 
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# CSS.

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# LOGO.

logo = current_dir / "assets" / "dkut-grading.jpeg"
logo = Image.open(logo)

st.header("kimathi-grading.")
st.image(logo, use_column_width=True)

# -------------------------------------------------- VARIABLES ----------------------------------------------------------

# SESSION STATES.

if ("assignment_1_score", "assignment_2_score", "assignment_3_score", "cat_1_score", "cat_2_score", "cat_3_score",
    "lab_1_score", "lab_2_score", "lab_3_score", "exam_score") not in st.session_state:
    st.session_state["assignment_1_score"] = 0
    st.session_state["assignment_2_score"] = 0
    st.session_state["assignment_3_score"] = 0
    st.session_state["cat_1_score"] = 0
    st.session_state["cat_2_score"] = 0
    st.session_state["cat_3_score"] = 0
    st.session_state["lab_1_score"] = 0
    st.session_state["lab_2_score"] = 0
    st.session_state["lab_3_score"] = 0
    st.session_state["exam_score"] = 0
    st.session_state["assignment_score"] = 0
    st.session_state["cat_score"] = 0
    st.session_state["lab_score"] = 0
    st.session_state["total_score"] = 0


# -------------------------------------------- UDFs ---------------------------------------------------------------------

def labels():  # LABELS.

    global entry, input_expander_label, assignment_1_label, assignment_2_label, assignment_3_label, cat_1_label, cat_2_label, cat_3_label, lab_1_label, lab_2_label, lab_3_label, project_label, exam_label

    if task == "Estimate my score":

        input_expander_label = "Enter your assessment estimates/actual scores."
        assignment_1_label = "Enter/Estimate your Assignment 1's score as a percentage:"
        assignment_2_label = "Enter/Estimate your Assignment 2's score as a percentage:"
        assignment_3_label = "Enter/Estimate your Assignment 3's score as a percentage:"
        cat_1_label = "Enter/Estimate your CAT 1's percentage score:"
        cat_2_label = "Enter/Estimate your CAT 2's percentage score:"
        cat_3_label = "Enter/Estimate your CAT 3's percentage score:"
        lab_1_label = "Enter/Estimate your Lab 1's percentage score:"
        lab_2_label = "Enter/Estimate your Lab 2's percentage score:"
        lab_3_label = "Enter/Estimate your Lab 3's percentage score:"
        project_label = "Enter/Estimate your Unit Project's percentage score:"
        exam_label = "Enter/Estimate your Exam score as is e.g. out of 70:"

    else:

        input_expander_label = "Enter your assessment targets."
        assignment_1_label = "Set a target score for Assignment 1 as a percentage:"
        assignment_2_label = "Set a target score for Assignment 2 as a percentage:"
        assignment_3_label = "Set a target score for Assignment 3 as a percentage:"
        cat_1_label = "Set a target score for CAT 1 as a percentage:"
        cat_2_label = "Set a target score for CAT 2 as a percentage:"
        cat_3_label = "Set a target score for CAT 3 as a percentage:"
        lab_1_label = "Set a target score for Lab 1 as a percentage:"
        lab_2_label = "Set a target score for Lab 2 as a percentage:"
        lab_3_label = "Set a target score for Lab 3 as a percentage:"
        project_label = "Set a target score for the Unit Project as a percentage:"
        exam_label = "Set a target score for the Exam as is i.e. out of 70:"

    entry = st.expander(label=input_expander_label, expanded=True)

    return entry, input_expander_label, assignment_1_label, assignment_2_label, assignment_3_label, cat_1_label, cat_2_label, cat_3_label, lab_1_label, lab_2_label, lab_3_label, project_label, exam_label


def prac_inclusive():
    entry.info(
        "Enter scores as a percentage apart from the examination score e.g. if an assignment was marked out of 10 and you scored, think you will score or target to score 7 marks, drag the slider in red to 70.")
    st.session_state.assignment_1_score = entry.slider(label=assignment_1_label, min_value=0, max_value=100, step=1,
                                                       value=0)
    st.session_state.assignment_2_score = entry.slider(label=assignment_2_label, min_value=0, max_value=100, step=1,
                                                       value=0)
    st.session_state.assignment_3_score = entry.slider(label=assignment_3_label, min_value=0, max_value=100, step=1,
                                                       value=0)

    entry.info(
        "If a given assessment was never administered, kindly don't slide the bar pertaining to that assessment.")

    st.session_state.cat_1_score = entry.slider(label=cat_1_label, min_value=0, max_value=100, step=1, value=0)
    st.session_state.cat_2_score = entry.slider(label=cat_2_label, min_value=0, max_value=100, step=1, value=0)
    st.session_state.cat_3_score = entry.slider(label=cat_3_label, min_value=0, max_value=100, step=1, value=0)

    st.session_state.lab_1_score = entry.slider(label=lab_1_label, min_value=0, max_value=100, step=1, value=0,
                                                key="lab_1")
    st.session_state.lab_2_score = entry.slider(label=lab_2_label, min_value=0, max_value=100, step=1, value=0)
    st.session_state.lab_3_score = entry.slider(label=lab_3_label, min_value=0, max_value=100, step=1, value=0)

    st.session_state.project_score = entry.slider(label=project_label, min_value=0, max_value=100, step=1, value=0,
                                                  disabled=st.session_state.lab_1,
                                                  help="A lab and unit project are not administered together, drag the lab scores to 0 to enter project score(when project score is entered any lab marks will be ignored during calculation, the vice versa is TRUE). More about the Unit Project... some units do not have lab sessions, to ensure practical skills, a unit project is administered. It is also marked out of 15. ")

    st.session_state.exam_score = entry.slider(label=exam_label, min_value=0, max_value=70, step=1, value=0)

    st.session_state.assignment_score = ((
                                                     st.session_state.assignment_1_score + st.session_state.assignment_2_score + st.session_state.assignment_3_score) / 3) * 0.05
    st.session_state.cat_score = ((
                                              st.session_state.cat_1_score + st.session_state.cat_2_score + st.session_state.cat_3_score) / 3) * 0.1

    if st.session_state.lab_1:

        st.session_state.prac_score = ((
                                                   st.session_state.lab_1_score + st.session_state.lab_2_score + st.session_state.lab_3_score) / 3) * 0.15

    else:

        st.session_state.prac_score = st.session_state.project_score * 0.15

    st.session_state.total_score = st.session_state.assignment_score + st.session_state.cat_score + st.session_state.prac_score + st.session_state.exam_score

    return st.session_state.total_score


def prac_exclusive():
    entry.info(
        "Enter scores as a percentage apart from the examination score e.g. if an assignment was marked out of 10 and you scored, think you will score or target to score 7 marks, drag the slider in red to 70.")

    st.session_state.assignment_1_score = entry.slider(label=assignment_1_label, min_value=0, max_value=100, step=1,
                                                       value=0)
    st.session_state.assignment_2_score = entry.slider(label=assignment_2_label, min_value=0, max_value=100, step=1,
                                                       value=0)
    st.session_state.assignment_3_score = entry.slider(label=assignment_3_label, min_value=0, max_value=100, step=1,
                                                       value=0)

    entry.info(
        "If a given assessment was never administered, kindly don't slide the bar pertaining to that assessment.")

    st.session_state.cat_1_score = entry.slider(label=cat_1_label, min_value=0, max_value=100, step=1, value=0)
    st.session_state.cat_2_score = entry.slider(label=cat_2_label, min_value=0, max_value=100, step=1, value=0)
    st.session_state.cat_3_score = entry.slider(label=cat_3_label, min_value=0, max_value=100, step=1, value=0)

    st.session_state.exam_score = entry.slider(label=exam_label, min_value=0, max_value=70, step=1, value=0)

    st.session_state.assignment_score = ((
                                                     st.session_state.assignment_1_score + st.session_state.assignment_2_score + st.session_state.assignment_3_score) / 3) * 0.1
    st.session_state.cat_score = ((
                                              st.session_state.cat_1_score + st.session_state.cat_2_score + st.session_state.cat_3_score) / 3) * 0.2

    st.session_state.total_score = st.session_state.assignment_score + st.session_state.cat_score + st.session_state.exam_score

    return st.session_state.total_score


def grade():
    if 70 <= st.session_state.total_score <= 100:  # 70 -100

        return "That's an A."

    elif 60 <= st.session_state.total_score <= 69:  # 60 - 69

        return "That's a B."

    elif 50 <= st.session_state.total_score <= 59:  # 50 - 59

        return "That's a C."

    elif 40 <= st.session_state.total_score <= 49:  # 40 - 49

        return "That's a D."

    elif 0 <= st.session_state.total_score <= 39:  # 0 - 39

        return "That's an E."

    else:
        pass



def programme():

    global prac_inclusive_units, prac_exclusive_units, all_units

    program_finder_from_reg()

    if program == "":

        prac_inclusive_units = ""
        prac_exclusive_units = ""
        all_units = ""

    else:

        with open("programme_units.json") as db:

            programs = json.load(db)  # convert the json object to a Python dic.

        for key in programs:
            if key == program:
                prac_inclusive_units = programs[key][0]
                prac_exclusive_units = programs[key][1]

        all_units = []
        all_units.extend(prac_inclusive_units)
        all_units.extend(prac_exclusive_units)
        all_units.sort()

    return prac_inclusive_units, prac_exclusive_units, all_units


#-------------------------------------------------- APPLICATION --------------------------------------------------------

task = st.selectbox("I want to", ("Estimate a score for a given unit", "Set a target for a given unit"))
st.write(" ")

reg_no = st.text_input(label="Enter ur registration number, correctly.", placeholder="X000-00-0000/0000", help="The only info of interest is the programme code. It is not a bug when you don't have to enter your registration number in full in order to select a unit.")

def reg_no_programme_extractor():

    global reg_programme

    if reg_no == "":  # cater for error raised when no input is given to the reg no text input widget.

        reg_programme = ""

    else:
        reg_list = []

        for item in reg_no:
            reg_list.append(item)
        
        if len(reg_list) < 4:  # cater for invalid programme entered.
            reg_programme = "invalid"

        if len(reg_list) >= 4:
            reg_programme = reg_list[1:4]

    return reg_programme

def program_finder_from_reg(): # avail units based on info from reg no.

    global program

    reg_no_programme_extractor()

    if reg_programme == "":

        programme_from_reg_no = ""

    else:

        programme_from_reg_no = reg_programme[0] + reg_programme[1] + reg_programme[2]

    with open("programme_codes.json", "r") as codes:

        programme_codes = json.load(codes)

    for key in programme_codes:
        if key == programme_from_reg_no:
            program = programme_codes[key]
            break
        else:
            program = ""

    return program

unit = st.selectbox("What's ur unit of interest?", programme()[2], help="A valid registration number is required to avail units for each programme.")
st.write(" ")
st.write(" ")
st.write(" ")

find_exc = 0
find_inc = 0

while True:

    if find_exc >= len(prac_exclusive_units):
        break

    else:
        if unit == prac_exclusive_units[find_exc]:
            labels()
            prac_exclusive()
            break

        find_exc += 1

while True:

    if find_inc >= len(prac_inclusive_units):
        break

    else:
        if unit == prac_inclusive_units[find_inc]:
            labels()
            prac_inclusive()
            break

        find_inc += 1

if task == "Estimate my score":
    if unit != None:

        st.success(
            "Your total estimated score for the unit, " + unit + ", is: " + str(round(st.session_state.total_score, 1)) + " %. " + str(
                grade()))
    else:
        pass

else:

    if unit != None:
        st.success(
            "Your target score for the unit, " + unit + ", is: " + str(round(st.session_state.total_score, 1)) + " %. " + str(grade()))

    else:
        pass


st.write(" ")
st.write(" ")
st.write(" ")
st.write("© dkut-grading 2024.")
