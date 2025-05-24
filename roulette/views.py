from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from decimal import Decimal




def home(request):
    return render(request, 'roulette/home.html')


@csrf_exempt  # Allow AJAX requests
@login_required  # Make sure the user is logged in
def spin_result(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)  # Debug print
            bet_amount = Decimal(str(data.get('bet_amount')))
            bet_color = data.get('bet_color')
            winner_color = data.get('winner_color')
            print(f"bet_amount={bet_amount}, bet_color={bet_color}, winner_color={winner_color}")  # Debug print

            profile = request.user.profile

            if profile.money < bet_amount:
                return JsonResponse({'success': False, 'error': 'Not enough money to place this bet.'})

            if bet_color == winner_color:
                winnings = bet_amount
                profile.money += winnings
                message = f'You won! You earned ${winnings:.2f}.'
            else:
                profile.money -= bet_amount
                message = f'You lost ${bet_amount:.2f}. Better luck next time.'

            profile.save()

            return JsonResponse({'success': True, 'message': message, 'new_money': float(profile.money)})

        except Exception as e:
            print("Error:", e)  # Debug print error
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method.'})
