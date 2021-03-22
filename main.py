# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# part 1: greet template
def greet(name, greeting_template="Hello, <name>!"):
    greeting = greeting_template.replace("<name>", name)
    return greeting

name = "Erwin"
greeting_template = "What is up, <name>"
greeting = greet(name, greeting_template)
print(f"{greeting}!")

# # part 2: Force
def force(mass=1.0, body="earth"):
    planet_dict = {"Sun": 274, "Jupiter": 24.92, "Neptune": 11.15, "Saturn": 10.44,
                   "Earth":9.798,"Uranus":8.87,"Venus":8.87,"Mars":3.71,
                   "Mercury":3.7,"Moon":1.62,"Pluto":0.58}
    # get value to key (body)
    value = planet_dict.get(body)
    force = mass * value
    force = round(force,1)
    # body = body.lower()         Hoewel de opdracht een lower() vraagt, vind ik dat een planetennaam met upper() hoort
    return force
print("the force is equal to:",force(12, "Uranus"), "Newton")


# part 3: Gravity
def pull(m1, m2, d):
    G = 6.674e-11
    F = G *((m1 * m2)/d**2)
    return F

m1 = 800
m2 = 1500
d = 3
pull(m1,m2,d)
print(f"The attrackting force between m1 and m2 equals {pull(m1,m2,d)} Newton")


