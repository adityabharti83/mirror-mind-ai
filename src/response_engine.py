from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='gpt2')
set_seed(42)

def generate_response(user_input, profile):
    tone = "peaceful" if profile.get("peaceful") == "yes" else "neutral"
    mood = "optimistic" if profile.get("positivity", 0) > 0 else "realistic"
    prompt = f"As a {tone}, {mood} person, how would you respond to: '{user_input}'?\nYou say:"
    output = generator(prompt, max_length=60, num_return_sequences=1)
    return output[0]['generated_text']
