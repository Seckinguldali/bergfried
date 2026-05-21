# Bergfried
Open-source fleet monitoring for small-scale operations.

## Dataflow
```Mermaid
graph TD
A[Data Collection] --> B[Data Clean Up]
B --> C[Short Term Storage]
C --> D[Data Transmission]
D --> E[Data Processing and Analysis]
E --> F[User Interface]
```

>Data Collection in sensors and devices
>Data clean up on device
>Short term storage on device
>Data transmission to central server and cloud platform
>Data storage on central server and cloud platform
>Data processing and analysis on server
>User interface for monitoring and reporting

1. **Data Collection**: Sensors and devices installed on assets collect real-time data such as location, speed, altitute, temperature, and other relevant metrics.
2. **Data Clean Up**: The collected data is cleaned and preprocessed on the device to ensure accuracy and consistency. (e.g., removing outliers, weeding redundant data)
3. **Short Term Storage**: Preprocessed data is stored temporarily on the device until it is confirmed that it is transmitted successfully to the central server.
4. **Data Transmission**: The stored data is transmitted to a central server and cloud platform (if there is one).
5. **Data Storage on Central Server and Cloud Platform**: The transmitted data is stored securely on the central server and cloud platform.
6. **Data Processing and Analysis**: The data is processed and analyzed on the server to generate insights, daily reports, warnings, and other relevant information for fleet monitoring.
7. **User Interface and reporting**: A UI is provided for users to monitor their assets in real-time, view historical data, and generate custom reports based on their needs.

## Features
- Real-time tracking of assets
- Historical data analysis and reporting
- User-friendly interface for easy navigation
- Integration with existing systems and sensors

## Technology Stack
- **OSes**: Alpine Linux for devices, Debian for servers
- **Programming Languages**: Python for data processing and analysis, JavaScript for user interface development
- **Databases**: PostgreSQL for data storage
- **Cloud Services**: Supabase for cloud storage and backend services

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## Issue Tracking
Please use the issue tracker to report bugs, suggest features, or ask questions.