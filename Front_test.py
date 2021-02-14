from selenium import webdriver
import time
import re

def test_one():
   errors = []
   driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

   driver.get("http://the-internet.herokuapp.com/broken_images")

   element = driver.find_element_by_id("content")
   print(element.text)

   if(element.text != "Broken Images"): #Verying the Broken Images text
      errors.append("Expected message does not exist on the page")
      
   driver.close()

   assert not errors, "errors occured:\n{}".format("\n".join(errors))
   
def test_two():
   errors = []
   driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

   driver.get("http://the-internet.herokuapp.com/forgot_password")

   element = driver.find_element_by_id("content")
   print(element.text)

   if "Forgot Password" not in element.text: #Verying the Forgot Password text
      errors.append("Expected message does not exist on the page")

   driver.close()

   assert not errors, "errors occured:\n{}".format("\n".join(errors))

def test_three():

   errors = []
   driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

   driver.get("http://the-internet.herokuapp.com/login")

   usernamel = driver.find_element_by_id("username") # Giving wrong username and correct password
   usernamel.send_keys("dummy")

   passwordl = driver.find_element_by_id("password")
   passwordl.send_keys("SuperSecretPassword!")

   driver.find_element_by_class_name("radius").click()

   time.sleep(10)

   elementl = driver.find_element_by_id("flash-messages")

   print(elementl.text)

   if "Your username is invalid!" not in elementl.text:
      errors.append("Expected error message is not shown")

   time.sleep(5)
   usernamep = driver.find_element_by_id("username") # Giving correct username and wrong password
   usernamep.send_keys("tomsmith")

   password = driver.find_element_by_id("password")
   password.send_keys("dummy")

   driver.find_element_by_class_name("radius").click()

   time.sleep(10)

   elementp = driver.find_element_by_id("flash-messages")

   print(elementp.text)

   if "Your password is invalid!" not in elementp.text:
      errors.append("Expected error message is not shown")

   driver.close()

   assert not errors, "errors occured:\n{}".format("\n".join(errors))

def test_four():

   errors = []

   driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

   driver.get("http://the-internet.herokuapp.com/inputs")

   username = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/input")

   username.send_keys("abc")

   attr = username.get_attribute("value")

   print("attr",attr)

   time.sleep(2)

   if(attr == ""): #Verying the text after entering alphabets
      errors.append("We are not able to enter the alphabets")

   time.sleep(2)
   driver.close()

   assert not errors, "errors occured:\n{}".format("\n".join(errors))


def test_five():

   errors = []
   driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

   driver.get("http://the-internet.herokuapp.com/tables")

   unsortedlist1 = []
   mytable1 = driver.find_element_by_id('table1')
   for row in mytable1.find_elements_by_css_selector('tr'):
      for cell in row.find_elements_by_tag_name('td'):
         amount = re.findall("\d+\.\d+", cell.text)
         if(amount):
            unsortedlist1.append(float(amount[0]))

   print("unsortedlist1",unsortedlist1)
   time.sleep(2)
   due = driver.find_element_by_xpath("/html/body/div[2]/div/div/table[1]/thead/tr/th[4]/span")

   time.sleep(2)
   due.click()
   time.sleep(5)

   sortedlist1 = []
   mytable11 = driver.find_element_by_id('table1')
   for row in mytable11.find_elements_by_css_selector('tr'):
      for cell in row.find_elements_by_tag_name('td'):
         amount = re.findall("\d+\.\d+", cell.text)
         if(amount):
            sortedlist1.append(float(amount[0]))

   print("sortedlist1", sortedlist1)
   time.sleep(2)

   for i in range(len(sortedlist1)):
      if(sortedlist1[i] != sorted(unsortedlist1)[i]): #Verying the table1 is sorted or not
         errors.append("Table1 is not sorted by the due amount")

   unsortedlist2 = []
   mytable1 = driver.find_element_by_id('table2')
   for row in mytable1.find_elements_by_css_selector('tr'):
      for cell in row.find_elements_by_tag_name('td'):
         amount = re.findall("\d+\.\d+", cell.text)
         if(amount):
            unsortedlist2.append(float(amount[0]))

   print("unsortedlist2",unsortedlist2)
   time.sleep(2)
   due = driver.find_element_by_xpath("/html/body/div[2]/div/div/table[2]/thead/tr/th[4]/span")

   time.sleep(2)
   due.click()
   time.sleep(5)

   sortedlist2 = []
   mytable11 = driver.find_element_by_id('table2')
   for row in mytable11.find_elements_by_css_selector('tr'):
      for cell in row.find_elements_by_tag_name('td'):
         amount = re.findall("\d+\.\d+", cell.text)
         if(amount):
            sortedlist2.append(float(amount[0]))

   print("sortedlist2", sortedlist2)
   time.sleep(2)

   for i in range(len(sortedlist2)):
      if(sortedlist2[i] != sorted(unsortedlist2)[i]): #Verying the table2 is sorted or not
         errors.append("Table2 is not sorted by the due amount")

   time.sleep(2)
   driver.close()

   assert not errors, "errors occured:\n{}".format("\n".join(errors))

def test_six():

   errors = []
   driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

   driver.get(" http://the-internet.herokuapp.com/notification_message_rendered")

   for i in range(10):
      element = driver.find_element_by_link_text("Click here")
      print(element)

      time.sleep(5)
      element.click()

      time.sleep(5)

      elementf = driver.find_element_by_id("flash-messages")

      print(elementf.text)

      if "Action successful" not in elementf.text: #Verying the Action successful text
         continue
      else:
         break
   else:
      errors.append("Expected successful notification is not shown")

   driver.close()
   assert not errors, "errors occured:\n{}".format("\n".join(errors))
