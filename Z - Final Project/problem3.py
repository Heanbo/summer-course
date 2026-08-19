# Our inbound colonists rapidly approach Mars atmosphere, but we still do not have reliable comms with them.
# We must rapidly launch our spare rocket to establish comms and share the correct telemetry data with them before they smash into Mars!

# There's no time to unload the modules that are on the rocket, and we must begin fueling right away.
# The problem is, we do not know how much fuel we need.

# As you rush to the rocket, you notice a list of all of the modules' mass on board (your python file input).

# Fuel required to launch a given module is based on its mass.
# Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

# For example:

# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.

# As the Chief Engineer, you need to calculate the total fuel requirement.
# To find the total fuel requirement, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

# What is the sum of the fuel requirements for all of the modules on your spacecraft?

# Once you solve this problem, issue a pull request with all three of your solutions to the International Space Station (https://github.com/Ryan-L-N/cohort-7-practical.git).
# To keep the International Space Station's file system clean, your solutions should be inside of a folder with your last name.

# Finally, create a broadcast beacon with Earth to state that the crisis was averted.
# To do this, create a VM, host a website with a picture of your choice on the VM, and share the public IP address of your website with the International Space Station.


# calculate the fuel required for a given mass
def calculate_fuel(mass):
    return mass // 3 - 2


# Read the masses from the input file
with open("input.txt", "r") as f:
    masses = [int(line.strip()) for line in f]

# Calculate the total fuel requirement
total_fuel = sum(calculate_fuel(mass) for mass in masses)

print(f"Total fuel required: {total_fuel}")
