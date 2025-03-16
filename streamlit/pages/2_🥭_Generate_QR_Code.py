import streamlit as st
import qrcode
import io
from PIL import Image

st.title("QR Code Generator")

if 'vcard_string' not in st.session_state or st.session_state.vcard_string is None:
    st.warning("Please generate a vCard first on the main page.")
else:
    qr_vcard = st.session_state.vcard_string.decode('utf-8')
    print("Retrieved vCard string:", qr_vcard)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=2,
    )

    bg = (255, 255, 255) # white
    fill = (0, 0, 0) # black

    qr.add_data(qr_vcard)
    qr.make(fit=True) #added fit = true to make sure the qr code is properly generated.
    img = qr.make_image(back_color=bg, fill_color=fill)

     # Convert PIL Image to bytes
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")  # Save as PNG
    img_bytes = img_bytes.getvalue()  # Get byte string

    st.image(img_bytes)  # Display the image as bytes

    st.download_button(
        label="Download QR Code",
        data=img_bytes,
        file_name="vcard_qrcode.png",
        mime="image/png",
    )