import obd

connection = obd.OBD() # auto-connect to bluetooth port

if connection.is_connected():
    print("Connected to OBD-II adapter")

speed = obd.commands.SPEED
coolant = obd.commands.COOLANT_TEMP
fuel = obd.commands.FUEL_RATE
oil_temp = obd.commands.OIL_TEMP

responses = [
    connection.query(speed),
    connection.query(coolant),
    connection.query(fuel),
    connection.query(oil_temp)
    ]
print(f"Speed: {responses[0].value }")
print(f"Coolant Temperature: {responses[1].value}")
print(f"Fuel Rate: {responses[2].value}")
print(f"Oil temperature: {responses[3].value}")

for cmd in [obd.commands.PIDS_A, obd.commands.PIDS_B]:
    resp = connection.query(cmd)
    print(cmd.name, resp.value

# obd.commands.SPEED                  # Vehicle speed (confirmed)
# obd.commands.RPM                    # Engine RPM (confirmed)
# obd.commands.COOLANT_TEMP           # Coolant temp (confirmed)
# obd.commands.INTAKE_TEMP            # Intake air temp (confirmed)
# obd.commands.MAF                    # Mass airflow (confirmed)
# obd.commands.TIMING_ADVANCE         # Spark timing (confirmed)
# obd.commands.BAROMETRIC_PRESSURE    # Barometric pressure (confirmed)
# obd.commands.FUEL_LEVEL             # Fuel level % (confirmed)
# obd.commands.CONTROL_MODULE_VOLTAGE # ECU voltage (confirmed)
# obd.commands.ABSOLUTE_LOAD          # Absolute engine load (confirmed)
