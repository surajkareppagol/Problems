def lengthOfLastWord(s: str) -> int:
        if s is None:
            return 0
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
                    
            result = result.strip()

        return len(result.split(" ")[-1])

print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))