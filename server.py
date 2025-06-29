"""Import the Flask class from flask module"""
from flask import Flask,make_response,request
app = Flask(__name__)

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

"""Define a route for the root URL ("/")"""
@app.route("/")
def index():
    #function  that handles requests to the root URL
    return {"message": "Hello, World!"}
@app.route("/no_content")
def no_content():
    return ({"message":"No content found"},204)

@app.route("/exp")
def index_explicit():
    resp = make_response({"message":"Hello, World!"})
    resp.status_code = 200
    return resp

@app.route("/data")
def get_data():
    try:
        if data and  len(data) > 0:
            return {"message": f"{len(data)} found"}
        else:
            #If 'data' is empty, return a JSON response with a 500 Internal Server status code
            return {"message": "Data is empty"},500
    except NameError:
            #Handle the case where 'data' is not defined
            # Return a JSON response with a 404 Not found status code
            return {"message": "Data not found"}, 404

@app.route("/name_search")
def name_search():
        """Find a person in the database.
        Returns:
            json: Person if found, with status of 200
            404: If not found
            400: If argument 'q' is missing
            422: If argument 'q' is present but invalid
        """
        # Get the argument 'q' from the query parameters of the request
        query = request.args.get("q")

        if query is None:
            return {"message": "Query parameter 'q' is missing"}, 400

        # Check if the query parameter is present but invalid (e.g., empty or numeric)
        if query.strip() == "" or query.isdigit():
            return {"message": "Invalid input parameter"},422

        # Iterate through the 'data' list to search for a matching person
        for person in data:
            # Check if the query string is present in the person's first name (case-insensitive)
            if query.lower() in person["first_name"].lower():
                # Return the matching person as a JSON response with a 200 OK status code
                return person, 200

        # If no matching person is found, return a JSON response with a message and a 404 Not Found
        return {"message": "Person not found"}, 404

@app.get("/count")
def count():
    try:
        return{"data count": len(data)},200
    except NameError:
        return{"message":"Data not found"},500

@app.get("/person/<var_name>")
def find_by_uuid(var_name):
        for person in data:
            if person["id"] in str(var_name):
                return person, 200

        return {"message": "Person not found"}, 404

@app.delete("/person/<uuid:id>")
def delete_by_uuid(id):
       for person in data:
           if person["id"] in str(id):
               data.remove(person)
               return {"message": f"Person with ID {person['id']} was deleted"}, 200
       return {"message": "Person not found"}, 404
@app.route("/person", methods=["POST"])
def add_by_uuid():
     new_person = request.get_json()

     if not new_person:
         return {"message": "Invalid input, data no provided"}, 422

     try:
         data.append(new_person)
     except NameError:
         return {"message": "Data not defined"}, 500

     return {"message":"Person added successfully"}, 200

@app.errorhandler(404)
def api_not_found():
    # This function is a custom error handler for 404 Not Found errors
    # It is triggered whenever a 404 error occurs within the Flask application
    return {"message": "API not found"}, 404

@app.errorhandler(Exception)
def handle_exception(e):
    return {"message": str(e)}, 500

@app.route("/test500")
def test500():
    raise Exception("Forced exception for testing")
