# import streamlit as st
# import pandas as pd
# from gliner import GLiNER

# # Load the fine-tuned GLiNER model
# model = GLiNER.from_pretrained("gretelai/gretel-gliner-bi-large-v1.0")

# # Define PII labels
# labels = [
#     "medical_record_number", "date_of_birth", "ssn", "date", "first_name", "email", "last_name",
#     "customer_id", "employee_id", "name", "street_address", "phone_number", "ipv4", "credit_card_number",
#     "license_plate", "address", "user_name", "device_identifier", "bank_routing_number", "date_time",
#     "company_name", "unique_identifier", "biometric_identifier", "account_number", "city",
#     "certificate_license_number", "time", "postcode", "vehicle_identifier", "coordinate", "country",
#     "api_key", "ipv6", "password", "health_plan_beneficiary_number", "national_id", "tax_id", "url",
#     "state", "swift_bic", "cvv", "pin"
# ]

# def detect_pii(text):
#     """Detect PII in a given text and return detected entities."""
#     entities = model.predict_entities(text, labels, threshold=0.7)
#     return entities

# def process_uploaded_file(file):
#     """Load tabular data and check for PII."""
#     if file.name.endswith('.csv'):
#         df = pd.read_csv(file)
#     elif file.name.endswith(('.xls', '.xlsx')):
#         df = pd.read_excel(file)
#     else:
#         st.error("Unsupported file format. Please upload a CSV or Excel file.")
#         return None
    
#     pii_detected = []
#     for col in df.columns:
#         for value in df[col].dropna().astype(str):
#             entities = detect_pii(value)
#             for entity in entities:
#                 pii_detected.append([value, entity['text'], entity['label'], col])
    
#     return df, pii_detected

# def main():
#     st.title("PII Detection in Text and Tabular Data -GlINER")
    
#     # File Upload Section
#     uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xls", "xlsx"])
    
#     # Text Input Section
#     user_text = st.text_area("Or paste a text snippet")
    
#     if uploaded_file:
#         df, pii_results = process_uploaded_file(uploaded_file)
#         if df is not None:
#             st.subheader("Uploaded Data")
#             st.write(df.head())
        
#             if pii_results:
#                 st.subheader("Detected PII in Tabular Data")
#                 pii_df = pd.DataFrame(pii_results, columns=["Original Value", "Detected PII", "Type", "Column"])
#                 st.dataframe(pii_df)
#             else:
#                 st.success("No PII detected in the uploaded dataset.")
    
#     if user_text:
#         pii_entities = detect_pii(user_text)
#         if pii_entities:
#             st.subheader("Detected PII in Text")
#             pii_text_df = pd.DataFrame(pii_entities, columns=["text", "label"])
#             st.dataframe(pii_text_df)
#         else:
#             st.success("No PII detected in the provided text.")

# if __name__ == "__main__":
#     main()




# import streamlit as st
# import pandas as pd
# from gliner import GLiNER

# # Load the fine-tuned GLiNER model
# model = GLiNER.from_pretrained("gretelai/gretel-gliner-bi-large-v1.0")

# # Define PII labels
# labels = [
#     "medical_record_number", "date_of_birth", "ssn", "date", "first_name", "email", "last_name",
#     "customer_id", "employee_id", "name", "street_address", "phone_number", "ipv4", "credit_card_number",
#     "license_plate", "address", "user_name", "device_identifier", "bank_routing_number", "date_time",
#     "company_name", "unique_identifier", "biometric_identifier", "account_number", "city",
#     "certificate_license_number", "time", "postcode", "vehicle_identifier", "coordinate", "country",
#     "api_key", "ipv6", "password", "health_plan_beneficiary_number", "national_id", "tax_id", "url",
#     "state", "swift_bic", "cvv", "pin"
# ]

# def detect_pii(text):
#     """Detect PII in a given text and return detected entities."""
#     entities = model.predict_entities(text, labels, threshold=0.7)
#     return entities

# def process_uploaded_file(file):
#     """Load tabular data and check for PII."""
#     if file.name.endswith('.csv'):
#         df = pd.read_csv(file)
#     elif file.name.endswith(('.xls', '.xlsx')):
#         df = pd.read_excel(file)
#     else:
#         st.error("Unsupported file format. Please upload a CSV or Excel file.")
#         return None, []
    
#     pii_detected = []
#     for col in df.columns:
#         for value in df[col].dropna().astype(str):
#             entities = detect_pii(value)
#             for entity in entities:
#                 pii_detected.append([value, entity['text'], entity['label'], col])
    
#     return df, pii_detected

