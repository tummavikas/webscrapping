
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import tkinter as tk

def print_inputs():
    global user_id,pass_id,subject
    user_id = user_id_entry.get()
    pass_id = pass_id_entry.get()
    subject = subject_entry.get()
    print(f"User ID: {user_id}, Pass ID: {pass_id}, Subject: {subject}")

root = tk.Tk()

user_id_label = tk.Label(root, text="User ID:")
user_id_label.pack()
user_id_entry = tk.Entry(root)
user_id_entry.pack()

pass_id_label = tk.Label(root, text="Pass ID:")
pass_id_label.pack()
pass_id_entry = tk.Entry(root)
pass_id_entry.pack()

subject_label = tk.Label(root, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(root)
subject_entry.pack()

print_button = tk.Button(root, text="Print Inputs", command=print_inputs)
print_button.pack()

root.mainloop()
#close the window after pressing inputs

cService = webdriver.ChromeService(executable_path=r'C:\Users\tumma_dfb60wc\OneDrive\Documents\chromedriver.exe')
driver = webdriver.Chrome(service = cService)
driver.get("https://twitter.com/login")

# Setup the log in
sleep(3)
username = driver.find_element(By.XPATH,"//input[@name='text']")
username.send_keys(user_id)
sleep(3)
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next_button.click()

sleep(3)
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys(pass_id)
sleep(3)
log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
log_in.click()
sleep(10)

search_box = driver.find_element(By.XPATH,"//input[@enterkeyhint='search']")
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)

sleep(3)
people = driver.find_element(By.XPATH,"//span[contains(text(),'People')]")
people.click()

sleep(3)
profile = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[1]/a/div/div[1]/span/span[1]")
profile.click()

sleep(10)

UserTags=[]
TimeStamps=[]
Tweets=[]
Replys=[]
reTweets=[]
Likes=[]

articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
sleep(3)
while True:
    new_tweets = []
    for article in articles:
        UserTag = article.find_element(By.XPATH(".//div[@data-testid='User-Names']")).text
        UserTags.append(UserTag)
        if UserTags == "":
            UserTags = "0"

        TimeStamp = article.find_element(By.XPATH(".//time")).get_attribute('datetime')
        TimeStamps.append(TimeStamp)
        if timestamp == "":
          timestamp = "0"

        Tweet = driver.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
        if Tweet == "":
             Tweet = "0"
        Tweets.append(Tweet)
        
        Reply = driver.find_element(By.XPATH,".//div[@data-testid='reply']").text
        if Reply == "":
            Reply = "0"
        Replys.append(Reply)
        
        reTweet = driver.find_element(By.XPATH,".//div[@data-testid='retweet']").text
        if reTweets == "":
         reTweets = "0"
        reTweets.append(reTweet)
        
        Like = driver.find_element(By.XPATH,".//div[@data-testid='like']").text
        if Likes == "":
          Likes = "0"
        Likes.append(Like)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(3)
    articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
    Tweets2 = list(set(Tweets))
    if len(Tweets2) > 5:
        break

    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(3)
    articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")

    # Find unique tweets and check if there are more than 5 unique tweets
    unique_tweets = list(set(new_tweets))
    if len(unique_tweets) > 5:
        break

print(len(UserTags),
len(TimeStamps),len(Tweets),
len(Replys),
len(reTweets),
len(Likes))
