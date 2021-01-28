from Color import color

from GET_PATH import get_path as start

'''
start의 첫번째인자는 Slack Channel 디렉터리 들이 모여있는 폴더를 작성해주시면 됩니다.
start의 두번째 인자는 보기 원하는 채널을 작성해주세요
단, 리스트 규격은 지켜주세요
(만일 아무것도 적지 않을 시 모든 채널을 출력합니다.
'''
top = None # Slack Channel 디렉터리 들이 모여있는 폴더를 작성해주시면 됩니다.
second_parameter = [] # 보기 원하는 채널 작성

start(top,second_parameter)

'''
회사에서 잠깐 할 게 있어서 만들었다..
슬랙 채널 복구를 원하면

https://slack.com/intl/ko-kr/help/articles/217872578-%ED%95%9C-Slack-%EC%9B%8C%ED[…]%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0

이곳의 글을 참조하면 된다.

나는 그냥 재미로 만들었고 별로 중요한 시스템은 아니지만
프로그램을 짜본다는 경험은 언제나 좋다.
끝
'''