import subprocess
import time

# Set this to your actual Chrome executable path
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Define profile paths and their websites
chrome_profiles = {
    "Profile 6": [
        "https://chat.deepseek.com/",
        "https://youtube.com/",
        "https://chat.qwen.ai/",
        "https://chatgpt.com/"
    ],
    "Profile 4": [
        "https://youtube.com/",
        "https://studio.bilibili.tv/archive-list?type=&reload=1",
        "https://www.bilibili.tv/",
        "https://khansmm.shop/orders",
        "https://dailyroutinehealthmeditation009.blogspot.com/"
    ],
    "Default": [
        "https://www.blogger.com/blog/posts/6617787372142740637",
        "https://search.google.com/search-console?utm_source=about-page&resource_id=https://www.movielx.xyz/",
        "https://chat.deepseek.com/",
        "https://www.instagram.com/",
        "https://www.emailnator.com/",
        "https://wrtn.ai/"
    ],
    "Profile 18": [
        "https://www.youtube.com/",
        "https://studio.youtube.com/channel/UCQxZiPtW9x6wl8gemrEhlwg",
        "https://chat.qwen.ai/",
        "https://chatgpt.com/"
    ],
    "Profile 5": [
        "https://beta.publishers.adsterra.com/websites/",
        "https://chatgpt.com/",
        "https://myninja.ai/"
    ]
}

# Base Chrome User Data folder
BASE_USER_DATA = r"C:\Users\Good\AppData\Local\Google\Chrome\User Data"

def launch_chrome(profile_name, urls):
    profile_dir = f"--profile-directory={profile_name}"
    for url in urls:
        print(f"Opening {url} in {profile_name}...")
        subprocess.Popen([
            CHROME_PATH,
            profile_dir,
            url
        ])
        time.sleep(1.5)  # delay to avoid launching all at once

def main():
    for profile, websites in chrome_profiles.items():
        launch_chrome(profile, websites)

if __name__ == "__main__":
    main()
