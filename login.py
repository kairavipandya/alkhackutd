import streamlit as st

# Add a title and header
st.title('State Farm')

# Create two columns for the Agent and Customer login forms
col1, col2 = st.columns(2)

with col1:
    st.header("Agent")
    agent_username = st.text_input("Username", key="agent_username")
    agent_password = st.text_input(
        "Password", type="password", key="agent_password")
    agent_login = st.button("Log In", key="agent_login")

    # Here you would handle the login logic for the agent
    if agent_login:
        st.write("Login logic for Agent")

with col2:
    st.header("Customer")
    customer_username = st.text_input("Username", key="customer_username")
    customer_password = st.text_input(
        "Password", type="password", key="customer_password")
    customer_login = st.button("Log In", key="customer_login")

    # Here you would handle the login logic for the customer
    if customer_login:
        st.write("Login logic for Customer")

# You could add additional functionality like handling logins, displaying messages, etc.
