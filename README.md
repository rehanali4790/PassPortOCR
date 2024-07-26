# PassPortOCR
An OCR designed to ectract the Bio data from the given picture for efficient and autonomous data entry

Passport OCR Application
Project by Rehan Ali
Contact: rehanalikhan4790@gmail.com

Overview
The Passport OCR Application is a powerful tool designed to extract and process information from passport images using Optical Character Recognition (OCR) technology. 
The application employs the passporteye library for MRZ (Machine Readable Zone) extraction and the easyocr library for character recognition. 
The entire process is facilitated through a user-friendly web interface built with Streamlit.

## Features
1. Image Upload: Users can upload passport images in JPG, JPEG, or PNG format.
2. MRZ Extraction: Extracts the MRZ from the uploaded passport image.
3. OCR Processing: Processes the extracted MRZ to obtain text data.
4. Data Parsing: Parses the extracted text to obtain structured data such as name, surname, gender, date of birth, nationality, passport number, issuing country, expiration date, and personal number.
5. Data Display: Displays the extracted and parsed data in a readable format.
6. Offline Operation: The application operates fully offline, ensuring no risk of data leakage as no external APIs are used.
7. Versatility: While primarily designed for passports, the OCR capabilities can be modified for other purposes, making it a versatile tool for various text recognition needs.

## Setup and Usage
**Prerequisites**
1. Python 3.8 or higher
2. Streamlit
3. easyocr
4. passporteye
5. OpenCV
6. Matplotlib
7. dateutil
8. Installation
9. Clone the repository:


git clone https://github.com/rehanali4790/PassPortOCR.git
cd PassPortOCR
Install the required packages:

pip install streamlit easyocr passporteye opencv-python-headless matplotlib python-dateutil
Run the Streamlit app:
streamlit run app.py

**Usage**
1. Open the Streamlit app in your web browser.
2. Upload a passport image by clicking on "Choose a passport image..." and selecting the image file (JPG, JPEG, or PNG format).
3. View the uploaded image displayed on the interface.
4. Wait for the processing to complete as the application extracts and parses the data.
5. View the extracted data displayed in a structured JSON format.

# Application in the Government Sector
## The Passport OCR Application can be a valuable tool in the government sector for various applications, including but not limited to:

1. Border Control and Immigration: Automating the process of reading and verifying passport information, reducing wait times, and increasing efficiency at border checkpoints.
2. Law Enforcement: Assisting in the identification of individuals during investigations and security operations.
3. Public Service Centers: Streamlining the process of passport verification in public service centers, ensuring quicker service delivery.
4. Travel and Tourism: Enhancing the check-in and boarding processes at airports and other travel hubs by automating passport data entry.
5. Healthcare: Facilitating the identification process in healthcare settings, especially for international patients.
6. By integrating the Passport OCR Application into various government departments, efficiency and security can be significantly improved, leading to better service delivery and more informed decision-making.

## Beyond Passport OCR
The OCR capabilities of this application are not limited to passports. The underlying technology can be adapted for various other purposes, such as:

* Driving Licenses: Extracting and processing information from driving licenses.
* ID Cards: Recognizing and extracting data from various types of identification cards.
* Documents: General document processing for extracting structured data from forms, letters, and other textual documents.
* This versatility makes the application a powerful tool for numerous text recognition and data extraction tasks across different domains.

For any queries or further assistance, please contact at rehanalikhan4790@gmail.com.

for demo video please visit this link https://www.linkedin.com/posts/rehan-ali-6a725924a_ocr-machinelearning-dataextraction-activity-7217439911614783489-wF2L?utm_source=share&utm_medium=member_desktop
