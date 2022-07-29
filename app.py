import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

from PIL import Image

st.set_page_config(
     page_title='Hiper Automotive Task',
     layout="centered",
     initial_sidebar_state="expanded",
)

vehicle=pd.read_csv("vehicle_list.csv")
al=pd.read_csv("ashok_leyland")
tata=pd.read_csv("tata")

def main():
    image = Image.open('icon.jpg')
    st.sidebar.image(image,width=100)
    st.sidebar.title("Hiper Automotive Task")
    col1, col2 = st.columns( [0.7, 0.3])
    with col1:
        st.title("Hiper Automotive Task")   
    with col2:
       st.image(image,  width=150)
    page = st.sidebar.selectbox("Select One", ['ABOUT',"DASHBOARD"])
    if page == "ABOUT":
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('Creator Profile:')
        st.write('**Name:** Ashwin')
        st.write('**Email:** ash.kek.08@gmail.com')
        st.write('**Github:** https://github.com/ashwinak894')

    if page == "DASHBOARD":
        component=Image.open('Component Layout.png')
        col1,col2,col3 = st.columns([0.3,0.4,0.3])
        with col1:
            manu = st.selectbox('Manufacturer',vehicle.Manufacturer.unique())
        with col2:
            model = st.selectbox('Model',vehicle.Model.unique())
        with col3:
            vn = st.selectbox('Select to View Dashboards',['Fuel Injector','Common Rail','Metering Unit','Water Fuel Seperator','Protect Filter','Fuel Tank'])
        if manu == 'AL':
            img1 = Image.open('bg2.png')
            st.image(img1,use_column_width= 'always')
            st.image(component,use_column_width= 'always')
            st.write('## DASHBOARD REQUESTED')
            if vn == 'Fuel Injector':
                fig=px.scatter(al,x=al['master_row_id'],y=al['Errorrate_Inj'],color='master_row_id')
                fig.update_layout(font_family="Courier New",font_color="blue",title_font_family="Times New Roman",title_font_color="red",
		title={'text': "Fuel Injector Error rate",'y':1,'x':0.5,'xanchor': 'center','yanchor': 'top'})
                st.plotly_chart(fig,use_column_width= 'always')
                col1, col2, col3 = st.columns( [0.25,0.25,0.5])
                with col1:
                    al_avg1=np.mean(al['Errorrate_Inj'])
                    val=float('{:.2f}'.format(al_avg1))
                    col1.metric(label='Error Percentage',value=str(val)+'%',delta='-100%')
                with col2:
                    col2.metric(label='Efficiency',value=str(100-val)+'%',delta='100%')
                with col3:
                    fuel = Image.open('Injector.png')
                    col3.image(fuel,width=150,caption = 'Injector')
            elif vn == 'Common Rail':
                fig=px.scatter(al,x=al['master_row_id'],y=al['Errorrate_RP'],color='master_row_id')
                fig.update_layout(font_family="Courier New",font_color="blue",title_font_family="Times New Roman",title_font_color="red",
		title={'text': "Common Rail Error rate",'y':1,'x':0.5,'xanchor': 'center','yanchor': 'top'})
                st.plotly_chart(fig,use_column_width= 'auto')
                col1, col2, col3 = st.columns( [0.25,0.25,0.5])
                with col1:
                    al_avg1=np.mean(al['Errorrate_RP'])
                    val=float('{:.2f}'.format(al_avg1))
                    st.metric(label='Error Percentage',value=str(val)+'%',delta='-100%')
                with col2:
                    st.metric(label='Efficiency',value=str(val+100)+'%',delta='100%')
                with col3:
                    cm = Image.open('Common Rail.png')
                    st.image(cm,caption = 'Common Rail')
            elif vn == 'Metering Unit':
                fig=px.scatter(al,x=al['master_row_id'],y=al['Errorrate_MU'],color='master_row_id')
                fig.update_layout(font_family="Courier New",font_color="blue",title_font_family="Times New Roman",title_font_color="red",
		title={'text': "Metering Unit Error rate",'y':1,'x':0.5,'xanchor': 'center','yanchor': 'top'})
                st.plotly_chart(fig,use_column_width= 'auto')
                col1, col2, col3 = st.columns( [0.25,0.25,0.5])
                with col1:
                    al_avg1=np.mean(al['Errorrate_MU'])
                    val=float('{:.2f}'.format(al_avg1))
                    col1.metric(label='Error Percentage',value=str(val)+'%',delta='-100%')
                with col2:
                    col2.metric(label='Efficiency',value=str(val+100)+'%',delta='100%')
                with col3:
                    mu = Image.open('Metering Unit.png')
                    col3.image(mu,use_column_width= 'auto',caption = 'Metering Unit')
            elif vn == 'Water Fuel Seperator':
                st.subheader('No data given for this Subsytem hence just displaying the Image')
                wfs = Image.open('Water Fuel Seperator.png')
                st.image(wfs,use_column_width= 'auto',caption = 'Water Fuel Seperator')
            elif vn == 'Protect Filter':
                st.subheader('No data given for this Subsytem hence just displaying the Image')
                pf = Image.open('Fuel Filter.png')
                st.image(pf,use_column_width= 'auto',caption = 'Protect Filter')
            elif vn == 'Fuel Tank':
                st.subheader('No data given for this Subsytem hence just displaying the Image')
                ft = Image.open('Fuel Tank.png')
                st.image(ft,use_column_width= 'auto',caption = 'Fuel tank')
                
        elif manu == 'TATA':
            img2 = Image.open('bg1.png')
            st.image(img2,use_column_width= 'always')
            st.image(component,use_column_width= 'always')
            st.write('## DASHBOARD REQUESTED')
            if vn == 'Fuel Injector':
                fig=px.scatter(tata,x=tata['master_row_id'],y=tata['Errorrate_Inj'],color='master_row_id')
                fig.update_layout(font_family="Courier New",font_color="blue",title_font_family="Times New Roman",title_font_color="red",
		title={'text': "Fuel Injector Error rate",'y':1,'x':0.5,'xanchor': 'center','yanchor': 'top'})
                st.plotly_chart(fig,use_column_width= 'always')
                col1, col2, col3 = st.columns( [0.25,0.25,0.5])
                with col1:
                    al_avg1=np.mean(tata['Errorrate_Inj'])
                    val=float('{:.2f}'.format(al_avg1))
                    st.metric(label='Error Percentage',value=str(val)+'%',delta='-100%')
                with col2:
                    st.metric(label='Efficiency',value=str(100-val)+'%',delta='100%')
                with col3:
                    fuel = Image.open('Injector.png')
                    st.image(fuel,use_column_width= 'auto',caption = 'Injector')
            elif vn == 'Common Rail':
                fig=px.scatter(al,x=al['master_row_id'],y=al['Errorrate_RP'],color='master_row_id')
                fig.update_layout(font_family="Courier New",font_color="blue",title_font_family="Times New Roman",title_font_color="red",
		title={'text': "Common Rail Error rate",'y':1,'x':0.5,'xanchor': 'center','yanchor': 'top'})
                st.plotly_chart(fig,use_column_width= 'auto')
                col1, col2, col3 = st.columns( [0.25,0.25,0.5])
                with col1:
                    al_avg1=np.mean(al['Errorrate_RP'])
                    val=float('{:.2f}'.format(al_avg1))
                    st.metric(label='Error Percentage',value=str(val)+'%',delta='-100%')
                with col2:
                    st.metric(label='Efficiency',value=str(val+100)+'%',delta='100%')
                with col3:
                    cm = Image.open('Common Rail.png')
                    st.image(cm,use_column_width= 'auto',caption = 'Common Rail')
            elif vn == 'Metering Unit':
                fig=px.scatter(al,x=al['master_row_id'],y=al['Errorrate_MU'],color='master_row_id')
                fig.update_layout(font_family="Courier New",font_color="blue",title_font_family="Times New Roman",title_font_color="red",
		title={'text': "Metering Unit Error rate",'y':1,'x':0.5,'xanchor': 'center','yanchor': 'top'})
                st.plotly_chart(fig,use_column_width= 'auto')
                col1, col2, col3 = st.columns( [0.25,0.25,0.5])
                with col1:
                    al_avg1=np.mean(al['Errorrate_MU'])
                    val=float('{:.2f}'.format(al_avg1))
                    st.metric(label='Error Percentage',value=str(val)+'%',delta='-100%')
                with col2:
                    st.metric(label='Efficiency',value=str(val+100)+'%',delta='100%')
                with col3:
                    mu = Image.open('Metering Unit.png')
                    st.image(mu,use_column_width= 'auto',caption = 'Metering Unit')
            elif vn == 'Water Fuel Seperator':
                st.subheader('No data given for this Subsytem hence just displaying the Image')
                wfs = Image.open('Water Fuel Seperator.png')
                st.image(wfs,use_column_width= 'auto',caption = 'Water Fuel Seperator')
            elif vn == 'Protect Filter':
                st.subheader('No data given for this Subsytem hence just displaying the Image')
                pf = Image.open('Fuel Filter.png')
                st.image(pf,use_column_width= 'auto',caption = 'Protect Filter')
            elif vn == 'Fuel Tank':
                st.subheader('No data given for this Subsytem hence just displaying the Image')
                ft = Image.open('Fuel Tank.png')
                st.image(ft,use_column_width= 'auto',caption = 'Fuel tank')

if __name__=='__main__':
    main()
