#@DiamondFlight on Github

import os
import requests
from datetime import datetime, timezone
import tkinter as tk
from tkinter import messagebox, ttk
from calendar import monthrange
import threading

radarList = ['KABR', 'KENX', 'KABX', 'KAMA', 'PAHG', 'PGUA', 'KFFC', 'KBBX', 'PABC', 'KBLX', 'KBGM', 'PACG', 'KBMX', 'KBIS', 'KFCX', 'KCBX', 'KBOX', 'KBRO', 'KBUF',
             'KCXX', 'RKSG', 'KFDX', 'KCBW', 'KICX', 'KGRK', 'KCLX', 'KRLX', 'KCYS', 'KLOT', 'KILN', 'KCLE', 'KCAE', 'KGWX', 'KCRP', 'KFTG', 'KDMX', 'KDTX', 'KDDC',
             'KDOX', 'KDLH', 'KDYX', 'KEYX', 'KEPZ', 'KLRX', 'KBHX', 'KVWX', 'PAPD', 'KFSX', 'KSRX', 'KFDR', 'KHPX', 'KPOE', 'KEOX', 'KFWS', 'KAPX', 'KGGW', 'KGLD',
             'KMVX', 'KGJX', 'KGRR', 'KTFX', 'KGRB', 'KGSP', 'KUEX', 'KHDX', 'KHGX', 'KHTX', 'KIND', 'KJKL', 'KDGX', 'KJAX', 'RODN', 'PHKM', 'KEAX', 'KBYX', 'PAKC',
             'KMRX', 'RKJK', 'KARX', 'KLCH', 'KLGX', 'KESX', 'KDFX', 'KILX', 'KLZK', 'KVTX', 'KLVX', 'KLBB', 'KMQT', 'KMXX', 'KMAX', 'KMLB', 'KNQA', 'KAMX', 'PAIH',
             'KMAF', 'KMKX', 'KMPX', 'KMBX', 'KMSX', 'KMOB', 'PHMO', 'KTYX', 'KVAX', 'KMHX', 'KOHX', 'KLIX', 'KOKX', 'PAEC', 'KLNX', 'KIWX', 'KEVX', 'KTLX', 'KOAX',
             'KPAH', 'KPDT', 'KDIX', 'KIWA', 'KPBZ', 'KSFX', 'KGYX', 'KRTX', 'KPUX', 'KDVN', 'KRAX', 'KUDX', 'KRGX', 'KRIW', 'KJGX', 'KDAX', 'KMTX', 'KSJT', 'KEWX',
             'KNKX', 'KMUX', 'KHNX', 'TJUA', 'KSOX', 'KATX', 'KSHV', 'KFSD', 'PHKI', 'PHWA', 'KOTX', 'KSGF', 'KLSX', 'KCCX', 'KLWX', 'KTLH', 'KTBW', 'KTWX', 'KEMX',
             'KINX', 'KVNX', 'KVBX', 'KAKQ', 'KICT', 'KLTX', 'KYUX']

def getUTCTime():
    return datetime.now(timezone.utc)

def getCurrentYear():
    return int(str(datetime.now(timezone.utc))[:4])

def getCurrentMonth():
    return int(str(datetime.now(timezone.utc))[5:7])

def getCurrentDay():
    return int(str(datetime.now(timezone.utc))[8:10])

def getCurrentHour():
    return int(str(datetime.now(timezone.utc))[11:13])

def getCurrentMinute():
    return int(str(datetime.now(timezone.utc))[14:16])

def m(n):
    if int(n) < 10:
        return str("0"+n)
    else:
        return str(n)

def year_box_change(event):
    modifyBox("month", mDDown)
    modifyBox("day", dDDown)
    modifyBox("hour", hDDown)

def month_box_change(event):
    modifyBox("day", dDDown)
    modifyBox("hour", hDDown)

def day_box_change(event):
    modifyBox("hour", hDDown)

def radar_box_change(event):
    modifyBox("hour",hDDown)

def modifyBox(typ="month",box=None):
    if box == None: print("ERROR")
    if typ=="month":
        box['values'] = returnData("month",int(yDDown.get()))
    elif typ=="day":
        box['values'] = returnData("day",str(yDDown.get() + "" + mDDown.get()))
    elif typ=="radar":
        box['values'] = returnData("radar",str(year_entry+""+month_entry+""+day_entry))
    elif typ=="hour":
        d = returnData("hour",str(yDDown.get() +""+ mDDown.get() +""+ dDDown.get()))

        if d == ["Null"]:
            box.set('Null')
            box['values'] = ["Null"]
        else:
            box['values'] = d
        

