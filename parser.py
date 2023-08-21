# Modules
import json

# Read File
with open("sample.json", "r") as json_file:
    data = json.load(json_file)

# List Seperation
accessories = []
fibers = []
fiber_details = []

# Parsing File
for item in data:
    if item["type"] == "accessory model":
        accessories.append(item["filename"])
    elif item["type"] == "fiber model":
        fibers.append(item["filename"])
        fiber_details.append((item["filename"], item["start"], item["end"]))

# Output
print("{" + ",".join(accessories) + "}")
print("{" + ",".join(fibers) + "}")

for fiber, start, end in fiber_details:
    print(f"{fiber.replace(' ', '_')} {start} {end}")
