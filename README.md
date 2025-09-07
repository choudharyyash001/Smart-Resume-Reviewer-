  # Smart-Resume-Reviewer-  An intelligent, user-friendly resume analysis tool built with Flask, powered by local LLMs via Ollama (LLaMA 3 or Gemma). It parses PDF resumes and delivers actionable, emoji-enhanced feedback across key sections like Education, Experience, Skills, and Formatting.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
  # Features
 Upload PDF resumes for instant review
 Local LLM integration via Ollama (LLaMA 3 / Gemma)
 Section-wise feedback with collapsible UI blocks
 Emoji mapping and ratings for intuitive UX
 Modular backend for easy model swapping
 Runs locally — no cloud dependency
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
 #Tech Stack
Layer               	Tools Used
Backend           	Python, Flask, Ollama
Models            	LLaMA 3 / Gemma (locally run)
Frontend          	HTML, CSS, JavaScript
UX Enhancers       	Emoji mapping, collapsible sections
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Installation
**Clone the repo
git clone https://github.com/your-username/smart-resume-reviewer.git
cd smart-resume-reviewer

**Set up virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

**Install dependencies
 pip install -r requirements.txt

**Run the Flask app
 flask run
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
 #Screenshots
 <img width="937" height="288" alt="image" src="https://github.com/user-attachments/assets/d26bcba0-c9de-4e12-8fd8-72d39117ccd3" />
<img width="937" height="354" alt="image" src="https://github.com/user-attachments/assets/91820e19-f7a0-47b7-8053-a916060ac7a6" />
<img width="944" height="816" alt="image" src="https://github.com/user-attachments/assets/926fe2ec-9eea-4aa8-976a-da05a26dfc71" />
<img width="926" height="837" alt="image" src="https://github.com/user-attachments/assets/13c2b194-a12d-4a80-99ef-c8b74372833b" />

------------------------------------------------------------------------------------------------------------------------------------------------------------------
# How It Works
User uploads a PDF resume.
Flask backend sends the resume text to the local LLM via Ollama.
Model returns structured feedback per section.
Frontend displays feedback with emojis and collapsible blocks.
------------------------------------------------------------------------------------------------------------------------------------------------------------------
