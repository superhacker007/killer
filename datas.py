import random

available_places_sydney = [
    ["place", "description", "city", "id"],
    ["Sydney Opera House", "Iconic performing arts venue with a distinctive sail-like design.", "Sydney", "1"],
    ["Sydney Harbour Bridge", "Famous bridge offering panoramic views of the city and harbour.", "Sydney", "2"],
    ["Bondi Beach", "World-renowned beach known for surfing, swimming, and beach culture.", "Sydney", "3"],
    ["Taronga Zoo", "Popular zoo located on Sydney Harbour, home to native Australian wildlife and exotic animals.", "Sydney", "4"],
    ["Royal Botanic Garden", "Historic botanical garden offering stunning views of Sydney Harbour.", "Sydney", "5"],
    ["The Rocks", "Historic area known for its markets, pubs, and colonial-era buildings.", "Sydney", "6"],
    ["Darling Harbour", "Vibrant waterfront area with shops, restaurants, museums, and entertainment venues.", "Sydney", "7"],
    ["Manly Beach", "Famous beach accessible by ferry, known for its surf culture and scenic walks.", "Sydney", "8"],
    ["Art Gallery of New South Wales", "Major public gallery featuring Australian, European, and Asian art.", "Sydney", "9"],
    ["Hyde Park", "Historic park in the heart of Sydney, known for its monuments and tree-lined avenues.", "Sydney", "10"],
    ["Queen Victoria Building", "Elegant 19th-century shopping center featuring a variety of boutiques and cafes.", "Sydney", "11"],
    ["Sydney Tower Eye", "Observation tower offering 360-degree views of Sydney and beyond.", "Sydney", "12"],
    ["Luna Park", "Heritage-listed amusement park on Sydney Harbour, known for its iconic entrance.", "Sydney", "13"],
    ["SEA LIFE Sydney Aquarium", "Aquarium showcasing Australia's marine life, including sharks, rays, and penguins.", "Sydney", "14"],
    ["WILD LIFE Sydney Zoo", "Zoo in Darling Harbour focusing on Australian wildlife.", "Sydney", "15"],
    ["Barangaroo Reserve", "Urban park with waterfront walkways, native gardens, and cultural spaces.", "Sydney", "16"],
    ["Museum of Contemporary Art Australia", "Museum dedicated to contemporary art, located in the historic Rocks area.", "Sydney", "17"],
    ["Circular Quay", "Major transport hub and tourist destination, with ferries to many of Sydney's attractions.", "Sydney", "18"],
    ["Watsons Bay", "Harbourside suburb known for its seafood restaurants and scenic coastal walks.", "Sydney", "19"],
    ["Bronte Beach", "Popular beach with a family-friendly atmosphere and beautiful coastal views.", "Sydney", "20"],
    ["Sydney Observatory", "Historic observatory offering stargazing sessions and exhibits on astronomy.", "Sydney", "21"]
]

available_places_toronto = [
    ["place", "description", "city", "id"],
    ["CN Tower", "Iconic tower offering panoramic views of the city and a glass floor experience.", "Toronto", "1"],
    ["Royal Ontario Museum", "Large museum showcasing art, world culture, and natural history.", "Toronto", "2"],
    ["Ripley's Aquarium of Canada", "Aquarium featuring marine life from across the world, with an underwater tunnel.", "Toronto", "3"],
    ["Toronto Islands", "Group of small islands with beaches, parks, and recreational activities.", "Toronto", "4"],
    ["Art Gallery of Ontario", "One of the largest art museums in North America, with a vast collection of Canadian and international art.", "Toronto", "5"],
    ["Casa Loma", "Gothic Revival-style mansion and garden, now a museum and landmark.", "Toronto", "6"],
    ["Distillery District", "Historic district known for its Victorian industrial architecture, art galleries, and restaurants.", "Toronto", "7"],
    ["St. Lawrence Market", "Historic market featuring fresh produce, specialty foods, and artisanal products.", "Toronto", "8"],
    ["Toronto Zoo", "One of the largest zoos in the world, home to over 5,000 animals.", "Toronto", "9"],
    ["Hockey Hall of Fame", "Museum dedicated to the history of ice hockey, with exhibits and interactive displays.", "Toronto", "10"],
    ["High Park", "Large park with trails, a zoo, playgrounds, and seasonal cherry blossoms.", "Toronto", "11"],
    ["Kensington Market", "Eclectic neighborhood known for its diverse shops, cafes, and street art.", "Toronto", "12"],
    ["Rogers Centre", "Multi-purpose stadium home to the Toronto Blue Jays, known for its retractable roof.", "Toronto", "13"],
    ["Ontario Science Centre", "Interactive science museum with hands-on exhibits and a planetarium.", "Toronto", "14"],
    ["Nathan Phillips Square", "Public square in front of Toronto City Hall, famous for its reflecting pool and 'Toronto' sign.", "Toronto", "15"],
    ["Toronto Eaton Centre", "Large shopping mall in the heart of downtown Toronto, with a wide variety of retailers.", "Toronto", "16"],
    ["Bata Shoe Museum", "Unique museum showcasing a collection of footwear from around the world.", "Toronto", "17"],
    ["Scarborough Bluffs", "Dramatic cliffs along Lake Ontario, offering scenic views and hiking opportunities.", "Toronto", "18"],
    ["Harbourfront Centre", "Cultural center on the waterfront, hosting events, art exhibitions, and performances.", "Toronto", "19"],
    ["Fort York", "Historic site featuring a preserved military fort from the War of 1812.", "Toronto", "20"],
    ["Yonge-Dundas Square", "Public square known for its vibrant atmosphere, large video displays, and events.", "Toronto", "21"]
]



available_places_vancouver = [
    ["place", "description", "city", "id"],
    ["Stanley Park", "Vancouver's largest urban park, known for its lush landscape and seawall.", "Vancouver", "1"],
    ["Granville Island", "Vibrant shopping district known for its public market, artisans, and eateries.", "Vancouver", "2"],
    ["Capilano Suspension Bridge", "Historic suspension bridge offering picturesque views of the forest below.", "Vancouver", "3"],
    ["Vancouver Aquarium", "A center for marine research, conservation, and marine animal rehabilitation.", "Vancouver", "4"],
    ["Grouse Mountain", "Popular location for skiing, hiking, and enjoying spectacular city views.", "Vancouver", "5"],
    ["Butchart Gardens", "Stunning floral display gardens with themed areas.", "Victoria", "6"],
    ["Royal BC Museum", "Museum showcasing British Columbia's natural and human history.", "Victoria", "7"],
    ["Whistler Blackcomb", "World-renowned ski resort offering a plethora of year-round outdoor activities.", "Whistler", "8"],
    ["Pacific Rim National Park Reserve", "Breathtaking coastal national park known for its hiking trails and surfing spots.", "Tofino", "9"],
    ["Okanagan Valley", "Region known for its wineries and fruit orchards, with lakes and mountains.", "Kelowna", "10"],
    ["Kootenay National Park", "National park featuring hot springs, hiking trails, and diverse ecosystems.", "Radium Hot Springs", "11"],
    ["Mount Robson Provincial Park", "Home to the highest peak in the Canadian Rockies, offering hiking and camping.", "Valemount", "12"],
    ["Yoho National Park", "Park known for its waterfalls, rock formations, and fossil beds.", "Field", "13"],
    ["Hell's Gate Airtram", "Airtram providing spectacular views of Fraser River's narrowest point.", "Boston Bar", "14"],
    ["Glacier National Park", "Park known for its extensive glacier coverage and alpine scenery.", "Revelstoke", "15"],
    ["Sun Peaks Resort", "Year-round resort offering skiing, golfing, and mountain biking.", "Kamloops", "16"],
    ["Gastown", "Historic neighborhood known for its whistling Steam Clock and Victorian architecture.", "Vancouver", "17"],
    ["Queen Elizabeth Park", "Horticultural jewel with quarry garden, arboretum, and scenic views.", "Vancouver", "18"],
    ["Science World", "Science museum in a geodesic dome with interactive & hands-on exhibits.", "Vancouver", "19"],
    ["The Royal Hudson Steam Train", "Heritage steam train offering scenic journeys along the coast.", "Squamish", "20"],
    ["Goat Range Provincial Park", "Remote park known for its pristine wilderness and wildlife viewing.", "Nelson", "21"]
]

