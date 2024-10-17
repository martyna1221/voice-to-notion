# Voice to LinkedIn Post Generator

This project is a branch of the original voice-to-notion project, focusing on converting voice inputs into LinkedIn posts using OpenAI's API.

## New Functionality

- Converts voice input into LinkedIn posts instead of Notion database entries
- Uses a corpus of LinkedIn post guidelines and samples to generate relevant content
- Generates multiple LinkedIn posts from a single voice input

## Getting Started

Follow these steps to set up the project on your local machine.

### Prerequisites

- **Git**: Ensure you have Git installed to clone the repository.
- **Python**: Make sure Python 3.9 or higher is installed on your system.
- **FFmpeg**: Download and install FFmpeg for your OS from [here](https://ffmpeg.org/download.html). Unzip it and add the `/bin` directory to your system's PATH. Verify installation by running `ffmpeg -version` in your terminal.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/martyna1221/voice-to-notion.git
   cd voice-to-notion
   git checkout linkedin-post
   ```

2. **Create an `.env` File**:
   Create a `.env` file in the root directory. Include your OpenAI API key as shown below:
   ```plaintext
   OPENAI_API_KEY=sk-***************
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

### Local Testing

To test the application locally:

1. Ensure your virtual environment is activated and you're in the `streamlit-app` directory.
2. Run the Streamlit app: `streamlit run main.py`
3. Open a web browser and go to `http://localhost:8501`
4. Click the "Click to record" button and speak your content
5. Click "Click to stop recording" when finished
6. The app will transcribe your audio and generate LinkedIn posts based on your input

### Docker Support

This project includes a Dockerfile for containerization. To build and run the Docker container:

1. Build the Docker image:
   ```bash
   docker build -t voice-to-linkedin .
   ```

2. Run the container:
   ```bash
   docker run -p 8080:8080 --env-file .env voice-to-linkedin
   ```

3. Access the application at `http://localhost:8080`

## Project Structure

- `streamlit-app/`: Main application directory
  - `main.py`: Streamlit application entry point
  - `applications/`: Contains core functionality
    - `chatgpt.py`: Handles interaction with OpenAI API
  - `corpus/`: Contains LinkedIn post guidelines and samples

## Notes

- This branch focuses on LinkedIn post generation and does not include Notion integration.
- The corpus files in the `streamlit-app/corpus/` directory are used to guide the AI in generating relevant LinkedIn posts.

## Contributing

Feel free to fork the repository and submit pull requests for any enhancements.

## License

This project is open-source and available under the MIT License.

Martyna Paruch, 2024
