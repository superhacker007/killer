from openai import OpenAI
from jinja2 import Template
import os , pdfplumber, requests, json, time, humanize

def read_cv(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            try:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            except UnicodeDecodeError:
                text += "[Error decoding text on this page]\n"
    return text

# Continue with the rest of the script...

def dosop(my_cv, course, university):

    cv_content = read_cv(my_cv)
    course = course
    university = university

    # Use the CV content to generate an SOP with GPT
    prompt_template = Template("""
    Based on the following CV content:
    
    {{ cv_content }}
    
    Write the main content of a Statement of Purpose for a {{course}} at the {{university}}. 
    The statement should be engaging and personalized, avoiding overly formal language. Exclude any greeting or closing phrases; provide only the content of the statement.
    
    The content should:
    - Be well-structured with clear paragraphs.
    - Include the applicant's motivations, relevant background, specific interests in the program, and future goals.
    - Be detailed and reflective of the applicant's passion and suitability for the program.
    - Minimum 1000 words
""")


    prompt = prompt_template.render(cv_content=cv_content, course=course,university=university)

    client = OpenAI(
        api_key = os.getenv("OPENAI_API_KEY")
    )

    completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    )

    sop = completion.choices[0].message.content.strip()


    sop_human = humanize.doit(sop)

    time.sleep(20)

    if sop_human == None:
        return sop
    else:
        return sop_human
        

    
    