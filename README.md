# Savarkar-GPT

![Screenshot](Screenshot.png)

Savarkar-GPT is an AI-powered chatbot designed to answer questions about the ideology and works of **Vinayak Damodar Savarkar**. By leveraging Savarkar's books and writings, this project creates a knowledge base that allows users to explore his thoughts and philosophy interactively.

---

## 🚀 Features

- **AI-Powered Chatbot**: Ask questions about Savarkar's ideology, writings, and philosophy.
- **Knowledge Base**: Built using Savarkar's books, processed into a searchable database.
- **Streamlit UI**: A user-friendly interface for interacting with the chatbot.
- **Flask API**: Backend API to handle queries and generate responses.

---

## 📚 Project Structure

```
savarkar-gpt/
├── main.py               # Flask API backend
├── ui.py                 # Streamlit-based user interface
├── pdf_loader.py         # Utility to load and process PDF files
├── embedding_utils.py    # Embedding manager for ChromaDB
├── config.py             # Configuration file for models and paths
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🛠️ Installation and Setup

Follow these steps to set up and run the project:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/savarkar-gpt.git
cd savarkar-gpt
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up ChromaDB
Ensure ChromaDB is installed and configured. The project uses ChromaDB for managing the knowledge base.

### 4. Add Savarkar's Books
Place the PDF files of Savarkar's books in the project directory. Update the `pdf_path` in `main.py` to point to the correct file.

### 5. Run the Flask API
Start the backend API:
```bash
python main.py
```
The API will run at `http://127.0.0.1:5000`.

### 6. Run the Streamlit UI
Start the user interface:
```bash
streamlit run ui.py
```
The UI will be available at `http://localhost:8501`.

---

## 🧠 How It Works


### 📖 PDF Processing
- `pdf_loader.py` extracts text from Savarkar's books and splits it into manageable chunks.

### 🏛️ Knowledge Base
- The text chunks are stored in a **ChromaDB collection** for efficient querying.

### 🔍 Query Handling
- The **Flask API** processes user queries, retrieves relevant text from the knowledge base, and generates responses.

### 💬 Streamlit UI
- A simple and interactive interface for users to ask questions and view responses.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for more details.

