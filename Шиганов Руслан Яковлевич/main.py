import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, root_validator
import geojson

app = FastAPI()


class Dot(BaseModel):
    x: float
    y: float


@app.get("/info/neighbour/{x}/{y}")
async def root(x, y):
    try:
        dot = Dot(x=x, y=y)
    except ValidationError as e:
        return {"error": str(e)}
    return {"dot_coordinate": str(dot)}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
