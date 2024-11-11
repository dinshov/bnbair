import csv
import sys
import os
import ast
Ginfo, Hinfo=[],[]
def welcome():
    print('WELCOME TO AIRDPC TOURS AND TRAVELS SERVICES!')
    print('*************************************************************************************')
    print('*************************************************************************************')
    user=input('Enter G if you are here as a Guest or H if you are a host').upper()
    if user in ['H', 'G']:
        return user
    else:
        print('Ooops! wrong code :(')
        welcome()
def mainmenug():
    print('*************************************************************************************')
    print('                                                MAIN MENU                                              ')
    print('*************************************************************************************')
    print('''Welcome again! Please enter the option corresponding to your desired ammendments
1) VIEW YOUR ACCOUNT
2) UPDATE YOUR ACCOUNT
3) BOOK OUR TRAVEL PLAN
4) BOOK HOTEL SERVICES ONLY
5) BOOK TRANSPORT SERVICES ONLY
6) EXIT''')
    c=int(input())
    return c
def authen(p,x):
    if p==x:
        return 1
    else:
        return 0
def inserttog(gid,name,cn,p):
    l=[gid,name,cn,p]
    f1=open('guest.csv','w', newline='')
    fw=csv.writer(f1)
    fw.writerow(l)
    f1.close()
    global Ginfo
    Ginfo=l
def createg():
    gname=input('NAME:')
    gid=input('GUEST ID:')
    cn=input('CONTACT NO:')
    passwd=input('Enter Password:')
    x=input('Confirm Password')
    if authen(passwd,x)==1:
        print('Account creation is successful')
        inserttog(gid,gname,cn,passwd)
        
    else:
        a=int(input('''Oops! Password is not verified, do you want to
1)create new password?
2)Exit?'''))
        if a==1:
            ps=input('Enter password:')
            x=input('Confirm password:')
            if authen(ps,x)==1:
                print('Account creation is successful')
                inserttog(gid,gname,cn,ps)
                
            else:
                print('Sorry we are unable to connect you to our services. Program terminating')
                sys.exit()
        else:
            sys.exit()
def existingg():
    gid=input('GUEST ID:')
    ps=input('PASSWORD:')
    f1=open('guest.csv','r',newline='')
    global Ginfo
    fr=csv.reader(f1)
    for row in fr:
        if row[0]==gid:
            if authen(ps,row[3])==1:
                Ginfo=row
                return 0
            else:
                print('Incorrect password')
                a=int(input(''' Do you want to:
    1) TRY AGAIN?
    2) EXIT'''))
                if a==1:
                    existingg()
                else:
                    print('PROGRAM TERMINATING')
            
    else:
        print('Sorry, user not found')
        a=int(input('''1)TRY AGAIN?
2) CREATE NEW ACCOUNT?
3) EXIT'''))
        if a==1:
             existingg()
        elif a==2:
            createg()
        elif a==3:
            print('PROGRAM TERMINATING')
            sys.exit()
        else:
            print('Oops! Incorrect choice. you will be taken to log in portal')
            return 3
def retryg():
    x=existingg()
    if x==0:
        print('LOG IN SUCCESSFUL')
    elif x==1:
        y=existingg()
        if y==1:
            print('Incorrect Password. You have exceeded the number of tries to sign in. Thank you')
            return 3
        elif y==0:
            print('LOG IN SUCCESSFUL')
        elif y==2:
            print('PROGRAM TERMINATING')
            sys.exit()
        elif y==3:
            return 3
    elif x==2:
        print('PROGRAM TERMINATING')
        sys.exit()
    elif x==3:
        return 3
def loging():
    print('*************************************************************************************')
    print('                        AUTHORISATION AND AUTHENTICATION                        ')
    print('*************************************************************************************')
    
    a=int(input('''CHOOSE METHOD OF AUTHORISATION:
1) LOG IN
2) SIGN UP
3) EXIT'''))
    if a==1:
        x=retryg()
        if x==3:
            loging()
    elif a==2:
        createg()
    elif a==3:
        print('PROGRAM TERMINATING')
        sys.exit()
    else:
        print('Sorry, invalid choice')
        loging()
def displayg():
    print('GUEST ID', Ginfo[0])
    print('GUEST NAME', Ginfo[1])
    print('CONTACT DETAILS:', Ginfo[2])

def updateg():
    f1=open('guest.csv','r', newline='')
    print('*************************************************************************************')
    print('                             ORIGINAL GUEST INFORMATION                               ')
    print('*************************************************************************************')
    displayg()
    



def mainmenuh():
    print('*************************************************************************************')
    print('                                             MAIN MENU                                               ')
    print('*************************************************************************************')
    print('''Welcome again! Please enter the option corresponding to your desired ammendments
1)VIEW YOUR ACCOUNT
2)UPDATE YOUR ACCOUNT''')
    c=int(input())
    return c
def authen(p,x):
    if p==x:
        return 1
    else:
        return 0
def inserttoh(hid,hname,cn,p):
    l=[hid,hname,cn,p]
    f1=open('host.csv','w', newline='')
    fw=csv.writer(f1)
    fw.writerow(l)
    f1.close()
    global Hinfo
    Hinfo=l
def createh():
    hname=input('NAME:')
    hid=input(' HOST ID:')
    cn=input('CONTACT NO:')
    passwd=input('Enter Password:')
    x=input('Confirm Password')
    if authen(passwd,x)==1:
        print('Account creation is successful')
        inserttoh(hid,hname,cn,passwd)
        
    else:
        a=int(input('''Oops! Password is not verified, do you want to
1)create new password?
2)Exit?'''))
        if a==1:
            ps=input('Enter password:')
            x=input('Confirm password:')
            if authen(ps,x)==1:
                print('Account creation is successful')
                inserttoh(hid,hname,cn,ps)
                
            else:
                print('Sorry we are unable to connect you to our services. Program terminating')
                sys.exit()
        else:
            sys.exit()
