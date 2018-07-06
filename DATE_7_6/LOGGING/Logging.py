import logging

logging.warning("조심")
logging.info('정보 확인 요!')            #출력되지 않음. 파이썬의 기본 로거는 root 이며,
                                           # 로그 레벨은 Warining 이므로 낮은 레벨인 Info, debug는 출력

logging.root.setLevel(logging.DEBUG)        #로그 레벨 변경
logging.info('정보 확인 바람!')

logger = logging.getLogger(__name__)
logger.warn('문제가 생길지도 모름')