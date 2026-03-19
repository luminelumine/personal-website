# Lessons Learned

## Patterns to Follow

### Tone Alignment
- **Pattern**: Match requested audience voice before finalizing structure.
- **Why**: Tone mismatch causes major rewrites even if facts are correct.
- **Example**: Public-facing investigation should prioritize direct narrative and clear claims over academic sectioning language.

## Mistakes to Avoid

### 2026-03-11 - Over-academic Framing on First Draft
- **What happened**: The first revision used a research-paper style with legal hedging language.
- **Root cause**: Defaulted to formal analytical template rather than explicit audience tone in user intent.
- **Prevention rule**: For article rewrites, lock audience and stance first (public narrative vs. academic vs. legal-risk-neutral) before writing headings and conclusion language.

### 2026-03-12 - Publication Date Metadata Mismatch
- **What happened**: A newly published article used a default recent date instead of the user-intended historical publication date.
- **Root cause**: Date metadata was not explicitly confirmed against the source memo timeline before publishing.
- **Prevention rule**: Before syncing writings, verify subtitle/meta date in article HTML matches the user-specified publication month/year.

### 2026-03-12 - Direct Copy Edit Must Be Literal
- **What happened**: User requested exact title and full section removal after publication adjustments.
- **Root cause**: Publication iteration introduced extra review loops instead of immediate literal application.
- **Prevention rule**: When user provides exact replacement text and explicit deletion scope, apply it verbatim and re-sync index pages in the same step.

### 2026-03-14 - Timepoint Integrity in Research Conclusions
- **What happened**: Conclusion draft mixed post-2022 realized market outcomes into a section that should be written strictly from a 2022 perspective.
- **Root cause**: Applied current-state evidence style without preserving the requested historical viewpoint constraint.
- **Prevention rule**: When user asks for a viewpoint anchored to a specific year, avoid any hindsight facts after that year and use conditional forward-looking language only.

### 2026-03-14 - Draft Positioning and Audience Scope Must Be Explicit
- **What happened**: Initial draft framing still reflected source-format context and mixed language expectations.
- **Root cause**: Did not fully enforce the requested delivery constraints (English-only, research voice, beginner-friendly mechanism explanation, and screenshot curation) across all sections.
- **Prevention rule**: For research rewrites, lock four constraints before drafting: publication voice (research), language (single target language), audience baseline knowledge, and visual inclusion threshold (only evidence-bearing figures).

### 2026-03-14 - Preserve Core Investment Thesis and Numeric Examples
- **What happened**: The first English rewrite omitted two core analytical anchors: Fluid's ultra-low fee thesis and the canonical debt-recomposition swap example.
- **Root cause**: Over-compression during editorial cleanup removed high-signal mechanism details from the source.
- **Prevention rule**: Before delivering a rewrite, verify that all user-flagged key claims, numeric values, and worked examples are explicitly retained in the final draft.

### 2026-03-14 - Honor Explicit Section Deletion Requests Without Substitutes
- **What happened**: A user-requested section removal required an immediate structural edit before publication.
- **Root cause**: Draft flow initially preserved broader analysis sections that the user wanted removed.
- **Prevention rule**: When a section is explicitly marked for deletion, remove the full block and immediately revalidate numbering/labels before publishing.
