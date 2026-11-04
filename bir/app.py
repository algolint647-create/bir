
import streamlit as st
from datetime import datetime
import html

st.set_page_config(
    page_title="Birthday Surprise 🎂",
    page_icon="🎁",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #16001f, #3b0754, #12001a);
    color: white;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    max-width: 650px;
    padding-top: 3rem;
}

.login-box {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 22px;
    padding: 30px;
    text-align: center;
    box-shadow: 0 0 30px rgba(255,0,150,0.15);
}

.logo {
    font-size: 42px;
    font-weight: bold;
    background: linear-gradient(45deg,#ff8a00,#e1306c,#833ab4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    color: #e8c9f5;
    font-size: 14px;
}

.birthday-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #ff9ad5;
    text-shadow: 0 0 20px #ff2f9c;
}

.birthday-card {
    background: rgba(255,255,255,0.09);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    margin-top: 20px;
}

.message {
    font-size: 18px;
    line-height: 1.8;
    color: #ffe4f4;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    border: none;
    background: linear-gradient(90deg,#ff8a00,#e1306c,#833ab4);
    color: white;
    font-weight: bold;
    padding: 12px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- LOGIN PAGE ----------------
if not st.session_state.unlocked:

    st.markdown("""
    <div class="login-box">
        <div class="logo">BirthdayGram ✨</div>
        <p class="subtitle">A little surprise is waiting for you...</p>
        <h3>🎁 Birthday Surprise Login</h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    with st.form("birthday_login"):

        username = st.text_input(
            "Username",
            placeholder="Enter your name"
        )

        password = st.text_input(
            "Demo password",
            type="password",
            placeholder="Enter anything you like"
        )

        st.caption(
            "This is an independent birthday demo, not Instagram. "
            "The password is not checked or stored."
        )

        submit = st.form_submit_button("Unlock Surprise 🎉")

        if submit:

            if username.strip():

                # Save username and submission metadata only.
                # Never save the password.
                safe_username = username.strip()

                with open("user_records.txt", "a", encoding="utf-8") as file:
                    file.write(
                        f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n"
                        f"Username: {safe_username}\n"
                        f"Password: [NOT STORED]\n"
                        f"Password field submitted: {'Yes' if password else 'No'}\n"
                        f"{'-' * 35}\n"
                    )

                st.session_state.username = safe_username
                st.session_state.unlocked = True
                st.rerun()

            else:
                st.warning("Please enter your username first ❤️")


# ---------------- BIRTHDAY SURPRISE ----------------
else:

    name = html.escape(st.session_state.username)

    st.balloons()

    st.markdown(
        f'<div class="birthday-title">Happy Birthday {name}! 🎂</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="birthday-card">
        <div style="font-size:65px;">🎉🎂🎁</div>
        <h2 style="color:#ff9ad5;">Your Special Day Is Here!</h2>
        <p class="message">
            Today is not just another day.<br>
            It's a celebration of YOU! ✨<br><br>
            May your life be filled with happiness,
            success, laughter and unforgettable memories.<br><br>
            Keep shining, keep smiling and never stop dreaming. 💜
        </p>
        <div style="font-size:35px;">🥳 🎈 💖 🎊</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.markdown(
        "<h3 style='text-align:center;color:#ffb6df;'>"
        "One more year, countless new possibilities! ✨"
        "</h3>",
        unsafe_allow_html=True
    )

    if st.button("Replay Surprise 🔁"):
        st.session_state.unlocked = False
        st.session_state.username = ""
        st.rerun()