def existingh():
    hid=input('HOST ID:')
    ps=input('PASSWORD:')
    f1=open('host.csv','r',newline='')
    fr=csv.reader(f1)
    for row in fr:
        if row[0]==hid:
             l=row
         
             if authen(ps,l[3])==1:
                 global Hinfo
                 Hinfo=l
                 return 0
             else:
                 print('Incorrect password')
                 a=int(input(''' Do you want to:
            1) TRY AGAIN?
            2) EXIT'''))
                 return a
            
        
    else:
        print('Sorry, user not found')
        a=int(input('''1)TRY AGAIN?
2) CREATE NEW ACCOUNT?
3) EXIT'''))
        if a==1:
            existingh()
        elif a==2:
            createh()
        elif a==3:
            print('PROGRAM TERMINATING')
            sys.exit()
        else:
            print('Oops! Incorrect choice. you will be taken to log in portal')
            return 3
def retryh():
    x=existingh()
    if x==0:
        print('LOG IN SUCCESSFUL')
        
    elif x==1:
        y=existingh()
        if y==1:
            print('Incorrect Password. You have exceeded the number of tries to sign in. Thank you')
            return 3
        elif y==0:
            print('LOG IN SUCCESSFUL')
            
        elif y==2:
            print('PROGRAM TERMINATING')
            sys.exit()
        elif y==3:
            return 3
    elif x==2:
        print('PROGRAM TERMINATING')
        sys.exit()
    elif x==3:
        return 3
def loginh():
    print('*************************************************************************************')
    print('                        AUTHORISATION AND AUTHENTICATION                        ')
    print('*************************************************************************************')
    
    a=int(input('''CHOOSE METHOD OF AUTHORISATION:
1) LOG IN
2) SIGN UP
3) EXIT'''))
    if a==1:
        x=retryh()
        if x==3:
            loginh()
    elif a==2:
        createh()
    elif a==3:
        print('PROGRAM TERMINATING')
        sys.exit()
    else:
        print('Sorry, invalid choice')
        loginh()

def host_interface():
    loginh()

def guest_interface():
    loging()

