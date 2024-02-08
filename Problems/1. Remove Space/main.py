def remove_spaces(s = None):
    if s is None:
        return ""
    else:
        result = ""
        
        is_character = False
        
        # Add more characters
        characters = [",", ".", "!"]
        
        for letter in s.strip():
            if letter in characters:
                result += letter
                
            elif letter.isalnum() and is_character:
                result += letter
                
            elif letter.isalnum():
                is_character = True
                result += " "
                result += letter
                
            elif letter == " ":
                is_character = False
                
        return result.strip()

print(remove_spaces("Multiple spaces  are    removed , hurray !!!   !"))

