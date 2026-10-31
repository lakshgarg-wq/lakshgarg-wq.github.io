"""Builds index.html and cases/*.html. Run from the site root: python3 tools/build.py ."""
import os, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
SITE = "https://lakshgarg-wq.github.io/"
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">'
LI = "https://www.linkedin.com/in/lakshay-garg-66840947"
MAIL = "laksh.garg@gmail.com"

def head(title, desc, root, og=None, path=""):
    img = f'<meta property="og:image" content="{SITE}og/{og}.png"><meta name="twitter:card" content="summary_large_image">' if og else ""
    meta = f'<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{SITE}{path}">{img}'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{FONTS}
{meta}
<link rel="stylesheet" href="{root}site.css">
</head>
<body>
<div class="wrap">
<nav class="top"><a class="brand mono" href="{root}index.html"><b>●</b> lakshay.garg</a><span class="links"><a href="{root}index.html#professional">/work</a><a href="{root}index.html#personal">/builds</a><a href="{root}index.html#contact">/contact</a></span></nav>
'''

def foot():
    return f'''<footer id="contact">
  <h2>Want AI to take work off your desk?</h2>
  <p>I help founders set up AI in their business. First I look at how you work. Then I build the tools that save you time.</p>
  <div class="cta"><a class="btn primary" href="mailto:{MAIL}">{MAIL}</a><a class="btn" href="{LI}">LinkedIn ↗</a></div>
  <p class="fine mono">© 2026 Lakshay Garg</p>
