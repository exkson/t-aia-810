from fastapi import FastAPI, Response
from pydantic import BaseModel
from constants import SUPPORTED_LANGUAGES


from google import translate


app = FastAPI(title="Traduction FON - FRA", version="1.0")


class TranslationResponse(BaseModel):
    translation: str


@app.get("/api/v1/translate")
async def translate_endpoint(
    text: str, lang: str = "fon_Latn", to: str = "fra_Latn"
) -> TranslationResponse:
    if lang not in SUPPORTED_LANGUAGES or to not in SUPPORTED_LANGUAGES:
        return Response(
            content={
                "error": "Unsupported language. Supported languages are: "
                + ", ".join(SUPPORTED_LANGUAGES)
            },
            status_code=400,
        )
    translated_text = await translate(text, lang, to)
    return {"translation": translated_text}
