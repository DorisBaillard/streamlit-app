import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import glob
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import pickle
import io
import streamlit.components.v1 as stc






def main():

    st.set_page_config(layout="wide", initial_sidebar_state='expanded')
    st.image("images/logo-recom2.png", width=100)
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    hide_menu = """
    <style>
    #MainMenu {
    visibility:visible;
    }

    footer{
        visibility:visible;
    }
    footer:after {
        content: 'Recom © 2022 - Doris BAILLARD';
        display: block;
        position: relative;
        color:blue;

    }
    </style>
    """

    st.markdown(hide_menu, unsafe_allow_html=True)


    sidebar_header = '''This is a demo of Recom solution version 1.0.0. This demo gathers the main options. Please give it a try :'''
    
    page_options = ["Recommendations base on reviews",
                    "Recommendations based on product similarity",
                    "Generate email"]
    
    st.sidebar.info(sidebar_header)


    
    page_selection = st.sidebar.radio("Try", page_options)


    #########################################################################################
    if page_selection == "Recommendations base on reviews":
        pid_to_idx = pd.read_pickle("data/pid_to_idx.pkl")
        idx_to_pid = pd.read_pickle("data/idx_to_pid.pkl")
        
        
        products = pd.read_pickle("data/products.pkl") 
        lightfm_similarity = pd.read_pickle("data/lightfm-similarity.pkl") 
        items_pivot=pd.read_pickle("data/items_pivot.pkl")
        items_sparse = csr_matrix(items_pivot)
        model = NearestNeighbors(algorithm="brute")
        model.fit(items_sparse)


        def get_product_name(pid, product):
            try:
                name = products.loc[products.product_ids == pid].titles.values[0]
            except:
                name = "Unknown"
            return name

        def get_product_id(name):
            try:
                product_id = products.loc[products.titles == name].product_ids.values[0]
            except:
                product_id = "Unknown"
            return product_id


        def get_sim_scores(pid):
            idx = pid_to_idx[pid]
            sims = lightfm_similarity[idx]
            return sims


        def get_ranked_recos(sims):
            recos = []
        
            for idx in np.argsort(-sims):
                pid = idx_to_pid[idx]
                name = get_product_name(pid, products)
                score = sims[idx]
                recos.append((name,pid))
            return recos




        st.markdown('<p style="color:darkblue;font-size:160%">Products Recommender System</p>',  unsafe_allow_html=True)
        st.markdown('This option will allow you to publish on your site recommendations of products "appreciated by other customers". These recommendations are based on the reviews of other customers. ')
        product_list = products['titles'].values
        selected_product = st.selectbox(
        "Type or select a product from the dropdown",
        product_list
    )
        product_id = get_product_id(selected_product)
        sims = get_sim_scores(product_id)
        result = get_ranked_recos(sims)[:5]

        recommendation_button = st.button('Show Recommendation')
        if recommendation_button:
            product_id = get_product_id(selected_product)
            sims = get_sim_scores(product_id)
            result = get_ranked_recos(sims)[:5]
    

            with st.form("reco1"):
                cols = st.columns((1, 3))
                cols[0].image('images/'+result[0][1]+'.jpg', width=200)
                cols[1].markdown('<p style="color:#3498db;font-size:160%">Product Name and ID: </p>',  unsafe_allow_html=True)
                cols[1].markdown(result[0])
                cols[1].markdown("Url : yoursiteurl")
                cols[1].markdown('<p style="color:#3498db;font-size:160%">Description :</p>', unsafe_allow_html=True)
                cols[1].text('Lorem ipsum dolor sit amet, consectetur adipiscing elit,\nsed do eiusmod tempor incididunt \nut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco.')
                with cols[1]:
                    submitted = st.form_submit_button('Deploy')
                    submitted_all = st.form_submit_button('Deploy All')

                

                
            with st.form("reco2"):
                cols2 = st.columns((1, 3))
                cols2[0].image('images/'+result[1][1]+'.jpg', width=200)
                cols2[1].markdown('<p style="color:#3498db;font-size:160%">Product Name and ID:</p>', unsafe_allow_html=True)
                cols2[1].text(result[1])
                cols2[1].markdown("Url : yoursiteurl")
                cols2[1].markdown('<p style="color:#3498db;font-size:160%">Description :</p>', unsafe_allow_html=True)
                cols2[1].text('Lorem ipsum dolor sit amet, consectetur adipiscing elit,\nsed do eiusmod tempor incididunt \nut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco.')
                cols2[1].form_submit_button('Deploy')
                cols2[1].form_submit_button('Deploy All')



            with st.form("reco3"):
                cols3= st.columns((1, 3))
                cols3[0].image('images/'+result[2][1]+'.jpg', width=200)
                cols3[1].markdown('<p style="color:#3498db;font-size:160%">Product Name and ID:</p>', unsafe_allow_html=True)
                cols3[1].text(result[2])
                cols3[1].markdown("Url : yoursiteurl")
                cols3[1].markdown('<p style="color:#3498db;font-size:160%">Description :</p>', unsafe_allow_html=True)
                cols3[1].text('Lorem ipsum dolor sit amet, consectetur adipiscing elit,\nsed do eiusmod tempor incididunt \nut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco.')
                cols3[1].form_submit_button('Deploy')
                cols3[1].form_submit_button('Deploy All')


            with st.form("reco4"):
                cols4 = st.columns((1, 3))
                cols4[0].image('images/'+result[3][1]+'.jpg', width=200)
                cols4[1].markdown('<p style="color:#3498db;font-size:160%">Product Name and ID:</p>', unsafe_allow_html=True)
                cols4[1].text(result[3])
                cols4[1].markdown("Url : yoursiteurl")
                cols4[1].markdown('<p style="color:#3498db;font-size:160%">Description :</p>', unsafe_allow_html=True)
                cols4[1].text('Lorem ipsum dolor sit amet, consectetur adipiscing elit,\nsed do eiusmod tempor incididunt \nut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco.')
                cols4[1].form_submit_button('Deploy')
                cols4[1].form_submit_button('Deploy All')



            with st.form("reco5"):        
                cols5 = st.columns((1, 3))
                cols5[0].image('images/'+result[4][1]+'.jpg', width=200)
                cols5[1].markdown('<p style="color:#3498db;font-size:160%">Product Name and ID:</p>', unsafe_allow_html=True)
                cols5[1].text(result[4])
                cols5[1].markdown("Url : yoursiteurl")
                cols5[1].markdown('<p style="color:#3498db;font-size:160%">Description :</p>', unsafe_allow_html=True)
                cols5[1].text('Lorem ipsum dolor sit amet, consectetur adipiscing elit,\nsed do eiusmod tempor incididunt \nut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco.')
                cols5[1].form_submit_button('Deploy')
                cols5[1].form_submit_button('Deploy All')

                st.markdown("<hr/>", unsafe_allow_html=True)
                st.success("Successfuly Deployed !")
                st.success("output 'Deploy' :")
                st.write("Clients also liked : ")
                st.image('images/'+result[4][1]+'.jpg', width=150)
                st.markdown(result[0][0])

                st.markdown("<hr/>", unsafe_allow_html=True)
                st.success("Successfuly Deployed !")
                st.success("output 'Deploy All' :")

                st.write("Clients also liked : ")
                cols_deploy = st.columns(5)           
                cols_deploy[0].image('images/'+result[0][1]+'.jpg', width=150)
                cols_deploy[0].markdown(result[0][0])
                cols_deploy[1].image('images/'+result[1][1]+'.jpg', width=150)
                cols_deploy[1].markdown(result[1][0])
                cols_deploy[2].image('images/'+result[2][1]+'.jpg', width=150)
                cols_deploy[2].markdown(result[2][0])
                cols_deploy[3].image('images/'+result[3][1]+'.jpg', width=150)
                cols_deploy[3].markdown(result[3][0])
                cols_deploy[4].image('images/'+result[4][1]+'.jpg', width=150)
                cols_deploy[4].markdown(result[4][0])

