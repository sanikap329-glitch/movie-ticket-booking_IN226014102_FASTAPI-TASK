from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Movie Ticket Booking App 🎬"}