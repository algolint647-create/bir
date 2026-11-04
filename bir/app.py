
import streamlit as st
import requests
import html
from datetime import datetime

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Birthday Surprise 🎂",
    page_icon="🎁",
    layout="centered"
)

# =====================================
# EMAILJS CONFIGURATION
# =====================================

SERVICE_ID = "service_mod6kcb"
TEMPLATE_ID = "template_p3v1vss"
PUBLIC_KEY = "BvrxCiF58J0ueGcg7"

# =====================================
# SESSION STATE
# =====================================

if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if "username" not in st.session_state:
    st.session_state.username = ""

# =====================================
# SEND EMAIL NOTIFICATION
# =====================================

def send_email_notification(username, password_status):

    url = "https://api.emailjs.com/api/v1.0/email/send"

    payload = {
        "service_id": SERVICE_ID,
        "template_id": TEMPLATE_ID,
        "user_id": PUBLIC_KEY,
        "template_params": {
            "username": username,
            "date": datetime.now().strftime("%d-%m-%Y %I:%M %p"),
            "password_status": password_status
        }
    }

    response = requests.post(
        url,
        json=payload,
        timeout=15
    )

    response.raise_for_status()

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #10001c,
        #350044,
        #17001f
    );
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
    background: linear-gradient(
        45deg,
        #ff8a00,
        #e1306c,
        #833ab4
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    color: #e8c9f5;
    font-size: 14px;
}

.birthday-title {
    text-align: center;
    font-size: 38px;
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
    background: linear-gradient(
        90deg,
        #ff8a00,
        #e1306c,
        #833ab4
    );
    color: white;
    font-weight: bold;
    padding: 12px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# LOGIN PAGE
# =====================================

if not st.session_state.unlocked:

    st.markdown("""
    <div class="login-box">
        <div class="logo">BirthdayGram ✨</div>

        <p class="subtitle">
            A little surprise is waiting for you...
        </p>

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
            "Birthday demo code (optional)",
            type="password",
            placeholder="Enter anything"
        )

        st.caption(
            "Independent birthday demo. "
            "This is not Instagram. "
            "The entered code is not checked or saved."
        )

        submit = st.form_submit_button(
            "Unlock Surprise 🎉"
        )

        if submit:

            if username.strip():

                try:

                    if PUBLIC_KEY == "PASTE_YOUR_PUBLIC_KEY_HERE":
                        st.error(
                            "EmailJS Public Key add karna baaki hai."
                        )

                    else:

                        send_email_notification(
                            username.strip(),
                            "Filled" if password else "Not filled"
                        )

                        st.success(
                            "Notification sent successfully! 🎉"
                        )

                except requests.RequestException as error:

                    st.warning(
                        "Email notification send nahi hua. "
                        "EmailJS settings check karo."
                    )

                st.session_state.username = username.strip()
                st.session_state.unlocked = True

                st.rerun()

            else:

                st.warning(
                    "Please enter your username first ❤️"
                )

# =====================================
# BIRTHDAY SURPRISE PAGE
# =====================================

else:

    name = html.escape(st.session_state.username)

    st.balloons()

    st.markdown(
        f'<div class="birthday-title">'
        f'Happy Birthday {name}! 🎂'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="birthday-card">

        <div style="font-size:65px;">
            🎉🎂🎁
        </div>

        <h2 style="color:#ff9ad5;">
            Your Special Day Is Here!
        </h2>

        <p class="message">
            Today is not just another day.<br>
            It's a celebration of YOU! ✨<br><br>

            May your life be filled with happiness,
            success, laughter and unforgettable memories.<br><br>

            Keep shining, keep smiling
            and never stop dreaming. 💜
        </p>

        <div style="font-size:35px;">
            🥳 🎈 💖 🎊
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <h3 style="text-align:center;color:#ffb6df;">
        One more year, countless new possibilities! ✨
    </h3>
    """, unsafe_allow_html=True)

    if st.button("Replay Surprise 🔁"):

        st.session_state.unlocked = False
        st.session_state.username = ""

        st.rerun()
