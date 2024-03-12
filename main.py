from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[['STANAME                                 ', 'STAID', 'CN']]


@app.route('/')
def home():
    return render_template('home.html', data=stations.to_html())


@app.route('/api/v1/<station>/<date>', methods=['GET'])
def get_temp_by_station_id_and_date(station, date):
    filename = "data/TG_STAID" + str(station.zfill(6) + ".txt")
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10

    return \
        {
            "station": station,
            "date": date,
            "temperature": temperature
        }


@app.route('/api/v1/<station>', methods=['GET'])
def get_temp_list_by_station_id(station):
    filename = "data_small/TG_STAID" + str(station.zfill(6) + ".txt")
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    result = df.to_dict(orient="records")
    return result


@app.route('/api/v1/annual/<station>/<year>', methods=['GET'])
def get_temp_by_station_id_and_year(station, year):
    filename = "data_small/TG_STAID" + str(station.zfill(6) + ".txt")
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[
        df['    DATE'].str.startswith(str(year))
    ].to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True)
