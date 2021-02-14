import requests
import json

connection = requests.Session()
hdr = {"accept": "application/json", "Content-Type": "application/json"}


def test_one():
   errors = []
   data = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
   }
   response = connection.post("https://reqres.in/api/register",data = json.dumps(data), headers=hdr)

   if(response.status_code != 200):#we are verifying the status code for registration
      errors.append("Status code is not 200")

   responedata = response.json()
   print("responedata",responedata)

   token = responedata['token']

   datav = {
      "email": "eve.holt@reqres.in",
      "password": "cityslicka"
   }

   responsev = connection.post("https://reqres.in/api/login",data = json.dumps(datav), headers=hdr)
   responedatav = responsev.json()
   print("responedatav",responedatav)

   tokenv = responedatav['token']
   if(tokenv != token): # we are verifying the token value should be same for login
      errors.append("token id is not matching")

   assert not errors, "errors occured:\n{}".format("\n".join(errors))


def test_two():
   errors = []
   response = connection.delete("https://reqres.in/api/users/4",headers=hdr)

   if(response.status_code != 204): #we are verifying the status code for deletion
      errors.append("Status code is not 204")

   datal = {
      "email": "eve.holt@reqres.in",
      "password": "cityslicka"
   }

   responsev = connection.post("https://reqres.in/api/login",data = json.dumps(datal), headers=hdr)

   if(responsev.status_code == 200):
      errors.append("Status code is 200 for login even after deleting the user")

   responedatav = responsev.json()
   print("responedatal",responedatav)

   if'token' in responedatav: # we are verifying the token for login api
      errors.append("token is present in response even after deleting the user ")

   assert not errors, "errors occured:\n{}".format("\n".join(errors))


def test_three():
   errors = []
   response = connection.get("https://reqres.in/api/unknown",headers=hdr)

   if(response.status_code != 200): #we are verifying the status code for deletion
      errors.append("Status code is not 200")

   responedata = response.json()
   print("responedata",responedata)

   if(responedata['page'] != 1): # we are verifying the page no.
      errors.append("Page no. is not matching as expected")

   for ele in responedata['data']:
      if(ele["id"] == 2 and ele["year"] == 2001):
         break
   else:
      errors.append("Expected ID and year does not exist in response")

   assert not errors, "errors occured:\n{}".format("\n".join(errors))

def test_four():
   errors = []
   response = connection.get("https://reqres.in/api/users?page=2",headers=hdr)

   if(response.status_code != 200): #we are verifying the status code for deletion
      errors.append("Status code is not 200")

   responedata = response.json()
   print("responedata",responedata)

   for ele in responedata['data']:
      if(ele["id"] == 7 and ele["last_name"] == "Lawson"):
         break
   else:
      errors.append("Expected ID and lastname does not exist in response")

   assert not errors, "errors occured:\n{}".format("\n".join(errors))

def test_five():
   errors = []
   response = connection.get("https://reqres.in/api/users/2",headers=hdr)

   if(response.status_code != 200): #we are verifying the status code for deletion
      errors.append("Status code is not 200")

   responedata = response.json()
   print("responedata",responedata)

   if(responedata['data']['first_name'] != "John"):
      errors.append("first_name is not John in the response")

   assert not errors, "errors occured:\n{}".format("\n".join(errors))
