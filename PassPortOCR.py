import os
import string as st
from dateutil import parser
import matplotlib.image as mpimg
import cv2
from passporteye import read_mrz
import easyocr
import streamlit as st
import json
import warnings

warnings.filterwarnings("ignore")

# Function definitions
def parse_date(string, iob=True):
    date = parser.parse(string, yearfirst=True).date()
    return date.strftime('%d/%m/%Y')

def clean(string):
    return ''.join(i for i in string if i.isalnum()).upper()

def get_country_name(country_code):
    if '1' in country_code:
        country_code.replace('1', 'I')
    return country_code

def get_gender(code):
    if code in ['M', 'm', 'F', 'f']:
        sex = code.upper()
    elif code == '0':
        sex = 'M'
    else:
        sex = 'F'
    return sex

def print_data(data):
    for key in data.keys():
        info = key.replace('_', ' ').capitalize()
        print(f'{info}\t:\t{data[key]}')
    return

def get_data(img_name):
    reader = easyocr.Reader(['en'])
    user_info = {}
    new_im_path = 'tmp.png' # temp image path
    im_path = img_name

    # Crop image to Machine Readable Zone(MRZ)
    mrz = read_mrz(im_path, save_roi=True)

    if mrz:
        mpimg.imsave(new_im_path, mrz.aux['roi'], cmap='gray')

        # image manipulation
        img = cv2.imread(new_im_path)
        img = cv2.resize(img, (1110, 140))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image to grayscale to enhance the OCR process

        # remove < from mrz code
        allowlist = st.ascii_letters + st.digits + '< '
        code = reader.readtext(img, paragraph=False, detail=0, allowlist=allowlist)
        a, b = code[0].upper(), code[1].upper()

        if len(a) < 44:
            a = a + '<' * (44 - len(a))
        if len(b) < 44:
            b = b + '<' * (44 - len(b))

        # Split data to first name and surname
        surname_names = a[5:44].split('<<', 1)
        if len(surname_names) < 2:
            surname_names += ['']
        surname, names = surname_names

        # mapping data
        user_info['name'] = names.replace('<', ' ').strip().upper()
        user_info['surname'] = surname.replace('<', ' ').strip().upper()
        user_info['gender'] = get_gender(clean(b[20]))
        user_info['date_of_birth'] = parse_date(b[13:19])
        user_info['nationality'] = get_country_name(clean(b[10:13]))
        user_info['passport_type'] = clean(a[0:2])
        user_info['passport_number'] = clean(b[0:9])
        user_info['issuing_country'] = get_country_name(clean(a[2:5]))
        user_info['expiration_date'] = parse_date(b[21:27])
        user_info['personal_number'] = clean(b[28:42])
    else:
        st.error(f'Machine cannot read image {img_name}.')
        return None

    os.remove(new_im_path)

    return user_info

# Streamlit interface
st.title('Passport OCR Application')

uploaded_file = st.file_uploader("Choose a passport image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    img_path = os.path.join("tempDir", uploaded_file.name)
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.image(img_path, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Processing...")
    
    data = get_data(img_path)
    if data:
        st.write("Extracted Data:")
        st.json(data)
