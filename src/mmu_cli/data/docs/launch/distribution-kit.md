# Distribution Kit — Copy-Paste Launch Posts

Everything below is ready to post as-is. The repo is polished; stars now come
from showing up where builders already are. One channel per day, always reply
to every comment within a few hours, never cross-post the same text to two
places on the same day.

Ground rules (so this never reads as spam):

- Post as yourself, in first person, and say you built it.
- Lead with the problem, not the project.
- Reply to every comment — the reply thread is the actual marketing.
- If a post flops, don't repost the same text; rewrite the angle first.

Suggested order (2 weeks):

| Day | Channel | Asset below |
|-----|---------|-------------|
| 1 | GeekNews (news.hada.io) | Korean post |
| 2 | r/SideProject | Reddit A |
| 3 | X/Twitter thread | Thread |
| 5 | r/ClaudeAI | Reddit B |
| 7 | Show HN (Tue–Thu, 8–10am ET) | HN post |
| 8 | r/Python | Reddit C |
| 10 | awesome-list PRs + MCP directories | Snippets |
| 12+ | Dev.to / 요즘IT article | Outline |

---

## Show HN

**Title:**

> Show HN: Make Me Unicorn – catch what AI-generated SaaS code misses

**Text:**

> I ship side projects with AI coding tools, and I kept making the same
> mistakes: login flow with no password reset, Stripe webhooks with no
> signature verification, launching with no OG tags so every shared link
> looked broken.
>
> The code was never the problem — tracking what matters was. So I built an
> open-source CLI that treats "ready to launch" as something you can measure.
>
> `mmu init && mmu scan && mmu` gives you a launch-readiness dashboard: 670+
> checklist items across 15 categories, 6 stage gates (problem fit → scale
> fit), scored against only what applies to your stack. `mmu vibecheck` scans
> for the specific gaps AI assistants introduce most (hardcoded secrets,
> f-string SQL, wildcard CORS, missing rate limits) and fails CI on
> launch-blocking findings.
>
> It also runs as an MCP server and a Claude Code plugin, so the same
> checklist your CI reads is what your AI agent reads — no re-explaining your
> project every session.
>
> Zero dependencies for the core CLI, MIT, Python 3.10+. Would love feedback
> on the vibecheck heuristics — what does AI-generated code get wrong in your
> experience?
>
> https://github.com/minjikim89/make-me-unicorn

---

## Reddit A — r/SideProject

**Title:**

> I kept shipping AI-generated SaaS with the same holes (no password reset, unverified webhooks), so I built an open-source launch checklist CLI

**Body:**

> Solo builder here. Every project I shipped with AI assistance had the same
> pattern: the code worked, but something invisible was missing. Users locked
> out on day one because I built login but not password reset. A Stripe
> webhook anyone could forge because I skipped signature verification.
>
> I stopped trusting my memory and made the checklist executable:
>
> - `mmu init && mmu scan && mmu` → launch-readiness dashboard in your
>   terminal (670+ items, 15 categories, scored against your actual stack)
> - `mmu vibecheck` → scans for what AI code misses most: hardcoded secrets,
>   f-string SQL, wildcard CORS, missing rate limiting. Fails CI on blockers.
> - Your "unicorn" evolves as your score climbs: Egg → Hatching → Foal →
>   Young → Unicorn 🦄
>
> It's MIT, Python, zero deps for the core CLI. Honest question for other
> solo builders: what's the thing YOU always forget before launch? I want to
> turn the answers into checks.
>
> GitHub: https://github.com/minjikim89/make-me-unicorn

---

## Reddit B — r/ClaudeAI (or r/mcp)

**Title:**

> I turned my SaaS launch checklist into an MCP server + Claude Code plugin — my agent now reads the same gates my CI does

**Body:**

> The biggest problem I had with AI coding wasn't code quality — it was
> context. Every session I re-explained the project, and the agent happily
> rebuilt things while missing what actually blocked launch.
>
> So I made the checklist the shared source of truth:
>
> - **MCP server** (`mmu serve-mcp`): Claude Desktop / Claude Code / Cursor
>   can list 17 launch blueprints, pull any of them as tools, and even
>   validate a startup idea against real HN + Reddit threads
>   (`mmu_validate_idea`, free mode — no API keys).
> - **Claude Code plugin**: `/plugin marketplace add minjikim89/make-me-unicorn`
>   — auto-invokes when you mention launching, validation, or Product Hunt.
> - **`mmu start --mode backend --agent`**: loads only the docs that mode
>   needs, so the context window isn't drowned in your whole repo.
>
> Core CLI is zero-dependency; the AI parts are optional extras. MIT.
> Curious how others keep agent context in sync across sessions — files?
> MCP? something else?
>
> https://github.com/minjikim89/make-me-unicorn

---

## Reddit C — r/Python

**Title:**

> make-me-unicorn: a zero-dependency CLI that scores your project's launch readiness (and vibe-checks AI-generated code)

**Body:**

> I built a Python CLI for a problem linters don't cover: the gap between
> "code runs" and "safe to launch."
>
> - Core CLI has **zero external dependencies** (stdlib only) — `pip install
>   make-me-unicorn`, works on 3.10+
> - `mmu scan` detects your stack and auto-checks items you've implemented
> - `mmu vibecheck` greps for the classics: hardcoded secrets, f-string SQL,
>   wildcard CORS, `DEBUG = True`, webhook handlers without signature
>   verification — exits non-zero on blockers so it drops into CI
> - Optional extras: `[llm]` (Anthropic doc generation), `[mcp]` (MCP
>   server), `[validate]` (HN/Reddit idea validation with local VADER
>   sentiment)
> - 125 unit tests, ruff + mypy in CI
>
> Architecture feedback welcome — especially on keeping the stdlib-only core
> honest while extras grow.
>
> https://github.com/minjikim89/make-me-unicorn

