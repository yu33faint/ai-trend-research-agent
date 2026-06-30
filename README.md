# AI Trend Research Agent

AI・ソフトウェア・関連企業の最新情報を取得し、要約・分類して毎朝確認できる形に整理するエージェントです。

## 目的

- AIエージェント開発を学ぶ
- 毎朝、重要なAI・ソフトウェア関連ニュースを確認できるようにする
- 出典リンク付きで情報を整理する
- 日常的に使える実用ツールにする

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
- サンプル出力を `examples/` に配置

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

実行すると、複数のRSS情報源からAI・ソフトウェア関連の記事を取得し、Markdown形式のレポートを `reports/YYYY-MM-DD.md` に保存します。

`reports/` は実行時に生成されるファイルの保存先であり、Git管理対象外です。

## AI要約設定の切り替え

AI要約機能は、環境変数で一時的に切り替えられます。

通常は `ENABLE_AI_SUMMARY = False` のため、生成AI APIは呼び出されません。

PowerShellでダミー要約を有効化する例:

```powershell
$env:ENABLE_AI_SUMMARY="true"
$env:AI_PROVIDER="dummy"
$env:MAX_AI_SUMMARIES="1"
python main.py
```

### 動作確認パターン

#### 1. 通常実行

```powershell
python main.py
```

`ENABLE_AI_SUMMARY` を設定しない場合、AI要約は実行されません。

#### 2. ダミー要約を有効化する

```powershell
$env:ENABLE_AI_SUMMARY="true"
$env:AI_PROVIDER="dummy"
$env:MAX_AI_SUMMARIES="1"
python main.py
```

この設定では、最新1件だけダミー要約に差し替わります。Gemini APIは呼び出されないため、料金は発生しません。

#### 3. Geminiを選ぶが、APIキー未設定で確認する

```powershell
$env:ENABLE_AI_SUMMARY="true"
$env:AI_PROVIDER="gemini"
$env:MAX_AI_SUMMARIES="1"
python main.py
```

`.env` または環境変数に `GEMINI_API_KEY` が設定されていない場合、要約欄には `Gemini APIキーが設定されていません。` と表示されます。

この段階ではAPI呼び出し処理は未実装のため、Gemini APIは呼び出されません。

## APIキー管理について

将来的にGemini APIの無料枠を使って要約機能を追加する予定です。

本物のAPIキーは `.env` に保存し、Git管理対象には含めません。必要な環境変数の例は `.env.example` に記載しています。

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

## 現在の要約機能について

現時点では、料金が発生しないように生成AI APIは呼び出していません。

`summarizer.py` ではダミー要約を返す実装にしており、将来的にはGemini APIの無料枠を使って、最新記事1件から段階的にAI要約を有効化する予定です。

`config.py` の以下の設定により、AI要約の有効化・利用プロバイダー・要約件数を制御する想定です。

```python
ENABLE_AI_SUMMARY = get_bool_env("ENABLE_AI_SUMMARY", False)
AI_PROVIDER = os.getenv("AI_PROVIDER", "dummy")
MAX_AI_SUMMARIES = get_int_env("MAX_AI_SUMMARIES", 1)
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")
```

## 現在の構成

```txt
main.py
  全体の実行入口です。RSS取得、分類、重要度判定、要約処理、Markdown生成、ファイル保存の流れを実行します。

config.py
  RSS情報源、取得記事数、1ソースあたりの記事数、AI要約設定などを管理します。

fetch_rss.py
  複数RSSから記事を取得し、重複除外・公開日時順ソートを行います。

classifier.py
  記事タイトルや出典をもとに、カテゴリ分類と重要度判定を行います。

summarizer.py
  現時点ではダミー要約を返します。将来的にGemini APIによる要約処理を実装する予定です。

report_builder.py
  記事一覧を重要度ごとに整理し、Markdown形式のレポート本文に変換します。

report_writer.py
  Markdownレポートを reports フォルダに日付付きファイルとして保存します。

reports/
  実行時に生成される日次レポートを保存します。Git管理対象外です。

examples/
  GitHubで確認できるサンプル出力を保存します。
```

## サンプル出力

生成されるMarkdownレポートの例は `examples/sample_report.md` にあります。

## 次に追加したいこと

- Gemini API無料枠を使った最新記事1件の要約
- Gemini API利用時のエラー処理
- Gemini API利用時のレート制限・無料枠を意識した制御
- 本文取得による要約精度の向上
- カテゴリ分類・重要度判定の精度改善
- 毎朝の自動実行
