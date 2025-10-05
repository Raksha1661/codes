def calculate_velocity(u, a, t):
    # Final velocity: v = u + a*t
    return u + a * t

def calculate_displacement(u, a, t):
    # Displacement: s = u*t + 0.5*a*t^2
    return u * t + 0.5 * a * t**2

# Input values
u = float(input("Enter initial velocity (u) in m/s: "))
a = float(input("Enter acceleration (a) in m/s²: "))
t = float(input("Enter time (t) in seconds: "))

# Calculations
v = calculate_velocity(u, a, t)
s = calculate_displacement(u, a, t)

# Output
print(f"\nFinal Velocity: {v:.2f} m/s")
print(f"Displacement: {s:.2f} meters")
