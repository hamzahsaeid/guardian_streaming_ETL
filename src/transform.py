
def transform(input_data):
    """ Transforms the input dictionaries and produces required output

    Given a list of dictionaries, the function creates a new list of dictionaries
    with four key-value pairs

    Arg:
        input_data: raw api extract 

    Returns:
        a new list with four key-value pairs
    """
    if not isinstance(input_data, list): # validates the input data type
        raise TypeError("Input data must be a list")
    
    if not input_data: # validates that the input list is not empty
        return "No data to transform"

    # Creates a new list of dictionaries containing only the relevant values    
    transformed_data = [
                        {
                        "webPublicationDate": record["webPublicationDate"],
                        'webTitle': record["webTitle"],
                        "webUrl": record["webUrl"],
                        "content_preview": record["fields"]["body"][:1000]
                        } 
                        for record in input_data
    ]
    return transformed_data