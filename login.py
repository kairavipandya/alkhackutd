import streamlit as st

# Function to create a login box


def create_login_box(user_type):
    st.subheader(user_type)
    username = st.text_input("Username", key=f"{user_type}_username")
    password = st.text_input(
        "Password", key=f"{user_type}_password", type="password")
    if st.button("Log In", key=f"{user_type}_login"):
        st.write(f"Login button clicked for {user_type}")
        # Here you would include the logic to validate the username and password


# Layout settings to divide the page into two columns
col1, col2 = st.columns(2)

with col1:
    create_login_box("Agent")

with col2:
    create_login_box("Customer")

# Assuming you may want to have a language selection or help link
st.sidebar.title("Settings")
st.sidebar.selectbox("Language", ["English", "Español"])
st.sidebar.text("Need help?")
