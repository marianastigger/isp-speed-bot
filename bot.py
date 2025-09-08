from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


class InternetSpeedTwitterBot:

    def __init__(self, promised_down, promised_up):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)
        self.down = promised_down
        self.up = promised_up
        self.get_internet_speed()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        wait = WebDriverWait(self.driver, 60)

        start_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "js-start-test"))
        )
        start_button.click()

        try:
            close_btn = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "close-btn"))
            )
            close_btn.click()
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
            pass

        down_speed = float(wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "download-speed"))
        ).text)
        up_speed = float(wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "upload-speed"))
        ).text)

        if down_speed < self.down or up_speed < self.up:
            self.tweet_at_provider(down_speed, up_speed)

    def tweet_at_provider(self, down, up):

        client = tweepy.Client(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        tweet_text = (f"Hey Internet Provider, why is my internet speed {down} down/{up} up when I pay for "
                      f"{self.down} down/{self.up} up?")
        try:
            response = client.create_tweet(text=tweet_text)
            print(f"Tweet posted successfully! Tweet ID: {response.data['id']}.")
        except tweepy.TweepyException as e:
            print(f"Error posting tweet: {e}.")
