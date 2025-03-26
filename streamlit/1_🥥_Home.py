import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon=":coconut:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.header("🪸 Share your contact info!")

st.subheader("About this App")
st.markdown("Going to a conference and want to share your contact info? Here's an easy way to create a QR code for reading a vCard (virtual business card) object and a website. I wanted to have the QR codes at hand so I updated a version of my phone's wallpaper by adding them in it. This way, I just swap the wallpapers whenever I want to share the information and other people can scan them. I also added the QR codes in my presentation's final slide. You can create a wearable pin, add it to your physical business card or have it printed in a shirt, I don't know. I just use it in my phone. Enjoy!")


st.subheader("How to Use")
st.markdown("In 🍉 **Generate vCard**, you will be prompted to input basic information to fill a vCard. Fill in as much as you want, though name and email are required. If you have a website, you can include it. Once finished, you can download the file it generates. In 🥭 **Generate QR Code**, you will see either one or two QR codes displayed, depending on wether or not you added a website")

st.subheader("Display it!")
st.markdown("Once you download the QR codes, you can create your own background for your phone and have it in there for an easy way to share your contact info")

col_left1, col_left2, col_center, col_right1, col_right2 = st.columns([1, 1, 2, 1, 1])  # Create three columns
with col_center:
    st.image(
        image="./streamlit/images/wallpaper_screenshot.png",
        caption="Screenshot of phone background as an idea to easily share the QR code",
        width=300
    )

st.subheader("How it works")
st.markdown("This Streamlit app generates vCards (Virtual Business Cards) based on user input. It uses the [vobject](https://github.com/py-vobject/vobject) and [qrcode](https://github.com/lincolnloop/python-qrcode) modules. I wanted to leverage an easy way to share a vCard during conferences instead of paper ones, so it was easier to create QR codes that everyone could scan. The QR codes can be added into your presentation slides or even as a phone background for easy sharing.")