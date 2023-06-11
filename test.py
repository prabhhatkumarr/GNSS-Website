import streamlit as st

# Define the available topics, their content, and associated image URLs
topics = {
    "Agri": {
        "content": "Information about agriculture",
        "image": r"Agri.jpg"
    },
    "Sky Plots": {
        "content": "Information about sky plots",
        "image": r"SkyPlot1.jpg"
    },
    # Add more topics, content, and image URLs as needed
}

# Render the introduction on the entry page
intro_placeholder = st.empty()
intro_placeholder.title("Welcome to the Knowledge Base!")
intro_placeholder.write("This website provides information on various topics. Please select a topic from the sidebar to learn more.")

# Render the sidebar with the topic buttons
st.sidebar.title("Topics")

# Check if a topic button is clicked
clicked_topic = None
for topic in topics:
    if st.sidebar.button(topic):
        clicked_topic = topic

# Clear the introduction section if a topic is clicked
if clicked_topic:
    intro_placeholder.empty()

    st.title(clicked_topic)
    # Style the topic font and align center
    st.markdown(f"<h2 style='font-family: Arial; text-align: center;'>{clicked_topic}</h2>", unsafe_allow_html=True)

    # Render the image with reduced size
    image_url = topics[clicked_topic]["image"]
    if image_url:
        st.image(image_url, width=300)  # Adjust the width as needed

    # Render the content
    content = topics[clicked_topic]["content"]
    st.write(content)
