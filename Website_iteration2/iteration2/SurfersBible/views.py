# from django.shortcuts import render
from django.shortcuts import render
from .models import *
from datetime import datetime 
import pytz
import json
import requests
import pandas as pd
from datetime import timedelta
# from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.
import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext
  
def water_temp_wet_suit_type_func(water_temperature_C):
    # calculate fahrenheit
    water_temperature_F = (water_temperature_C * 1.8) + 32.0
    
    if (water_temperature_F <= 58.0):
        return "Full Suit, Boots, Gloves and Hood"
    
    elif (water_temperature_F > 58.0) & (water_temperature_F <= 63.0):
        return "Full Suit and Boots"
    elif (water_temperature_F > 63.0) & (water_temperature_F <= 68.0):
        return "Full Suit"
    
    elif (water_temperature_F > 68.0) & (water_temperature_F <= 75.0):
        return "Top and Shorts"
    
    elif (water_temperature_F > 75.0) :
        return "Rash-guard"

def simplify_wave_period_func(wave_period):
    if (wave_period <= 5.0):
        return "Un-surfable"
    
    elif (wave_period > 5.0) & (wave_period <= 8.0):
        return "Weak"
    elif (wave_period > 8.0) & (wave_period <= 10.0):
        return "Average"
    
    elif (wave_period > 10.0) & (wave_period <= 12.0):
        return "Good"
    
    elif (wave_period > 12.0) :
        return "Excellent"
		
def simplify_wave_height_func(wave_height_m):
    wave_height_ft = wave_height_m / 0.3048
#     feet
    if (wave_height_ft > 0.0) & (wave_height_ft <= 1.0):
        return "Ankle to Knee"
    
    elif (wave_height_ft > 1.0) & (wave_height_ft <= 2.0):
        return "Knee to Thigh"
		
    elif (wave_height_ft > 2.0) & (wave_height_ft <= 3.0):
        return "Thigh to Waist"
    
    elif (wave_height_ft > 3.0) & (wave_height_ft <= 4.0):
        return "Waist to Chest"
    
    elif (wave_height_ft > 4.0) & (wave_height_ft <= 5.0):
        return "Chest to Head" 
    else:
        return "Above Head"
		

	
def index(request):
	return render(request=request,
				  template_name="SurfersBible/index.html")
				  

def board(request):
	dataset_path = r""
	# surf_board_df = pd.read_csv(dataset_path + "All_Las_Bambas_Assay_Method_SG_Data.xlsx")
	Wt_Vol_df = pd.read_excel('Surfboard_Reco_Datasets.xlsx', sheet_name = "Wt_Vol")
	print("Wt_Vol_df.shape = ", Wt_Vol_df.shape)
	Wt_Vol_df["Weight (Kg)"] = Wt_Vol_df["Weight (Kg)"].astype(str).apply(lambda x: x.strip())
	wt_dict = Wt_Vol_df.to_dict(orient='records')
	
	# surf_board_df = pd.read_csv(dataset_path + "All_Las_Bambas_Assay_Method_SG_Data.xlsx")
	Age_Factor_df = pd.read_excel(dataset_path + "Surfboard_Reco_Datasets.xlsx", 
                              sheet_name = "Age_Factor")
	print("Age_Factor_df.shape = ", Age_Factor_df.shape)
	Age_Factor_df["Age"] = Age_Factor_df["Age"].astype(str).apply(lambda x: x.strip())

	age_dict = Age_Factor_df.to_dict(orient='records')
	
	Fitness_Factor_df = pd.read_excel(dataset_path + "Surfboard_Reco_Datasets.xlsx", 
                              sheet_name = "Fitness_Factor")
	print("Fitness_Factor_df.shape = ", Fitness_Factor_df.shape)
	Fitness_Factor_df[['fitness_level','fitness_des']] = Fitness_Factor_df.Fitness.str.split("-",expand=True,)
	Fitness_Factor_df["fitness_level"] = Fitness_Factor_df["fitness_level"].astype(str).apply(lambda x: x.strip())
	Fitness_Factor_df["fitness_des"] = Fitness_Factor_df["fitness_des"].astype(str).apply(lambda x: x.strip())

	fitness_dict = Fitness_Factor_df.to_dict(orient='records')
	
	# surf_board_df = pd.read_csv(dataset_path + "All_Las_Bambas_Assay_Method_SG_Data.xlsx")
	surfboard_dimensions_df = pd.read_excel(dataset_path + "Surfboard_Reco_Datasets.xlsx", 
                              sheet_name = "surfboard_dimensions")
	print("surfboard_dimensions_df.shape = ", surfboard_dimensions_df.shape)
	surfboard_dict = surfboard_dimensions_df.to_dict(orient='records')
	return render(request=request,
				  template_name="SurfersBible/surfboard.html",
				  context={"weight" : json.dumps(wt_dict),
							"age" : json.dumps(age_dict),
							"fitness" : json.dumps(fitness_dict),
							"surfboard" : json.dumps(surfboard_dict)})
