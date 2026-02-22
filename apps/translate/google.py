from googletrans import Translator
from constants import LANGUAGES_MAP

translator = Translator()


async def translate(text: str, lang: str = "fon_Latn", to: str = "fra_Latn"):
    return (await translator.translate(text, src=LANGUAGES_MAP[lang], dest=LANGUAGES_MAP[to])).text