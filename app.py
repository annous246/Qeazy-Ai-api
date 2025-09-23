from flask import Flask, request, jsonify
from summarizer.hf_script import summary
from chromaInit.chroma import collection

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Summarizer Running!"
@app.route("/categories",methods=["POST"])
def get_categories():
    categories=[]
    print("sending cats")
    if(request.method=="POST"):
        data = request.get_json()
        text = data.get("text")
        categories=collection.query(query_texts=text,n_results=3)
    print(categories)
    return jsonify({"categories":categories['documents'][0]})
    

@app.route("/summarize", methods=["POST"])
def summarize_text():
    data = request.get_json(force=True)
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400
    
    text = data["text"]
    try:
        result = summary(text)
        print(result)

        return jsonify({"summary": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(app,host="0.0.0.0", port=5001)