available_places_quebec = [
    ["place", "description", "city", "id"],
    ["Château Frontenac", "Iconic castle-like hotel overlooking the St. Lawrence River, a UNESCO World Heritage Site.", "Quebec", "1"],
    ["Old Quebec", "Historic neighborhood with cobblestone streets, charming buildings, and centuries-old architecture.", "Quebec", "2"],
    ["Montmorency Falls", "Spectacular waterfall that is taller than Niagara Falls, with hiking trails and a cable car.", "Quebec", "3"],
    ["Plains of Abraham", "Large urban park and historic battlefield from the Seven Years' War.", "Quebec", "4"],
    ["Musée de la Civilisation", "Interactive museum showcasing the history and culture of Quebec.", "Quebec", "5"],
    ["Basilica of Sainte-Anne-de-Beaupré", "A large Roman Catholic basilica known for its beautiful architecture and pilgrimage significance.", "Quebec", "6"],
    ["Citadelle of Quebec", "Fortified military structure with stunning views of the city and guided tours.", "Quebec", "7"],
    ["Dufferin Terrace", "Scenic boardwalk offering panoramic views of the St. Lawrence River and Château Frontenac.", "Quebec", "8"],
    ["Parliament Building", "Home to the National Assembly of Quebec, with beautiful architecture and gardens.", "Quebec", "9"],
    ["Île d'Orléans", "Picturesque island known for its historic villages, farms, and local products like cider and maple syrup.", "Quebec", "10"],
    ["La Promenade Samuel-De Champlain", "Waterfront park with bike paths, art installations, and beautiful views along the St. Lawrence River.", "Quebec", "11"],
    ["Battlefields Park", "Expansive green space that is part of the Plains of Abraham, offering historical monuments and walking trails.", "Quebec", "12"],
    ["Petit Champlain", "Charming pedestrian street in Old Quebec, known for its boutiques, restaurants, and European feel.", "Quebec", "13"],
    ["Fortifications of Quebec", "Historic walls surrounding Old Quebec, offering a glimpse into the city's defensive past.", "Quebec", "14"],
    ["Aquarium du Québec", "Aquarium featuring marine animals from cold and warm water environments, including polar bears and walruses.", "Quebec", "15"],
    ["Mont-Sainte-Anne", "Popular ski resort and outdoor destination with year-round activities like hiking and mountain biking.", "Quebec", "16"],
    ["Observatoire de la Capitale", "Observation deck offering 360-degree views of Quebec City from the top of a skyscraper.", "Quebec", "17"],
    ["Place Royale", "Historic square in Old Quebec, known for its cobblestone streets and beautiful 17th-century buildings.", "Quebec", "18"],
    ["Parc de la Chute-Montmorency", "Park surrounding Montmorency Falls, with hiking trails, zip lining, and a suspension bridge.", "Quebec", "19"],
    ["Vieux-Port de Québec", "The old port area, featuring a bustling marketplace, waterfront views, and local vendors.", "Quebec", "20"]
]


available_places_albania = [
    ["place", "description", "city", "id"],
    ["Skanderbeg Square", "The main plaza in Tirana, known for its cultural landmarks and vibrant atmosphere.", "Tirana", "1"],
    ["National History Museum", "Albania's largest museum, showcasing the country's history from ancient times to modern day.", "Tirana", "2"],
    ["Et'hem Bey Mosque", "A historic mosque in Tirana, known for its stunning frescoes and cultural significance.", "Tirana", "3"],
    ["Bunk'Art", "A museum set in a Cold War bunker, offering insight into Albania's communist history.", "Tirana", "4"],
    ["Mount Dajti", "A popular mountain near Tirana, accessible by cable car, offering panoramic views and hiking trails.", "Tirana", "5"],
    ["The Blue Eye", "A natural spring with mesmerizing blue and turquoise waters, surrounded by lush greenery.", "Sarandë", "6"],
    ["Butrint National Park", "A UNESCO World Heritage site featuring ancient ruins from Greek, Roman, and Byzantine times.", "Sarandë", "7"],
    ["Ksamil Beach", "A beautiful beach with crystal-clear waters and small islands just off the coast.", "Ksamil", "8"],
    ["Berat Castle", "A historic castle offering stunning views of Berat, known as the 'City of a Thousand Windows.'", "Berat", "9"],
    ["Gjirokastër Castle", "One of Albania's largest castles, offering panoramic views of the city and historical exhibits.", "Gjirokastër", "10"],
    ["Apollonia Archaeological Park", "An ancient Greek city with well-preserved ruins, including a theater and temples.", "Fier", "11"],
    ["Llogara Pass", "A scenic mountain pass offering breathtaking views of the Albanian Riviera.", "Vlora", "12"],
    ["Durrës Amphitheatre", "One of the largest Roman amphitheaters in the Balkans, located in the coastal city of Durrës.", "Durrës", "13"],
    ["Rozafa Castle", "A hilltop castle with views over Shkodër and the surrounding rivers.", "Shkodër", "14"],
    ["Osumi Canyon", "A dramatic canyon known for its towering cliffs, waterfalls, and opportunities for rafting.", "Skrapar", "15"],
    ["Albanian Riviera", "A stunning coastal region with beautiful beaches, crystal-clear waters, and picturesque villages.", "Himara", "16"],
    ["Lake Ohrid", "One of Europe's oldest and deepest lakes, straddling the border between Albania and North Macedonia.", "Pogradec", "17"],
    ["Valbona Valley National Park", "A national park known for its rugged mountains, hiking trails, and pristine natural beauty.", "Valbona", "18"],
    ["Shëngjin Beach", "A popular beach destination with sandy shores and a vibrant atmosphere.", "Shëngjin", "19"],
    ["Pyramid of Tirana", "A controversial structure in Tirana, originally built as a museum, now a cultural landmark.", "Tirana", "20"],
    ["Theth National Park", "A remote national park known for its alpine scenery, waterfalls, and traditional mountain villages.", "Theth", "21"]
]

