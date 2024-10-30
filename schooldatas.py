import random
from datetime import datetime

universities_courses_apply = {
    "University Of Greenwich": {
        "city": "Greenwich",
        "categories": {
            "Science": [
                "Master of Science - Engineering (By Research)",
            ],
            "Accounting": [
                "Master of Science - Engineering (By Research)",
            ]
        }
    },
    # Try loan
    "The University of Edinburgh": {
        "city": "Edinburgh",
        "categories": {
            "Science": [
                "Master of Science by Research - Infection and Immunity",
                "Master of Science by Research - Reproductive Sciences",
                "Master of Science - Natural Resources (By Research)",
                "Master of Science - Engineering (By Research)"
            ],
            "Health": [
                "Master of Science by Research - Nursing Studies",
                "Master of Science by Research - Infection and Immunity",
                "Master of Science by Research - Inflammation",
                "Master of Science by Research - Health Humanities and Arts",
            ],
            "Accounting": [
                "Master of Science by Research - Management",
                "Master of Science - Natural Resources (By Research)",
                "Master of Science - Engineering (By Research)",
            ],
            "Arts": [
                "Master of Science by Research - Philosophy",
                "Master of Science by Research - Human Geography",
                "Master of Science by Research - History of Art",
                "Master of Science by Research - History",
                "Master of Science by Research - English Language",
                "Master of Science by Research - English Literature",
                "Master of Science by Research - Linguistics",
                "Master of Science by Research - Infrastructure and the Environment",
                "Master of Science by Research - Counselling Studies",
                "Master of Science by Research - Architecture",
            ],
            "IT": [
                "Master of Science by Research - Informatics: ANC: Machine Learning, Computational Neuroscience, Computational Biology",
                "Master of Science by Research - Informatics: IPAB: Robotics, Computer Vision, Computer Graphics and Animation",
            ],
        }
    },
    "Swansea University": {
        "city": "Swansea",
        "categories": {
            "Science": [
                "Master of Science by Research - Psychology",
                "Master of Science by Research - Chemistry",
                "MSc by Research Computer Science",
                "Master of Science by Research - Experimental Physics",
                "Master of Science by Research - Theoretical Physics",
                "Master of Science by Research - Applied Physics and Materials",
                "Master of Science by Research - Sports Science",
            ],
            "Accounting": [
                "Master of Arts by Research - International Development",
                "Master of Science by Research - Urban Studies",
                "Master of Science by Research - Global Environmental Modelling",
                "MSc by Research Computer Science",
                "Master of Science by Research - Sports Science",
            ],
            "Arts": [
                "MA by Research Media Studies",
                "Master of Science by Research - Media Geographies",
                "Master of Science by Research - Social Theory and Space",
                "Master of Science by Research - Global Migration",
                "Master of Science by Research - Global Environmental Modelling",
                "Master of Arts by Research - English Literature",
                "Master of Science by Research - Earth Observation",
                "Master of Arts by Research - Applied Linguistics",
                "Master of Arts by Research - War and Society",
            ],
            "IT": [
                "MSc by Research Computer Science",
            ],
            "Health": [
                "Master of Science by Research - Health Economics",
                "Master of Science by Research - Social Policy",
                "Master of Science by Research - Sports Science",
            ]
        }
    },
    "University of Hertfordshire": {
        "city": "Hertfordshire",
        "categories": {
            "Science": [
                "Master by Research Sustainable Energy Technologies",
            ],
            "Law": [
                "Masters by Research Law",
            ],
        }
    },
    "University of Bradford": {
        "city": "Bradford",
        "categories": {
            "Science": [
                "Master by Research - Drug Development",    
            ],
        }
    },
    "Royal Holloway, University of London": {
        "city": "Egham",
        "categories": {
            "Science": [
                "Master of Science by Research - Physics",    
            ],
            "Arts": [
                "Master of Arts by Research - Film, Television and Digital Production",
                "Master of Arts by Research - Drama, Theatre and Dance",
                "Master of Arts by Research - Comparative Literature and Culture",
                "Master of Arts by Research - Classical Reception",
            ],
            "IT": [
                "Master of Science by Research - Computer Science",
            ]
        }
    },
    "Bangor University": {
        "city": "Bangor",
        "categories": {
            "Science": [
                "Master of Science by Research - Biological Sciences",    
            ],
            "Arts": [
                "Master of Arts by Research - Music",
                "Master of Music by Research - Music",
            ],
            "Health": [
                "Master of Science by Research - Ageing and Dementia Studies",
            ]
        }
    },
    "Nottingham Trent University - Clifton Campus": {
        "city": "Clifton",
        "categories": {
            "Arts": [
                "Master of Arts - Linguistics (by Research)",
                "Master of Arts - Philosophy (by Research)",
            ]
        }
    },
    "University of Reading": {
        "city": "Reading",
        "categories": {
            "Science": [
                "Master of Science by Research - Agriculture, Ecology and Environment",
                "Master of Science by Research - Biomedicine",
            ],
            "Accounting": [
                "Master of Science by Research - Entomology",
            ],
            "Arts": [
                "Master of Arts by Research - Typography and Graphic Communication",
                "Master of Arts by Research - Philosophy",
                "Master of Science by Research - Entomology",
            ],
        }
    },
    "University of Birmingham": {
        "city": "Edgbaston",
        "categories": {
            "Arts": [
                "Master of Arts - Music Performance Practice by Research",
            ],
        }
    },
    # No loan
    "University of Gloucestershire": {
        "city": "Oxstalls",
        "categories": {
            "Accounting": [
                "Master of Science by Research - International Business",
            ],
            "Health": [
                "Master of Science by Research - Health and Social Care",
            ],
            "IT": [
                "Master of Science by Research - Game Technologies",
            ],
            "Arts": [
                "Master of Arts by Research - Performing Art and Production",
            ]
        }
    },
    "Abertay University": {
        "city": "Abertay",
        "categories": {
            "Accounting": [
                "Master of Science by Research - Business and Management",
                "Master of Science by Research - Marketing",
                "Master of Science by Research - Accounting and Finance (OGAF)",
            ],
            "Health": [
                "Master of Science by Research - Food & Drink Science & Technology",
            ],
            "IT": [
                "Master of Science by Research - Computing",
                "Master of Science by Research - Game Design",
                "Master of Science by Research - Game Art and Animation",
                "Master of Science by Research - Game Technologies",
                "Master of Science by Research - Data Science and Systems Modelling",
            ],
            "Arts": [
                "Master of Arts by Research - Performing Art and Production",
            ],
            "Science": [
                "Master of Science by Research - Microorganisms and Antimicrobial Resistance in the Environment",
            ]
        }
    },
}

