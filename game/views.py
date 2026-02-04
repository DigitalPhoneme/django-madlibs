# game/views.py
from django.shortcuts import render
from django.views import View
from .story_generator import get_templates, generate_story
from .forms import MadLibsForm
import random

class HomeView(View):
    def get(self, request):
        return render(request, 'game/home.html')

class PlayView(View):
    def get(self, request):
        templates = get_templates()
        template = random.choice(templates)
        form = MadLibsForm(template['prompts'])
        return render(request, 'game/form.html', {
            'form': form,
            'template_name': template['name']
        })
    
    def post(self, request):
        print("POST request received!")
        print("POST data:", request.POST)
        template_name = request.POST.get('template_name')
        templates = get_templates()
        template = next((t for t in templates if t['name'] == template_name), None)
        if not template:
            # Handle error - fallback to random or error page
            template = random.choice(templates)
        
        form = MadLibsForm(template['prompts'], request.POST)
        
        if form.is_valid():
            print("Form is valid!")
            words = form.cleaned_data
            story = generate_story(words, template['template'])
            return render(request, 'game/result.html', {'story': story, 'template_name': template['name']})
        else:
            print("Form INVALID. Errors:", form.errors)
            return render(request, 'game/form.html', {
                'form': form,
                'template_name': template_name
            })