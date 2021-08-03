import json
import base64

# filename = "allcharities.json"
filename = "easiermethod.json"

with open(filename) as f:
    data = json.load(f)

charity_info = data["charityInfosData"]

# with open("allcharityIDs.txt","w+") as out:
with open("ipcIDs.txt","w+") as out:
    index = 0
    for i in charity_info:
        # name = charity_info["CharityIPCName"]
        id = charity_info[index]["CharityAccountCRMRecordID"]
        id_encoded = base64.b64encode(id.encode("utf-8"))
        out.write(str(id_encoded,"utf-8") + "\n")
        index += 1