available_places_lisbon = [
    ["place", "description", "city", "id"],
    ["Belém Tower", "A historic tower on the banks of the Tagus River, symbolizing the Age of Discoveries.", "Lisbon", "1"],
    ["Jerónimos Monastery", "A UNESCO World Heritage site and stunning example of Manueline architecture.", "Lisbon", "2"],
    ["Praça do Comércio", "A grand public square by the Tagus River, surrounded by historic buildings and cafes.", "Lisbon", "3"],
    ["São Jorge Castle", "A medieval castle offering panoramic views over Lisbon and the Tagus River.", "Lisbon", "4"],
    ["Alfama District", "The oldest district of Lisbon, known for its narrow streets, Fado music, and cultural heritage.", "Lisbon", "5"],
    ["LX Factory", "A creative hub with art studios, restaurants, and shops in a former industrial complex.", "Lisbon", "6"],
    ["Lisbon Oceanarium", "One of the largest aquariums in Europe, featuring diverse marine life from around the world.", "Lisbon", "7"],
    ["Elevador de Santa Justa", "A striking iron elevator offering views over central Lisbon.", "Lisbon", "8"],
    ["Carmo Convent", "A partially ruined Gothic convent, preserved as a reminder of the 1755 earthquake.", "Lisbon", "9"],
    ["Museu Calouste Gulbenkian", "A renowned museum housing an impressive collection of ancient and modern art.", "Lisbon", "10"],
    ["Rossio Square", "A lively square in the heart of Lisbon, known for its wavy-patterned pavement and historic fountains.", "Lisbon", "11"],
    ["National Museum of Ancient Art", "Portugal's national museum featuring a vast collection of European and Portuguese art.", "Lisbon", "12"],
    ["Padrão dos Descobrimentos", "A monumental sculpture celebrating Portugal's explorers during the Age of Discoveries.", "Lisbon", "13"],
    ["Lisbon Cathedral", "The oldest church in the city, blending Romanesque, Gothic, and Baroque architectural styles.", "Lisbon", "14"],
    ["Fado Museum", "A museum dedicated to Fado music, Portugal's traditional soulful genre.", "Lisbon", "15"],
    ["Chiado District", "A cultural and shopping area with historic cafes, theaters, and boutiques.", "Lisbon", "16"],
    ["Parque das Nações", "A modern district along the riverfront, home to the Lisbon Oceanarium and Vasco da Gama Bridge.", "Lisbon", "17"],
    ["Vasco da Gama Bridge", "Europe’s longest bridge, spanning 17.2 km across the Tagus River.", "Lisbon", "18"],
    ["Gare do Oriente", "An architectural masterpiece and major transport hub designed by Santiago Calatrava.", "Lisbon", "19"],
    ["MAAT - Museum of Art, Architecture, and Technology", "A modern museum with innovative exhibits set along the waterfront.", "Lisbon", "20"],
    ["Parque Eduardo VII", "A large park offering scenic views over central Lisbon and the Tagus River.", "Lisbon", "21"]
]

hotels_lisbon = [
    ["city", "hotel", "address", "suburb", "telephone", "fax", "stars"],
    ["Lisbon", "Four Seasons Hotel Ritz Lisbon", "Rua Rodrigo da Fonseca 88 - 1099-039", "Avenidas Novas", "+351 21 381 1400", "+351 21 383 1783", "5-star"],
    ["Lisbon", "Altis Grand Hotel", "Rua Castilho 11 - 1269-072", "Santo António", "+351 21 310 6000", "+351 21 310 6099", "5-star"],
    ["Lisbon", "Pestana Palace Lisboa", "Rua Jau 54 - 1300-314", "Alcântara", "+351 21 361 5600", "+351 21 361 5678", "5-star"],
    ["Lisbon", "The Lumiares Hotel & Spa", "Rua do Diário de Notícias 142 - 1200-146", "Bairro Alto", "+351 21 116 0200", "+351 21 116 0300", "5-star"],
    ["Lisbon", "Memmo Alfama Hotel", "Travessa das Merceeiras 27 - 1100-348", "Alfama", "+351 21 049 5660", "+351 21 049 5661", "5-star"],
    ["Lisbon", "Corinthia Lisbon", "Avenida Columbano Bordalo Pinheiro 105 - 1099-031", "Sete Rios", "+351 21 723 6363", "+351 21 724 4070", "5-star"],
    ["Lisbon", "Tivoli Avenida Liberdade Lisboa", "Avenida da Liberdade 185 - 1269-050", "Avenida da Liberdade", "+351 21 319 8900", "+351 21 319 8989", "5-star"],
    ["Lisbon", "Hotel Avenida Palace", "Rua 1º de Dezembro 123 - 1200-360", "Rossio", "+351 21 321 8100", "+351 21 321 8181", "5-star"],
    ["Lisbon", "InterContinental Lisbon", "Rua Castilho 149 - 1099-034", "Amoreiras", "+351 21 381 8700", "+351 21 384 7361", "5-star"],
    ["Lisbon", "Myriad by SANA Hotels", "Cais das Naus, Lote 2.21.01 - 1990-173", "Parque das Nações", "+351 21 302 3100", "+351 21 302 3199", "5-star"],
    ["Lisbon", "Sofitel Lisbon Liberdade", "Avenida da Liberdade 127 - 1269-038", "Avenida da Liberdade", "+351 21 322 8300", "+351 21 322 8399", "5-star"],
    ["Lisbon", "EPIC SANA Lisboa Hotel", "Avenida Engenheiro Duarte Pacheco 15 - 1070-100", "Amoreiras", "+351 21 159 7300", "+351 21 159 7400", "5-star"],
    ["Lisbon", "Altis Belém Hotel & Spa", "Doca do Bom Sucesso - 1400-038", "Belém", "+351 21 040 0200", "+351 21 040 0300", "5-star"],
    ["Lisbon", "NH Collection Lisboa Liberdade", "Avenida da Liberdade 180-B - 1250-146", "Avenida da Liberdade", "+351 21 351 4060", "+351 21 351 4061", "4-star"],
    ["Lisbon", "Lisboa Carmo Hotel", "Rua da Oliveira ao Carmo 1 - 1200-307", "Chiado", "+351 21 326 4707", "+351 21 326 4799", "4-star"],
    ["Lisbon", "Bairro Alto Hotel", "Praça Luís de Camões 2 - 1200-243", "Bairro Alto", "+351 21 340 8288", "+351 21 340 8280", "5-star"],
    ["Lisbon", "Olissippo Lapa Palace", "Rua do Pau de Bandeira 4 - 1249-021", "Lapa", "+351 21 394 9494", "+351 21 395 0024", "5-star"],
    ["Lisbon", "The Ivens Hotel", "Rua Capelo 5 - 1200-224", "Chiado", "+351 21 246 0111", "+351 21 246 0122", "5-star"],
    ["Lisbon", "Dom Pedro Lisboa", "Avenida Engenheiro Duarte Pacheco 24 - 1070-110", "Amoreiras", "+351 21 389 6600", "+351 21 387 7100", "5-star"],
    ["Lisbon", "Palácio do Governador", "Rua Bartolomeu Dias 117 - 1400-031", "Belém", "+351 21 040 3600", "+351 21 040 3699", "5-star"]
]


hotels_sydney = [
    ["city", "hotel", "address", "suburb", "telephone", "fax", "stars"],
    ["Sydney", "Shangri-La Hotel Sydney", "176 Cumberland Street - 2000", "The Rocks", "+61 2 9250 6000", "+61 2 9250 6250", "5-star"],
    ["Sydney", "The Langham Sydney", "89-113 Kent Street - 2000", "Millers Point", "+61 2 9256 2222", "+61 2 8248 5201", "5-star"],
    ["Sydney", "Four Seasons Hotel Sydney", "199 George Street - 2000", "The Rocks", "+61 2 9250 3100", "+61 2 9250 3299", "5-star"],
    ["Sydney", "Park Hyatt Sydney", "7 Hickson Road - 2000", "The Rocks", "+61 2 9256 1234", "+61 2 9256 1555", "5-star"],
    ["Sydney", "InterContinental Sydney", "117 Macquarie Street - 2000", "Sydney", "+61 2 9253 9000", "+61 2 9253 9111", "5-star"],
    ["Sydney", "The Star Grand Hotel and Residences Sydney", "80 Pyrmont Street - 2009", "Pyrmont", "+61 2 9777 9000", "+61 2 9777 9099", "5-star"],
    ["Sydney", "Sofitel Sydney Darling Harbour", "12 Darling Drive - 2000", "Darling Harbour", "+61 2 8388 8888", "+61 2 8388 8899", "5-star"],
    ["Sydney", "The Darling at The Star", "80 Pyrmont Street - 2009", "Pyrmont", "+61 2 9777 9000", "+61 2 9777 9999", "5-star"],
    ["Sydney", "Hilton Sydney", "488 George Street - 2000", "Sydney", "+61 2 9266 2000", "+61 2 9266 2088", "5-star"],
    ["Sydney", "Hyatt Regency Sydney", "161 Sussex Street - 2000", "Sydney", "+61 2 8099 1234", "+61 2 9290 3838", "5-star"],
    ["Sydney", "QT Sydney", "49 Market Street - 2000", "Sydney", "+61 2 8262 0000", "+61 2 8262 0001", "5-star"],
    ["Sydney", "Sheraton Grand Sydney Hyde Park", "161 Elizabeth Street - 2000", "Sydney", "+61 2 9286 6000", "+61 2 9286 6888", "5-star"],
    ["Sydney", "Pullman Quay Grand Sydney Harbour", "61 Macquarie Street - 2000", "Circular Quay", "+61 2 9256 4000", "+61 2 9256 4066", "5-star"],
    ["Sydney", "Rydges Sydney Harbour", "55 George Street - 2000", "The Rocks", "+61 2 9251 6711", "+61 2 9251 3773", "4-star"],
    ["Sydney", "The Fullerton Hotel Sydney", "1 Martin Place - 2000", "Sydney", "+61 2 8223 1111", "+61 2 8223 1110", "5-star"],
    ["Sydney", "Meriton Suites World Tower", "95 Liverpool Street - 2000", "Sydney", "+61 2 8263 8888", "+61 2 8263 8889", "5-star"],
    ["Sydney", "Sir Stamford at Circular Quay", "93 Macquarie Street - 2000", "Sydney", "+61 2 9252 4600", "+61 2 9252 5633", "5-star"],
    ["Sydney", "Ovolo Woolloomooloo", "6 Cowper Wharf Roadway - 2011", "Woolloomooloo", "+61 2 9331 9000", "+61 2 9331 9001", "5-star"],
    ["Sydney", "The Westin Sydney", "1 Martin Place - 2000", "Sydney", "+61 2 8223 1111", "+61 2 8223 1200", "5-star"],
    ["Sydney", "Radisson Blu Plaza Hotel Sydney", "27 O'Connell Street - 2000", "Sydney", "+61 2 8214 0000", "+61 2 8214 0001", "5-star"]
]


hotels_albania = [
    ["city", "hotel", "address", "suburb", "telephone", "fax", "stars"],
    ["Tirana", "Rogner Hotel Tirana", "Bulevardi Dëshmorët e Kombit - 1001", "Blloku", "+355 4 223 5035", "+355 4 223 5078", "5-star"],
    ["Tirana", "Tirana International Hotel & Conference Centre", "Skanderbeg Square 8 - 1001", "City Center", "+355 4 223 4185", "+355 4 222 2719", "4-star"],
    ["Tirana", "Maritim Hotel Plaza Tirana", "Rruga 28 Nëntori - 1001", "City Center", "+355 4 222 2100", "+355 4 222 2101", "5-star"],
    ["Tirana", "Mak Albania Hotel", "Sheshi Italia - 1001", "City Center", "+355 4 227 4707", "+355 4 227 4710", "5-star"],
    ["Tirana", "Hotel Opera", "Rruga Urani Pano - 1001", "City Center", "+355 4 227 0955", "+355 4 227 0956", "4-star"],
    ["Tirana", "Hotel Colosseo Tirana", "Rruga e Dibrës - 1001", "City Center", "+355 4 222 3113", "+355 4 222 3114", "4-star"],
    ["Tirana", "Mondial Hotel", "Rruga Muhamet Gjollesha - 1001", "City Center", "+355 4 223 2372", "+355 4 223 2375", "4-star"],
    ["Tirana", "Grand Hotel & Spa Tirana", "Bulevardi Dëshmorët e Kombit - 1001", "Blloku", "+355 4 225 1172", "+355 4 225 1173", "5-star"],
    ["Tirana", "Hotel Boutique Kotoni", "Rruga Donika Kastrioti - 1001", "Blloku", "+355 4 227 4407", "+355 4 227 4408", "4-star"],
    ["Tirana", "Hotel Vila Alba", "Rruga Xhorxhi Martini - 1001", "City Center", "+355 4 224 7295", "+355 4 224 7296", "4-star"],
    ["Tirana", "Sar'Otel Boutique Hotel", "Rruga Kostandin Kristoforidhi 1 - 1001", "City Center", "+355 4 226 7890", "+355 4 226 7891", "4-star"],
    ["Tirana", "Hotel Tafaj", "Rruga Mine Peza - 1001", "City Center", "+355 4 222 7531", "+355 4 222 7532", "3-star"],
    ["Tirana", "Hotel Doro City", "Rruga Muhamet Gjollesha - 1001", "City Center", "+355 4 223 2021", "+355 4 223 2022", "4-star"],
    ["Tirana", "Capital Tirana Hotel", "Rruga Qemal Stafa - 1001", "City Center", "+355 4 224 3470", "+355 4 224 3471", "3-star"],
    ["Tirana", "Sky Tower Hotel", "Rruga Deshmoret e 4 Shkurtit - 1001", "Blloku", "+355 4 225 9577", "+355 4 225 9578", "4-star"],
    ["Tirana", "Hotel Baron", "Rruga Elbasanit - 1001", "City Outskirts", "+355 4 238 2398", "+355 4 238 2399", "3-star"],
    ["Tirana", "The Rooms Hotel & Residence", "Rruga Sami Frashëri - 1001", "Blloku", "+355 4 223 3232", "+355 4 223 3233", "4-star"],
    ["Tirana", "VH Premier AS Tirana Hotel", "Rruga Reshit Petrela - 1001", "City Center", "+355 4 223 2902", "+355 4 223 2903", "4-star"],
    ["Tirana", "Hotel Viktoria Tirana", "Rruga E Elbasanit - 1001", "City Outskirts", "+355 4 237 0028", "+355 4 237 0029", "3-star"],
    ["Tirana", "Hotel Hermes Tirana", "Rruga Vaso Pasha - 1001", "Blloku", "+355 4 225 1952", "+355 4 225 1953", "4-star"]
]




hotels_vancouver = [
    ["city", "hotel", "address", "suburb", "telephone", "fax", "stars"],
    ["Vancouver", "Beijing Bed & Breakfast", "4636 Kitcher Place - V6X 3V3", "Richmond", "+12367777718", "+12367777718", "Not Rated"],
    ["Vancouver", "Fairmont Hotel Vancouver", "900 West Georgia Street - V6C 2W6", "Vancouver", "+1 604 684 3131", "+1 604 662 1929", "5-star"],
    ["Vancouver", "Pan Pacific Vancouver", "300-999 Canada Pl - V6C 3B5", "Vancouver", "+1 604 662 8111", "+1 604 685 8690", "5-star"],
    ["Vancouver", "Vancouver Marriott Pinnacle Downtown Hotel", "1128 West Hastings Street - V6E 4R5", "Vancouver", "+1 604 684 1128", "+1 604 298 1128", "4-star"],
    ["Vancouver", "The Westin Bayshore, Vancouver", "1601 Bayshore Dr - V6G 2V4", "Vancouver", "+1 604 682 3377", "+1 604 691 6980", "4-star"],
    ["Vancouver", "Holiday Inn & Suites Vancouver Downtown", "1110 Howe Street - V6Z 1R2", "Vancouver", "+1 604 684 2151", "+1 604 684 4736", "3-star"],
    ["Vancouver", "Best Western Plus Sands", "1755 Davie Street - V6G 1W5", "Vancouver", "+1 800 663 9400", "+1 604 682 1831", "3-star"],
    ["Vancouver", "Auberge Vancouver Hotel", "837 West Hastings Street - V6C 1B6", "Vancouver", "+1 604 678 8899", "+1 855 678 8998", "4-star"],
    ["Vancouver", "Embarc Vancouver", "2951-1001 Hornby Street - V6Z 3A5", "Vancouver", "+1 604 893 7444", "+1 604 893 7444", "4-star"],
    ["Vancouver", "Sutton Place Hotel Vancouver", "845 Burrard Street - V6Z 2K6", "Vancouver", "+1 604 682 5511", "+1 604 682 5511", "5-star"],
    ["Vancouver", "Paradox Hotel Vancouver", "1161 West Georgia Street - V6E 0C6", "Vancouver", "+1 236 900 6001", "+1 236 900 6001", "5-star"],
    ["Vancouver", "Hyatt Regency Vancouver", "655 Burrard Street - V6C 2R7", "Vancouver", "+1 604 683 1234", "+1 604 689 5175", "4-star"],
    ["Vancouver", "Four Seasons Hotel Vancouver", "791 West Georgia Street - V6C 2T4", "Vancouver", "+1 604 689 9333", "+1 604 689 9333", "5-star"],
    ["Vancouver", "Shangri-La Hotel Vancouver", "1128 West Georgia Street - V6E 0A8", "Vancouver", "+1 604 689 1120", "+1 604 689 1120", "5-star"],
    ["Vancouver", "Fairmont Pacific Rim", "1038 Canada Place - V6C 0B9", "Vancouver", "+1 604 695 5300", "+1 604 695 5300", "5-star"],
    ["Vancouver", "L'Hermitage Hotel Vancouver", "788 Richards Street - V6B 3A4", "Vancouver", "+1 778 327 4100", "+1 778 327 4100", "4-star"],
    ["Vancouver", "Opus Hotel Vancouver", "322 Davie Street - V6B 5Z6", "Vancouver", "+1 604 642 6787", "+1 604 642 6787", "4-star"],
    ["Vancouver", "JW Marriott Parq Vancouver", "39 Smithe Street - V6B 0R3", "Vancouver", "+1 604 676 0888", "+1 604 676 0888", "5-star"],
    ["Vancouver", "Rosewood Hotel Georgia", "801 West Georgia Street - V6C 1P7", "Vancouver", "+1 604 682 5566", "+1 604 682 5566", "5-star"],
    ["Vancouver", "Hotel Blu Vancouver", "177 Robson Street - V6B 0N3", "Vancouver", "+1 604 620 6200", "+1 604 620 6200", "4-star"]
]


