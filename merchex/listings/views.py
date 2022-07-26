from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing


def hello(request):
    bands =  Band.objects.all()

    return HttpResponse(f"""
    <h1>Hello Django!</h1>
    <p>Mes groupes préférés sont : </p>
    <ul>
        <li>{bands[0].name}</li>
        <li>{bands[1].name}</li>
        <li>{bands[2].name}</li>
    </ul>
    """)

def about(request):
    return HttpResponse('<h1>A propos !</h1> <p>Lorem ipsum blablabla !</p>')


def listings(request):

    listings =  Listing.objects.all()

    out = """<h1>Liste des articles</h1>
    <p>
        <ul>
    """

    for item in listings:
        out+=f"""
                <li>
                    {item.title}
                </li>
        """

    out+="""
        </ul>
    </p>
    """
    
    return HttpResponse(out)

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