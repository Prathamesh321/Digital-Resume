import streamlit as st
from pathlib import Path

st.set_page_config(page_title='Digital CV | Prathamesh Udawant')

out_col1,out_col2=st.columns([0.69,0.3],gap='small')

with st.container():
    with out_col1:
        st.title('Prathamesh Gajendra Udawant')
        in_col1,in_col2=st.columns([2,1])

        with in_col1:
            st.write('✉ prathameshudawant@gmail.com')
            st.write('🏠 Nashik,Maharashtra') 
            

        with in_col2:
            st.write('📱 8208949239')
            st.write('🔗 [Linkedin](www.linkedin.com/in/prathamesh-udawant-profile)')

    
    with out_col2:
        st.image('C:/Streamlit_practice/Resume Build/images/my_pic.png',width=200)

st.divider()

st.subheader('**:green[✔] :blue[Objective]**')
st.write('Detail-oriented senior software Engineer with 2+ years of experience in Data Engineering. Well-equipped with Snowflake,Matillion,Tableau and SQL. I am looking to explore and experience new challenging roles where I can add value to the company.')

st.divider()

st.subheader('💼 :blue[Professional Experience]')

exp_col1,exp_col2=st.columns([0.8,0.3])

with exp_col1:
    st.write(':grey[Senior Software Engineer],[Kipi.bi ↗](https://www.kipi.bi/)')
    st.write(':grey[Software Engineer],[Kipi.bi ↗](https://www.kipi.bi/)')
    st.write(':grey[Software Engineer],[Apisero ↗](https://us.nttdata.com/en/about-us/content/acquisitions/apisero-is-now-ntt-data)')

with exp_col2:
    st.write('10/2022 - present ')
    st.write('01/2022 - 10/2022 ')
    st.write('10/2021 - 12/2021')

st.divider()

st.subheader('📁 :blue[Projects]')

with st.container():
    proj_col1,proj_col2=st.columns([0.8,0.3])

    with proj_col1:
        st.write('**:grey[Client:] :orange[Kiniksa Pharmaceuticals]**')
        st.write('**:grey[Description:]** The Main objective of the project is to migrate data from AWS Athena to snowflake with the help of Matillion ELT and also migrate and repoint existing dashboards to snowflake.')
    st.write('**:green[Responsibilities:]**')
    st.write("""● I handled snowflake platform setup and role-based access control (RBAC) in the client's environment.<br>
        ● Developed ETL pipelines to extract data from various sources like S3, Veeva CRM, and Veeva Network into Snowflake using Matillion.<br>
        ● Successfully transitioned over 25 existing Athena dashboards to Snowflake.<br>
        ● Conducted PoCs for automating Matillion jobs triggered by file uploads in S3 using lambda function,SQS queues and Event Bridge rules.<br>
        ● I'm currently making sure that our dashboards are ready for use in the real world, and I'm testing them thoroughly to ensure they work correctly during this production deployment phase.<br>
    ● Additionally, I worked on PoCs and actual implementation for data retrieval from an SFTP server and upsertion into Salesforce CRM using custom Python code.""",unsafe_allow_html=True)
    st.write('**:grey[Environment/Applications Used:]** Snowflake,Matillion,Tableau')

        
    with proj_col2:
        st.write('02/2023 - Present')

with st.container():
    proj_col1,proj_col2=st.columns([0.8,0.3])

    with proj_col1:
        st.write('**:grey[Client:] :orange[Audacy]**')
        st.write('**:grey[Description :]** The Main objective of the project is to reduce snowflake platform cost by analyzing various different factors such as compute,storage etc. Also suggesting some good RBAC practices to client for better user and role management.')

        st.write('**:green[Responsibilities:]**')
    st.write("""● My primary task involved optimizing costs on the Snowflake platform.<br>
        ● I analyzed various factors contributing to increased cost consumption, including short and long-running queries and Snowpipes.<br>
        ● To address the high consumption problem because of flattening huge data at runtime, I recommended a custom code approach, supported by a successful proof of concept (PoC) and cost comparison.<br>
        ● I implemented cost optimization accelerators like Watchkeeper and Collie RBAC accelerator inthe client's environment.<br>
    ● I provided guidelines for effective role management in the Snowflake platform, optimizing their role usage.""",unsafe_allow_html=True)
        
    st.write('**:grey[Environment/Applications Used:]** Snowflake')
        

        
    with proj_col2:
        st.write('03/2023 - 05/2023')