def emergency(request):
	if request.method == "POST":
		for key, value in request.POST.items():
			print(f'Key: {key}')
			print(f'Value: {value}')
		post_latitude = request.POST.get("latitude", "")
		post_longitude = request.POST.get("longitude","")
		post_service = request.POST.get("service","")
		print(post_latitude)
		print(post_longitude)
		print(post_service)
		hospital_table = HospitalTable.objects.values_list('hospital_formatted_address',flat=True).distinct('hospital_formatted_address').values()
		length_hos = len(hospital_table)
		print(length_hos)
		distance_hospital = ""
		
		for i in range(0,length_hos):
			if i == length_hos -1:
				distance_hospital = distance_hospital + str(hospital_table[i]['hospital_latitude']) + ','
				distance_hospital = distance_hospital + str(hospital_table[i]['hospital_longitude'])
			else:
				distance_hospital = distance_hospital + str(hospital_table[i]['hospital_latitude']) + ','
				distance_hospital = distance_hospital + str(hospital_table[i]['hospital_longitude']) + ';'
		# for beach in beaches_table:
				# print(beach)

		# print(len(d))
		# print(len(with_image_url_beach_df.objects.filter(country_state="Victoria").values()))
		origin = str(post_latitude) + "," + str(post_longitude)
		req_url = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins="+origin+"&destinations="+distance_hospital+"&travelMode=driving&key=Ak3-o8CO3qFVx_harLT-jG_GJDf1RWNrcwYZqgu_yhRB-3AwSmsGuaWwzTXxa5_5"
		distance_response = requests.get(req_url)
		print(distance_response.status_code)
		distance_recieved = distance_response.json()
		sorted_destinations = sorted(distance_recieved['resourceSets'][0]['resources'][0]['results'], key = lambda i: i['travelDistance']) 
		# print(sorted_destinations[:6])
		hospitals = []
		filter_ids = []
		for i in  range(0,len(sorted_destinations[:6])):
			hospital = {}
			for key, value in hospital_table[sorted_destinations[i]['destinationIndex']].items():
				if key=="hospital_id":
					filter_ids.append(value)
					s = []
					for each in HospitalServicesTable.objects.filter(hospital_id=value).values():
						# print(each)
						s.append(ServicesTable.objects.values_list("services",flat=True).get(services_id=each["services_id"]))
					hospital["services"] = s			
				# print(key,type(value))
				hospital[key] = value
				hospital['distance'] = sorted_destinations[i]['travelDistance']
			
			hospitals.append(hospital)
		
		print([h["services"]for h in hospitals])
		# print(len(hospitals))
		return render(request=request,
						template_name="SurfersBible/emergencyservice.html",
						context={"hospitals" : hospitals})
	return render(request=request,
				template_name="SurfersBible/locatione.html")

