from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (Replace with your ChromeDriver path)
driver = webdriver.Chrome("C:\chrome-win64")

# Open YouTube and log in
driver.get("https://www.youtube.com")
time.sleep(5)  # Wait for page to load

# Manually log in if not already logged in

def add_video_to_playlist(video_url, playlist_name):
    driver.get(video_url)
    time.sleep(5)
    
    # Click the 'Save' button
    save_button = driver.find_element(By.XPATH, "//button[@aria-label='Save to playlist']")
    save_button.click()
    time.sleep(2)
    
    # Select the playlist
    playlist = driver.find_element(By.XPATH, f"//span[contains(text(), '{playlist_name}')]")
    playlist.click()
    time.sleep(2)
    
    print(f"Added {video_url} to {playlist_name}")

# Example Usage
video_links = [
    "https://www.youtube.com/embed/1z6dJ2qgnas?feature=oembed"
    "https://www.youtube.com/embed/8uFWG6xfkuc?feature=oembed"
]
playlist_name = "Math and Number Theory"

for video in video_links:
    add_video_to_playlist(video, playlist_name)

driver.quit()
