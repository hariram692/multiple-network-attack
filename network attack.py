

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

intrusion_model = pickle.load(open('C:/Users/HP/Music/attack/network.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('DDOS ATTACK PREDICTION using ml',
                          
                          [ 'Home',
                            'INTRUSION ATTACK PREDICTION'
                           
                            ],
                          default_index=0)

# intrusion Prediction Page
if (selected == 'Home'):
    
    # page title
    st.title('INTRUSION ATTACK PREDICTION using ml')



   # st.image('11.jpg')

  
    
# intrusion Prediction Page
if (selected == 'INTRUSION ATTACK PREDICTION'):
    
    # page title
    st.title('INTRUSION ATTACK PREDICTION ML')

   
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
   
        
    with col1:
         duration = st.text_input('duration ')
    
    with col2:
         protocoltype = st.text_input('protocoltype')
    
    with col3:
         service	 = st.text_input(' service')
    
    with col1:
         flag= st.text_input(' flag')
    
    with col2:
         srcbytes	 = st.text_input('  srcbytes	')
    
    with col3:
         dstbytes	 = st.text_input(' dstbytes	')
    
    with col1:
         land = st.text_input('land')

    with col2:
         wrongfragment = st.text_input('wrongfragment')

    with col3:
         urgent = st.text_input('urgent')
    
    with col1:
         hot = st.text_input('hot')
    
    with col2:
         numfailedlogins = st.text_input('numfailedlogins')
    
    with col3:
         loggedin = st.text_input('loggedin')
    
    with col1:
         numcompromised = st.text_input('numcompromised')
    
    with col2:
         rootshell = st.text_input('rootshell')
    
    with col3:
         suattempted = st.text_input('suattempted')

    with col1:
         numroot = st.text_input('numroot')

    with col2:
         numfilecreations = st.text_input('numfilecreations')

    with col3:
         numshells = st.text_input('numshells')

    with col1:
         numaccessfiles = st.text_input('numaccessfiles')

    with col2:
         numoutboundcmds = st.text_input('numoutboundcmds')

    with col3:
         ishostlogin = st.text_input('ishostlogin')

    with col1:
         isguestlogin = st.text_input('isguestlogin')

    with col2:
         count = st.text_input('count')

    with col3:
         srvcount = st.text_input('srvcount')

    with col1:
         serrorrate = st.text_input('serrorrate')

   
    
    # code for Prediction
    intru_predict = ''
    
    # creating a button for Prediction
    
    if st.button('INTRUSION RESULT'):
        intrusion_prediction = intrusion_model.predict([[ duration, protocoltype, service, flag, srcbytes,
        dstbytes, land, wrongfragment, urgent, hot,
        numfailedlogins, loggedin, numcompromised, rootshell,
        suattempted, numroot, numfilecreations, numshells,
        numaccessfiles, numoutboundcmds, ishostlogin,
        isguestlogin, count, srvcount, serrorrate,
        ]])

        st.success('The output is {}'.format(intrusion_prediction ))
        
        
        
    


   

if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")








