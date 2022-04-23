import requests


class openStates:

    # TODO:: #2 Make Missouri the default state for people searches

    def __init__(self, apikey):
        self.apikey = apikey

    def search_people(self, name):

        # TODO: #3 Add more examples of responses

        # sample response from people query

        # [{'id': 'ocd-person/7529d2d2-0cc1-4d30-9e8f-12d3773dff8d', 'name': 'Cody Smith', 'party': 'Republican', 'current_role': {'title': 'Representative', 'org_classification': 'lower', 'district': '163', 'division_id': 'ocd-division/country:us/state:mo/sldl:163'}, 'jurisdiction': {'id': 'ocd-jurisdiction/country:us/state:mo/government', 'name': 'Missouri', 'classification': 'state'}, 'given_name': 'Cody', 'family_name': 'Smith', 'image': 'https://house.mo.gov/MemberPhoto.aspx?id=1945', 'email': 'Cody.Smith@house.mo.gov', 'gender': '', 'birth_date': '', 'death_date': '', 'extras': {'last_name': 'Smith', 'first_name': 'Cody'}, 'created_at': '2018-10-18T14:50:03.411887+00:00', 'updated_at': '2022-01-18T19:14:48.394654+00:00', 'openstates_url': 'https://openstates.org/person/cody-smith-3Z5DMzR5JXS1p9YheB8WBp/'}, {'id': 'ocd-person/c8f4ccf3-c7c4-4e71-8226-6ee92bdf501e', 'name': 'David Smith', 'party': 'Democratic', 'current_role': {'title': 'Representative', 'org_classification': 'lower', 'district': '45', 'division_id': 'ocd-division/country:us/state:mo/sldl:45'}, 'jurisdiction': {'id': 'ocd-jurisdiction/country:us/state:mo/government', 'name': 'Missouri', 'classification': 'state'}, 'given_name': 'David', 'family_name': 'Smith', 'image': 'https://house.mo.gov/MemberPhoto.aspx?id=2290', 'email': '', 'gender': '', 'birth_date': '', 'death_date': '', 'extras': {'last_name': 'Smith', 'first_name': 'David'}, 'created_at': '2021-04-12T20:36:19.250884+00:00', 'updated_at': '2021-12-16T18:58:02.288806+00:00', 'openstates_url': 'https://openstates.org/person/david-smith-67CL3LrJDWc3Nd74p76TgU/'}, {'id': 'ocd-person/0c9efb98-e995-4927-a2c1-ee627a5faf0a', 'name': 'Neil Smith', 'party': 'Democratic', 'current_role': {'title': 'Representative', 'org_classification': 'lower', 'district': '67', 'division_id': 'ocd-division/country:us/state:mo/sldl:67'}, 'jurisdiction': {'id': 'ocd-jurisdiction/country:us/state:mo/government', 'name': 'Missouri', 'classification': 'state'}, 'given_name': 'Neil', 'family_name': 'Smith', 'image': 'https://house.mo.gov/MemberPhoto.aspx?id=2223', 'email': '', 'gender': '', 'birth_date': '', 'death_date': '', 'extras': {}, 'created_at': '2021-01-08T00:10:43.128377+00:00', 'updated_at': '2021-12-16T18:57:50.794324+00:00', 'openstates_url': 'https://openstates.org/person/neil-smith-NoYvCOja2EjTGL6DBOGlO/'}, {'id': 'ocd-person/74efb08b-f153-4d63-b6d6-c685d6a04790', 'name': 'Travis Smith', 'party': 'Republican', 'current_role': {'title': 'Representative', 'org_classification': 'lower', 'district': '155', 'division_id': 'ocd-division/country:us/state:mo/sldl:155'}, 'jurisdiction': {'id': 'ocd-jurisdiction/country:us/state:mo/government', 'name': 'Missouri', 'classification': 'state'}, 'given_name': 'Travis', 'family_name': 'Smith', 'image': 'https://house.mo.gov/MemberPhoto.aspx?id=2239', 'email': '', 'gender': '', 'birth_date': '', 'death_date': '', 'extras': {}, 'created_at': '2021-01-08T00:10:43.293248+00:00', 'updated_at': '2022-01-18T19:15:38.819031+00:00', 'openstates_url': 'https://openstates.org/person/travis-smith-3YeeCRrk8avvhGpmFltoWm/'}]

        dict = {}

        self.name = name

        headers = {
            "accept": "application/json",
        }

        # Setting jurisdiction to Missouri so only Missouri people are returned

        params = {
            "jurisdiction": "ocd-jurisdiction/country:us/state:mo/government",
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

        return response
