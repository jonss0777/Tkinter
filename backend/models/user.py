
class User:
    def __init__(self):
        self.__email = ""
        self.__username = ""
        self.__password = ""
        self.__description = ""
        self.__rank = ""
        self.__bestScore = ""
        self.__friendList = ""
        self.__friendRequestList = ""

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email  = email

    def getUsername(self):
        return self.__username

    def setUsername(self, username):
        self.__email = username

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password

    def getDescription(self):
        return self.__description

    def setDescription(self, description):
        self.__description = description

    def getRank(self):
        return self.__rank

    def setRank(self, rank):
        self.__rank = rank

    def getScore(self):
        return self.__bestScore

    def setScore(self, bestScore):
        self.__bestScore = bestScore

    def getFriendList(self):
        return self.__friendList

    def setFriendList(self, friendList):
        self.__friendList = friendList

    def getFriendRequestList(self):
        return self.__friendRequestList

    def setFriendRequestList(self, friendRequestList):
        self.__friendRequestList = friendRequestList