hotels_toronto = [
    ["city", "hotel", "address", "suburb", "telephone", "fax", "stars"],
    ["Toronto", "The Ritz-Carlton, Toronto", "181 Wellington Street West - M5V 3G7", "Downtown Toronto", "+1 416 585 2500", "+1 416 585 2600", "5-star"],
    ["Toronto", "Fairmont Royal York", "100 Front Street West - M5J 1E3", "Downtown Toronto", "+1 416 368 2511", "+1 416 368 9040", "4-star"],
    ["Toronto", "Shangri-La Hotel Toronto", "188 University Avenue - M5H 0A3", "Downtown Toronto", "+1 647 788 8888", "+1 647 788 8889", "5-star"],
    ["Toronto", "The St. Regis Toronto", "325 Bay Street - M5H 4G3", "Financial District", "+1 416 306 5800", "+1 416 306 5801", "5-star"],
    ["Toronto", "The Westin Harbour Castle, Toronto", "1 Harbour Square - M5J 1A6", "Harbourfront", "+1 416 869 1600", "+1 416 869 0573", "4-star"],
    ["Toronto", "Four Seasons Hotel Toronto", "60 Yorkville Avenue - M4W 0A4", "Yorkville", "+1 416 964 0411", "+1 416 964 2301", "5-star"],
    ["Toronto", "InterContinental Toronto Centre", "225 Front Street West - M5V 2X3", "Entertainment District", "+1 416 597 1400", "+1 416 597 8128", "4-star"],
    ["Toronto", "Park Hyatt Toronto", "4 Avenue Road - M5R 2E8", "Yorkville", "+1 416 925 1234", "+1 416 924 2930", "5-star"],
    ["Toronto", "The Hazelton Hotel", "118 Yorkville Avenue - M5R 1C2", "Yorkville", "+1 416 963 6300", "+1 416 963 6305", "5-star"],
    ["Toronto", "The Omni King Edward Hotel", "37 King Street East - M5C 1E9", "Downtown Toronto", "+1 416 863 9700", "+1 416 863 3240", "4-star"],
    ["Toronto", "Delta Hotels by Marriott Toronto", "75 Lower Simcoe Street - M5J 3A6", "Downtown Toronto", "+1 416 849 1200", "+1 416 849 1201", "4-star"],
    ["Toronto", "Toronto Marriott City Centre Hotel", "One Blue Jays Way - M5V 1J4", "Downtown Toronto", "+1 416 341 7100", "+1 416 341 7101", "4-star"],
    ["Toronto", "Hilton Toronto", "145 Richmond Street West - M5H 2L2", "Downtown Toronto", "+1 416 869 3456", "+1 416 869 3187", "4-star"],
    ["Toronto", "Bisha Hotel Toronto", "80 Blue Jays Way - M5V 2G3", "Entertainment District", "+1 416 551 2800", "+1 416 551 2801", "5-star"],
    ["Toronto", "The Drake Hotel", "1150 Queen Street West - M6J 1J3", "West Queen West", "+1 416 531 5042", "+1 416 531 6040", "3-star"],
    ["Toronto", "The Anndore House", "15 Charles Street East - M4Y 1S1", "Downtown Toronto", "+1 416 924 1222", "+1 416 924 2277", "4-star"],
    ["Toronto", "Le Germain Hotel Toronto Mercer", "30 Mercer Street - M5V 1H3", "Entertainment District", "+1 416 345 9500", "+1 416 345 9501", "4-star"],
    ["Toronto", "The Broadview Hotel", "106 Broadview Avenue - M4M 2G1", "Riverside", "+1 416 362 8439", "+1 416 362 8439", "4-star"],
    ["Toronto", "One King West Hotel & Residence", "1 King Street West - M5H 1A1", "Financial District", "+1 416 548 8100", "+1 416 548 8101", "4-star"],
    ["Toronto", "The Yorkville Royal Sonesta Hotel Toronto", "220 Bloor Street West - M5S 1T8", "Yorkville", "+1 416 960 5200", "+1 416 960 5046", "4-star"]
]


