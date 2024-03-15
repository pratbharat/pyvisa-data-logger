# pyvisa-data-logger
Python Script for Data Logging and Measurement using PyVISA for multiple channel
# Multi-Channel Temperature Data Logger
This Python script communicates with measurement instruments using the PyVISA library to log temperature readings from multiple channels over time. It supports instruments connected via GPIB, USB, Ethernet, or other supported interfaces.
## Features
- **Multi-Channel Logging:** Collect temperature readings from multiple channels simultaneously.
- **Flexible Instrument Support:** Works with a wide range of measurement instruments supported by PyVISA.
- **CSV Data Export:** Save collected data to a CSV file for further analysis.
- **Real-Time Plotting:** Plot temperature data in real-time using Matplotlib.
## Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.x
- PyVISA library (`pip install pyvisa`)
- Matplotlib library (`pip install matplotlib`)
## Usage
1. Connect your measurement instruments to your computer via the appropriate interface (GPIB, USB, Ethernet, etc.).
2. Modify the script to configure the instrument settings, such as channel numbers and measurement functions.
3. Run the Python script (`python data_logger.py`) to start logging temperature data.
4. Data will be saved to a CSV file named `example.csv` in the current directory.
5. Monitor temperature readings in real-time using the console output and plotted graphs.
## Configuration
- **Instrument Setup:** Modify the script to configure instrument settings such as channel numbers, measurement functions, and communication parameters.
- **Data Logging Interval:** Adjust the time interval between each data logging iteration using the `time.sleep()` function.
## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.
