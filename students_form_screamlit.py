import streamlit as st

## Code by: Vesselee G.Flomo from the IT department @ Apex University


# Initialize persistent session state for database storage
if "saved_data" not in st.session_state:
    st.session_state.saved_data = {}

# Initialize session state for form inputs to allow clear/search refills
form_fields = [
    "first_name", "last_name", "gender", "email", "student_id", "department", "address", "contact",
    "father_first", "father_last", "father_address", "father_contact",
    "mother_first", "mother_last", "mother_address", "mother_contact", "search_id"
]
for field in form_fields:
    if field not in st.session_state:
        st.session_state[field] = ""

# Helper function to clear all form fields
def clear_fields():
    for field in form_fields:
        st.session_state[field] = ""

# --- APPLICATION HEADER & BANNER DESIGN ---
st.markdown(
    """
    <div style="background-color: orange; padding: 10px; text-align: center; width: 100%; border-radius: 5px; margin-bottom: 20px;">
        <h1 style="background-color: orange; color: white; font-family: Arial; font-weight: bold; font-size: 35px; margin: 0; padding: 15px; border-radius: 5px;">
            Student Detail Portal
        </h1>
    </div>
    """, 
    unsafe_allow_html=True
)

# Custom Label Styling Component
def blue_label(text):
    return f'<span style="background-color: blue; color: white; padding: 4px 8px; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;">{text}</span>'

# Use a centered structural layout constraint
main_layout, _ = st.columns([8, 1])