universities_courses_kc = {
    "University Of Glasgow": {
        "city": "Glasgow",
        "categories": {
            "Science": [
                "MRes Global Health",
            ],
            "Health": [
                "MRes Global Health",
            ],
            "Arts": [
                "MRes Global Health",
            ],
            "Accounting": [
                "MRes Global Health",
            ],
            "IT": [
                "MRes Global Health",
            ],
        }
    },
    "Aberystwyth University": {
        "city": "Aberystwyth",
        "categories": {
            "Science": [
                "MRes Biosciences",
            ],
            "Health": [
                "MRes Biosciences",
            ],
            "Arts": [
                "MRes Animal Science",
            ],
            "Accounting": [
                "MRes Parasite Control",
            ],
        }
    },
    "University of Dundee": {
        "city": "Dundee",
        "categories": {
            "Accounting": [
                "MRes Business Research Methods",
            ]
        }
    },
    "Queen Mary University of London": {
        "city": "London",
        "categories": {
            "Accounting": [
                "MRes Work and Organisation",
                "MRes Finance",
                "MRes Economics",
            ],
            "Science": [
                "MRes Work and Organisation",
                "Mres global public health policy",
            ],
            "Arts": [
                "MRes Work and Organisation",
                "Mres international relations",
                "Mres Human rights law ",
            ],
            "Health": [
                "Mres global public health policy",
                "MRes Work and Organisation",
            ],
            "Law": [
                "Mres Human rights law ",
                "MRes Work and Organisation",
            ]
            
        }
    },
    "University of Portsmouth": {
        "city": "Portsmouth",
        "categories": {
            "Science": [
                "MRes Science and Health",
            ],
            "Health": [
                "MRes Science and Health",
            ],
        }
    },
    "University of Exeter": {
        "city": "Exeter",
        "categories": {
            "Accounting": [
                "Mres Global Political Economy",
            ],
            "Science": [
                "Mres Global Political Economy",
                "Mres Advanced Biological Science",
            ],
            "Arts": [
                "Mres Global Political Economy",
            ],
            "Health": [
                "Mres Global Political Economy",
            ],
            "Law": [
                "Mres Global Political Economy",
                "Mres Socio Legal Research",
            ]        
        }
    },
}

universities_courses_edvoy = {
    "University of Central Lancashire": {
        "city": "Preston",
        "categories": {
            "Accounting": [
                "Mres Management"
            ],
            "Science": [
                "Mres Neuroscience"
            ],
            "Health": [
                "Mres Management"
            ],
        }
    },
    "University of Sussex": {
        "city": "Sussex",
        "categories": {
            "Science": [
                "MRes Advanced Artificial Intelligence"
            ],
            "IT": [
                "MRes Advanced Artificial Intelligence"
            ],
        }
    },
    "University of Birmingham": {
        "city": "Birmingham",
        "categories": {
            "Science": [
                "MRes Clinical Health Research",
            ],
            "Health": [
                "MRes Clinical Health Research",
            ],
        }
    },
    "University of Portsmouth": {
        "city": "Portsmouth",
        "categories": {
            "Science": [
                "MRes Science and Health",
            ],
            "Health": [
                "MRes Science and Health",
            ],
        }
    },
    "Bangor University": {
        "city": "Bangor",
        "categories": {
            "Science": [
                "Mres Electronic Engineering",
            ],
        }
    },
    "University of Brighton": {
        "city": "Brighton",
        "categories": {
            "Accounting": [
                "Mres Health Research",
            ],
            "Science": [
                "Mres Health Research",
            ],
            "Arts": [
                "Mres Health Research",
            ],
            "Health": [
                "Mres Health Research",
            ],
            "Law": [
                "Mres Health Research",
            ],
            "IT": [
                "Mres Health Research",
            ]
        }
    },
    "Sheffield Hallam University": {
        "city": "Sheffield",
        "categories": {
            "Science": [
                "Mres Cancer Biology",
            ],
        }
    },
    "Newcastle University": {
        "city": "Newcastle",
        "categories": {
            "Science": [
                "Mres Epidemiology",
            ],
        }
    },
    "University Of Derby": {
        "city": "Derby",
        "categories": {
            "Science": [
                "MRes Psychology",
                "MRes Leadership and Management",
            ],
            "Accounting": [
                "MRes Leadership and Management",
            ],
            "Arts": [
                "MRes Psychology",
                "MRes Leadership and Management",
            ],
            "IT": [
                "MRes Leadership and Management",
            ],
        }
    },
    "University Of Greenwich": {
        "city": "Greenwich",
        "categories": {
            "Science": [
                "MSc by Research Science",
                "Master of Science - Natural Resources (By Research)",
                "Master of Science - Engineering (By Research)"
            ],
            "Accounting": [
                "MSc by Research Science",
                "Master of Science - Natural Resources (By Research)",
                "Master of Science - Engineering (By Research)",
            ],
            "Arts": [
                "MSc by Research Science",
                "Master of Science - Natural Resources (By Research)",
                "Master of Science - Engineering (By Research)",
            ],
            "IT": [
                "MSc by Research Science",
                "Master of Science - Natural Resources (By Research)",
                "Master of Science - Engineering (By Research)",
            ],
        }
    },
    "University of Salford": {
        "city": "Salford",
        "categories": {
            "Science": [
                "MSc by Research in Psychology",
            ],
            "Accounting": [
                "MSc by Research in Psychology",
            ],
            "Arts": [
                "MSc by Research in Psychology",
            ],
            "IT": [
                "MSc by Research in Psychology",
            ],
        }
    },
    # No loan
    "University of Bolton": {
        "city": "Bolton",
        "categories": {
            "Science": [
                "MRes Computing",
                "MRes Environmental Management"
            ],
            "Health": [
                "MRes Strategy and Leadership",
            ],
            "IT": [
                "MRes Computing",
                "MRes Artificial Intelligence"
            ],
            "Accounting": [
                "MRes Logistics and Supply Chain Management",
            ],
            "Arts": [
                "MRes Educational Leadership",
            ],
        }
    },
    "Bournemouth University": {
        "city": "Lansdowne",
        "categories": {
            "Science": [
                "Master of Research - Health and Social Sciences",
            ],
            "Health": [
                "Master of Research - Health and Social Sciences",
            ],
            "IT": [
                "Master of Research - Health and Social Sciences",
            ],
            "Accounting": [
                "Master of Research - Health and Social Sciences",
            ],
        }
    },
}

