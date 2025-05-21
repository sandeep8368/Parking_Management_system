import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render

def index(request):
    return render(request, "html/index.html")


@csrf_exempt
def get_vehicle_info(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            vehicle_no = data.get("vehicle_no")
            print(f"Received vehicle_no: {vehicle_no}")

            url = "https://rto-vehicle-information-india.p.rapidapi.com/getVehicleChallan"
            headers = {
                "Content-Type": "application/json",
                "x-rapidapi-host": "rto-vehicle-information-india.p.rapidapi.com",
                "x-rapidapi-key": "528b90cef4mshda95b396748bf83p1b42ecjsnae627841bde8"  # Replace this
            }

            payload = {
                "vehicle_no": vehicle_no,
                "consent": "Y",
                "consent_text": "I hereby give my consent for Eccentric Labs API to fetch my information"
            }

            response = requests.post(url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            print(f"API response JSON: {data}")

            return JsonResponse(data, safe=False)

        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST requests allowed"}, status=405)
