# import os
# import pickle
# from flask import Flask
# from flask_restful import Resource, Api, reqparse
# from flask import Flask, request, jsonify # loading in Flask
# import pandas as pd # loading pandas for reading csv
# from flask_cors import CORS
# import numpy as np
# app = Flask(__name__)
# CORS(app)
# api = Api(app)
# # Require a parser to parse our POST request.
# parser = reqparse.RequestParser()
# parser.add_argument("title")
# parser.add_argument("gender")
# parser.add_argument("type")
# # Unpickle our model so we can use it!
# if os.path.isfile("./our_model.pkl"):
#   model = pickle.load(open("./our_model.pkl", "rb"))
# else:
#   raise FileNotFoundError
# class Predict(Resource):
#   def post(self):
#     # Get data from Post request
#     # data = request.form
#     data = request.get_json()
#     # Make prediction
#     df = pd.DataFrame(([data]), index=[0])
#     print(df.head())
#     # making predictions
#     pred = model.predict(df)
    
#     if 1 in pred:
#         return("A+")
#     elif 2 in pred:
#         return("A-")
#     elif 3 in pred:
#         return("B+")
#     elif 4 in pred:
#         return("B-")
#     elif 5 in pred:
#         return("C+")
#     elif 6 in pred:
#         return("C-")
#     elif 7 in pred:
#         return("D+")
#     elif 8 in pred:
#         return("D-")
#     elif 9 in pred:
#         return("E+")
#     elif 10 in pred:
#         return("E-")
        
# #     args = parser.parse_args()
# # # Sklearn is VERY PICKY on how you put your values in...
# #     X = (
# #       np.array(
# #         [
# #           args["gender"],
# #           args["type"]
# #         ]
# #       ).astype("float").reshape(1, -1)
# #     )
# #     _y = model.predict([X])
# #     return {"class": _y}
# api.add_resource(Predict, "/predict")

# class Percent(Resource):
#   def post(self):

#     data = request.get_json()
#     # Make prediction
#     df = pd.DataFrame(([data]), index=[0])
#     # making predictions
#     pred = model.predict(df)
#     predP = model.predict_proba(df)*100
#     predP_list = predP[0,:].tolist()
#     predP_json = pd.Series(predP_list).to_json(orient='values')
#     print("Sou eu Krl: ", predP_json)
#     return (predP_json)

# api.add_resource(Percent, "/percent")

# if __name__ == "__main__":
#   app.run(debug=True)



from flask import Flask, request, jsonify # loading in Flask
import pandas as pd # loading pandas for reading csv
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import json
import pickle

app = Flask(__name__)
CORS(app)
api = Api(app)
model = pickle.load(open("./our_model.pkl", "rb"))

@app.route('/predict',methods=['POST'])

def predict():
    
    # Get data from Post request
    data = request.get_json()
    # Make prediction
    df = pd.DataFrame(([data]), index=[0])
    print(df.head())
    # making predictions
    pred = model.predict(df)
    predP = model.predict_proba(df)
    print(pred)
    print(predP.tolist)
    if 1 in pred:
        return("A+")
    elif 2 in pred:
        return("A-")
    elif 3 in pred:
        return("B+")
    elif 4 in pred:
        return("B-")
    elif 5 in pred:
        return("C+")
    elif 6 in pred:
        return("C-")
    elif 7 in pred:
        return("D+")
    elif 8 in pred:
        return("D-")
    elif 9 in pred:
        return("E+")
    elif 10 in pred:
        return("E-")
    # returning the predictions as json

@app.route('/percent',methods=['POST'])

def percent():
    
    # Get data from Post request
    data = request.get_json()
    # Make prediction
    df = pd.DataFrame(([data]), index=[0])
    # making predictions
    predP = model.predict_proba(df)*100
    predP_list = predP[0,:].tolist()
    predP_listt = [round(x,2) for x in predP_list]
    predP_json = pd.Series(predP_listt).to_json(orient='values')
    # predP_json = json.dumps(predP_list)
    print("Sou eu Krl: ", predP_listt)
    # return jsonify(str(predP_json)[1:-1])
    return (predP_json)




if __name__ == '__main__':
    app.run(port=5000, debug=True)