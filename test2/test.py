import requests
import unittest

class TestAPI(unittest.TestCase):
    def test_api(self):
        #GET landing page
        response = requests.get("https://clarity.dexcom.com")
        assert response.status_code == 200
        #GET login page
        response = requests.get("https://clarity.dexcom.com/users/auth/dexcom_sts", allow_redirects=False)
        url = response.headers['location']
        #redirect, GET authorization
        response = requests.get(url, allow_redirects=False)
        url = response.headers['location']
        print(response.headers['location'])
        #redirect, GET login authorization finally and show login screen
        response = requests.get(url, allow_redirects=False)
        print(response.content)


if __name__ == "__main__":
    unittest.main()