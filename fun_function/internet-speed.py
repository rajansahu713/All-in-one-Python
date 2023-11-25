import speedtest

wifi  = speedtest.Speedtest()

print("Wifi Download Speed is ", wifi.download())

print("Wifi Upload Speed is ", wifi.upload())

print("Wifi Ping is ", wifi.results.ping)

print("Wifi Server is ", wifi.results.server)

print("Wifi Timestamp is ", wifi.results.timestamp)
