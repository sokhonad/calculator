from fastapi import FastAPI, HTTPException
app = FastAPI()
from fastapi.responses import StreamingResponse
import csv
from io import StringIO
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from calculator import Calculator
from database import SessionLocal, Operation, create_database
create_database() 

origins = ["*"]  

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)


@app.get("/")
def read_root():
    calculator = Calculator()
    result = calculator.calculate("3 4 + 5 *")
    return {"Hello": "World","resu" : result}


class CalculationRequest(BaseModel):
    expression: str

@app.post("/calculate")
def calculate(expression: CalculationRequest):
    db = SessionLocal()
    calculator = Calculator()
    try:
        expression = expression.expression
        result = calculator.calculate(expression)
        
        operation = Operation(expression=expression, result=result)
        db.add(operation)
        db.commit()

        return {"result": operation.result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=CalculationRequest(e))
    finally:
        db.close()

        

@app.get("/export_csv")
def export_csv():
    db_session = SessionLocal()
    operations = db_session.query(Operation).all()

    # Create a CSV string in memory
    csv_data = StringIO()
    writer = csv.writer(csv_data)

    # CSV Header
    writer.writerow(["Expression", "Result"])

    # CSV Data
    for operation in operations:
        writer.writerow([operation.expression, operation.result])

    db_session.close()

    # Reset the position in the StringIO to the beginning
    csv_data.seek(0)

    # Use StreamingResponse with content as the CSV string
    response = StreamingResponse(iter([csv_data.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = 'attachment; filename="operations.csv"'

    return response



