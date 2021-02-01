import os
from company import getCompanyList
from soup import getSoup
from jobs import getMaxPage, getJobList

os.system("clear")

def main():
  companyList = getCompanyList()
  scrap_alba_list(companyList)

def scrap_alba_list(companyList):
  for company in companyList:
    pageNum = 1
    url = f"{company['link']}?page={pageNum}&pagesize=50"
    soup = getSoup(url)
    print(f"Scraping {company['name']} ...")
    max_page = (getMaxPage(soup))
    getJobList(soup, company['name'], True)

    if(max_page != 0 and max_page > 1):
      for i in range(2, max_page + 1):
        pageNum = i
        soup = getSoup(url)
        getJobList(soup, company['name'], False)

if __name__ == "__main__":
  main()