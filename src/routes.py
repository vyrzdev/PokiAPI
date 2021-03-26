from . import app
from . import models
from flask import jsonify, send_file
from . import hostname


@app.route("/")
def random_poki():
    pipeline = [
        {"$sample": {"size": 1}}
    ]
    cursor = models.PokiPic.objects().aggregate(pipeline, )
    if not cursor.alive:
        return jsonify({
            "failed": "It appears the Pokimane database is empty!",
            "code": "EMPTY"
        }), 500
    for doc in cursor:
        poki_doc_json = doc
        continue

    poki_doc_id = str(poki_doc_json.get("_id"))
    return jsonify({
        "image_id": poki_doc_id,
        "image_url": f"{hostname}/image/{poki_doc_id}"
    })


@app.route("/image/<id>")
def get_specific_image(id: str):
    poki_doc = models.PokiPic.objects(id=id).first()
    if poki_doc is None:
        return jsonify({
            "failed": "This Pokimane pic doesn't exist!",
            "code": "NONEXISTENT"
        }), 404
    mimetype = f"image/{poki_doc.format}"
    return send_file(poki_doc.image, mimetype=mimetype, as_attachment=False)
