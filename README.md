# Voice to Notion

This project allows you to convert voice inputs into Notion database entries using OpenAI's API.
![](https://voice-to-notion/Voice-to-TicketCreator.gif)

## Getting Started

Follow these steps to set up the project on your local machine.

### Prerequisites

- **Git**: Ensure you have Git installed to clone the repository.
- **Python**: Make sure Python is installed on your system.
- **FFmpeg**: Download and install FFmpeg for your OS from [here](https://ffmpeg.org/download.html). Unzip it and add the `/bin` directory to your system's PATH. Verify installation by running `ffmpeg -version` in your terminal.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/martyna1221/voice-to-notion.git
   ```

2. **Create an `.env` File**:
   Create a `.env` file in the root directory. Include your API keys as shown below (keys are censored for security):
   ```plaintext
   OPENAI_API_KEY=sk-***************
   NOTION_API_KEY=secret_***********
   NOTION_DB_ID=***********
   ```

3. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

4. **Install Dependencies**:
   Navigate to the `streamlit-app` directory and install the required packages:
   ```bash
   cd streamlit-app
   pip install -r requirements.txt
   ```

5. **Run the Application**:
   Launch the app on `localhost:8501`:
   ```bash
   streamlit run main.py
   ```

### Notes

- All Notion-related functions are commented out. Customize them as needed.
- Notion integration requires a couple of extra steps. Let me know if you need configuring those.

### Happy Coding!

Martyna Paruch, 2024