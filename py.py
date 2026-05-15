import streamlit as st
import pandas as pd

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Ahsan's Medicine Finder",
    page_icon="💊",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

.block-container {
    padding-top: 2rem;
}

.med-card {
    background-color: #111827;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #374151;
    margin-top: 15px;
}

.big-font {
    font-size:22px !important;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# MEDICINE DATABASE
# =========================================

medicine_data = {

    "paracetamol": {
        "Brand": "Panadol, Calpol",
        "Category": "Painkiller",
        "Used For": "Fever and pain relief",
        "Dose": "500mg every 4-6 hours",
        "Side Effects": "Nausea, liver damage in overdose",
        "Warning": "Do not exceed recommended dose",
        "Prescription": "No",
        "Pregnancy": "Generally safe in normal doses",
        "Storage": "Store below 25°C",
        "Interaction": "Avoid alcohol overdose",
        "Alternative": "Ibuprofen",
        "Rating": "4.7/5"
    },

    "ibuprofen": {
        "Brand": "Brufen, Advil",
        "Category": "NSAID",
        "Used For": "Pain, swelling, fever",
        "Dose": "200mg-400mg every 6-8 hours",
        "Side Effects": "Ulcers, stomach pain",
        "Warning": "Take after meals",
        "Prescription": "No",
        "Pregnancy": "Avoid in late pregnancy",
        "Storage": "Cool dry place",
        "Interaction": "Avoid with aspirin",
        "Alternative": "Paracetamol",
        "Rating": "4.5/5"
    },

    "amoxicillin": {
        "Brand": "Amoxil",
        "Category": "Antibiotic",
        "Used For": "Bacterial infections",
        "Dose": "250mg-500mg every 8 hours",
        "Side Effects": "Diarrhea, allergy",
        "Warning": "Complete full course",
        "Prescription": "Yes",
        "Pregnancy": "Usually safe",
        "Storage": "Away from moisture",
        "Interaction": "May affect birth control pills",
        "Alternative": "Azithromycin",
        "Rating": "4.6/5"
    },

    "cetirizine": {
        "Brand": "Zyrtec",
        "Category": "Antihistamine",
        "Used For": "Allergies and itching",
        "Dose": "10mg daily",
        "Side Effects": "Sleepiness",
        "Warning": "Avoid driving after taking",
        "Prescription": "No",
        "Pregnancy": "Consult doctor",
        "Storage": "Room temperature",
        "Interaction": "Avoid alcohol",
        "Alternative": "Loratadine",
        "Rating": "4.4/5"
    },

    "omeprazole": {
        "Brand": "Losec",
        "Category": "Acid Reducer",
        "Used For": "Acidity and ulcers",
        "Dose": "20mg before breakfast",
        "Side Effects": "Headache",
        "Warning": "Long use may reduce Vitamin B12",
        "Prescription": "No",
        "Pregnancy": "Consult doctor",
        "Storage": "Dry place",
        "Interaction": "May affect iron absorption",
        "Alternative": "Pantoprazole",
        "Rating": "4.3/5"
    },

    "metformin": {
        "Brand": "Glucophage",
        "Category": "Antidiabetic",
        "Used For": "Type 2 diabetes",
        "Dose": "500mg with meals",
        "Side Effects": "Diarrhea, weakness",
        "Warning": "Take with food",
        "Prescription": "Yes",
        "Pregnancy": "Doctor consultation required",
        "Storage": "Below 30°C",
        "Interaction": "Avoid excessive alcohol",
        "Alternative": "Insulin",
        "Rating": "4.6/5"
    },

    "salbutamol": {
        "Brand": "Ventolin",
        "Category": "Bronchodilator",
        "Used For": "Asthma and breathing issues",
        "Dose": "1-2 puffs when needed",
        "Side Effects": "Fast heartbeat",
        "Warning": "Overuse may worsen symptoms",
        "Prescription": "Yes",
        "Pregnancy": "Usually safe",
        "Storage": "Avoid heat",
        "Interaction": "Avoid overuse with caffeine",
        "Alternative": "Levalbuterol",
        "Rating": "4.5/5"
    },

    "atorvastatin": {
        "Brand": "Lipitor",
        "Category": "Cholesterol Medicine",
        "Used For": "Lower cholesterol",
        "Dose": "10mg daily",
        "Side Effects": "Muscle pain",
        "Warning": "Avoid grapefruit juice",
        "Prescription": "Yes",
        "Pregnancy": "Not recommended",
        "Storage": "Room temperature",
        "Interaction": "Avoid alcohol",
        "Alternative": "Rosuvastatin",
        "Rating": "4.4/5"
    },

    "aspirin": {
        "Brand": "Disprin",
        "Category": "Blood Thinner",
        "Used For": "Pain relief and blood thinning",
        "Dose": "75mg-325mg daily",
        "Side Effects": "Bleeding, stomach irritation",
        "Warning": "Avoid in ulcers",
        "Prescription": "No",
        "Pregnancy": "Consult doctor",
        "Storage": "Dry place",
        "Interaction": "Avoid with ibuprofen",
        "Alternative": "Clopidogrel",
        "Rating": "4.5/5"
    },

    "insulin": {
        "Brand": "Humulin",
        "Category": "Hormone",
        "Used For": "Control blood sugar",
        "Dose": "Doctor prescribed",
        "Side Effects": "Low blood sugar",
        "Warning": "Monitor glucose regularly",
        "Prescription": "Yes",
        "Pregnancy": "Usually safe",
        "Storage": "Refrigerated",
        "Interaction": "Alcohol may affect sugar levels",
        "Alternative": "Metformin",
        "Rating": "4.8/5"
    }
}

# =========================================
# SIDEBAR
# =========================================

st.sidebar.title("💊 Pro Medicine Finder")

menu = st.sidebar.radio(
    "Navigation",
    ["Search Medicine", "Medicine List", "Statistics", "About"]
)

# =========================================
# SEARCH PAGE
# =========================================

if menu == "Search Medicine":

    st.title("💊 Ahsan ki pharmacy")

    search = st.text_input(
        "Search Medicine",
        placeholder="Enter medicine name..."
    ).lower()

    st.caption("""
    💡 Popular Searches:
    paracetamol • ibuprofen • amoxicillin • cetirizine • omeprazole • metformin • insulin • salbutamol • atorvastatin • aspirin
    """)

    if search:

        if search in medicine_data:

            info = medicine_data[search]

            st.markdown(f"""
            <div class="med-card">
                <p class="big-font">{search.title()}</p>
            </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:
                st.info(f"🏷 Brand: {info['Brand']}")
                st.success(f"💊 Category: {info['Category']}")
                st.warning(f"📌 Used For: {info['Used For']}")
                st.write(f"💉 Dose: {info['Dose']}")
                st.write(f"⭐ Rating: {info['Rating']}")

            with col2:
                st.error(f"⚠ Side Effects: {info['Side Effects']}")
                st.write(f"🚫 Warning: {info['Warning']}")
                st.write(f"📄 Prescription Needed: {info['Prescription']}")
                st.write(f"🤰 Pregnancy: {info['Pregnancy']}")
                st.write(f"🧊 Storage: {info['Storage']}")

            st.subheader("Medicine Interaction")
            st.write(info["Interaction"])

            st.subheader("Alternative Medicine")
            st.write(info["Alternative"])

            st.progress(90)

        else:
            st.error("Medicine not found in database.")

# =========================================
# MEDICINE LIST PAGE
# =========================================

elif menu == "Medicine List":

    st.title("📋 Available Medicines")

    med_list = list(medicine_data.keys())

    df = pd.DataFrame({
        "Medicine": [m.title() for m in med_list]
    })

    st.dataframe(df, use_container_width=True)

# =========================================
# STATISTICS PAGE
# =========================================

elif menu == "Statistics":

    st.title("📊 Database Statistics")

    total = len(medicine_data)

    prescription_yes = sum(
        1 for m in medicine_data.values()
        if m["Prescription"] == "Yes"
    )

    prescription_no = total - prescription_yes

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Medicines", total)
    col2.metric("Prescription Medicines", prescription_yes)
    col3.metric("Non-Prescription", prescription_no)

    categories = {}

    for med in medicine_data.values():
        cat = med["Category"]
        categories[cat] = categories.get(cat, 0) + 1

    chart_df = pd.DataFrame({
        "Category": list(categories.keys()),
        "Count": list(categories.values())
    })

    st.bar_chart(chart_df.set_index("Category"))

# =========================================
# ABOUT PAGE
# =========================================

elif menu == "About":

    st.title("ℹ About")

    st.write("""
    ### Pro Medicine Finder

    Features:
    - Professional medicine database
    - Search system
    - Statistics dashboard
    - Medicine categories
    - Prescription checker
    - Pregnancy safety info
    - Drug interaction info
    - Alternative medicines
    - Ratings system

    ⚠ This application is for educational purposes only.
    Always consult a doctor before taking medicines.

    This app made by AHsan ch
    """)