#destination choosing
import csv
import os
import sys
def setdestinations():
    
    fd=open('internationd.csv','w', newline='')
    fw=csv.writer(fd)
   #dest list = [index, place, description, category,[plans],]
    l=[[1, "Paris, France", "The city of love, offering romantic strolls along the Seine, Eiffel Tower views, and charming cafés.", "Romantic Getaways", 
     ["Visit the Eiffel Tower", "Stroll along the Seine", "Explore Montmartre", "Cruise on the Seine River", "Visit the Louvre Museum", "Picnic in Jardin des Tuileries"]],
      [2, "Venice, Italy", "Famous for gondola rides through its picturesque canals and historic architecture.", "Romantic Getaways", 
     ["Gondola ride through the canals", "Visit St. Mark’s Basilica", "Explore the Doge's Palace", "Wander the narrow streets", "Shop for Murano glass"]],
      [3, "Bora Bora, French Polynesia", "Overwater bungalows and stunning turquoise lagoons, perfect for honeymooners.", "Romantic Getaways", 
     ["Stay in an overwater bungalow", "Snorkel in the crystal-clear lagoons", "Take a romantic boat cruise", "Relax on Matira Beach", "Explore Mount Otemanu"]],
      [4, "Santorini, Greece", "Gorgeous sunsets, whitewashed buildings, and serene beaches.", "Romantic Getaways", 
     ["Watch the sunset in Oia", "Stroll through Fira", "Visit ancient Akrotiri", "Relax at Red Beach", "Wine-tasting at local vineyards"]],
      [5, "Maldives", "Luxury overwater resorts with breathtaking beach views, perfect for an intimate getaway.", "Romantic Getaways", 
     ["Stay in an overwater villa", "Snorkel with tropical fish", "Private beach dinners", "Dive in coral reefs", "Spa treatments", "Relax in private infinity pools"]],
      [6, "Queenstown, New Zealand", "The adventure capital of the world, offering bungee jumping, skydiving, and skiing.", "Adventure Travel", 
     ["Bungee jump off the Kawarau Bridge", "Skydiving over Lake Wakatipu", "Take a jet boat ride", "Hike the Routeburn Track", "Skiing in the winter", "Go wine-tasting"]],
      [7, "Costa Rica", "Explore rainforests, volcanoes, wildlife, and go zip-lining, surfing, or white-water rafting.", "Adventure Travel", 
     ["Zip-line through rainforests", "Visit Arenal Volcano", "Surf at Playa Tamarindo", "Hike in Corcovado National Park", "White-water rafting", "Wildlife watching"]],
      [8, "Nepal", "Trekking to Everest Base Camp, the Annapurna Circuit, and rafting in the Trishuli River.", "Adventure Travel", 
     ["Trek to Everest Base Camp", "Rafting in the Trishuli River", "Visit Kathmandu's temples", "Explore Pokhara", "Hike in the Annapurna region", "Mountain biking"]],
      [9, "Iceland", "Glaciers, volcanoes, and hot springs; perfect for hiking, ice climbing, and exploring natural wonders.", "Adventure Travel", 
     ["Hike to Gullfoss Waterfall", "Visit the Blue Lagoon", "Go ice climbing", "Explore volcanoes", "Snorkel in Silfra Fissure", "Chase the Northern Lights"]],
      [10, "Patagonia, Argentina/Chile", "Hike through glaciers, fjords, and rugged mountains in one of the most remote and beautiful places on earth.", "Adventure Travel", 
     ["Hike in Torres del Paine National Park", "Visit Perito Moreno Glacier", "Boat ride through fjords", "Wildlife watching", "Climb Mount Fitz Roy"]],
      [11, "Monaco", "Luxury casinos, glamorous hotels, and a stunning yacht-filled marina.", "Luxury Travel", 
     ["Visit the Casino de Monte-Carlo", "Take a yacht tour", "Stroll the Boulevard des Moulins", "Visit the Prince's Palace", "Explore the Monaco Grand Prix race track"]],
      [12, "Dubai, UAE", "World-class shopping, fine dining, luxury hotels, and modern architecture like the Burj Khalifa.", "Luxury Travel", 
     ["Climb the Burj Khalifa", "Shop at the Dubai Mall", "Explore the Palm Jumeirah", "Visit the Dubai Opera", "Go on a desert safari", "Relax on Jumeirah Beach"]],
      [13, "St. Barts, Caribbean", "Exclusive beaches, private villas, and luxury shopping.", "Luxury Travel", 
     ["Relax on the exclusive beaches", "Stay in luxury villas", "Shop at high-end boutiques", "Private yacht rental", "Snorkel and dive in crystal-clear waters"]],
      [14, "Bora Bora, French Polynesia", "High-end resorts and secluded beaches perfect for relaxation.", "Luxury Travel", 
     ["Stay in an overwater bungalow", "Explore Bora Bora Lagoon", "Visit Matira Beach", "Snorkel with rays and sharks", "Private dining on the beach"]],
      [15, "Maldives", "Pristine beaches, overwater bungalows, and luxurious resorts offering private villas.", "Luxury Travel", 
     ["Indulge in spa treatments", "Private boat cruise", "Snorkel or dive in coral reefs", "Sunbathe on a private beach", "Stay in luxurious water villas"]],
      [16, "Orlando, USA", "Home to Disney World, Universal Studios, and SeaWorld, offering fun for the whole family.", "Family-Friendly Travel", 
     ["Visit Disney World", "Explore Universal Studios", "Go to SeaWorld", "Check out LEGOLAND", "Visit Kennedy Space Center", "Experience the Wizarding World of Harry Potter"]],
      [17, "Gold Coast, Australia", "Theme parks like Dreamworld and Wet’n’Wild, plus beautiful beaches and wildlife parks.", "Family-Friendly Travel", 
     ["Visit Dreamworld", "Go to Wet’n’Wild", "Relax at Surfers Paradise Beach", "See koalas and kangaroos at wildlife parks", "Explore Currumbin Wildlife Sanctuary"]],
      [18, "Tokyo, Japan", "Kid-friendly attractions including Tokyo Disneyland, science museums, and kid-friendly restaurants.", "Family-Friendly Travel", 
     ["Visit Tokyo Disneyland", "Explore Ueno Zoo", "Check out teamLab Borderless Museum", "Visit Tokyo Skytree", "Enjoy robot shows in Odaiba", "Play in Tokyo Dome City"]],
      [19, "London, UK", "Natural history museums, zoos, Harry Potter studios, and family-oriented events.", "Family-Friendly Travel", 
     ["Visit the Natural History Museum", "Explore the Tower of London", "Check out the Harry Potter Studios", "Visit London Zoo", "Ride the London Eye"]],
      [20, "Copenhagen, Denmark", "Visit Tivoli Gardens, family-friendly museums, and the Little Mermaid statue.", "Family-Friendly Travel", 
     ["Visit Tivoli Gardens", "Explore the National Museum", "Check out the Little Mermaid statue", "Go to Copenhagen Zoo", "Visit Frederiksborg Castle"]],
      [21, "Athens, Greece", "The Acropolis, Parthenon, ancient ruins, and Greek museums.", "Cultural & Historical Travel", 
     ["Visit the Acropolis", "Explore the Parthenon", "See the Temple of Olympian Zeus", "Visit the National Archaeological Museum", "Stroll through Plaka"]],
      [22, "Rome, Italy", "Explore the Colosseum, Vatican City, Roman Forum, and ancient temples.", "Cultural & Historical Travel", 
     ["Tour the Colosseum", "Visit Vatican City and St. Peter's Basilica", "Explore Roman Forum", "See the Pantheon", "Walk through Piazza Navona"]],
      [23, "Cairo, Egypt", "The Great Pyramids of Giza, the Sphinx, and the Egyptian Museum.", "Cultural & Historical Travel", 
     ["Visit the Pyramids of Giza", "Explore the Egyptian Museum", "See the Sphinx", "Take a cruise on the Nile", "Shop in Khan el-Khalili Bazaar"]],
      [24, "Jerusalem, Israel", "Sacred sites like the Western Wall, the Dome of the Rock, and the Church of the Holy Sepulchre.", "Cultural & Historical Travel", 
     ["Visit the Western Wall", "Explore the Dome of the Rock", "See the Church of the Holy Sepulchre", "Tour the Old City", "Walk along the Via Dolorosa"]],
      [25, "Machu Picchu, Peru", "Ancient Incan ruins set high in the Andes, an incredible historical and spiritual site.", "Cultural & Historical Travel", 
     ["Hike the Inca Trail", "Explore the ruins of Machu Picchu", "Visit the Sacred Valley", "Climb Huayna Picchu", "Take a train ride through the Andes"]],
      [26, "Maldives", "Turquoise waters, coral reefs, and luxury resorts, ideal for relaxation and water sports.", "Beach & Relaxation", 
     ["Snorkel in coral reefs", "Relax on private beaches", "Go scuba diving", "Enjoy spa treatments", "Take sunset boat cruises", "Kayak and paddleboard"]],
      [27, "Phuket, Thailand", "Beautiful beaches, clear waters, and a laid-back atmosphere with plenty of water activities.", "Beach & Relaxation", 
     ["Relax on Patong Beach", "Snorkel at Phi Phi Islands", "Explore Old Phuket Town", "Take a boat tour to Phang Nga Bay", "Visit Big Buddha", "Enjoy a Thai massage"]],
      [28, "Seychelles", "Pristine beaches, unique granite rocks, crystal-clear waters, and a peaceful atmosphere.", "Beach & Relaxation", 
     ["Relax on Anse Source d'Argent", "Snorkel at Sainte Anne Marine National Park", "Visit the Vallée de Mai", "Explore Curieuse Island", "Hike in Morne Seychellois National Park"]],
      [29, "Hawaii, USA", "Tropical paradise with beaches, volcanoes, and laid-back resorts.", "Beach & Relaxation", 
     ["Relax on Waikiki Beach", "Visit Pearl Harbor", "Snorkel in Hanauma Bay", "Hike to Diamond Head", "Visit Volcanoes National Park", "Explore the Na Pali Coast"]],
      [30, "Barbados", "White sand beaches, clear blue water, and a relaxing Caribbean vibe.", "Beach & Relaxation", 
     ["Relax on Crane Beach", "Go snorkeling in Carlisle Bay", "Take a catamaran cruise", "Explore Harrison’s Cave", "Enjoy water sports at Accra Beach"]],
      ]
    fw.writerow(l)
    fd.close()

    
    f2=open('indiand.csv','w', newline='')
    fw=csv.writer(f2)
    #l=[index, place, description, category, [plans], kms]
    l=[[1, "Agra, Uttar Pradesh", "Famous for the Taj Mahal, Agra Fort, and Fatehpur Sikri, showcasing Mughal architecture.", "Cultural & Heritage", 
     ["Visit the Taj Mahal", "Explore Agra Fort", "Tour Fatehpur Sikri", "Stroll through Mehtab Bagh"], 
     "2,450 km"],
      [2, "Jaipur, Rajasthan", "Known as the Pink City, with landmarks like Amber Fort, Hawa Mahal, and City Palace.", "Cultural & Heritage", 
     ["Visit Amber Fort", "Explore Hawa Mahal", "Tour City Palace", "Stroll through Jal Mahal", "Shop in Johari Bazaar"], 
     "2,600 km"],
      [3, "Varanasi, Uttar Pradesh", "One of the oldest cities in the world, famous for its ghats on the Ganges and spiritual rituals.", "Cultural & Heritage", 
     ["Take a boat ride on the Ganges", "Attend Ganga Aarti", "Visit Kashi Vishwanath Temple", "Explore Sarnath"], 
     "2,450 km"],
      [4, "Khajuraho, Madhya Pradesh", "Famous for ancient temples with intricate carvings, representing India’s rich architecture and artistry.", "Cultural & Heritage", 
     ["Visit the Western Group of Temples", "Explore Kandariya Mahadev Temple", "Admire the erotic sculptures", "Attend the Khajuraho Dance Festival"], 
     "2,430 km"],
      [5, "Mysore, Karnataka", "Known for the grand Mysore Palace, Chamundi Hill, and the famous Mysore Dasara festival.", "Cultural & Heritage", 
     ["Visit Mysore Palace", "Climb Chamundi Hill", "Attend the Mysore Dasara festival", "Explore St. Philomena’s Church"], 
     "350 km"],
      [6, "Madurai, Tamil Nadu", "Home to the stunning Meenakshi Temple, an important pilgrimage site.", "Cultural & Heritage", 
     ["Visit Meenakshi Temple", "Explore Thirumalai Nayak Palace", "Shop in Puthu Mandapam", "Attend the Meenakshi Tirukalyanam festival"], 
     "375 km"],
      [7, "Kerala (Backwaters)", "Serene houseboat cruises through the tranquil backwaters, surrounded by lush landscapes.", "Nature & Scenic", 
     ["Take a houseboat cruise", "Explore Vembanad Lake", "Visit Kumarakom Bird Sanctuary", "Relax in Alappuzha"], 
     "40 km"],
      [8, "Kashmir", "Known as ‘Paradise on Earth’ with Dal Lake, Gulmarg for skiing, and Pahalgam for scenic beauty.", "Nature & Scenic", 
     ["Take a shikara ride on Dal Lake", "Ski in Gulmarg", "Explore Pahalgam", "Visit Mughal Gardens", "Trek to Sonamarg"], 
     "3,150 km"],
      [9, "Coorg, Karnataka", "A hill station known for its coffee plantations, misty landscapes, and pleasant climate.", "Nature & Scenic", 
     ["Visit the coffee plantations", "Trek to Abbey Falls", "Explore Dubare Elephant Camp", "Visit Talakaveri", "Go birdwatching at Nagarhole National Park"], 
     "220 km"],
      [10, "Leh-Ladakh, Jammu & Kashmir", "A high-altitude desert region with stunning landscapes, Pangong Lake, and Nubra Valley.", "Nature & Scenic", 
     ["Visit Pangong Lake", "Explore Nubra Valley", "Trek to Stok Kangri", "Visit Leh Palace", "Tour Hemis Monastery"], 
     "3,600 km"],
      [11, "Munnar, Kerala", "Known for its tea gardens, misty landscapes, and wildlife sanctuaries.", "Nature & Scenic", 
     ["Visit tea plantations", "Trek to Anamudi Peak", "Explore Eravikulam National Park", "Visit Mattupetty Dam", "Relax in the Attukal Waterfalls"], 
     "130 km"],
      [12, "Manali, Himachal Pradesh", "Popular for adventure sports like paragliding and trekking, with scenic views and the Solang Valley.", "Adventure & Trekking", 
     ["Paragliding in Solang Valley", "Trekking to Rohtang Pass", "Rafting in Beas River", "Visit Hidimba Temple", "Explore Old Manali"], 
     "3,050 km"],
      [13, "Rishikesh, Uttarakhand", "Famous for white-water rafting, trekking, yoga retreats, and spiritual significance.", "Adventure & Trekking", 
     ["Go white-water rafting", "Visit Triveni Ghat", "Trek to Neelkanth Mahadev Temple", "Attend yoga retreats", "Explore Rajaji National Park"], 
     "2,600 km"],
      [14, "Nainital, Uttarakhand", "Known for its beautiful lakes and trekking opportunities, including Naina Devi Temple and Tiffin Top.", "Adventure & Trekking", 
     ["Boating in Naini Lake", "Trek to Tiffin Top", "Visit Naina Devi Temple", "Explore Snow View Point", "Visit the Eco Cave Gardens"], 
     "2,800 km"],
      [15, "Spiti Valley, Himachal Pradesh", "A remote and rugged destination, known for trekking, monasteries, and stark landscapes.", "Adventure & Trekking", 
     ["Trek to Chandratal Lake", "Visit Key Monastery", "Explore Tabo Monastery", "See the Kibber village", "Drive to the Spiti River"], 
     "3,000 km"],
      [16, "Tawang, Arunachal Pradesh", "A scenic hill station known for trekking and Buddhist monasteries.", "Adventure & Trekking", 
     ["Trek to Bumla Pass", "Visit Tawang Monastery", "Explore Madhuri Lake", "See Sela Pass", "Tour the Tawang War Memorial"], 
     "3,450 km"],
      [17, "Goa", "Famous for its beaches, vibrant nightlife, and Portuguese heritage.", "Beach Destinations", 
     ["Relax on Anjuna Beach", "Explore Old Goa", "Party in Baga Beach", "Visit Basilica of Bom Jesus", "Shop at the Anjuna Flea Market"], 
     "530 km"],
      [18, "Andaman and Nicobar Islands", "Known for its pristine beaches, clear waters, and water sports, especially around Havelock Island.", "Beach Destinations", 
     ["Relax on Radhanagar Beach", "Snorkel around Havelock Island", "Take a boat ride to Neil Island", "Visit Cellular Jail", "Explore Mahatma Gandhi Marine National Park"], 
     "2,750 km"],
      [19, "Kochi, Kerala", "Known for its beaches, backwaters, Chinese Fishing Nets, and the cultural Fort Kochi area.", "Beach Destinations", 
     ["Explore Fort Kochi", "Visit the Chinese Fishing Nets", "Relax on Cherai Beach", "Take a backwater tour", "See the Paradesi Synagogue"], 
     "60 km"],
      [20, "Pondicherry", "A blend of French colonial architecture and beautiful beaches, offering a relaxed vibe.", "Beach Destinations", 
     ["Stroll through the French Quarter", "Relax at Promenade Beach", "Visit Sri Aurobindo Ashram", "Explore Auroville", "Shop at the local boutiques"], 
     "570 km"],
      [21, "Gokarna, Karnataka", "A quieter alternative to Goa with serene beaches like Om Beach and Kudle Beach.", "Beach Destinations", 
     ["Relax on Om Beach", "Visit Kudle Beach", "Explore Gokarna Temple", "Go trekking to Mirjan Fort", "Visit Half Moon Beach"], 
     "530 km"],
      [22, "Tirupati, Andhra Pradesh", "One of the holiest pilgrimage sites in India, home to the famous Tirumala Venkateswara Temple.", "Spiritual Destinations", 
     ["Visit Tirumala Venkateswara Temple", "Explore Sri Padmavathi Ammavari Temple", "Climb the Tirumala Hills", "See the Akasaganga Waterfalls"], 
     "830 km"],
      [23, "Haridwar, Uttarakhand", "A spiritual hub on the banks of the Ganges, famous for the Ganga Aarti and holy temples.", "Spiritual Destinations", 
     ["Attend Ganga Aarti at Har Ki Pauri", "Visit Mansa Devi Temple", "Take a holy dip in the Ganges", "Explore Chandi Devi Temple"], 
     "2,580 km"],
      [24, "Rishikesh, Uttarakhand", "Known for its spiritual significance, yoga retreats, and adventure activities like rafting.", "Spiritual Destinations", 
     ["Yoga retreat at Parmarth Niketan", "White-water rafting in the Ganges", "Visit the Beatles Ashram", "Explore the Triveni Ghat"], 
     "2,600 km"],

    [25, "Ramanagaram, Karnataka", "Famous for its trekking trails and natural rock formations, often referred to as the ‘Ramgarh’ of Bollywood.", "Wildlife & National Parks", 
     ["Trek to the top of Ramadevara Betta", "Spot wildlife in Ramanagaram Forest", "Explore Giri Ganga", "Visit the Bilikal Rangaswamy Betta"], 
     "270 km"],
      [26, "Sariska National Park, Rajasthan", "A famous tiger reserve and sanctuary, known for its wildlife safaris.", "Wildlife & National Parks", 
     ["Go on a wildlife safari", "Spot Bengal tigers", "Visit the Sariska Palace", "Explore the Kankwari Fort"], 
     "2,600 km"],

    [27, "Kanha National Park, Madhya Pradesh", "One of India’s largest and most famous national parks, home to the royal Bengal tiger.", "Wildlife & National Parks", 
     ["Go on a jeep safari", "Spot tigers and other wildlife", "Visit the Kanha Museum", "Explore the Kisli and Mukki zones"], 
     "2,300 km"],

    [28, "Kaziranga National Park, Assam", "A UNESCO World Heritage Site, known for the endangered one-horned rhinoceros.", "Wildlife & National Parks", 
     ["Go on a safari", "Spot one-horned rhinoceros", "Visit the Kaziranga National Park Museum", "Go birdwatching at the park"], 
     "3,450 km"],

    [29, "Jim Corbett National Park, Uttarakhand", "India’s first national park, known for its tigers and wildlife safaris.", "Wildlife & National Parks", 
     ["Go on a jeep safari", "Spot tigers and leopards", "Visit the Corbett Museum", "Explore the Garjia Temple"], 
     "2,700 km"],

    [30, "Sundarbans, West Bengal", "Known for the largest mangrove forest and the royal Bengal tiger.", "Wildlife & National Parks", 
     ["Take a boat safari", "Spot tigers and crocodiles", "Explore the Sundarbans Tiger Reserve", "Visit the Sajnekhali Wildlife Sanctuary"], 
     "2,500 km"],

    [31, "Shimla, Himachal Pradesh", "A popular hill station with colonial architecture and scenic views.", "Romantic Destinations", 
     ["Stroll along Mall Road", "Visit the Ridge", "Explore Kufri", "Take a toy train ride to Kalka"], 
     "3,000 km"],

    [32, "Udaipur, Rajasthan", "Known for its lakes, palaces, and romantic ambiance, often called the 'Venice of the East'.", "Romantic Destinations", 
     ["Take a boat ride on Lake Pichola", "Visit the City Palace", "Explore Jag Mandir", "Visit Saheliyon ki Bari"], 
     "2,700 km"],

    [33, "Darjeeling, West Bengal", "A hill station famous for its tea gardens, the toy train, and views of Kanchenjunga.", "Romantic Destinations", 
     ["Ride the Darjeeling Himalayan Railway", "Visit Tiger Hill for sunrise", "Explore the Peace Pagoda", "Visit Batasia Loop"], 
     "2,900 km"],

    [34, "Kumarakom, Kerala", "Known for its backwaters, luxury resorts, and bird sanctuary.", "Romantic Destinations", 
     ["Relax in a houseboat", "Visit the Kumarakom Bird Sanctuary", "Go on a nature walk", "Explore Vembanad Lake"], 
     "40 km"],

    [35, "Taj Falaknuma Palace, Hyderabad", "An opulent palace offering a luxurious stay with a royal ambiance.", "Luxury & Heritage Stays", 
     ["Stay in the palace", "Dine at the luxurious Jade Room", "Explore the stunning interiors", "Relax in the palace gardens"], 
     "1,800 km"],

    [36, "Rambagh Palace, Jaipur", "A former royal residence, now a luxury hotel with rich heritage.", "Luxury & Heritage Stays", 
     ["Stay in the heritage rooms", "Relax by the pool", "Explore the palace gardens", "Indulge in royal cuisine"], 
     "2,600 km"],

    [37, "Oberoi Rajvilas, Jaipur", "A luxurious hotel with exquisite architecture, ideal for a royal experience.", "Luxury & Heritage Stays", 
     ["Stay in luxury tents", "Relax by the pool", "Dine at the Surya Mahal", "Explore the Jaipur city"], 
     "2,600 km"],

    [38, "The Leela Palace, Udaipur", "A lakeside palace offering panoramic views and luxurious services.", "Luxury & Heritage Stays", 
     ["Stay by Lake Pichola", "Relax at the spa", "Dine at the hotel’s signature restaurant", "Take a boat ride around the lake"], 
     "2,700 km"],

    [39, "Umaid Bhawan Palace, Jodhpur", "A royal palace offering an opulent stay, known for its grandeur and luxurious amenities.", "Luxury & Heritage Stays", 
     ["Stay in royal rooms", "Explore the museum", "Relax at the spa", "Enjoy the palatial gardens"], 
     "2,800 km"],

    [40, "Tirthan Valley, Himachal Pradesh", "An offbeat destination known for its rivers, scenic beauty, and adventure activities.", "Offbeat & Hidden Gems", 
     ["Trek to the Great Himalayan National Park", "Go river rafting", "Visit the Tirthan River", "Explore the surrounding villages"], 
     "3,050 km"]]
    fw.writerow(l)
    f2.close()

    f3=open('fest.csv','w',newline='')
    fw=csv.writer(f3)
    #l=[index, fest, place, description, month]
    l=[[1, "Carnival", "Rio de Janeiro, Brazil", "A vibrant and colorful festival featuring parades, samba music, and extravagant costumes, considered the biggest carnival in the world.", "February or March"],
    [2, "Oktoberfest", "Munich, Germany", "A world-famous beer festival with traditional Bavarian music, food, and, of course, a variety of beers.", "Late September to the first weekend of October"],
    [3, "Diwali", "New Delhi, India", "Known as the Festival of Lights, it celebrates the triumph of light over darkness with fireworks, sweets, and family gatherings.", "October or November (based on the lunar calendar)"],
    [4, "Mardi Gras", "New Orleans, USA", "A lively festival known for its parades, masquerade balls, and colorful beads, celebrated before the start of Lent.", "February or March (before Lent)"],
    [5, "Festival Fringe", "Edinburgh, Scotland", "The world’s largest arts festival, showcasing theatre, comedy, music, and dance performances in various venues across the city.", "August"],
    [6, "La Tomatina", "Buñol, Spain", "A fun and messy event where thousands of people throw tomatoes at each other in a friendly food fight.", "Last Wednesday of August"],
    [7, "Chinese New Year", "Beijing, China", "The celebration of the lunar new year with dragon dances, fireworks, family reunions, and traditional Chinese foods.", "January or February (based on the lunar calendar)"],
    [8, "Holi", "Kathmandu, Nepal", "The Festival of Colors, where people throw colored powders at each other to celebrate the arrival of spring and the victory of good over evil.", "March (on the full moon day of Phalguna month)"],
    [9, "Running of the Bulls", "Pamplona, Spain", "An adrenaline-pumping event where participants run in front of a group of bulls through the streets of Pamplona, culminating in bullfights.", "July (7–14)"],
    [10, "Songkran", "Bangkok, Thailand", "Thailand’s New Year celebration featuring large-scale water fights in the streets, along with temple visits and family gatherings.", "April 13-15"],
    [11, "Venice Carnival", "Venice, Italy", "A historic festival known for its grand masquerade balls, elaborate costumes, and iconic Venetian masks.", "February (usually in the weeks leading up to Lent)"],
    [12, "Glastonbury Festival", "Glastonbury, UK", "A massive music festival featuring diverse performances from rock, pop, and electronic music artists, along with dance and theatre performances.", "Late June"],
    [13, "Day of the Dead", "Oaxaca, Mexico", "A cultural celebration honoring deceased loved ones with vibrant parades, altars, sugar skulls, and marigold decorations.", "October 31 – November 2"],
    [14, "Loi Krathong & Yi Peng Lantern Festival", "Chiang Mai, Thailand", "A stunning festival where people release floating lanterns (krathongs) into rivers and light up the night sky with sky lanterns (khom loi).", "November (on the full moon of the 12th lunar month)"],
    [15, "Burning Man Festival", "Black Rock Desert, USA", "A unique event focused on self-expression, art installations, and community in the remote desert, with participants building a temporary city.", "Late August to early September"],
    [16, "Cherry Blossom Festival", "Tokyo, Japan", "A celebration of the beautiful cherry blossoms in full bloom, marked by picnics under the trees and a festive atmosphere.", "March to May (depending on the region)"],
    [17, "Kwanzaa", "Chicago, USA", "A week-long celebration of African-American culture and heritage, marked by lighting candles in a kinara, music, and family activities.", "December 26 – January 1"],
    [18, "Up Helly Aa", "Lerwick, Shetland Islands, Scotland", "A Viking fire festival where participants dress as Vikings and parade through the streets, culminating in the burning of a Viking longship.", "Last Tuesday in January"],
    [19, "Fête de la Musique", "Global", "A global music festival celebrating free public music performances in cities around the world, encouraging amateur and professional musicians to perform in public spaces.", "June 21"]]
    fw.writerow(l)
    f3.close()

