def generate_bc(url, separator):
    remove = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]
    breadcrumb = '<a href="/">HOME</a>'
    url = url.replace("http://","").replace("https://","")
    elements = url.split("/")[1:]
    elements = [i.split("#")[0].split("?")[0] for i in elements]
    if elements == []:
        return '<span class="active">HOME</span>'
    if len(elements) == 1 and (elements[-1].startswith("index") or elements[0] == ""):
        return '<span class="active">HOME</span>'    
    if elements[-1].startswith("index"):
        elements.pop()    
    for i,j in enumerate(elements):
        if i == len(elements)-1:            
            if len(j) > 30:
                breadcrumb +=  str(separator) + str('<span class="active">{0}</span>'.format("".join([k[0].upper() for k in j.split("-") if k not in remove])))
                break                
            breadcrumb +=  str(separator) + str('<span class="active">{0}</span>'.format(j.split(".")[0].upper().replace("-"," ")))
            break
        if len(j) > 30:
            breadcrumb +=  str(separator) +  str('<a href="/{0}/">{1}</a>'.format("/".join(elements[:i+1]),"".join([k[0].upper() for k in j.split("-") if k not in remove])))
            continue            
        breadcrumb +=  str(separator) +  str('<a href="/{0}/">{1}</a>'.format("/".join(elements[:i+1]),j.upper().replace("-"," ")))        
    return breadcrumb   
        
