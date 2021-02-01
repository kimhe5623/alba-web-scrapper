import math
from save import save_to_file

def getJobDetail(job_details):
  place = job_details[0].get_text().replace("\xa0", " ")
  title = job_details[1].find("span", {"class": "company"}).get_text()
  time_ = job_details[2].get_text()
  pay = job_details[3].get_text()
  date_ = job_details[4].get_text()
  return {
    "place": place,
    "title": title,
    "time": time_,
    "pay": pay,
    "date": date_
    }

def getJobList(soup, companyName, isNewLine):
  jobsContainer = soup.find("div", {"id":"NormalInfo"})
  jobs = jobsContainer.find("tbody").find_all("tr")
  
  cnt = len(jobs)
  jobList= []
  for i in range(cnt):
    job_details = jobs[i].find_all("td")
    if(len(job_details) == 5):
      jobList.append(getJobDetail(job_details))
  save_to_file(jobList, companyName, isNewLine)
    
def getMaxPage(soup):
  jobCount = soup.find("p", {"class": "jobCount"}).find("strong").get_text().replace(",", "")
  maxPageNum = math.ceil(int(jobCount)/50)
  return maxPageNum