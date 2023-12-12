import streamlit as st

st.write("Welcome to my computer quiz")

a = st.text_input("Do You want to play? ").lower()
score = 0

if a.lower() !="yes":
    quit()
st.write("Okay! Let's Play :)")
answer = st.text_input("What is CPU stand for? ").lower()
if answer.lower() == "central processing unit":
    st.write('Correct!')
    score +=1
else:
    st.write('Incorrect!')
answer = st.text_input("What is GPU stand for? ").lower()
if answer.lower() == "graphic processing unit":
    st.write('Correct!')
    score += 1
else:
    st.write('Incorrect!')
answer = st.text_input("What is RAM stand for? ").lower()
if answer.lower() == "random access memory":
    st.write('Correct!')
    score += 1
else:
    st.write('Incorrect!')
answer = st.text_input("What is PSU stand for? ").lower()
if answer.lower() == "power supply":
    st.write('Correct!')
    score += 1
else:
    st.write('Incorrect!')
st.write("You got" + str(score) + "question correct!")
st.write("You got" + str((score/4)*100) + "%.")