def displaycategindian():
    destination_categories = ["Cultural & Heritage","Nature & Scenic","Adventure & Trekking", "Beach Destinations","Spiritual Destinations","Wildlife & National Parks","Romantic Destinations","Luxury & Heritage Stays","Offbeat & Hidden Gems"]
    print('The categories of destination are as given below.')
    i=1
    for d in destination_categories:
        print(i, d)
        i=i+1
    c=int(input('Please enter the index to view the destinations'))
    if 0<c<10:
        i=1
        print()
        f2=open('indiand.csv', 'r', newline='')
        fr=csv.reader(f2)
        for base in fr:
            for loc in base:
                loc=ast.literal_eval(loc)
                
            
                if loc[3]==destination_categories[c-1]:
                    print(loc[0],'. ', loc[1], )
                    print(loc[2])
                    print('Distance from Anakkal, Kottayam:', loc[5])
                    print('Plans in ', loc[1],':')
                    for x in loc[4]:
                        print('  ->',x)
                    print('\n \n')
        ch=int(input('Enter the number before the place name to book the destination!'))
        f2.close()
        if ch in range(0,41):
            return ch
        else:
            print('Oops! wrong choice')
            return 0
    else:
        print('Sorry, wrong choice. try again, perhaps?')
        return 0

def displaycateginternational():
    destination_categories = ["Romantic Getaways","Adventure Travel","Luxury Travel","Family-Friendly Travel","Cultural & Historical Travel","Beach & Relaxation"]
    i=1
    for d in destination_categories:
        print(i, d)
        i=i+1
    c=int(input('Please enter the index to view the destinations'))
    if 0<c<7:
        i=1
        print()
        f1=open('internationd.csv', 'r', newline='')
        fr=csv.reader(f1)
        for row in fr:
            for loc in row:
                loc=ast.literal_eval(loc)
                if loc[3]==destination_categories[c-1]:
                    print(loc[0],'. ', loc[1], )
                    print(loc[2])
                    print('Plans in ', loc[1],':')
                    for x in loc[4]:
                        print('  ->',x)
        ch=int(input('Enter the number before the place name to book the destination!'))
        f1.close()
        if ch in range(0,31):
            return ch
        else:
            print('Oops! wrong choice')
            return 0
    else:
        print('Sorry, wrong choice. try again, perhaps?')
        return 0

