particles = "Fermions", "Bosons", "Gluons", "Protons", "Neutrons", "Mesons", "Pions", "Quark", "Eletron", "Muons", "Fotons"
print(particles[0:5])
print(particles[-4:])
print(sorted(particles))
for pos in particles:
    if pos == "Mesons":
        print(f"O Meson está na posição {particles.index(pos)}°")
#print(f"O Meson está na posição {particles.index("Mesons")}")

