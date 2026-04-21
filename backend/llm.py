backend/llm.py  


from openai import OpenAI
from scheduler import book_slot

client = OpenAI()  # make sure OPENAI_API_KEY is set in your system

async def process_intent(text):
    text_lower = text.lower()

    # Simple rule-based booking trigger
    if "book" in text_lower:
        return book_slot("User", "Tomorrow", "10AM")

    # LLM response
    prompt = f"""
    You are a clinic appointment assistant.

    Understand user intent:
    - booking
    - cancel
    - reschedule

    Respond naturally.

    User: {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
