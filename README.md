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

## v0.1 の到達点

現時点では、生成AI APIを呼び出さずに、RSSベースでAI・ソフトウェア関連情報を収集し、カテゴリ・重要度・ダミー要約付きのMarkdownレポートを生成できます。

### v0.1 でできること

- 複数RSS情報源からの記事取得
- URLをもとにした重複除外
- 公開日時の新しい順での記事並び替え
- 取得記事数の上限設定
- キーワードベースのカテゴリ分類
- キーワードベースの重要度判定
- 重要度ごとのMarkdownレポート整理
- ダミー要約欄の表示
- `reports/` への日付付きMarkdown保存
- 生成レポートをGit管理対象外にする運用

### 生成AI APIについて

現時点では、料金が発生しないように生成AI APIは呼び出していません。

`config.py` の `ENABLE_AI_SUMMARY` は将来的にAI要約を有効化するための設定です。現在は `False` にしており、`summarizer.py` にはOpenAI API連携予定箇所をコメントとして残しています。

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

- 複数のRSS情報源からAI・ソフトウェア関連の記事を取得する
- URLをもとに重複記事を除外する
- 公開日時の新しい順に記事を並べる
- 記事にカテゴリを付与する
- 記事に high / medium / low の重要度を付与する
- 重要度ごとにMarkdownレポートを整理する
- ダミー要約を表示する
- 生成したレポートを `reports/YYYY-MM-DD.md` として保存する

## 現在の要約機能について

現時点では、料金が発生しないように生成AI APIは呼び出していません。

`summarizer.py` ではダミー要約を返す実装にしており、将来的にOpenAI APIなどの生成AI APIを呼び出す予定箇所をコメントで残しています。

今後、APIキー管理、料金対策、エラー処理を整理したうえで、最新記事1件から段階的にAI要約を有効化する予定です。

## 現在の構成

```txt
main.py
  全体の実行入口です。RSS取得、要約処理、Markdown生成、ファイル保存の流れを実行します。

config.py
  RSS情報源、取得記事数、1ソースあたりの記事数などの設定を管理します。

fetch_rss.py
  複数RSSから記事を取得し、重複除外・公開日時順ソートを行います。

summarizer.py
  現時点ではダミー要約を返します。将来的に生成AI APIによる要約処理を実装する予定です。

report_builder.py
  記事一覧をMarkdown形式のレポート本文に変換します。

report_writer.py
  Markdownレポートを reports フォルダに日付付きファイルとして保存します。

classifier.py
  記事タイトルや出典をもとに、カテゴリ分類と重要度判定を行います。

reports/
  実行時に生成される日次レポートを保存します。Git管理対象外です。

examples/
  GitHubで確認できるサンプル出力を保存します。
```

## 次に追加したいこと

- キーワードベースのカテゴリ分類
- キーワードベースの重要度判定
- OpenAI APIによる最新記事1件の要約
- 複数記事へのAI要約適用
- API利用料金を抑えるためのON/OFF設定
- 本文取得による要約精度の向上
- 毎朝の自動実行

## サンプル出力

生成されるMarkdownレポートの例は `examples/sample_report.md` にあります。
