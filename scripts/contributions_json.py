"""Write the contribution calendar for every year to contributions.json.

Usage:  GITHUB_TOKEN=... python scripts/contributions_json.py <user> <out.json>
"""
import datetime as dt
import json
import os
import sys
import urllib.request

QUERY = """query($u:String!,$f:DateTime!,$t:DateTime!){user(login:$u){
  contributionsCollection(from:$f,to:$t){contributionCalendar{totalContributions
    weeks{contributionDays{date contributionCount contributionLevel}}}}}}"""
LEVELS = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2, "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}
FIRST_YEAR = 2020


def fetch(user: str, start: str, end: str, token: str) -> dict:
    body = json.dumps({"query": QUERY, "variables": {"u": user, "f": start, "t": end}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", body,
                                 {"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)["data"]["user"]["contributionsCollection"]["contributionCalendar"]


def main(user: str, out: str) -> None:
    token = os.environ["GITHUB_TOKEN"]
    today = dt.date.today()
    years = {}
    for year in range(FIRST_YEAR, today.year + 1):
        cal = fetch(user, f"{year}-01-01T00:00:00Z", f"{year}-12-31T23:59:59Z", token)
        years[str(year)] = {
            "total": cal["totalContributions"],
            "weeks": [[[d["date"], d["contributionCount"], LEVELS[d["contributionLevel"]]]
                       for d in w["contributionDays"]] for w in cal["weeks"]],
        }
    data = {"user": user, "generated": today.isoformat(), "years": years}
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, separators=(",", ":"))
    print(out, {y: v["total"] for y, v in years.items()})


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
