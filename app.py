#!/usr/bin/env python
# coding: utf-8

# In[9]:


from flask import Flask,render_template,request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app=Flask(__name__)
model=pickle.load(open('model_p','rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('Untitled-2.html')
standard_to=StandardScaler()
@app.route("/predict",methods=["POST"])
def predict():
    if request.method=='POST' :
        rl=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        SubD=request.form['division']
        if SubD=='ANDAMAN & NICOBAR ISLANDS' :
            rl[0]=1
        if SubD=='ARUNACHAL PRADESH' :
            rl[1]=1
        if SubD=='ASSAM & MEGHALAYA':
            rl[2]=1
        if SubD=='BIHAR':
            rl[3]=1
        if SubD=='CHHATTISGARH':
            rl[4]=1
        if SubD=='COASTAL ANDHRA PRADESH':
            rl[5]=1
        if SubD=='EAST MADHYA PRADESH':
            rl[6]=1
        if SubD=='EAST RAJASTHAN':
            rl[7]=1
        if SubD=='EAST UTTAR PRADESH':
            rl[8]=1
        if SubD=='GANGETIC WEST BENGAL':
            rl[9]=1
        if SubD=='GUJARAT REGION':
            rl[10]=1
        if SubD=='HIMACHAL PRADESH':
            rl[11]=1
        if SubD=='JAMMU & KASHMIR':
            rl[12]=1
        if SubD=='JHARKHAND':
            rl[13]=1
        if SubD=='KERALA':
            rl[14]=1
        if SubD=='KONKAN & GOA':
            rl[16]=1
        if SubD=='LAKSHADWEEP':
            rl[17]=1
        if SubD=='MADHYA MAHARASHTRA':
            rl[18]=1
        if SubD=='MATATHWADA':
            rl[19]=1
        if SubD=='ORISSA':
            rl[20]=1
        if SubD=='PUNJAB':
            rl[21]=1
        if SubD=='RAYALSEEMA':
            rl[22]=1
        if SubD=='SAURASHTRA & KUTCH':
            rl[23]=1
        if SubD=='SUB HIMALAYAN WEST BENGAL & SIKKIM':
            rl[24]=1
        if SubD=='UTTARAKHAND':
            rl[25]=1
        if SubD=='VIDARBHA':
            rl[26]=1
        if SubD=='WEST MADHYA PRADESH ':
            rl[27]=1
        if SubD=='WEST RAJASTHAN':
            rl[28]=1
     
        m1=int(request.form['m1'])
        m2=int(request.form['m2'])
        m3=int(request.form['m3'])
        l1=[]
        l2=[m1,m2,m3]+rl
        m11=m1**2
        m22=m2**2
        m33=m3**2
        mm=m1*m2*m3
        avg1=(m1+m2+m3)**2
        avg2=(m1+m2)**2+(m2+m3)**2+(m1+m3)**2
        l3=[m11,m22,m33,mm,avg1,avg2]
        l2=l2+l3
        l1.append(l2)
        ex=np.array(l1)
        prediction=model.predict(ex)
        output=round(prediction[0],2)
        if output<0 :
            return render_template('Untitled-2.html',prediction_texts="Sorry")
        else :
            return render_template('Untitled-2.html',prediction_text="Rain fall in predicted month is: {}".format(output))
    else :
        return render_template('Untitled-2.html')
if __name__=="__main__" :
    app.run(debug=True)
        


# In[ ]:




