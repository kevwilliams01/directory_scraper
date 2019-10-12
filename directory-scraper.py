from selenium import webdriver
import pandas




census = pandas.read_csv('YOUR_NAMES_LIST.csv')
surnames = census.name.tolist()
queries = surnames
#queries = ['woodward']
#f = open(filename, "w")
#headers = "email\n"
#f.write(headers)

for query in queries:
    driver = webdriver.Firefox()
    driver.get('YOUR_DIRECTORY_URL'+ query)
    #data we want is in an iframe
    iframes = driver.find_elements_by_tag_name("iframe")
    driver.switch_to.frame(iframes[0])
    #get each row in the iframe-generated table
    results = driver.find_elements_by_xpath("XPATH")
    
    
    urls = []
        

    for result in results:

        name = result.text
            
        if "Student" in name:
            #f.write(name + ", ")
            
            #print(name + ", ")
            try:
                link = result.find_element_by_tag_name('a')
                name_link = link.get_attribute("href")
                urls.append(name_link)
                #f.write(name_link + "\n")
                #emails = driver.find_elements_by_xpath("//*[@id='content']/div/div/dl[1]/dd")
                #print(email + "\n")
                #for email in emails:
                    #f.write(email.text + "\n")
                    #print(email.text + "\n")
                    
            except:
                #f.write("no email" + "\n")
                urls.append("no email")
   
        
           
        #print(name + " " + name_link)
                
    
    driver.quit()
    for url in urls:
        driver = webdriver.Firefox()
        try:
            driver.get(url)
            #get the element that is supposed to be the email
            results = driver.find_elements_by_xpath("XPATH")
            for result in results:
                word =result.text
                #only print the element if actually an email
                if "@" in word:
                    print(word)
        except:
            print("")

        driver.quit()
    

    
    











    