---

## GeekNews (news.hada.io) — Korean

**제목:**

> Make Me Unicorn — AI가 짠 SaaS 코드가 놓치는 것들을 잡아주는 오픈소스 출시 체크리스트 CLI

**본문:**

> 혼자 사이드프로젝트를 만들면서 매번 같은 실수를 반복했습니다. 로그인은
> 만들었는데 비밀번호 재설정이 없어서 첫날부터 사용자가 계정에 못 들어가고,
> Stripe 웹훅에 서명 검증이 없어서 누구나 결제 이벤트를 위조할 수 있는 상태로
> 배포하고, OG 태그 없이 출시해서 공유 링크가 전부 깨져 보이고.
>
> 코딩 실력 문제가 아니라 "챙겨야 할 것을 추적하지 못하는" 문제라서, 체크리스트를
> 실행 가능하게 만들었습니다.
>
> - `mmu init && mmu scan && mmu` → 터미널에 출시 준비도 대시보드 (15개 카테고리
>   670+ 항목, 내 스택에 해당하는 것만 점수에 반영)
> - `mmu vibecheck` → AI 생성 코드가 가장 자주 놓치는 것 스캔: 하드코딩된 시크릿,
>   f-string SQL, 와일드카드 CORS, rate limit 부재. 블로커 발견 시 CI 실패.
> - MCP 서버 + Claude Code 플러그인 — CI가 읽는 체크리스트를 AI 에이전트도 그대로
>   읽어서, 세션마다 프로젝트를 다시 설명할 필요가 없습니다.
> - 점수가 오르면 유니콘이 진화합니다: 알 → 부화 → 망아지 → 유니콘 🦄
>
> 코어 CLI는 의존성 제로(파이썬 표준 라이브러리만), MIT 라이선스입니다.
> "출시 전에 항상 까먹는 것"이 있다면 댓글로 알려주세요 — 체크 항목으로
> 만들겠습니다.
>
> https://github.com/minjikim89/make-me-unicorn

---

## X/Twitter Thread

> 1/ AI writes your code fast. Then day one: users can log in but can't
> reset passwords. Your Stripe webhook accepts forged events. Every shared
> link shows a broken preview.
>
> The code wasn't the problem. Tracking what matters was. So I open-sourced
> my fix 🧵
>
> 2/ `pip install make-me-unicorn` → `mmu init && mmu scan && mmu`
>
> A launch-readiness dashboard in your terminal. 670+ checks, 15 categories,
> 6 stage gates. Scored against YOUR stack only — no billing? billing items
> don't count against you.
>
> [demo.gif]
>
> 3/ `mmu vibecheck` scans for what AI-generated code misses most:
>
> ✗ hardcoded secrets
> ✗ webhooks without signature verification
> ✗ login without password reset
> ✗ f-string SQL
> ✗ wildcard CORS
>
> Blockers = CI fails. One YAML step in GitHub Actions.
>
> 4/ It's also an MCP server + Claude Code plugin. The same checklist your
> CI enforces is what your AI agent reads. No more re-explaining your
> project every session.
>
> 5/ Your unicorn evolves as you get closer to launch:
> Egg → Hatching → Foal → Young → Unicorn 🦄
>
> MIT. Zero-dep core. Python 3.10+.
> ⭐ https://github.com/minjikim89/make-me-unicorn

---

## Awesome-list PR snippets

Open a PR against each list adding one line (read each list's CONTRIBUTING
first; keep alphabetical order):

**awesome-mcp-servers** (`punkpeye/awesome-mcp-servers`, dev-tools section):

```markdown
- [make-me-unicorn](https://github.com/minjikim89/make-me-unicorn) 🐍 🏠 - SaaS launch-readiness checklists as tools: 17 launch blueprints, idea validation against real HN + Reddit threads, and AI-code vibe checks.
```

**awesome-claude-code / awesome-claude-skills** (plugins/skills section):

```markdown
- [make-me-unicorn](https://github.com/minjikim89/make-me-unicorn) - Launch OS for solo SaaS builders: readiness score, stage gates, and vibecheck for AI-generated code. `/plugin marketplace add minjikim89/make-me-unicorn`
```

## MCP directories

- **Official MCP Registry** — `server.json` is already in the repo root.
  Install `mcp-publisher`, run `mcp-publisher login github` then
  `mcp-publisher publish` from the repo root.
- **smithery.ai** — sign in with GitHub → Add server → point at the repo.
- **mcp.so** / **glama.ai** — both accept submissions via a form / GitHub
  issue; paste the repo URL and the one-liner below.

One-liner for directories:

> Launch OS for solo SaaS builders — launch-readiness score, 17 blueprints,
> idea validation against real HN + Reddit threads, and vibe checks for
> AI-generated code.

## Dev.to / 요즘IT article outline

Title: **"45% of AI-generated code ships with vulnerabilities. Here's the
checklist mine goes through."**

1. Hook: the day-one lockout story (login without password reset).
2. Why linters don't catch launch gaps (they check code, not product).
3. The 5 checks that catch 80% of AI-code incidents (walk through real
   `mmu vibecheck` output).
4. Making the checklist executable: score, gates, CI.
5. Same checklist for the agent: MCP + Claude Code plugin.
6. CTA: repo link + "what do you always forget? I'll turn it into a check."
