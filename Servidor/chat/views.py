from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai


class GC: 
    def __init__(self):
        genai.configure(api_key="AIzaSyCHqo2xJMsbc3MUkgGSXIqkehwQxzosa34")
        # self.gen_model = genai.GenerativeModel(model_name="tunedModels/unitaxx-dnpxjxbmqmcs")
        self.gen_model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    def ask(self, question):
        context = "Eres un asistente virtual llamado Unitaxx que va a estar interactuando con el usuario por medio de un chat de texto, contesta las preguntas de una manera de facil comprension y con una extension moderada de texto"
        
        response = self.gen_model.generate_content(context + question)

        return response.text

def process_text(request):
    if request.method == 'POST':
        prompt = request.POST.get('consulta', '') # TODO

        answer = GC()
        
        return JsonResponse(answer.ask(prompt))