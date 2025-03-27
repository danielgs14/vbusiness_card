import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon=":coconut:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.header("🪸 Create your vCard!")

st.subheader("About this project")
st.markdown("Going to a conference and want to share your contact info? Here's an easy way to create a QR code for reading a vCard (virtual business card) object and a website. Instead of relying on paper business cards for conferences and events, I wanted to have QR codes at hand so that people could scan and get my contact info. I updated a version of my phone's wallpaper by adding them in it. This way, I just swap the wallpapers whenever I want to share the information and other people can scan them. I also added the QR codes in my presentation's final slide. You can create a wearable pin, add it to your physical business card or have it printed in a shirt, I don't know. I just use it in my phone. Enjoy!")


st.subheader("How to Use")
st.markdown("In 🍉 **Generate vCard**, you will be prompted to input basic information to fill a vCard. Fill in as much as you want, though name and email are required. If you have a website, you can include it. Once finished, you can download the file it generates, a .vcf file. In 🥭 **Visualize QR Codes**, you will see either one or two QR codes displayed, depending on wether or not you added a website.")

st.subheader("Display it!")
st.markdown("Once you download the QR codes, you can create your own background for your phone and have it in there for an easy way to share your contact info")

col_left1, col_left2, col_center, col_right1, col_right2 = st.columns([1, 1, 2, 1, 1])  # Create three columns
with col_center:
    st.image(
        "https://i.imgur.com/bcGZVBE.png",
        caption="Screenshot of phone background as an idea to easily share the QR code",
        width=300
    )

st.subheader("How it works")
st.markdown("This Streamlit app generates vCards (Virtual Business Cards) based on your input. It uses the [vobject](https://github.com/py-vobject/vobject) and [qrcode](https://github.com/lincolnloop/python-qrcode) modules to create a .vcf file and then create a QR code in PNG format. It is important to note that **no information you enter is logged**. I think Streamlit only logs app views and stuff useful for debugging, but anything added into the text boxes isn't stored.")