import os
import json
script_dir = os.path.dirname(os.path.dirname(__file__))


def save_json(data, page) -> None:
    totGet = data["data"]["reportData"]["reports"]["per_page"] * page
    totLeft = data["data"]["reportData"]["reports"]["total"] - totGet
    print("Saved Page: " + str(page) + " Total: " + str(totGet) + " Remaining: " + str(totLeft))
    currFile = "\\scans\\" + "scan_" + str(page) + ".json"
    with open(script_dir + currFile, "w") as f:
        f.write(json.dumps(data, indent=2))


def json_to_html_table(json_data) -> None:
    html = ""

    for item in json_data["data"]["reportData"]["reports"]["data"]:
        code = item["code"]
        fights = item['fights']
        html += f"""<tr>
                <td><a href="https://classic.warcraftlogs.com/reports/{code}">{code}</a></td>
                <td></td>
                <td></td>
                <td></td>
                """
        for fight in fights:
            if not fight["encounterID"] == 0:
                name = fight["name"]
                bossPercentage = round(fight["bossPercentage"])
                encounterID = fight["encounterID"]
                kill = fight["kill"]
                if kill is True:
                    html += f"""<tr>
                                <td></td>
                                <td style="text-align: right;">{encounterID}</td>
                                <td style="color:green">{name}</td>
                                <td></td>
                            </tr>"""
                elif kill is False:
                    html += f"""<tr>
                                <td></td>
                                <td style="text-align: right;">{encounterID}</td>
                                <td style="color:red">{name} ({bossPercentage}%)</td>
                                <td><div style="width: 100%;background-color: #f44336!important;height:24px;width:{bossPercentage}%">{bossPercentage}</td>
                            </tr>"""
    return html
