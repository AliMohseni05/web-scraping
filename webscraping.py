
from selenium import webdriver
from selenium.webdriver.common.by import By

#start driver and make soeme option 

chrom_option=webdriver.ChromeOptions()
#chrom_option.add_argument("--headless=new") # withou opening chrome 
#diver= webdriver.Chrome(options=chrom_option) # start diver 

diver= webdriver.Chrome() # start diver 
#diver.get("https://www.adamchoi.co.uk/overs/detailed") # webcite for to go 
diver.get("https://songsara.net/") # webcite for to go 
#shoe or save starcker data
print(diver.title)

# Close the browser window
#diver.quit()

 # make this app mian to mrain runing 
#if __name__ == "__main__":
   #first_test_script()
#breakpoint()

#clt+f
#bilde x path 
# // tagName[@AttribateName="Value"]
# //label[@analytics-event="All matches"]


#all_matches_button  = diver.find_element(By.XPATH,'//label[@analytics-event="All matches"]')
elemet=diver.find_element(By.CLASS_NAME,'Malte Marten')
elemet.click
#all_matches_button.click
#print(all_matches_button)

##################### fire fox#####################
# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Firefox()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element 
element = driver.find_element(By.LINK_TEXT, "Master DS & ML")

# click the element
element.click()









#diver.quit()
