from soup import getSoup

def getCompanyList():
  url = "http://www.alba.co.kr/"
  soup = getSoup(url)
  brandBoxes = soup.find_all("ul", {"class": "goodsBox"})
  brands = brandBoxes[1].find_all("li", {"class": "impact"})
  
  companyList = []
  for brand in brands:
    name = brand.find("span", {"class": "company"}).get_text().replace("/", "_")
    link = brand.find("a", {"class": "goodsBox-info"})['href']
    companyList.append({
      "name": name,
      "link": link
    })
  return companyList