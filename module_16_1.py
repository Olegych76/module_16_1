from fastapi import FastAPI

app = FastAPI()

@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def get_user(user_id: int) -> dict:
    return {"Вы вошли как пользователь №": user_id}

@app.get("/user/")
async def user_info(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: '{username}', Возраст: {age}."}

@app.get("/")
async def root() -> dict:
    return {"message": "Главная страница"}