with main_layout:
    # Use TABS to reorganize the form positioning cleanly
    tab1, tab2, tab3 = st.tabs(["📋 Student Information; font-size:20px;", "👨‍👩‍👦 Parent Information; font-size:20px;", "🔍 Database Search Engine; font-size:20px;"])

    # --- TAB 1: STUDENT INFORMATION ---
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(blue_label("First Name"), unsafe_allow_html=True)
            first_name = st.text_input("First Name Label", value=st.session_state.first_name, label_visibility="collapsed", key="input_first")
            
            st.markdown(blue_label("Gender"), unsafe_allow_html=True)
            gender_options = ["", "Male", "Female"]
            idx_gender = gender_options.index(st.session_state.gender) if st.session_state.gender in gender_options else 0
            gender = st.selectbox("Gender Label", options=gender_options, index=idx_gender, label_visibility="collapsed", key="input_gender")
            
            st.markdown(blue_label("Student ID") + ' <span style="color: red; font-family: Arial; font-weight: bold; font-size: 14px;">(*) Numbers Only</span>', unsafe_allow_html=True)
            student_id_raw = st.text_input("ID Label", value=st.session_state.student_id, label_visibility="collapsed", key="input_id")
            if student_id_raw and not student_id_raw.isdigit():
                st.error("Validation Error: Student ID must contain numbers only.")
                student_id = ""
            else:
                student_id = student_id_raw

            st.markdown(blue_label("Address"), unsafe_allow_html=True)
            address = st.text_input("Address Label", value=st.session_state.address, label_visibility="collapsed", key="input_address")

        with col2:
            st.markdown(blue_label("Last Name"), unsafe_allow_html=True)
            last_name = st.text_input("Last Name Label", value=st.session_state.last_name, label_visibility="collapsed", key="input_last")
            
            st.markdown(blue_label("Email Address"), unsafe_allow_html=True)
            email = st.text_input("Email Label", value=st.session_state.email, label_visibility="collapsed", key="input_email")
            
            st.markdown(blue_label("Department"), unsafe_allow_html=True)
            dept_options = ["", "Civil Engineering", "Accountant", "Computer Science", "Nursing"]
            idx_dept = dept_options.index(st.session_state.department) if st.session_state.department in dept_options else 0
            department = st.selectbox("Dept Label", options=dept_options, index=idx_dept, label_visibility="collapsed", key="input_dept")
            
            st.markdown(blue_label("Contact"), unsafe_allow_html=True)
            contact = st.text_input("Contact Label", value=st.session_state.contact, label_visibility="collapsed", key="input_contact")

    # --- TAB 2: PARENT INFORMATION ---
    with tab2:
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown(blue_label("Father's First Name"), unsafe_allow_html=True)
            father_first = st.text_input("Father First Label", value=st.session_state.father_first, label_visibility="collapsed", key="input_f_first")
            
            st.markdown(blue_label("Address"), unsafe_allow_html=True)
            father_address = st.text_input("Father Addr Label", value=st.session_state.father_address, label_visibility="collapsed", key="input_f_addr")
            
            st.markdown(blue_label("Mother's First Name"), unsafe_allow_html=True)
            mother_first = st.text_input("Mother First Label", value=st.session_state.mother_first, label_visibility="collapsed", key="input_m_first")
            
            st.markdown(blue_label("Address"), unsafe_allow_html=True)
            mother_address = st.text_input("Mother Addr Label", value=st.session_state.mother_address, label_visibility="collapsed", key="input_m_addr")

        with col4:
            st.markdown(blue_label("Father's Last Name"), unsafe_allow_html=True)
            father_last = st.text_input("Father Last Label", value=st.session_state.father_last, label_visibility="collapsed", key="input_f_last")
            
            st.markdown(blue_label("Contact"), unsafe_allow_html=True)
            father_contact = st.text_input("Father Cont Label", value=st.session_state.father_contact, label_visibility="collapsed", key="input_f_cont")
            
            st.markdown(blue_label("Mother's Last Name"), unsafe_allow_html=True)
            mother_last = st.text_input("Mother Last Label", value=st.session_state.mother_last, label_visibility="collapsed", key="input_m_last")
            
            st.markdown(blue_label("Contact"), unsafe_allow_html=True)
            mother_contact = st.text_input("Mother Cont Label", value=st.session_state.mother_contact, label_visibility="collapsed", key="input_m_cont")

    # --- TAB 3: SEARCH SYSTEM ---
    with tab3:
        st.markdown("#### Search Records via ID Gateway")
        search_col1, search_col2 = st.columns([3, 1])
        
        with search_col1:
            search_id_raw = st.text_input("Search ID Input", value=st.session_state.search_id, label_visibility="collapsed", key="input_search")
            if search_id_raw and not search_id_raw.isdigit():
                st.error("Search Error: Student ID must be digits only.")
                search_id = ""
            else:
                search_id = search_id_raw

        with search_col2:
            if st.button("Search Database", use_container_width=True):
                if search_id.strip() == "":
                    st.error("Please enter Student ID to search.")
                elif search_id not in st.session_state.saved_data:
                    st.warning("No record found for this Student ID.")
                else:
                    record = st.session_state.saved_data[search_id]
                    for key in record:
                        st.session_state[key] = record[key]
                    st.session_state.search_id = search_id
                    st.success("Record loaded successfully! Head over to tabs to check data.")
                    st.rerun()

    # --- LOWER BASE ACTION PANEL ---
    st.markdown("---")
    
    # Custom Button Injection Styles
    st.markdown("""
        <style>
        div.stButton > button:first-child { font-weight: bold; color: blue!important; }
        div[data-testid="column"]::nth-of-type(1) button { background-color: green!important; border: 1px; }
        div[data-testid="column"]::nth-of-type(2) button { background-color: blue !important; border: 1px; }
        div[data-testid="column"]::nth-of-type(3) button { background-color: red !important; border: 1px; }
        </style>
    """, unsafe_allow_html=True)

    btn_col1, btn_col2, btn_col3 = st.columns(3)

    with btn_col1:
        if st.button("Submit Profile", use_container_width=True):
            if not first_name or not last_name or not student_id:
                st.error("Please fill in all required student fields.")
            elif not father_first or not mother_first:
                st.error("Please provide parent information.")
            else:
                st.session_state.saved_data[student_id] = {
                    "first_name": first_name, "last_name": last_name, "gender": gender, "email": email,
                    "student_id": student_id, "department": department, "address": address, "contact": contact,
                    "father_first": father_first, "father_last": father_last, "father_address": father_address, "father_contact": father_contact,
                    "mother_first": mother_first, "mother_last": mother_last, "mother_address": mother_address, "mother_contact": mother_contact
                }
                st.success("Details submitted successfully!")
                clear_fields()
                st.rerun()

    with btn_col2:
        if st.button("Update Profile", use_container_width=True):
            if not first_name or not last_name or not student_id:
                st.error("Please fill required fields before updating.")
            else:
                updated_payload = {
                    "first_name": first_name, "last_name": last_name, "gender": gender, "email": email,
                    "student_id": student_id, "department": department, "address": address, "contact": contact,
                    "father_first": father_first, "father_last": father_last, "father_address": father_address, "father_contact": father_contact,
                    "mother_first": mother_first, "mother_last": mother_last, "mother_address": mother_address, "mother_contact": mother_contact
                }
                if student_id in st.session_state.saved_data:
                    st.session_state.saved_data[student_id].update(updated_payload)
                    st.success("Data updated successfully!")
                    clear_fields()
                    st.rerun()
                else:
                    st.error("Student ID records do not exist to initiate updates.")

    with btn_col3:
        if st.button("Cancel", use_container_width=True):
            st.warning("Clear actions completed. Form wiped out safely.")
            clear_fields()
            st.rerun()
