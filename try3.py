import requests, json, time

url = "https://api.undetectable.ai/submit"

payload = json.dumps({
  "content": """Subject: Statement of Purpose to study Business Administration at Cranfield University

Dear Admissions Committee,

My name is {{current_user.username}}, a business professional with a fervent interest in the realm of Business Administration. I currently work as a Business Analyst at XYZ Corporation, London, and am resolute in my ambition to further broaden my comprehension in this field. I want to bring this ambition to life by studying a Master’s degree in Business Administration at Cranfield University. It is my firm belief that this innovative programme will provide me with the advanced concepts and methodologies desirable for a successful career in business management and leadership.

My interest in Business Administration emanated during my undergraduate years at the University of London. Here, I completed my Bachelor's Degree in Business Management with First Class Honours. This is where my foundation in entrepreneurship and innovation was laid. I found myself engrossed in the complexities of the business world and its functionality, and thus decided to explore this domain deeper. 

Beyond academics, I looked forward to applying acquired theoretical knowledge to real-life business scenarios. This propelled me onto my career path as a Business Analyst at XYZ Corporation in 2018. Over the next few years, I gained considerable professional experience, with key responsibilities including analyzing business processes and recommending improvements. 

My work experiences honed my analytical skills, where I observed the power of data in making critical business decisions. It also put my Project Management and Strategic Planning capabilities to the test. As I thrived in my roles, I was certain that I wanted to further enhance these skills and build a more comprehensive understanding of business administration.

Cranfield University’s rigorous MBA program grabbed my attention due to its strong focus on the relation between theory and practice. The globally renowned faculty, the culture of innovation, and the practical approach to teaching will undoubtedly provide a highly stimulating academic environment.

I truly believe it holds the resources and possibilities that will empower me to bring a greater impact in my future professional roles. My ambition is to continually evolve as a well-rounded business professional, who brings profound knowledge and superior skills to make strategic decisions and provide effective leadership. This program is the perfect conduit to fuel this aspiration.

I am confident that I will make a positive contribution to the vibrant and diverse student community at Cranfield. At the same time, I look forward to learning from my peers, absorbing their varied experiences and perspectives.

I am excited about the opportunities that studying at Cranfield University will bring, and the prospect of contributing to the business world in a meaningful way. 

Thank you for considering my application. Looking forward to the possibility of becoming a part of your esteemed institution.

Yours Sincerely,
{{current_user.username}}""",
  "readability": "High School",
  "purpose": "General Writing",
  "strength": "More Human"
})
headers = {
  'api-key': '1717156461456x425731042749940100',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

time.sleep(20)

url = "https://api.undetectable.ai/document"

payload = json.dumps({
  "id": response.json()['id']
})
headers = {
  'api-key': '1717156461456x425731042749940100',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)