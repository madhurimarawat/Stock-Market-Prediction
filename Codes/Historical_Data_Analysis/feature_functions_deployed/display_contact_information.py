# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

# Function to display team members' contact information in a column-wise format

def display_contact_information():

    # Define team member information as separate rows with transposed details
    team_members = [
        {
            "Name": "Madhurima Rawat",
            "Role": "Project Planner & Developer",
            "Responsibilities": "Project planning, managing GitHub repository, code documentation, setting up InfluxDB database, Grafana dashboard design, Streamlit deployment, Flask backend, styling and layout, data visualization and preprocessing of numerical data. Handled code integration for the Streamlit app.",
            "Tools": "GitHub, InfluxDB, Grafana, Streamlit, Python, Flask, Pandas, Matplotlib, Plotly",
            "GitHub": '<a href="https://github.com/madhurimarawat" target="_blank">GitHub</a>',
            "LinkedIn": '<a href="https://www.linkedin.com/in/madhurima-rawat/" target="_blank">LinkedIn</a>',
            "Email": '<a href="mailto:rawatmadhurima4@gmail.com" target="_blank">Email</a>',
            "Resume": '<a href="https://drive.google.com/file/d/1EYrjwt8p55lhdj78in0dio0IwTDdsPAL/view?usp=sharing" target="_blank">Resume</a>',
        },
        {
            "Name": "Geetanshu Dev Meshram",
            "Role": "Data Analyst & Backend Developer",
            "Responsibilities": "Model building for numerical data, basic Flask app design, created Power BI dashboard, and authored the official thesis documentation for the project.",
            "Tools": "Python, Flask, Power BI, Machine Learning libraries",
            "GitHub": '<a href="https://github.com/geetanshudev" target="_blank">GitHub</a>',
            "LinkedIn": '<a href="https://www.linkedin.com/in/geetanshu-dev-meshram-2b3b61240/" target="_blank">LinkedIn</a>',
            "Email": '<a href="mailto:meshramgeetanshudev@gmail.com" target="_blank">Email</a>',
            "Resume": '<a href="https://drive.google.com/file/d/1jnJFYVCFH-tUVdFWhkdTNCuRXH1rVGtu/view?usp=drive_link" target="_blank">Resume</a>',
        },
        {
            "Name": "Sneha Jha",
            "Role": "Data Analyst",
            "Responsibilities": "Processing text data, model building, hybrid model creation, developed real-time stock data prediction and visualization code, chatbot creation, and data fetching module.",
            "Tools": "NLP libraries, Machine Learning libraries, Hybrid Model Building",
            "GitHub": '<a href="https://github.com/Sneha100802" target="_blank">GitHub</a>',
            "LinkedIn": '<a href="https://www.linkedin.com/in/sneha-jha-808796261/" target="_blank">LinkedIn</a>',
            "Email": '<a href="mailto:jhasneha344@gmail.com" target="_blank">Email</a>',
            "Resume": '<a href="https://drive.google.com/file/d/1qMmiZ6y5QX0XRE--dNL9b-9TRIj4qMn3/view?usp=drive_link" target="_blank">Resume</a>',
        },
    ]

    # Display a brief summary of the team with names, LinkedIn profiles, and a description
    st.markdown("### Team Overview")
    st.markdown(
        "Our team consists of three passionate individuals who bring diverse skills to the table. "
        "We are focused on developing cutting-edge solutions in data analytics, backend development, and project management. "
        "Each team member plays a critical role in the success of the project, and we are excited to share our expertise and dedication."
    )

    # Explicitly written details for each team member with LinkedIn links
    st.markdown(
        "[Madhurima Rawat](https://www.linkedin.com/in/madhurima-rawat/) : &nbsp; Project Planner & Developer specialized in Project planning, managing GitHub repository, setting up InfluxDB database, Grafana dashboard design, Streamlit deployment, Flask styling and layout, data visualization and preprocessing of numerical data. Tools: GitHub, InfluxDB, Grafana, Streamlit, Python, Flask, Pandas, Matplotlib, Plotly"
    )
    st.markdown(
        "[Geetanshu Dev Meshram](https://www.linkedin.com/in/geetanshu-dev-meshram-2b3b61240/) :  &nbsp; Data Analyst & Backend Developer specialized in Model building for numerical data, basic Flask app design. Tools: Python, Flask, Machine Learning libraries"
    )
    st.markdown(
        "[Sneha Jha](https://www.linkedin.com/in/sneha-jha-808796261/) :  &nbsp; Data Analyst specialized in Processing text data, model building, and hybrid model building. Tools: NLP libraries, Hybrid Model Building"
    )

    st.markdown("---")

    # HTML Table with centered content and reduced width
    html_table = f"""
    <table style="width: 80%; border: 1px solid black; border-collapse: collapse; margin-left: auto; margin-right: auto;">
        <tr>
            <th style="padding: 8px; text-align: center;"><i class="fas fa-id-card"></i> &nbsp; Name</th>
            <th style="padding: 8px; text-align: center;">Madhurima Rawat</th>
            <th style="padding: 8px; text-align: center;">Geetanshu Dev Meshram</th>
            <th style="padding: 8px; text-align: center;">Sneha Jha</th>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fas fa-user-tie"></i> &nbsp; <strong>Role</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['Role']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['Role']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['Role']}</td>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fas fa-tasks"></i> &nbsp; <strong>Responsibilities</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['Responsibilities']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['Responsibilities']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['Responsibilities']}</td>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fas fa-tools"></i> &nbsp; <strong>Tools</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['Tools']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['Tools']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['Tools']}</td>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fab fa-github"></i> &nbsp;<strong>GitHub</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['GitHub']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['GitHub']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['GitHub']}</td>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fab fa-linkedin"></i> &nbsp;<strong>LinkedIn</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['LinkedIn']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['LinkedIn']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['LinkedIn']}</td>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fas fa-envelope"></i> &nbsp;<strong>Email</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['Email']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['Email']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['Email']}</td>
        </tr>
        <tr>
            <td style="padding: 8px; text-align: center;"><i class="fas fa-scroll"></i> &nbsp;<strong>Resume</strong></td>
            <td style="padding: 8px; text-align: center;">{team_members[0]['Resume']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[1]['Resume']}</td>
            <td style="padding: 8px; text-align: center;">{team_members[2]['Resume']}</td>
        </tr>

    </table>
    """

    # Render the table
    st.markdown(html_table, unsafe_allow_html=True)

