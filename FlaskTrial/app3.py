#Declare an app function that will return some HTML
@app.route("/")
def connect_mongo():

# Setup the webpage for app's frontend
html_str = '''
<!DOCTYPE html>
<html lang="en">
'''

# Have Flask return some MongoDB information
html_str = html_str + "

# Object Rocket Flask App Tutorial

"
html_str = html_str + "

## mongo.cx client instance:" + str(mongo.cx) + "


"
html_str = html_str + "

### " + str(db) + "

"
html_str = html_str + "

### " + str(col) + "

"

# Get a MongoDB document using PyMongo's find_one() method
html_str = html_str + "

" + str(col.find_one()) + "

</html>"

return html_str

if __name__ == '__main__':
app.run(debug=True)

