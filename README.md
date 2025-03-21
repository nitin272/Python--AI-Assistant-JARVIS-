# 🚀 Jarvis AI Assistant

Welcome to **Jarvis AI**, your smart Python-based assistant that listens to hotwords and executes tasks accordingly! 🧠💡 It features **real-time voice activation**, **parallel processing**, and an **interactive web UI**. 🎤📢

---

## ✨ Features
- 🎙️ **Voice Activation** – Detects hotwords like *Jarvis* or *Alexa* and responds!
- ⚡ **Parallel Processing** – Runs multiple processes for smooth performance.
- 🌍 **Web UI Integration** – Interactive UI powered by **Eel**.
- 🛠️ **Custom Commands** – Easily extendable with new features.

---

## 📂 Project Structure
```
📦 jarvis-ai
├── 🚀 run.py               # Main script to start Jarvis
├── 🔥 main.py              # Initializes UI & system sounds
├── 🎤 test.py              # Hotword detection using Porcupine
├── ⚡ tempCodeRunnerFile.py # Temporary runner file (can be ignored)
├── 🗄️ jarvis.db            # Database file (if applicable)
├── 🛠️ engine/              # Core logic & feature modules
│   ├── 🎛️ feature.py       # Defines assistant features
│   ├── 📝 command.py       # Handles commands execution
│   ├── ⚙️ config.py        # Configuration settings
└── 🌐 www/                 # Web UI files (HTML, CSS, JS)
```

---

## 🛠️ Setup & Installation
### ✅ Prerequisites
Ensure you have **Python 3.8+** installed. Download it from [Python's official site](https://www.python.org/downloads/).

### 🔽 1. Clone the Repository
```sh
git clone https://github.com/your-repo/jarvis-ai.git
cd jarvis-ai
```

### 📦 2. Install Dependencies
First, update **pip**:
```sh
pip install --upgrade pip
```
Then, install all dependencies:
```sh
pip install -r requirements.txt
```
If `requirements.txt` is missing, install dependencies manually:
```sh
pip install eel pyaudio pvporcupine pyautogui
```

### 🚀 3. Running Jarvis AI
Start Jarvis by running:
```sh
python run.py
```
🔹 **This will:**
✅ Launch the **interactive UI** 🌐
✅ Start listening for hotwords (`Jarvis`, `Alexa`) 🎤
✅ Execute commands based on detected hotwords 🛠️

### ❌ 4. Stopping Jarvis
Press `Ctrl + C` in the terminal or simply close the **UI window**.

---

## 🛠️ How It Works
🚀 **run.py** launches **two parallel processes:**
1️⃣ `startJarvis()`: Initializes the assistant UI.
2️⃣ `listenHotword()`: Listens for hotwords and triggers commands.

🎤 **test.py** runs the **Porcupine engine** to detect hotwords like *Jarvis* or *Alexa* and trigger actions!

---

---

## 🤝 Contributing
Want to improve Jarvis AI? Fork the repo and start contributing! PRs are welcome! 🛠️💡

---

## 📜 License
📝 MIT License – Free to use & modify!