def select_courses_by_category(category, platform):
    
    if platform == "ab":
        courses = universities_courses_apply
    elif platform == "ed":
        courses = universities_courses_edvoy
    else:
        courses = universities_courses_kc
    
    """
    Selects one random course per UK university based on the input category.

    :param category: The category of courses to select (e.g., 'Accounting', 'Science', 'Health', 'IT').
    :return: A list of one random course per university that matches the category.
    """
    selected_courses = []

    for university, details in courses.items():
        city = details["city"]
        categories = details["categories"]
        
        if category in categories and categories[category]:
            # Randomly select a course from the category
            course = random.choice(categories[category])
            selected_courses.append({
                "university": university,
                "city": city,
                "course": course
            })

    return selected_courses

def get_previous_uni(uni):
    universities_info = {
    "ug": {
        "school_name": "University of Ghana",
        "telephone": "+233 302 500381",
        "email": "admissions@ug.edu.gh",
        "website": "ug.edu.gh",
        "location": "Legon, Accra",
        "certificate_issuing_university": "University of Ghana",
        "color1": "#002147",  # Navy Blue
        "color2": "#FFCC00",  # Gold
        "logo": "ug_logo.png",
        "logowithname": "ug_logowithname.png"
    },
    "knust": {
        "school_name": "Kwame Nkrumah University of Science and Technology",
        "telephone": "+233 3220 60021",
        "email": "info@knust.edu.gh",
        "website": "knust.edu.gh",
        "location": "Kumasi",
        "certificate_issuing_university": "Kwame Nkrumah University of Science and Technology",
        "color1": "#006400",  # Dark Green
        "color2": "#FFD700",  # Gold
        "logo": "knust_logo.png",
        "logowithname": "knust_logowithname.png"
    },
    "ucc": {
        "school_name": "University of Cape Coast",
        "telephone": "+233 3321 32480",
        "email": "info@ucc.edu.gh",
        "website": "ucc.edu.gh",
        "location": "Cape Coast",
        "certificate_issuing_university": "University of Cape Coast",
        "color1": "#003366",  # Navy Blue
        "color2": "#FFD700",  # Gold
        "logo": "ucc_logo.png",
        "logowithname": "ucc_logowithname.png"
    },
    "uew": {
        "school_name": "University of Education, Winneba",
        "telephone": "+233 303 965012",
        "email": "info@uew.edu.gh",
        "website": "uew.edu.gh",
        "location": "Winneba",
        "certificate_issuing_university": "University of Education, Winneba",
        "color1": "#003366",  # Navy Blue
        "color2": "#FFCC00",  # Gold
        "logo": "uew_logo.png",
        "logowithname": "uew_logowithname.png"
    },
    "ashesi": {
        "school_name": "Ashesi University",
        "telephone": "+233 302 610 330",
        "email": "info@ashesi.edu.gh",
        "website": "ashesi.edu.gh",
        "location": "Berekuso, Eastern Region",
        "certificate_issuing_university": "Ashesi University",
        "color1": "#8B0000",  # Dark Red
        "color2": "#FFD700",  # Gold
        "logo": "ashesi_logo.png",
        "logowithname": "ashesi_logowithname.png"
    },
    "central": {
        "school_name": "Central University",
        "telephone": "+233 303 318 580",
        "email": "info@central.edu.gh",
        "website": "central.edu.gh",
        "location": "Miotso, Greater Accra",
        "certificate_issuing_university": "Central University",
        "color1": "red",  # Dark Blue
        "color2": "red",  # Gold
        "logo": "central_logo.png",
        "logowithname": "central_logowithname.png"
    },
    "valley_view": {
        "school_name": "Valley View University",
        "telephone": "+233 307 011 040",
        "email": "info@vvu.edu.gh",
        "website": "vvu.edu.gh",
        "location": "Oyibi, Greater Accra",
        "certificate_issuing_university": "Valley View University",
        "color1": "#00416A",  # Dark Blue
        "color2": "#FFD700",  # Gold
        "logo": "vvu_logo.png",
        "logowithname": "vvu_logowithname.png"
    },
    "presbyterian": {
        "school_name": "Presbyterian University College",
        "telephone": "+233 3420 92179",
        "email": "info@presbyuniversity.edu.gh",
        "website": "presbyuniversity.edu.gh",
        "location": "Abetifi, Eastern Region",
        "certificate_issuing_university": "Presbyterian University College",
        "color1": "#003366",  # Dark Blue
        "color2": "#FFD700",  # Gold
        "logo": "presbyterian_logo.png",
        "logowithname": "presbyterian_logowithname.png"
    },
    "pentecost": {
        "school_name": "Pentecost University",
        "telephone": "+233 302 417 057",
        "email": "info@pentvars.edu.gh",
        "website": "pentvars.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "Pentecost University",
        "color1": "#8A2BE2",  # Blue Violet
        "color2": "#FFD700",  # Gold
        "logo": "pentecost_logo.png",
        "logowithname": "pentecost_logowithname.png"
    },
    "methodist": {
        "school_name": "Methodist University College Ghana",
        "telephone": "+233 302 312 980",
        "email": "info@mucg.edu.gh",
        "website": "mucg.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "Methodist University College Ghana",
        "color1": "#800080",  # Purple
        "color2": "#FFD700",  # Gold
        "logo": "methodist_logo.png",
        "logowithname": "methodist_logowithname.png"
    },
    "baptist": {
        "school_name": "Ghana Baptist University College",
        "telephone": "+233 3220 22921",
        "email": "info@gbuc.edu.gh",
        "website": "gbuc.edu.gh",
        "location": "Kumasi",
        "certificate_issuing_university": "Ghana Baptist University College",
        "color1": "#2F4F4F",  # Dark Slate Gray
        "color2": "#FFD700",  # Gold
        "logo": "baptist_logo.png",
        "logowithname": "baptist_logowithname.png"
    },
    "csuc": {
        "school_name": "Christian Service University College",
        "telephone": "+233 3220 22575",
        "email": "info@csuc.edu.gh",
        "website": "csuc.edu.gh",
        "location": "Kumasi",
        "certificate_issuing_university": "Christian Service University College",
        "color1": "#556B2F",  # Dark Olive Green
        "color2": "#FFD700",  # Gold
        "logo": "csuc_logo.png",
        "logowithname": "csuc_logowithname.png"
    },
    "aucc": {
        "school_name": "African University College of Communications (AUCC)",
        "telephone": "+233 302 258 584",
        "email": "info@aucc.edu.gh",
        "website": "aucc.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "African University College of Communications",
        "color1": "#A52A2A",  # Brown
        "color2": "#FFD700",  # Gold
        "logo": "aucc_logo.png",
        "logowithname": "aucc_logowithname.png"
    },
    "wisconsin": {
        "school_name": "Wisconsin International University College",
        "telephone": "+233 302 504 391",
        "email": "info@wiuc-ghana.edu.gh",
        "website": "wiuc-ghana.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "Wisconsin International University College",
        "color1": "#4682B4",  # Steel Blue
        "color2": "#FFD700",  # Gold
        "logo": "wisconsin_logo.png",
        "logowithname": "wisconsin_logowithname.png"
    },
    "lancaster": {
        "school_name": "Lancaster University Ghana",
        "telephone": "+233 302 218 989",
        "email": "info@lancaster.edu.gh",
        "website": "lancaster.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "Lancaster University",
        "color1": "#B22222",  # Firebrick
        "color2": "#FFD700",  # Gold
        "logo": "lancaster_logo.png",
        "logowithname": "lancaster_logowithname.png"
    },
    "regent": {
        "school_name": "Regent University College of Science and Technology",
        "telephone": "+233 302 216 847",
        "email": "info@regent.edu.gh",
        "website": "regent.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "Regent University College of Science and Technology",
        "color1": "#800000",  # Maroon
        "color2": "#FFD700",  # Gold
        "logo": "regent_logo.png",
        "logowithname": "regent_logowithname.png"
    },
    "all_nations": {
        "school_name": "All Nations University",
        "telephone": "+233 3420 25622",
        "email": "info@anu.edu.gh",
        "website": "anu.edu.gh",
        "location": "Koforidua",
        "certificate_issuing_university": "All Nations University",
        "color1": "#000080",  # Navy
        "color2": "#FFD700",  # Gold
        "logo": "all_nations_logo.png",
        "logowithname": "all_nations_logowithname.png"
    },
    "catholic": {
        "school_name": "Catholic University College of Ghana",
        "telephone": "+233 3520 27087",
        "email": "info@cug.edu.gh",
        "website": "cug.edu.gh",
        "location": "Sunyani",
        "certificate_issuing_university": "Catholic University College of Ghana",
        "color1": "#4B0082",  # Indigo
        "color2": "#FFD700",  # Gold
        "logo": "catholic_logo.png",
        "logowithname": "catholic_logowithname.png"
    },
    "islamic": {
        "school_name": "Islamic University College",
        "telephone": "+233 302 913 404",
        "email": "info@iug.edu.gh",
        "website": "iug.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "Islamic University College",
        "color1": "#006400",  # Dark Green
        "color2": "#FFD700",  # Gold
        "logo": "islamic_logo.png",
        "logowithname": "islamic_logowithname.png"
    },
    "kings": {
        "school_name": "Kings University College",
        "telephone": "+233 302 960 059",
        "email": "info@kings.edu.gh",
        "website": "kings.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "Kings University College",
        "color1": "#8B0000",  # Dark Red
        "color2": "#FFD700",  # Gold
        "logo": "kings_logo.png",
        "logowithname": "kings_logowithname.png"
    },
    "zenith": {
        "school_name": "Zenith University College",
        "telephone": "+233 302 912 703",
        "email": "info@zenithuniversity.edu.gh",
        "website": "zenithuniversity.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "Zenith University College",
        "color1": "#2F4F4F",  # Dark Slate Gray
        "color2": "#FFD700",  # Gold
        "logo": "zenith_logo.png",
        "logowithname": "zenith_logowithname.png"
    },
    "knutsford": {
        "school_name": "Knutsford University College",
        "telephone": "+233 302 912 420",
        "email": "info@knutsford.edu.gh",
        "website": "knutsford.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "Knutsford University College",
        "color1": "#A52A2A",  # Brown
        "color2": "#FFD700",  # Gold
        "logo": "knutsford_logo.png",
        "logowithname": "knutsford_logowithname.png"
    },
    "dominion": {
        "school_name": "Dominion University College",
        "telephone": "+233 302 240 857",
        "email": "info@duc.edu.gh",
        "website": "duc.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "Dominion University College",
        "color1": "#008080",  # Teal
        "color2": "#FFD700",  # Gold
        "logo": "dominion_logo.png",
        "logowithname": "dominion_logowithname.png"
    },
    "bluecrest": {
        "school_name": "BlueCrest University College",
        "telephone": "+233 302 220 044",
        "email": "info@bluecrest.edu.gh",
        "website": "bluecrest.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "BlueCrest University College",
        "color1": "#4169E1",  # Royal Blue
        "color2": "#FFD700",  # Gold
        "logo": "bluecrest_logo.png",
        "logowithname": "bluecrest_logowithname.png"
    },
    "ghana_christian": {
        "school_name": "Ghana Christian University College",
        "telephone": "+233 302 937 207",
        "email": "info@gcuc.edu.gh",
        "website": "gcuc.edu.gh",
        "location": "Amrahia, Accra",
        "certificate_issuing_university": "Ghana Christian University College",
        "color1": "#006400",  # Dark Green
        "color2": "#FFD700",  # Gold
        "logo": "ghana_christian_logo.png",
        "logowithname": "ghana_christian_logowithname.png"
    },
    "anglican": {
        "school_name": "Anglican University College of Technology",
        "telephone": "+233 302 400 700",
        "email": "info@angutech.edu.gh",
        "website": "angutech.edu.gh",
        "location": "Nkoranza, Brong-Ahafo",
        "certificate_issuing_university": "Anglican University College of Technology",
        "color1": "#800080",  # Purple
        "color2": "#FFD700",  # Gold
        "logo": "anglican_logo.png",
        "logowithname": "anglican_logowithname.png"
    },
    "uds": {
        "school_name": "University for Development Studies",
        "telephone": "+233 3720 93382",
        "email": "info@uds.edu.gh",
        "website": "uds.edu.gh",
        "location": "Tamale",
        "certificate_issuing_university": "University for Development Studies",
        "color1": "#228B22",  # Forest Green
        "color2": "#FFD700",  # Gold
        "logo": "uds_logo.png",
        "logowithname": "uds_logowithname.png"
    },
    "umat": {
        "school_name": "University of Mines and Technology",
        "telephone": "+233 3123 20324",
        "email": "info@umat.edu.gh",
        "website": "umat.edu.gh",
        "location": "Tarkwa",
        "certificate_issuing_university": "University of Mines and Technology",
        "color1": "#8B4513",  # Saddle Brown
        "color2": "#FFD700",  # Gold
        "logo": "umat_logo.png",
        "logowithname": "umat_logowithname.png"
    },
    "uhas": {
        "school_name": "University of Health and Allied Sciences",
        "telephone": "+233 3620 28744",
        "email": "info@uhas.edu.gh",
        "website": "uhas.edu.gh",
        "location": "Ho",
        "certificate_issuing_university": "University of Health and Allied Sciences",
        "color1": "#008080",  # Teal
        "color2": "#FFD700",  # Gold
        "logo": "uhas_logo.png",
        "logowithname": "uhas_logowithname.png"
    },
    "uenr": {
        "school_name": "University of Energy and Natural Resources",
        "telephone": "+233 3520 23192",
        "email": "info@uenr.edu.gh",
        "website": "uenr.edu.gh",
        "location": "Sunyani",
        "certificate_issuing_university": "University of Energy and Natural Resources",
        "color1": "#006400",  # Dark Green
        "color2": "#FFCC00",  # Gold
        "logo": "uenr_logo.png",
        "logowithname": "uenr_logowithname.png"
    },
    "upsa": {
        "school_name": "University of Professional Studies, Accra",
        "telephone": "+233 302 500722",
        "email": "info@upsa.edu.gh",
        "website": "upsa.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "University of Professional Studies, Accra",
        "color1": "#000080",  # Navy Blue
        "color2": "#FFD700",  # Gold
        "logo": "upsa_logo.png",
        "logowithname": "upsa_logowithname.png"
    },
    "gimpa": {
        "school_name": "Ghana Institute of Management and Public Administration",
        "telephone": "+233 302 401681",
        "email": "info@gimpa.edu.gh",
        "website": "gimpa.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "Ghana Institute of Management and Public Administration",
        "color1": "#4B0082",  # Indigo
        "color2": "#FFD700",  # Gold
        "logo": "gimpa_logo.png",
        "logowithname": "gimpa_logowithname.png"
    },
    "uesd": {
        "school_name": "University of Environment and Sustainable Development",
        "telephone": "+233 302 906515",
        "email": "info@uesd.edu.gh",
        "website": "uesd.edu.gh",
        "location": "Somanya",
        "certificate_issuing_university": "University of Environment and Sustainable Development",
        "color1": "#008000",  # Green
        "color2": "#FFD700",  # Gold
        "logo": "uesd_logo.png",
        "logowithname": "uesd_logowithname.png"
    },
    "atu": {
        "school_name": "Accra Technical University",
        "telephone": "+233 302 221 644",
        "email": "info@atu.edu.gh",
        "website": "atu.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "Accra Technical University",
        "color1": "#00539C",  # Dark Blue
        "color2": "#FFD700",  # Gold
        "logo": "atu_logo.png",
        "logowithname": "atu_logowithname.png"
    },
    "ktu": {
        "school_name": "Kumasi Technical University",
        "telephone": "+233 3220 22387",
        "email": "info@kstu.edu.gh",
        "website": "kstu.edu.gh",
        "location": "Kumasi",
        "certificate_issuing_university": "Kumasi Technical University",
        "color1": "#00416A",  # Dark Blue
        "color2": "#FFD700",  # Gold
        "logo": "ktu_logo.png",
        "logowithname": "ktu_logowithname.png"
    },
    "ttu": {
        "school_name": "Takoradi Technical University",
        "telephone": "+233 3120 25096",
        "email": "info@ttu.edu.gh",
        "website": "ttu.edu.gh",
        "location": "Takoradi",
        "certificate_issuing_university": "Takoradi Technical University",
        "color1": "#006400",  # Dark Green
        "color2": "#FFD700",  # Gold
        "logo": "ttu_logo.png",
        "logowithname": "ttu_logowithname.png"
    },
    "cctu": {
        "school_name": "Cape Coast Technical University",
        "telephone": "+233 3321 22050",
        "email": "info@cctu.edu.gh",
        "website": "cctu.edu.gh",
        "location": "Cape Coast",
        "certificate_issuing_university": "Cape Coast Technical University",
        "color1": "#4B0082",  # Indigo
        "color2": "#FFD700",  # Gold
        "logo": "cctu_logo.png",
        "logowithname": "cctu_logowithname.png"
    },
    "tatu": {
        "school_name": "Tamale Technical University",
        "telephone": "+233 3720 22226",
        "email": "info@tatu.edu.gh",
        "website": "tatu.edu.gh",
        "location": "Tamale",
        "certificate_issuing_university": "Tamale Technical University",
        "color1": "#008080",  # Teal
        "color2": "#FFD700",  # Gold
        "logo": "tatu_logo.png",
        "logowithname": "tatu_logowithname.png"
    },
    "koforidua_tech": {
        "school_name": "Koforidua Technical University",
        "telephone": "+233 3420 25621",
        "email": "info@ktu.edu.gh",
        "website": "ktu.edu.gh",
        "location": "Koforidua",
        "certificate_issuing_university": "Koforidua Technical University",
        "color1": "#1E90FF",  # Dodger Blue
        "color2": "#FFD700",  # Gold
        "logo": "koforidua_tech_logo.png",
        "logowithname": "koforidua_tech_logowithname.png"
    },
    "stu": {
        "school_name": "Sunyani Technical University",
        "telephone": "+233 3520 27580",
        "email": "info@stu.edu.gh",
        "website": "stu.edu.gh",
        "location": "Sunyani",
        "certificate_issuing_university": "Sunyani Technical University",
        "color1": "#2F4F4F",  # Dark Slate Gray
        "color2": "#FFD700",  # Gold
        "logo": "stu_logo.png",
        "logowithname": "stu_logowithname.png"
    },
    "htu": {
        "school_name": "Ho Technical University",
        "telephone": "+233 3620 28222",
        "email": "info@htu.edu.gh",
        "website": "htu.edu.gh",
        "location": "Ho",
        "certificate_issuing_university": "Ho Technical University",
        "color1": "#006400",  # Dark Green
        "color2": "#FFD700",  # Gold
        "logo": "htu_logo.png",
        "logowithname": "htu_logowithname.png"
    },
    "btu": {
        "school_name": "Bolgatanga Technical University",
        "telephone": "+233 3820 22043",
        "email": "info@btu.edu.gh",
        "website": "btu.edu.gh",
        "location": "Bolgatanga",
        "certificate_issuing_university": "Bolgatanga Technical University",
        "color1": "#B22222",  # Firebrick
        "color2": "#FFD700",  # Gold
        "logo": "btu_logo.png",
        "logowithname": "btu_logowithname.png"
    },
    "wa_tech": {
        "school_name": "Wa Technical University",
        "telephone": "+233 3920 22053",
        "email": "info@watu.edu.gh",
        "website": "watu.edu.gh",
        "location": "Wa",
        "certificate_issuing_university": "Wa Technical University",
        "color1": "#000080",  # Navy Blue
        "color2": "#FFD700",  # Gold
        "logo": "wa_tech_logo.png",
        "logowithname": "wa_tech_logowithname.png"
    },
    "aamusted": {
        "school_name": "Akenten Appiah-Menka University of Skills Training and Entrepreneurial Development (AAMUSTED)",
        "telephone": "+233 3220 60205",
        "email": "info@aamusted.edu.gh",
        "website": "aamusted.edu.gh",
        "location": "Kumasi",
        "certificate_issuing_university": "Akenten Appiah-Menka University of Skills Training and Entrepreneurial Development",
        "color1": "#4B0082",  #Indigo
        "color2": "#FFD700",  #Gold
        "logo": "aamusted_logo.png",
        "logowithname": "aamusted_logowithname.png"
    },
    "ckt_utas": {
        "school_name": "C. K. Tedam University of Technology and Applied Science (CKT-UTAS)",
        "telephone": "+233 3820 92239",
        "email": "info@cktutas.edu.gh",
        "website": "cktutas.edu.gh",
        "location": "Navrongo, Upper East Region",
        "certificate_issuing_university": "C. K. Tedam University of Technology and Applied Science",
        "color1": "#228B22",  #Forest Green
        "color2": "#FFD700",  #Gold
        "logo": "ckt_utas_logo.png",
        "logowithname": "ckt_utas_logowithname.png"
    },
    "sdd_ubids": {
        "school_name": "Simon Diedong Dombo University of Business and Integrated Development Studies",
        "telephone": "+233 3920 22994",
        "email": "info@ubids.edu.gh",
        "website": "ubids.edu.gh",
        "location": "Wa, Upper West Region",
        "certificate_issuing_university": "Simon Diedong Dombo University of Business and Integrated Development Studies",
        "color1": "#2F4F4F",  #Dark Slate Gray
        "color2": "#FFD700",  #Gold
        "logo": "ubids_logo.png",
        "logowithname": "ubids_logowithname.png"
    },
    "regional_maritime": {
        "school_name": "Regional Maritime University",
        "telephone": "+233 303 200 092",
        "email": "info@rmu.edu.gh",
        "website": "rmu.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "Regional Maritime University",
        "color1": "#000080",  #Navy Blue
        "color2": "#FFD700",  #Gold
        "logo": "rmu_logo.png",
        "logowithname": "rmu_logowithname.png"
    },
    "gctu": {
        "school_name": "Ghana Communication Technology University",
        "telephone": "+233 302 200 612",
        "email": "info@gctu.edu.gh",
        "website": "gctu.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "Ghana Communication Technology University",
        "color1": "#2F4F4F",  #Dark Slate Gray
        "color2": "#FFD700",  #Gold
        "logo": "gctu_logo.png",
        "logowithname": "gctu_logowithname.png"
    },
    "unimac": {
        "school_name": "University of Media, Arts and Communication (UNIMAC)",
        "telephone": "+233 302 221 739",
        "email": "info@unimac.edu.gh",
        "website": "unimac.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "University of Media, Arts and Communication",
        "color1": "#8B0000",  #Dark Red
        "color2": "#FFD700",  #Gold
        "logo": "unimac_logo.png",
        "logowithname": "unimac_logowithname.png"
    },
    "kaaf": {
        "school_name": "KAAF University College",
        "telephone": "+233 208 148 166",
        "email": "info@kaafuni.edu.gh",
        "website": "kaafuni.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "KAAF University College",
        "color1": "#006400",  #Dark Green
        "color2": "#FFD700",  #Gold
        "logo": "kaaf_logo.png",
        "logowithname": "kaaf_logowithname.png"
    },
    "ait": {
        "school_name": "Accra Institute of Technology",
        "telephone": "+233 302 923 724",
        "email": "info@ait.edu.gh",
        "website": "ait.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "Accra Institute of Technology",
        "color1": "#4682B4",  #Steel Blue
        "color2": "#FFD700",  #Gold
        "logo": "ait_logo.png",
        "logowithname": "ait_logowithname.png"
    },
    "gcuc": {
        "school_name": "Garden City University College",
        "telephone": "+233 3220 90567",
        "email": "info@gcuc.edu.gh",
        "website": "gcuc.edu.gh",
        "location": "Kumasi",
        "certificate_issuing_university": "Garden City University College",
        "color1": "#6A5ACD",  #Slate Blue
        "color2": "#FFD700",  #Gold
        "logo": "gcuc_logo.png",
        "logowithname": "gcuc_logowithname.png"
    },
    "webster": {
        "school_name": "Webster University Ghana",
        "telephone": "+233 302 507 390",
        "email": "info@webster.edu.gh",
        "website": "webster.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "Webster University Ghana",
        "color1": "#1E90FF",  #Dodger Blue
        "color2": "#FFD700",  #Gold
        "logo": "webster_logo.png",
        "logowithname": "webster_logowithname.png"
    },
    "datalink": {
        "school_name": "Data Link University College",
        "telephone": "+233 303 311 244",
        "email": "info@datalink.edu.gh",
        "website": "datalink.edu.gh",
        "location": "Tema, Greater Accra",
        "certificate_issuing_university": "Data Link University College",
        "color1": "#708090",  #Slate Gray
        "color2": "#FFD700",  #Gold
        "logo": "datalink_logo.png",
        "logowithname": "datalink_logowithname.png"
    },
    "radford": {
        "school_name": "Radford University College",
        "telephone": "+233 302 520 531",
        "email": "info@radford.edu.gh",
        "website": "radford.edu.gh",
        "location": "Accra",
        "certificate_issuing_university": "Radford University College",
        "color1": "#B22222",  #Firebrick
        "color2": "#FFD700",  #Gold
        "logo": "radford_logo.png",
        "logowithname": "radford_logowithname.png"
    },
    "perez": {
        "school_name": "Perez University College",
        "telephone": "+233 302 518 525",
        "email": "info@perez.edu.gh",
        "website": "perez.edu.gh",
        "location": "Winneba, Central Region",
        "certificate_issuing_university": "Perez University College",
        "color1": "#FF4500",  #Orange Red
        "color2": "#FFD700",  #Gold
        "logo": "perez_logo.png",
        "logowithname": "perez_logowithname.png"
    },
    "mountcrest": {
        "school_name": "MountCrest University College",
        "telephone": "+233 302 221 318",
        "email": "info@mountcrest.edu.gh",
        "website": "mountcrest.edu.gh",
        "location": "Larteh, Eastern Region",
        "certificate_issuing_university": "MountCrest University College",
        "color1": "#483D8B",  #Dark Slate Blue
        "color2": "#FFD700",  #Gold
        "logo": "mountcrest_logo.png",
        "logowithname": "mountcrest_logowithname.png"
    },

    "kessben": {
        "school_name": "Kessben University College",
        "telephone": "+233 3220 93024",
        "email": "info@kessben.edu.gh",
        "website": "kessben.edu.gh",
        "location": "Kumasi, Ashanti Region",
        "certificate_issuing_university": "Kessben University College",
        "color1": "#8B4513",  #Saddle Brown
        "color2": "#FFD700",  #Gold
        "logo": "kessben_logo.png",
        "logowithname": "kessben_logowithname.png"
    },
    "christ_apostolic": {
        "school_name": "Christ Apostolic University College",
        "telephone": "+233 3220 94565",
        "email": "info@cauc.edu.gh",
        "website": "cauc.edu.gh",
        "location": "Kumasi, Ashanti Region",
        "certificate_issuing_university": "Christ Apostolic University College",
        "color1": "#A0522D",  #Sienna
        "color2": "#FFD700",  #Gold
        "logo": "cauc_logo.png",
        "logowithname": "cauc_logowithname.png"
    },
    "cibt": {
        "school_name": "Catholic Institute of Business and Technology",
        "telephone": "+233 302 200 315",
        "email": "info@cibt.edu.gh",
        "website": "cibt.edu.gh",
        "location": "Accra, Greater Accra",
        "certificate_issuing_university": "Catholic Institute of Business and Technology",
        "color1": "#800000",  #Maroon
        "color2": "#FFD700",  #Gold
        "logo": "cibt_logo.png",
        "logowithname": "cibt_logowithname.png"
    },
    "epuc": {
        "school_name": "Evangelical Presbyterian University College",
        "telephone": "+233 3620 96105",
        "email": "info@epuc.edu.gh",
        "website": "epuc.edu.gh",
        "location": "Ho, Volta Region",
        "certificate_issuing_university": "Evangelical Presbyterian University College",
        "color1": "#006400",  #Dark Green
        "color2": "#FFD700",  #Gold
        "logo": "epuc_logo.png",
        "logowithname": "epuc_logowithname.png"
    },
    "jayee": {
        "school_name": "Jayee University College",
        "telephone": "+233 302 512 706",
        "email": "info@jayeeuniversity.edu.gh",
        "website": "jayeeuniversity.edu.gh",
        "location": "Accra, Greater Accra",
        "certificate_issuing_university": "Jayee University College",
        "color1": "#8B4513",  #Saddle Brown
        "color2": "#FFD700",  #Gold
        "logo": "jayee_logo.png",
        "logowithname": "jayee_logowithname.png"
    },
    "spiritan": {
        "school_name": "Spiritan University College",
        "telephone": "+233 3220 94561",
        "email": "info@spiritan.edu.gh",
        "website": "spiritan.edu.gh",
        "location": "Ejisu, Ashanti Region",
        "certificate_issuing_university": "Spiritan University College",
        "color1": "#2F4F4F",  #Dark Slate Gray
        "color2": "#FFD700",  #Gold
        "logo": "spiritan_logo.png",
        "logowithname": "spiritan_logowithname.png"
    },
    "marshalls": {
        "school_name": "Marshalls University College",
        "telephone": "+233 302 254 696",
        "email": "info@marshalls.edu.gh",
        "website": "marshalls.edu.gh",
        "location": "Accra, Greater Accra",
        "certificate_issuing_university": "Marshalls University College",
        "color1": "#4682B4",  #Steel Blue
        "color2": "#FFD700",  #Gold
        "logo": "marshalls_logo.png",
        "logowithname": "marshalls_logowithname.png"
    },
    "west_end": {
        "school_name": "West End University College",
        "telephone": "+233 302 230 745",
        "email": "info@weuc.edu.gh",
        "website": "weuc.edu.gh",
        "location": "Accra, Greater Accra",
        "certificate_issuing_university": "West End University College",
        "color1": "#4169E1",  #Royal Blue
        "color2": "#FFD700",  #Gold
        "logo": "weuc_logo.png",
        "logowithname": "weuc_logowithname.png"
    },
    "maranatha": {
        "school_name": "Maranatha University College",
        "telephone": "+233 302 250 788",
        "email": "info@maranatha.edu.gh",
        "website": "maranatha.edu.gh",
        "location": "Accra, Greater Accra",
        "certificate_issuing_university": "Maranatha University College",
        "color1": "#8B0000",  #Dark Red
        "color2": "#FFD700",  #Gold
        "logo": "maranatha_logo.png",
        "logowithname": "maranatha_logowithname.png"
    }
    
}
    return universities_info[uni]
