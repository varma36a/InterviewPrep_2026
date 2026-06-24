# .NET + Angular + Azure Interview Prep

Interactive **Streamlit** app for full-stack interview preparation — phase-wise Q&A with detailed explanations and code examples.

## Topics covered (622+ interview Q&A)

| Section | Topics | Highlights |
|---|---|---|
| **System Design (HLD)** | 40 | CAP, sharding, microservices + classic designs (URL shortener, Twitter, Uber, etc.) |
| **CS Fundamentals** | 40 | OS, TCP/IP, ACID, concurrency, OAuth, CI/CD, Big O |
| **Design Patterns** | 29 | **23 GoF + SOLID** — live C# loaded from `DesignPatternsLearnignFolder` |
| **DSA Coding** | 50 | **Top 50** LeetCode-style problems — arrays, trees, graphs, DP, backtracking (C#) |
| **Core .NET** | 50+ | Nullable types, records, LINQ, reflection, Parallel LINQ, primary constructors |
| **ASP.NET Core** | 50+ | Minimal APIs, HttpClientFactory, FluentValidation, Serilog, Polly, MediatR, Kestrel |
| **Angular & TypeScript** | 60+ | Signals, standalone, guards, FormArray, zoneless, SSR, interceptors, NgRx |
| **Database & EF Core** | 50+ | CTEs, deadlocks, EF relationships, split queries, temporal tables, Specification |
| **Microsoft Azure** | 50+ | VMs, Static Web Apps, WAF, Private Link, Durable Functions, Azure Policy, Sentinel |
| **Best Practices** | 50+ | Clean Architecture, Saga, Outbox, design patterns, Hexagonal, Strangler Fig |
| **Docker & DevOps** | 50+ | K8s StatefulSet, ArgoCD, Istio, GitOps, Helm, Trivy, MassTransit |
| **LINQ Queries** | 53 | 40 Q&A + **13 runnable** scenarios from `Linq/LinqPractice` project |
| **HTML & CSS** | 50+ | CSS position, :has(), subgrid, dialog, transforms, SEO meta, aspect-ratio |

## New features

- **Search & Filter** — keyword search across all topics
- **Section filter** — e.g. only Azure or only Docker
- **Phase filter** — Foundation / Intermediate / Advanced
- **Quick search buttons** — JWT, Docker, RxJS, Terraform, etc.
- **Sidebar search** — jump to Search page from anywhere

Each topic includes:
- Interview question
- **Detailed explanation** (what, why, how, when, pitfalls)
- Key points checklist
- **Expanded code example** with comments (C#, TypeScript, SQL, YAML, Bash)

## Setup

```bash
cd NetAngularAzureInterviewPrep
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

Opens at `http://localhost:8501`.

## App pages

- **Home** — overview and career level guide
- **Search & Filter** — keyword + section + phase filters
- **Roadmap** — all questions listed by section/phase
- **Mock Interview** — full-stack login flow walkthrough
- **13 sections** — each with topic-wise phase tabs

## Project structure

```
NetAngularAzureInterviewPrep/
├── app.py
├── data/
│   ├── interview_content.py      # Core Q&A catalog
│   ├── extra_content.py          # Docker, Terraform, HTML/CSS extras
│   ├── detailed_content.py       # Merges enhanced explanations
│   ├── detailed_content_part1.py # .NET + ASP.NET detailed content
│   ├── detailed_content_part2.py # Frontend + DB + practices
│   ├── detailed_content_part3.py # Azure + Docker + HTML/CSS
│   ├── design_patterns_section.py  # GoF + SOLID (loads C# from sibling folder)
│   ├── design_patterns_loader.py   # Reads DesignPatternsLearnignFolder sources
│   ├── linq_loader.py            # Reads Linq/LinqPractice C# sources
│   ├── linq_project_topics.py    # Runnable scenario topics
│   ├── linq_section.py           # Dedicated LINQ section (40+ questions)
│   ├── dsa_section.py            # DSA coding section (50 questions)
│   ├── hld_section.py            # System design HLD (40 questions)
│   ├── cs_fundamentals_section.py # CS fundamentals (40 questions)
│   ├── market_dotnet_extra.py    # +20 .NET topics
│   ├── market_aspnet_extra.py    # +20 ASP.NET topics
│   ├── market_database_extra.py  # +20 Database topics
│   ├── market_azure_extra.py     # +20 Azure topics
│   ├── market_practices_extra.py # +19 Best Practices topics
│   ├── market_devops_extra.py    # +20 DevOps topics
│   ├── market_htmlcss_extra.py   # +20 HTML/CSS topics
│   └── market_topics.py          # Merges all market content
├── ../Linq/LinqPractice/           # Runnable LINQ interview console app
├── ../DesignPatternsLearnignFolder/  # Runnable GoF + SOLID pattern demos
├── requirements.txt
└── README.md
```
