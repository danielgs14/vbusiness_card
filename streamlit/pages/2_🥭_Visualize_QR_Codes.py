import streamlit as st
import qrcode
import io
from PIL import Image

st.title("🐙 Visualize your QR Code(s)")

st.markdown("This page will display the QR code(s) generated from the previous page. You can download the QR code(s) as PNG files.")

if 'vcard_string' not in st.session_state or st.session_state.vcard_string is None:
    st.warning("Please generate a vCard first on the main page.")
else:
    qr_vcard = st.session_state.vcard_string.decode('utf-8')
    website = st.session_state.get('website', None) # Get website or None

    st.header("vCard QR Code")

    qr_vcard_qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=2,
    )

    bg = (255, 255, 255)
    fill = (0, 0, 0)

    qr_vcard_qr.add_data(qr_vcard)
    qr_vcard_qr.make(fit=True)
    img_vcard = qr_vcard_qr.make_image(back_color=bg, fill_color=fill)

    img_vcard_bytes = io.BytesIO()
    img_vcard.save(img_vcard_bytes, format="PNG")
    img_vcard_bytes = img_vcard_bytes.getvalue()

    st.image(img_vcard_bytes)

    st.download_button(
        label="Download vCard QR Code",
        data=img_vcard_bytes,
        file_name="vcard_qrcode.png",
        mime="image/png",
    )

    if website:
        st.header("Website QR Code")

        qr_website_qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=2,
        )

        qr_website_qr.add_data(website)
        qr_website_qr.make(fit=True)
        img_website = qr_website_qr.make_image(back_color=bg, fill_color=fill)

        img_website_bytes = io.BytesIO()
        img_website.save(img_website_bytes, format="PNG")
        img_website_bytes = img_website_bytes.getvalue()

        st.image(img_website_bytes)

        st.download_button(
            label="Download Website QR Code",
            data=img_website_bytes,
            file_name="website_qrcode.png",
            mime="image/png",
        )

if st.button("Clear Cache for another entry!"):
    try:
        st.cache_data.clear()
        st.success("Streamlit's cache has been cleared.")
    except Exception as e:
        st.error(f"An error occurred while clearing the cache: {e}")