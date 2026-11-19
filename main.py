from pyscript import document
# Instrument, Measures, Unit of measurement, Purpose
Instruments = {
    "THERMOMETER": ("Air Temperature", "Degrees Celsius (ºC)", "Measures how hot or cold the air is."),
    "BAROMETER": ("Atmostpheric Pressure", "Hectopascals (hPa)", "Measures air pressure to help monitor weather changes."),
    "ANEMOMETER": ("Wind Speed", "Kilometers per hour (km/h)", "Measures how fast the wind is blowing."),
    "HYGROMETER": ("Relative Humidity", "Percent (%)", "Measures the amount of moisture in the air."),
    "RAIN GAUGE": ("Rainfall", "Milimeters (mm)", "Measures the amount of rainfall in an area."),
    "WIND VANE": ("Wind Direction", "Cardinal Directions", "Identifies the direction from which the wind is blowing."),
    "WEATHER BALLOON": ("Atmospheric Conditions", "Varies", "Collects atmospheric data at different altitudes."),
    "PYRANOMETER": ("Solar Radiation", "Watts per square meter (W/m^2)", "Measures incoming solar radiation."),
}

def search_instrument(e):
    Instrument1 = document.getElementById("Instrument1").value.strip().upper()

    result = Instruments.get(
        Instrument1,
        ("Weather Instrument not found", "-", "-", 
         "This instrument is not included.")
    )

#Instrument
    document.getElementById("Instrument").innerText = Instrument1
#Measures
    document.getElementById("Measures").innerText = result[0]
#Unit of Measurement
    document.getElementById("Unit").innerText = result[1]
#Purpose
    document.getElementById("Purpose").innerText = result[2]
