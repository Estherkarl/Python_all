#Task1
text = "Berlin is a world city of culture, politics, media and science."
first_whitespace = text.index(" ")
print(f"The first white-space character is located at position: {first_whitespace}")

#Task2
import re

def remove_leading_trailing_zeros(input_string):
    output_string = re.sub(r'^0+|0+$', '', input_string)
    return output_string

input_1 = "0023.07623070"
input_2 = "hello world"
input_3 = "01230"

output_1 = remove_leading_trailing_zeros(input_1)
output_2 = remove_leading_trailing_zeros(input_2)
output_3 = remove_leading_trailing_zeros(input_3)

print(output_1)  
print(output_2)  
print(output_3)  


#Task3
import re

paragraph = "In the bustling world of digital communication, emails serve as the lifeline of professional and personal correspondence. From boardrooms to living rooms, individuals rely on electronic messages to convey information swiftly and efficiently. JohnDoe123@example.com, a common placeholder, often finds itself at the forefront of test emails, representing the generic sender in countless trial messages. Meanwhile, JaneSmith456@gmail.com plays a similar role, popping up in various drafts and test scenarios across the virtual landscape. As emails traverse the cyber realm, TestUser789@hotmail.com emerges as another common character, standing in as a placeholder identity in the vast sea of trial messages. These digital avatars, like PlaceholderEmail1@domain.com and DummySender567@yahoo.com, dance through the interconnected web of communication as testers fine-tune the nuances of their messages. In the quest for email perfection, MessageTester987@mail.com and SenderPlaceholderXYZ@outlook.com take their turns, navigating the intricate pathways of the digital inbox. The symphony of electronic communication resonates with these fictional email personas, each contributing its part to the harmonious melody of the online exchange. Whether it's BusinessTestEmail789@domain.org or ExperimentMail456@protonmail.com, these dummy emails weave an intricate tapestry in the vast landscape of the digital communication ecosystem."

email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
emails = re.findall(email_pattern, paragraph)

print(emails)