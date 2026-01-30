from transformers import pipeline
# import torch


def translate(text: str, lang: str, to: str) -> str:
    """
    Translates the given text from the source language to the target language using the specified model.

    Args:
        text (str): The text to be translated.
        lang (str): The source language code (e.g., 'en' for English).
        to (str): The target language code (e.g., 'fr' for French).
        model (str): The translation model to use. Defaults to DEFAULT_TRANSLATION_MODEL.

    Returns:
        str: The translated text.
    """

    pipe = pipeline(
        "image-text-to-text",
        model="google/translategemma-4b-it",
        device="cuda",
        # dtype=torch.bfloat16,
    )
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "source_lang_code": lang,
                    "target_lang_code": to,
                    "text": text,
                }
            ],
        }
    ]
    output = pipe(text=messages, max_new_tokens=200)
    return output[0]["generated_text"][-1]["content"]
