# Weather Forecast Application

This project is a Python application that allows users to search for weather forecasts in various Japanese cities. Users can interact with a map of Japan to click on a city and retrieve the current weather information using a free weather API.

## Project Structure

```
Weather
├── app
│   ├── main.py               # Entry point of the application
│   ├── api
│   │   └── weather_api.py    # Functions to interact with the weather API
│   ├── utils
│   │   └── map_click_handler.py # Utility functions for handling map clicks
│   └── templates
│       └── index.html        # HTML template for the user interface
├── Dockerfile                 # Dockerfile to build the application image
├── requirements.txt           # Python dependencies for the project
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd Weather
   ```

2. **Build the Docker image:**
   ```
   docker build -t weather-app .
   ```

3. **Run the Docker container:**
   ```
   docker run -p 5000:5000 weather-app
   ```

4. **Access the application:**
   Open your web browser and go to `http://localhost:5000`.

## Usage

- Click on the map of Japan to select a city.
- The application will display the current weather information for the selected city.

## Dependencies

This project requires the following Python packages, which are listed in `requirements.txt`:

- Flask
- Requests
- Any other necessary libraries for handling API requests and map interactions.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.