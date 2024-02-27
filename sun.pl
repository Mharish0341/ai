% Facts representing information about specific planets
planet(mercury, distance_sun(0.39), mass(0.0553)). % Distance in AU, Mass in Earth masses
planet(saturn, orbital_period(29.45), day_length(0.44)). % Orbital period in Earth years, Day length in Earth days

% Rule to find the distance between two planets based on their positions from the Sun
distance_between(Planet1, Planet2, Distance) :-
    planet(Planet1, distance_sun(Dist1), _),
    planet(Planet2, distance_sun(Dist2), _),
    Distance is abs(Dist1 - Dist2).
closer_to_sun_than_earth(Planet) :-
    planet(Planet, distance_sun(Dist), _),
    planet(earth, distance_sun(EarthDist), _),
    Dist < EarthDist.