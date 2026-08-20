import streamlit as st

st.title("Lunch & Learn POC Builder")

st.header("Problem")

problem = st.text_input(
    "What problem are you solving?"
)

st.header("Hypothesis")

hypothesis = st.text_input(
    "What are you trying to prove?"
)

if st.button("Generate POC Summary"):

    st.success("POC defined!")

    st.write("### Problem")
    st.write(problem)

    st.write("### Hypothesis")
    st.write(hypothesis)