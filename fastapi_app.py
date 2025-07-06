from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()
DATA_FILE = "./data/fastapi_data.json"

# 初始化 store：list of {"name": ...}
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        store = json.load(f)
else:
    store = []  # ✅ 改成 list

def save_to_file():
    print("💾 正在寫入 data.json 檔案...")
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(store, f, ensure_ascii=False, indent=2)

class NameRequest(BaseModel):
    name: str

# GET 所有資料
@app.get("/hello")
def read_all():
    return store

# POST 新增一筆資料
@app.post("/hello")
def create_name(request: NameRequest):
    store.append({"name": request.name})
    save_to_file()
    return {"message": f"已新增：{request.name}"}

# PUT 更新第 n 筆
@app.put("/hello/{index}")
def update_name(index: int, request: NameRequest):
    if index < 0 or index >= len(store):
        raise HTTPException(status_code=404, detail="資料不存在")
    store[index]["name"] = request.name
    save_to_file()
    return {"message": f"第 {index} 筆已更新為：{request.name}"}

# DELETE 刪除第 n 筆
@app.delete("/hello/{index}")
def delete_name(index: int):
    if index < 0 or index >= len(store):
        raise HTTPException(status_code=404, detail="資料不存在")
    deleted = store.pop(index)
    save_to_file()
    return {"message": f"已刪除：{deleted['name']}"}
