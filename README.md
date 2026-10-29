
# 🌍 Travel Guide Assistant

An AI-powered Travel Guide Assistant built using Python, LangChain, and Google Gemini to provide brief recommendations for tourist destinations.

## 🚀 Features

- AI-powered travel recommendations
- Google Gemini integration
- LangChain conversation management
- Secure API key management using environment variables
- AI-generated destination suggestions

## 🛠️ Technologies Used

- Python
- LangChain
- Google Gemini
- python-dotenv

## ⚙️ Setup Instructions

### 1. Install Dependencies

Install the required Python packages:

```bash
pip install -U langchain langchain-google-genai python-dotenv
```

### 2. Configure API Key

Create a `.env` file in your project directory and add your Gemini API key:

```env
GEMINI_API_KEY="your_api_key_here"
```

Get your API key from [Google AI Studio](https://aistudio.google.com/).

### 3. Project Structure

```text
travel-guide-assistant/
├── .env
├── .gitignore
└── README.md
```

## 💬 Example Usage

**SystemMessage:**

You are a travel guide who gives brief recommendations for tourist destinations.

**HumanMessage:**

Suggest top 3 places to visit in Japan.

## 📌 Example Output

1. **Tokyo** – Explore modern attractions, shopping districts, and Japanese culture.
2. **Kyoto** – Discover traditional temples, beautiful gardens, and historic streets.
3. **Mount Fuji** – Enjoy breathtaking mountain views and scenic landscapes.

*Note: The actual response may vary depending on the model's output.*

## 🧠 How It Works

1. Load environment variables using `load_dotenv()`.
2. Retrieve the Gemini API key using `os.getenv("GEMINI_API_KEY")`.
3. Initialize the Google Gemini chat model using LangChain's `init_chat_model()`.
4. Create a `SystemMessage` to define the assistant's role.
5. Create a `HumanMessage` containing the travel query.
6. Store both messages in a list.
7. Invoke the model using `invoke()` and display the response with `response.content`.

## 🔐 Security

Add the following entries to your `.gitignore` file:

```gitignore
.env
__pycache__/
*.pyc
.venv/
```

**Important:** Never share your Gemini API key publicly or commit your `.env` file to GitHub.

## 🎯 Learning Outcomes

- Understand LangChain chat model initialization.
- Learn how system and human messages work.
- Integrate Google Gemini with Python.
- Manage API keys securely using environment variables.
- Generate AI responses using LangChain.

## 🔮 Future Enhancements

- Personalized travel recommendations
- Travel itinerary planning
- Budget-based destination suggestions
- Hotel and restaurant recommendations
- Interactive travel assistant interface

## 📄 License

This project is intended for educational and learning purposes.
