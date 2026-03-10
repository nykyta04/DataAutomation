import pyautogui
import openpyxl
import time
import keyboard

# Disable pyautogui's default failsafe (mouse to corner)
pyautogui.FAILSAFE = False

# Configuration
EXCEL_FILE = "Book2.xlsx"  # Replace with your Excel file path
DELAY_BETWEEN_KEYS = 1.5  # Seconds between each action (adjustable)
COUNTDOWN_SECONDS = 5  # Time you have to switch to the data entry software

# Emergency stop flag
stop_requested = False

def emergency_stop():
    """Called when F12 is pressed"""
    global stop_requested
    stop_requested = True
    print("\n" + "="*50)
    print("F12 PRESSED - EMERGENCY STOP ACTIVATED!")
    print("="*50)

# Set up F12 as emergency stop
keyboard.on_press_key('f12', lambda _: emergency_stop())

def press_key(key, delay=None):
    """Press a key and wait"""
    if stop_requested:
        raise KeyboardInterrupt("Emergency stop requested")
    if delay is None:
        delay = DELAY_BETWEEN_KEYS
    pyautogui.press(key)
    print(f"Pressed: {key}")
    time.sleep(delay)

def type_text(text, delay=None):
    """Type text and wait"""
    if stop_requested:
        raise KeyboardInterrupt("Emergency stop requested")
    if delay is None:
        delay = DELAY_BETWEEN_KEYS
    pyautogui.write(str(text))
    print(f"Typed: {text}")
    time.sleep(delay)

def process_row(value1, value2):
    """Process a single row of data"""
    print(f"\n--- Processing row: {value1} | {value2} ---")
    
    # Type first column value
    type_text(value1)
    time.sleep(0.75)
    # Press F8
    press_key('f8', delay=.75)
    
    # Press END
    press_key('end', delay=.75)
    
    # Press ENTER
    press_key('enter', delay=.2)
    
    # Extra pause before F2
    print("Extra 3-second pause before F2...")
    time.sleep(3)
    
    # Press F2
    press_key('f2')

    # Press ENTER
    press_key('enter',delay=1)
    press_key('enter',delay=.5)
    
    pyautogui.click()
    time.sleep(0.5)
    
    # Press ENTER 33 times (faster delay)
    for i in range(33):
        press_key('enter', delay=0.01)  
    
    # MANUAL PAUSE - Wait for user to press F11
    print("\n" + "="*50)
    print("PAUSED - Position NEW SKU")
    print("Press F11 when ready to continue...")
    print("="*50)
    keyboard.wait('f11')  # Wait until F11 is pressed
    print("F11 pressed - continuing...\n")
    
    # Type second column value
    type_text(value2)
    
    # Press ENTER
    press_key('enter',delay=0.5)
    
    # Press ESC
    press_key('esc')
    
    # Press ENTER 4 times
    for i in range(3):
        print(f"ENTER {i+1}/4")
        press_key('enter', delay=.5)
      # Press ENTER
    press_key('enter',delay=1)
    # Press ESC 2 times
    time.sleep(1.5)
    for i in range(2):
        print(f"ESC {i+1}/2")
        press_key('esc',delay=2.2)
    
    # Press F6
    press_key('f6')
    
    print("--- Row completed ---\n")

def main():
    # Load Excel file
    print(f"Loading Excel file: {EXCEL_FILE}")
    try:
        workbook = openpyxl.load_workbook(EXCEL_FILE)
        sheet = workbook.active
    except FileNotFoundError:
        print(f"ERROR: Could not find {EXCEL_FILE}")
        print("Please update EXCEL_FILE variable with the correct path.")
        return
    
    # Read data from columns A and B
    data_rows = []
    for row in sheet.iter_rows(min_row=1, max_col=2, values_only=True):
        if row[0] is not None and row[1] is not None:  # Skip empty rows
            data_rows.append((row[0], row[1]))
    
    print(f"Found {len(data_rows)} rows to process")
    print("\nFirst few rows:")
    for i, (val1, val2) in enumerate(data_rows[:3]):
        print(f"  Row {i+1}: {val1} | {val2}")
    
    # Countdown before starting
    print(f"\n{'='*50}")
    print("SWITCH TO GSI NOW!")
    print(f"{'='*50}")
    for i in range(COUNTDOWN_SECONDS, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)
    print("STARTING!\n")
    
    # Process each row
    try:
        for i, (value1, value2) in enumerate(data_rows, 1):
            print(f"\n{'='*50}")
            print(f"Processing row {i}/{len(data_rows)}")
            print(f"{'='*50}")
            process_row(value1, value2)
            
            # Pause between rows for safety
            if i < len(data_rows):
                time.sleep(1)
        
        print("\n" + "="*50)
        print("ALL ROWS COMPLETED!")
        print("="*50)
    except KeyboardInterrupt:
        print("\n" + "="*50)
        print("Script stopped by user (F12 pressed)")
        print("="*50)

if __name__ == "__main__":
    # Safety feature: Press F12 to stop the script
    print("SAFETY TIP: Press F12 at any time to immediately stop the script!")
    print()
    main()
