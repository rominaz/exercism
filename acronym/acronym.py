
def abbreviate(words):
    import re
    justchar = re.sub('[-]' , ' ' , words) #remvoing any non-Character or digits from string
    first_letters = "".join(re.findall('^\w|\s\w' , justchar)) #finding first character of words joining them in a string  
    acronym = (re.sub('\s' , '' , first_letters)).upper()  #removing additional whitspaces between frist characters and converting them to uppercase letters
    return acronym