def shark(request):

	if request.method == "POST":
		
		# for key, value in request.POST.items():
			# print(f'Key: {key}')
			# print(f'Value: {value}')
		post_latitude = request.POST.get("latitude", "")
		post_longitude = request.POST.get("longitude", "")
		post_date = request.POST.get("selected date", "")
		post_hour = request.POST.get("myRange","")
		# print("lat: ",post_latitude)
		# print("lng:", post_longitude)
		print("selectedHour:", post_hour)
		if post_hour == "0":
			post_hour = "00"
		elif post_hour == "1":
			post_hour = "01"
		elif post_hour == "2":
			post_hour = "02"
		elif post_hour == "3":
			post_hour = "03"
		elif post_hour == "4":
			post_hour = "04"
		elif post_hour == "5":
			post_hour = "05"
		elif post_hour == "6":
			post_hour = "06"
		elif post_hour == "7":
			post_hour = "07"
		elif post_hour == "8":
			post_hour = "08"
		elif post_hour == "9":
			post_hour = "09"
		else:
			post_hour = post_hour

		aest = pytz.timezone('Australia/Victoria')
		if post_date == "Today":
			date_now = datetime.date(datetime.now(aest)).strftime("%Y-%m-%d")
			t = date_now+"T"+post_hour+":00:00"
			astronomy_time = date_now+"T10:00:00"
			print(t)
			print(date_now)
		elif post_date == "Tomorrow":
			date_now = datetime.date(datetime.now(aest) + timedelta(days=1)).strftime("%Y-%m-%d")
			print(date_now)
			t = date_now+"T"+post_hour+":00:00"
			astronomy_time = date_now+"T10:00:00"
			print(t)
		elif post_date == "Day After Tomorrow":
			date_now = datetime.date(datetime.now(aest) + timedelta(days=2)).strftime("%Y-%m-%d")
			print(date_now)
			t = date_now+"T"+post_hour+":00:00"
			astronomy_time = date_now+"T10:00:00"
			print(t)
		
		
		beaches_table = BeachTable.objects.all().values()
		length = len(beaches_table)
		# print(length)
		distance_beach_1 = ""
		distance_beach_2 = ""
		
		for i in range(0,int(length/2)):
			if i == int(length/2) -1:
				distance_beach_1 = distance_beach_1 + str(beaches_table[i]['beach_latitude']) + ','
				distance_beach_1 = distance_beach_1 + str(beaches_table[i]['beach_longitude'])
			else:
				distance_beach_1 = distance_beach_1 + str(beaches_table[i]['beach_latitude']) + ','
				distance_beach_1 = distance_beach_1 + str(beaches_table[i]['beach_longitude']) + ';'
				
		print("completed distance_beach_1")

		for i in range(int(length/2), length):
			if i == length -1:
				distance_beach_2 = distance_beach_2 + str(beaches_table[i]['beach_latitude']) + ','
				distance_beach_2 = distance_beach_2 + str(beaches_table[i]['beach_longitude'])
			else:
				distance_beach_2 = distance_beach_2 + str(beaches_table[i]['beach_latitude']) + ','
				distance_beach_2 = distance_beach_2 + str(beaches_table[i]['beach_longitude']) + ';'
		# for beach in beaches_table:
				# print(beach)

		print("completed distance_beach_2")

		# print(len(with_image_url_beach_df.objects.filter(country_state="Victoria").values()))
		origin = str(post_latitude) + "," + str(post_longitude)
		req_url_1 = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins="+origin+"&destinations="+distance_beach_1+"&travelMode=driving&key=Ak3-o8CO3qFVx_harLT-jG_GJDf1RWNrcwYZqgu_yhRB-3AwSmsGuaWwzTXxa5_5"
		distance_response_1 = requests.get(req_url_1)
		print(distance_response_1.status_code)
		distance_recieved_1 = distance_response_1.json()
		
		req_url_2 = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins="+origin+"&destinations="+distance_beach_2+"&travelMode=driving&key=Ak3-o8CO3qFVx_harLT-jG_GJDf1RWNrcwYZqgu_yhRB-3AwSmsGuaWwzTXxa5_5"
		distance_response_2 = requests.get(req_url_2)
		print(distance_response_2.status_code)
		distance_recieved_2 = distance_response_2.json()
		
		for i in distance_recieved_2['resourceSets'][0]['resources'][0]['results']:
			i['destinationIndex'] = i['destinationIndex']+100

		distance_recieved = distance_recieved_1['resourceSets'][0]['resources'][0]['results'] + distance_recieved_2['resourceSets'][0]['resources'][0]['results']
		
		sorted_destinations = sorted(distance_recieved, key = lambda i: i['travelDistance']) 
		# print(sorted(distance_recieved['resourceSets'][0]['resources'][0]['results'], key = lambda i: i['travelDistance']))
		# print(sorted_destinations)
		beaches_distance = []
		beaches = []
		filter_ids = []
		for i in  range(0,len(sorted_destinations[:20])):
			beach = {}
			for key, value in beaches_table[sorted_destinations[i]['destinationIndex']].items():
				if key=="beach_id":
					print(value)
					filter_ids.append(value)
					beach["airtemperature"] = SwellTable.objects.values_list("airtemperature",flat=True).filter(beach_id=value).filter(time=t)[0]
					beach["equipment_list"] = water_temp_wet_suit_type_func(SwellTable.objects.values_list("watertemperature",flat=True).filter(beach_id=value).filter(time=t)[0])
					# beach["water_quality"] = SeaWaterQualityTable.objects.values_list("ph",flat=True).filter(beach_id=value).filter(time=t)[0]
					beach["wave_period"] = simplify_wave_period_func(SwellTable.objects.values_list("waveperiod",flat=True).filter(beach_id=value).filter(time=t)[0])
					beach["wave_height"] = simplify_wave_height_func(SwellTable.objects.values_list("waveheight",flat=True).filter(beach_id=value).filter(time=t)[0])
					beach["htt"] = ExtremesHeightTable.objects.values_list("datetime",flat=True).filter(beach_id=value).filter(state="HIGH TIDE").filter(date = date_now)
					beach["htt"] = [datetime.strptime(i,"%Y-%m-%dT%H:%M:%S").strftime("%I:%M %p ") for i in beach["htt"]]
					beach["hth"] = ExtremesHeightTable.objects.values_list("height",flat=True).filter(beach_id=value).filter(state="HIGH TIDE").filter(date=date_now)
					beach["ltt"] = ExtremesHeightTable.objects.values_list("datetime",flat=True).filter(beach_id=value).filter(state="LOW TIDE").filter(date=date_now)
					beach["ltt"] = [datetime.strptime(i,"%Y-%m-%dT%H:%M:%S").strftime("%I:%M %p ") for i in beach["ltt"]]
					beach["lth"] = ExtremesHeightTable.objects.values_list("height",flat=True).filter(beach_id=value).filter(state="LOW TIDE").filter(date=date_now)
					beach["sunrise"] = datetime.strptime(AstronomyTable.objects.values_list("sunrise",flat=True).filter(beach_id=value).filter(time=astronomy_time)[0] ,"%Y-%m-%dT%H:%M:%S").strftime("%I:%M %p ")
					beach["sunset"] = datetime.strptime(AstronomyTable.objects.values_list("sunset",flat=True).filter(beach_id=value).filter(time=astronomy_time)[0] ,"%Y-%m-%dT%H:%M:%S").strftime("%I:%M %p ")
				beach[key] = value
				beach['distance'] = sorted_destinations[i]['travelDistance']
			
			beaches.append(beach)
			# beaches_table[sorted_destinations[i]['destinationIndex']].distance = sorted_destinations[i]['travelDistance']
			# print(sorted_destinations[i]['travelDistance'])
			# print(beaches_table[sorted_destinations[i]['destinationIndex']])
		
		print("hth:",len(beaches[0]["hth"]))
		print("htt:",len(beaches[0]["htt"]))
		print("lth:",len(beaches[0]["lth"]))
		print("ltt:",len(beaches[0]["hth"]))
		print(beaches[0])
			# print(sorted_destinations[i]['destinationIndex'])
			# print(type(sorted_destinations[i]['destinationIndex']))
		# prediction_table = join_weather_tide_df_07_05.objects.filter(country_state="Victoria").filter(date=date_now)
		prediction_table = SharkPredictionTable.objects.filter(beach__in=filter_ids).filter(date=date_now).values()
		# print(prediction_table)
		return render(request=request,
				  template_name="SurfersBible/explorebeach.html",
				  context={"beaches" : beaches,
							"prediction" : prediction_table,
							"post_date" : post_date,
							"post_hour" : post_hour})
	
	return render(request=request,
				  template_name="SurfersBible/locationb.html")
				  
