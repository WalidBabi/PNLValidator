import re

# Define your regular expression patterns and compile them
patterns = [
    re.compile(r'^(?P<PNL>PNL)$'),
    re.compile(r'^(?P<Header>[A-Z]{2}\d{3}/\d{2}[A-Z]{3} [A-Z]{3} PART\d{1,2})$'),
    re.compile(r'^(?P<HyphenLine>-[A-Z]{3}\d{2,3}[A-Z])$'),
    re.compile(r'^(?P<PassengerNameLine>1[A-Z]+/[A-Z]+(MR|MS|MRs)?(-[A-Z]{1,2}[0-9])?( \.[A-Z]/[A-Z]+)?)$'),
    re.compile(r'^(?P<CHLDLine>\.R/CHLD HK1 \d{2}[A-Z]{3}\d{2}-[A-Z]+/[A-Z]+)$'),
    re.compile(r'^(?P<FOIDLine>\.R/FOID HK1 ([A-Z]+\d{9})?[A-Z0-9]+)$'),
    re.compile(r'^(?P<TKNELine>\.R/TKNE HK1 ([A-Z]{1,3})?\d{13}/\d{1})$'),
    re.compile(r'^(?P<INFTLine>\.R/INFT HK1 [A-Z]+/[A-Z]+)$'),
    re.compile(r'^(?P<DOCSLine>\.R/DOCS HK1/P/[A-Z]{2}/([A-Z]*[0-9]{9})?[A-Z0-9]+/[A-Z]{2}/\d{2}[A-Z]{3}\d{2}/[M|F|MI|FI]/\d{2}[A-Z]{3}\d{2}/[A-Z]+/[A-Z]+)$'),
    re.compile(r'^(?P<ENDLine>ENDPART\d{1,2})$',),
    re.compile(r'^(?P<ENDPNL>ENDPNL)$')
]

file_path = "wrong.txt"

with open(file_path, 'r') as file:
    pnl_data = file.read()

pnl_data= pnl_data.split("\n")
   
# Initialize a list to collect error messages
error_messages = []


line_number = 0
    
    # Iterate through the lines and apply validation rules
for line in pnl_data:
    line_number += 1
    matched = False

    # Check each pattern against the line
    for pattern in patterns:
        match = pattern.match(line)
        if match:
            # Line matches a pattern
            matched = True
            break  # No need to check other patterns once a match is found
    
    if not matched:
        # If no pattern matched, add an error message to the list
        error_messages.append(f"Line {line_number}: Invalid format: {line}")

# Check if there are any error messages
if error_messages:
    print("Validation Errors:")
    for error_message in error_messages:
        print(error_message)
else:
    print("Validation passed.")
