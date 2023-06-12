import streamlit as st

# Set page config
st.set_page_config(page_title="Webpage Example", page_icon=":earth_americas:")

# Custom CSS
custom_css = """
<style>
:root {
    --sidebar-width: 200px;
    color: green;
}

/* Reduce the sidebar width */
.stSidebar > div:first-child {
    width: var(--sidebar-width);
}

/* Center align the headings */
h1, h2, h3, h4, h5, h6 {
    text-align: center;
    color: black;
}

/* Center align the images */
.stImage {
    display: block;
    margin-left: auto;
    margin-right: auto;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Topics")
topic = st.sidebar.radio("", ("Home", "Agri", "Sky Plots", "Contact Us"))

# Main content
st.title("Welcome!")

if topic == "Home":
    # st.header("Home")
    st.image("https://images.edexlive.com/uploads/user/imagelibrary/2020/5/14/original/25948_IITK_New.jpg")
    # st.write("This is the Home page.")

elif topic == "Agri":
    st.header("Agri")
    st.image("Agri.jpg")
    st.write("This is the Sites page. Here, you can find information about different sites.")

elif topic == "Sky Plots":
    st.header("Sky Plots")
    st.image("SkyPlot1.jpg")
    st.write("This is the Sky Plots page. Here, you can explore various sky plots.")

elif topic == "Contact Us":
    st.header("Contact Us")
    # st.image("contact_us_image.jpg")
    st.write("This is the Contact Us page. You can reach out to us through the provided contact details.")
