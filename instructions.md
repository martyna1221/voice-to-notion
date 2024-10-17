# Product Brief: LinkedIn Post Generator from Voice Notes

## Overview
This project aims to create an automated pipeline that allows users to record voice notes, which are then transcribed and used to generate LinkedIn posts. The application will be containerized and deployed on Google Cloud Platform's Cloud Run (GCP CR).

## Key Requirements
1. Voice note recording functionality (on Streamlit UI)
2. Transcription of voice notes
3. LinkedIn post generation using LLM, inspired by sample posts
4. Containerization for GCP CR deployment
5. No data storage or user authentication required

## Existing Codebase Utilization
We can leverage significant portions of the existing codebase, which already includes voice recording and transcription functionality. The following modifications and additions will be necessary:

### 1. Streamlit Application
- Modify the existing Streamlit app to focus on LinkedIn post generation instead of ticket creation
- Update the UI to reflect the new functionality

### 2. Voice Recording and Transcription
- Retain the existing voice recording functionality
- Keep the transcription service integration

### 3. LLM Integration
- Replace the ticket creation logic with LinkedIn post generation
- Integrate sample LinkedIn posts as inspiration for the LLM
- Implement prompt engineering to guide the LLM in generating appropriate posts

### 4. Containerization
- Create a `Dockerfile` for containerizing the application
- Ensure all dependencies are listed in `requirements.txt`

### 5. Cloud Deployment
- Prepare the application for GCP CR deployment
- Create necessary configuration files for GCP CR

## File Structure and Modifications

1. `streamlit-app/applications/__init__.py`:
   - Update to reflect new LinkedIn post generation functionality

2. `.env`:
   - Add any new environment variables required for LinkedIn post generation and GCP deployment

3. `.gitignore`:
   - Ensure it includes necessary files for Docker and GCP

4. Create new files:
   - `Dockerfile`
   - `requirements.txt`
   - `linkedin_post_generator.py` (or similar) for the LLM-based post generation logic

5. Modify existing files:
   - Update `streamlit-app/applications/main.py` (or equivalent) to incorporate LinkedIn post generation flow

## Next Steps
1. Implement LinkedIn post generation logic [DONE]
2. Integrate sample LinkedIn posts as inspiration for the LLM [DONE]
3. Create Dockerfile and update requirements.txt [DONE]
4. Modify Streamlit app for new functionality [DONE]
5. Test containerized application locally [DONE]
6. Set up GCP CR and deploy the application
7. Perform end-to-end testing on the deployed application

## Notes
- This is a quick and dirty implementation without data storage or user authentication
- Ensure all necessary API keys and credentials are securely managed for cloud deployment
- Consider future enhancements such as user authentication and data persistence if required
