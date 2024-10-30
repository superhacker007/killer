import random, schooldatas

companies = [
    ["companyname", "telephonenumber", "email", "logo"],
    ["Tullow Oil Plc", "0309847857", "info@tullowoil.com", "tullow.png"],
    ["KPMG Ghana", "0302774533", "info@kpmg.com.gh", "kpmg.png"],
    ["Bank of Ghana", "0302666174", "info@bog.gov.gh", "bog.png"],
    # ["Nestlé Ghana", "0302543150", "info@gh.nestle.com", "nestle.jpg"],
    # ["Deloitte Ghana", "0302221312", "info@deloitte.com.gh", "deloitte.jpg"],
    # ["MTN Ghana", "0244300000", "info@mtn.com.gh", "mtn.jpg"],
    # ["Ghana National Petroleum Corporation (GNPC)", "0302770003", "info@gnpcghana.com", "gnpc.jpg"],
    # ["Ecobank Ghana", "0302662511", "info@ecobank.com", "ecobank.jpg"],
    # ["Standard Chartered Bank Ghana", "0302744474", "info@sc.com", "stanchart.jpg"],
    # ["AirtelTigo", "0277551000", "info@airteltigo.com.gh", "airteltigo.jpg"]
]

def getemployed():
    # Randomly selecting 3 places from the list (excluding the header)
    if len(companies) > 4:
        selected_places = random.sample(companies[1:], 3)
    else:
        selected_places = companies[1:]
    return selected_places

def get_jobs(sector, number_of_jobs=2):
    """
    Selects a specified number of random jobs from the given sector.
    
    :param sector: The sector from which to select jobs (e.g., 'health', 'education').
    :param number_of_jobs: The number of jobs to select (default is 3).
    :return: A list of randomly selected jobs.
    """
    if sector in schooldatas.employment_list:
        jobs = random.sample(schooldatas.employment_list[sector], min(number_of_jobs, len(schooldatas.employment_list[sector])))
        return jobs
    else:
        return []
