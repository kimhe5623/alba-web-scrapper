import csv

def save_to_file(job_details, companyName, isNewLine):
  file = open(f"alba/{companyName}.csv", mode = "w" if isNewLine else "a+")
  writer = csv.writer(file)
  writer.writerow(['place', 'title', 'time', 'pay', 'date'])

  for job_detail in job_details:
    writer.writerow(list(job_detail.values()))
  return