import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Feedback, Profile
from .forms import UserRegisterForm, ProfileRegisterForm

# Load environment variables from .env immediately on startup
load_dotenv()

def index(request):
    return render(request, 'index.html')

@login_required
def feedback(request):
    if request.method == "POST":
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_message = request.POST.get('message')
        feedback_entry = Feedback(name=user_name, email=user_email, message=user_message)
        feedback_entry.save()
        messages.success(request, "Thank you! Your feedback has been saved.")
        return redirect('feedback')
    return render(request, 'feedback.html')

def aisuggestions(request):
    return render(request, 'aisuggestions.html')

def about(request):
    return render(request, 'about.html')

def footer(request):
    return render(request, 'footer.html')

@login_required
def navbar(request):
    return render(request, 'navbar.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        p_form = ProfileRegisterForm(request.POST, request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save(commit=False)
            user.set_password(u_form.cleaned_data['password'])
            user.save()
            profile = p_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, f'Account created for {user.username}! You can now login.')
            return redirect('login')
    else:
        u_form = UserRegisterForm()
        p_form = ProfileRegisterForm()
    return render(request, 'register.html', {'u_form': u_form, 'p_form': p_form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('profile')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def terms(request):
    return render(request, 'terms.html')

def logout_view(request):
    auth_logout(request)
    return render(request, 'index.html')

def chat_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()
            if not user_message:
                return JsonResponse({'response': 'Please enter a message.'})

            # Fetch the API key
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                print("SERVER ERROR: GEMINI_API_KEY not found in environment!")
                return JsonResponse({'response': 'API key not configured on server. Check .env file.'}, status=500)

            genai.configure(api_key=api_key)

            model = genai.GenerativeModel(
                'gemini-2.5-flash',
                system_instruction=(
                    "You are a helpful family assistant. Your name is Buddy. "
                    "Keep your answers short, concise, and under 60 words. "
                    "You are here for the person who is very lonely and can't express their feelings to anyone so you are helpful for them. "
                    "You can answer in any language. You can generate the message in Hindi or Marathi text format. "
                    "You are an advanced AI chatbot. Analyze past context and give appropriate supportive answers."
                )
            )

            chat_response = model.generate_content(user_message)
            try:
                bot_reply = chat_response.text
            except ValueError:
                bot_reply = "I'm sorry, I can't answer that due to safety guidelines."

            return JsonResponse({'response': bot_reply})
        except Exception as e:
            print(f"SERVER ERROR: {e}")
            return JsonResponse({'response': f'Server error: {e}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required
def ai_assistant_view(request):
    return render(request, 'assistant.html')