# List of employments in various sectors in Ghana
employment_list = {
    "health": [
        {"company": "Korle Bu Teaching Hospital", "job_title": "Nurse", "location": "Accra"},
        {"company": "37 Military Hospital", "job_title": "Medical Laboratory Technician", "location": "Accra"},
        {"company": "Ridge Hospital", "job_title": "Pharmacist", "location": "Accra"},
        {"company": "Komfo Anokye Teaching Hospital", "job_title": "Radiographer", "location": "Kumasi"},
        {"company": "Nyaho Medical Centre", "job_title": "Healthcare Assistant", "location": "Accra"},
        {"company": "Tamale Teaching Hospital", "job_title": "Midwife", "location": "Tamale"}
    ],
    "education": [
        {"company": "KNUST", "job_title": "Research Assistant", "location": "Kumasi"},
        {"company": "Ghana International School", "job_title": "Primary School Teacher", "location": "Accra"},
        {"company": "Achimota School", "job_title": "Guidance Counselor", "location": "Accra"},
        {"company": "Ashesi University", "job_title": "Admissions Officer", "location": "Berekuso"},
        {"company": "Central University", "job_title": "Finance Officer", "location": "Accra"}
    ],
    "finance": [
        {"company": "Ecobank Ghana", "job_title": "Financial Analyst", "location": "Accra"},
        {"company": "GCB Bank", "job_title": "Bank Teller", "location": "Accra"},
        {"company": "Prudential Bank", "job_title": "Credit Analyst", "location": "Accra"},
        {"company": "Fidelity Bank", "job_title": "Account Manager", "location": "Accra"},
        {"company": "Stanbic Bank", "job_title": "Risk Manager", "location": "Accra"},
        {"company": "Absa Bank Ghana", "job_title": "Branch Manager", "location": "Accra"}
    ],
    "technology": [
        {"company": "MTN Ghana", "job_title": "Software Developer", "location": "Accra"},
        {"company": "Vodafone Ghana", "job_title": "Network Engineer", "location": "Accra"},
        {"company": "Google Ghana", "job_title": "Data Analyst", "location": "Accra"},
        {"company": "IBM Ghana", "job_title": "IT Support Specialist", "location": "Accra"},
        {"company": "Rancard Solutions", "job_title": "Product Manager", "location": "Accra"},
        {"company": "Andela", "job_title": "Backend Developer", "location": "Accra"}
    ],
    "marketing": [
        {"company": "Unilever Ghana", "job_title": "Marketing Coordinator", "location": "Tema"},
        {"company": "Coca-Cola Bottling Company of Ghana", "job_title": "Brand Manager", "location": "Accra"},
        {"company": "Nestlé Ghana", "job_title": "Sales Executive", "location": "Tema"},
        {"company": "Guinness Ghana Breweries", "job_title": "Market Research Analyst", "location": "Accra"},
        {"company": "MTN Ghana", "job_title": "Digital Marketing Specialist", "location": "Accra"},
        {"company": "Tigo Ghana", "job_title": "Advertising Executive", "location": "Accra"}
    ],
    # Add more sectors and companies as needed
}

