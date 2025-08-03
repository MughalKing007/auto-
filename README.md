# auto-Here's a complete `README.md` for your **Chrome Profile Launcher Tool** — ideal for GitHub or local documentation:

---
Support Our Work
Help us maintain and improve MovieLX by donating. Your support means a lot to us! ❤️

PayPal Donation
PayPal Account: ameermughal2002@gmail.com

PayPal
Donate via PayPal

## 🚀 Chrome Profile Launcher Tool

Automatically open specific websites in designated Google Chrome profiles using Python.

### ✅ Features

* Open multiple websites in multiple Chrome profiles.
* Supports daily automation (via Windows Task Scheduler).
* Easily customizable: add or remove profiles and links anytime.
* Works on Windows.

---

## 📁 Folder Structure

```
chrome-launcher/
├── chrome_launcher.py
├── README.md
```

---

## 🔧 Requirements

* Python 3.6+
* Windows OS
* Google Chrome installed at:

  ```
  C:\Program Files\Google\Chrome\Application\chrome.exe
  ```

---

## 🛠️ Setup

1. Clone or download the repository.

2. Open the file `chrome_launcher.py` and modify these variables:

   ```python
   CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
   BASE_USER_DATA = r"C:\Users\Good\AppData\Local\Google\Chrome\User Data"
   ```

3. Define your Chrome profiles and links:

   ```python
   chrome_profiles = {
       "Profile 6": ["https://youtube.com", "https://chatgpt.com"],
       "Default": ["https://instagram.com"]
   }
   ```

---

## ▶️ How to Run

From the command line:

```bash
python chrome_launcher.py
```

This will open all websites listed under each profile.

---

## ⏰ Automate Daily Launch (Optional)

You can automate this tool to run daily using **Windows Task Scheduler**:

1. Open Task Scheduler.
2. Create a new task.
3. Under **Actions**, set:

   ```
   Program/script: python
   Add arguments: "C:\Path\To\chrome_launcher.py"
   ```
4. Under **Triggers**, set it to run **Daily** at your preferred time.
5. Save and enable the task.

---

## 🧠 How to Find Your Chrome Profile Name

1. Open Chrome.
2. Visit: `chrome://version`
3. Check the **Profile Path** (e.g., `Profile 6`, `Default`, etc.)

---

## ✍️ Example

**Profile 6** opens:

* [https://chat.deepseek.com/](https://chat.deepseek.com/)
* [https://youtube.com/](https://youtube.com/)

**Default** opens:

* [https://chatgpt.com/](https://chatgpt.com/)
* [https://movielx.xyz/](https://movielx.xyz/)

---

## 📄 License

MIT — Support Our Work
Help us maintain and improve MovieLX by donating. Your support means a lot to us! ❤️

PayPal Donation
PayPal Account: ameermughal2002@gmail.com

PayPal
Donate via PayPal to use and modify.
https://www.movielx.xyz/p/contact-us.html
* [(https://movielx.xyz/](https://www.movielx.xyz/p/contact-us.html)
---

Let me know if you'd like a ready-to-use ZIP or `.bat` launcher too!
