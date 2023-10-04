import re
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Define your regular expression patterns and compile them
patterns = [
    re.compile(r'^(?P<PNL>PNL)$'),
    re.compile(r'^(?P<Header>[A-Z]{2}\d{3}/\d{2}[A-Z]{3} [A-Z]{3})$'),
    re.compile(r'^(?P<HyphenLine>-[A-Z]{2,3}\d{2,3}[A-Z])$'),
    re.compile(r'^(?P<PassengerNameLine>1[A-Z]+/[A-Z]+(MR|MS|MRs)?(-[A-Z]{1,2}[0-9])?( \.L/[A-Z]+)?)$'),
    re.compile(r'^(?P<CHLDLine>\.R/CHLD HK1 \d{2}[A-Z]{3}\d{2}-[A-Z]+/[A-Z]+)$'),
    re.compile(r'^(?P<FOIDLine>\.R/FOID HK1 [A-Z0-9]+)$'),
    re.compile(r'^(?P<TKNELine>\.R/TKNE HK1 \d{13}/\d{1})$'),
    re.compile(r'^(?P<INFTLine>\.R/INFT HK1 [A-Z]+/[A-Z]+)$'),
    re.compile(r'^(?P<DOCSLine>\.R/DOCS HK1/P/[A-Z]{2}/([A-Z]*[0-9]{9})?[A-Z0-9]+/[A-Z]{2}/\d{2}[A-Z]{3}\d{2}/([M|F])?([MI|FI])?/\d{2}[A-Z]{3}\d{2}/[A-Z]+/[A-Z]+)$'),
    re.compile(r'^(?P<ENDPNL>ENDPNL)$')
]

def validate_text():
    # Clear any existing tags and error count label
    text_area.tag_remove("error", "1.0", "end")
    error_count_label.config(text="")

    pnl_data = text_area.get("1.0", "end-1c").split("\n")

    line_number = 0
    error_lines = []

    for line in pnl_data:
        line_number += 1
        matched = False

        for pattern in patterns:
            match = pattern.match(line)
            if match:
                matched = True
                break

        if not matched:
            error_lines.append(line_number)

    if error_lines:
        for line_number in error_lines:
            start_index = f"{line_number}.0"
            end_index = f"{line_number + 1}.0"
            text_area.tag_add("error", start_index, end_index)

    text_area.tag_config("error", background="red")

    # Display the error count
    error_count = len(error_lines)
    error_count_label.config(text=f" {error_count} Invalid Formats")

# Create the main window
root = tk.Tk()
root.title("Cham Wings PNL Validator")

# Create a text area for input
text_area = scrolledtext.ScrolledText(root, width=80, height=30)
text_area.pack(padx=10, pady=10)

# Create a button to trigger validation
validate_button = tk.Button(root, text="Validate", command=validate_text)
validate_button.pack(padx=10, pady=5)

# Create a label to display the error count
error_count_label = tk.Label(root, text="", fg="red")
error_count_label.pack(pady=5)

# Run the Tkinter main loop
root.mainloop()