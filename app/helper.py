class Helper:    

    @staticmethod
    def keysExistAndNotEmptyString(required_strings, search_data):

        for field in required_strings:
            if not Helper.keyExistAndNotEmptyString(field, search_data):
                return False
        
        return True

    @staticmethod
    def keyExistAndNotEmptyString(key, search_data):            
        return (key in search_data) and (search_data[key]) and (isinstance(search_data[key], str)) and (search_data[key].strip())

    