import pandas as pd
marker = pd.read_excel('support/GKTW_Markers.xlsx')
distanceMatrix = pd.read_excel('support/Zone Distance_Time Matrix .xlsx')

def zoneLookUp(start, dest):
    startZone = marker[marker['Name'].str.contains(start)].Zones.item()
    destZone = marker[marker['Name'].str.contains(dest)].Zones.item()
    time = distanceMatrix.loc[distanceMatrix['Zones'] == startZone, destZone].item()
    return time