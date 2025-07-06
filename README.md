# RESTful API 範例：Flask 與 FastAPI 比較

本專案包含兩個 Python API 範例：
- `flask_app.py`：使用 Flask 框架
- `fastapi_app.py`：使用 FastAPI 框架

兩者皆支援基本的 CRUD 操作，並將資料儲存在本機 JSON 檔案中。

請在終端機輸入以下指令，就可以獲取這個資料夾囉！

```bash
git clone https://github.com/EntropiaTsai/restfulapi_database.git
```

---

## 📦 環境需求

- Python 3.9+
- 安裝依賴套件（Flask 與 FastAPI）：

```bash
pip install flask fastapi uvicorn
```

---

## 🚀 啟動方式

### 🔸 Flask 版本

```bash
python flask_app.py
```

伺服器啟動後會運行於：  
👉 http://127.0.0.1:5000

---

### 🔸 FastAPI 版本

```bash
uvicorn fastapi_app:app --reload --port 8000
```

伺服器啟動後會運行於：  
👉 http://127.0.0.1:8000  
Swagger UI 測試介面：  
👉 http://127.0.0.1:8000/docs

---

## 🔧 API 路由說明（兩個版本功能一致）

| 方法   | 路徑                  | 功能說明               |
|--------|-----------------------|------------------------|
| GET    | `/hello`              | 取得所有資料           |
| POST   | `/hello`              | 新增一筆資料           |
| PUT    | `/hello/<index>`      | 根據 index 更新資料    |
| DELETE | `/hello/<index>`      | 根據 index 刪除資料    |

---

## 🧪 測試範例

### 🔹 Flask 測試範例

```bash
# 新增資料
curl -X POST -H "Content-Type: application/json" \
     -d '{"name": "小明"}' \
     http://127.0.0.1:5000/hello

# 更新第 0 筆資料
curl -X PUT -H "Content-Type: application/json" \
     -d '{"name": "小華"}' \
     http://127.0.0.1:5000/hello/0

# 刪除第 0 筆資料
curl -X DELETE http://127.0.0.1:5000/hello/0
```

---

### 🔹 FastAPI 測試範例

> 注意：FastAPI 的路由通常不使用 `<index>`，請根據你實作的版本為主。以下假設你使用列表儲存。

```bash
# 查詢目前資料（GET）
curl http://127.0.0.1:8000/hello

# 新增資料（POST）
curl -X POST -H "Content-Type: application/json" \
     -d '{"name": "小綠"}' \
     http://127.0.0.1:8000/hello

# 更新第 0 筆資料（PUT）
curl -X PUT -H "Content-Type: application/json" \
     -d '{"name": "小藍"}' \
     http://127.0.0.1:8000/hello/0

# 刪除第 0 筆資料（DELETE）
curl -X DELETE http://127.0.0.1:8000/hello/0
```

也可使用 Swagger UI 進行互動操作：  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 💾 資料儲存

- Flask 儲存於：`./data/flask_data.json`
- FastAPI 儲存於：`./data/fastapi_data.json`

所有新增、修改、刪除操作都會同步寫入檔案。

---

## 📚 Flask vs FastAPI 功能比較

| 項目        | Flask                     | FastAPI                     |
|-------------|---------------------------|-----------------------------|
| 啟動方式    | `python flask_app.py`     | `uvicorn fastapi_app:app`   |
| 文件支援    | 無內建，自行整合 Swagger | 內建 Swagger UI (`/docs`)  |
| 資料驗證    | 需手動檢查                | 自動使用 `pydantic` 處理   |
| 適合場景    | 小型專案、簡易 REST API   | 生產環境、速度效能導向     |

---

## 📝 備註

- 所有 `name` 都以字典格式儲存，例如：`{"name": "小明"}`
- 若使用 FastAPI，請務必透過 Swagger UI 測試 request body JSON 結構

---

歡迎依據需求選擇適合的框架來開發 RESTful API ✨