hotels_quebec = [
    ["city", "hotel", "address", "suburb", "telephone", "fax", "stars"],
    ["Quebec City", "Fairmont Le Château Frontenac", "1 Rue des Carrières - G1R 4P5", "Old Quebec", "+1 418 692 3861", "+1 418 692 1751", "5-star"],
    ["Quebec City", "Hôtel Le Germain Québec", "126 Rue Saint-Pierre - G1K 4A8", "Old Port", "+1 418 692 2224", "+1 418 692 2225", "4-star"],
    ["Quebec City", "Hôtel Manoir Victoria", "44 Côte du Palais - G1R 4H8", "Old Quebec", "+1 418 692 1030", "+1 418 692 3822", "4-star"],
    ["Quebec City", "Hôtel 71", "71 Rue Saint-Pierre - G1K 4A4", "Old Port", "+1 418 692 1171", "+1 418 692 1187", "4-star"],
    ["Quebec City", "Auberge Saint-Antoine", "8 Rue Saint-Antoine - G1K 4C9", "Old Port", "+1 418 692 2211", "+1 418 692 2224", "5-star"],
    ["Quebec City", "Hôtel PUR Quebec", "395 Rue de la Couronne - G1K 7X4", "Saint-Roch", "+1 418 647 2611", "+1 418 647 2612", "4-star"],
    ["Quebec City", "Hôtel Château Laurier Québec", "1220 Place George V Ouest - G1R 5B8", "Grande Allée", "+1 418 522 8108", "+1 418 647 4439", "4-star"],
    ["Quebec City", "Delta Hotels by Marriott Quebec", "690 Boulevard René-Lévesque Est - G1R 5A8", "Downtown Quebec", "+1 418 647 1717", "+1 418 647 1116", "4-star"],
    ["Quebec City", "Le Capitole Hôtel", "972 Rue Saint-Jean - G1R 1R5", "Old Quebec", "+1 418 694 4040", "+1 418 694 2294", "5-star"],
    ["Quebec City", "Hôtel du Vieux-Québec", "1190 Rue Saint-Jean - G1R 1S6", "Old Quebec", "+1 418 692 1850", "+1 418 692 3766", "4-star"],
    ["Quebec City", "Hotel Clarendon", "57 Rue Sainte-Anne - G1R 3X4", "Old Quebec", "+1 418 692 2480", "+1 418 692 4240", "4-star"],
    ["Quebec City", "Hôtel Plaza Québec", "3031 Boulevard Laurier - G1V 2M2", "Sainte-Foy", "+1 418 658 2727", "+1 418 658 5365", "4-star"],
    ["Quebec City", "Hôtel Alt Québec", "1200 Avenue Germain des Prés - G1V 3M7", "Sainte-Foy", "+1 418 658 1224", "+1 418 658 1225", "3-star"],
    ["Quebec City", "Hôtel Le Concorde Québec", "1225 Cours du Général-de-Montcalm - G1R 4W6", "Grande Allée", "+1 418 647 2222", "+1 418 647 0777", "3-star"],
    ["Quebec City", "Hôtel Bonaparte", "447 Rue Saint-Jean - G1R 1P7", "Old Quebec", "+1 418 694 4446", "+1 418 694 5510", "3-star"],
    ["Quebec City", "Hôtel Québec Inn", "7175 Boulevard Wilfrid-Hamel - G2G 1B6", "L'Ancienne-Lorette", "+1 418 872 9831", "+1 418 872 3011", "4-star"],
    ["Quebec City", "Auberge Place d'Armes", "24 Rue Sainte-Anne - G1R 3X5", "Old Quebec", "+1 418 694 9485", "+1 418 694 9486", "4-star"],
    ["Quebec City", "Monastère des Augustines", "77 Rue des Remparts - G1R 0C3", "Old Quebec", "+1 418 694 1639", "+1 418 694 1897", "4-star"],
    ["Quebec City", "Le Saint-Pierre Auberge Distinctive", "79 Rue Saint-Pierre - G1K 4A3", "Old Port", "+1 418 694 7981", "+1 418 694 7907", "4-star"],
    ["Quebec City", "Hôtel Terrasse Dufferin", "6 Rue de la Terrasse-Dufferin - G1R 4N5", "Old Quebec", "+1 418 692 2482", "+1 418 692 3788", "3-star"],
    ["Montreal", "Hotel Le Cantlie Suites", "1110 Sherbrooke St W, Montreal, QC H3A 1G8", "Downtown Montreal", "+1 514 844 3951", "+1 514 844 3150","4-star"],
    ["Montreal", "Sheraton Montreal Hotel", "1201 Boulevard Rene-Levesque O, Montreal, QC H3B 2L7", "Downtown Montreal", "+1 514 878 2000", "+1 514 878 3958","4-star"],
    ["Montreal", "Renaissance Montreal Downtown Hotel", "1250 Boulevard Robert-Bourassa, Montreal, QC H3B 3B8", "Downtown Montreal", "+1 514 657 5000", "+1 514 657 5001","4-star"],
    ["Montreal", "Hotel Omni Mont-Royal", "1050 Sherbrooke St W, Montreal, QC H3A 2R6", "Downtown Montreal", "+1 514 284 1110", "+1 514 284 2098","4-star"],
    ["Montreal", "Best Western Plus Montreal Downtown-Hotel Europa", "1240 Drummond St, Montreal, QC H3G 1V7", "Downtown Montreal", "+1 514 866 6492", "+1 514 861 4089","3-star"]
]



# conferences = [
#         ["conname", "comstart", "venue","address","summary","code","heldon","senton","link","city"],
#         [   
#             "13th Global Conference on African Economy and Culture (GCAEC)",
#             "2024-11-01",
#             "George Brown College",
#             "80 Cooperage St, Toronto, Ontario, M5A 0J3",
#             """The 13th Global Conference on African Economy and Culture (GCAEC) – Toronto, Canada, November 01-03, 2024, aims to showcase and develop Africa’s diverse economic and cultural potential.""",
#             "2024-TOR-GCAEC-NOV","Nov 01-03","Oct 28","https://globalconference.ca/conference/2nd-global-conference-on-public-health-and-epidemiology-gcphe/"
#             ,"Vancouver BC"
#         ]

        
#     ]


conferences = [
        ["conname", "comstart", "venue","address","summary","code","heldon","senton","link","city"],
        [   
            "2nd Global Conference on African Business and Technology (GCABT)",
            "2024-10-25",
            "The University of British Columbia",
            "800 Robson Street, Vancouver, BC, Canada V6Z 3B7",
            """
            The core objective of the African Business and Technology Conference, helmed by Global Conference Alliance Inc., 
            is to foster a collaborative platform that bridges the intersection of business and technology in Africa’s 
            rapidly evolving landscape. We aim to spotlight the continent’s burgeoning tech hubs, innovation in sectors from
            fintech to agriculture, and the transformative power of digital solutions in addressing socio-economic challenges.
            """,
            "2024-VAN-GCABT-OCT","Oct 25-27","Oct 21","https://globalconference.ca/conference/2nd-global-conference-on-public-health-and-epidemiology-gcphe/"
            ,"Vancouver BC"
        ],
        [   
            "2nd Global Conference on African Business and Technology (GCABT)",
            "2024-10-25",
            "The University of British Columbia",
            "800 Robson Street, Vancouver, BC, Canada V6Z 3B7",
            """
            The core objective of the African Business and Technology Conference, helmed by Global Conference Alliance Inc., 
            is to foster a collaborative platform that bridges the intersection of business and technology in Africa’s 
            rapidly evolving landscape. We aim to spotlight the continent’s burgeoning tech hubs, innovation in sectors from
            fintech to agriculture, and the transformative power of digital solutions in addressing socio-economic challenges.
            """,
            "2024-VAN-GCABT-OCT","Oct 25-27","Oct 21","https://globalconference.ca/conference/2nd-global-conference-on-public-health-and-epidemiology-gcphe/"
            ,"Vancouver BC"
        ],
        [   
            "2nd Global Conference on African Business and Technology (GCABT)",
            "2024-10-25",
            "The University of British Columbia",
            "800 Robson Street, Vancouver, BC, Canada V6Z 3B7",
            """
            The core objective of the African Business and Technology Conference, helmed by Global Conference Alliance Inc., 
            is to foster a collaborative platform that bridges the intersection of business and technology in Africa’s 
            rapidly evolving landscape. We aim to spotlight the continent’s burgeoning tech hubs, innovation in sectors from
            fintech to agriculture, and the transformative power of digital solutions in addressing socio-economic challenges.
            """,
            "2024-VAN-GCABT-OCT","Oct 25-27","Oct 21","https://globalconference.ca/conference/2nd-global-conference-on-public-health-and-epidemiology-gcphe/"
            ,"Vancouver BC"
        ],
        [   
            "2nd Global Conference on African Business and Technology (GCABT)",
            "2024-10-25",
            "The University of British Columbia",
            "800 Robson Street, Vancouver, BC, Canada V6Z 3B7",
            """
            The core objective of the African Business and Technology Conference, helmed by Global Conference Alliance Inc., 
            is to foster a collaborative platform that bridges the intersection of business and technology in Africa’s 
            rapidly evolving landscape. We aim to spotlight the continent’s burgeoning tech hubs, innovation in sectors from
            fintech to agriculture, and the transformative power of digital solutions in addressing socio-economic challenges.
            """,
            "2024-VAN-GCABT-OCT","Oct 25-27","Oct 21","https://globalconference.ca/conference/2nd-global-conference-on-public-health-and-epidemiology-gcphe/"
            ,"Vancouver BC"
        ],

        
    ]


