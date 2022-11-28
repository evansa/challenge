import requests

  

def get_countries_from_api():
 
    BASE_URL = "https://countriesnow.space/api/v0.1/countries/capital"
     
    response = requests.get(BASE_URL)
    js = response.json()

    for i in js["data"]:
        country = i["name"]
        capital = i["capital"] or "Unknown"          
    
        """
        In a real world application, this should be written into  a DB or redis as the data does not change. 
        So, using a cached copy makes more sense rather than making api request on every page load. 

        For the purpose of this task, I have written the response to a text file so it can be tested easily without dependencies.
        """
        with open("countries.txt", "a") as f:
            f.write(f"{country}, {capital} \n")    

def get_countries_from_cache():
    countries = []
    try:
        with open('countries.txt') as f:
            for line in f:
                line = line.rstrip(' \n')
                line = line.split(', ')
                countries.append([line[0], line[1]])
            return countries
    except:  
        pass

def fetch_countries_and_capitals():
    data = get_countries_from_cache()

    if data is not None:
        return data
    else:
        get_countries_from_api()
        data = get_countries_from_cache()
    return data