</footer>
</div>
</body>
</html>
'''

def pipe(steps):
    return '<div class="pipe">' + ''.join(
        f'<div class="{"h" if h else ""}"><span>{i+1:02d} · {"human" if h else "system"}</span><b>{a}</b><p>{b}</p></div>'
        for i, (a, b, h) in enumerate(steps)) + '</div>'

# Reading order across case pages.
ORDER = ["sentinel", "account-intelligence", "outbound", "audit-loop", "grantscope",
         "nse-pulse", "ledgerlens", "chief-of-staff", "token-economics"]
NAMES = {}

def case(slug, kind, title, short, lede, steps, secs, box=None, chips=()):
    NAMES[slug] = short
    CASES[slug] = (kind, title, lede, steps, secs, box, chips)

CASES = {}

case("sentinel", "Professional · Signal intelligence",
 "Sentinel: one intelligence layer for buying signals", "Sentinel",
 "A system that watches many market sources, turns what it sees into one view of which accounts are worth approaching now, and feeds that view to outreach every day.",
 [("collect", "Many independent trackers", 0), ("normalise", "One signal shape", 0), ("merge", "Signals into accounts", 0), ("prioritise", "Hot · Warm · Cold", 0), ("brief", "Feeds the daily queue", 1)],
 [("The problem", "Buying signals were scattered across feeds such as filings, tenders, deals, hiring and news. Each had its own format and its own idea of what counts as important, so there was no single ranked view of the market."),
  ("Collection", "Independent trackers watch the market, and the daily queue is only ever fed fresh data."),
  ("One view per account", "Every source lands in one place, grouped by account. What used to be scattered feeds is now one picture of each account."),
  ("Priority", "The market is sorted into Hot, Warm and Cold, so each day starts with the few accounts worth approaching now. A headline that sounds good is not enough to make an account hot."),
  ("Applied across four geographies", "The same design runs for the EU, the GCC, India and the US. Each region has its own sources and its own morning brief. One system serves four markets."),
  ("Feeding outreach", 'Sentinel is the starting point for the daily outbound engine, and results flow back into it. Read more about that engine <a href="outbound.html">here</a>.')],
 ["Runs daily at a fraction of the usual model cost."],
 ["Intent data", "Signal design", "Lead scoring", "Data pipelines", "Multi-market GTM"])

case("account-intelligence", "Professional · Account intelligence",
 "Account intelligence: finding upsell in 1,000+ client accounts", "Account intelligence",
 "A pipeline that turns a bare list of more than a thousand existing client accounts into sourced facts, and those facts into new upsell opportunities.",
 [("client list", "Names only", 0), ("enrich", "Public sources", 0), ("extract", "Facts at scale", 0), ("sourced facts", "Every fact has a source", 0), ("upsell", "Opportunities routed", 1)],
 [("The problem", "The firm had more than a thousand existing client accounts and almost nothing about them beyond a name. Researching each one by hand was impossible, and running an AI agent per account would have been slow and expensive."),
  ("Enrichment at scale", "The pipeline enriches the whole client list from public sources, without anyone researching a thousand companies by hand."),
  ("Cost under control", "The full list is processed at a fraction of what per-account AI research would cost, and effort goes where an opportunity is plausible."),
  ("Provenance on every fact", "Every fact carries its source. Because these packets travel to account owners, nothing unsourced is allowed through."),
  ("From facts to pipeline", "The output is a table of facts per account that maps each client to the services they don't buy yet. It becomes a ranked pipeline of upsell opportunities, routed to the people who own those relationships.")],
 ["Covers 1,000+ accounts at a fraction of the usual model cost."],
 ["Account intelligence", "Cross-sell / upsell", "Data enrichment", "Pipeline design", "Token economics"])

case("outbound", "Professional · Agent orchestration",
 "Agent-orchestrated outbound: from signal to sent message", "Outbound orchestration",
 "A daily system that decides which accounts to approach, researches them and gets a personalised first message ready. Agents do the work and a person owns every send.",
 [("admit", "Only accounts with a real signal", 0), ("rank", "Today's shortlist", 0), ("research", "Packet, then challenge", 0), ("draft + gate", "Checked before it reaches me", 0), ("send", "I approve and send", 1)],
 [("Admission", "An account only enters the system with a real reason to approach it now. Everything else is dropped. That keeps the pipeline small enough to work properly."),
  ("Selection and ranking", "Admitted accounts are ranked every day, and the top few become the working list."),
  ("Research per account", 'An agent researches each account, and a person challenges that research before anything is drafted. Read more about that loop <a href="audit-loop.html">here</a>.'),
  ("Agent orchestration", "Several agents share the work, each matched to the job it does, and a supervisor reviews what comes back."),
  ("Drafts, then my approval", "Every draft is checked before it reaches me. Nothing is sent without my approval."),
  ("Connected to a central intelligence layer", 'The daily queue isn\'t built from scratch. It draws on Sentinel, the signal layer that watches the market and decides what is hot. Read more about this engine <a href="sentinel.html">here</a>.')],
 ["Runs every day at a fraction of the usual model cost."],
 ["Agent orchestration", "Lead scoring", "AI research", "Human-in-the-loop"])

case("audit-loop", "Professional · Human-in-the-loop",
 "The research and audit loop: agents propose, people challenge, the system improves", "Research & audit loop",
 "A workflow where an agent's research is handed to a person whose job is to test it, every verdict is recorded, and the whole system is audited and improved every month.",
 [("agent research", "A packet per account", 0), ("analyst review", "A person tests it", 1), ("record", "Every verdict kept", 0), ("feedback", "How it landed", 0), ("monthly audit", "Improve the workflow", 1)],
 [("The problem", "Agent research reads just as confidently when it is wrong as when it is right. The real risk isn't a wrong fact. It's the decisions and assumptions an agent makes quietly along the way: why this account, why this person, why this angle."),
  ("A person in the loop", "My agent's research on each account goes to an analyst who reports to me. Their job is to test it, not trust it, and to add what the model couldn't see or got wrong."),
  ("Recording the change", "Every verdict is recorded and the system learns from it, so the same mistake doesn't come back."),
  ("Feedback from what is actually sent", "What I actually send, and how it lands, flows back into the same loop. Over time the drafts move closer to my own judgment."),
  ("Catching silent failures", "A job can fail and still report success. The system watches for that and tells me when something slips. It has already caught a retired model that the scripts had been hiding for weeks."),
  ("Monthly audit of the system", "Once a month the whole workflow is audited. The findings change how the system works, not just its output. One audit showed the constraint was follow-up volume, not message quality, so the build effort moved there. Another found a hidden bias in how accounts were picked: daily picks ran at roughly 50 to 70% from one region, which was 18% of the eligible pool. That bias is now fixed.")],
 None,
 ["Human-in-the-loop", "Process design", "Quality systems", "Continuous improvement", "Team enablement"])

case("grantscope", "Professional · Data platform",
 "GrantScope: who actually wins deeptech grants", "GrantScope",
 "A database of every company that won a Spanish or EU deeptech grant, rebuilt each month from public sources and used for startup scouting and account discovery.",
 [("collect", "Nine grant programmes", 0), ("match", "One company, many spellings", 0), ("tag", "A deeptech core", 0), ("export", "Filtered lists + dashboard", 0), ("use", "Shortlists for events", 1)],
 [("The problem", "Grant results were spread across nine national, regional and EU programmes, each with its own site, format and naming. Building a shortlist meant days of manual searching."),
  ("Collection", "Each programme is collected on a monthly cycle, including one source with more than 400,000 rows. A full refresh takes about 12 minutes."),
  ("Entity matching", "The same company appears under different spellings and IDs across sources. The system matches them into one record, which is the hard part."),
  ("Classification", "The system separates real deeptech from the rest: a core of about 1,600 companies, out of more than 22,000."),
  ("Use", "Shortlists for ecosystem events now take minutes instead of days. The same pattern runs for EU tenders, private-equity deal flow and export-import buyer discovery.")],
 ["Refreshes every month at almost no model cost."],
 ["Data sourcing", "Entity matching", "Market mapping", "Account discovery"])

case("nse-pulse", "Personal · Market intelligence",
 "Indian equity market trading intelligence", "Indian Equity Market Trading Intelligence",
 "A personal research system for Indian equities. It ingests exchange data every day, parses company documents the moment they are published, and tests trading ideas on an engine built not to flatter them.",
 [("ingest", "Daily exchange reports", 0), ("parse", "Filings and earnings calls", 0), ("signal", "Conviction and risk flags", 0), ("dashboard", "Critical highlights", 1), ("backtest", "Honest engine", 0)],
 [("A daily data pipeline", "Every trading day the system downloads the exchange's public reports, structures them and loads them into a local database. The data is checked before anything downstream uses it."),
  ("Signals, not noise", "From that data it ranks stocks by conviction, flags risk, and shows which names keep coming up, not just today's."),
  ("Automated document parsing", "Company filings and earnings-call transcripts are parsed automatically as soon as they are published. The results feed a dashboard of critical highlights: what changed, what was promised and what looks like a red flag."),
  ("A deep-dive page per stock", "Each stock has its own page with scores and a private investment journal. Theses, checkpoints and notes accumulate, so the page gets more useful every quarter."),
  ("Backtesting that doesn't lie", "One engine prices every test the way real trading would. Every strategy has to survive hard attempts to break it before any result is believed."),
  ("Weekly audit and improvement", "Every mistake, mine or the AI's, is logged and reviewed weekly, and the system gets stricter each time.")],
 ["Runs daily at a fraction of the usual model cost: one reading job went from ~155k to ~11k tokens per request with the same output quality."],
 ["Data pipelines", "Document AI", "Dashboards", "Backtesting", "Investment research"])

case("ledgerlens", "Personal · Behavioural analytics",
 "Personalised trading monitoring and intelligence", "Personalised Trading Monitoring & Intelligence",
 "A web app that turns years of my own broker trade files into a ledger of every decision, then tells me what kind of trader I was at each stage and where my habits cost me.",
 [("import", "Broker trade files", 0), ("ledger", "Every lot, every decision", 0), ("tag", "Behaviour patterns", 0), ("personas", "Trader type per era", 0), ("replay", "My exits vs rules", 1)],
 [("The problem", "A broker shows profit and loss. It doesn't show behaviour: why I bought, why I sold, and whether my habits helped or hurt."),
  ("A ledger of every decision", "Trade files spanning several years are rebuilt into a ledger of every decision, each one linked to what the market was doing at that moment."),
  ("Behaviour tags", "Each closed trade is tagged with the behaviour it shows, and the trades that made or broke a period are pulled out."),
  ("Trader personas", "My history is split into eras, each with its own trader persona, and the app explains which habit changed between them."),
  ("Replaying my exits", "My real trades are replayed under rule-based exits, to see where discipline would have beaten my own calls. The results shaped how I trade now.")],
 None,
 ["Behavioural analytics", "Product build", "Data modelling", "Self-measurement"])

case("chief-of-staff", "Personal · Context engineering",
 "Teaching every AI model how I work, once", "AI chief of staff",
 "A system that learns from my own work history and builds a portable profile that any AI model can load, so it behaves like a chief of staff from the very first message.",
 [("collect", "My own work history", 0), ("extract", "Patterns, not summaries", 0), ("weigh", "Evidence-backed claims", 0), ("package", "A portable profile", 0), ("use", "Any model, day one", 1)],
 [("The problem", "Every AI model starts from zero about me, and each one quietly builds its own picture of who I am. I wanted one picture that I own and can check."),
  ("Collection", "My history with AI tools and the records of my working sessions are gathered into one corpus."),
  ("Extraction", "Instead of summarising, the system looks for the patterns in how I actually work."),
  ("Evidence, not opinion", "Every finding is backed by evidence, and I correct it where it's wrong."),
  ("Output", "A portable profile any model can load. It covers how I work, how I think and what I'm focused on now, so a new session behaves like a chief of staff who already knows me.")],
 ["The finished profile is compact and loads in one step, not a pile of history."],
 ["Context engineering", "AI memory", "Knowledge systems", "Model routing"])

case("token-economics", "Personal · Token economics",
 "Token economics: making AI systems cheap enough to run every day", "Token economics",
 "Agent systems are only useful if they can run daily without the bill or the limits stopping them. I measure and cut what my AI systems spend.",
 [("measure", "Where tokens go", 0), ("diet", "Leaner requests", 0), ("route", "Right model per task", 0), ("automate", "Runs every day", 0), ("tooling", "See it live", 1)],
 [("Measure first", "I studied 480 of my own AI sessions to see where the tokens actually went, and found where most of the spend was coming from."),
  ("A token-diet playbook", "I wrote a reusable playbook for cutting what an AI job spends without losing quality. On one real job it cut a ~155k-token request to ~11k with the same output quality."),
  ("Model routing", "Each task goes to the model it actually needs, so the most expensive model is used only where it earns its cost."),
  ("Built to run daily", "My scheduled jobs run every day without the bill or the limits stopping them."),
  ("Tooling around it", "I built add-ons that show context size and cost live and give one view of every running session and background job.")],
 None,
 ["Token economics", "Cost management", "Model routing", "Agent operations"])

# ---------- write case pages ----------
os.makedirs(os.path.join(OUT, "cases"), exist_ok=True)
for i, slug in enumerate(ORDER):
    kind, title, lede, steps, secs, box, chips = CASES[slug]
    s = head(f"{NAMES[slug]} — Lakshay Garg", lede, "../", slug if slug in ("sentinel", "audit-loop") else "home", f"cases/{slug}.html")
    s += f'<main class="case"><header><div class="mono prompt">{kind}</div><h1>{title}</h1><p class="lede">{lede}</p></header>\n'
    s += pipe(steps) + "\n"
    for j, (h, body) in enumerate(secs):
        s += f'<section><h2><small>{j+1:02d}</small>{h}</h2><p>{body}</p></section>\n'
    if box:
        s += '<div class="box"><h3>Built to be token-efficient</h3><ul>' + ''.join(f'<li>{x}</li>' for x in box) + '</ul></div>\n'
    s += '<div class="chips">' + ''.join(f'<span class="chip">{c}</span>' for c in chips) + '</div>\n'
    prev = f'<a href="{ORDER[i-1]}.html">← {NAMES[ORDER[i-1]]}</a>' if i else '<a href="../index.html#professional">← All work</a>'
    nxt = f'<a href="{ORDER[i+1]}.html">{NAMES[ORDER[i+1]]} →</a>' if i < len(ORDER)-1 else '<a href="../index.html#personal">All work →</a>'
    s += f'<div class="next"><span>{prev}</span><span>{nxt}</span></div></main>\n'
    s += foot()
    open(os.path.join(OUT, "cases", slug + ".html"), "w").write(s)

# ---------- landing page ----------
CARD = {
 "sentinel": "Many market trackers merged into one ranked view of which accounts to approach now. Runs across the EU, the GCC, India and the US.",
 "account-intelligence": "1,000+ existing client accounts turned into sourced facts and a pipeline of upsell opportunities, without paying a model to read everything.",
 "outbound": "Admission, ranking, research, drafting and gating, orchestrated across agents, with a person approving every send.",
 "audit-loop": "Agents propose, a person challenges, every verdict is recorded, and the system is audited and improved monthly.",
 "grantscope": "Nine Spanish and EU grant programmes matched into one deeptech account database, refreshed monthly in about 12 minutes.",
 "nse-pulse": "Daily exchange data, documents parsed the moment they are published, a highlights dashboard and backtests that can't flatter themselves.",
 "ledgerlens": "Years of my own trades rebuilt into a ledger of decisions, with behaviour tags, trader personas and exit replays.",
 "chief-of-staff": "A portable profile, built from my own work history, that lets any AI model work like a chief of staff from message one.",
 "token-economics": "A 480-session usage study, a token-diet playbook (~155k → ~11k tokens), model routing and the tooling to run agents daily.",
}
def cards(slugs):
    return '<div class="cards">' + ''.join(
        f'<a class="card" href="cases/{s}.html"><div class="k">{CASES[s][0].split("· ")[1]}</div><h3>{NAMES[s] if s != "chief-of-staff" else "AI chief of staff"}</h3><p>{CARD[s]}</p><span class="go">read case →</span></a>'
        for s in slugs) + '</div>'

idx = head("Lakshay Garg — AI for founders", "I help founders set up AI in their business. First I look at how you work. Then I build the tools that save you time.", "", "home")
idx += f'''<header class="hero">
  <div class="mono prompt">$ whoami → founder · engineer · AI builder</div>
  <h1>I help founders set up <em>AI that saves them time</em>.</h1>
  <p class="lede">I founded and ran a chemicals business, then worked in the offices of CEOs and ministers. Now I build AI tools for founders. I start with how you work, then build what saves you time. You keep the decisions.</p>
  <div class="cta"><a class="btn primary" href="#professional">see the work</a><a class="btn" href="{LI}">LinkedIn ↗</a><a class="btn" href="mailto:{MAIL}">email</a></div>
  <div class="path">
    <div><span>2012</span><b>Process engineering</b></div>
    <div><span>2014</span><b>Founded a chemicals venture</b></div>
    <div><span>2018</span><b>M&amp;A and IPO advisory, Berlin</b></div>
    <div><span>2021</span><b>Minister's office, Govt. of India</b></div>
    <div><span>2022</span><b>Chief of Staff, Global CEO office</b></div>
    <div class="now"><span>Now</span><b>AI tools for founders</b></div>
  </div>
