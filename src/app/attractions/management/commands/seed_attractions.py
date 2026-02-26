"""
Management command to seed Tanzania tourism attractions with real GPS-accurate data.
Run: python src/manage.py seed_attractions
"""
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from app.regions.models import Region
from app.attractions.models import Attraction, AttractionTip

User = get_user_model()


REGIONS = [
    {
        "name": "Kilimanjaro",
        "slug": "kilimanjaro",
        "description": (
            "The Kilimanjaro Region is located in northern Tanzania, bordering Kenya to the north. "
            "It is home to Africa's highest peak, Mount Kilimanjaro (5,895 m), and the town of Moshi, "
            "the main gateway for Kilimanjaro climbs. The region features a rich blend of highland "
            "coffee farms, Chagga cultural villages, and the famous Chemka (Kikuletwa) Hot Springs. "
            "Kilimanjaro International Airport (JRO) connects the region to the world."
        ),
        "latitude": "-3.361",
        "longitude": "37.341",
    },
    {
        "name": "Arusha",
        "slug": "arusha",
        "description": (
            "Arusha Region is the safari capital of Tanzania and the northern circuit hub. "
            "It is home to Arusha National Park (Mount Meru), the Ngorongoro Conservation Area, "
            "Olduvai Gorge, and serves as the gateway to Serengeti and Tarangire National Parks. "
            "Kilimanjaro International Airport and Arusha Airport link this region to global travellers."
        ),
        "latitude": "-3.386925",
        "longitude": "36.682995",
    },
    {
        "name": "Mara",
        "slug": "mara",
        "description": (
            "The Mara Region lies in northwestern Tanzania, bordering Kenya's Masai Mara. "
            "It covers the western and northern Serengeti, witnessing the spectacular Great Wildebeest "
            "Migration river crossings at the Mara River between July and October. "
            "The region is largely rural with the Kurya, Luo, and Kuria peoples calling it home."
        ),
        "latitude": "-1.7471",
        "longitude": "34.0757",
    },
    {
        "name": "Manyara",
        "slug": "manyara",
        "description": (
            "The Manyara Region lies south of Arusha and is named after Lake Manyara, "
            "a shallow alkaline lake famous for tree-climbing lions and vast flamingo flocks. "
            "The region also hosts Tarangire National Park, renowned for its massive elephant herds "
            "and ancient baobab trees. The Great Rift Valley escarpment dominates the landscape."
        ),
        "latitude": "-4.3154",
        "longitude": "35.9017",
    },
    {
        "name": "Zanzibar",
        "slug": "zanzibar",
        "description": (
            "The Zanzibar Archipelago (officially Unguja and Pemba) sits in the Indian Ocean off the "
            "Tanzania mainland coast. Zanzibar City's Stone Town is a UNESCO World Heritage Site "
            "blending Swahili, Arab, Indian, and European architecture. The islands are famous for "
            "white sand beaches, turquoise waters, world-class diving and snorkelling, historic spice "
            "farms, and the birthplace of Freddie Mercury."
        ),
        "latitude": "-6.165173",
        "longitude": "39.202641",
    },
    {
        "name": "Pwani",
        "slug": "pwani",
        "description": (
            "Pwani (Coastal) Region stretches along Tanzania's Indian Ocean coastline south of Dar es Salaam. "
            "It encompasses the pristine Mafia Island Marine Park — a world-class diving and whale shark "
            "destination — and forms the northeastern border of Nyerere (Selous) National Park, "
            "Africa's largest national park. The region offers mangrove estuaries, coral reefs, and "
            "unspoilt coastal villages."
        ),
        "latitude": "-7.3833",
        "longitude": "39.1833",
    },
    {
        "name": "Kigoma",
        "slug": "kigoma",
        "description": (
            "Kigoma Region borders Lake Tanganyika, the world's longest and second-deepest freshwater lake, "
            "on Tanzania's western edge. It is home to Mahale Mountains National Park — one of Africa's best "
            "chimpanzee trekking destinations — and Gombe Stream National Park, where Jane Goodall conducted "
            "her landmark chimpanzee research. Kigoma town is a key port for Lake Tanganyika ferry services."
        ),
        "latitude": "-4.8833",
        "longitude": "29.6333",
    },
    {
        "name": "Lindi",
        "slug": "lindi",
        "description": (
            "Lindi Region in southern Tanzania borders Mozambique and covers much of the southern portion of "
            "Nyerere National Park (formerly Selous Game Reserve), Africa's largest protected area. "
            "The region is characterised by miombo woodland, the Rufiji River delta, and a largely untouched "
            "wilderness offering exclusive wildlife encounters away from the northern circuit crowds."
        ),
        "latitude": "-9.9980",
        "longitude": "39.7170",
    },
]


