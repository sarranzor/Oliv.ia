attributes_mapping = {
    "AcceptsInsurance" : lambda v: (
        "Accepts insurance payments" if v 
        else "Does not accept insurance payments"
    ),
    "AgesAllowed" : lambda v: (
        "Accepts minimum age of 18" if str(v) == "18plus" 
        else "Accepts minimum age of 21" if str(v) == "21plus" 
        else "Accepts all ages"
    ),
    "Ambience.casual" : lambda v: (
        "Casual atmosphere" if str(v) == "True"
        else "Not a casual atmosphere" if str(v) == "False"
        else None
    ),
    "Ambience.classy" : lambda v: (
        "Classy atmosphere" if str(v) == "True"
        else "Not a classy atmosphere" if str(v) == "False"
        else None
    ),
    "Ambience.divey" : lambda v: (
        "Divey atmosphere" if str(v) == "True"
        else "Not a divey atmosphere" if str(v) == "False"
        else None
    ),
    "Ambience.hipster" : lambda v: (
        "Hipster atmosphere" if str(v) == "True"
        else "Not a hipster atmosphere" if str(v) == "False"
        else None
    ),
    "Ambience.intimate" : lambda v: (
        "Intimate atmosphere" if str(v) == "True"
        else "Not an intimate atmosphere" if str(v) == "False"
        else None
    ),
    "Ambience.romantic" : lambda v: (
        "Romantic atmosphere" if str(v) == "True"
        else "Not a romantic atmosphere" if str(v) == "False"
        else None
    ),
    "Ambience.touristy" : lambda v: (
        "Touristy atmosphere" if str(v) == "True"
        else "Not a touristy atmosphere" if str(v) == "False"
        else None
    ),
    "Ambience.trendy" : lambda v: (
        "Trendy atmosphere" if str(v) == "True"
        else "Not a trendy atmosphere" if str(v) == "False"
        else None
    ),
    "Ambience.upscale" : lambda v: (
        "Upscale atmosphere" if str(v) == "True"
        else "Not an upscale atmosphere" if str(v) == "False"
        else None
    ),
    "BestNights.monday" : lambda v: (
        "Best on Monday" if str(v) == "True"
        else None
    ),
    "BestNights.tuesday" : lambda v: (
        "Best on Tuesday" if str(v) == "True"
        else None
    ),
    "BestNights.wednesday" : lambda v: (
        "Best on Wednesday" if str(v) == "True"
        else None
    ),
    "BestNights.thursday" : lambda v: (
        "Best on Thursday" if str(v) == "True"
        else None
    ),
    "BestNights.friday" : lambda v: (
        "Best on Friday" if str(v) == "True"
        else None
    ),
    "BestNights.saturday" : lambda v: (
        "Best on Saturday" if str(v) == "True"
        else None
    ),
    "BestNights.sunday" : lambda v: (
        "Best on Sunday" if str(v) == "True"
        else None
    ),
    "BikeParking" : lambda v: (
        "Bike parking available" if str(v) == "True"
        else "No bike parking available" if str(v) == "False"
        else None
    ),
    "BusinessAcceptsBitcoin" : lambda v: (
        "Accepts Bitcoin" if str(v) == "True"
        else "Does not accept Bitcoin" if str(v) == "False"
        else None
    ),
    "BusinessAcceptsCreditCards" : lambda v: (
        "Accepts credit cards" if str(v) == "True"
        else "Does not accept credit cards" if str(v) == "False"
        else None
    ),
    "BusinessParking.garage" : lambda v: (
        "Garage parking available" if str(v) == "True"
        else "No garage parking available" if str(v) == "False"
        else None
    ),
    "BusinessParking.street" : lambda v: (
        "Street parking available" if str(v) == "True"
        else "No street parking available" if str(v) == "False"
        else None
    ),
    "BusinessParking.validated" : lambda v: (
        "Validated parking available" if str(v) == "True"
        else "No validated parking available" if str(v) == "False"
        else None
    ),
    "BusinessParking.lot" : lambda v: (
        "Lot parking available" if str(v) == "True"
        else "No lot parking available" if str(v) == "False"
        else None
    ),
    "BusinessParking.valet" : lambda v: (
        "Valet parking available" if str(v) == "True"
        else "No valet parking available" if str(v) == "False"
        else None
    ),
    "ByAppointmentOnly" : lambda v: (
        "By appointment only" if str(v) == "True"
        else "Not by appointment only" if str(v) == "False"
        else None
    ),
    "BYOB" : lambda v: (
        "Bring your own bottle available" if str(v) == "True"
        else "Bring your own bottle unavailable" if str(v) == "False"
        else None
    ),"BYOBCorkage" : lambda v: (
        "Bring your own bottle free" if str(v) == "Yes_free"
        else "Bring your own bottle with corkage fee" if str(v) == "Yes_corkage"
        else "Bring your own bottle unavailable" if str(v) == "No"
        else None
    ),
    "Corkage" : lambda v: (
        "Corkage fee available" if str(v) == "True"
        else "No corkage fee available" if str(v) == "False"
        else None
    ),
    "Caters" : lambda v: (
        "Caters available" if str(v) == "True"
        else "Does not cater" if str(v) == "False"
        else None
    ),
    "CoatCheck" : lambda v: (
        "Coat check available" if str(v) == "True"
        else "No coat check available" if str(v) == "False"
        else None
    ),
    "DietaryRestrictions.gluten_free" : lambda v: (
        "Gluten-free options available" if v
        else "No gluten-free options available"
    ),
    "DietaryRestrictions.kosher" : lambda v: (
        "Kosher options available" if v
        else "No kosher options available"
    ),
    "DietaryRestrictions.vegan" : lambda v: (
        "Vegan options available" if v
        else "No vegan options available"
    ),
    "DietaryRestrictions.vegetarian" : lambda v: (
        "Vegetarian options available" if v
        else "No vegetarian options available"
    ),
    "DietaryRestrictions.dairy-free" : lambda v: (
        "Dairy-free options available" if v
        else "No dairy-free options available"
    ),
    "DietaryRestrictions.halal" : lambda v: (
        "Halal options available" if v
        else "No halal options available"
    ),
    "DietaryRestrictions.soy-free" : lambda v: (
        "Soy-free options available" if v
        else "No soy-free options available"
    ),
    "DogsAllowed" : lambda v: (
        "Dogs allowed" if str(v) == "True"
        else "Dogs not allowed" if str(v) == "False"
        else None
    ),
    "DriveThru" : lambda v: (
        "Drive-thru available" if str(v) == "True"
        else "No drive-thru available" if str(v) == "False"
        else None
    ),
    "GoodForDancing" : lambda v: (
        "Good for dancing" if v
        else "Not good for dancing"
    ),
    "GoodForKids" : lambda v: (
        "Good for kids" if str(v) == "True"
        else "Not good for kids" if str(v) == "False"
        else None
    ),
    "GoodForMeal.breakfast" : lambda v: (
        "Good for breakfast" if str(v) == "True"
        else "Not good for breakfast" if str(v) == "False"
        else None
    ),
    "GoodForMeal.brunch" : lambda v: (
        "Good for brunch" if str(v) == "True"
        else "Not good for brunch" if str(v) == "False"
        else None
    ),
    "GoodForMeal.lunch" : lambda v: (
        "Good for lunch" if str(v) == "True"
        else "Not good for lunch" if str(v) == "False"
        else None
    ),
    "GoodForMeal.dinner" : lambda v: (
        "Good for dinner" if str(v) == "True"
        else "Not good for dinner" if str(v) == "False"
        else None
    ),
    "GoodForMeal.latenight" : lambda v: (
        "Good for late night" if str(v) == "True"
        else "Not good for late night" if str(v) == "False"
        else None
    ),
    "GoodForMeal.dessert" : lambda v: (
        "Good for dessert" if str(v) == "True"
        else "Not good for dessert" if str(v) == "False"
        else None
    ),
    "HappyHour" : lambda v: (
        "Happy hour available" if str(v) == "True"
        else "No happy hour available" if str(v) == "False"
        else None
    ),
    "HasTV" : lambda v: (
        "Has TV" if str(v) == "True"
        else "No TV" if str(v) == "False"
        else None
    ),
    "Music.background_music" : lambda v: (
        "Background music available" if v
        else "No background music available"
    ),
    "Music.dj" : lambda v: (
        "DJ available" if str(v) == "True"
        else "No DJ available" if str(v) == "False"
        else None
    ),
    "Music.jukebox" : lambda v: (
        "Jukebox available" if str(v) == "True"
        else "No jukebox available" if str(v) == "False"
        else None
    ),
    "Music.live" : lambda v: (
        "Live music available" if str(v) == "True"
        else "No live music available" if str(v) == "False"
        else None
    ),
    "Music.karaoke" : lambda v: (
        "Karaoke available" if str(v) == "True"
        else "No karaoke available" if str(v) == "False"
        else None
    ),
    "Music.video" : lambda v: (
        "Video available" if v
        else "No video available"
    ),
    "NoiseLevel" : lambda v: (
        f"Noise level is {v}" if v
        else None
    ),
    "Open24Hours" : lambda v: (
        "Open 24 hours" if v
        else "Not open 24 hours"
    ),
    "OutdoorSeating" : lambda v: (
        "Outdoor seating available" if str(v) == "True"
        else "No outdoor seating available" if str(v) == "False"
        else None
    ),
    "RestaurantsAttire" : lambda v: (
        "Casual attire" if str(v) == "Casual"
        else "Formal attire" if str(v) == "Formal"
        else "Dressy attire" if str(v) == "Dressy"
        else None
    ),
    "RestaurantsCounterService" : lambda v: (
        "Counter service available" if v
        else "No counter service available"
    ),
    "RestaurantsDelivery" : lambda v: (
        "Delivery avaiable" if str(v) == "True"
        else "Delivery unavaible" if str(v) == "False"
        else None
    ),
    "RestaurantsGoodForGroups" : lambda v: (
        "Good for groups" if str(v) == "True"
        else "Not good for groups" if str(v) == "False"
        else None
    ),
    "RestaurantsPriceRange2" : lambda v: (
        "Cheap price" if str(v) == "1"
        else "Medium price" if str(v) == "2"
        else "Expensive price" if str(v) == "3"
        else "Luxury price" if str(v) == "4"
        else None
    ),
    "RestaurantsReservations" : lambda v: (
        "Reservations avaiable" if str(v) == "True"
        else "Reservations not avaiable" if str(v) == "False"
        else None
    ),
    "RestaurantsTableService" : lambda v: (
        "Table service avaiable" if str(v) == "True"
        else "Table service not avaiable" if str(v) == "False"
        else None
    ),
    "RestaurantsTakeOut" : lambda v: (
        "Take out avaiable" if str(v) == "True"
        else "Take out not avaiable" if str(v) == "False"
        else None
    ),
    "Smoking" : lambda v: (
        "Smoking avaiable indoors" if str(v) == "Yes"
        else "Smoking only avaiable outdoors" if str(v) == "Outdoor"
        else "Smoking prohibited" if str(v) == "No"
        else None
    ),
    "WheelchairAccessible" : lambda v: (
        "Wheelchair accessible" if str(v) == "True"
        else "Not accesible for wheelchairs" if str(v) == "False"
        else None
    ),
    "WiFi" : lambda v: (
        "Free WiFi" if str(v) == "Free"
        else "Paid WiFi" if str(v) == "Paid"
        else "No WiFi" if str(v) == "No"
        else None
    )
}