first_male_names = [
    'Kwame', 'Kojo', 'Kofi', 'Yaw',
    'Kwesi', 'Kwabena', 'Kwaku',
    'James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Charles', 'Thomas',
    'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Donald', 'Mark', 'Paul', 'Steven', 'Andrew', 'Kenneth',
    'Joshua', 'George', 'Kevin', 'Brian', 'Edward', 'Ronald', 'Timothy', 'Jason', 'Jeffrey', 'Ryan',
    'Jacob', 'Gary', 'Nicholas', 'Eric', 'Jonathan', 'Stephen', 'Larry', 'Justin', 'Scott', 'Brandon',
    'Frank', 'Benjamin', 'Gregory', 'Samuel', 'Raymond', 'Patrick', 'Alexander', 'Jack', 'Dennis', 'Jerry',
    'Tyler', 'Aaron', 'Jose', 'Henry', 'Douglas', 'Adam', 'Peter', 'Nathan', 'Zachary', 'Walter',
    'Kyle', 'Harold', 'Carl', 'Jeremy', 'Keith', 'Roger', 'Gerald', 'Ethan', 'Arthur', 'Terry',
    'Christian', 'Sean', 'Lawrence', 'Austin', 'Joe', 'Noah', 'Jesse', 'Albert', 'Bryan', 'Billy',
    'Bruce', 'Willie', 'Jordan', 'Dylan', 'Alan', 'Ralph', 'Gabriel', 'Roy', 'Juan', 'Wayne',
    'Eugene', 'Logan', 'Randy', 'Louis', 'Russell', 'Vincent', 'Philip', 'Bobby', 'Johnny', 'Bradley'
]

land_at = [
    '123 Kwame Nkrumah Ave, Accra',
    '456 Independence Ave, Accra',
    '789 Osu Oxford St, Accra',
    '101 Adabraka Road, Accra',
    '202 Labone Crescent, Accra',
    '303 Cantonments Road, Accra',
    '404 Ridge Street, Accra',
    '505 East Legon Ave, Accra',
    '606 Spintex Road, Accra',
    '707 Airport Residential Area, Accra',
    '808 Tema Harbour Road, Tema',
    '909 Community 1 Road, Tema',
    '1010 Community 2 Avenue, Tema',
    '1111 Sakumono Estates, Tema',
    '1212 Ashaiman Main Road, Ashaiman',
    '1313 Community 25 Road, Tema',
    '1414 West Hills Mall Road, Weija',
    '1515 Kasoa Main Street, Kasoa',
    '1616 Madina Road, Madina',
    '1717 Legon Campus Road, Legon',
    '1818 Haatso Main Road, Haatso',
    '1919 Abeka Lapaz Road, Lapaz',
    '2020 Dome Pillar 2 Road, Dome',
    '2121 Achimota Mile 7 Road, Achimota',
    '2222 Kwashieman Street, Kwashieman',
    '2323 Dansoman High Street, Dansoman',
    '2424 Kaneshie Market Road, Kaneshie',
    '2525 Odorkor Tipper Road, Odorkor',
    '2626 Bubuashie Road, Bubuashie',
    '2727 North Kaneshie Road, North Kaneshie',
    '2828 Awoshie Pokuase Road, Awoshie',
    '2929 Ablekuma Road, Ablekuma',
    '3030 Darkuman Road, Darkuman',
    '3131 Taifa Burkina Street, Taifa',
    '3232 Pokuase Road, Pokuase',
    '3333 Amasaman Road, Amasaman',
    '3434 Achimota Retail Centre, Achimota',
    '3535 Adenta Housing Road, Adenta',
    '3636 Dodowa Road, Dodowa',
    '3737 Ashongman Estate Road, Ashongman',
    '3838 Kwabenya Road, Kwabenya',
    '3939 Nungua Barrier Road, Nungua',
    '4040 Teshie Nungua Road, Teshie',
    '4141 La Beach Road, La',
    '4242 Nungua Central Road, Nungua',
    '4343 Kpone Road, Kpone',
    '4444 Sakumono Beach Road, Sakumono',
    '4545 Prampram Road, Prampram',
    '4646 Shai Hills Road, Shai Hills',
    '4747 Dawhenya Road, Dawhenya',
    '4848 Ada Foah Road, Ada Foah',
    '4949 Afienya Road, Afienya',
    '5050 Oyibi Road, Oyibi',
    '5151 Koforidua Road, Koforidua',
    '5252 Aburi Road, Aburi',
    '5353 Akropong Road, Akropong',
    '5454 Mamfe Road, Mamfe',
    '5555 Nsawam Road, Nsawam',
    '5656 Suhum Road, Suhum',
    '5757 Nkawkaw Road, Nkawkaw',
    '5858 Mpraeso Road, Mpraeso',
    '5959 Obomeng Road, Obomeng',
    '6060 Obo Road, Obo',
    '6161 Abetifi Road, Abetifi',
    '6262 Kwahu Tafo Road, Kwahu Tafo',
    '6363 Nkawkaw-Atibie Road, Nkawkaw',
    '6464 Kibi Road, Kibi',
    '6565 Akyem Oda Road, Akyem Oda',
    '6666 Akwatia Road, Akwatia',
    '6767 Asamankese Road, Asamankese',
    '6868 Somanya Road, Somanya',
    '6969 Kpong Road, Kpong',
    '7070 Juapong Road, Juapong',
    '7171 Asutsuare Road, Asutsuare',
    '7272 Senchi Ferry Road, Senchi Ferry',
    '7373 Sogakope Road, Sogakope',
    '7474 Ho Road, Ho',
    '7575 Aflao Road, Aflao',
    '7676 Keta Road, Keta',
    '7777 Anloga Road, Anloga',
    '7878 Denu Road, Denu',
    '7979 Agbozume Road, Agbozume',
    '8080 Kpetoe Road, Kpetoe',
    '8181 Dzodze Road, Dzodze',
    '8282 Hohoe Road, Hohoe',
    '8383 Jasikan Road, Jasikan',
    '8484 Nkwanta Road, Nkwanta',
    '8585 Kadjebi Road, Kadjebi',
    '8686 Kpando Road, Kpando',
    '8787 Akosombo Road, Akosombo',
    '8888 Amedzofe Road, Amedzofe',
    '8989 Fodome Road, Fodome',
    '9090 Dambai Road, Dambai',
    '9191 Krachi Road, Krachi',
    '9292 Sefwi Wiawso Road, Sefwi Wiawso',
    '9393 Bibiani Road, Bibiani',
    '9494 Juaboso Road, Juaboso',
    '9595 Enchi Road, Enchi',
    '9696 Asankragwa Road, Asankragwa',
    '9797 Elubo Road, Elubo',
    '9898 Half Assini Road, Half Assini',
    '9999 Axim Road, Axim',
    '100100 Agona Nkwanta Road, Agona Nkwanta'
]


first_female_names = [
    'Abena', 'Akua','Esi', 'Efua','Adjoa', 'Akosua', 'Yaa','Ama', 'Afia','Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Jessica', 'Sarah', 'Karen',
    'Nancy', 'Lisa', 'Margaret', 'Betty', 'Sandra', 'Ashley', 'Dorothy', 'Kimberly', 'Emily', 'Donna',
    'Michelle', 'Carol', 'Amanda', 'Melissa', 'Deborah', 'Stephanie', 'Rebecca', 'Sharon', 'Laura', 'Cynthia',
    'Kathleen', 'Amy', 'Shirley', 'Angela', 'Helen', 'Anna', 'Brenda', 'Pamela', 'Nicole', 'Samantha',
    'Katherine', 'Christine', 'Debra', 'Rachel', 'Carolyn', 'Janet', 'Catherine', 'Maria', 'Heather', 'Diane',
    'Ruth', 'Julie', 'Olivia', 'Joyce', 'Virginia', 'Victoria', 'Kelly', 'Lauren', 'Christina', 'Joan',
    'Evelyn', 'Judith', 'Megan', 'Cheryl', 'Andrea', 'Hannah', 'Martha', 'Jacqueline', 'Frances', 'Gloria',
    'Ann', 'Teresa', 'Kathryn', 'Sara', 'Janice', 'Jean', 'Alice', 'Madison', 'Doris', 'Abigail',
    'Julia', 'Judy', 'Grace', 'Denise', 'Amber', 'Marilyn', 'Beverly', 'Danielle', 'Theresa', 'Sophia',
    'Marie', 'Diana', 'Brittany', 'Natalie', 'Isabella', 'Charlotte', 'Rose', 'Alexis', 'Kayla', 'Ella'
]

