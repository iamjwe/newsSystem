class News:
    def __init__(self, id=None, newsid=None, is_release=None, browse_count=None):
        self.__id = id
        self.__newsid = newsid
        self.__is_release = is_release
        self.__browse_count = browse_count


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def newsid(self):
        return self.__newsid

    @newsid.setter
    def newsid(self, value):
        self.__newsid = value

    @property
    def is_release(self):
        return self.__is_release

    @is_release.setter
    def is_release(self, value):
        self.__is_release = value

    @property
    def browse_count(self):
        return self.__browse_count

    @browse_count.setter
    def browse_count(self, value):
        self.__browse_count = value


class NewsDetail:

    def __init__(self, newsid=None,title=None,content=None):
        self.__newsid = newsid
        self.__title = title
        self.__content = content

    def __str__(self):
        return self

    @property
    def newsid(self):
        return self.__newsid

    @newsid.setter
    def newsid(self, value):
        self.__newsid = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value
