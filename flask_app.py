from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "./data/flask_data.json"

# 載入資料（如果檔案存在）
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        store = json.load(f)
else:
    store = []

def save_to_file():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(store, f, ensure_ascii=False, indent=2)

@app.route("/hello", methods=["GET"])
def get_all():
    return jsonify(store), 200

@app.route("/hello", methods=["POST"])
def create_hello():
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "請提供 name 欄位"}), 400
    store.append({"name": name})
    save_to_file()  # ✅ 寫入檔案
    return jsonify({"message": f"已新增：{name}"}), 201

@app.route("/hello/<int:index>", methods=["PUT"])
def update_hello(index):
    if index < 0 or index >= len(store):
        return jsonify({"error": "索引不存在"}), 404
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "請提供 name 欄位"}), 400
    store[index]["name"] = name
    save_to_file()  # ✅ 寫入檔案
    return jsonify({"message": f"第 {index} 筆已更新為 {name}"}), 200

@app.route("/hello/<int:index>", methods=["DELETE"])
def delete_hello(index):
    if index < 0 or index >= len(store):
        return jsonify({"error": "索引不存在"}), 404
    deleted = store.pop(index)
    save_to_file()  # ✅ 寫入檔案
    return jsonify({"message": f"已刪除：{deleted['name']}"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
