# AI Trend Research Agent

AI・ソフトウェア・関連企業の最新情報を取得し、要約・分類して毎朝確認できる形に整理するエージェントです。

## 目的

- AIエージェント開発を学ぶ
- 毎朝、重要なAI・ソフトウェア関連ニュースを確認できるようにする
- 出典リンク付きで情報を整理する
- 日常的に使える実用ツールにする

## 最初のMVP

1つのRSSから最新記事を取得し、以下の情報を表示する。

- タイトル
- 公開日
- 出典元
- 元記事URL

## 今後追加したい機能

- 複数情報源からの収集
- AIによる要約
- カテゴリ分類
- 重要度判定
- Markdown形式の日次レポート生成
- 毎朝の自動実行

## セットアップ

Pythonの仮想環境を作成し、必要なライブラリをインストールします。

```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 実行方法

以下のコマンドで、AI関連ニュースの取得とMarkdownレポート生成を実行します。

```bash
python main.py
```

実行すると、Hacker News RSSからAI関連の新着記事を取得し、Markdown形式のレポートを `reports/YYYY-MM-DD.md` に保存します。

## 現在の構成

```txt
main.py
  全体の実行入口です。RSS取得、Markdown生成、ファイル保存の流れを実行します。

fetch_rss.py
  Hacker News RSSからAI関連の記事を取得し、title / url / source / published_at を持つ辞書データに整理します。

report_builder.py
  記事一覧をMarkdown形式のレポート本文に変換します。

report_writer.py
  Markdownレポートを reports フォルダに日付付きファイルとして保存します。

reports/
  生成された日次レポートを保存します。
```

## 現在できること

- Hacker News RSSからAI関連の新着記事を取得する
- 記事タイトル、公開日、出典元、URLを取得する
- 取得した記事を辞書形式で整理する
- Markdown形式の日次レポートを生成する
- 生成したレポートを `reports/YYYY-MM-DD.md` として保存する

## 次に追加したいこと

- 複数のRSS情報源に対応する
- 記事の重複を除外する
- AIによる要約を追加する
- カテゴリ分類を追加する
- 重要度判定を追加する
- 毎朝自動実行できるようにする

## サンプル出力

生成されるMarkdownレポートの例は `examples/sample_report.md` にあります。
