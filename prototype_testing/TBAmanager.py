import requests

class TBAmanager:
    """
    This class is used to manage the connection to the TBA API. It is the parent class of all other classes in this package.
    """
    # Static Methods
    @staticmethod
    def __findEvents_inCountry(country, eventList):
        if (len(eventList) == 0):
            return []
        elif (country.lower() == eventList[0]["country"].lower()):
            return [eventList[0]] + TBAmanager.__findEvents_inCountry(country, eventList[1:])
    
    # Class Methods 
    
    # Constructor 
    def __init__(self, authKey):
        """
        Constructor for TBAmanager, use your TBA API token to create an instance of this class.

        Args:
            authKey (string): Get your TBA API token from https://www.thebluealliance.com/account
        """
        self.__url = "https://www.thebluealliance.com/api/v3"
        self.__header = {"X-TBA-Auth-Key": authKey}
        
    # Instance Methods
    def testStatus(self, statusCode = False):
        """_summary_
        Test the connecrtion to the TBA API.
        
        Args:
            statusCode (bool, optional): Set to True in order to print the status code. Defaults to False.

        Returns:
            int: status code of the request, 200 means success
            dict: json response from the request
        """
        if (statusCode):
            return requests.get(self.__url + "/status", headers=self.__header).status_code
        else:
            return requests.get(self.__url + "/status", headers=self.__header).json()
    
    def listEvents_inCountry(self, year, country, printData = False):
        """_summary_
        List all events in a given country for a given year.

        Args:
            year (int): The year you want to list events for.
            country (string): The country you want to list events for.
            printData (bool, optional): Set to True in order to print the data. Defaults to False.

        Returns:
            list: A list of event keys for the given year.
        """
        eventList = requests.get(self.__url + f"/events/{year}/simple", headers=self.__header).json()
        
        listByCountry = TBAmanager.__findEvents_inCountry(country, eventList)
        
        if (printData):
            print(listByCountry)
        else:
            return listByCountry