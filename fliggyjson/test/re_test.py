str= "https:sijipiao.fliggy.com/ie/flight_search_result_poller.do?_ksTS=1544111304859_4610&callback=jsonp4611&supportMultiTrip=true&searchBy=1281&childPassengerNum=0&infantPassengerNum=0&searchJourney=[%7B'arrCityCode':%20'MEL',%20'depCityCode':%20'CGO',%20'depDate':%20'2018-12-23',%20'selectedFlights':%20[]%7D]&tripType=0&searchCabinType=0&agentId=-1"
import re
r = re.findall(r"\d{4}-\d{2}-\d{2}",str)
print(type(r))
print (r)