def news(request):
	# "shark+australia"
	# "beach+jellyfish+australia"
	# "beach+rip+currents"
	# "beach+surfing+australia"
	# "surfing+guide"
	# "surfing+events"
	aest = pytz.timezone('Australia/Victoria')
	date_now = datetime.date(datetime.now(aest)).strftime("%Y-%m-%d")
	# print(date_now,type(date_now))
	all_news = NewsTable.objects.values_list('title',flat=True).distinct('title').filter(description__isnull=False).filter(url__isnull=False).filter(urltoimage__isnull=False).values()
	all_news = sorted(all_news, key=lambda x: datetime.strptime(x["publishedat"],"%Y-%m-%dT%H:%M:%S"), reverse=True)
	
	# print(len(all_news))
	# news = NewsTable.objects.filter(date="2020-05-16").values()
	# print(len(news))
	date_ex = datetime.strptime(all_news[0]["publishedat"],"%Y-%m-%dT%H:%M:%S")
	for each in all_news:
		each["publishedat"] = datetime.strptime(each["publishedat"],"%Y-%m-%dT%H:%M:%S").strftime("%I:%M %p %b %d, %Y")
		each["description"] = cleanhtml(each["description"])
	print(all_news[0])
	return render(request=request,
					template_name="SurfersBible/News.html",
					context = {"allnews" : all_news})
					