#########################################################################################


    if page_selection == "Recommendations based on product similarity": 
        products = pd.read_pickle("data/products.pkl") 
        feature_list = np.array(pickle.load(open('data/embeddings.pkl','rb')))
        filenames = pickle.load(open('data/filenamesdf.pkl','rb'))


        def recommend(features,feature_list):
            neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
            neighbors.fit(feature_list)

            distances, indices = neighbors.kneighbors([features])

            return indices

        def reco2(indices):
            for i in range(len(indices)):
                cols = st.columns((1, 3))
                cols[1].markdown(filenames.index[indices[i]])
                cols[1].markdown(filenames.titles[indices[i]])
                cols[0].image(filenames.image_path[indices[i]].tolist())


        st.markdown("<p style='color:darkblue;font-size:160%'>Recommender System - image similarity</p>", unsafe_allow_html=True)
        st.markdown('This feature will enable you to publish on your site recommendations of "similar products". These recommendations are based on similarities between product images.')
        product_list = filenames['titles'].values
        
        selected_product = st.selectbox("Type or select a product from the dropdown",product_list)
        
        if st.button('Recommendation'):
            
            id = np.where(selected_product == product_list)
            id2 = int(id[0])

            result= recommend(feature_list[id2],feature_list)
            results = list(result)

            with st.form("reco1"):
                cols = st.columns((1, 3))
                cols[0].image(filenames.image_path[results[0]].tolist()[0], width=200)
                cols[1].markdown('<p style="color:#3498db;font-size:160%">Product Name and ID:</p>', unsafe_allow_html=True)
                cols[1].markdown(filenames.titles[results[0]].tolist()[0])
                cols[1].markdown('<p style="color:#3498db;font-size:160%">Description :</p>', unsafe_allow_html=True)
                cols[1].text('Lorem ipsum dolor sit amet, consectetur adipiscing elit,\nsed do eiusmod tempor incididunt \nut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco.')
                cols[1].form_submit_button('Deploy')

            with st.form("reco2"):
                cols = st.columns((1, 3))
                cols[0].image(filenames.image_path[results[0]].tolist()[1], width=200)
                cols[1].markdown('<h4 style="color:#3498db;">Product Name and ID:</h2>', unsafe_allow_html=True)
                cols[1].markdown(filenames.titles[results[0]].tolist()[1])
                cols[1].markdown('<p style="color:#3498db;font-size:160%">Description :</p>', unsafe_allow_html=True)
                cols[1].text('Lorem ipsum dolor sit amet, consectetur adipiscing elit,\nsed do eiusmod tempor incididunt \nut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco.')
                cols[1].form_submit_button('Deploy')


            with st.form("reco3"):
                cols = st.columns((1, 3))
                cols[0].image(filenames.image_path[results[0]].tolist()[2], width=200)
                cols[1].markdown('<p style="color:#3498db;font-size:160%">Product Name and ID:</p>', unsafe_allow_html=True)
                cols[1].markdown(filenames.titles[results[0]].tolist()[2])
                cols[1].markdown('<p style="color:#3498db;font-size:160%">Description :</p>', unsafe_allow_html=True)
                cols[1].text('Lorem ipsum dolor sit amet, consectetur adipiscing elit,\nsed do eiusmod tempor incididunt \nut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco.')
                cols[1].form_submit_button('Deploy')

            with st.form("reco4"):
                cols = st.columns((1, 3))
                cols[0].image(filenames.image_path[results[0]].tolist()[3], width=200)
                cols[1].markdown('<p style="color:#3498db;font-size:160%">Product Name and ID:</p>', unsafe_allow_html=True)
                cols[1].markdown(filenames.titles[results[0]].tolist()[3])
                cols[1].markdown('<p style="color:#3498db;font-size:160%">Description :</p>', unsafe_allow_html=True)
                cols[1].text('Lorem ipsum dolor sit amet, consectetur adipiscing elit,\nsed do eiusmod tempor incididunt \nut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco.')
                cols[1].form_submit_button('Deploy')

            with st.form("reco5"):
                cols = st.columns((1, 3))
                cols[0].image(filenames.image_path[results[0]].tolist()[4], width=200)
                cols[1].markdown('<p style="color:#3498db;font-size:160%">Product Name and ID:</p>', unsafe_allow_html=True)
                cols[1].markdown(filenames.titles[results[0]].tolist()[4])
                cols[1].markdown('<p style="color:#3498db;font-size:160%">Description :</p>', unsafe_allow_html=True)
                cols[1].text('Lorem ipsum dolor sit amet, consectetur adipiscing elit,\nsed do eiusmod tempor incididunt \nut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco.')
                cols[1].form_submit_button('Deploy')
                cols[1].form_submit_button('Deploy All')

                st.markdown("<hr/>", unsafe_allow_html=True)
                st.success("Successfuly Deployed !")
                st.success("output 'Deploy' :")
                st.write("Similar products : ")
                st.image(filenames.image_path[results[0]].tolist()[0], width=150)
                st.markdown(filenames.titles[results[0]].tolist()[4])

                st.markdown("<hr/>", unsafe_allow_html=True)
                st.success("Successfuly Deployed !")
                st.success("output 'Deploy All' :")
                st.write("Similar products : ")
                cols_deploy = st.columns(5)           
                cols_deploy[0].image(filenames.image_path[results[0]].tolist()[0], width=150)
                cols_deploy[0].markdown(filenames.titles[results[0]].tolist()[0])
                cols_deploy[1].image(filenames.image_path[results[0]].tolist()[1], width=150)
                cols_deploy[1].markdown(filenames.titles[results[0]].tolist()[1])
                cols_deploy[2].image(filenames.image_path[results[0]].tolist()[2], width=150)
                cols_deploy[2].markdown(filenames.titles[results[0]].tolist()[2])
                cols_deploy[3].image(filenames.image_path[results[0]].tolist()[3], width=150)
                cols_deploy[3].markdown(filenames.titles[results[0]].tolist()[3])
                cols_deploy[4].image(filenames.image_path[results[0]].tolist()[4], width=150)
                cols_deploy[4].markdown(filenames.titles[results[0]].tolist()[4])