def displayallindian():
    f2=open('indiand.csv','r', newline='')
    fr=csv.reader(f2)
    for row in fr:
            for loc in row:
                loc=ast.literal_eval(loc)
                print(loc[0],'. ', loc[1], )
                print(loc[2])
                print('Distance from Anakkal, Kottayam:', loc[5])
                print('Plans in ', loc[1],':')
                for x in loc[4]:
                    print('  ->',x)
    ch=int(input('Enter the number before the place name to book the destination!'))
    f2.close()
    if ch in range(0,41):
        return ch
    else:
        print('Oops! wrong choice')
        return 0

def displayallinternational():
    f2=open('internationd.csv','r', newline='')
    fr=csv.reader(f2)
    for row in fr:
            for loc in row:
                loc=ast.literal_eval(loc)
                print(loc[0],'. ', loc[1], )
                print(loc[2])
                print('Plans in ', loc[1],':')
                for x in loc[4]:
                    print('  ->',x)
    ch=int(input('Enter the number before the place name to book the destination!'))
    f2.close()
    if ch in range(0,31):
        return ch
    else:
        print('Oops! wrong choice')
        return 0

def displayfest():
    f3=open('fest.csv','r', newline='')
    fr=csv.reader(f3)
    for row in fr:
        for fest in row:
            fest=ast.literal_eval(fest)
            print(fest[0],'. ', fest[1])
            print('At ', fest[2])
            print('On ', fest[4])
            print('->', fest[3])
    ch=int(input('Enter the number before the place name to book the destination!'))
    f3.close()
    if ch in range(0,20):
        return ch
    else:
        print('Oops! wrong choice')
        return 0

