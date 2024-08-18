import streamlit as st
import time

def generate_itinerary(address, days, people, q1, q2, q3):
    # Simulate a delay for processing
    time.sleep(10)
    
    # Create a mock itinerary
    itinerary = f"""
    **Itinerary for {people} people:**

    **Address:** {address}
    **Duration:** {days} days

    **Details:**
    - **Day 1:** Arrival at {address}. Explore local attractions.
    - **Day 2-{int(days) - 1}:** Various activities tailored for {people} people.
    - **Day {days}:** Departure.

    **Additional Information:**
    - **Question 1 Response:** {q1}
    - **Question 2 Response:** {q2}
    - **Question 3 Response:** {q3}
    """
    
    return itinerary


# First row of input fields
col1, col2, col3 = st.columns(3)

with col1:
    address = st.text_input("Destination")
with col2:
    days = st.number_input("How many days", min_value=1, step=1)
with col3:
    people = st.number_input("Number of people", min_value=1, step=1)

# Second row of input fields


q1 = st.text_area("Additional Question 1")

q2 = st.text_area("Additional Question 2")

q3 = st.text_area("Additional Question 3")

# Submit button and processing
if st.button("Submit"):
    with st.spinner("Generating itinerary..."):
        itinerary = generate_itinerary(address, days, people, q1, q2, q3)
        st.success("Itinerary generated successfully!")
        st.markdown(itinerary)
