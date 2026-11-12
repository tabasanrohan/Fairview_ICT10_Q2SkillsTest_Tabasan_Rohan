from pyscript import document
# Atomic Number, Atomic Mass, Element Name
non_metals = {
    "H": ("Hydrogen", 1, "1.008"),
    "HE": ("Helium", 2, "4.0026"),
    "C": ("Carbon", 6, "12.011"),
    "N": ("Nitrogen", 7, "14.007"),
    "O": ("Oxygen", 8, "15.999"),
    "S": ("Sulfur", 16, "32.06"),
    "CL": ("Chlorine", 17, "35.45"),
    "AR": ("Argon", 18, "39.948"),
    "SE": ("Selenium", 34, "78.971"),
    "BR": ("Bromine", 35, "79.904"),
    "KR": ("Krypton", 36, "83.798"),
    "I": ("Iodine", 53, "126.904"),
    "XE": ("Xenon", 54, "131.293"),
    "F": ("Fluorine", 9, "18.998"),
    "NE": ("Neon", 10, "20.180"),
    "P": ("Phosphorus", 15, "30.974"),
    "AT": ("Astatine", 85, "210"),
    "RN": ("Radon", 86, "222")
}
def search_element(e):
    Element1 = document.getElementById("Element1").value.strip().upper()
    result = non_metals.get(Element1, ("Element not found", "-", "-"))
    if result[0] == "Element not found":
        document.getElementById("symbol").innerText = "-"
        document.getElementById("name").innerText = result[0]
        document.getElementById("atomnumber").innerText = result[1]
        document.getElementById("mass").innerText = result[2]
    else:
        document.getElementById("symbol").innerText = Element1
        document.getElementById("name").innerText = result[0]
        document.getElementById("atomnumber").innerText = result[1]
        document.getElementById("mass").innerText = result[2]