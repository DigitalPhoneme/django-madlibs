import random

def get_templates():
    return [
        {
            "name": "Office Chaos",
            "prompts": ["job", "food", "emotion", "object", "celebrity", "verb"],
            "template": """
At work today, the {job} accidentally microwaved a {food}.
It exploded all over the {object} while {celebrity} watched.
Everyone felt very {emotion}, so naturally they decided to {verb}.
{ending}
"""
        },
        {
            "name": "Reality TV Drama",
            "prompts": ["name", "adjective", "object", "emotion", "verb", "place"],
            "template": """
Breaking news: {name} was voted off the {adjective} island
after throwing a {object} across the set in {place}.
They were extremely {emotion} and promised to {verb} next season.
{ending}
"""
        },
        {
            "name": "Fantasy Gone Wrong",
            "prompts": ["creature", "weapon", "adjective", "emotion", "food", "verb"],
            "template": """
The legendary {creature} pulled out a {adjective} {weapon}
to defend the kingdom… but got distracted by a {food}.
Feeling {emotion}, it chose to {verb} instead of fighting.
Honestly? Probably the right call.
{ending}
"""
        },
        {
            "name": "Awkward Date",
            "prompts": ["celebrity", "food", "place", "emotion", "object", "verb"],
            "template": """
My date with {celebrity} started great at {place},
until they ordered a {food} and pulled a {object} out of nowhere.
Things got {emotion}, so I had no choice but to {verb}.
Dating apps are exhausting.
{ending}
"""
        },
        {
            "name": "Apocalypse But Make It Dumb",
            "prompts": ["animal", "object", "celebrity", "emotion", "verb", "place"],
            "template": """
Scientists confirmed the apocalypse began when a {animal}
pressed a giant {object} while {celebrity} livestreamed it from {place}.
Humanity felt {emotion} and immediately tried to {verb}.
Honestly… we had a good run.
{ending}
"""
        },
        {
            "name": "Superhero Origin Story",
            "prompts": ["adjective", "animal", "substance", "superpower", "emotion", "verb"],
            "template": """
After being bitten by a {adjective} {animal}
and falling into a vat of {substance},
I gained the power of {superpower}.
I felt {emotion}, so obviously I decided to {verb}.
This is probably fine.
{ending}
"""
        }
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