#########################################################################################


    if page_selection == "Generate email": 
        user_cart = pd.read_pickle('data/user_cart.pkl')
        name_list = user_cart['user_name'].values
        feature_list = np.array(pickle.load(open('data/embeddings.pkl','rb')))
        filenames = pickle.load(open('data/filenamesdf.pkl','rb'))


        def recommend(features,feature_list):
            neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
            neighbors.fit(feature_list)

            distances, indices = neighbors.kneighbors([features])

            return indices

        def reco2(indices):
            for i in range(len(indices)):
                cols = st.columns((1, 3))
                cols[1].markdown(filenames.index[indices[i]])
                cols[1].markdown(filenames.titles[indices[i]])
                cols[0].image(filenames.image_path[indices[i]].tolist())
        
        st.markdown("<p style='color:darkblue;font-size:160%'>Mail Generator</p>", unsafe_allow_html=True)
        st.markdown('With this feature you will be able to generate automatic emails to ask for feedback from old and new customers.\nThis email will include a request for feedback on the last product purchased, \nas well as product recommendations.', unsafe_allow_html=True)

        selected_user = st.selectbox("Type or select a user from the dropdown",name_list)
    

        if st.button('generate mailing'):

            name = np.where(selected_user == user_cart['user_name'].values)
            name_id = int(name[0])
            reco_mailing2 = recommend(feature_list[name_id],feature_list)
            reco_mailing2 = list(reco_mailing2)           

            st.markdown('>To: '+ selected_user+'', unsafe_allow_html=True)
            st.markdown("<hr/>", unsafe_allow_html=True)

            st.markdown("<p style='color:Black;font-size:160%'>Hello "+ selected_user+' :) !</p', unsafe_allow_html=True)


            st.markdown('We are constantly striving to improve, and we’d love to hear from you about the following your last command:')

            st.markdown('<p style="font-size:120%">Rate your purchased product:</p>', unsafe_allow_html=True)
            #[a scale from 1 to 5]
            cols= st.columns((3))
            cols[0].empty()
            cols[1].markdown(user_cart.titles[name_id])
            cols[1].image(user_cart.image_path[name_id], width=200)
            cols[1].markdown(":star::star::star::star::star:")

            cols[1].button('Rate this article on company.com')
            cols[2].empty()
            
            st.text('\n\n')           
              

            
            st.markdown('Your feedback helps us improve and reach more great customers like you.')

           
            st.text('\n\n')           
            st.markdown("<hr/>", unsafe_allow_html=True)

            st.markdown('<p style="font-size:120%">Discover products in the same category: </p>', unsafe_allow_html=True)
            st.text('\n\n')
            cols_mail = st.columns((7))
            cols_mail[0].empty()
            cols_mail[1].image(filenames.image_path[reco_mailing2[0]].tolist()[0], width=100)
            cols_mail[1].markdown(filenames.titles[reco_mailing2[0]].tolist()[0])
            cols_mail[1].markdown(":star::star::star::star::star:")
            cols_mail[2].image(filenames.image_path[reco_mailing2[0]].tolist()[1], width=100)
            cols_mail[2].markdown(filenames.titles[reco_mailing2[0]].tolist()[1])
            cols_mail[2].markdown(":star::star::star::star:")
            cols_mail[3].image(filenames.image_path[reco_mailing2[0]].tolist()[2], width=100)
            cols_mail[3].markdown(filenames.titles[reco_mailing2[0]].tolist()[2])
            cols_mail[3].markdown(":star::star::star::star::star:")
            cols_mail[4].image(filenames.image_path[reco_mailing2[0]].tolist()[3], width=100)
            cols_mail[4].markdown(filenames.titles[reco_mailing2[0]].tolist()[3])
            cols_mail[4].markdown(":star::star::star::star:")
            cols_mail[5].image(filenames.image_path[reco_mailing2[0]].tolist()[4], width=100)
            cols_mail[5].markdown(filenames.titles[reco_mailing2[0]].tolist()[4])
            cols_mail[5].markdown(":star::star::star::star::star:")
            cols_mail[6].empty()

            st.text('\n\n')
            st.markdown("<hr/>", unsafe_allow_html=True)
            st.markdown('<p style="font-size:120%">Discover our new products: </p>', unsafe_allow_html=True)
            st.text('\n\n')
            cols_mail2 = st.columns((4))
          
            cols_mail2[0].image('images/velo.jpg', width=200)
            cols_mail2[1].image('images/sac.jpg', width=200)
            cols_mail2[2].image('images/shoes.jpg', width=200)
            cols_mail2[3].image('images/survet.jpg', width=200)
            
            st.text('\n\n\n\n')
            st.markdown("<hr/>", unsafe_allow_html=True)

            st.markdown('Always yours,')
            st.markdown('[company] team')




if __name__ == '__main__':
    main()