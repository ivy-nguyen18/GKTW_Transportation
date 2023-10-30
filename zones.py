import pandas as pd
marker = pd.read_excel('GKTW_Markers_2 (1).xlsx')
distanceMatrix = pd.read_excel('Zone Distance_Time Matrix .xlsx')

def zoneLookUp(start, dest):
    startZone = marker[marker['Name'].str.contains(start)].Zones.item()
    destZone = marker[marker['Name'].str.contains(dest)].Zones.item()
    time = distanceMatrix.loc[distanceMatrix['Zones'] == startZone, destZone].item()
    return time