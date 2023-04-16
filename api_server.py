#Ref: https://www.analyticsvidhya.com/blog/2022/01/rest-api-with-python-and-flask/#What_Is_Flask-Restful?
from flask import Flask, render_template, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

data = {
    "Ampang": "34.1",
    "Cheras": "33.1",
    "Kajang": 34.9
}

class WeatherTemperature(Resource):
    def __init__(self):
        pass
    
    def get(self):
        location = request.args.get("location")
        return_all_data = request.args.get("return_all_data")
        if return_all_data is not None:
            return data
        
        if location in data:
            temp = {}
            temp["temperature"] = data[location]
            temp["location"] = location
            return temp
        else:
            return {"error": f"{location} not found"}

    def post(self):
        location = request.args.get("location")
        temperature = request.args.get("temperature")

        if location in data:
            return {"error": f"{location} exists!"}

        else:
            data[location] = temperature
            return {"message": f"{location}={temperature} is added in the database successfully."}

    def put(self):
        location = request.args.get("location")
        temperature = request.args.get("temperature")

        if location in data:
            data[location] = temperature
            return {"message": f"{location}={temperature} updated successfully."}

        else:
            return {"error": f"{location} not found"}

    def delete(self):
        location = request.args.get("location")
        if location in data:
            del data[location]
            return {"message": f"{location} data removed successfully."}
        else:
            return {"error": f"{location} not found"}


api.add_resource(WeatherTemperature, '/')

@app.route('/')
def index():
    # call the API to get the response
    response = api.get('/').json()
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
