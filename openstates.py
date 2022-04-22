import requests


class openStates:
    def __init__(self, apikey):
        self.apikey = apikey

    def search_people(self, name):
        names_list = []
        dict = {}

        self.name = name

        headers = {
            "accept": "application/json",
        }

        params = {
            "name": self.name,
            "page": "1",
            "per_page": "50",
            "apikey": self.apikey,
        }

        openstates_api = requests.get(
            "https://v3.openstates.org/people", headers=headers, params=params
        )

        jsonResponse = openstates_api.json()
        response = jsonResponse["results"]

        length = jsonResponse["pagination"]["max_page"] + 1
        for page in range(2, length):
            headers = {
                "accept": "application/json",
            }

            params = {
                "name": name,
                "page": {page},
                "per_page": "50",
                "apikey": self.apikey,
            }

            openstates_api = requests.get(
                "https://v3.openstates.org/people", headers=headers, params=params
            )
            jsonResponse = openstates_api.json()
            response.extend(jsonResponse["results"])

        # length = len(response)

        # for index in range(0, length):
        #     name = response[index]["name"]
        #     state = response[index]["jurisdiction"]["name"]
        #     party = response[index]["party"]
            
        #     dict = {"name": name, "state": state, "party": party}
        #     names_list.append(dict)

        return response

    # [{'id': 'ocd-person/7ec31266-6738-481f-aaf9-c89ff8a7965b', 'name': 'Nick Schroer', 'party': 'Republican', 'current_role': {'title': 'Representative', 'org_classification': 'lower', 'district': '107', 'division_id': 'ocd-division/country:us/state:mo/sldl:107'}, 'jurisdiction': {'id': 'ocd-jurisdiction/country:us/state:mo/government', 'name': 'Missouri', 'classification': 'state'}, 'given_name': 'Nick', 'family_name': 'Schroer', 'image': 'https://house.mo.gov/MemberPhoto.aspx?id=1909', 'email': 'Nick.Schroer@house.mo.gov', 'gender': '', 'birth_date': '', 'death_date': '', 'extras': {'last_name': 'Schroer', 'first_name': 'Nick'}, 'created_at': '2018-10-18T14:50:12.914972+00:00', 'updated_at': '2021-10-08T14:42:35.515156+00:00', 'openstates_url': 'https://openstates.org/person/nick-schroer-3rCBEu0FO6RbwoHdPehtwh/'}]
