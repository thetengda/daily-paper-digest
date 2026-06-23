# Daily GNSS Digest

GNSS / 多源融合导航 / SLAM / 自动驾驶 相关文献每日自动检索与摘要。

## 功能

- 每日自动搜索 arXiv、IEEE、Springer 期刊的最新论文
- 使用 Google Gemini AI 生成中文摘要
- 自动提交到 GitHub，生成 Markdown 报告
- 支持 Telegram / 企业微信通知（可选）

## 使用方法

### 1. 注册 Google Gemini API Key（免费）

1. 访问 https://aistudio.google.com/apikey
2. 点击 "Create API Key"
3. 复制生成的 API Key

### 2. 配置 GitHub Secrets

在 GitHub 仓库的 `Settings → Secrets and variables → Actions` 中添加：

| Secret | 说明 | 必填 |
|--------|------|------|
| `LLM_API_KEY` | Google Gemini API Key | 是（否则无AI摘要） |
| `IEEE_API_KEY` | IEEE Xplore API Key | 否（跳过IEEE搜索） |

### 3. 手动触发

在 GitHub 仓库的 `Actions → Daily Literature Digest → Run workflow` 中手动触发。

之后每天 UTC 02:00（北京时间 10:00）自动运行。

## 项目结构

```
daily-gnss-digest/
├── .github/workflows/daily-digest.yml
├── src/
│   ├── config.py          # 配置
│   ├── summarizer.py      # LLM 摘要
│   ├── report.py          # 报告生成
│   ├── notifier.py        # 通知（暂不启用）
│   ├── main.py            # 入口
│   └── sources/
│       ├── arxiv_client.py
│       ├── ieee_client.py
│       └── journal_client.py
├── output/                # 每日报告
│   ├── README.md          # 索引
│   └── YYYY-MM-DD.md
└── requirements.txt
```

## 本地测试

```bash
pip install -r requirements.txt
export LLM_API_KEY=your_key
export IEEE_API_KEY=your_key
python src/main.py
```
