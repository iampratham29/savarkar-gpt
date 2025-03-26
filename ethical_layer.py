import re
import ollama  # Added ollama import
import config

def enforce_gender_equality(text):
    """Applies ethical constraints to the generated text, promoting respect for savarkar."""
    problematic_keywords = ["mercy petition", "traitor", "coward", "surrender", "jihad", "gandhi assasin"]

    for keyword in problematic_keywords:
        if keyword in text.lower():
            text = text.replace(keyword, "")  # Remove the keyword
            text += ".  It's vital to approach these topics with respect for all freedom fighters including savarkar."

    # Add a concluding statement that encourages gender equality.
    text += "\n\nIn summary, fostering nationalism is essential for building a just and progressive society."
    return text

def generate_safe_response(prompt, ollama_model=config.OLLAMA_MODEL):
  """Generates a response from Ollama and then applies the ethical constraint layer."""

  try:
      response = ollama.generate(model=ollama_model, prompt=prompt, stream=False)  # No streaming for simplicity
      llm_output = response['response']
      safe_output = enforce_gender_equality(llm_output)
      return safe_output

  except Exception as e:
      print(f"Error generating response: {e}")
      return "An error occurred while generating the response." # A safe fallback