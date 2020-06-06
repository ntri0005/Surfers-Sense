from django.shortcuts import render
from .models import join_weather_tide_df_27_04, with_image_url_beach_df, beach_hospital_df
from datetime import datetime 
import pytz
import json
# Create your views here.

def index(request):
	return render(request=request,
				  template_name="SurfersBible/index.html")


def shark(request):
	aest = pytz.timezone('Australia/Victoria')
	date_now = datetime.date(datetime.now(aest)).strftime("%Y-%m-%d")
	beaches_table = with_image_url_beach_df.objects.filter(country_state="Victoria")
	prediction_table = join_weather_tide_df_27_04.objects.filter(country_state="Victoria").filter(date=date_now)
	return render(request=request,
				  template_name="SurfersBible/shark.html",
				  context={"beaches" : beaches_table,
							"prediction": prediction_table})
				  

def prediction(request):

	if request.method == "POST":
			send={}
			print("hello")
			post_latitude = request.POST.get("latitude", "")
			post_longitude = request.POST.get("longitude","")
			post_name = request.POST.get("name","")
			print("lat",post_latitude)
			print("long",post_longitude)
			# state = json.loads(state.decode('utf8'))
			# request.session['state'] = state
			# print(post_latitude,post_longitude)
			beach1_table = join_weather_tide_df_27_04.objects.filter(latitude=float(post_latitude)).filter(longitude=float(post_longitude))
			i = 0
			for predict in beach1_table:
				i += 1
				data= {}
				data['date'] = predict.date
				data['percentage'] = predict.shark_attack_percentage
				data['SightingPercentage'] = predict.shark_sighting_percentage
				c = json.dumps(data)
				# print("dumped",d)
				d = json.loads(c)
				# print("loaded",r)/
				
				send[str(i)] = d
				
			print(float(post_latitude))
			beach_table = with_image_url_beach_df.objects.filter(beach_name=post_name)
			# print("joined",beach1_table)
			print("beach",beach_table)
			hospital_table = beach_hospital_df.objects.filter(beach_name=post_name).order_by("beach_hospital_distance_km")[:5]
			# hospital1_table = hospital_table.objects.all().order_by('beach_hospital_distance_km')
			print("hospital",hospital_table)
			# print("hospital",hospital1_table)
			return render(request=request,
						template_name="SurfersBible/prediction.html",
						context={"attack" : json.dumps(send),
								 "beach" : beach_table,
								 "hospitals" : hospital_table})
	
	else:
		message = "You have not selected beach, Please select one from shark page"
		return render(request=request,
						template_name="SurfersBible/noselection.html",
						context={"message" : message})