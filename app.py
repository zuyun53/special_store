import streamlit as st
import requests



def getAllBookstore():
    url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' # 在這裡輸入目標 url
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res

def getCountyOption(items):
    optionList = []
    for item in items:
        name = item['cityName'][0:3]
        if name not in optionList:
            optionList.append(name)
    return optionList

def getSpecificBookstore(items, county):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
    # 如果 name 不是我們選取的 county 則跳過
    if county in name:
        specificBookstoreList.append(item)
    # hint: 用 if-else 判斷並用 continue 跳過
    return specificBookstoreList

def getBookstoreInfo(items):
    expanderList = []
    for item in items:
        expander = st.expander(item['name'])
        expander.image(item['representImage'])
        expander.metric('hitRate', item['hitRate'])
        expander.subheader('Introduction')
        # 用 expander.write 呈現書店的 Introduction
        expander.write(item['intro'])
        expander.subheader('Address')
        # 用 expander.write 呈現書店的 Address
        expander.write(item['Adress'])
        expander.subheader('Open Time')
        # 用 expander.write 呈現書店的 Open Time
        expander.write(item['Open Time'])
        expander.subheader('Email')
        # 用 expander.write 呈現書店的 Email
        expander.write(item['Email'])


        # 將該 expander 放到 expanderList 中
        expanderList.append(expander)
    return expanderList


def app():
    bookstoreList = getAllBookstore()
    countyOption = getCountyOption(bookstoreList)
    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstoreList)) 
    county = st.selectbox('請選擇縣市', countyOption)
    
    specificBookstore = getSpecificBookstore(bookstoreList, county)
    num = len(specificBookstore)
    st.write(f'總共有{num}項結果', num)
    st.snow()
    bookstoreInfo = getBookstoreInfo(specificBookstore)

if __name__ == '__main__':
    app()

