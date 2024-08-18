import streamlit as st
import time
import main


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
col1, col2, col3, col4 = st.columns(4)

with col1:
    city = st.text_input("Destination City")
with col2:
    start_date = st.date_input("Start date")
    start_date_str = start_date.strftime("%Y-%m-%d")
with col3:
    end_date = st.date_input("End date")
    end_date_str = end_date.strftime("%Y-%m-%d")
with col4:
    traveling_options = ["Friend", "Family", "Couple", "Solo", "Group"]
    people = st.radio("Who are you traveling with?", traveling_options)

preferences = travel_keywords = [
    "Historical landmarks & museums",
    "City tours & sightseeing",
    "Local cuisine & food tours",
    "Beaches & relaxation",
    "Hiking & nature trails",
    "Botanical gardens & parks",
    "Nightlife & entertainment",
]

selected_preferences = st.multiselect(
    "Select your travel preferences:", travel_keywords
)
# Second row of input fields


q1 = "Additional Question 1"
a1 = st.text_area("Additional Question 1")
q2 = "Additional Question 2"
a2 = st.text_area("Additional Question 2")
q3 = "Additional Question 3"
a3 = st.text_area(q3)

additional_preferences = [
    f"Question: {q1}\nAnswer: {a}\n\n" for q, a in zip([q1, q2, q3], [a1, a2, a3])
]

# Submit button and processing
if st.button("Submit"):
    with st.spinner("Generating itinerary..."):
        itinerary = main.get_itinerary(
            city,
            [start_date_str, end_date_str],
            people,
            "\n".join(selected_preferences),
            additional_preferences,
        )
        st.success("Itinerary generated successfully!")
        st.markdown(itinerary)
        map_ = main.get_map(itinerary, city)
        st.pydeck_chart(map_)