def sharknews(request):
	# "shark+australia"
	# "beach+jellyfish+australia"
	# "beach+rip+currents"
	# "beach+surfing+australia"
	# "surfing+guide"
	# "surfing+events"
	aest = pytz.timezone('Australia/Victoria')
	date_now = datetime.date(datetime.now(aest)).strftime("%Y-%m-%d")
	# print(date_now,type(date_now))
	s_news = NewsTable.objects.values_list('title',flat=True).distinct('title').filter(news_topic="shark+australia").filter(description__isnull=False).filter(url__isnull=False).filter(urltoimage__isnull=False).values()
	s_news = sorted(s_news, key=lambda x: datetime.strptime(x["publishedat"],"%Y-%m-%dT%H:%M:%S"), reverse=True)
	# print(len(all_news))
	# news = NewsTable.objects.filter(date="2020-05-16").values()
	# print(len(news))
	date_ex = datetime.strptime(s_news[0]["publishedat"],"%Y-%m-%dT%H:%M:%S")
	for each in s_news:
		each["publishedat"] = datetime.strptime(each["publishedat"],"%Y-%m-%dT%H:%M:%S").strftime("%I:%M %p %b %d, %Y")
		each["description"] = cleanhtml(each["description"])
		# each["description"] = cleanhtml(each["description"][0])
	print(s_news[0])
	return render(request=request,
					template_name="SurfersBible/SharkNews.html",
					context = {"allnews" : s_news})
					
def ripcurrentnews(request):
	# "shark+australia"
	# "beach+jellyfish+australia"
	# "beach+rip+currents"
	# "beach+surfing+australia"
	# "surfing+guide"
	# "surfing+events"
	aest = pytz.timezone('Australia/Victoria')
	date_now = datetime.date(datetime.now(aest)).strftime("%Y-%m-%d")
	# print(date_now,type(date_now))
	rc_news = NewsTable.objects.values_list('title',flat=True).distinct('title').filter(news_topic="beach+rip+currents").filter(description__isnull=False).filter(url__isnull=False).filter(urltoimage__isnull=False).values()
	rc_news = sorted(rc_news, key=lambda x: datetime.strptime(x["publishedat"],"%Y-%m-%dT%H:%M:%S"), reverse=True)
	# print(len(all_news))
	# news = NewsTable.objects.filter(date="2020-05-16").values()
	# print(len(news))
	date_ex = datetime.strptime(rc_news[0]["publishedat"],"%Y-%m-%dT%H:%M:%S")
	for each in rc_news:
		each["publishedat"] = datetime.strptime(each["publishedat"],"%Y-%m-%dT%H:%M:%S").strftime("%I:%M %p %b %d, %Y")
		each["description"] = cleanhtml(each["description"])
		# each["description"] = cleanhtml(each["description"][0])
	print(rc_news[0])
	return render(request=request,
					template_name="SurfersBible/ripcurrentNews.html",
					context = {"allnews" : rc_news})
					
