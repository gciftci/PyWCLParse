import os
import json
from src.handle_json import save_json, json_to_html_table
from src.oauth2 import get_token, get_data
from src.graphql import query
script_dir = os.path.dirname(__file__)

if __name__ == "__main__":
    html_start = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
    <table id="myTable">
        <tr class="header">
            <th style="width:auto">Log-Code (URL)</th>
            <th style="width: 10%">Encounter-ID</th>
            <th style="width: 50%">Name of Fight</th>
            <th style="width: 40%">%</th>
        </tr>
        """
    with open(script_dir + "\\page\\index.html", "w") as f:
        f.write(html_start)
    html_content = ""
    html_end = """
        </table>
        </body>
        </html>"""
    get_token()
    currPage = 1
    while True:
        response = get_data(query)
        save_json(response, currPage)
        #with open(script_dir + '\\scans\\scan_0.json') as f:
        #    response = json.load(f)

        html_content = json_to_html_table(response)
        with open(script_dir + "\\page\\index.html", "a") as f:
            f.write(html_content)
        if not (response["data"]["reportData"]["reports"]["has_more_pages"]):
            break
        else:
            currPage += 1
        break # trash
    html = html_start + html_content + html_end
    with open(script_dir + "\\page\\index.html", "a") as f:
        f.write(html_end)
