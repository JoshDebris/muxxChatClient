# muxxChatClient – Gemini Terminal ChatBot 🤖

A simple but powerful **Command-Line ChatBot** using **Google's Gemini API**, with stylish terminal output, spinner animations, and context-aware conversation flow. Fully customizable with API key management via `.env` file.

---

## ✨ Features
- Uses **Google Generative AI (Gemini 1.5 Flash)** for responses.
- Stylish Terminal UI with colors and spinner animations.
- Context-aware conversation (remembers the last 10 exchanges).
- API-Key is securely managed via `.env` file.
- Error handling included (Quota errors, API timeouts etc.).

---

## 🗂️ Project Files
```
muxxChatClient.py
.env.example
```

---

## 🚀 How to Use
1. Install required Python modules:
   ```bash
   pip install google-generativeai colored yaspin python-dotenv
   ```

2. Rename `.env.example` to `.env` and insert your Gemini API Key:
   ```env
   GENAI_API_KEY=your_real_api_key_here
   ```

3. Run the ChatClient:
   ```bash
   python muxxChatClient_optimized.py
   ```

4. Start chatting! (Type `exit` to leave the conversation.)

---

## 🖥️ Example Session
```
👽 Du: Hello there!
🤖 Bot: Hello! How can I assist you today?

👽 Du: Tell me a joke.
🤖 Bot: Why don’t skeletons fight each other? They don’t have the guts.
```

---

## 📖 License
MIT License – free to use, modify, and share.

---

## 🧰 TODO
- Save conversation history to a text file.
- Add different AI models for selection (Flash, Pro).
- Customizable conversation memory length.
