from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>A propos !</h1> <p>Lorem ipsum blablabla !</p>')


def listings(request):
    return HttpResponse('''<h1>Liste des articles</h1>
    <p>
        <ul>
            <li>
                Article 1
            </li>
            <li>
                Article 2
            </li>
            <li>
                Article 3
            </li>
        </ul>
    </p>
    ''')

def contact(request):
    return HttpResponse('''<h1>Page de contact</h1> 
    <p>
        <form action="" method="get" class="form-example">
            <div>
                <label for="name"> Entrez votre nom : </label>
                <input type="text" name="name" id="name" required >
            </div>
            <div>
                <label for="email"> Entrez votre email : </label>
                <input type="email" name="email" id="email" required >
            </div>
            <div>
                <label for="message">Votre message : </label>
                <textarea name="message" id="message" rows=5 cols=10>
                Entrez ici votre message
                </textarea>
            </div>
        </form>
    </p>
    ''')