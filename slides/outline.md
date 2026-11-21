# 簡報大綱：AI Agents 是什麼？
觀眾：修過 AI 入門課的同學｜約 15 分鐘｜14 張
規則：只用 Wiki 內容；每張標 wiki: 來源頁

## S1 封面：AI Agents 是什麼？
wiki: overview
- 副標：從「會回答」的 LLM，到「會自己做事」的系統
- 一句話定義：讓 LLM 在迴圈裡自己決定下一步、透過工具和環境互動，直到完成任務

## S2 暖身：聊天機器人 vs Agent
wiki: what-is-an-agent, agency-spectrum
- 「不是 agent」的例子：簡單 chatbot、單輪 LLM 呼叫、情緒分類器
- 關鍵問題：LLM 的輸出有沒有控制程式流程？
note: 先問同學「ChatGPT 算不算 agent？」

## S3 三個來源怎麼定義 agent
wiki: what-is-an-agent, agent-definitions-compared
- OpenAI：代替你獨立完成任務的系統
- Hugging Face：利用 AI 模型和環境互動，達成使用者目標
- Lilian Weng：LLM 大腦 + 規劃 + 記憶 + 工具
- 共識：LLM 控制流程 + 透過工具和環境互動

## S4 Alfred 煮咖啡
wiki: what-is-an-agent, src-hf-what-is-an-agent
- 理解 → 規劃 → 使用工具（咖啡機）→ 交付
- 大腦（模型）想，身體（工具）做

## S5 Agent 的元件
wiki: what-is-an-agent, augmented-llm, planning, memory
- 大腦 LLM、規劃（拆解 / 反思）、記憶（短期 context、長期向量資料庫）、工具、指令
- Augmented LLM：LLM + 檢索 + 工具 + 記憶 是基本積木

## S6 核心迴圈：Thought → Action → Observation
wiki: agent-loop
- 互動動畫：一步步跑完範例
- 停止條件：最終輸出工具、沒有工具呼叫、錯誤、最大回合數

## S7 為什麼要邊想邊做？ReAct
wiki: src-react-paper, agent-loop, source-discrepancies
- 2022 年提出；推理和行動交錯
- ALFWorld 成功率 +34%、WebShop +10%，只用 1–2 個範例
- 減少幻覺與錯誤傳遞、推理過程看得懂

## S8 Agency 光譜
wiki: agency-spectrum, agent-definitions-compared
- ☆☆☆ Simple processor → ★☆☆ Router → ★★☆ Tool caller → ★★★ Multi-step agent / Multi-agent
- 來源差異：Anthropic 把 routing 算 workflow

## S9 Workflow vs Agent 與五種模式
wiki: workflow-vs-agent, workflow-patterns
- 誰決定流程：預先寫好的程式路徑 vs LLM 自己決定
- Prompt chaining、Routing、Parallelization、Orchestrator-workers、Evaluator-optimizer

## S10 工具決定 agent 能做什麼：ACI 與 MCP
wiki: tools-and-aci, mcp
- 工具三類：Data / Action / Orchestration
- ACI：工具說明要像寫給新人的文件；poka-yoke 防呆（強制絕對路徑的例子）
- MCP：MCP server 公開工具、MCP client 連接

## S11 一個不夠？多代理
wiki: multi-agent-orchestration
- 先從單一 agent 開始
- Manager（工具呼叫）vs Decentralized（handoff）

## S12 什麼時候該用 agent？
wiki: when-to-use-agents
- 先求最簡單；用延遲和成本換表現
- 三個判斷條件：複雜決策、難以維護的規則、非結構化資料

## S13 風險與 Guardrails
wiki: agent-challenges, guardrails-and-oversight
- 挑戰：context 有限、長期規劃、介面不可靠、錯誤累積
- 分層 guardrails；高風險動作交給人類

## S14 總結與小測驗
wiki: overview, agency-spectrum, agent-loop
- 三個共同結論
- 小測驗：這是幾顆星？
