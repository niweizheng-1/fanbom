# fanbom

シンプルなブラウザ画面録画ツール。インストール不要、サーバー不要、完全クライアントサイド。

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

---

## 機能

- 画面・ウィンドウ・タブの選択録画（OS標準ピッカー）
- マイク音声・システム音声のトグル（AudioContext でミキシング）
- 画質設定（480p / 720p / 1080p / 元解像度）
- 一時停止・再開
- 録画後プレビューと WebM/MP4 形式でのダウンロード
- ダークテーマ UI

## 使い方

### ローカル起動（Python）

```bash
python3 start.py
```

ブラウザで `http://localhost:8765` が自動で開きます。

### オンラインでの利用

HTTPS 環境にデプロイするか、GitHub Pages で公開してください。
`getDisplayMedia` は **HTTPS または localhost** でのみ動作します。

---

## ブラウザ対応

| ブラウザ | 画面録画 | システム音声 | マイク |
|----------|----------|--------------|--------|
| Chrome / Edge | ✅ | ✅（要チェック）| ✅ |
| Firefox | ✅ | ✅（限定的） | ✅ |
| Safari | ✅ | ❌ | ✅ |

### 保存ファイル形式

- Chrome / Edge → **WebM** (VP9+Opus)
- Safari → **MP4** (H.264+AAC) ※対応時
- WebM ファイルは **VLC・Chrome・Firefox** で再生できます。Windows Media Player や macOS QuickTime では開けない場合があります。

### システム音声について

- Chrome のみ対応。画面共有ダイアログで「**音声を共有**」にチェックが必要です。
- macOS は OS の制限により、システム音声のキャプチャができません。
- マイクとシステム音声を同時使用する場合、`AudioContext` で自動ミキシングされます。

---

## データとプライバシー

| 項目 | 内容 |
|------|------|
| サーバー送信 | **なし** — すべての処理はブラウザ内で完結します |
| データ保存場所 | ブラウザのメモリ（RAM）のみ。タブを閉じると消えます |
| 外部リソース | なし（CDN・フォント・アナリティクス等を一切読み込みません）|
| トラッキング | なし |
| Cookie / localStorage | 免責事項の同意状態のみ保存（録画データは保存しません）|

---

## 免責事項 / Disclaimer

**本ソフトウェアは「現状のまま（AS IS）」提供されます。**

- 本ツールを使用して行われた録画の内容・目的・影響について、開発者は一切の責任を負いません。
- 第三者の映像・音声を録画する行為は、各国・地域の法律（録音禁止法、個人情報保護法、盗撮禁止法等）の対象となる場合があります。ご利用前に適用法令を確認し、必要な同意を取得してください。
- 本ツールの使用によって生じたいかなる損害（データ損失・法的問題を含む）についても、開発者は責任を負いません。

**This software is provided "AS IS" without warranty of any kind.**

- The developer assumes no responsibility for the content, purpose, or impact of recordings made with this tool.
- Recording third-party video or audio may be subject to laws in your jurisdiction. Ensure you have obtained all required consents before recording.

---

## ライセンス / License

MIT License

Copyright (c) 2025 niweizheng-1

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