# def main():
#     st.title("🔍 PII Detection in Text and Tabular Data")
    
#     # Selection between Text or Tabular Data
#     option = st.radio("Select input type:", ("Text", "Tabular Data"))
    
#     user_text, uploaded_file = None, None
    
#     if option == "Text":
#         user_text = st.text_area("Paste a text snippet")
#     else:
#         uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xls", "xlsx"])
    
#     if st.button("Detect PII"):
#         if option == "Text" and user_text:
#             pii_entities = detect_pii(user_text)
#             if pii_entities:
#                 st.warning("⚠️ **Personal Data Found!**")
#                 pii_text_df = pd.DataFrame(pii_entities, columns=["Detected PII", "Type"])
#                 st.dataframe(pii_text_df)
#             else:
#                 st.success("✅ No PII detected in the provided text.")
        
#         elif option == "Tabular Data" and uploaded_file:
#             df, pii_results = process_uploaded_file(uploaded_file)
#             if df is not None:
#                 st.subheader("📊 Uploaded Data Preview")
#                 st.dataframe(df.head())
                
#                 if pii_results:
#                     st.warning("⚠️ **Personal Data Found in the Dataset!**")
#                     pii_df = pd.DataFrame(pii_results, columns=["Original Value", "Detected PII", "Type", "Column"])
#                     st.dataframe(pii_df)
#                 else:
#                     st.success("✅ No PII detected in the uploaded dataset.")
#         else:
#             st.error("❌ Please provide input data for detection.")

# if __name__ == "__main__":
#     main()


import streamlit as st
import pandas as pd
from gliner import GLiNER

# Load the fine-tuned GLiNER model
model = GLiNER.from_pretrained("gretelai/gretel-gliner-bi-large-v1.0")

# Define PII labels
labels = [
    "medical_record_number", "date_of_birth", "ssn", "date", "first_name", "email", "last_name",
    "customer_id", "employee_id", "name", "street_address", "phone_number", "ipv4", "credit_card_number",
    "license_plate", "address", "user_name", "device_identifier", "bank_routing_number", "date_time",
    "company_name", "unique_identifier", "biometric_identifier", "account_number", "city",
    "certificate_license_number", "time", "postcode", "vehicle_identifier", "coordinate", "country",
    "api_key", "ipv6", "password", "health_plan_beneficiary_number", "national_id", "tax_id", "url",
    "state", "swift_bic", "cvv", "pin"
]

def detect_pii(text):
    """Detect PII in a given text and return detected entities."""
    entities = model.predict_entities(text, labels, threshold=0.7)
    return entities

def process_uploaded_file(file):
    """Load tabular data and check for PII."""
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.name.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file)
    else:
        st.error("Unsupported file format. Please upload a CSV or Excel file.")
        return None, []
    
    pii_detected = []
    for col in df.columns:
        for value in df[col].dropna().astype(str):
            entities = detect_pii(value)
            for entity in entities:
                pii_detected.append([value, entity['text'], entity['label'], col])
    
    return df, pii_detected

def main():
    st.title("🔍 PII Detection in Text and Tabular Data")
    
    # Selection between Text or Tabular Data
    option = st.radio("Select input type:", ("Text", "Tabular Data"))
    
    user_text, uploaded_file = None, None
    
    if option == "Text":
        user_text = st.text_area("Paste a text snippet")
    else:
        uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xls", "xlsx"])
    
    if st.button("Detect PII"):
        if option == "Text" and user_text:
            pii_entities = detect_pii(user_text)
            if pii_entities:
                st.warning("⚠️ **Personal Data Found!**")
                pii_data = [{"Detected PII": entity["text"], "Type": entity["label"]} for entity in pii_entities]
                pii_text_df = pd.DataFrame(pii_data)
                st.dataframe(pii_text_df)
            else:
                st.success("✅ No PII detected in the provided text.")
        
        elif option == "Tabular Data" and uploaded_file:
            df, pii_results = process_uploaded_file(uploaded_file)
            if df is not None:
                st.subheader("📊 Uploaded Data Preview")
                st.dataframe(df.head())
                
                if pii_results:
                    st.warning("⚠️ **Personal Data Found in the Dataset!**")
                    pii_df = pd.DataFrame(pii_results, columns=["Original Value", "Detected PII", "Type", "Column"])
                    st.dataframe(pii_df)
                else:
                    st.success("✅ No PII detected in the uploaded dataset.")
        else:
            st.error("❌ Please provide input data for detection.")
    st.markdown("---")
    st.markdown("© 2024 HM Team | HSAA")

if __name__ == "__main__":
    main()