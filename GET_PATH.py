import os
from Color import color
from JSONDATACLASS import JSONDATA

class get_path:

    def __init__(self, top_path, channel=[]):

        '''
        top_path 설정을 해준다.
        :param top_path: slack channel 디렉터리 모아둔 폴더
        '''

        self.top_path = top_path

        if not channel:
            # channel 비어있으면 = 모두 검사
            self.Top_Diretory = os.listdir(self.top_path)
        else:
            self.Top_Diretory = channel

        self.channel_paths = None
        self.json_files = None
        self.Dates = dict()
        self.Each_Json_file = dict()
        self.run()

    def SET_CHANNEL_PATH(self):
        # GET Channel_PATH
        self.channel_paths = \
            [self.top_path + "/" + each_Directory
             for each_Directory in self.Top_Diretory
             if ".ipynb_checkpoints" not in each_Directory]

    def GET_FILES_IN_CHANNEL(self):
        # GET JSON FILE EACH PATH
        self.json_files = \
            {key: os.listdir(key) for key in self.channel_paths}

    def GET_DATES_FROM_FILE(self):
        # GET DATES INFO
        for key, value in self.json_files.items():
            channel_date = [fordate[0:10] for fordate in value]
            self.Dates[key] = channel_date

    def SET_JSON_DATAS(self):

        for key, value in self.json_files.items():
            self.Each_Json_file[key] = JSONDATA(value, key)

    def run(self):
        self.SET_CHANNEL_PATH()
        self.GET_FILES_IN_CHANNEL()
        self.GET_DATES_FROM_FILE()
        self.SET_JSON_DATAS()
        self.print()

    def print(self):
        for key, value in self.Each_Json_file.items():

            for Data, Date in zip(value.JSONDATA, self.Dates[key]):
                print(
                    "----------------------------------------------------------------------------------------------------")
                print(color.BOLD + color.RED + Date + color.END + "\n")

                for chat in Data:
                    if 'user_profile' in chat.keys() and 'real_name' in chat['user_profile'].keys():
                        print(color.BOLD + color.BLUE + chat['user_profile'][
                            'real_name'] + color.END + "\n" + color.BOLD + chat['text'] + color.END + "\n")
