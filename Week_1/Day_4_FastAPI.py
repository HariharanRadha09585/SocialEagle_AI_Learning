'''

import fastapi
from fastapi import FastAPI

import streamlit as st

"""
# Test
appTest = FastAPI()

@appTest.get("/")
def read_root():
    return {"Hello": "World"}

@appTest.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
"""

st.title("FastAPI and Streamlit Integration")
st.write("This is a simple example of integrating FastAPI with Streamlit.")


st.header("FastAPI Endpoints")
st.write("You can define FastAPI endpoints and interact with them through Streamlit.")
st.subheader("Example Endpoint")
st.markdown("TEst..................")

name = st.text_input("Enter your name:")
#st.write(f"Hello, {name}!")

age = st.number_input("Enter your age:", min_value=0, max_value=120)
#st.write(f"You are {age} years old.")

#Button to submit the form
if st.button("Submit"):
    st.write(f"Hello, {name}! You are {age} years old.")

#Slider to select a number
number = st.slider("Select a number:", min_value=0, max_value=100)
st.write(f"You selected the number {number}.")

#Select box to choose an option
option = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
agree = st.checkbox("I agree to the terms and conditions.")
st.write(f"You selected: {option}")

#Showing messgaes 
st.success("This is a success message.")
st.info("This is an info message.")
st.warning("This is a warning message.")
st.error("This is an error message.")

'''
import streamlit as st


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="centered"
)


# -----------------------------
# Grade Calculation Function
# -----------------------------
def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


# -----------------------------
# Session State
# -----------------------------
# Create students list only once
if "students" not in st.session_state:
    st.session_state.students = []


# -----------------------------
# Title
# -----------------------------
st.title("🎓 Student Grade Manager")

st.write("Enter student details below to calculate and manage grades.")


# -----------------------------
# Student Form
# -----------------------------
with st.form("student_form"):

    name = st.text_input("Student Name")

    mark = st.number_input(
        "Student Mark",
        min_value=0,
        max_value=100,
        step=1
    )

    submit = st.form_submit_button("Add Student")


# -----------------------------
# Add Student
# -----------------------------
if submit:

    if name.strip() == "":
        st.error("Please enter the student's name.")

    else:

        grade = calculate_grade(mark)

        student = {
            "Name": name,
            "Mark": mark,
            "Grade": grade
        }

        st.session_state.students.append(student)

        st.success(f"{name} added successfully!")


# -----------------------------
# Display Students
# -----------------------------
st.subheader("Student Results")

if len(st.session_state.students) > 0:

    st.table(st.session_state.students)


    # -----------------------------
    # Class Statistics
    # -----------------------------

    marks = []

    for student in st.session_state.students:
        marks.append(student["Mark"])


    average_mark = sum(marks) / len(marks)

    highest_mark = max(marks)

    lowest_mark = min(marks)


    st.subheader("Class Statistics")


    col1, col2, col3 = st.columns(3)


    with col1:
        st.metric(
            label="Average",
            value=f"{average_mark:.2f}"
        )


    with col2:
        st.metric(
            label="Highest",
            value=highest_mark
        )


    with col3:
        st.metric(
            label="Lowest",
            value=lowest_mark
        )

else:

    st.info("No students added yet.")