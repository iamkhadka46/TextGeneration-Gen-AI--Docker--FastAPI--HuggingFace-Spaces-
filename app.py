from fastapi import FastAPI
from transformers import pipeline

## FastAPI Instance

app = FastAPI()

pipe = pipeline("text2text-generation", model="google/flan-t5-base")


@app.get("/")
async def home():
    return {"message": "Hello World"}

@app.get("/generate")
async def generate(text: str):
    output = pipe(text)

    return {"output": output[0]['generated_text']}