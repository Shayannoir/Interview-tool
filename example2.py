import streamlit as st

st.title("Nested Buttons Example")

if 'show_second_button' not in st.session_state:
    st.session_state.show_second_button = False

if 'show_third_button' not in st.session_state:
    st.session_state.show_third_button = False

if 'show_reset_button' not in st.session_state:
    st.session_state.show_reset_button = False

if st.button("First Button"):
    st.session_state.show_second_button = True

if st.session_state.show_second_button:
    st.write("Revealed.")
    if st.button("Second Button"):
       st.session_state.show_third_button = True

if st.session_state.show_third_button:
    st.write("Second Revealed")
    if st.button("Third Button"):
       st.session_state.show_reset_button = True

if  st.session_state.show_reset_button:
    st.write("Third Revealed")
    if st.button("Reset"):
        st.session_state.show_third_button = False
        st.session_state.show_second_button = False
        st.session_state.show_reset_button = False
        st.rerun()
    

    


       
       


       



