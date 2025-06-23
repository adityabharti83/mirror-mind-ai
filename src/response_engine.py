from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='gpt2')
set_seed(42)

def generate_response(user_input, profile):
    prompt = f"User: {user_input}\nThoughts ({profile}):"
    response = generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']
    return response[len(prompt):].strip()
