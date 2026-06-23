"""
通知模块 — 已实现 Telegram Bot 和 WeChat Bot (企业微信/Server酱)
暂不启用 (NOTIFICATION_ENABLED = False)
"""
import json
from typing import Optional

import requests

from .config import (
    NOTIFICATION_ENABLED,
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID,
    WECHAT_WEBHOOK,
)


def send_telegram(message: str) -> bool:
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return False
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        resp = requests.post(url, json={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message[:4096],
            "parse_mode": "Markdown",
        }, timeout=15)
        return resp.ok
    except Exception:
        return False


def send_wechat(message: str) -> bool:
    if not WECHAT_WEBHOOK:
        return False
    try:
        resp = requests.post(WECHAT_WEBHOOK, json={
            "msgtype": "markdown",
            "markdown": {"content": message},
        }, timeout=15)
        return resp.ok
    except Exception:
        return False


def send_notification(summary_text: str, date_str: str) -> None:
    if not NOTIFICATION_ENABLED:
        return
    message = f"📄 每日文献速递 {date_str}\n\n{summary_text[:3000]}"
    send_telegram(message)
    send_wechat(message)
