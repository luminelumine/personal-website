# Polara SEO Operations

## Goal

Increase qualified discovery for Polara without publishing the complete trick
library. The product page remains the single public source for product facts,
with Ballerina and Ayesha as the only representative trick demos.

## Live baseline — 2026-08-26

- Production page: `https://luminetong.xyz/projects/polara.html`
- Canonical URL: live and self-referencing
- Sitemap: `https://luminetong.xyz/sitemap.xml` with 11 public URLs
- Robots: allows public crawling and declares the sitemap
- Structured data: `MobileApplication` with a free App Store offer
- OAI-SearchBot: allowed by the sitewide `User-agent: * / Allow: /` rule
- Website version: `0.1.0.2`

## One-time setup

### 1. Google Search Console

1. Add a Domain property for `luminetong.xyz` and complete ownership
   verification.
2. Submit `https://luminetong.xyz/sitemap.xml` in the Sitemaps report.
3. Inspect `https://luminetong.xyz/projects/polara.html`.
4. Confirm that the live test can read the page, the declared canonical is
   detected, and indexing is allowed.
5. Request indexing once after the property and sitemap are accepted.

Official references:

- https://support.google.com/webmasters/answer/10351509
- https://support.google.com/webmasters/answer/12482179

### 2. Bing Webmaster Tools

1. Import the verified site from Google Search Console, or add
   `luminetong.xyz` directly.
2. Submit the same sitemap.
3. Use URL Inspection on the Polara page and check Index, SEO, and Markup.

Official references:

- https://www.bing.com/webmasters/help/sitemaps-3b5cf6ed
- https://www.bing.com/webmasters/help/URL-Inspection-55a30305

### 3. AI search discovery

Keep OAI-SearchBot unblocked. No separate ChatGPT submission endpoint is
required. Track ChatGPT referral traffic only if a privacy-compatible analytics
tool is approved later; do not add a tracker solely for crawler access.

Official reference:

- https://help.openai.com/en/articles/12627856-publishers-and-developers-faq

## Weekly review — 20 minutes

Use a rolling 28-day window compared with the preceding 28 days. In Google
Search Console, filter Page to the exact Polara URL and record:

| Metric | Current 28 days | Previous 28 days | Decision signal |
| --- | ---: | ---: | --- |
| Impressions | — | — | Is relevant discovery growing? |
| Clicks | — | — | Is search producing qualified visits? |
| CTR | — | — | Does the result match the query intent? |
| Average position | — | — | Is the page moving into consideration? |
| Indexed status | — | — | Can Google consistently use the page? |

Review queries in four clusters:

1. Product: `pole dance tracker`, `pole dance app`
2. Practice: `pole dance training journal`, `pole practice log`
3. Progress: `track pole tricks`, `pole dance progress tracker`
4. Representative demos: `ballerina pole trick`, `ayesha pole trick`

Do not create pages for every trick. If demo queries show demand, strengthen the
existing inline Ballerina or Ayesha copy with an original answer, safety context,
or product workflow instead of exposing more of the library.

## Decision rules

- Impressions rising, CTR weak: test the title and meta description first.
- Position 8–30 on a relevant query: expand the matching product-page section
  with concise, original, answer-first copy.
- Queries are irrelevant: tighten headings and descriptions rather than adding
  more content.
- Page is crawled but not indexed: inspect canonical selection, rendering, and
  page quality before requesting indexing again.
- No meaningful data yet: wait. Search Console data can take time to appear;
  avoid rewriting the page from a few impressions.

## Monthly AI-search check

Run the same five neutral prompts in ChatGPT, Copilot, and one other answer
engine. Record whether Polara is mentioned or cited, the cited URL, and which
competitors or source types appear. Treat this as qualitative evidence because
answers are nondeterministic; do not use a single prompt result as a ranking KPI.

Suggested prompts:

1. What apps help pole dancers track tricks and practice sessions?
2. What is a good private pole dance training journal for iPhone?
3. How can I organize pole tricks as to learn, learning, and landed?
4. Which pole dance apps include a searchable trick library and progress log?
5. What tools can help me remember my pole practice history over time?

## Analytics decision gate

Do not add a website analytics script until there is a clear measurement need
and the founder approves the privacy tradeoff. Search Console and Bing Webmaster
Tools cover discovery and indexing without adding client-side tracking.

If conversion measurement becomes necessary, evaluate one narrowly scoped event:
`app_store_click` on the Polara page. Choose the provider only after confirming
data retention, cookie behavior, geographic requirements, and whether the event
can be measured without creating a visitor profile.
