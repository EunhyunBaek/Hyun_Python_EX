import  logging
import  logging.config
logging.config.fileConfig('logging_conf')
"""
#콘솔 출력용 핸들러 생성
handler = logging.StreamHandler()
# 포매터 생성
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s - %(message)s')
#핸들러에 포매터 설정
handler.setFormatter(formatter)

#로거 생성 및 로그 레벨 설정
logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
"""
#로그 메시지 출력
logging.debug('이 메시지는 개발자만 이해해요.')
logging.info('생각대로 동작 하고 있어요.')
logging.warning('곧 문제가 생길 가능성이 높습니다.')
logging.error('문제가 생겼어요. 기능이 동작 안해요.')
logging.critical('시스템이 다운됩니다!')