with st.container():
    proj_col1,proj_col2=st.columns([0.8,0.3])

    with proj_col1:
        st.write('**:grey[Client:] :orange[Diversitech]**')
        st.write(':grey[**Description** :] The Client wans to migrate data from the MS-SQL server to snowflake with the help of the Informatica ETL tool')

        st.write('**:green[Responsibilities:]**')
    st.write("""● Converting MS-SQL stored procedure into snowflake compatible version <br> 
                 ● Create mappings in Informatica to transfer data from MS-SQL to snowflake<br>
                 ● Working on Data Transformation""",unsafe_allow_html=True)

    st.write('**:grey[Environment/Applications Used:]** Snowflake,Informatica')
        

        
    with proj_col2:
        st.write('11/2022 - 04/2023')


with st.container():
    proj_col1,proj_col2=st.columns([0.8,0.3])

    with proj_col1:
        st.write('**:orange[Decode Analytics]**')
        st.write(""":grey[**Description** :] The client has multiple data sources. We have used the Talend tool for the Extraction
and loading of static data into our Warehouse. We also used a snowpipe for loading data from s3
buckets to the warehouse. Once data is loaded into our warehouse, we are using Stored procedures
written in SQL and Javascript for the Transformations and loading the final data into the reporting
stage for Analytics. Tableau is the tool we are using for Reporting.""")

        st.write('**:green[Responsibilities:]**')
    st.write("""● Handled ETL development for multiple databases of the Client.<br>
● Working with Tableau to develop client-required KPIs Dashboards.""",unsafe_allow_html=True)

    st.write('**:grey[Environment/Applications Used:]** Snowflake,Tableau,Talend,AWS,Python,Github')
        

        
    with proj_col2:
        st.write('01/2022 - 03/2022')


st.divider()

st.subheader("👨🏻‍💻 :blue[Skills]")

with st.container():
    sk1,sk2,sk3,sk4=st.columns(4,gap='large')

    sk1.write('• Snowflake')
    sk2.write('• Matillion')
    sk3.write('• Tableau')
    sk4.write('• SQL')
    sk1.write('• Python')

st.divider()

st.subheader('🎖️ :blue[Certificates]')

with st.container():
    c1,c2,c3=st.columns([0.38,0.3,0.4],gap='medium')

    c1.write('[Snowflake Snowpro Core ↗](https://achieve.snowflake.com/843b82c6-a789-487b-94c7-59187da30f2a#gs.doqwwc)')
    c2.write('[Snowflake Advanced Data Engineer ↗](https://achieve.snowflake.com/aac1dcb3-83e2-424d-b55b-43393a68de99#gs.dor09e)')
    c3.write('[Tableau Desktop Specialist ↗](https://www.credly.com/badges/10259924-ed11-4e39-b612-d2f887d3150a/public_url)')
    c1.write('<br>[Matillion Associate ↗](https://www.credly.com/badges/5fb95fa1-567d-4eb2-8f26-81c9a1f84a99/public_url)',unsafe_allow_html=True)
    c2.write('[Matillion DPC ↗](https://www.credly.com/badges/c6e1d0e8-6dbc-4395-acfb-b0e02b297381/public_url)')


st.divider()  

st.subheader('🎓 :blue[Education]')

with st.container():
    e1,e2=st.columns([0.8,0.3])

    with e1:
        st.write("""
        **:orange[Bachelor of Engineering in Information Technology]**,Savitribai Phule Pune University<br>
        **:grey[College Name:]** K. K. Wagh Institute of Engineering Education And Research<br>
        **:grey[Percentage:]** 80.08
        """,unsafe_allow_html=True)


    with e2:
        st.write("""06/2017 - 06/2021<br> Pune,India""",unsafe_allow_html=True)


with st.container():
    e1,e2=st.columns([0.8,0.3])

    with e1:
        st.write("""
        **:orange[H.S.C]**<br>
        **:grey[College Name:]** R.N.C commerce,J.D.B Arts & N.S.C Science College<br>
        **:grey[Percentage:]** 84.31
        """,unsafe_allow_html=True)


    with e2:
        st.write("""06/2016 - 06/2017<br> Nashik,India""",unsafe_allow_html=True)

with st.container():
    e1,e2=st.columns([0.8,0.3])

    with e1:
        st.write("""
        **:orange[S.S.C]**<br>
        **:grey[School Name:]** Purushottam English School,Nashik Road<br>
        **:grey[Percentage:]** 92.20
        """,unsafe_allow_html=True)


    with e2:
        st.write("""06/2014 - 06/2015<br> Nashik,India""",unsafe_allow_html=True)
        


#css styling
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)





