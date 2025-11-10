#Write a function that when given a URL as a string, 
# parses out just the domain name and returns it as a string. 
# For example: url = "http://github.com/carbonfive/raygun" -> domain name = "github"

def domain_name(url):
    # Eliminar el prefijo del esquema si está presente
    if "://" in url:
        url = url.split("://")[1] # Obtener la parte después de '://'
    
    # Eliminar 'www.' si está presente
    if url.startswith("www."): #o url.replace("www.","",1)
        url = url[4:]
    
    # Extraer el dominio antes del primer '/'
    domain = url.split('/')[0] # Obtener la parte antes de '/'
    
    # Extraer el dominio antes del primer '.'
    domain = domain.split('.')[0]# Obtener la parte antes de '.'
    
    return domain

# Ejemplos de uso
print(domain_name("http://www.github.com/carbonfive/raygun"))  # Imprime: github






