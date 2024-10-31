
# Task 1
settings = {'title': 'My original title'}

def change_site_title(new_title):
    global settings
    settings['title'] = new_title

print(settings)
change_site_title("A new fancy title")
print(settings)


# Task 2
default_settings = {'title': 'My original title'}

def get_title(settings=default_settings):
    return settings.get('title')

print(get_title(settings))
print(get_title())
change_site_title("A new fancy title")
print(get_title(settings))
print(get_title())


# Task 3
settings = {'title': 'My original title', 'pages': []}
default_settings = {'title': 'My original title', 'pages': []}

def get_pages(settings=default_settings):
    return settings.get('pages')

def add_page(page, settings=default_settings):
    settings['pages'].append(page)

home = {"title": "Home", "path": "/"}
add_page(home)
print(get_pages())
print(get_pages(settings))
about = {"title": "About", "path": "/about/"}
add_page(about, settings)
print(get_pages())
print(get_pages(settings))


# Task 4
def print_user_profile(gender='female', first=None, last='Doe', pictures=[]):
    if first is None:
        first = 'John' if gender == 'male' else 'Jane'
    print(f"The user {first} {last} has the following pictures:")
    print("common_header.png")
    for picture in pictures:
        print(picture)

test_data1 = {"gender": "male", "last": "Brown", "pictures": ["holidays1.png", "easter_grandma.png"]}
test_data2 = {"first": "Alicia", "last": "Schmidt"}
test_data3 = {"last": "Korkov", "pictures": ["sunset.png"]}

print_user_profile(**test_data1)
print_user_profile(**test_data2)
print_user_profile(**test_data3)
print_user_profile(**test_data2)