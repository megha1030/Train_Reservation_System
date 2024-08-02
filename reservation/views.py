from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Train, Ticket
from .forms import CustomUserCreationForm


# Create your views here.


def index(request):
    return render(request, 'index.html')

def train_search(request):
    return render(request, 'train_search.html')


@login_required
def bookings(request):
    user_tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'bookings.html', {'user_tickets': user_tickets})


User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'Registration failed: {str(e)}')
        else:
            # Log detailed form errors
            error_messages = form.errors.as_json()
            messages.error(request, f'Registration failed. Form errors: {error_messages}')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('train_search')  # Redirect to home page after login
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def train_details(request):
    if request.method == 'GET':
        source = request.GET.get('source')
        destination = request.GET.get('destination')
        if source and destination:
            trains = Train.objects.filter(start=source, end=destination)
            return render(request, 'train_details.html', {'trains': trains})
    # Handle invalid or no source/destination selected
    messages.error(request, 'Please select both source and destination.')
    return redirect('index')

def book_ticket(request, train_id):
    train = Train.objects.get(id=train_id)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        travel_class = request.POST['travel_class']
        journey_date = request.POST['journey_date']
        price = {
            'Sleeper': train.price_sleeper,
            '3AC': train.price_3ac,
            '2AC': train.price_2ac,
            '1AC': train.price_1ac,
        }[travel_class]
        ticket = Ticket.objects.create(
            user=request.user,
            train=train,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            travel_class=travel_class,
            journey_date=journey_date,
            price=price
        )
        messages.success(request, 'Ticket booked successfully!')
        return redirect('ticket', ticket_id=ticket.id)
    return render(request, 'book_ticket.html', {'train': train})

def ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'ticket.html', {'ticket': ticket})