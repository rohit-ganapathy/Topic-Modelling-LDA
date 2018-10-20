

def clean(file):
   
    links=[]
    articles=[]
    article=""
    file=open(file)
    
    for line in file:
      if "http://" in line and "URL" in line:
          
         links.append(line.split(": ")[1])
         
         if len(article)!=0:
           articles.append(article.replace("\n",""))
         article=""
            
      else:
           article=article+line
    
    articles.append(article.replace("\n",""))
    
    return links,articles