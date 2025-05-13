### 🎬 YouTube Script Writing Tool

Generate YouTube video titles and scripts using AI (powered by LLMs + DuckDuckGo search) with a simple and elegant Streamlit interface.

---

## 🌟 Features

- 🧠 Uses LLMs (LLaMA 3.1 via Groq) to generate catchy titles and scripts
- 🔎 Incorporates live web search data using DuckDuckGo
- 🎨 Customize creativity and video length
- 💻 User-friendly Streamlit UI
- 🔐 API key management with session storage


## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/Zoya28/youtube-script-writer.git
cd youtube-script-writer
````

### 2. Set Up Virtual Environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the App

```bash
streamlit run app.py
```

---

## 🧪 Project Structure

```bash
├── app.py              # Frontend code with Streamlit
├── backend.py          # LLM and search logic
├── requirements.txt    # Python dependencies
├── .env                # API Key config (not included in Git)
├── README.md           # Project overview
└── youtube-logo.png    # App branding image
```

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **LangChain**
* **LLaMA 3.1 via Groq**
* **DuckDuckGo Search**
* **dotenv**

## 🧕 About Me

Built with love by **Zoya Qureshi** – final year engineering student, aspiring AI developer. 🌸

Let’s connect on [LinkedIn](https://www.linkedin.com/in/zoya28/) 💼