def searchbymonth():
    month=input('Enter the month you want to search').upper()
    f3=open('fest.csv','r', newline='')
    fr=csv.reader(f3)
    f=0
    for row in fr:
        for fest in row:
            fest=ast.literal_eval(fest)
            if month in fest[4].upper():
                f=1
                print(fest[0],'. ', fest[1])
                print('At ', fest[2])
                print('On ', fest[4])
                print('->', fest[3])
        ch=int(input('Enter the number before the place name to book the destination!'))
    f3.close()
    if f==0:
        print('Sorry! No fests found in that month')
    if ch in range(0,20):
        return ch
    else:
        print('Oops! wrong choice')
        return 0

def display_brindian(booked_row):
    print(booked_row[0],'. ', booked_row[1], )
    print(booked_row[2])
    print('Distance from Anakkal, Kottayam:', booked_row[5])
    print('Plans in ', booked_row[1],':')
    for x in booked_row[4]:
        print('  ->',x)

def display_brinternational(br):
    print(br[0],'. ', br[1] )    
    print(br[2])
    print('Plans in ', br[1],':')
    for x in br[4]:
        print('  ->',x)

def display_brfest(br):
    print(br[0],'. ', br[1])
    print('At ', br[2])
    print('On ', br[4])
    print('->', br[3])

