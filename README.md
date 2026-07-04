# AI Trend Research Agent

AI・ソフトウェア・関連企業の最新情報をRSSから収集し、重要そうな記事を整理してSlackに通知するニュース収集エージェントです。

毎朝8時を基準に、直近24時間に公開された記事を対象として、AI関連の記事を抽出し、情報源ごとの取得状況も含めてレポートします。

## 主な機能

- 複数RSS情報源からの記事取得
- 昨日8時から今日8時までの24時間を対象にした記事抽出
- AI関連キーワードによる記事フィルタ
- カテゴリ分類と重要度判定
- 情報源ごとのSlack掲載記事選定
- Markdownレポート生成
- Slack Incoming Webhookによる通知
- GitHub Actionsによる毎朝8時の自動実行
- Source Statusによる取得状況の可視化

## 情報源

現在は以下のRSSを対象にしています。

- Hacker News RSS
- OpenAI Blog
- GitHub Blog
- Google AI Blog
- AINOW
- Publickey
- @IT
- SHIFT AI TIMES

## 処理の流れ

```text
RSS取得
→ 対象期間でフィルタ
→ AI関連の記事に絞り込み
→ カテゴリ分類
→ 重要度判定
→ 情報源ごとにSlack掲載記事を選定
→ Markdownレポート生成
→ Slack通知
```

## Source Status

Source Statusでは、各情報源の記事がどの段階まで残ったかを表示します。

```text
- Hacker News RSS: fetched 20件 / window 7件 / ai 5件 / slack 1件
- OpenAI Blog: fetched 3件 / window 0件 / ai 0件 / slack 0件
- Publickey: fetch failed / window 0件 / ai 0件 / slack 0件
```

これにより、記事が少ない日でも以下を区別できます。

- RSS取得に失敗した
- RSSは取得できたが対象期間内の記事がなかった
- 対象期間内の記事はあったがAI関連ではなかった
- AI関連の記事はあったがSlack掲載対象にはならなかった

## セットアップ

Pythonの仮想環境を作成し、依存ライブラリをインストールします。

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

`.env.example` を参考に `.env` を作成します。

```env
GEMINI_API_KEY=your_gemini_api_key_here
SLACK_WEBHOOK_URL=your_slack_webhook_url_here

ENABLE_SLACK_NOTIFY=false
ENABLE_AI_SUMMARY=false
AI_PROVIDER=dummy
MAX_AI_SUMMARIES=1
REPORT_HOUR=8
```

## 環境変数

| 変数名                | 内容                                              |
| --------------------- | ------------------------------------------------- |
| `SLACK_WEBHOOK_URL`   | Slack Incoming WebhookのURL                       |
| `ENABLE_SLACK_NOTIFY` | Slack通知を有効にするか                           |
| `GEMINI_API_KEY`      | Gemini APIキー                                    |
| `ENABLE_AI_SUMMARY`   | AI要約を有効にするか                              |
| `AI_PROVIDER`         | 使用するAIプロバイダー。現在は `dummy` / `gemini` |
| `MAX_AI_SUMMARIES`    | AI要約する記事数の上限                            |
| `REPORT_HOUR`         | レポート対象期間の基準時刻                        |

通常は、APIコストを避けるため `ENABLE_AI_SUMMARY=false` で運用します。

## ローカル実行

通常の実行は以下です。

```powershell
python main.py
```

日次実行用スクリプトを使う場合は以下です。

```powershell
.\run_daily_report.bat
```

`run_daily_report.bat` は実行ログを `logs/` に出力します。

## GitHub Actionsでの自動実行

GitHub Actionsで毎朝8時に自動実行します。

GitHub ActionsのcronはUTC基準です。日本時間8:00に実行するため、workflowでは以下のcronを設定しています。

```yaml
schedule:
  - cron: "0 23 * * *"
```

Slack通知を行うため、GitHubリポジトリのSecretsに以下を登録します。

```text
SLACK_WEBHOOK_URL
```

手動実行もできるように、workflowには `workflow_dispatch` を設定しています。

```text
Actions
→ Daily AI Trend Report
→ Run workflow
```

## 出力

Markdownレポートは `reports/` に生成されます。

```text
reports/YYYY-MM-DD.md
```

`reports/` は実行時に生成される出力先のため、Git管理対象外です。

サンプル出力は `examples/` に配置します。

## Slack通知

Slackには、選定された記事とSource Statusを投稿します。

主な表示内容は以下です。

- 本日のピックアップ件数
- 記事タイトル
- source
- category
- importance
- selection reason
- 元記事リンク
- summary
- Source Status

## 現在のAI利用方針

現時点では、APIコストを避けるためAI要約はデフォルトでOFFにしています。

```env
ENABLE_AI_SUMMARY=false
AI_PROVIDER=dummy
```

将来的にはGemini APIを使って、以下を段階的に改善する予定です。

- 要約
- AI関連判定
- 重要度判定
- Slack掲載判断
- 技術面 / ビジネス面の分類

## 今後の改善予定

- Gemini APIによる要約精度の改善
- AI関連判定の精度向上
- 重要度判定ロジックの改善
- Slack表示のさらなる整理
- 情報源ごとの取得安定性向上
