import random

def get_templates():
    return [
        {
            "name": "Adventure",
            "prompts": ["noun", "adjective", "verb", "place", "celebrity", "animal", "emotion"],
            "template": """
    One day in {place}, a {adjective} {noun} decided to {verb} with {celebrity}.
    Suddenly, a wild {animal} appeared, feeling very {emotion}. {ending} 
    """
        },
        {
            "name": "Sci-Fi",
            "prompts": ["planet", "alien", "gadget", "superpower", "emotion"],
            "template": """
On the distant planet {planet}, a sneaky {alien} invented a {gadget} 
that granted {superpower}. The galaxy shook as they felt extremely {emotion}.
{ending}
            """
        },
    
    ]
    
def generate_story(words, template):
    emotion = words.get("emotion", "mysterious").lower()
    ending = {
        "happy": "and everyone lived happily ever after!",
        "sad": "but then it all fell apart..."
    }.get(emotion,"and that's how the cookie crumbled!")
    
    try:
        return template.format(**words, ending=ending)
    except KeyError as e:
        return f"Oops! Missing word: {e}"