def confirm_plan(ch, domain):
    if domain==1:
        f1=open('indiand.csv','r', newline='')
        fr=csv.reader(f1)
        for row in fr:
            for loc in row:
                loc=ast.literal_eval(loc)
                if loc[0]== int(ch):
                    booked_row = loc
        display_brindian(booked_row)
        f1.close()
    elif domain==2:
        f1=open('internationd.csv','r', newline='')
        fr=csv.reader(f1)
        for row in fr:
            for loc in row:
                loc=ast.literal_eval(loc)
                if loc[0]== int(ch):
                    booked_row = loc
        f1.close()
        display_brinternational(booked_row)
    elif domain==3:
        f1=open('fest.csv','r', newline='')
        fr=csv.reader(f1)
        for row in fr:
            for loc in row:
                loc=ast.literal_eval(loc)
                if loc[0]== int(ch):
                    booked_row = loc
        f1.close()
        display_brfest(booked_row)
    confirmation=input('Please Enter Y to confirm your plan').upper()
    if confirmation=='Y':
        return 1
    else:
        return 0

def register(ch, domain, Ginfo):
    if domain==1:
        f1=open('indiand.csv','r', newline='')
        fr=csv.reader(f1)
        for row in fr:
            for loc in row:
                loc=ast.literal_eval(loc)
                if loc[0]== int(ch):
                    booked_row = loc
        
        f1.close()
    elif domain==2:
        f1=open('internationd.csv','r', newline='')
        fr=csv.reader(f1)
        for row in fr:
            for loc in row:
                loc=ast.literal_eval(loc)
                if loc[0]== int(ch):
                    booked_row = loc
        f1.close()

    elif domain==3:
        f1=open('fest.csv','r', newline='')
        fr=csv.reader(f1)
        for row in fr:
            for loc in row:
                loc=ast.literal_eval(loc)
                if loc[0]== int(ch):
                    booked_row = loc
        f1.close()
        #l=[gid, gname, cn, placeno, domain, place name]
        l=[Ginfo[0], Ginfo[1], Ginfo[2], domain, booked_row[0], booked_row[1]]
        f4=open('register.csv','w', newline='')
        fw=csv.writer(f4)
        fw.writerow(l)
        f4.close()

