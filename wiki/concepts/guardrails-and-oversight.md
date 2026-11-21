---
title: Guardrails 與人類監督
type: concept
sources: [01, 04]
updated: 2026-11-15
---

# Guardrails 與人類監督

## 分層防護
- 單一 guardrail 不夠，要組合多層（LLM 檢查、regex 規則、moderation API）。〔raw:04〕
- Guardrails 用來補強身分驗證、權限控管等一般資安措施，不是取代它們。〔raw:04〕

| 類型 | 作用 |
|---|---|
| Relevance classifier | 擋掉離題的請求〔raw:04〕 |
| Safety classifier | 偵測 jailbreak、prompt injection〔raw:04〕 |
| PII filter | 檢查輸出有沒有個資〔raw:04〕 |
| Moderation | 標記仇恨、騷擾、暴力內容〔raw:04〕 |
| Tool safeguards | 依唯讀或可寫、可不可逆、權限、金額影響，把工具分成低／中／高風險〔raw:04〕 |
| Rules-based | 黑名單、輸入長度限制、regex〔raw:04〕 |
| Output validation | 確保輸出符合品牌價值〔raw:04〕 |

## 什麼時候要交給人類
- **失敗次數超過門檻**：例如多次重試仍無法理解使用者意圖。〔raw:04〕
- **高風險動作**：取消訂單、大額退款、付款等，在 agent 證明可靠之前都應該由人類把關。〔raw:04〕
- Anthropic：agent 可以在檢查點或卡住時暫停、請人類回饋；並建議在沙盒中大量測試。〔raw:01〕

## 建立順序
- 先處理資料隱私和內容安全 → 遇到真實的邊界案例再補 → 在安全與使用體驗之間取得平衡。〔raw:04〕

## 相關頁面
[[agent-challenges]]、[[agent-loop]]、[[tools-and-aci]]
