"""
message = "Hello python world!"
print(message)

message = "Hello python crash course world!"
print(message)

name = "tom palmer"
print(name.title())

name = 'Tom Palmer'
print(name.upper())
print(name.lower())

first_name = "tom"
last_name = "palmer"
full_name = f"{first_name} {last_name}"
message = (f"Hello, {full_name.title()}!")
print(message)

"""
"""
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0].title())
print(bicycles[3].title())
"""
"""
bicycles =['trek','cannondale','redline','specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)
"""

"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
"""
"""
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
"""

"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)
"""

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")