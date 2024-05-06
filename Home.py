import streamlit as st
from PIL import Image
from pathlib import Path

# STREAMLIT PAGE CONFIG.

st.set_page_config(page_title='kimathi-grading', page_icon='🎯', layout="centered", initial_sidebar_state="collapsed")

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

logo = current_dir / "assets" / "logo.jpg"
logo = Image.open(logo)

st.header("kimathi-grading.")
st.image(logo, use_column_width=True)

task = st.selectbox("What do you wanna do?", ("Estimate my score.", "Set target(s)."))
st.write(" ")
st.selectbox("Which school are you in?", ("Engineering", "Computer Science and Information Technology", "Science"))
st.write(" ")
st.selectbox("Which department are you in?", ("Electrical/TIE", "Mechanical", "Civil"))
st.write(" ")
st.selectbox("What programme do you take?", ("BSc. TIE", "BSc. EEE", "BEd. EEE"))
st.write(" ")
st.selectbox("What's ur unit of interest?", ("Radio Frequency Circuits.", "Machine Learning.", "Digital Communication."))

# SESSION STATES.

if ("assignment_1_score", "assignment_2_score", "assignment_3_score", "cat_1_score", "cat_2_score", "cat_3_score", "lab_1_score", "lab_2_score","lab_3_score", "exam_score") not in st.session_state:
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


if task == "Estimate my score.":

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


input = st.expander(label=input_expander_label, expanded=True)

input.info("Enter scores as a percentage apart from the examination score e.g. if an assignment was marked out of 10 and you scored/think you will score/target to score 7 marks, drag the slider in red to 70.")
st.session_state.assignment_1_score = input.slider(label=assignment_1_label, min_value=0, max_value=100, step=1, value=0)
st.session_state.assignment_2_score = input.slider(label=assignment_2_label, min_value=0, max_value=100, step=1, value=0)
st.session_state.assignment_3_score = input.slider(label=assignment_3_label, min_value=0, max_value=100, step=1, value=0)

input.info("If a given assessment was never administered, kindly don't slide the bar pertaining to that assessment.")

st.session_state.cat_1_score = input.slider(label=cat_1_label, min_value=0, max_value=100, step=1, value=0)
st.session_state.cat_2_score = input.slider(label=cat_2_label, min_value=0, max_value=100, step=1, value=0)
st.session_state.cat_3_score = input.slider(label=cat_3_label, min_value=0, max_value=100, step=1, value=0)

st.session_state.lab_1_score = input.slider(label=lab_1_label, min_value=0, max_value=100, step=1, value=0, key="lab_1")
st.session_state.lab_2_score = input.slider(label=lab_2_label, min_value=0, max_value=100, step=1, value=0)
st.session_state.lab_3_score = input.slider(label=lab_3_label, min_value=0, max_value=100, step=1, value=0)

st.session_state.project_score = input.slider(label=project_label, min_value=0, max_value=100, step=1, value=0, disabled=st.session_state.lab_1, help="A lab and unit project are not administered together, drag the lab scores to 0 to enter project score(when project score is entered any lab marks will be ignored during calculation, the vice versa is TRUE). More about the Unit Project... some units do not have lab sessions, to ensure practical skills, a unit project is administered. It is also marked out of 15. ")

st.session_state.exam_score = input.slider(label=exam_label, min_value=0, max_value=70, step=1, value=0)

st.session_state.assignment_score = ((st.session_state.assignment_1_score + st.session_state.assignment_2_score + st.session_state.assignment_3_score)/3) * 0.05
st.session_state.cat_score = ((st.session_state.cat_1_score + st.session_state.cat_2_score + st.session_state.cat_3_score)/3) * 0.1

if st.session_state.lab_1:

    st.session_state.prac_score = ((st.session_state.lab_1_score + st.session_state.lab_2_score + st.session_state.lab_3_score) / 3) * 0.15

else:

    st.session_state.prac_score = st.session_state.project_score * 0.15

st.session_state.total_score = st.session_state.assignment_score + st.session_state.cat_score + st.session_state.prac_score + st.session_state.exam_score

#                 *--------------  GRADING --------------------------------------------*

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


if task == "Estimate my score.":

    st.success("Your total estimated score for that unit is: " + str(round(st.session_state.total_score, 1)) + " %. " + str(grade()))

else:

    st.success("Your target score for that unit is: " + str(round(st.session_state.total_score, 1)) + " %. " + str(grade()))

st.write(" ")
st.write(" ")
st.write(" ")
st.write("© kimathi-grading 2024.")
