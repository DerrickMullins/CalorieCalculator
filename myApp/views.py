from django.shortcuts import render, redirect
from .models import Food, Consume
from django.contrib.auth.decorators import login_required

# Create your views here.
# User must login
@login_required
def index(request):
	# if user adds food
	if request.method == "POST":
		# food_consumed = food just added
		food_consumed = request.POST['food_consumed']
		# get food_consumed
		consume = Food.objects.get(name=food_consumed)
		# get user
		user = request.user
		# instantiating consume class with user and food_consumed
		consume = Consume(user=user, food_consumed=consume)
		# save
		consume.save()
		foods = Food.objects.all()
	else:
		foods = Food.objects.all()

	consumed_food = Consume.objects.filter(user=request.user)
	context = {
		'foods': foods, 
		'consumed_food': consumed_food,
	}

	return render(request, 'myApp/index.html', context)

# model to delete consumed food
def delete_consume(request, id):
	consumed_food = Consume.objects.get(id=id)
	if request.method == 'POST':
		consumed_food.delete()
		return redirect('/')
	return render(request, 'myApp/delete.html')
