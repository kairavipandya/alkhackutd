import streamlit as st

# Title and header layout
st.title("State Farm")
st.subheader("Small Business Assistant")

# Use columns to create a side-by-side layout
col1, col2 = st.columns(2)

with col1:
    # Display articles using expander or just markdown text
    st.markdown("### Articles")
    with st.expander("Flooring Contractor Insurance"):
        st.write("Why you need flooring contractor insurance...")
        # Add more content here

    with st.expander("Contractor Insurance"):
        st.write("Details about contractor insurance...")

    with st.expander("Worker's Compensation"):
        st.write("Information on worker's compensation...")

    with st.expander("Liability Umbrella"):
        st.write("Understanding liability umbrella insurance...")

with col2:
    # Appointments calendar and list
    st.markdown("### Appointments")
    # Simple calendar view (placeholder)
    st.write("Calendar Placeholder")

    # Appointment slots (placeholder)
    for i in range(8):  # Assuming there are 8 appointment slots
        st.write(f"9:15 - Appointment Slot {i+1}")

# Chatbox at the bottom (placeholder)
st.text_input("Type your message", key="message")

# Assuming there's a send button for the chat
st.button("Send")

# Additional components like login or search can be added as needed