last_names = [
    'Mensah', 'Osei', 'Asare', 'Boateng', 'Addo', 'Adjei', 'Agyei', 'Ofori',
    'Nkansah', 'Dankwah', 'Bonsu', 'Acheampong', 'Opoku', 'Nyarko', 'Doku', 'Gyamfi'
]

# List of friends in JSON format
friends_list = [
    {
        "firstname": random.choice(first_male_names),
        "lastname": random.choice(last_names),
        "friendyears": random.randint(2, 3),
        "employercompany": "TechCorp",
        "friendaddress": "123 Maple St, Vancouver, BC",
        "friendroleincomp": "Software Engineer",
        "phonenumber": "123-456-7890"
    },
    {
        "firstname": random.choice(first_male_names),
        "lastname": random.choice(last_names),
        "friendyears": random.randint(2, 3),
        "employercompany": "InnovateTech",
        "friendaddress": "456 Oak St, Vancouver, BC",
        "friendroleincomp": "Project Manager",
        "phonenumber": "234-567-8901"
    },
    {
        "firstname": random.choice(first_male_names),
        "lastname": random.choice(last_names),
        "friendyears": random.randint(2, 3),
        "employercompany": "DevSolutions",
        "friendaddress": "789 Pine St, Vancouver, BC",
        "friendroleincomp": "QA Analyst",
        "phonenumber": "345-678-9012"
    },
    {
        "firstname": random.choice(first_male_names),
        "lastname": random.choice(last_names),
        "friendyears": random.randint(2, 3),
        "employercompany": "WebWorks",
        "friendaddress": "101 Birch St, Vancouver, BC",
        "friendroleincomp": "Frontend Developer",
        "phonenumber": "456-789-0123"
    },
    {
        "firstname": random.choice(first_male_names),
        "lastname": random.choice(last_names),
        "friendyears": random.randint(2, 3),
        "employercompany": "DataScape",
        "friendaddress": "202 Cedar St, Vancouver, BC",
        "friendroleincomp": "Data Scientist",
        "phonenumber": "567-890-1234"
    },
    {
        "firstname": random.choice(first_male_names),
        "lastname": random.choice(last_names),
        "friendyears": random.randint(2, 3),
        "employercompany": "AI Dynamics",
        "friendaddress": "303 Spruce St, Vancouver, BC",
        "friendroleincomp": "Machine Learning Engineer",
        "phonenumber": "678-901-2345"
    }
]

def previous_travel():
    travels = [
        {
        "country": "Dubai",
        "country2": "China",
        "tripyear": "2018",
        "purpose": "tourism",
        "nature": "the nature of my trip was strictly tourism",
    },
    {
        "country": "Egypt",
        "country2": "Ethiopia",
        "tripyear": "2018",
        "purpose": "tourism",
        "nature": "the nature of my trip was strictly tourism",
    },
    {
        "country": "Kenya",
        "country2": "Nigeria",
        "tripyear": "2018",
        "purpose": "tourism",
        "nature": "the nature of my trip was strictly tourism",
    },
    {
        "country": "Dubai",
        "country2": "South Africa",
        "tripyear": "2020",
        "purpose": "tourism",
        "nature": "the nature of my trip was strictly tourism",
    },
    {
        "country": "Dubai",
        "country2": "South Africa",
        "tripyear": "2018",
        "purpose": "tourism",
        "nature": "the nature of my trip was strictly tourism",
    },
    {
        "country": "Dubai",
        "country2": "South Africa",
        "tripyear": "2017",
        "purpose": "tourism",
        "nature": "the nature of my trip was strictly tourism",
    },{
        "country": "Qatar",
        "country2": "Saudi Arabia",
        "tripyear": "2022",
        "purpose": "to watch the world cup",
        "nature": "the nature of my trip was strictly to see the world cup and tour the middle east",
    }

    ]

school_churches = [
    'Presby',
    'Roman Catholic',
    'SDA',
    'Pentecost',
    'Methodist',
    'Anglican',
    'Baptist',
    'Assemblies of God',
    'Lutheran',
    'Evangelical',
    'Charismatic',
    'Apostolic',
]


values = {
        "licenceno": random.choices(range(10000, 99999), k=4),
        "certno": random.choices(range(10000, 99999), k=4),
        "date": "2024",
        "year": ["2024", "2025", "2026", "2027"],
        "location": ["New York", "Los Angeles", "Chicago", "Houston"],
        "marriagecity": ["San Francisco", "Boston", "Miami", "Seattle"],
        "marriageno": ["001", "002", "003", "004"],
        "nameofspouse": ["Alice", "Bob", "Charlie", "Dana"],
        "spousework": ["Engineer", "Doctor", "Teacher", "Artist"],
        "wifeaddress": ["123 Main St", "456 Elm St", "789 Oak St", "101 Pine St"],
        "spousefather": ["{{current_user.username}}", "Michael Smith", "William Johnson", "David Brown"],
        "inlawwork": ["Lawyer", "Architect", "Dentist", "Chef"],
        "role": ["Manager", "Developer", "Designer", "Consultant"],
        "myaddress": ["321 Maple St", "654 Spruce St", "987 Birch St", "202 Cedar St"],
        "myfather": ["Robert Doe", "James Smith", "Charles Johnson", "Thomas Brown"],
        "myfatherwork": ["Plumber", "Electrician", "Mechanic", "Carpenter"],
        "witness1": ["Samuel Green", "Lucas White", "Henry Black", "Owen Gray"],
        "witness1sig": ["SGreen", "LWhite", "HBlack", "OGray"],
        "witness2": ["Olivia Blue", "Isabella Pink", "Sophia Purple", "Emma Red"],
        "witness2sig": ["OBlue", "IPink", "SPurple", "ERed"],
        "mysig": ["JSmith", "EJohnson", "AWilliams", "BJones"],
        "wifesig": ["JDoe", "EBlack", "AWilson", "BMartinez"]
    }

travels = [
        {
        "country": "Dubai",
        "country2": "China",
        "tripyear": "2018",
        "purpose": "tourism",
        "nature": "the nature of my trip was strictly tourism",
    },
    {
        "country": "Egypt",
        "country2": "Ethiopia",
        "tripyear": "2018",
        "purpose": "tourism",
        "nature": "the nature of my trip was strictly tourism",
    },
    {
        "country": "Kenya",
        "country2": "Nigeria",
        "tripyear": "2018",
        "purpose": "tourism",
        "nature": "the nature of my trip was strictly tourism",
    },
    {
        "country": "Dubai",
        "country2": "South Africa",
        "tripyear": "2020",
        "purpose": "tourism",
        "nature": "the nature of my trip was strictly tourism",
    },
    {
        "country": "Dubai",
        "country2": "South Africa",
        "tripyear": "2018",
        "purpose": "tourism",
        "nature": "the nature of my trip was strictly tourism",
    },
    {
        "country": "Dubai",
        "country2": "South Africa",
        "tripyear": "2017",
        "purpose": "tourism",
        "nature": "the nature of my trip was strictly tourism",
    },{
        "country": "Qatar",
        "country2": "Saudi Arabia",
        "tripyear": "2022",
        "purpose": "to watch the world cup",
        "nature": "the nature of my trip was strictly to see the world cup and tour the middle east",}]