def returnData(typ="year", eData=0):
    rTable = []
    
    if typ == "year":
        eYear = getUTCTime()
        eYear = int(str(eYear)[:4])

        it = 1990

        while it < eYear:
            it += 1

            rTable.append(it)
        return rTable
    elif typ == "month":
        eMonth = 12
        if eData == int(getCurrentYear()):
            eMonth = getUTCTime()
            eMonth = int(str(eMonth)[5:7])

            if int(eMonth) > int(getCurrentMonth()):
                eMonth = int(getCurrentMonth())
                mDDown.set(str(eMonth-1))
                

        it = 0

        while it < eMonth:
            it += 1

            rTable.append(it)
        print(eData)
        if int(eData) == 1991:
            rTable = [6,7,8,9,10,11,12]
        return rTable
    elif typ=="day":
        
        n = datetime(getCurrentYear(), getCurrentMonth(), getCurrentDay())
        eDay = monthrange(int(str(eData)[:4]), int(str(eData)[4:]))[1]

        if eData == (str(int(getCurrentYear())) + str(int(getCurrentMonth()))):
            eDay = datetime(getCurrentYear(), getCurrentMonth(), getCurrentDay())
            eDay = int(str(eDay)[8:10])

        it = 0

        while it < eDay:
            it += 1
            rTable.append(it)
        return rTable
    elif typ=="radar":
        i = 0
        t = """for x in radarList:
            i+=1
            print(f"Checking Radars, Please Wait:\n[{i*'/'}{(len(radarList)-i)*'-'}] {i}/{len(radarList)}")
            url = f"https://www.ncdc.noaa.gov/nexradinv/bdp-download.jsp?id={x}&yyyy={yDDown.get()}&mm={m(mDDown.get())}&dd={m(dDDown.get())}&product=AAL2"

            try:
                response = requests.get(url, timeout=0.00001)
            except requests.exceptions.Timeout:
                print(f"Failed to locate Data for Site {x}")
                continue

            if response.status_code == 200:
                rTable.append(x)

        if len(rTable) == 0:
            rTable = ["Null"]
            rDDown.set("Null")"""
        return radarList
    elif typ=='hour':
        n = datetime(getCurrentYear(), getCurrentMonth(), getCurrentDay(), getCurrentHour(), getCurrentMinute())
        eHAM = 2359

        print(eData)

        if eData == (str(int(getCurrentYear())) + str(int(getCurrentMonth())) + str(int(getCurrentDay()))):
            eHAM = int((str(n)[11:13])+(str(n)[14:16]))
        it = 0

        url = f"https://www.ncdc.noaa.gov/nexradinv/bdp-download.jsp?id={radar_site}&yyyy={yDDown.get()}&mm={m(mDDown.get())}&dd={m(dDDown.get())}&product=AAL2"

        response = requests.get(url)


        if response.status_code == 200:
            html_content = response.text

            file_names = [filename.strip() for filename in html_content.split() if filename.startswith(f"{radar_site}{yDDown.get()}{m(mDDown.get())}{m(dDDown.get())}")]

            if len(file_names) == 0:
                print("No Records Found!")
                rTable = ["Null"]
            else:
                for fn in file_names:
                    rTable.append(str(fn.split("_")[1])[:6])
        return rTable

class DropDownGui:
    def __init__(self, Info, row, column, textLbl):
        self.info = Info
        self.row = row
        self.column = column
        self.textLbl = textLbl

    def __load__(self):
        tk.Label(root, text=self.textLbl).grid(row=self.row, column=self.column, sticky="w")
        comb = ttk.Combobox(values=self.info)
        comb.grid(row=self.row, column=self.column+1)
        comb.current(0)
        
        return comb
        

