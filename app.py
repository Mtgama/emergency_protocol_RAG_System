# app.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import openai
import requests

app = FastAPI()

# API Keys
VECTORIZE_TOKEN = os.getenv("VECTORIZE_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ORGANIZATION_ID = os.getenv("ORGANIZATION_ID")
PIPELINE_ID = os.getenv("PIPELINE_ID")

openai.api_key = OPENAI_API_KEY

# Template & Static
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# HTML page
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API endpoint
@app.post("/chat")
async def chat_api(query: str = Form(...)):
    try:
        chunks = retrieve_relevant_chunks(query)
        response = generate_response(query, chunks)
        return JSONResponse({"response": response})
    except Exception as e:
        return JSONResponse({"response": f"❌ خطا: {str(e)}"})

def retrieve_relevant_chunks(question: str, num_results: int = 5):
    url = f"https://api.vectorize.io/v1/org/{ORGANIZATION_ID}/pipelines/{PIPELINE_ID}/retrieval"
    headers = {
        "Authorization": VECTORIZE_TOKEN,
        "Content-Type": "application/json"
    }
    payload = {"question": question, "numResults": num_results, "rerank": True}
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    result = response.json()
    return [(doc["text"], doc.get("similarity", 0)) for doc in result.get("documents", [])]

def generate_response(query: str, relevant_chunks):
    context = "\n\n".join([chunk for chunk, _ in relevant_chunks])
    prompt = f"""
    شما یک دستیار پزشکی تخصصی هستید که فقط بر اساس پروتکل‌های اورژانس زیر پاسخ می‌دهید...
    متن پروتکل‌ها:
    {context}
    سوال کاربر:
    {query}
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "شما یک دستیار پزشکی هستید که فقط بر اساس متن ارائه‌شده پاسخ می‌دهد."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()