ATTRACTIONS = [
    # ──────────────────────────────────────────────────────────────
    # 1. CHEMKA HOT SPRINGS (KIKULETWA)
    # ──────────────────────────────────────────────────────────────
    {
        "name": "Chemka Hot Springs (Kikuletwa)",
        "slug": "chemka-hot-springs-kikuletwa",
        "region_slug": "kilimanjaro",
        "category": "other",
        "description": (
            "Chemka Hot Springs, locally known as Kikuletwa Hot Springs, is a stunning geothermal oasis "
            "hidden within the semi-arid plains near Boma Ng'ombe village, approximately 40 km west of Moshi. "
            "Fed by underground geothermal springs, the pools maintain a constant temperature of 25–30°C "
            "year-round, producing crystal-clear turquoise water of exceptional visibility. "
            "Towering fig trees and tropical palms overhang the pools, creating a lush canopy that provides "
            "natural shade. The springs are famous for rope swings, snorkelling among freshwater fish, "
            "and peaceful picnics on the grassy banks.\n\n"
            "Visitors typically arrive as part of a day trip from Moshi or Arusha, often combining the visit "
            "with a Kilimanjaro climbing preparation or post-summit recovery. The site is managed by the local "
            "Boma Ng'ombe community, and entrance fees directly support village development projects. "
            "Altezza Travel, one of Tanzania's leading operators, offers fully guided day trips including "
            "return transport from Moshi, entrance tickets, picnic lunch, and optional snorkelling equipment. "
            "Weekend visits tend to be busier; early morning arrivals enjoy the clearest water and the most "
            "tranquil atmosphere before tour groups arrive."
        ),
        "short_description": (
            "A geothermal oasis 40 km from Moshi with crystal-clear turquoise pools at 25–30°C, "
            "rope swings, and lush tropical palms — perfect for swimming, snorkelling, and picnics."
        ),
        "latitude": "-3.444300",
        "longitude": "37.193800",
        "altitude": 850,
        "difficulty_level": "easy",
        "access_info": (
            "From Moshi: Take the B1 road west towards Boma Ng'ombe, then follow signposted dirt roads "
            "(approx. 40 min drive). A 4WD vehicle is recommended in the wet season due to the unpaved "
            "access track. Most visitors arrange transfers through tour operators in Moshi or Arusha. "
            "Public transport: dalla-dalla from Moshi to Boma Ng'ombe, then short walk or motorbike taxi."
        ),
        "nearest_airport": "Kilimanjaro International Airport (JRO)",
        "distance_from_airport": "65.00",
        "best_time_to_visit": "Year-round; June–October and January–February for dry roads",
        "seasonal_availability": (
            "Open year-round. During heavy rains (March–May), the access dirt road can become muddy and "
            "4WD is essential. Water clarity is best in the dry season (June–October). "
            "Weekdays are significantly quieter than weekends."
        ),
        "estimated_duration": "4–6 hours (full day trip)",
        "entrance_fee": "10.00",
        "requires_guide": False,
        "requires_permit": False,
        "is_featured": True,
        "tips": [
            {
                "title": "Bring Water Shoes",
                "description": (
                    "The entry into the pools is over smooth but slippery rocks. Water shoes or old trainers "
                    "protect your feet and give much better grip than bare feet."
                ),
            },
            {
                "title": "Arrive Early for Best Clarity",
                "description": (
                    "Arrive before 10 AM for the clearest, most pristine water. By midday tour groups "
                    "arrive and the water becomes slightly murkier from swimmers."
                ),
            },
            {
                "title": "Snorkelling Gear is Worth It",
                "description": (
                    "The crystal-clear water offers surprising visibility. Bring or rent a snorkel mask "
                    "to see freshwater fish and the spring vents bubbling from the sandy floor."
                ),
            },
            {
                "title": "Book Through a Licensed Operator",
                "description": (
                    "Operators like Altezza Travel include transport from Moshi, entrance fees, and packed "
                    "lunch in one fee (~$85 per person for groups of 5+), which is better value and more "
                    "reliable than arranging everything independently."
                ),
            },
        ],
    },

    # ──────────────────────────────────────────────────────────────
    # 2. MOUNT KILIMANJARO
    # ──────────────────────────────────────────────────────────────
    {
        "name": "Mount Kilimanjaro",
        "slug": "mount-kilimanjaro",
        "region_slug": "kilimanjaro",
        "category": "mountain",
        "description": (
            "Mount Kilimanjaro is Africa's highest peak at 5,895 metres (19,341 ft) and the world's tallest "
            "free-standing mountain. Its summit, Uhuru Peak, crowns the Kibo crater and is a UNESCO World "
            "Heritage Site. Kilimanjaro rises dramatically from the surrounding savannah plains in "
            "northeastern Tanzania, visible from over 200 km away on clear days. The mountain is divided "
            "into Kilimanjaro National Park, covering 1,688 km² and containing five distinct climate zones: "
            "cultivated farmland, rainforest, heath and moorland, alpine desert, and the arctic summit.\n\n"
            "Six official trekking routes offer varying experiences:\n"
            "• **Marangu (Coca-Cola Route)** – 5–6 days, only route with hut accommodation, beginner-friendly\n"
            "• **Machame (Whiskey Route)** – 6–7 days, most scenic, high success rate, popular choice\n"
            "• **Lemosho** – 7–8 days, remote approach from the west, highest success rate (90%+)\n"
            "• **Rongai** – 6–7 days, dry northern approach from Kenya border, least crowded\n"
            "• **Shira** – 7 days, starts high (3,500m) so acclimatisation is critical\n"
            "• **Umbwe** – 5–6 days, steepest and most direct, for fit, experienced trekkers\n\n"
            "All climbs must be arranged through licensed TANAPA operators. An armed ranger and registered "
            "guide accompany every group. The mountain supports extraordinary biodiversity including giant "
            "groundsels, lobelias, colobus monkeys, leopards, buffaloes, and over 180 bird species in the "
            "rainforest zone. Tipping culture is strong — budget at least $200–$300 in guide/porter tips."
        ),
        "short_description": (
            "Africa's highest peak (5,895 m) and a UNESCO World Heritage Site — six trekking routes, "
            "five climate zones, and one of the world's most iconic summit experiences."
        ),
        "latitude": "-3.065653",
        "longitude": "37.352013",
        "altitude": 5895,
        "difficulty_level": "difficult",
        "access_info": (
            "Main trekking gates: Marangu Gate (Marangu route, 1,860m), Machame Gate (Machame route, 1,800m), "
            "Londorossi Gate (Lemosho/Shira routes), Rongai Gate (Rongai route), Umbwe Gate (Umbwe route). "
            "All gates are within 1–2 hours' drive from Moshi. Kilimanjaro International Airport (JRO) is "
            "the nearest airport, 35 km from Moshi. Independent trekking is NOT permitted; all climbers must "
            "be accompanied by a licensed guide and at least one porter."
        ),
        "nearest_airport": "Kilimanjaro International Airport (JRO)",
        "distance_from_airport": "35.00",
        "best_time_to_visit": "January–March and June–October (dry seasons)",
        "seasonal_availability": (
            "Open year-round. Two dry seasons offer the best summit conditions: "
            "January–March (warm, dry, excellent summit visibility) and June–October (cold but clear). "
            "April–May (long rains) and November (short rains) bring cloud, rain, and snow above 4,000m, "
            "reducing summit success rates. December is popular for Christmas/New Year summits."
        ),
        "estimated_duration": "5–9 days depending on route",
        "entrance_fee": "70.00",
        "requires_guide": True,
        "requires_permit": True,
        "is_featured": True,
        "tips": [
            {
                "title": "Choose the Lemosho Route for Best Success Rate",
                "description": (
                    "The 7–8 day Lemosho Route has a 90%+ summit success rate due to excellent "
                    "acclimatisation. Longer routes always outperform shorter ones — avoid the 5-day "
                    "Marangu if summit success is your goal."
                ),
            },
            {
                "title": "Pole Pole — Go Slowly",
                "description": (
                    "Altitude sickness affects around 75% of trekkers above 3,000m. The Swahili phrase "
                    "'pole pole' (slowly, slowly) is the trekker's mantra. Rushing increases risk of AMS. "
                    "Acclimatisation days are built into longer routes for good reason."
                ),
            },
            {
                "title": "Pack Layers for Every Climate",
                "description": (
                    "You'll walk through rainforest, moorland, alpine desert, and arctic summit in one climb. "
                    "Bring waterproofs for the forest, warm mid-layers for moorland, and a -20°C sleeping bag "
                    "plus down jacket and balaclava for summit night (temperatures can drop to -20°C)."
                ),
            },
            {
                "title": "Budget $200–$300 for Tips",
                "description": (
                    "Tanzania's trekking industry relies on tipping. The standard tip is $20–$30/day for guides "
                    "and $10–$15/day per porter. For a 7-day climb with 5 crew this is $700–$1,000 total. "
                    "Bring cash (USD) as ATMs on Kili do not exist."
                ),
            },
        ],
    },

    # ──────────────────────────────────────────────────────────────
    # 3. SERENGETI NATIONAL PARK
    # ──────────────────────────────────────────────────────────────
    {
        "name": "Serengeti National Park",
        "slug": "serengeti-national-park",
        "region_slug": "mara",
        "category": "national_park",
        "description": (
            "Serengeti National Park, Tanzania's oldest and most famous national park, covers 14,763 km² "
            "of endless open savannah, riverine forests, rocky kopjes, and seasonal wetlands across northern "
            "Tanzania. A UNESCO World Heritage Site since 1981 and an IUCN Biosphere Reserve, the Serengeti "
            "is synonymous with the Great Wildebeest Migration — the largest terrestrial mammal migration on "
            "Earth, involving 1.5 million wildebeest, 400,000 zebra, and 200,000 Thomson's gazelle cycling "
            "between Tanzania and Kenya's Masai Mara year-round.\n\n"
            "The park is divided into three main areas: the southern Ndutu plains (calving season, Jan–Mar), "
            "the central Seronera valley (year-round predator activity), and the northern Kogatende area "
            "(dramatic Mara River crossings, Jul–Oct). The Serengeti hosts Africa's largest lion population "
            "(around 3,000), large cheetah numbers, leopards, the Big Five, African wild dogs, hyenas, and "
            "over 500 bird species. Night drives are not permitted inside the park.\n\n"
            "Entry is by TANAPA card or Visa/Mastercard; cash is not accepted at park gates. The nearest "
            "main entry gate is Naabi Hill Gate (southern), with additional gates at Ndabaka (west) "
            "and Klein's (north). Charter flights operate to Seronera, Grumeti, and Kogatende airstrips."
        ),
        "short_description": (
            "Africa's most iconic national park — home to the Great Wildebeest Migration, the Big Five, "
            "and endless savannah stretching to the horizon across 14,763 km²."
        ),
        "latitude": "-2.333333",
        "longitude": "34.833332",
        "altitude": 1525,
        "difficulty_level": "easy",
        "access_info": (
            "By road from Arusha: 7–8 hours via Ngorongoro Conservation Area and Naabi Hill Gate. "
            "By air: Charter flights from Arusha, Kilimanjaro, or Dar es Salaam to Seronera Airstrip (SEU), "
            "Grumeti Airstrip, or Kogatende Airstrip (north). Main entry gates: "
            "Naabi Hill Gate (main south), Ndabaka Gate (west), Klein's Gate (north), "
            "Fort Ikoma Gate (northwest), Bolongoja Gate (east)."
        ),
        "nearest_airport": "Seronera Airstrip (inside park) / Kilimanjaro International (JRO)",
        "distance_from_airport": "325.00",
        "best_time_to_visit": "June–October for migration crossings; January–March for calving",
        "seasonal_availability": (
            "Open year-round. Peak season (June–October) offers dry conditions and the famous Mara River "
            "crossings in the north. Calving season (January–March) features newborn wildebeest and intense "
            "predator action in the southern plains. Green season (November–May) has lower fees, lush "
            "scenery, and excellent bird watching but roads can be muddy in April–May."
        ),
        "estimated_duration": "2–5 days",
        "entrance_fee": "70.00",
        "requires_guide": False,
        "requires_permit": False,
        "is_featured": True,
        "tips": [
            {
                "title": "Visit the North (Kogatende) for River Crossings",
                "description": (
                    "The dramatic Mara River crossings happen in the Northern Serengeti (Kogatende) from "
                    "July to October. Book a camp in this area to be on-site when crossings occur — it can "
                    "require waiting several hours at the river bank."
                ),
            },
            {
                "title": "Pay Electronically — No Cash at Gates",
                "description": (
                    "TANAPA gates do not accept cash. Bring a Visa or Mastercard, or use the TANAPA online "
                    "portal to pre-pay your park fees. Amex and other cards are often rejected."
                ),
            },
            {
                "title": "Book Camps Early for Peak Season",
                "description": (
                    "July–October is high season. Central Serengeti lodges and migration-area tented camps "
                    "book out 6–12 months in advance. Flexible low-season (April–May) travel offers "
                    "significant savings with excellent wildlife still present."
                ),
            },
        ],
    },

    # ──────────────────────────────────────────────────────────────
    # 4. NGORONGORO CRATER
    # ──────────────────────────────────────────────────────────────
    {
        "name": "Ngorongoro Crater",
        "slug": "ngorongoro-crater",
        "region_slug": "arusha",
        "category": "national_park",
        "description": (
            "The Ngorongoro Crater is the world's largest intact, unflooded volcanic caldera, stretching "
            "260 km² and sitting at a rim altitude of 2,300–2,400 m above sea level. The crater floor "
            "at 1,700 m is a self-contained Eden supporting approximately 25,000–30,000 large animals. "
            "A UNESCO World Heritage Site since 1979, it is managed by the Ngorongoro Conservation Area "
            "Authority (NCAA) and is unique in that Maasai pastoralists share the conservation area.\n\n"
            "The crater's dense populations of the Big Five make it one of Africa's most reliable game "
            "viewing destinations. It hosts the highest density of predators in Africa — up to 62 lions, "
            "large spotted hyena clans, cheetahs, leopards, and the last breeding population of black "
            "rhinoceros in Tanzania. Lake Magadi in the crater floor attracts thousands of flamingos "
            "and over 500 bird species. The descent into the crater is via 4WD only along steep gravel roads.\n\n"
            "Nearby Olduvai Gorge (45 km) is easily combined into a single day visit. The crater rim "
            "offers spectacular views and cool highland air even during the heat of the dry season. "
            "The Lerai Forest on the crater floor is famous for its elephant families and yellow fever trees."
        ),
        "short_description": (
            "The world's largest intact volcanic caldera (260 km²) — a natural Eden with 25,000+ animals "
            "including the Big Five, black rhino, and Africa's densest predator population."
        ),
        "latitude": "-3.161100",
        "longitude": "35.587700",
        "altitude": 2300,
        "difficulty_level": "easy",
        "access_info": (
            "3–4 hours by road from Arusha via the A104 highway. The crater rim villages of "
            "Ngorongoro Conservation Area are accessible by standard vehicle, but 4WD is mandatory "
            "for crater descent. Day visitors must enter and exit the crater on the same day. "
            "Nearest airports: Kilimanjaro International (JRO, ~4 hrs), Arusha Airport (ARK, ~3 hrs). "
            "There are several airstrips near the crater rim for charter flights."
        ),
        "nearest_airport": "Kilimanjaro International Airport (JRO)",
        "distance_from_airport": "185.00",
        "best_time_to_visit": "Year-round; June–October for dry crater floors",
        "seasonal_availability": (
            "Open year-round. The crater is accessible in all seasons — the enclosed microclimate means "
            "game is concentrated regardless of season. Dry season (June–October) offers drier crater "
            "tracks and more vegetation-free viewing. The crater rim is cool and misty year-round, "
            "especially at night (temperatures can drop below 5°C at 2,400m)."
        ),
        "estimated_duration": "Full day (6–8 hours) or combined 2-day Ngorongoro + Serengeti",
        "entrance_fee": "70.80",
        "requires_guide": False,
        "requires_permit": True,
        "is_featured": True,
        "tips": [
            {
                "title": "Pre-book Your Crater Descent",
                "description": (
                    "The NCAA limits the number of vehicles inside the crater daily. Pre-book your "
                    "crater descent permit ($295/vehicle for non-residents) via the NCAA online system "
                    "or through your operator, especially for peak season (June–September)."
                ),
            },
            {
                "title": "Pack Warm Clothes for the Rim",
                "description": (
                    "At 2,300m the rim is cold, especially at night and early morning. Bring a fleece "
                    "and windproof jacket even if visiting during Tanzania's warm months."
                ),
            },
            {
                "title": "Combine with Olduvai Gorge",
                "description": (
                    "Olduvai Gorge is only 45 km from the crater rim and can be easily combined. "
                    "The museum and guided gorge walk take 1.5–2 hours and are well worth including "
                    "in your Ngorongoro day."
                ),
            },
        ],
    },

    # ──────────────────────────────────────────────────────────────
    # 5. STONE TOWN, ZANZIBAR
    # ──────────────────────────────────────────────────────────────
    {
        "name": "Stone Town, Zanzibar",
        "slug": "stone-town-zanzibar",
        "region_slug": "zanzibar",
        "category": "cultural",
        "description": (
            "Stone Town is the historic core of Zanzibar City on Unguja Island and a UNESCO World Heritage "
            "Site since 2000. It represents an exceptional fusion of Swahili, Arab, Indian, Persian, "
            "and European cultures accumulated over centuries of Indian Ocean trade. The town's "
            "labyrinthine alleyways are lined with carved coral-stone buildings, elaborately decorated "
            "wooden doors, mosques, Hindu temples, and colonial-era mansions.\n\n"
            "Covering 96 hectares, Stone Town was once East Africa's most important slave trading port. "
            "The Anglican Cathedral, built over the site of the last great slave market, stands as a "
            "powerful reminder of this history. Other key sites include the House of Wonders (Beit el-Ajaib), "
            "the Old Arab Fort (Ngome Kongwe), the Sultan's Palace Museum, the Darajani Market, "
            "Forodhani Gardens night food market, and the Mercury's House — birthplace of rock legend "
            "Freddie Mercury (born Farrokh Bulsara, 1946).\n\n"
            "Stone Town is a living, working town. Residents navigate the same narrow streets as tourists, "
            "dhows are built and repaired on the waterfront, and the call to prayer echoes from dozens of "
            "minarets. The town serves as the base for Zanzibar spice tours, beach excursions to the north "
            "and east coasts, Jozani Forest (red colobus monkeys), Prison Island (giant tortoises), and "
            "sunset dhow cruises."
        ),
        "short_description": (
            "A UNESCO World Heritage Site of Swahili, Arab, Indian, and European architecture, "
            "carved doors, rich slave history, and the birthplace of Freddie Mercury."
        ),
        "latitude": "-6.162400",
        "longitude": "39.191300",
        "altitude": 10,
        "difficulty_level": "easy",
        "access_info": (
            "Abeid Amani Karume International Airport (ZNZ) is 7 km from Stone Town — 15–20 min by taxi. "
            "From Dar es Salaam: Azam Marine and Coastal Fast Ferries operate high-speed services "
            "(2 hours) to Zanzibar port, which is within walking distance of Stone Town. "
            "Stone Town itself is best explored on foot due to the narrow, vehicle-impassable alleyways."
        ),
        "nearest_airport": "Abeid Amani Karume International Airport (ZNZ)",
        "distance_from_airport": "7.00",
        "best_time_to_visit": "June–October and December–January (dry season)",
        "seasonal_availability": (
            "Open year-round. Heavy rains fall in April–May (long rains) and brief rains in November. "
            "The dry season (June–October) is most pleasant, with warm temperatures (26–30°C), low humidity, "
            "and reliably blue skies. December–January is also excellent, coinciding with the festive period "
            "and Zanzibar International Film Festival (ZIFF) in July."
        ),
        "estimated_duration": "1–3 days (town exploration + day trips)",
        "entrance_fee": "2.00",
        "requires_guide": False,
        "requires_permit": False,
        "is_featured": True,
        "tips": [
            {
                "title": "Hire a Local Walking Guide",
                "description": (
                    "Stone Town's alleys are famously disorienting. A licensed local guide unlocks hidden "
                    "stories of each carved door, family history, and neighbourhood — far more enriching "
                    "than self-guided wandering. Negotiate fees (~$10–20 for 2 hours) at the tourist info "
                    "office near the port."
                ),
            },
            {
                "title": "Visit Forodhani Gardens at Night",
                "description": (
                    "The Forodhani waterfront night market comes alive after 6 PM with vendors selling "
                    "Zanzibar pizza, fresh seafood, sugar cane juice, and Urojo (Zanzibar mix) soup. "
                    "It is one of the best street food experiences in East Africa."
                ),
            },
            {
                "title": "Dress Modestly",
                "description": (
                    "Zanzibar is a predominantly Muslim community. Cover knees and shoulders when visiting "
                    "the old town, mosques, and local markets out of respect for local culture. "
                    "Swimwear is only appropriate at the beach, not in town."
                ),
            },
        ],
    },

    # ──────────────────────────────────────────────────────────────
    # 6. LAKE MANYARA NATIONAL PARK
    # ──────────────────────────────────────────────────────────────
    {
        "name": "Lake Manyara National Park",
        "slug": "lake-manyara-national-park",
        "region_slug": "manyara",
        "category": "national_park",
        "description": (
            "Lake Manyara National Park is a compact but extraordinarily diverse park of 325 km² "
            "situated at the base of the Great Rift Valley escarpment in northern Tanzania. "
            "The park's centrepiece is the shallow, alkaline Lake Manyara which, at peak season, turns "
            "shocking pink with hundreds of thousands of lesser and greater flamingos. "
            "Ernest Hemingway praised it as 'the loveliest lake in Africa'.\n\n"
            "The park is famous for its tree-climbing lions — an unusual behaviour found almost uniquely "
            "here and in Uganda's Queen Elizabeth National Park. Large elephant herds, hippo pools, "
            "breeding colonies of straw-coloured fruit bats (October–July), giraffes, buffaloes, "
            "blue monkeys, baboons, and over 400 bird species inhabit the park's mosaic of groundwater "
            "forest, acacia woodland, and lakeshore marshes.\n\n"
            "The park is often used as the first leg of Tanzania's classic Northern Circuit safari, "
            "combined with Ngorongoro Crater (2 hrs south) and Tarangire (1 hr south). Night drives, "
            "tree canopy walks, and cultural Maasai Boma visits are available as add-ons."
        ),
        "short_description": (
            "A compact Rift Valley park famous for tree-climbing lions, pink flamingo flocks on Lake Manyara, "
            "and over 400 bird species — perfect as the first stop on the Northern Circuit."
        ),
        "latitude": "-3.500000",
        "longitude": "36.000000",
        "altitude": 960,
        "difficulty_level": "easy",
        "access_info": (
            "130 km southwest of Arusha on the B144 road — approximately 2 hours by road. "
            "The main park gate (Mto wa Mbu Gate) is in Mto wa Mbu village. "
            "No direct scheduled flights; nearest airports are Arusha Airport (ARK, 2 hrs) "
            "and Kilimanjaro International (JRO, 2.5 hrs). "
            "Charter flights can land at the park's small airstrip."
        ),
        "nearest_airport": "Arusha Airport (ARK)",
        "distance_from_airport": "130.00",
        "best_time_to_visit": "June–October and January–February",
        "seasonal_availability": (
            "Open year-round. Dry season (June–October) offers best game viewing with animals "
            "concentrated near water. Wet season (March–May) brings lush green scenery and excellent "
            "bird watching as migratory species arrive. Flamingos are most visible October–June when "
            "lake water levels are higher."
        ),
        "estimated_duration": "Half day to full day",
        "entrance_fee": "50.00",
        "requires_guide": False,
        "requires_permit": False,
        "is_featured": False,
        "tips": [
            {
                "title": "Scan the Acacia Trees for Sleeping Lions",
                "description": (
                    "Manyara's tree-climbing lions are most often spotted in yellow fever acacia trees "
                    "along the lakeshore road in the early morning. Ask your driver-guide to scan "
                    "tree branches carefully — they are very well-camouflaged."
                ),
            },
            {
                "title": "Combine with Tarangire and Ngorongoro",
                "description": (
                    "Lake Manyara works perfectly as a half-day stop on the way from Arusha to "
                    "Tarangire (south) or Ngorongoro (west), making it efficient to include on a "
                    "multi-park Northern Circuit safari."
                ),
            },
        ],
    },

    # ──────────────────────────────────────────────────────────────
    # 7. TARANGIRE NATIONAL PARK
    # ──────────────────────────────────────────────────────────────
    {
        "name": "Tarangire National Park",
        "slug": "tarangire-national-park",
        "region_slug": "manyara",
        "category": "national_park",
        "description": (
            "Tarangire National Park covers 2,850 km² of ancient miombo woodland and open savannah in "
            "the Manyara Region, dominated by one of Africa's most spectacular landscapes: thousands of "
            "ancient baobab trees (some over 1,000 years old) rising from the red-ochre earth beside the "
            "seasonal Tarangire River.\n\n"
            "The park hosts Tanzania's largest concentration of elephants — in the dry season (June–October) "
            "over 3,000 elephants converge on the Tarangire River, one of the only permanent water sources "
            "in the area. This congregation creates some of Africa's most impressive elephant watching, "
            "often with multi-generational herds of 50+ individuals. The park is also famous for its "
            "tree-climbing lions, large python sightings, African wild dogs, and a remarkable 550+ bird "
            "species including migratory birds from the Palaearctic zone.\n\n"
            "Tarangire receives far fewer visitors than Serengeti or Ngorongoro, meaning more exclusive "
            "game viewing and uncrowded drives. Entry gates: Kuro Gate (main, southern), Boundary Hill "
            "Gate (north). Kuro Airstrip inside the park serves charter flights. Walking safaris with "
            "armed rangers are available in the park concession areas to the south."
        ),
        "short_description": (
            "Tanzania's elephant haven — 3,000+ elephants gather along the Tarangire River, surrounded by "
            "ancient baobab trees and 550+ bird species in an uncrowded wilderness."
        ),
        "latitude": "-3.833000",
        "longitude": "36.000000",
        "altitude": 1100,
        "difficulty_level": "easy",
        "access_info": (
            "120 km southwest of Arusha — approximately 2 hours by road via the A104. "
            "Main access: Kuro Gate off the A104 highway between Arusha and Dodoma. "
            "Nearest airports: Arusha Airport (ARK, 2 hrs) and Kilimanjaro International (JRO, 2.5 hrs). "
            "Charter flights to Kuro Airstrip inside the park are available from Arusha and Dar es Salaam."
        ),
        "nearest_airport": "Arusha Airport (ARK)",
        "distance_from_airport": "120.00",
        "best_time_to_visit": "June–October (peak elephant concentration)",
        "seasonal_availability": (
            "Open year-round. Dry season (June–October) is peak season when elephants congregate at the "
            "Tarangire River and all other water-dependent wildlife is concentrated in the park. "
            "Wet season (November–May) brings lush greenery and excellent birding with dispersed game. "
            "April–May sees the park at its most verdant and least visited."
        ),
        "estimated_duration": "1–3 days",
        "entrance_fee": "50.00",
        "requires_guide": False,
        "requires_permit": False,
        "is_featured": False,
        "tips": [
            {
                "title": "Visit During the Dry Season for Elephants",
                "description": (
                    "The dry season (June–October) concentrates 3,000+ elephants along the Tarangire "
                    "River — one of the most spectacular wildlife gatherings in Africa. The river drive "
                    "in the morning offers guaranteed elephant encounters."
                ),
            },
            {
                "title": "Look Up in the Baobab Trees",
                "description": (
                    "Leopards rest in the branches of large baobabs during the day. Tree-climbing lions "
                    "are also occasionally spotted. Always scan branches when you stop for any large tree."
                ),
            },
        ],
    },

    # ──────────────────────────────────────────────────────────────
    # 8. MOUNT MERU
    # ──────────────────────────────────────────────────────────────
    {
        "name": "Mount Meru",
        "slug": "mount-meru",
        "region_slug": "arusha",
        "category": "mountain",
        "description": (
            "Mount Meru (4,566 m / 14,980 ft) is Africa's fifth-highest peak and Tanzania's second-highest "
            "mountain, rising majestically inside Arusha National Park just 70 km west of Kilimanjaro. "
            "Often called 'Kilimanjaro's little sister', Meru is a challenging but rewarding 3–4 day trek "
            "through extraordinary scenery: dense rainforest, open moorland, dramatic volcanic cliffs, "
            "and a spectacular crater rim leading to Socialist Peak (summit).\n\n"
            "The Momella Route is the only official trekking route, accessed via Momella Gate at 1,500 m. "
            "An armed park ranger accompanies every group through the park due to elephant, buffalo, and "
            "giraffe on the lower slopes. The trek involves a dramatic crescent-shaped crater rim ascent "
            "on summit day — at times with sheer 1,500m drops into the ash cone below.\n\n"
            "The summit rewards climbers with one of East Africa's finest sunrise views of Kilimanjaro "
            "floating above the clouds. Arusha National Park surrounding the mountain also offers world-class "
            "wildlife game drives: giraffe, zebra, colobus monkey, waterbuck, flamingos on Momella Lakes, "
            "and the occasional leopard."
        ),
        "short_description": (
            "Africa's fifth-highest peak (4,566 m) inside Arusha National Park — a dramatic 3–4 day trek "
            "through forest, moorland, and volcanic crater rim with stunning Kilimanjaro sunrise views."
        ),
        "latitude": "-3.246670",
        "longitude": "36.748330",
        "altitude": 4566,
        "difficulty_level": "challenging",
        "access_info": (
            "Momella Gate (1,500 m) is 25 km from Arusha town — approximately 45 minutes by road via "
            "Usa River. All treks must be booked through a licensed TANAPA operator. An armed ranger "
            "accompanies every group (mandatory, included in park fees). "
            "Nearest airport: Kilimanjaro International (JRO, ~1 hr) and Arusha Airport (ARK, ~45 min)."
        ),
        "nearest_airport": "Kilimanjaro International Airport (JRO)",
        "distance_from_airport": "55.00",
        "best_time_to_visit": "June–October and December–February",
        "seasonal_availability": (
            "Best trekking in the dry seasons: June–October (cold, clear) and December–February "
            "(warm, dry). Long rains (March–May) make the upper slopes muddy and cloud-covered; "
            "short rains (November) bring mist but fewer trekkers. Some operators close November."
        ),
        "estimated_duration": "3–4 days",
        "entrance_fee": "45.00",
        "requires_guide": True,
        "requires_permit": True,
        "is_featured": False,
        "tips": [
            {
                "title": "Use Meru as Kilimanjaro Acclimatisation",
                "description": (
                    "Many Kilimanjaro operators recommend climbing Meru first. The 4,566 m summit "
                    "provides genuine high-altitude acclimatisation that significantly improves "
                    "Kilimanjaro summit success rates. Many trekkers do Meru + Kili back-to-back."
                ),
            },
            {
                "title": "Summit Night Starts at Midnight",
                "description": (
                    "The summit push from Saddle Hut (3,570 m) begins around midnight to reach the "
                    "summit for sunrise over Kilimanjaro. Dress in your warmest layers — the "
                    "exposed crater rim at 4,500 m is extremely cold and windy before dawn."
                ),
            },
        ],
    },

    # ──────────────────────────────────────────────────────────────
    # 9. NYERERE NATIONAL PARK (SELOUS)
    # ──────────────────────────────────────────────────────────────
    {
        "name": "Nyerere National Park",
        "slug": "nyerere-national-park",
        "region_slug": "lindi",
        "category": "national_park",
        "description": (
            "Nyerere National Park, formerly known as Selous Game Reserve, is Africa's largest national park "
            "at 30,893 km², comprising part of one of the world's largest intact ecosystems. "
            "A UNESCO World Heritage Site since 1982, it was renamed in honour of Tanzania's founding "
            "president Julius Nyerere in 2019. The park covers vast stretches of miombo woodland, seasonal "
            "floodplains, and the Rufiji River — Africa's largest river by water volume.\n\n"
            "Unlike northern Tanzania's parks, Nyerere specialises in water-based safaris: motorboat safaris "
            "along the Rufiji, dugout canoe paddles through hippo-rich channels, and walking safaris with "
            "armed rangers through pristine wilderness. The park hosts one of Africa's largest elephant "
            "populations, enormous hippo and crocodile concentrations, the largest lion population in any "
            "single protected area on Earth, wild dogs, sable antelope, and exceptional bird life.\n\n"
            "The park is remote — 230 km and 6 hours from Dar es Salaam by road, or 45 minutes by charter "
            "flight to Mtemere or Matambwe airstrips. This remoteness means genuine exclusivity: far fewer "
            "tourists than the northern circuit with comparable or superior wildlife."
        ),
        "short_description": (
            "Africa's largest national park (30,893 km²) — remote wilderness on the Rufiji River famous for "
            "boat safaris, walking safaris, and the Earth's largest lion population."
        ),
        "latitude": "-9.000000",
        "longitude": "37.400000",
        "altitude": 120,
        "difficulty_level": "moderate",
        "access_info": (
            "By road: 230 km from Dar es Salaam to Mtemere Gate (~6 hours). Road conditions vary; "
            "4WD recommended. By air: Charter flights from Dar es Salaam to Mtemere Airstrip (~45 min) "
            "or Matambwe Airstrip. Arusha charter flights also available (1.5 hrs). "
            "Main gates: Mtemere Gate (eastern, most popular), Matambwe Gate (northwest)."
        ),
        "nearest_airport": "Julius Nyerere International Airport, Dar es Salaam (DAR)",
        "distance_from_airport": "230.00",
        "best_time_to_visit": "June–October (dry season)",
        "seasonal_availability": (
            "Open year-round, but many camps close during the long rains (March–May) when "
            "park roads become impassable and the Rufiji floods. Peak season June–October "
            "offers dry conditions, concentrated wildlife, and the best boat safari experiences. "
            "January–February is a good shoulder season with lower rates and fewer visitors."
        ),
        "estimated_duration": "3–5 days",
        "entrance_fee": "70.00",
        "requires_guide": True,
        "requires_permit": False,
        "is_featured": False,
        "tips": [
            {
                "title": "Book a Boat Safari on the Rufiji",
                "description": (
                    "The Rufiji River boat safari is Nyerere's signature experience — floating past "
                    "hippo pods, basking crocodiles, fish eagles, and elephants drinking from the bank. "
                    "It is completely different from a standard game drive and not available anywhere "
                    "else on the northern Tanzania circuit."
                ),
            },
            {
                "title": "Fly In — Don't Drive",
                "description": (
                    "The 6-hour road from Dar es Salaam to Mtemere is rough. Flying in by charter "
                    "(~$200–350 one way from Dar es Salaam, 45 min) saves a full day of travel and is "
                    "worth the cost for a 3–4 day visit."
                ),
            },
        ],
    },

    # ──────────────────────────────────────────────────────────────
    # 10. OLDUVAI GORGE
    # ──────────────────────────────────────────────────────────────
    {
        "name": "Olduvai Gorge",
        "slug": "olduvai-gorge",
        "region_slug": "arusha",
        "category": "historical",
        "description": (
            "Olduvai Gorge is one of the most important paleoanthropological sites on Earth — a 48 km "
            "gorge cutting through the Serengeti plains in the Ngorongoro Conservation Area, exposing "
            "geological strata spanning 2 million years of human evolution. The gorge was made globally "
            "famous by Louis and Mary Leakey, who made a series of landmark fossil discoveries here from "
            "the 1930s to 1970s, including Paranthropus boisei ('Nutcracker Man') in 1959 and Homo habilis "
            "in 1960 — the first specimens of Homo habilis ever found.\n\n"
            "The Olduvai Gorge Museum (rebuilt 2017) is a modern interpretive centre displaying original "
            "fossils, stone tools from the Oldowan and Acheulean industries, and life-sized reconstructions "
            "of early hominins. A licensed guide leads visitors on a 1.5-hour walk into the gorge to the "
            "actual excavation sites still actively worked by archaeologists from around the world. "
            "The gorge is set within dramatic open plains with views of the volcanic Ngorongoro highlands "
            "and Lemagrut volcano.\n\n"
            "The site is easily combined with a Ngorongoro Crater visit (45 km) or en route between "
            "Ngorongoro and the Serengeti."
        ),
        "short_description": (
            "The cradle of humanity — a 2-million-year-old gorge in the Ngorongoro Conservation Area "
            "where the Leakeys discovered Homo habilis and Paranthropus boisei, reshaping human history."
        ),
        "latitude": "-2.993600",
        "longitude": "35.351100",
        "altitude": 1490,
        "difficulty_level": "easy",
        "access_info": (
            "Located 45 km west of Ngorongoro Crater on the road to Serengeti (B142). "
            "Accessible by standard 4WD vehicle on a tarmac/gravel road. "
            "Most visitors stop here en route from Ngorongoro to Serengeti or as a day trip "
            "from Ngorongoro rim lodges. Nearest airports: Kilimanjaro International (JRO, ~4 hrs) "
            "and Arusha Airport (ARK, ~3.5 hrs)."
        ),
        "nearest_airport": "Kilimanjaro International Airport (JRO)",
        "distance_from_airport": "230.00",
        "best_time_to_visit": "Year-round",
        "seasonal_availability": (
            "Open year-round. The gorge itself is accessible in all weather conditions. "
            "The road from Ngorongoro to Olduvai and onto Serengeti can become difficult in heavy rains "
            "(April–May), but the site itself is always accessible."
        ),
        "estimated_duration": "1.5–2.5 hours",
        "entrance_fee": "30.00",
        "requires_guide": True,
        "requires_permit": False,
        "is_featured": False,
        "tips": [
            {
                "title": "A Guide is Mandatory and Worthwhile",
                "description": (
                    "The gorge requires a licensed guide who explains what you are seeing at excavation "
                    "sites — without this context the rocky gorge walls appear unremarkable. "
                    "The guide fee is included in the entrance fee."
                ),
            },
            {
                "title": "Combine with Ngorongoro for a Full Day",
                "description": (
                    "Olduvai Gorge (1.5 hrs) combines perfectly with a Ngorongoro Crater day. "
                    "Start with the crater game drive (morning), stop at Olduvai en route to the "
                    "Serengeti in the afternoon."
                ),
            },
        ],
    },

    # ──────────────────────────────────────────────────────────────
    # 11. MAFIA ISLAND MARINE PARK
    # ──────────────────────────────────────────────────────────────
    {
        "name": "Mafia Island Marine Park",
        "slug": "mafia-island-marine-park",
        "region_slug": "pwani",
        "category": "island",
        "description": (
            "Mafia Island Marine Park is one of the largest marine protected areas in the Indian Ocean, "
            "covering 822 km² of pristine coral reef ecosystems, seagrass beds, mangrove forests, and "
            "open ocean off Tanzania's southern coast. The park is widely regarded as one of East Africa's "
            "finest diving and snorkelling destinations, with vibrant coral gardens, pelagic fish schools, "
            "manta rays, turtles, and excellent macro photography subjects.\n\n"
            "Mafia Island is most famous for its whale shark aggregation (October–March, peak Nov–Feb) — "
            "one of the most predictable whale shark encounters in the world, with groups of up to 20 "
            "individuals feeding in the shallow Ras Kisimani waters. All whale shark swimming is "
            "regulated by PADI-trained conservation guides who enforce no-touch rules.\n\n"
            "The island itself remains refreshingly undeveloped compared to Zanzibar, with a genuine "
            "Swahili fishing community, the historic ruins of Kua on Juani Island (a 9th-century Shirazi "
            "settlement destroyed by Sakalava pirates in 1820), and a slow, authentic pace of life. "
            "Dive operators Big Blu and Mafia Island Diving operate PADI courses and fun dives "
            "year-round from Utende Beach."
        ),
        "short_description": (
            "East Africa's finest marine park — world-class coral reefs, predictable whale shark encounters "
            "(Oct–Mar), manta rays, and authentic Swahili island life, free from Zanzibar's crowds."
        ),
        "latitude": "-7.850000",
        "longitude": "39.783300",
        "altitude": 5,
        "difficulty_level": "easy",
        "access_info": (
            "By air: Daily Coastal Aviation and Auric Air flights from Dar es Salaam to Mafia Airport "
            "(MFA) — 45 minutes. By ferry: Weekly MV Kilimanjaro ferry from Dar es Salaam to Kilindoni "
            "Port (~6 hours). Most dive resorts arrange transfers from the airport/port. "
            "Utende Beach (main dive area) is 14 km from Kilindoni town."
        ),
        "nearest_airport": "Mafia Airport (MFA)",
        "distance_from_airport": "14.00",
        "best_time_to_visit": "October–March for whale sharks; June–September for best dive visibility",
        "seasonal_availability": (
            "Open year-round but some dive operators close in April–May during the heavy monsoon. "
            "October–March is whale shark season. June–September offers the best underwater visibility "
            "(30m+) and calm seas. Avoid the long rains (April–May) for diving as visibility drops."
        ),
        "estimated_duration": "3–7 days",
        "entrance_fee": "23.50",
        "requires_guide": False,
        "requires_permit": False,
        "is_featured": False,
        "tips": [
            {
                "title": "Book Whale Shark Trips in Advance",
                "description": (
                    "Whale shark season (October–March) is Mafia's busiest period. Pre-book your "
                    "whale shark swim directly with Big Blu or Mafia Island Diving at least 2 months "
                    "in advance. Each swim is limited to 4 swimmers per shark."
                ),
            },
            {
                "title": "Visit Kua Ruins on Juani Island",
                "description": (
                    "The Kua Ruins on adjacent Juani Island are one of Tanzania's most atmospheric "
                    "historical sites — a deserted 9th-century Shirazi city reclaimed by jungle. "
                    "Combine with snorkelling at nearby Chole Bay for a perfect day trip."
                ),
            },
        ],
    },

    # ──────────────────────────────────────────────────────────────
    # 12. MAHALE MOUNTAINS NATIONAL PARK
    # ──────────────────────────────────────────────────────────────
    {
        "name": "Mahale Mountains National Park",
        "slug": "mahale-mountains-national-park",
        "region_slug": "kigoma",
        "category": "national_park",
        "description": (
            "Mahale Mountains National Park is one of Africa's most remote and extraordinary wildlife "
            "destinations, situated on the eastern shore of Lake Tanganyika — the world's longest lake "
            "and second deepest — in western Tanzania. The park's 1,613 km² protect the Mahale Mountain "
            "range rising to 2,462 m from the lake shore, covered in dense montane forest, miombo woodland, "
            "and grassland.\n\n"
            "Mahale is one of only two Tanzanian parks (alongside Gombe) where habituated chimpanzees can "
            "be tracked on foot. The park hosts approximately 800–1,000 eastern chimpanzees, many of whom "
            "have been studied since the 1960s by Kyoto University researchers. Trekking involves following "
            "ranger trackers through dense forest — when you find a chimp family, you spend one hour "
            "observing from 8 metres as they groom, play, and forage above you.\n\n"
            "The park has no roads — the only access is by boat from Kigoma or by charter aircraft. "
            "This isolation guarantees an exclusive experience: a maximum of 3–4 groups of 4 people "
            "track chimps per day, ensuring no crowding. Lake Tanganyika's crystal-clear water, snorkelling "
            "with colourful endemic cichlid fish, and sunset views over the lake add to Mahale's "
            "unique combination of forest and beach."
        ),
        "short_description": (
            "Africa's most remote chimp trekking — 800+ habituated eastern chimpanzees in pristine "
            "forest above Lake Tanganyika's crystal-clear shores, accessible only by boat or charter plane."
        ),
        "latitude": "-6.267000",
        "longitude": "29.933000",
        "altitude": 773,
        "difficulty_level": "challenging",
        "access_info": (
            "By air: Charter flights from Dar es Salaam or Arusha to Mahale airstrip (~2.5 hrs). "
            "By ferry + boat: MV Liemba ferry from Kigoma (12 hrs south along Lake Tanganyika) "
            "then dugout canoe transfer to park HQ. Kigoma is reached by air from Dar es Salaam "
            "(1 hr) or by TAZARA railway (36 hrs). There are no roads inside the park."
        ),
        "nearest_airport": "Kigoma Airport (TKQ)",
        "distance_from_airport": "120.00",
        "best_time_to_visit": "June–October (dry season, best chimp tracking)",
        "seasonal_availability": (
            "Open year-round, but the rainy season (November–April) makes forest trails very muddy "
            "and chimp tracking more difficult. Dry season (June–October) is optimal for tracking "
            "with clear trails and chimps moving more predictably. Some lodges close April–May."
        ),
        "estimated_duration": "3–5 days",
        "entrance_fee": "80.00",
        "requires_guide": True,
        "requires_permit": True,
        "is_featured": False,
        "tips": [
            {
                "title": "Maximum 1 Hour with the Chimps",
                "description": (
                    "TANAPA regulations strictly limit each group to 1 hour with a chimp family, "
                    "maximum 4 people per permit. Arrive in peak condition: trekking to find chimps "
                    "can involve 2–5 hours of steep, humid forest walking."
                ),
            },
            {
                "title": "Snorkel in Lake Tanganyika",
                "description": (
                    "Don't miss snorkelling in Lake Tanganyika's gin-clear water. The lake is home "
                    "to over 250 species of endemic cichlid fish found nowhere else on Earth. "
                    "Many lodges provide snorkel equipment from the beach."
                ),
            },
        ],
    },

    # ──────────────────────────────────────────────────────────────
    # 13. ZANZIBAR SPICE TOUR
    # ──────────────────────────────────────────────────────────────
    {
        "name": "Zanzibar Spice Farms",
        "slug": "zanzibar-spice-farms",
        "region_slug": "zanzibar",
        "category": "cultural",
        "description": (
            "Zanzibar has been known as the 'Spice Island' for over five centuries, and a spice farm tour "
            "is one of the most memorable cultural experiences the island offers. The spice farms of "
            "central Zanzibar (mainly around Kizimbani and Kindichi villages, 10–15 km from Stone Town) "
            "grow over 60 spice and tropical plant varieties including cloves (Zanzibar once produced 80% "
            "of the world's supply), nutmeg, vanilla, cardamom, cinnamon, black pepper, turmeric, "
            "lemongrass, ylang-ylang, henna, and dozens of tropical fruits: jackfruit, breadfruit, "
            "papaya, starfruit, and soursop.\n\n"
            "Licensed Zanzibari guides lead visitors through working farms, identifying plants by smell "
            "and taste, demonstrating traditional uses in cooking and medicine, and showing the art of "
            "climbing coconut palms barefoot. Most tours end with a freshly cooked Swahili lunch on "
            "the farm, featuring the spices harvested during the walk. The experience gives vivid context "
            "to the same aromas found in Stone Town's markets and restaurants.\n\n"
            "Tours typically include Kidichi Persian Baths (built 1850 for Sultan Seyyid Said's Persian wife), "
            "Kizimbani State Farm, and optional Prison Island stop for Aldabra giant tortoises."
        ),
        "short_description": (
            "A multi-sensory walk through working spice farms growing cloves, vanilla, and 60+ spices "
            "that built Zanzibar's fame as the 'Spice Island' — ending with a fresh Swahili farm lunch."
        ),
        "latitude": "-6.165900",
        "longitude": "39.202600",
        "altitude": 50,
        "difficulty_level": "easy",
        "access_info": (
            "Spice farm tours depart from Stone Town daily — most operators pick up from hotels. "
            "The farms are 10–15 km from Stone Town (20–30 min drive) near Kizimbani village. "
            "Tours can be booked at guesthouses, tour agencies along Creek Road in Stone Town, "
            "or through major operators like Sama Tours and Authentic Zanzibar. "
            "Nearest airport: Abeid Amani Karume International (ZNZ, 15 min from Stone Town)."
        ),
        "nearest_airport": "Abeid Amani Karume International Airport (ZNZ)",
        "distance_from_airport": "20.00",
        "best_time_to_visit": "Year-round; clove harvest (July–September) for extra atmosphere",
        "seasonal_availability": (
            "Tours run year-round. The clove harvest season (July–September) is particularly atmospheric "
            "as you can see and smell fresh cloves being harvested and dried. Tours continue during "
            "rain seasons but are more pleasant in dry conditions (June–October and December–January)."
        ),
        "estimated_duration": "3–5 hours (half day)",
        "entrance_fee": "15.00",
        "requires_guide": True,
        "requires_permit": False,
        "is_featured": False,
        "tips": [
            {
                "title": "Wear Comfortable Shoes and Clothes That Can Get Dirty",
                "description": (
                    "Spice farm walks go through muddy red earth paths and require you to handle "
                    "plants and fruit. Wear closed shoes (not sandals) and clothes you don't mind "
                    "getting stained from turmeric and soil."
                ),
            },
            {
                "title": "Bring Small USD Bills for Tipping and Craft Sellers",
                "description": (
                    "Guides expect a small tip (~$5–10) for excellent tours. Local women often "
                    "weave palm fronds into hats and baskets for you during the tour — have $2–5 "
                    "ready to support their craft."
                ),
            },
        ],
    },

    # ──────────────────────────────────────────────────────────────
    # 14. RUAHA NATIONAL PARK
    # ──────────────────────────────────────────────────────────────
    {
        "name": "Ruaha National Park",
        "slug": "ruaha-national-park",
        "region_slug": "lindi",
        "category": "national_park",
        "description": (
            "Ruaha National Park is Tanzania's second-largest national park at 22,000 km², lying in the "
            "heart of the country in the Iringa and Ruaha highlands. It is one of Africa's most wild and "
            "exclusive safari destinations — receiving only a fraction of the visitors of the northern "
            "circuit, yet supporting some of Africa's highest densities of elephant, lion, leopard, "
            "cheetah, and African wild dog.\n\n"
            "The Great Ruaha River forms the park's spine, creating dramatic riverine corridors through "
            "ancient miombo woodland and rocky baobab-studded hills. The river is particularly spectacular "
            "in the dry season (May–November) when elephants, hippos, crocodiles, and lions gather "
            "along its banks. Ruaha hosts Tanzania's largest elephant population (over 20,000 individuals) "
            "and the world's largest remaining population of greater kudu. "
            "African wild dogs are frequently seen here — more reliably than almost anywhere else.\n\n"
            "Unlike the northern parks, Ruaha offers genuine wilderness: you can drive for hours without "
            "seeing another vehicle. Walking safaris with armed rangers are available and add a completely "
            "different dimension to the wildlife experience."
        ),
        "short_description": (
            "Tanzania's second-largest park (22,000 km²) — an exclusive, uncrowded wilderness with "
            "20,000+ elephants, Africa's most reliable wild dog sightings, and dramatic Ruaha River scenery."
        ),
        "latitude": "-7.800000",
        "longitude": "34.900000",
        "altitude": 950,
        "difficulty_level": "moderate",
        "access_info": (
            "By air: Charter flights from Dar es Salaam or Arusha to Msembe Airstrip inside the park "
            "(~1.5 hrs from Dar es Salaam). By road: 625 km from Dar es Salaam via Iringa (~8–10 hrs), "
            "or 9 hours from Arusha. 4WD mandatory. Main gate: Msembe Gate (park HQ). "
            "Nearest city: Iringa (130 km from Msembe Gate)."
        ),
        "nearest_airport": "Julius Nyerere International Airport, Dar es Salaam (DAR)",
        "distance_from_airport": "625.00",
        "best_time_to_visit": "May–November (dry season)",
        "seasonal_availability": (
            "Best visited during the long dry season (May–November) when the Ruaha River is low, "
            "vegetation is sparse, and wildlife congregates at water points. December–April brings "
            "the rains; parks roads become challenging but birding is excellent. "
            "Some camps close January–March during the wettest months."
        ),
        "estimated_duration": "3–5 days",
        "entrance_fee": "70.00",
        "requires_guide": False,
        "requires_permit": False,
        "is_featured": False,
        "tips": [
            {
                "title": "Request Wild Dog Tracking",
                "description": (
                    "Ruaha has some of Africa's best African wild dog viewing. Ask your guide to radio "
                    "other camps for dog sightings on arrival — many lodges share real-time data "
                    "to maximise guest sightings."
                ),
            },
            {
                "title": "Fly In for the Best Experience",
                "description": (
                    "The road from Dar es Salaam is long and rough. Charter flights to Msembe Airstrip "
                    "from Dar es Salaam (~$300–400 one way) save a full day and are strongly recommended "
                    "for any visit under 5 days."
                ),
            },
        ],
    },

    # ──────────────────────────────────────────────────────────────
    # 15. MIKUMI NATIONAL PARK
    # ──────────────────────────────────────────────────────────────
    {
        "name": "Mikumi National Park",
        "slug": "mikumi-national-park",
        "region_slug": "lindi",
        "category": "national_park",
        "description": (
            "Mikumi National Park covers 3,230 km² of open flood plains, acacia woodland, and miombo "
            "hills in central Tanzania, bisected by the A7 Dar es Salaam–Zambia highway. It is Tanzania's "
            "most accessible national park from Dar es Salaam, just 283 km and 4.5–5 hours away, making "
            "it a popular weekend destination for Dar residents and a productive short safari option for "
            "travellers with limited time.\n\n"
            "The Mkata Flood Plain in the park's northern section is its wildlife engine — "
            "a seasonally flooded grassland that concentrates large herds of buffalo (up to 1,000 strong), "
            "elephants, wildebeest, zebra, impala, warthog, giraffe, and eland. Lions are regularly seen "
            "here, as are leopards in the miombo woodland and hippos at Hippo Pool. "
            "The park is sometimes called 'Tanzania's little Serengeti' for the Mkata Plain's open views.\n\n"
            "Mikumi is managed jointly with the adjacent Selous (Nyerere) ecosystem — migratory corridors "
            "allow wildlife to move freely between the two. The park offers excellent value for travellers "
            "who cannot afford the longer northern or southern circuit trips."
        ),
        "short_description": (
            "The closest national park to Dar es Salaam (283 km) — 'Tanzania's little Serengeti' with "
            "large buffalo herds, elephants, lions, and open Mkata flood plains, perfect for weekends."
        ),
        "latitude": "-7.316700",
        "longitude": "36.883300",
        "altitude": 550,
        "difficulty_level": "easy",
        "access_info": (
            "283 km from Dar es Salaam on the A7 tarmac highway — 4.5 to 5 hours by road. "
            "Standard vehicles are fine on main park roads in the dry season; 4WD recommended "
            "for off-road tracks and wet season. Main gate: Mikumi Gate (main entrance off A7). "
            "Nearest airport: Julius Nyerere International, Dar es Salaam (DAR). "
            "Charter flights to Mikumi Airstrip are also available."
        ),
        "nearest_airport": "Julius Nyerere International Airport, Dar es Salaam (DAR)",
        "distance_from_airport": "283.00",
        "best_time_to_visit": "June–October (dry season) and January–February",
        "seasonal_availability": (
            "Open year-round. Dry season (June–October) offers the best game viewing on the Mkata "
            "Plain as animals concentrate near the Mkata River. Wet season (March–May) brings "
            "dramatic skies and lush green scenery but some tracks flood. "
            "January–February is a productive shoulder season with fewer visitors."
        ),
        "estimated_duration": "1–3 days",
        "entrance_fee": "45.00",
        "requires_guide": False,
        "requires_permit": False,
        "is_featured": False,
        "tips": [
            {
                "title": "Drive the Mkata Plain at Dawn",
                "description": (
                    "The Mkata Flood Plain is most active at dawn — lions are still on their night hunts, "
                    "buffaloes are moving to water, and the light is spectacular for photography. "
                    "Leave camp at 6 AM for the best experience."
                ),
            },
            {
                "title": "Book a Weekend Package from Dar es Salaam",
                "description": (
                    "Several Dar es Salaam operators offer Friday afternoon departure / Sunday return "
                    "packages for Mikumi (from ~$300–500/person all-inclusive). This is one of Africa's "
                    "most affordable national park experiences for the quality of wildlife seen."
                ),
            },
        ],
    },
]


