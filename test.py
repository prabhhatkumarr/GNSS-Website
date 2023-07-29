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
topic = st.sidebar.radio("", ("Home", "AGRI", "HA11", "WLEO", "FAAP", "BUHJ", "MCPG", "NITW", "IHET", "Contact Us" ))

# Main content


if topic == "Home":
    st.title("Heterogenous Network of Low-Cost GNSS Receivers")
    st.image(r"I1.png")
    # st.write("This is the Home page.")

elif topic == "AGRI":
    st.header("Agricultural Plot(AGRI)")
    st.image("I2.png")
    st.write("This is the Sites page. Here, you can find information about different sites.")

elif topic == "HA11":
    st.header("Hall of Residence - XI")
    st.image("I3.png")
    st.write("Hall 11 Info")

elif topic == "WLEO":
    st.header("Western Lab Extension")
    st.image("I4.png")
    
elif topic == "FAAP":
    st.header("Faculty Apartment")
    st.image("I5.png")
    
elif topic == "BUHJ":
    st.header("Bundelkhand University, Jhansi, Uttar Pradesh")
    st.image("I6.png")
    
elif topic == "MCPG":
    st.header("Manas College, Pitthoragarh, Uttarakhand")
    st.image("I7.png")
    
elif topic == "NITW":
    st.header("National Institute of Technology, Warangal, Telangana")
    st.image("I8.png")
    
elif topic == "IHET":
    st.header("Institute of Hydropower Engineering and Technology, Tehri, Uttarakhand ")
    st.image("I9.png")

elif topic == "Contact Us":
    st.header("Contact Us")
    # st.image("contact_us_image.jpg")
    st.write("This is the Contact Us page. You can reach out to us through the provided contact details.")
