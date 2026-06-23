import os

# 搜索关键词
KEYWORDS = [
    "GNSS", "multi-GNSS", "RTK", "PPP", "PPP-RTK",
    "multi-sensor fusion navigation", "GNSS/IMU integration",
    "GNSS LiDAR", "GNSS visual", "GNSS+INS",
    "SLAM", "visual SLAM", "LiDAR SLAM", "factor graph",
    "autonomous driving localization", "urban navigation",
    "deep learning navigation",
    "inertial navigation", "Kalman filter", "sensor fusion",
    "point cloud registration", "ICP",
    "ORB-SLAM", "LOAM", "LIO-SAM", "FAST-LIO",
    "GPS Solutions", "Journal of Geodesy",
]

# arXiv 分类
ARXIV_CATEGORIES = [
    "cs.RO", "cs.CV", "cs.AI", "cs.LG",
    "eess.SP", "eess.SY",
    "physics.geo-ph", "math.OC",
]

# IEEE 搜索关键词
IEEE_KEYWORDS = [
    "GNSS", "GPS", "inertial navigation", "sensor fusion",
    "SLAM", "autonomous driving localization",
    "multi-sensor fusion navigation",
]

# 期刊 RSS 源
JOURNAL_FEEDS = {
    "GPS Solutions":
        "https://link.springer.com/search.rss?facet-content-type=Article"
        "&facet-journal-id=10291",
    "Journal of Geodesy":
        "https://link.springer.com/search.rss?facet-content-type=Article"
        "&facet-journal-id=190",
}

# LLM 配置
LLM_PROVIDER = "gemini"
LLM_API_KEY = os.environ.get("LLM_API_KEY", "")
LLM_MODEL = "gemini-2.0-flash"

# IEEE 配置
IEEE_API_KEY = os.environ.get("IEEE_API_KEY", "")

# 通知配置 (暂不启用)
NOTIFICATION_ENABLED = False
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")
WECHAT_WEBHOOK = os.environ.get("WECHAT_WEBHOOK", "")

# 输出配置
OUTPUT_DIR = "output"
MAX_PAPERS_PER_SOURCE = 20
MAX_TOTAL_PAPERS = 50