def download_nexrad_files(radar_site, year, month, day, hour, output_directory, stop_after_24):
    # Format the URL with the provided parameters
    url = f"https://www.ncdc.noaa.gov/nexradinv/bdp-download.jsp?id={radar_site}&yyyy={year}&mm={month}&dd={day}&product=AAL2"
    print(url)
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the HTML content
        html_content = response.text
        # Find all occurrences of file names in the HTML content
        file_names = [filename.strip() for filename in html_content.split() if filename.startswith(f"{radar_site}{year}{month}{day}")]

        # Create a directory to save the files if it doesn't exist
        directory = os.path.join(output_directory, f"{radar_site}_{year}{month}{day}")
        if not os.path.exists(directory):
            os.makedirs(directory)
        print(f"Downloading files to directory: {directory}")

        # Download each file
        scan_count = 0  # Counter for the number of scans downloaded
        for file_name in file_names:
            try:
                # Extract the timestamp from the file name
                timestamp_str = file_name.split('_')[1][:6]  # Extract HHMMSS
                # Convert the timestamp string to a datetime object
                timestamp = datetime.strptime(timestamp_str, '%H%M%S')
                # Convert the specified hour to a datetime object
                specified_hour = datetime.strptime(str(hour), '%H%M%S')
                # Compare the timestamp with the specified hour
                if timestamp >= specified_hour:
                    # Construct the file URL
                    file_url = f"https://noaa-nexrad-level2.s3.amazonaws.com/{year}/{month}/{day}/{radar_site}/{file_name}"
                    # Create the full file path
                    file_path = os.path.join(directory, file_name)
                    #print(f"Downloading file: {file_name} from {file_url}")  # Print download info
                    print(f"Downloading Files, Please Wait:\n[{scan_count*'/'}{(len(file_names)-scan_count)*'-'}] {scan_count}/{len(file_names)}")
                    try:
                        # Download the file using requests
                        file_response = requests.get(file_url)
                        
                        with open(file_path, 'wb') as file:
                            file.write(file_response.content)
                        #print(f"Downloaded {file_name}")
                        #print(f"Saved at: {file_path}")  # Print the full file path
                        scan_count += 1  # Increment the scan counter
                        if stop_after_24 and scan_count >= 24:
                            print("Stopped downloading after 24 scans.")
                            break  # Exit the loop if stop_after_24 is True and 24 scans are downloaded
                    except Exception as e:
                        print(f"Error downloading {file_name}: {e}")
            except IndexError:
                print(f"Skipping file {file_name}: Unable to extract timestamp from filename")
    else:
        print("Failed to retrieve data from the server.")

def download_files():
    radar_site = rDDown.get()
    year = str(yDDown.get())
    month = m(mDDown.get())
    day = m(dDDown.get())
    hour = hDDown.get()
    output_directory = output_var.get()
    stop_after_24 = stop_after_24_var.get()
    download_nexrad_files(radar_site, year, month, day, hour, output_directory, stop_after_24)

def exit_program():
    answer = messagebox.askyesno("Exit", "Do you want to exit the program?")
    if answer:
        root.destroy()

root = tk.Tk()
root.title("Nexrad Downloader")

radar_site = "KTLX"
# Create labels and entry widgets
yDDown = DropDownGui(returnData("year"), 0, 0, "Year: ").__load__()
year_entry = yDDown.get()

mDDown = DropDownGui(returnData("month",year_entry),1,0,"Month: ").__load__()
month_entry = mDDown.get()

dDDown = DropDownGui(returnData("day",str(year_entry+""+month_entry)),2,0,"Day: ").__load__()
day_entry = dDDown.get()

rDDown = DropDownGui(returnData("radar",str(year_entry+""+month_entry+""+day_entry)),3,0,"Radar Site: ").__load__()
radar_entry = rDDown.get()

hDDown = DropDownGui(returnData("hour",str(year_entry+""+month_entry+""+day_entry)),4,0,"Hour Start: ").__load__()
hour_entry = hDDown.get()




yDDown.validate = "all"
yDDown.validatecommand = modifyBox("month", mDDown)
yDDown.bind("<<ComboboxSelected>>", year_box_change)

mDDown.validate = "all"
mDDown.validatecommand = modifyBox("day", dDDown)
mDDown.bind("<<ComboboxSelected>>", month_box_change)

rDDown.validate = "all"
rDDown.validatecommand = modifyBox("radar", dDDown)
rDDown.bind("<<ComboboxSelected>>", radar_box_change)

dDDown.validate = "all"
dDDown.validatecommand = modifyBox("day", hDDown)
dDDown.bind("<<ComboboxSelected>>", day_box_change)


tk.Label(root, text="Output Directory:").grid(row=5, column=0, sticky="w")
output_var = tk.StringVar()
output_entry = tk.Entry(root, textvariable=output_var)
output_entry.grid(row=5, column=1)

# Create checkbox for stop after 24 scans
stop_after_24_var = tk.BooleanVar()
stop_after_24_checkbox = tk.Checkbutton(root, text="Stop after 24 scans", variable=stop_after_24_var)
stop_after_24_checkbox.grid(row=6, column=0, columnspan=2)

# Create download and exit buttons
download_btn = tk.Button(root, text="Download Files", command=download_files)
download_btn.grid(row=7, column=0, columnspan=2, pady=10)

exit_btn = tk.Button(root, text="Exit", command=exit_program)
exit_btn.grid(row=8, column=0, columnspan=2)

# Create label for hour display
hour_display = tk.Label(root, text="Hour= HHMMSS (UTC)\n If it stops responding, it's probably downloading\n Will make a folder where the .py is if a directory is not specified", anchor="e", padx=10)
hour_display.grid(row=0, column=2, rowspan=9, sticky="ns")



root.mainloop()
