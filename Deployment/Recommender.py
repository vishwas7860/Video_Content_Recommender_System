import streamlit as st
import pickle
import pandas as pd

cntnt = pickle.load(open("content.pkl", "rb"))
cntnt = pd.DataFrame(cntnt)

user_list = pickle.load(open("user.pkl", "rb"))
users = pd.DataFrame(user_list)

cs1 = pickle.load(open("similarity.pkl", "rb"))
di = pickle.load(open("diction.pkl", "rb"))

def recommended(m_id):
    content_index = cntnt[cntnt["content_id"] == m_id].index[0]
    distances = cs1[content_index]

    recommended_content = list(sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:51])

    cont = []
    for x in recommended_content:
        cont.append(cntnt["content_id"][x[0]])

    rc = []
    for x in recommended_content:
        rc.append((x[1]))
    c_cont = dict(zip(cont, rc))

    return c_cont

def show(x):
    ans = {}
    try:
        for i in range(1):
            ans.update(recommended(di[x][:][i][1]))
    except:
        exit()
    ddd = dict(sorted(ans.items(), key=lambda y: y[1]))
    give = ddd.keys()
    for y in give:
        st.write(y)


st.title("Video Recommender System")

selected_user = st.selectbox("Select User Id:", users["user_id"].values)

if st.button("Recommend"):
    st.write(selected_user)
    show(selected_user)