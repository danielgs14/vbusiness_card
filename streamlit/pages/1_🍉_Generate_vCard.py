import streamlit as st
from utils.vcard_helper import cardgenerator

if 'vcard_string' not in st.session_state:
    st.session_state.vcard_string = None

st.set_page_config(
    page_title="vCard Generator",
    page_icon=":coconut:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("vCard Generator")
st.markdown("Add your information below to generate a vCard.")

st.header("Contact Information")

# Input fields for user data
name = st.text_input("Name", placeholder="Your Full Name")
title = st.text_input("Title", placeholder="Principal Investigator at [name] lab")
organization = st.text_input("Organization", placeholder="Your affiliation")
email = st.text_input("Email", placeholder="your.email@example.com")
phone = st.text_input("Phone", placeholder="Remember to add area code (+nnn) if needed")
website = st.text_input("Website", placeholder="www.example.com")
# address = st.text_area("Address", placeholder="123 Main Street, Anytown, CA 91234")
# linkedin = st.text_input("LinkedIn Profile URL", placeholder="linkedin.com/in/johndoe")
# github = st.text_input("GitHub Profile URL", placeholder="github.com/johndoe")
# twitter = st.text_input("Twitter Profile URL", placeholder="twitter.com/johndoe")
# Add other social media or fields as needed

if st.button("Generate vCard"):
    if not name or not email:
        st.error("Name and Email are required fields.")
    else:
        try:
            vcard = cardgenerator(
                name=name,
                title=title,
                organization=organization,
                email=email,
                phone=phone,
                website=website
                # address=address,
                # linkedin=linkedin,
                # github=github,
                # twitter=twitter,
            )
            vcard_string = vcard.generate_vcard()
            print("Generated vCard string:", vcard_string)
            st.session_state.vcard_string = vcard_string.encode('utf-8')
            st.session_state.website = website

            st.download_button(
                label="Download vCard",
                data=vcard_string,
                file_name=f"{name.replace(' ', '_')}_vcard.vcf",
                mime="text/vcard",
            )
            st.success("vCard generated successfully!")

        except Exception as e:
            st.error(f"An error occurred: {e}")