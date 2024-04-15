from fastapi import FastAPI

app = FastAPI()   

@app.get("/") 
async def get_main_route():     
  return {"healthy"}


