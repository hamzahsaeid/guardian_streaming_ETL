import re

def url_string(text_string, date_from=None):
    """
    This function creates a search string for the API URL
    It includes the optional date_from string
    """
    
    search_list = text_string.split() # Split the list
    seperator = "%20" # space seperator  

    if date_from:
        regex = re.compile("[0-9]{4}\-[0-9]{2}\-[0-9]{2}")
        match = re.match(regex, date_from)
        
        if not (match):
            return "Please enter date is correct format, as follows: YYYY-MM-DD"

    if len(search_list) > 1: # if the list contains more than 1 element
        
        join_words = seperator.join(search_list) # insert '%20' between each word

        final__string_text = f'%22{join_words}%22' # create a new string - starts & ends with '%22'.
        
        return final__string_text if not date_from else f"from-date={date_from}&q={final__string_text}"
    else:
        return text_string
  
  
