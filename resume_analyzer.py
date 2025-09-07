import fitz  # PyMuPDF
from ollama import chat
import logging

logging.basicConfig(level=logging.INFO)

# Emoji map for feedback sections
emoji_map = {
    "Structure": "📐",
    "Skills": "🛠️",
    "Experience": "💼",
    "Education": "🎓",
    "Projects": "🧪",
    "Languages": "🗣️",
    "Formatting and Tone": "🖋️",
    "Additional Suggestions": "✨"
}

def extract_text_from_pdf(filepath):
    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def analyze_resume(filepath):
    resume_text = extract_text_from_pdf(filepath)

    if not resume_text.strip():
        return {"Error": ["No readable text found in the PDF. Please upload a text-based resume."]}

    resume_text = resume_text[:3000]  # Trim for performance

    prompt = f"""
You're a professional resume reviewer. Analyze the following resume and return feedback in this exact format:

Section: [Section Name]
- [Point 1]
- [Point 2]

Only use this format. Do not include summaries, introductions, or paragraphs. Just list each section followed by bullet points.

Resume:
{resume_text}
"""

    try:
        response = chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )
        feedback_text = response["message"]["content"]

        feedback = {}
        current_section = None

        for line in feedback_text.splitlines():
            line = line.strip()
            if line.startswith("Section:"):
                raw_section = line.replace("Section:", "").strip()
                emoji = emoji_map.get(raw_section, "")
                current_section = f"{emoji} {raw_section}" if emoji else raw_section
                feedback[current_section] = []
            elif line.startswith("-") and current_section:
                feedback[current_section].append(line[1:].strip())
            elif current_section and line:
                feedback[current_section].append(line)

        if not feedback or all(len(v) == 0 for v in feedback.values()):
            return {"Gemma Feedback": ["The resume was processed, but the feedback format was unclear. Please try again with a cleaner resume or check formatting."]}

        return feedback

    except Exception as e:
        logging.error("Error during resume analysis", exc_info=True)
        return {"Error": [str(e)]}