</header>

<section class="how">
  <div class="sec-head"><span class="mono">// how my GTM systems work</span><h2>Machines do the volume. People make the calls.</h2></div>
  {pipe([("signals","Filings, tenders, deals and news collected",0),("score","Accounts ranked by who matters now",0),("research","Agents build a packet per account",0),("challenge","An analyst tests the agent's research",1),("approve","I decide and send",1)])}
</section>

<section id="professional">
  <div class="sec-head"><span class="mono">// professional</span><h2>GTM systems in production</h2><p>Built for a US-headquartered advisory firm, across the EU, the GCC, India and the US.</p></div>
  {cards(ORDER[:5])}
</section>

<section id="personal">
  <div class="sec-head"><span class="mono">// personal</span><h2>Things I build for myself</h2><p>Same habits, my own money and time: market research, self-measurement and the economics of running AI.</p></div>
  {cards(ORDER[5:])}
</section>

<section id="approach">
  <div class="sec-head"><span class="mono">// approach</span><h2>How I build</h2></div>
  <div class="grid4">
    <div><h4>Process before tool</h4><p>Map the flow, the controls and the failure points first, then pick the stack.</p></div>
    <div><h4>Humans own the judgment</h4><p>Agents research and draft. People challenge, decide and own the relationship.</p></div>
    <div><h4>Every loop closes</h4><p>Outcomes feed back into rules, and audits change the system itself.</p></div>
    <div><h4>Decisions in writing</h4><p>One decision record is the final word, so anyone can pick the system up.</p></div>
  </div>
</section>

<section>
  <div class="sec-head"><span class="mono">// stack</span></div>
  <div class="chips">{''.join(f'<span class="chip">{c}</span>' for c in ["Claude Code &amp; agents","MCP connectors","Python","DuckDB / SQL","APIs &amp; data pipelines","Local models","CRM workflows","Streamlit / Dash","JavaScript","Git"])}</div>
</section>
'''
idx += foot()
open(os.path.join(OUT, "index.html"), "w").write(idx)
print("built", len(ORDER), "cases")
