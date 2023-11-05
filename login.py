import streamlit as st

# Custom CSS to inject into the Streamlit page
st.markdown(
    """
    <style>
    .login-box {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 5px 5px 5px #aaaaaa;
    }
    .login-button {
        background-color: #e60000;
        color: white;
        padding: 10px 24px;
        margin: 8px 0;
        border: none;
        cursor: pointer;
        width: 100%;
        opacity: 0.9;
        border-radius: 10px;
    }
    .login-button:hover {
        opacity: 1;
    }
    .stTextInput>div>div>input {
        color: #000;
        background-color: #FFF;
        border-radius: 5px;
        border: 1px solid #ced4da;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #e60000;
        color: white;
        padding: 10px 24px;
        margin: 8px 0;
        border: none;
    }
    .stButton>button:hover {
        background-color: #cc0000;
    }
    .agent-header, .customer-header {
        color: #CE0606;
        text-align: center;
        font-family: 'Inter', sans-serif;
        font-size: 60px;
        font-weight: 600;
        line-height: normal;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create the layout with columns
col1, col2 = st.columns([1, 1])

with col1:
    # Create a box for the Agent login form
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown('<h2 class="agent-header">Agent</h2>', unsafe_allow_html=True)
    agent_username = st.text_input("Username", key="agent_username")
    agent_password = st.text_input(
        "Password", type="password", key="agent_password")
    if st.button('Log In', key='agent_login'):
        # Perform login action
        st.write("Agent Login Clicked")  # Placeholder for actual login logic
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # Create a box for the Customer login form
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown('<h2 class="customer-header">Customer</h2>',
                unsafe_allow_html=True)
    customer_username = st.text_input("Username", key="customer_username")
    customer_password = st.text_input(
        "Password", type="password", key="customer_password")
    if st.button('Log In', key='customer_login'):
        # Perform login action
        # Placeholder for actual login logic
        st.write("Customer Login Clicked")
    st.markdown('</div>', unsafe_allow_html=True)

# Set background color
st.markdown(
    """
    <style>
    .stApp {
        background: #8c0000;
    }
    </style>
    """,
    unsafe_allow_html=True
)
