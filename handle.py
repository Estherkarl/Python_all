
#Your result should look like this: London

city = "London"
print(city)


#Your result should look like this: Berlin: 3645000

city = "berlin"
population = 3645000
capitalising = city.capitalize()
concatenation= capitalising + ": " + str(population)
print(concatenation)

#Your result should look like this: City: London (True) Population: 9000000

city = "london"
population = 9000000
print("City: " + city.capitalize() + " (" + str(isinstance(city, str)) + ") Population: " + str(population))

#Your result should look like this: capital: 92

text_92 = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital." 
word_92 = "capital" 
if word_92 in text_92:     
    index = text_92.index(word_92)    
    print(f"{word_92}: {index}") 
    
#Your result should look like this: ['Berlin', 'straddles

text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau." 
result5 = text.split()
print(result5)

#Your result should look like this: Berlin is surrounded by the State 

text_capital = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
new_text = text_capital.replace("capital", "capital of Germany")
print(new_text)


#task7

def check_even_odd_string(string):
    if len(string) % 2 == 0:
        return "even"
    else:
        return "odd"


string1 = "hello world"
string2 = "hello planet"
string3 = ""

print(check_even_odd_string(string1))  
print(check_even_odd_string(string2))  
print(check_even_odd_string(string3))  

#Task8

string8 = "The Quick BroWnFoX jumps over the laZy Dog!"
print("Original String:", string8)
print("String in uppercase:", string8.upper())
print("String in lowercase:", string8.lower())


#Task 9

def find_nemo(sentence):
    sentence_lower = sentence.lower()
    if "nemo" in sentence_lower:
        index = sentence_lower.index("nemo")
        return f"I found Nemo at {index}!"
    else:
        return "I can't find Nemo :("

# Example usage:
print(find_nemo("I am finding Nemo !"))  # Output: I found Nemo at 13!
print(find_nemo("Nemo is me"))  # Output: I found Nemo at 0!
print(find_nemo("I Nemo am"))  # Output: I found Nemo at 2!
print(find_nemo("Hello World"))  # Output: I can't find Nemo :(
 


#Task 10


sentence = "A dogmatic dog buys dogecoin to become rich and buy hotdogs every day."
new_sentence = sentence.replace(" dog ", " cat ")
print(f"Output: {new_sentence}")

