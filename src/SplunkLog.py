def Save(price_pannel):
    my_str = "Flight information: Company = {0}, Flight = {1}, Aircraft Type = {2}, Takeoff City = {3}, Arrival City = {4}, Departure Time = {5}, Price = {6}, Query Time = {7}".format(\
                price_pannel.company, price_pannel.flight, price_pannel.aircraft_type, price_pannel.takeoff_city, price_pannel.arrival_city,
                price_pannel.departure_time, price_pannel.price, price_pannel.query_time)
    print (my_str)