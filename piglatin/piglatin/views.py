from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request, 'home.html')


def translate(request):
    original_text = request.GET['text'].lower()
    translated_text = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for word in original_text.split():
        if word[0] in vowels:
            word += 'way '
        else:
            leftover_consonant = ''
            for letter in word:
                if letter in vowels:
                    break
                else:
                    leftover_consonant += letter
                    word = word[1:]
            word += leftover_consonant + 'ay '
        translated_text += word
    return render(request, 'translate.html', {'original': original_text, 'translated': translated_text})

