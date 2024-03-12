# historical-weather-data-api
Simple api built with flask which returns weather data

<b> URL format: </b>
    <pre>
        localhost:5000/api/v1/station/date
        localhost:5000/api/v1/station
        localhost:5000/api/v1/annual/station/YYYY
    </pre>
<b> Examples: </b>
    <pre>
        - to get data per station for a certain date: localhost:5000/api/v1/10/1988-10-25
        - to get all data per station: localhost:5000/api/v1/10
        - to get data per station per year: localhost:5000/api/v1/annual/10/1988
    </pre>