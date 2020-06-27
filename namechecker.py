from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

############################################################################
#  First use words.py to put the word combinations into wordlist.txt !!!   #
############################################################################

available = []
rejected = []
nottested = []
nottested2 = []

# Add what is already in the files (if there is anything) to the lists so that
# it works if you stop the program mid-run
with open("rejected.txt", "r+") as t:
    rejected = [line[:-1] for line in t]
with open("accepted.txt", "r+") as t:
    available = [line[:-1] for line in t]

print("available:")
print(available)
print("rejected:")
print(rejected)

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
assert "Instagram" in driver.title
elem = driver.find_element_by_name("username")

nottestedfile = open("nottested.txt", "a")
rejectedfile = open("rejected.txt", "a")
acceptedfile = open("accepted.txt", "a")


with open("wordlist.txt", "r") as file:
    filelist = [line[:-1] for line in file]

username_accepted = False

for username in filelist:
    if username in available or username in rejected:
        print(username + ": Already checked")
        continue
    found = False
    for i in range(30):
        elem.send_keys(Keys.BACKSPACE)
    elem.send_keys(username)
    elem.send_keys(Keys.RETURN)
    time.sleep(0.3)
    try:

        elem2 = driver.find_element_by_class_name("coreSpriteInputError")
        print(username + ": Rejected")
        found = True
        username_accepted = False
    except:
        i=i

    try:
        elem2 = driver.find_element_by_class_name("coreSpriteInputAccepted")
        print(username + ": Accepted")
        available.append(username)
        with open("accepted.txt", "a") as acceptedfile:
            acceptedfile.write(username+"\n")
        found = True
        username_accepted = True
    except:
        i=i
    if not found:
        driver.close()
        time.sleep(20)
        driver = webdriver.Chrome()
        driver.get("https://www.instagram.com/")
        assert "Instagram" in driver.title
        elem = driver.find_element_by_name("username")
        nottested.append(username)
        with open("nottested.txt", "a") as nottestedfile:
            nottestedfile.write(username+"\n")
    elif not username_accepted:
        with open("rejected.txt", "a") as rejectedfile:
            rejectedfile.write(username+"\n")

# Second loop to test the stuff in that wasn't tested in the first run
for username in nottested:
    found = False
    for i in range(30):
        elem.send_keys(Keys.BACKSPACE)
    elem.clear()
    elem.send_keys(username)
    elem.send_keys()
    elem.send_keys(Keys.RETURN)
    time.sleep(0.3)
    try:

        elem2 = driver.find_element_by_class_name("coreSpriteInputError")
        print(username + ": Rejected")
        found = True
        username_accepted = False
    except:
        found = False
    try:
        elem2 = driver.find_element_by_class_name("coreSpriteInputAccepted")
        print(username + ": Accepted")
        available.append(username)
        with open("accepted.txt", "a") as acceptedfile:
            acceptedfile.write(username+"\n")
        found = True
        username_accepted = True
    except:
        found = False
    if not found:
        driver.close()
        time.sleep(20)
        driver = webdriver.Chrome()
        driver.get("https://www.instagram.com/")
        assert "Instagram" in driver.title
        elem = driver.find_element_by_name("username")
        nottested.append(username)
        with open("nottested.txt", "a") as nottestedfile:
            nottestedfile.write(username + "\n")
    elif not username_accepted:
        with open("rejected.txt", "a") as rejectedfile:
            rejectedfile.write(username + "\n")


print("\n\n\n--------------------------------------------------\n")
print("List of available names:")
for i in available:
    print(i)


print("\n\n--------------------------------------------------\n")
print("Not tested:")
for i in nottested2:
    print(i)

driver.close()