def consultation_billing(ch, domain, Ginfo):
    
    print('*************************************************************************************')
    print('                            CONSULTATION BILL                                   ')
    print('*************************************************************************************')
    print('USER\'S DETAILS:')
    displayg()
    print('THE BOOKED PLAN:')
    if domain==1:
        f1=open('indiand.csv','r', newline='')
        fr=csv.reader(f1)
        for row in fr:
            for loc in row:
                loc=ast.literal_eval(loc)
                if loc[0]== int(ch):
                    booked_row = loc
        display_brindian(booked_row)
        f1.close()
        cf=500
    elif domain==2:
        f1=open('internationd.csv','r', newline='')
        fr=csv.reader(f1)
        for row in fr:
            for loc in row:
                loc=ast.literal_eval(loc)
                if loc[0]== int(ch):
                    booked_row = loc
        f1.close()
        display_brinternational(booked_row)
        cf=1000
    elif domain==3:
        f1=open('fest.csv','r', newline='')
        fr=csv.reader(f1)
        for row in fr:
            for loc in row:
                loc=ast.literal_eval(loc)
                if loc[0]== int(ch):
                    booked_row = loc
        f1.close()
        display_brfest(booked_row)
        cf=1500
    print('\n CONSULTATION FEE= Rs.',cf)
    return cf
    

def choose_destination():
    setdestinations()
    print('*************************************************************************************')
    print('                          CHOOSE YOUR DESTINATION!                                         ')
    print('*************************************************************************************')
    domain=int(input('''WELCOME TO OUR TRAVEL SERVICES!
Please enter your choice of destination:
1) Within India
2) Foreign destinations
3) Festivals across the globe
4) Exit from booking portal'''))
    if domain==4:
        print('PROGRAM TERMINATING')
        print('THANK YOU!')
        sys.exit()
    if domain in [1,2]:
        tx=int(input('''How do you want to choose your destination?
1) Display by category
2) Display all'''))
        if tx not in [1,2]:
            print('Oops! wrong choice')
            choose_destination()
    elif domain==3:
        tx=int(input('''How do you want to choose your destination?
1) Search by month
2) Display all'''))
        if tx not in [1,2]:
            print('Oops! wrong choice')
            choose_destination()
    else:
        print('Oops! wrong choice')
        choose_destination()
    if domain==1 and tx==1:
        ch=displaycategindian()
    elif domain==1 and tx==2:
        ch=displayallindian()
    elif domain==2 and tx==1:
        ch=displaycateginternational()
    elif domain==2 and tx==2:
        ch=displayallinternational()
    elif domain==3 and tx==1:
        ch=searchbymonth()
    elif domain==3 and tx==2:
        ch= displayfest()
    
    if ch==0:
        tx=int(input('''Do you want to
1) Go back to choosing your destination?
2) Go back to main menu?
3) Exit?'''))
        if tx==1:
            choose_destination()
        elif tx==3:
            print('THANK YOU FOR USING OUR SERVICES! PROGRAM TERMINATING.')
            sys.exit()
    else:
        confirmation=confirm_plan(ch, domain)
        if confirmation==1:
            register(ch, domain, Ginfo)
            billc = consultation_billing(ch, domain, Ginfo)
            print('Your booking is confirmed! You will be redirected to our other services')
        else:
            print('Your booking is cancelled. REDIRECTING TO MAIN MENU')

user= welcome()
if user=='H':
    loginh()
    #while True:
    #hotel
elif user=='G':
    loging()
    while True:
        mc=mainmenug()
        if mc==1:
            displayg()
        elif mc==2:
            updateg()
        elif mc==3:
            choose_destination()
        elif mc==4:
            print('will be redirected to transport services')
            
            
            #hotel
        elif mc==5:
            print('will be redirected to transport services')
            #transport
        elif mc==6:
            print('PROGRAM TERMINATING')
            sys.exit()
        else:
            print('oops, wrong choice. try again')