class Command(BaseCommand):
    help = "Seed the database with 15 GPS-accurate Tanzania tourism attractions and required regions"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Clear existing attractions and regions before seeding",
        )

    def handle(self, *args, **options):
        if options["clear"]:
            self.stdout.write("Clearing existing data...")
            Attraction.objects.all().delete()
            Region.objects.all().delete()
            self.stdout.write(self.style.WARNING("Existing attractions and regions deleted."))

        # Use first superuser as creator
        user = User.objects.filter(is_superuser=True).first()
        if not user:
            self.stdout.write(self.style.ERROR(
                "No superuser found. Create one first: python src/manage.py createsuperuser"
            ))
            return

        self.stdout.write(f"Using user '{user.username}' as creator.")

        # ── Seed Regions ──────────────────────────────────────────
        self.stdout.write("\nSeeding regions...")
        region_map = {}
        for r_data in REGIONS:
            region, created = Region.objects.get_or_create(
                slug=r_data["slug"],
                defaults={
                    "name": r_data["name"],
                    "description": r_data["description"],
                    "latitude": r_data["latitude"],
                    "longitude": r_data["longitude"],
                },
            )
            region_map[r_data["slug"]] = region
            status = "CREATED" if created else "EXISTS"
            self.stdout.write(f"  [{status}] {region.name}")

        # ── Seed Attractions ──────────────────────────────────────
        self.stdout.write("\nSeeding attractions...")
        created_count = 0
        skipped_count = 0

        for a_data in ATTRACTIONS:
            region = region_map.get(a_data["region_slug"])
            if not region:
                self.stdout.write(self.style.ERROR(
                    f"  [ERROR] Region '{a_data['region_slug']}' not found for '{a_data['name']}'"
                ))
                continue

            tips_data = a_data.pop("tips", [])
            region_slug = a_data.pop("region_slug")

            attraction, created = Attraction.objects.get_or_create(
                slug=a_data["slug"],
                defaults={
                    **{k: v for k, v in a_data.items() if k not in ("slug",)},
                    "region": region,
                    "created_by": user,
                    "featured_image": "",  # placeholder — add images via admin/Cloudinary
                },
            )

            if created:
                # Seed tips
                for tip in tips_data:
                    AttractionTip.objects.create(
                        attraction=attraction,
                        title=tip["title"],
                        description=tip["description"],
                        created_by=user,
                    )
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f"  [CREATED] {attraction.name} — {len(tips_data)} tips")
                )
            else:
                skipped_count += 1
                self.stdout.write(f"  [EXISTS]  {attraction.name}")

        self.stdout.write(
            self.style.SUCCESS(
                f"\n✓ Done: {created_count} attractions created, {skipped_count} skipped (already exist)."
            )
        )
        self.stdout.write(
            self.style.WARNING(
                "\nNote: featured_image is set to empty string. "
                "Upload images via Django Admin or Cloudinary API before publishing."
            )
        )