specific_interests = [
    "Healthcare and patient care",
    "Public health and community outreach",
    "Biotechnology and medical research",
    "Environmental sustainability",
    "Educational development and teaching",
    "Data analysis and statistics",
    "Financial management and investment strategies",
    "Software development and programming",
    "Digital marketing and social media",
    "Entrepreneurship and business innovation",
    "Sports science and fitness",
    "Graphic design and creative arts",
    "Human rights and social justice",
    "Travel and cultural exchange",
    "Languages and linguistics",
]

specific_skills = [
    "Clinical assessment and patient care",
    "Laboratory techniques and data analysis",
    "Project management and organizational skills",
    "Effective communication and presentation",
    "Advanced proficiency in Microsoft Office Suite",
    "Fluency in multiple languages (e.g., English, French, Twi)",
    "Programming languages (e.g., Python, JavaScript)",
    "Digital marketing strategies and analytics",
    "Team leadership and conflict resolution",
    "Financial analysis and budgeting",
    "Teaching and curriculum development",
    "Problem-solving and critical thinking",
    "Customer service and client relations",
    "Adaptability and quick learning",
    "Research and report writing",
]

achievements = [
    "Completed a research project on the impact of climate change on local biodiversity",
    "Led a successful community health outreach program, reaching over 500 participants",
    "Published a paper in the Journal of Environmental Studies",
    "Secured a scholarship for outstanding performance in undergraduate studies",
    "Recognized for exceptional volunteer service at a local orphanage",
    "Achieved a high distinction in a national certification exam",
]

extracurricular_activities = [
    "Volunteered at a local health outreach program, educating communities on basic healthcare",
    "Participated in a robotics club, developing teamwork and technical skills",
    "Played for the university football team, demonstrating teamwork and discipline",
    "Involved in student government as a class representative",
    "Organized fundraising events for a charity organization",
    "Active member of the Environmental Club, promoting sustainability initiatives on campus",
    "Engaged in a coding bootcamp, learning new programming languages",
    "Conducted workshops on financial literacy for underprivileged youth",
]

def select_random_items(category, number_of_items=3):
    """
    Selects a specified number of random items from the given category list.
    
    :param category: The list from which to select items (e.g., 'specific_interests', 'specific_skills').
    :param number_of_items: The number of items to select (default is 3).
    :return: A list of randomly selected items.
    """
    if category in globals():
        items = globals()[category]
        return random.sample(items, min(number_of_items, len(items)))
    else:
        return []
