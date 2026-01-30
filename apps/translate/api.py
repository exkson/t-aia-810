from starlette.requests import Request
from starlette.applications import Starlette
from starlette.responses import JSONResponse

from translate_nllb import translate

app = Starlette()


@app.route("/translate", methods=["GET"])
async def translate_endpoint(request: Request):
    text = request.query_params.get("text", "")
    lang = request.query_params.get("lang", "en")
    to = request.query_params.get("to", "fr")

    translated_text = translate(text, lang, to)
    return JSONResponse({"translation": translated_text})
