# Create your own virtual business card

An easy way to create a QR code for reading a vCard object and a website. The outputs of this project are two QR codes: one containing your contact information in a vCard object and stored in a QR code and another containing the QR code for your website. 

# Folder structure
Three folders constitute this repository. 
* In ``scripts`` you will find the python files needed to create a vcf file and a QR code. 
* The folder ``tests`` contains Jupyter notebooks to test the scripts and store the files produced.
* ``files`` will have the output of the python scripts. 

## Create .vcf file and QR code
The ``vcard_generator.py`` file will create a .vcf file with your contact information once you replace the template with your actual values. It will also store your .vcf file and create a QR code that can be scanned to save your contact information.

## Create .png file with the QR code
I used the [python QR Code Generator](https://github.com/lincolnloop/python-qrcode) to create the png files.  
Running this script will generate a QR code for your website. 