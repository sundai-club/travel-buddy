import openai

openai_client = openai.OpenAI()


def get_preferences(questionnaire):
    prompt = f"""
    Based on the following information, generate a list of types of activities, things to do, kind of places to visit 
    that a person would like to do based on the questionnaire they answered.
    
    Generate 10-12 preferences.

    {questionnaire}
    
    the output should be a json object with the following format:
    {{'preferences': [p_1, p_2, p_3, p_4, p_5, ...]}}

    output:
    """
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content
