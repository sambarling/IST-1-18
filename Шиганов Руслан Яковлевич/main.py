import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, root_validator
import csv
import sys

app = FastAPI()

#запрос на получения данных для карты населения
@app.get("/info/neighbour/{x}/{y}")
async def root(x, y):
    try:
        map = 0
        number1 = x
        number2 = y
        with open("pars.csv", encoding='utf-8') as r_file:
            # Создаем объект reader, указываем символ-разделитель ";"
            file_reader = csv.reader(r_file, delimiter=";")
            # Считывание данных из CSV файла
            for row in file_reader:
                #поиск по координатам
                if number1 == row[1] and number2 == row[2]:
                    map = (row[4])
                if map == 0:
                    map = "Wrong coords"    
    except ValidationError as e:
        return {"error": str(e)}
    return {"population_map": map}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