def jellyfishnews(request):
	# "shark+australia"
	# "beach+jellyfish+australia"
	# "beach+rip+currents"
	# "beach+surfing+australia"
	# "surfing+guide"
	# "surfing+events"
	aest = pytz.timezone('Australia/Victoria')
	date_now = datetime.date(datetime.now(aest)).strftime("%Y-%m-%d")
	# print(date_now,type(date_now))
	jf_news = NewsTable.objects.values_list('title',flat=True).distinct('title').filter(news_topic="beach+jellyfish+australia").filter(description__isnull=False).filter(url__isnull=False).filter(urltoimage__isnull=False).values()
	jf_news = sorted(jf_news, key=lambda x: datetime.strptime(x["publishedat"],"%Y-%m-%dT%H:%M:%S"), reverse=True)
	# print(len(all_news))
	# news = NewsTable.objects.filter(date="2020-05-16").values()
	# print(len(news))
	date_ex = datetime.strptime(jf_news[0]["publishedat"],"%Y-%m-%dT%H:%M:%S")
	for each in jf_news:
		each["publishedat"] = datetime.strptime(each["publishedat"],"%Y-%m-%dT%H:%M:%S").strftime("%I:%M %p %b %d, %Y")
		each["description"] = cleanhtml(each["description"])
		# each["description"] = cleanhtml(each["description"][0])
	print(jf_news[0])
	return render(request=request,
					template_name="SurfersBible/jellyfishNews.html",
					context = {"allnews" : jf_news})								
					
def surfingnewsaustralia(request):
	# "shark+australia"
	# "beach+jellyfish+australia"
	# "beach+rip+currents"
	# "beach+surfing+australia"
	# "surfing+guide"
	# "surfing+events"
	aest = pytz.timezone('Australia/Victoria')
	date_now = datetime.date(datetime.now(aest)).strftime("%Y-%m-%d")
	# print(date_now,type(date_now))
	sa_news = NewsTable.objects.values_list('title',flat=True).distinct('title').filter(news_topic="beach+surfing+australia").filter(description__isnull=False).filter(url__isnull=False).filter(urltoimage__isnull=False).values()
	sa_news = sorted(sa_news, key=lambda x: datetime.strptime(x["publishedat"],"%Y-%m-%dT%H:%M:%S"), reverse=True)
	# print(len(all_news))
	# news = NewsTable.objects.filter(date="2020-05-16").values()
	# print(len(news))
	date_ex = datetime.strptime(sa_news[0]["publishedat"],"%Y-%m-%dT%H:%M:%S")
	for each in sa_news:
		each["publishedat"] = datetime.strptime(each["publishedat"],"%Y-%m-%dT%H:%M:%S").strftime("%I:%M %p %b %d, %Y")
		each["description"] = cleanhtml(each["description"])
		# each["description"] = cleanhtml(each["description"][0])
	print(sa_news[0])
	return render(request=request,
					template_name="SurfersBible/surfingausNews.html",
					context = {"allnews" : sa_news})	
					
def surfingcompetitionnews(request):
	# "shark+australia"
	# "beach+jellyfish+australia"
	# "beach+rip+currents"
	# "beach+surfing+australia"
	# "surfing+guide"
	# "surfing+events"
	aest = pytz.timezone('Australia/Victoria')
	date_now = datetime.date(datetime.now(aest)).strftime("%Y-%m-%d")
	# print(date_now,type(date_now))
	sc_news = NewsTable.objects.values_list('title',flat=True).distinct('title').filter(news_topic="surfing+events").filter(description__isnull=False).filter(url__isnull=False).filter(urltoimage__isnull=False).values()
	sc_news = sorted(sc_news, key=lambda x: datetime.strptime(x["publishedat"],"%Y-%m-%dT%H:%M:%S"), reverse=True)
	# print(len(all_news))
	# news = NewsTable.objects.filter(date="2020-05-16").values()
	# print(len(news))
	date_ex = datetime.strptime(sc_news[0]["publishedat"],"%Y-%m-%dT%H:%M:%S")
	for each in sc_news:
		each["publishedat"] = datetime.strptime(each["publishedat"],"%Y-%m-%dT%H:%M:%S").strftime("%I:%M %p %b %d, %Y")
		each["description"] = cleanhtml(each["description"])
		# each["description"] = cleanhtml(each["description"][0])
	print(sc_news[0])
	return render(request=request,
					template_name="SurfersBible/surfingcompNews.html",
					context = {"allnews" : sc_news})	
					
					
def error_404_view(request,exception):
	return render(request=request,
					template_name='SurfersBible/404error.html')
					
def error_500_view(request):
	return render(request=request,
					template_name='SurfersBible/500error.html')