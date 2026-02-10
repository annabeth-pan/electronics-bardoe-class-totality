import network
import time
import urequests

SSID="GalaxyS248708"
PASSWORD="xrucs332pxce5dt"

def connect_wifi(wlan, ssid, password, max_s = 15):
    wlan.active(True)
    wlan.connect(ssid, password)
    
    attempts = 1
    start = time.ticks_ms()

    while not wlan.isconnected():
        print(f"connecting || attempt {attempts} || status: {wlan.status()}")
        
        if time.ticks_diff(time.ticks_ms(),  start) > max_s*1000:
            print(f"Failed to connect within {max_s}. Timed out.")
            wlan.active(False)
            return False;
        if wlan.status() == -1:
            print(f"Connection failed.")
            return False
        if wlan.status() == -2:
            print(f"Network doesn't exist.")
            return False
        if wlan.status() == -3:
            print(f"Wrong password.")
            return False
        
        attempts += 1
        time.sleep(1)

    print(f"----------  Connected after {time.ticks_diff(time.ticks_ms(),  start)} ms")
    print(f"Network config: {wlan.ifconfig()}")
    return True

wlan=network.WLAN(network.STA_IF)
wlan.active(False)
if(connect_wifi(wlan, SSID, PASSWORD, 30)):
    url = "https://api.open-meteo.com/v1/forecast?latitude=39.96&longitude=83.00&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,apparent_temperature" 
    try:
        response = urequests.get(url)
        if response.status_code == 200:
            weatherdata = json.loads(response.text)
            print("API Data Pulled")
        else:
            print(f"Error: API request failed with status code {response.status_code}")
        response.close()
    except Exception as e:
        print("An error occurred:", e)

    print(f"It is currently {weatherdata.time}, and {weatherdata.temperature} (feels like {weatherdata.apparent_temperature} degrees outside in Columbus, OH.")

wlan.active(False)